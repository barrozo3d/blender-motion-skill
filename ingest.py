"""
ingest.py — Data collection for blender-motion skill (Step 1 of 2)

NO API CALLS. Collects everything and saves to disk for Claude Code extraction.

Pipeline:
  1. yt-dlp metadata + chapter parsing
  2. Whisper transcription (falls back to yt-dlp captions)
  3. Transcript segmented by chapters
  4. Low-quality video download + ffmpeg frame extraction at chapter boundaries
  5. Save raw .md to tutorials/<slug>.md
  6. Save frames to tutorials/frames/<slug>/ (local only, not committed to git)
  7. Update INDEX.md with pending stub
  8. git commit + push (raw .md + INDEX only)

Claude Code reads the saved file + frames and runs the extraction pass (Step 2).
The path of the saved file is printed at the end — Claude uses that to start extraction.

Usage:
  python ingest.py <youtube-url>
  python ingest.py <youtube-url> --whisper-model small
  python ingest.py <youtube-url> --skip-video   (no frames, text-only extraction)
  python ingest.py <article-url>
"""

import sys, os, re, json, subprocess, tempfile, shutil, argparse
from datetime import datetime
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────────────

SKILL_DIR     = Path(__file__).parent
TUTORIALS_DIR = SKILL_DIR / "tutorials"
FRAMES_DIR    = TUTORIALS_DIR / "frames"
INDEX_FILE    = TUTORIALS_DIR / "INDEX.md"
DEFAULT_WHISPER = "base"

# ── Utilities ─────────────────────────────────────────────────────────────────

def slugify(text):
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    return s.strip("-")[:80]

def _ytdlp_cmd():
    """Return yt-dlp invocation, using cookies.txt if present for YouTube bot bypass.

    YouTube bot detection requires authentication. To fix 429/sign-in errors:
    1. Install browser extension: 'Get cookies.txt LOCALLY' (Chrome/Edge/Firefox)
    2. Go to youtube.com while logged in
    3. Click the extension -> Export -> save as cookies.txt in this skill directory
    4. Re-run ingest.py — it will pick up cookies.txt automatically
    """
    base = ["yt-dlp"] if shutil.which("yt-dlp") else [sys.executable, "-m", "yt_dlp"]
    cookies_file = SKILL_DIR / "cookies.txt"
    if cookies_file.exists():
        return base + ["--cookies", str(cookies_file), "--remote-components", "ejs:github"]
    return base

def _get_api_key():
    """Not needed for collection — kept so check_prerequisites stays simple."""
    return True

def check_prerequisites():
    missing = []
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "--version"],
                       capture_output=True)
    if r.returncode != 0:
        missing.append("yt-dlp (pip install yt-dlp)")
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

