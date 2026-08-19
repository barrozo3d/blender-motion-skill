"""
ingest.py — Data collection for blender-motion skill (Step 1 of 2)

NO API CALLS. Collects everything and saves to disk for Claude Code extraction.

Pipeline (Step 1 — this script):
  1. yt-dlp metadata + chapter parsing
  2. Whisper transcription (falls back to yt-dlp captions), per-sentence
     timestamps preserved even inside chapters
  3. Transcript segmented by chapters (or one "Full Content" section)
  4. Save raw .md to tutorials/<slug>.md (frame_status: pending-selection)
  5. Update INDEX.md with pending stub
  6. git commit + push (raw .md + INDEX only)

No video is downloaded and no frames are extracted here — frame timestamps
need judgment (which moment actually shows the technique), not a blind
percentage split, so that's deferred to select_frames.py (Step 2), run by
Claude Code after reading the timestamped transcript. See select_frames.py's
docstring for that step. Frames land in tutorials/frames/<slug>/ (local only,
not committed to git) once selected.

Usage:
  python ingest.py <youtube-url>
  python ingest.py <youtube-url> --whisper-model small
  python ingest.py <youtube-url> --skip-video   (no frames ever, text-only extraction)
  python ingest.py <article-url>
"""

import sys, os, re, json, subprocess, tempfile, shutil, argparse
from datetime import datetime
from pathlib import Path

# Ensure stdout handles Unicode on Windows (cp1252 default breaks non-ASCII titles)
# and flushes per line — block-buffered prints otherwise arrive after subprocess
# (git/yt-dlp) output when both are captured, scrambling the step order in logs.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)

# ── Configuration ─────────────────────────────────────────────────────────────

SKILL_DIR     = Path(__file__).parent
TUTORIALS_DIR = SKILL_DIR / "tutorials"
FRAMES_DIR    = TUTORIALS_DIR / "frames"
INDEX_FILE    = TUTORIALS_DIR / "INDEX.md"
def _default_whisper_model():
    """small on GPU (better accuracy, still fast), base on CPU (speed matters more)."""
    try:
        import torch
        if torch.cuda.is_available():
            return "small"
    except Exception:
        pass
    return "base"

DEFAULT_WHISPER = _default_whisper_model()

# ── Utilities ─────────────────────────────────────────────────────────────────

def slugify(text):
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    return s.strip("-")[:80]

def _ytdlp_cmd():
    """Return yt-dlp invocation, using cookies.txt if present for YouTube bot bypass.

    Without cookies.txt, the 'android' player client is forced — as of 2026-08
    YouTube's default web_safari client started throwing HTTP 429 + "Sign in
    to confirm you're not a bot" on many (not all) videos. The android client
    sidesteps that check without needing authentication. It only exposes a
    single combined mp4 (no audio-only stream), which is fine here since
    download_audio() re-encodes whatever format it gets to mp3 anyway.

    If a video still fails under the android client too, fall back to cookies:
    1. Install browser extension: 'Get cookies.txt LOCALLY' (Chrome/Edge/Firefox)
    2. Go to youtube.com while logged in
    3. Click the extension -> Export -> save as cookies.txt in this skill directory
    4. Re-run ingest.py — it will pick up cookies.txt automatically
    """
    base = ["yt-dlp"] if shutil.which("yt-dlp") else [sys.executable, "-m", "yt_dlp"]
    cookies_file = SKILL_DIR / "cookies.txt"
    if cookies_file.exists():
        return base + ["--cookies", str(cookies_file), "--remote-components", "ejs:github"]
    return base + ["--extractor-args", "youtube:player_client=android"]

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

WHISPER_VOCAB_HINT = ("Blender, geometry nodes, Cycles, EEVEE, shader editor, Node Wrangler, Principled BSDF, subdivision surface, UV unwrap, HDRI, compositor, grease pencil, VDB, displacement, bevel, boolean, Mix Shader, Color Ramp")

