"""
ingest.py — Enhanced tutorial ingestion for blender-motion skill

Pipeline:
  1. yt-dlp metadata + chapter parsing
  2. Whisper transcription (falls back to yt-dlp captions)
  3. Transcript segmented by chapters
  4. Low-quality video download → ffmpeg frame extraction at chapter boundaries
  5. Claude vision analysis per frame (reads node graphs, settings, viewport)
  6. Multi-pass Claude extraction (Pass 1+2: steps/nodes; Pass 3: tags)
  7. Auto cross-linking against existing library (2+ shared tags)
  8. Write tutorial .md + update INDEX.md + backlink existing files
  9. git commit + push

Requirements:
  pip install yt-dlp openai-whisper anthropic
  ffmpeg must be on PATH  →  https://ffmpeg.org/download.html
  ANTHROPIC_API_KEY must be set in environment

Usage:
  python ingest.py <youtube-url>
  python ingest.py <youtube-url> --whisper-model small
  python ingest.py <youtube-url> --skip-video   (transcript + API only, no frames)
  python ingest.py <article-url>
"""

import sys, os, re, json, subprocess, tempfile, shutil, base64, argparse
from datetime import datetime
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────────────

SKILL_DIR     = Path(__file__).parent
TUTORIALS_DIR = SKILL_DIR / "tutorials"
INDEX_FILE    = TUTORIALS_DIR / "INDEX.md"

VISION_MODEL     = "claude-opus-4-7"
EXTRACTION_MODEL = "claude-opus-4-7"
TAGGING_MODEL    = "claude-sonnet-4-6"
DEFAULT_WHISPER  = "base"   # tiny / base / small / medium / large

TAGS_POOL = [
    "geometry-nodes", "simulation", "particles", "fluid", "rigid-body", "cloth",
    "smoke-fire", "materials", "shaders", "procedural", "displacement",
    "animation", "rigging", "camera", "compositing", "rendering", "cycles",
    "eevee", "lighting", "hdri", "volume", "product-viz", "motion-design",
    "abstract", "logo-animation", "typography", "glass", "metal", "organic",
    "brand-video", "beginner", "intermediate", "advanced", "expert",
    "blender-3x", "blender-4x", "blender-5x",
]

VISION_PROMPT = """This is a frame from a Blender tutorial (chapter: "{chapter}").

Identify exactly what is visible:
1. Which editor is shown? (Node Editor: Geometry Nodes / Shader Editor / Compositor / Animation Nodes; 3D Viewport; Properties panel; Graph Editor; Timeline; UV Editor; Outliner)
2. List every visible node name exactly as labeled in any Node Editor
3. Visible parameter values, slider positions, or settings panels — quote the numbers
4. What geometry, material, or effect is displayed in the 3D Viewport
5. Any on-screen text, annotations, or labels

Be precise and technical. Exact node names and numeric values matter for the knowledge base."""

# ── Utilities ─────────────────────────────────────────────────────────────────

def slugify(text):
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    return s.strip("-")[:80]

def b64_image(path):
    return base64.standard_b64encode(Path(path).read_bytes()).decode()

def extract_json(text):
    """Parse JSON from Claude response, handling markdown fences."""
    try:
        return json.loads(text)
    except Exception:
        pass
    for pat in [r"```json\s*(\{.*?\})\s*```", r"```\s*(\{.*?\})\s*```", r"(\{[^{}]*\})"]:
        m = re.search(pat, text, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(1))
            except Exception:
                continue
    return {}