def extract_frames(video_path, timestamps, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    frames = []
    for i, ts in enumerate(timestamps):
        dst = out_dir / f"frame_{i:03d}.jpg"
        subprocess.run(
            ["ffmpeg", "-ss", str(max(ts, 0)), "-i", str(video_path),
             "-frames:v", "1", "-q:v", "2", str(dst), "-y"],
            capture_output=True
        )
        if dst.exists():
            frames.append(dst)
    return frames

# ── Ingest safeguards ─────────────────────────────────────────────────────────

_STOP_WORDS = {
    'the','a','an','and','or','in','of','to','is','it','i','we','you','this',
    'that','for','are','on','at','be','by','with','have','was','as','from',
    'so','if','but','not','do','my','me','he','she','they','up','out','just',
    'can','all','now','will','our','when','their','what','about','here','one',
    'been','some','get','which','there','has','had','his','her','its','them',
    'then','than','also','into','more','would','could','should','very','like',
}

def _detect_hallucination(text):
    """Content word repeated >= 8x in last 50 words → probable ASR loop."""
    import collections
    lines = [l for l in text.splitlines()
             if not re.search(r'frame_\d+\.(jpg|png)|tutorials[/\\]frames', l, re.I)]
    words = re.findall(r'\b[a-z]+\b', ' '.join(lines).lower())
    if not words:
        return False, '', 0
    tail = [w for w in words[-50:] if w not in _STOP_WORDS]
    if not tail:
        return False, '', 0
    top_word, top_count = collections.Counter(tail).most_common(1)[0]
    return top_count >= 8, top_word, top_count

def run_safeguards(ch_transcripts, frame_paths, expected_frames, has_video):
    """
    Run all ingest quality checks.
    Returns (warnings, critical) — critical items mark extraction_status: needs-review.
    """
    warnings, critical = [], []
    total_chars = sum(len(ch.get('text', '')) for ch in ch_transcripts)

    # 1. Chapter transcript coverage
    for ch in ch_transcripts:
        text = ch.get('text', '').strip()
        name = ch.get('title', '?')
        if not text:
            critical.append(f"Empty transcript in chapter '{name}'")
        elif len(text) < 50:
            warnings.append(f"Very short transcript ({len(text)} chars) in '{name}'")

    # 2. Total transcript completeness
    if total_chars < 500:
        critical.append(
            f"Total transcript only {total_chars} chars (min 500). "
            "Captions unavailable or audio silent — extraction will be poor."
        )
    elif total_chars < 1200:
        warnings.append(
            f"Thin transcript: {total_chars} chars. "
            "Notes may be shallow — consider --whisper-model small."
        )

    # 3. ASR hallucination detection (per chapter)
    for ch in ch_transcripts:
        text = ch.get('text', '')
        if len(text) > 200:
            hallu, word, count = _detect_hallucination(text)
            if hallu:
                critical.append(
                    f"ASR hallucination in '{ch.get('title', '?')}': "
                    f"'{word}' x{count} in last 50 content words. "
                    "Review and truncate the affected section before extracting."
                )

    # 4. Frame count validation
    if has_video and expected_frames > 0:
        got = len(frame_paths)
        if got == 0:
            critical.append(
                f"Frame extraction produced 0/{expected_frames} frames. "
                "Check that ffmpeg is in PATH and the video downloaded successfully."
            )
        elif got < expected_frames:
            warnings.append(f"Partial frames: {got}/{expected_frames} captured.")

    return warnings, critical

def _print_safeguard_report(warnings, critical):
    if not warnings and not critical:
        print("[SAFEGUARD] All checks passed")
        return
    print("[SAFEGUARD] Quality issues found:")
    for w in warnings:
        print(f"      WARNING  : {w}")
    for c in critical:
        print(f"      CRITICAL : {c}")
    if critical:
        print("      => extraction_status set to 'needs-review'")

# ── Build raw .md ──────────────────────────────────────────────────────────────

def build_raw_md(info, ch_transcripts, frame_paths, slug):
    title    = info.get("title", "Unknown")
    url      = info.get("webpage_url", "")
    author   = info.get("uploader", "Unknown")
    today    = datetime.now().strftime("%Y-%m-%d")
    duration = info.get("duration", 0)
    dur_str  = f"{int(duration)//60}m{int(duration)%60}s" if duration else "unknown"
    n_frames = len(frame_paths)

    # Chapter breakdown with transcript excerpts + frame paths
    chapters_section = ""
    for i, ch in enumerate(ch_transcripts):
        t_fmt = f"{int(ch.get('start',0))//60}:{int(ch.get('start',0))%60:02d}"
        chapters_section += f"\n### {ch['title']} [{t_fmt}]\n"
        if ch["text"]:
            chapters_section += f"**Transcript:** {ch['text']}\n\n"
        if i < len(frame_paths):
            # Path relative to skill root for Claude's Read tool
            rel = frame_paths[i].relative_to(SKILL_DIR)
            chapters_section += f"**Frame:** {rel}\n"

    return f"""---
title: {title}
source: YouTube
url: {url}
author: {author}
ingested: {today}
blender_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/{slug}/
frame_count: {n_frames}
---

# {title}

**Source:** [YouTube]({url})
**Author:** {author}
**Duration:** {dur_str} | {len(ch_transcripts)} section(s)

---

## Raw Data (for Claude Code extraction)

{chapters_section}

---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Blender Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
"""

def update_index_pending(info, slug, filename):
    title  = info.get("title", "Unknown")
    url    = info.get("webpage_url", "")
    author = info.get("uploader", "Unknown")

    entry = f"""

### {title}
- **Source:** YouTube
- **URL:** {url}
- **Author:** {author}
- **Blender Version:** [PENDING]
- **Tags:** [PENDING]
- **Summary:** [PENDING EXTRACTION]
- **File:** tutorials/{filename}
"""
    content = INDEX_FILE.read_text(encoding="utf-8")
    if f"tutorials/{filename}" in content or (url and url in content):
        print(f"      INDEX.md already has an entry for {filename} — skipping (re-ingest will refresh the .md file but not duplicate the index)")
        return
    placeholder = "*(Empty — add your first tutorial by saying"
    if placeholder in content:
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
            "webpage_url": url, "chapters": []}

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Blender tutorial data collection (Step 1 of 2)")
    parser.add_argument("url")
    parser.add_argument("--whisper-model", default=DEFAULT_WHISPER,
                        choices=["tiny", "base", "small", "medium", "large"])
    parser.add_argument("--skip-video", action="store_true",
                        help="Skip video download and frame extraction")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite an existing tutorial file even if extraction_status: complete")
    args = parser.parse_args()

    has_ffmpeg, has_whisper = check_prerequisites()
    is_yt = "youtube.com" in args.url or "youtu.be" in args.url
    tmp = Path(tempfile.mkdtemp())

    try:
        # 1. Metadata
        print("[1/6] Fetching metadata...")
        if is_yt:
            info = get_info(args.url)
        else:
            info = fetch_article(args.url)

        title    = info.get("title", "Unknown")
        chapters = info.get("chapters") or []
        duration = info.get("duration", 0)
        print(f"      {title}")
        print(f"      {len(chapters)} chapter(s), {int(duration//60)}m{int(duration)%60}s")

        slug   = slugify(title)
        out_md = TUTORIALS_DIR / f"{slug}.md"
        frames_out = FRAMES_DIR / slug

        if out_md.exists() and not args.force:
            existing = out_md.read_text(encoding="utf-8")
            if "extraction_status: complete" in existing:
                print(f"      {out_md.name} is already fully extracted — refusing to overwrite.")
                print(f"      Pass --force to re-collect anyway (this will wipe the existing Structured Notes).")
                return

        # 2. Transcript
        ch_transcripts = []
        if is_yt:
            if has_whisper:
                print(f"[2/6] Downloading audio + transcribing with Whisper ({args.whisper_model})...")
                try:
                    audio = download_audio(args.url, tmp)
                    transcript = whisper_transcribe(audio, args.whisper_model)
                    ch_transcripts = segment_by_chapters(transcript, chapters)
                    print(f"      {len(transcript.get('segments',[]))} segments -> {len(ch_transcripts)} sections")
                except Exception as e:
                    print(f"      Whisper failed ({e}), using yt-dlp captions")
                    text = ytdlp_captions(args.url, tmp)
                    ch_transcripts = [{"title": "Full Content", "start": 0, "text": text}]
            else:
                print("[2/6] Whisper not installed - using yt-dlp captions (pip install openai-whisper for better results)")
                text = ytdlp_captions(args.url, tmp)
                ch_transcripts = [{"title": "Full Content", "start": 0, "text": text}]
        else:
            print("[2/6] Article - using page text")
            ch_transcripts = [{"title": "Full Content", "start": 0,
                               "text": info.get("description", "")}]

        # 3+4. Video + frames
        frame_paths = []
        expected_frames = 0
        video_attempted = is_yt and not args.skip_video and has_ffmpeg
        if video_attempted:
            if chapters:
                timestamps = [ch.get("start_time", 0) + 5 for ch in chapters]
            elif duration:
                timestamps = [duration * p for p in [0.1, 0.3, 0.55, 0.8]]
            else:
                timestamps = [30, 120, 300]
            expected_frames = len(timestamps)
            print("[3/6] Downloading video (lowest quality)...")
            try:
                video = download_video_low(args.url, tmp)
                print(f"[4/6] Extracting {expected_frames} frame(s) to {frames_out.relative_to(SKILL_DIR)}...")
                frame_paths = extract_frames(video, timestamps, frames_out)
                print(f"      {len(frame_paths)} frame(s) saved")
            except Exception as e:
                print(f"      Frame extraction failed ({e}), continuing without frames")
        else:
            reason = "article" if not is_yt else ("--skip-video" if args.skip_video else "ffmpeg not found")
            print(f"[3/6] Skipping video download ({reason})")
            print("[4/6] Skipping frame extraction")

        # Safeguard checks
        sg_warnings, sg_critical = run_safeguards(
            ch_transcripts, frame_paths, expected_frames, video_attempted
        )
        _print_safeguard_report(sg_warnings, sg_critical)

        # 5. Write raw .md
        print("[5/6] Writing raw tutorial file...")
        md = build_raw_md(info, ch_transcripts, frame_paths, slug)
        if sg_critical:
            md = md.replace("extraction_status: pending", "extraction_status: needs-review", 1)
        out_md.write_text(md, encoding="utf-8")
        update_index_pending(info, slug, out_md.name)

        # 6. Git commit + push (raw .md + INDEX only, not frames)
        print("[6/6] Committing raw data to GitHub...")
        os.chdir(SKILL_DIR)
        subprocess.run(["git", "add", str(out_md.relative_to(SKILL_DIR)),
                        str(INDEX_FILE.relative_to(SKILL_DIR))], check=True)
        subprocess.run(["git", "commit", "-m", f"collect: {title}"], check=True)
        subprocess.run(["git", "push"], check=True)

        # Summary for Claude Code
        print(f"\n{'='*60}")
        print(f"  Collection complete. Claude Code: run extraction now.")
        print(f"  Tutorial file: tutorials/{out_md.name}")
        if frame_paths:
            print(f"  Frames:        tutorials/frames/{slug}/ ({len(frame_paths)} frames)")
        else:
            print(f"  Frames:        none (text-only extraction)")
        print(f"{'='*60}\n")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    main()