def _load_whisper_model(model_name):
    """First use of a model downloads its weights, and tqdm floods captured
    output with hundreds of progress-bar lines on stderr. Print one notice
    instead; replay the captured stderr only if loading actually fails."""
    import io, contextlib, whisper
    cache_dir = Path(os.getenv("XDG_CACHE_HOME", str(Path.home() / ".cache"))) / "whisper"
    if not (cache_dir / f"{model_name}.pt").exists():
        print(f"      Whisper model '{model_name}' not cached yet - downloading weights (one-time)...")
    captured = io.StringIO()
    try:
        with contextlib.redirect_stderr(captured):
            return whisper.load_model(model_name)
    except Exception:
        sys.stderr.write(captured.getvalue())
        raise

def whisper_transcribe(audio_path, model_name):
    model = _load_whisper_model(model_name)
    # initial_prompt biases decoding toward this skill's vocabulary — without it
    # Whisper mis-hears domain terms (e.g. "COPs" -> "cups", "Houdini" -> "Odini").
    return model.transcribe(str(audio_path), initial_prompt=WHISPER_VOCAB_HINT)

def download_audio(url, tmp):
    out = str(tmp / "audio.%(ext)s")
    cmd = _ytdlp_cmd() + ["-x", "--audio-format", "mp3", "--audio-quality", "0",
         "--no-playlist", "-o", out, url]
    # YouTube throttling makes one-off download failures common; a single retry
    # usually recovers and preserves the timestamped Whisper transcript instead
    # of degrading to the timestamp-less captions fallback.
    for attempt in (1, 2):
        try:
            subprocess.run(cmd, capture_output=True, timeout=300, check=True)
            break
        except subprocess.CalledProcessError:
            if attempt == 2:
                raise
            print("      Audio download failed - retrying once...")
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
    """
    Bucket the Whisper transcript into sections (by official chapters, or one
    "Full Content" section if none exist). Each section keeps both a joined
    `text` blob (for the completeness/hallucination safeguards) and a
    per-sentence `segments` list of (start_seconds, text) tuples — the fine
    timestamps are what let Step 2 pick content-anchored frame moments instead
    of trusting chapter boundaries blindly.
    """
    segs = transcript.get("segments", [])
    if not chapters:
        all_segs = [(s.get("start", 0), s["text"].strip()) for s in segs]
        return [{"title": "Full Content", "start": 0,
                 "text": transcript.get("text", "").strip(),
                 "segments": all_segs}]
    result = []
    for i, ch in enumerate(chapters):
        t0 = ch.get("start_time", 0)
        t1 = chapters[i+1].get("start_time", float("inf")) if i+1 < len(chapters) else float("inf")
        in_range = [s for s in segs if t0 <= s.get("start", 0) < t1]
        text = " ".join(s["text"].strip() for s in in_range).strip()
        seg_list = [(s.get("start", 0), s["text"].strip()) for s in in_range]
        result.append({"title": ch.get("title", f"Chapter {i+1}"), "start": t0,
                        "text": text, "segments": seg_list})
    return result

# ── Step 3: Frame extraction ───────────────────────────────────────────────────

def download_video_low(url, tmp):
    """
    Download the video for frame extraction, at a resolution frames can be READ at.

    This used to request `worst[ext=mp4]/worst` -- literally the lowest stream
    available -- which produced 256x144 frames. Measured 2026-08-19 across the
    ingested libraries: unreal-sidekick's frames are 256x144 (avg 11KB) and
    nuke-em-all's are 256x144/426x240, resolutions at which node names and
    parameter values in a screencast are simply not legible. Frame grounding
    cannot work when the frame cannot be read, so the whole point of Step 2 was
    being lost.

    Capped at 720p rather than uncapped: frames are only sampled at a handful of
    timestamps, but yt-dlp still downloads the whole file, and these run in
    batches of hundreds. Set INGEST_FRAME_HEIGHT to raise it (1080 helps for
    dense UI like Nuke's node graph or Houdini's parameter pane).
    """
    h = os.environ.get("INGEST_FRAME_HEIGHT", "720")
    fmt = (f"bestvideo[height<={h}][ext=mp4]/bestvideo[height<={h}]/"
           f"best[height<={h}][ext=mp4]/best[height<={h}]/best")
    out = str(tmp / "video.%(ext)s")
    cmd = _ytdlp_cmd() + ["-f", fmt, "--no-playlist", "-o", out, url]
    # Same one-off YouTube throttling failures as the audio download in Step 1;
    # a single retry usually recovers (select_frames.py depends on this helper).
    for attempt in (1, 2):
        try:
            subprocess.run(cmd, capture_output=True, timeout=600, check=True)
            break
        except subprocess.CalledProcessError:
            if attempt == 2:
                raise
            print("      Video download failed - retrying once...")
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