def _get_api_key():
    """Return ANTHROPIC_API_KEY from env, Windows registry, or Claude Code credentials."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        return key
    # Windows user environment (set via setx or PowerShell SetEnvironmentVariable)
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
            value, _ = winreg.QueryValueEx(k, "ANTHROPIC_API_KEY")
            if value:
                os.environ["ANTHROPIC_API_KEY"] = value
                return value
    except Exception:
        pass
    # Claude Code OAuth token (~/.claude/.credentials.json)
    try:
        creds = Path.home() / ".claude" / ".credentials.json"
        if creds.exists():
            import json as _json
            data = _json.loads(creds.read_text(encoding="utf-8"))
            token = data.get("claudeAiOauth", {}).get("accessToken", "")
            if token:
                os.environ["ANTHROPIC_API_KEY"] = token
                return token
    except Exception:
        pass
    return None

def _ytdlp_cmd():
    """Return the yt-dlp invocation that works regardless of PATH."""
    if shutil.which("yt-dlp"):
        return ["yt-dlp"]
    return [sys.executable, "-m", "yt_dlp"]

def check_prerequisites():
    missing = []
    # Check yt-dlp as module (more reliable than PATH check)
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "--version"],
                       capture_output=True)
    if r.returncode != 0:
        missing.append("yt-dlp (pip install yt-dlp)")
    try:
        import anthropic
    except ImportError:
        missing.append("anthropic (pip install anthropic)")
    if not _get_api_key():
        missing.append("ANTHROPIC_API_KEY environment variable")
    if missing:
        print("Missing prerequisites:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)

    has_ffmpeg  = bool(shutil.which("ffmpeg"))
    has_whisper = False
    try:
        import whisper
        has_whisper = True
    except ImportError:
        pass

    return has_ffmpeg, has_whisper

# ── Step 1: Metadata ───────────────────────────────────────────────────────────

def get_info(url):
    r = subprocess.run(
        _ytdlp_cmd() + ["--dump-json", "--no-playlist", url],
        capture_output=True, text=True, timeout=60, check=True
    )
    return json.loads(r.stdout)

# ── Step 2: Transcript ─────────────────────────────────────────────────────────

def whisper_transcribe(audio_path, model_name):
    import whisper
    model = whisper.load_model(model_name)
    return model.transcribe(str(audio_path))

def download_audio(url, tmp):
    out = str(tmp / "audio.%(ext)s")
    subprocess.run(
        _ytdlp_cmd() + ["-x", "--audio-format", "mp3", "--audio-quality", "0",
         "--no-playlist", "-o", out, url],
        capture_output=True, timeout=300, check=True
    )
    for f in tmp.iterdir():
        if f.suffix in (".mp3", ".m4a", ".ogg", ".webm"):
            return f
    raise FileNotFoundError("Audio file not found after download")

def ytdlp_captions(url, tmp):
    """Fallback: yt-dlp auto-captions → plain text."""
    subprocess.run(
        _ytdlp_cmd() + ["--write-auto-subs", "--sub-lang", "en",
         "--sub-format", "vtt", "--skip-download", "--no-playlist",
         "-o", str(tmp / "%(id)s"), url],
        capture_output=True, timeout=120
    )
    for f in tmp.glob("*.vtt"):
        raw = f.read_text(encoding="utf-8", errors="ignore")
        lines = []
        for line in raw.splitlines():
            if "-->" in line or line.startswith("WEBVTT") or line.strip().isdigit():
                continue
            clean = re.sub(r"<[^>]+>", "", line).strip()
            if clean and (not lines or clean != lines[-1]):
                lines.append(clean)
        f.unlink()
        return " ".join(lines)
    return ""

def segment_by_chapters(transcript, chapters):
    """Split whisper segment list by chapter boundaries."""
    segs = transcript.get("segments", [])
    if not chapters:
        return [{"title": "Full Content", "start": 0,
                 "text": transcript.get("text", "").strip()}]
    result = []
    for i, ch in enumerate(chapters):
        t0 = ch.get("start_time", 0)
        t1 = chapters[i+1].get("start_time", float("inf")) if i+1 < len(chapters) else float("inf")
        text = " ".join(s["text"] for s in segs if t0 <= s.get("start", 0) < t1).strip()
        result.append({"title": ch.get("title", f"Chapter {i+1}"), "start": t0, "text": text})
    return result

# ── Step 3: Frame extraction ───────────────────────────────────────────────────

def download_video_low(url, tmp):
    out = str(tmp / "video.%(ext)s")
    subprocess.run(
        _ytdlp_cmd() + ["-f", "worst[ext=mp4]/worst", "--no-playlist", "-o", out, url],
        capture_output=True, timeout=600, check=True
    )
    for f in tmp.iterdir():
        if f.suffix in (".mp4", ".webm", ".mkv"):
            return f
    raise FileNotFoundError("Video not found after download")

def extract_frames(video_path, timestamps, tmp):
    frames = []
    for i, ts in enumerate(timestamps):
        dst = tmp / f"frame_{i:03d}.jpg"
        r = subprocess.run(
            ["ffmpeg", "-ss", str(max(ts, 0)), "-i", str(video_path),
             "-frames:v", "1", "-q:v", "2", str(dst), "-y"],
            capture_output=True
        )
        if dst.exists():
            frames.append(dst)
    return frames

# ── Step 4: Vision analysis ────────────────────────────────────────────────────

def analyze_frames(frames, chapters, client):
    import time
    analyses = []
    for i, frame in enumerate(frames):
        chapter_title = chapters[i]["title"] if i < len(chapters) else f"Section {i+1}"
        prompt = VISION_PROMPT.format(chapter=chapter_title)
        for attempt in range(6):
            try:
                resp = client.messages.create(
                    model=VISION_MODEL,
                    max_tokens=800,
                    messages=[{"role": "user", "content": [
                        {"type": "image", "source": {
                            "type": "base64", "media_type": "image/jpeg",
                            "data": b64_image(frame)
                        }},
                        {"type": "text", "text": prompt}
                    ]}]
                )
                analyses.append({"chapter": chapter_title, "visual": resp.content[0].text})
                print(f"      Frame {i+1}/{len(frames)}: {chapter_title[:50]}")
                time.sleep(3)  # brief pause between frames to stay under rate limit
                break
            except Exception as e:
                if "429" in str(e) or "rate_limit" in str(e).lower():
                    wait = 60 * (attempt + 1)
                    print(f"      Rate limited on frame {i+1}, waiting {wait}s (attempt {attempt+1}/6)...")
                    time.sleep(wait)
                else:
                    raise
        else:
            print(f"      Frame {i+1} skipped after 6 rate-limit retries")
            analyses.append({"chapter": chapter_title, "visual": "Frame analysis skipped (rate limited)"})
    return analyses

# ── Step 5: Multi-pass extraction ──────────────────────────────────────────────

def build_context(info, ch_transcripts, frame_analyses):
    ctx = f"Title: {info.get('title', '')}\n"
    ctx += f"Author: {info.get('uploader', '')}\n"
    ctx += f"Description: {info.get('description', '')[:400]}\n\n"
    ctx += "=== Chapter-by-Chapter Content ===\n"
    for i, ch in enumerate(ch_transcripts):
        ctx += f"\n--- {ch['title']} [t={ch.get('start',0):.0f}s] ---\n"
        if ch["text"]:
            ctx += f"Transcript: {ch['text'][:900]}\n"
        if i < len(frame_analyses):
            ctx += f"Frame analysis: {frame_analyses[i]['visual']}\n"
    return ctx

def _api_call_with_retry(fn, max_attempts=6):
    import time
    for attempt in range(max_attempts):
        try:
            return fn()
        except Exception as e:
            if "429" in str(e) or "rate_limit" in str(e).lower():
                wait = 60 * (attempt + 1)
                print(f"      Rate limited, waiting {wait}s (attempt {attempt+1}/{max_attempts})...")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("Exceeded max retries due to rate limiting")

def pass_1_2(ctx, client):
    """Extract core technique, key steps, nodes/settings, summary."""
    prompt = f"""You are building a searchable Blender tutorial knowledge base.

{ctx}

Extract the following. Return ONLY valid JSON with no markdown wrapping:
{{
  "core_technique": "one sentence: the main Blender technique this tutorial teaches",
  "summary": "2-3 sentences describing what the viewer learns and the end result",
  "difficulty": "Beginner|Intermediate|Advanced|Expert",
  "version": "Blender version if explicitly mentioned, else Not specified",
  "key_steps": [
    "Step with exact Blender node name or menu path (5-10 steps)",
    "..."
  ],
  "nodes_and_settings": [
    "Node Name or setting → value",
    "..."
  ]
}}

key_steps must be specific enough for a viewer to reproduce — include exact node names, menu paths, and keyboard shortcuts visible in the transcript or frames."""

    return extract_json(_api_call_with_retry(
        lambda: client.messages.create(
            model=EXTRACTION_MODEL,
            max_tokens=3000,
            messages=[{"role": "user", "content": prompt}]
        )
    ).content[0].text)

def pass_3_tags(extraction, client):
    """Generate tags from the approved pool."""
    pool_str = ", ".join(TAGS_POOL)
    prompt = f"""Tag this Blender tutorial using ONLY tags from this list:
{pool_str}

Tutorial details:
Core technique: {extraction.get('core_technique', '')}
Summary: {extraction.get('summary', '')}
Key steps sample: {json.dumps(extraction.get('key_steps', [])[:5])}
Nodes sample: {json.dumps(extraction.get('nodes_and_settings', [])[:6])}