def run_safeguards(ch_transcripts):
    """
    Run all Step-1 ingest quality checks (transcript completeness + ASR hallucination).
    Returns (warnings, critical) — critical items mark extraction_status: needs-review.

    Frame-count validation is NOT done here: ingest.py no longer downloads video or
    extracts frames (deferred to select_frames.py, Step 2), so there's nothing to check
    yet at this point. See select_frames.py's own safeguard checks + append_safeguard_note()
    for the frame-capture-time equivalent.
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

def build_safeguard_section(warnings, critical):
    """
    Render the WARNING/CRITICAL findings as a markdown section. Returns "" if both
    lists are empty (clean ingests get no extra section — matches the console
    behavior of only speaking up when something's actually wrong).

    Persisting this into the .md file (not just printing to console) is what makes
    a `needs-review` flag auditable later — otherwise the *reason* a tutorial got
    flagged only ever existed in whatever terminal happened to be open at ingest time.
    """
    if not warnings and not critical:
        return ""
    lines = [
        "\n## Ingest Safeguard Report\n",
        "_Auto-generated at ingest/frame-capture time — explains why "
        "`extraction_status` may be `needs-review`. Safe to delete once reviewed._\n",
    ]
    for c in critical:
        lines.append(f"- **CRITICAL:** {c}")
    for w in warnings:
        lines.append(f"- WARNING: {w}")
    lines.append("\n---\n")
    return "\n".join(lines)

def append_safeguard_note(content, note, level="WARNING"):
    """
    Insert one more finding into an existing '## Ingest Safeguard Report' section,
    or create that section if this is the first finding for the file (e.g. Step 1's
    transcript checks were clean but Step 2's frame-capture check in select_frames.py
    found a problem). Shared by both ingest.py and select_frames.py so all quality-check
    reasoning ends up in one place inside the file, regardless of which step found it.
    """
    line = f"- **{level}:** {note}" if level == "CRITICAL" else f"- {level}: {note}"
    m = re.search(r"\n## Ingest Safeguard Report\n.*?\n---\n", content, re.DOTALL)
    if m:
        insertion_point = content.rindex("\n---\n", m.start(), m.end())
        return content[:insertion_point] + line + "\n" + content[insertion_point:]
    header = "## Raw Data (for Claude Code extraction)\n"
    idx = content.index(header) + len(header)
    section = (
        "\n## Ingest Safeguard Report\n\n"
        "_Auto-generated at ingest/frame-capture time — explains why "
        "`extraction_status` may be `needs-review`. Safe to delete once reviewed._\n\n"
        f"{line}\n\n---\n"
    )
    return content[:idx] + section + content[idx:]

# ── Build raw .md ──────────────────────────────────────────────────────────────

def build_raw_md(info, ch_transcripts, slug, frame_status="pending-selection",
                  sg_warnings=None, sg_critical=None):
    title    = info.get("title", "Unknown")
    url      = info.get("webpage_url", "")
    author   = info.get("uploader", "Unknown")
    today    = datetime.now().strftime("%Y-%m-%d")
    duration = info.get("duration", 0)
    dur_str  = f"{int(duration)//60}m{int(duration)%60}s" if duration else "unknown"

    # Chapter breakdown with per-sentence timestamped transcript.
    # No frames yet at this point — frame capture is Step 2 (content-aware,
    # see select_frames.py), not blind-timestamped here in Step 1.
    chapters_section = ""
    for ch in ch_transcripts:
        t_fmt = f"{int(ch.get('start',0))//60}:{int(ch.get('start',0))%60:02d}"
        chapters_section += f"\n### {ch['title']} [{t_fmt}]\n"
        segs = ch.get('segments') or []
        if segs:
            chapters_section += "**Transcript (timestamped):**\n"
            for t, txt in segs:
                if not txt:
                    continue
                mm, ss = int(t) // 60, int(t) % 60
                chapters_section += f"[{mm}:{ss:02d}] {txt}\n"
            chapters_section += "\n"
        elif ch.get("text"):
            chapters_section += f"**Transcript:** {ch['text']}\n\n"

    if frame_status == "skipped":
        frame_note = "Frame capture was skipped for this ingest (--skip-video). Text-only extraction."
    else:
        frame_note = (
            f"Frames are not captured yet. Read the timestamped transcript below, pick moments\n"
            f"that actually show a technique/result worth a still (not blind percentages —\n"
            f"even within a named chapter, verify the real moment against its timestamps), then run:\n"
            f"  python select_frames.py {slug} <ts1> <ts2> ...\n"
            f"(seconds or mm:ss). This appends a \"Captured Frames\" section and updates the\n"
            f"frontmatter before you write the Structured Notes below."
        )

    safeguard_section = build_safeguard_section(sg_warnings or [], sg_critical or [])

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
frame_count: 0
frame_status: {frame_status}
---

# {title}

**Source:** [YouTube]({url})
**Author:** {author}
**Duration:** {dur_str} | {len(ch_transcripts)} section(s)

---

## Raw Data (for Claude Code extraction)
{safeguard_section}

{frame_note}

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

def update_readme_tutorial_count():
    """
    Keep README.md's "N tutorials ingested" line in sync with the real count on
    disk, so it can never silently go stale the way a hand-written number would.
    No-op if README.md has no line matching the expected pattern (e.g. it was
    reworded) — fails quiet rather than corrupting the file.
    """
    readme = SKILL_DIR / "README.md"
    if not readme.exists():
        return
    count = len([f for f in TUTORIALS_DIR.glob("*.md") if f.name != "INDEX.md"])
    content = readme.read_text(encoding="utf-8")
    new_content = re.sub(
        r"\*\*\d+\s*tutorials ingested\*\*",
        f"**{count} tutorials ingested**",
        content,
        count=1,
    )
    if new_content != content:
        readme.write_text(new_content, encoding="utf-8")

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

def find_duplicate_by_video_id(video_id, exclude_name):
    """Return the tutorial file that already references this YouTube video ID, if any.

    Slug/URL checks miss re-ingests where the uploader changed the title (new slug,
    new URL text) — the 11-char video ID is the stable identity, so search for it.
    """
    if not video_id:
        return None
    needle = f"v={video_id}"
    for f in TUTORIALS_DIR.glob("*.md"):
        if f.name in ("INDEX.md", exclude_name):
            continue
        try:
            if needle in f.read_text(encoding="utf-8", errors="ignore"):
                return f
        except OSError:
            continue
    return None


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
        print("[1/4] Fetching metadata...")
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

        if is_yt and not args.force:
            dup = find_duplicate_by_video_id(info.get("id", ""), out_md.name)
            if dup:
                print(f"      This video is already in the library under a different title:")
                print(f"        {dup.name}")
                print(f"      Skipping (same YouTube video ID). Pass --force to ingest anyway.")
                return

        if out_md.exists() and not args.force:
            existing = out_md.read_text(encoding="utf-8")
            if "extraction_status: complete" in existing:
                print(f"      {out_md.name} is already fully extracted — refusing to overwrite.")
                print(f"      Pass --force to re-collect anyway (this will wipe the existing Structured Notes).")
                return

        # 2. Transcript (per-sentence timestamps preserved — see segment_by_chapters)
        ch_transcripts = []
        used_captions_fallback = False
        if is_yt:
            if has_whisper:
                print(f"[2/4] Downloading audio + transcribing with Whisper ({args.whisper_model})...")
                try:
                    audio = download_audio(args.url, tmp)
                    transcript = whisper_transcribe(audio, args.whisper_model)
                    ch_transcripts = segment_by_chapters(transcript, chapters)
                    print(f"      {len(transcript.get('segments',[]))} segments -> {len(ch_transcripts)} sections")
                except Exception as e:
                    print(f"      Whisper failed ({e}), using yt-dlp captions")
                    used_captions_fallback = True
                    text = ytdlp_captions(args.url, tmp)
                    ch_transcripts = [{"title": "Full Content", "start": 0, "text": text, "segments": []}]
            else:
                print("[2/4] Whisper not installed - using yt-dlp captions (pip install openai-whisper for better results)")
                used_captions_fallback = True
                text = ytdlp_captions(args.url, tmp)
                ch_transcripts = [{"title": "Full Content", "start": 0, "text": text, "segments": []}]
        else:
            print("[2/4] Article - using page text")
            ch_transcripts = [{"title": "Full Content", "start": 0,
                               "text": info.get("description", ""), "segments": []}]

        # Frame capture is deferred to Step 2 (select_frames.py), driven by Claude
        # reading the timestamped transcript below — content-aware beats blind
        # percentage timestamps, and picking *which* moments matter needs judgment
        # this script deliberately doesn't have (no API calls made here).
        can_have_frames = is_yt and not args.skip_video and has_ffmpeg
        frame_status = "pending-selection" if can_have_frames else "skipped"
        if not can_have_frames:
            reason = "article" if not is_yt else ("--skip-video" if args.skip_video else "ffmpeg not found")
            print(f"[3/4] Frame capture skipped ({reason})")
        else:
            print("[3/4] Frame capture deferred to Step 2 (content-aware selection via select_frames.py)")

        # Safeguard checks — transcript completeness/hallucination only; frame-count
        # validation now happens in select_frames.py once real timestamps are chosen.
        sg_warnings, sg_critical = run_safeguards(ch_transcripts)
        if used_captions_fallback:
            sg_warnings.append('Transcript came from the yt-dlp captions fallback - NO per-sentence timestamps. Content-anchored frame selection (select_frames.py) will have to estimate moments; consider re-running ingest.py to retry Whisper before extracting.')
        _print_safeguard_report(sg_warnings, sg_critical)

        # 4. Write raw .md + commit
        print("[4/4] Writing raw tutorial file...")
        md = build_raw_md(info, ch_transcripts, slug, frame_status, sg_warnings, sg_critical)
        if sg_critical:
            md = md.replace("extraction_status: pending", "extraction_status: needs-review", 1)
        out_md.write_text(md, encoding="utf-8")
        update_index_pending(info, slug, out_md.name)
        update_readme_tutorial_count()

        print("      Committing raw data to GitHub...")
        os.chdir(SKILL_DIR)
        git_add = [str(out_md.relative_to(SKILL_DIR)), str(INDEX_FILE.relative_to(SKILL_DIR))]
        if (SKILL_DIR / "README.md").exists():
            git_add.append("README.md")
        subprocess.run(["git", "add"] + git_add, check=True)
        subprocess.run(["git", "commit", "-m", f"collect: {title}"], check=True)
        subprocess.run(["git", "push"], check=True)

        # Summary for Claude Code
        print(f"\n{'='*60}")
        print(f"  Collection complete. Claude Code: run extraction now.")
        print(f"  Tutorial file: tutorials/{out_md.name}")
        if can_have_frames:
            print(f"  Next: read the timestamped transcript, then run")
            print(f"        python select_frames.py {slug} <ts1> <ts2> ...")
            print(f"        before writing Structured Notes.")
        else:
            print(f"  Frames:        none (text-only extraction)")
        print(f"{'='*60}\n")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    main()