Return ONLY valid JSON: {{"tags": ["tag1", "tag2", ...]}}
Pick 5-10 tags. Always include one difficulty tag. Include version tags (blender-4x etc) only if version is known."""

    return extract_json(_api_call_with_retry(
        lambda: client.messages.create(
            model=TAGGING_MODEL,
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )
    ).content[0].text).get("tags", [])

# ── Step 6: Auto cross-linking ─────────────────────────────────────────────────

def find_related(tags, new_title):
    if not INDEX_FILE.exists():
        return []
    content = INDEX_FILE.read_text(encoding="utf-8")
    related = []
    for entry in re.split(r"\n(?=### )", content):
        m = re.match(r"### (.+)", entry)
        if not m:
            continue
        entry_title = m.group(1).strip()
        if entry_title == new_title:
            continue
        entry_tags = re.findall(r"#([\w-]+)", entry)
        overlap = list(set(tags) & set(entry_tags))
        if len(overlap) >= 2:
            fm = re.search(r"\*\*File:\*\* (tutorials/[\w.-]+\.md)", entry)
            related.append({
                "title": entry_title,
                "overlap": sorted(overlap),
                "file": fm.group(1) if fm else None
            })
    return sorted(related, key=lambda x: len(x["overlap"]), reverse=True)[:5]

def backlink_existing(new_title, new_filename, related):
    for rel in related:
        if not rel.get("file"):
            continue
        fp = SKILL_DIR / rel["file"]
        if not fp.exists():
            continue
        content = fp.read_text(encoding="utf-8")
        if new_title in content:
            continue
        link = f"- [{new_title}](./{new_filename})"
        if "## Related Tutorials" in content:
            content = content.replace("## Related Tutorials\n",
                                      f"## Related Tutorials\n{link}\n")
        else:
            content += f"\n\n## Related Tutorials\n{link}\n"
        fp.write_text(content, encoding="utf-8")

# ── Build output ───────────────────────────────────────────────────────────────

def build_md(info, extraction, tags, ch_transcripts, frame_analyses, related):
    title   = info.get("title", "Unknown")
    url     = info.get("webpage_url", "")
    author  = info.get("uploader", "Unknown")
    today   = datetime.now().strftime("%Y-%m-%d")
    version = extraction.get("version", "Not specified")
    duration = info.get("duration", 0)
    chapters_count = len(ch_transcripts)

    tags_str  = " ".join(f"#{t}" for t in tags)
    steps_str = "\n".join(f"{i+1}. {s}" for i, s in enumerate(extraction.get("key_steps", [])))
    nodes_str = "\n".join(f"- {n}" for n in extraction.get("nodes_and_settings", []))

    chapter_section = ""
    for i, ch in enumerate(ch_transcripts):
        t_fmt = f"{int(ch.get('start',0))//60}:{int(ch.get('start',0))%60:02d}"
        chapter_section += f"\n### {ch['title']} [{t_fmt}]\n"
        if ch["text"]:
            excerpt = ch["text"][:600]
            chapter_section += f"**Transcript:** {excerpt}{'...' if len(ch['text'])>600 else ''}\n\n"
        if i < len(frame_analyses):
            chapter_section += f"**Visual analysis:** {frame_analyses[i]['visual']}\n"

    cross_links = ""
    if related:
        cross_links = "\n## Related Tutorials\n"
        for r in related:
            shared = ", ".join(f"#{t}" for t in r["overlap"][:4])
            cross_links += f"- [{r['title']}](./{Path(r['file']).name}) — {shared}\n"

    dur_str = f"{int(duration)//60}m{int(duration)%60}s" if duration else "unknown"

    return f"""---
title: {title}
source: YouTube
url: {url}
author: {author}
ingested: {today}
blender_version: "{version}"
tags: {json.dumps(tags)}
---

# {title}

**Source:** [YouTube]({url})
**Author:** {author}
**Ingested:** {today}
**Duration:** {dur_str} | {chapters_count} section(s)

---

## Structured Notes

### Core Technique
{extraction.get('core_technique', '')}

### Summary
{extraction.get('summary', '')}

### Key Steps
{steps_str}

### Nodes / Settings
{nodes_str}

### Difficulty
{extraction.get('difficulty', 'Not specified')}

### Blender Version
{version}

### Tags
{tags_str}

---

## Chapter Breakdown
{chapter_section}
{cross_links}"""

def update_index(info, extraction, tags, filename):
    title   = info.get("title", "Unknown")
    url     = info.get("webpage_url", "")
    author  = info.get("uploader", "Unknown")
    version = extraction.get("version", "Not specified")
    summary = extraction.get("summary", "")
    tags_str = " ".join(f"#{t}" for t in tags)

    entry = f"""

### {title}
- **Source:** YouTube
- **URL:** {url}
- **Author:** {author}
- **Blender Version:** {version}
- **Tags:** {tags_str}
- **Summary:** {summary}
- **File:** tutorials/{filename}
"""
    content = INDEX_FILE.read_text(encoding="utf-8")
    placeholder = "*(Empty — add your first tutorial by saying"
    if placeholder in content:
        # Replace the entire placeholder line
        content = re.sub(r"\*\(Empty[^)]+\)\*", entry.strip(), content)
    elif "\n---\n\n## Tag Reference" in content:
        content = content.replace("\n---\n\n## Tag Reference",
                                  f"{entry}\n---\n\n## Tag Reference")
    else:
        idx = content.rfind("\n---")
        if idx != -1:
            content = content[:idx] + entry + content[idx:]
        else:
            content += entry

    INDEX_FILE.write_text(content, encoding="utf-8")

# ── Article ingestion (non-YouTube) ───────────────────────────────────────────

def fetch_article(url):
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL)
    html = re.sub(r"<[^>]+>", " ", html)
    html = re.sub(r"&[a-z]+;", " ", html)
    text = re.sub(r"\s+", " ", html).strip()
    tm = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    title = tm.group(1).strip() if tm else url
    from urllib.parse import urlparse
    return {"title": title, "uploader": urlparse(url).netloc,
            "description": text[:8000], "duration": 0,
            "webpage_url": url, "chapters": [], "_is_article": True}

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Enhanced Blender tutorial ingestion")
    parser.add_argument("url")
    parser.add_argument("--whisper-model", default=DEFAULT_WHISPER,
                        choices=["tiny","base","small","medium","large"])
    parser.add_argument("--skip-video", action="store_true",
                        help="Skip video download and frame extraction")
    args = parser.parse_args()

    has_ffmpeg, has_whisper = check_prerequisites()

    import anthropic
    client = anthropic.Anthropic()
    tmp = Path(tempfile.mkdtemp())

    is_yt = "youtube.com" in args.url or "youtu.be" in args.url

    try:
        # 1. Metadata
        print("[1/8] Fetching metadata...")
        if is_yt:
            info = get_info(args.url)
        else:
            info = fetch_article(args.url)

        title    = info.get("title", "Unknown")
        chapters = info.get("chapters") or []
        duration = info.get("duration", 0)
        print(f"      {title}")
        print(f"      {len(chapters)} chapter(s), {int(duration//60)}m{int(duration%60)}s")

        slug   = slugify(title)
        out_md = TUTORIALS_DIR / f"{slug}.md"

        # 2. Transcript
        ch_transcripts = []
        if is_yt:
            if has_whisper:
                print(f"[2/8] Downloading audio for Whisper ({args.whisper_model})...")
                try:
                    audio = download_audio(args.url, tmp)
                    print("      Transcribing...")
                    transcript = whisper_transcribe(audio, args.whisper_model)
                    ch_transcripts = segment_by_chapters(transcript, chapters)
                    print(f"      {len(transcript.get('segments',[]))} segments -> {len(ch_transcripts)} sections")
                except Exception as e:
                    print(f"      ⚠ Whisper failed ({e}), falling back to yt-dlp captions")
                    text = ytdlp_captions(args.url, tmp)
                    ch_transcripts = [{"title": "Full Content", "start": 0, "text": text}]
            else:
                print("[2/8] Whisper not installed — using yt-dlp captions (install openai-whisper for better results)")
                text = ytdlp_captions(args.url, tmp)
                ch_transcripts = [{"title": "Full Content", "start": 0, "text": text}]
        else:
            print("[2/8] Article — using page text as transcript")
            ch_transcripts = [{"title": "Full Content", "start": 0,
                               "text": info.get("description", "")}]

        # 3+4. Video download + frame extraction
        frames = []
        if is_yt and not args.skip_video and has_ffmpeg:
            print("[3/8] Downloading video (lowest quality for frame extraction)...")
            try:
                video = download_video_low(args.url, tmp)
                if chapters:
                    timestamps = [ch.get("start_time", 0) + 5 for ch in chapters]
                elif duration:
                    timestamps = [duration * p for p in [0.1, 0.3, 0.55, 0.8]]
                else:
                    timestamps = [30, 120, 300]
                print(f"[4/8] Extracting {len(timestamps)} frame(s)...")
                frames = extract_frames(video, timestamps, tmp)
                print(f"      {len(frames)} frame(s) extracted")
            except Exception as e:
                print(f"      ⚠ Frame extraction failed ({e}), continuing without frames")
        else:
            reason = "article" if not is_yt else ("--skip-video" if args.skip_video else "ffmpeg not found")
            print(f"[3/8] Skipping video download ({reason})")
            print("[4/8] Skipping frame extraction")

        # 5. Vision analysis
        if frames:
            print(f"[5/8] Running Claude vision analysis ({len(frames)} frames)...")
            frame_analyses = analyze_frames(frames, chapters or [{"title": "Overview"}], client)
        else:
            print("[5/8] Skipping vision analysis (no frames)")
            frame_analyses = []

        # 6. Multi-pass extraction
        print("[6/8] Building context + running multi-pass extraction...")
        ctx = build_context(info, ch_transcripts, frame_analyses)

        extraction = pass_1_2(ctx, client)
        print(f"      Core: {extraction.get('core_technique','')[:80]}")

        tags = pass_3_tags(extraction, client)
        print(f"      Tags: {' '.join('#'+t for t in tags)}")

        # 7. Cross-linking
        print("[7/8] Scanning library for related tutorials...")
        related = find_related(tags, title)
        print(f"      {len(related)} related tutorial(s) found")

        # 8. Write files
        print("[8/8] Writing tutorial and updating INDEX...")
        md = build_md(info, extraction, tags, ch_transcripts, frame_analyses, related)
        out_md.write_text(md, encoding="utf-8")
        update_index(info, extraction, tags, out_md.name)
        if related:
            backlink_existing(title, out_md.name, related)

        # 9. Git push
        os.chdir(SKILL_DIR)
        subprocess.run(["git", "add", "tutorials/"], check=True)
        subprocess.run(["git", "commit", "-m", f"ingest+extract: {title}"], check=True)
        subprocess.run(["git", "push"], check=True)

        print(f"\n✓ Done → tutorials/{out_md.name}")
        if related:
            print(f"  Cross-linked: {[r['title'][:40] for r in related]}")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    main()
