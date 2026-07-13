"""
select_frames.py — Content-aware frame capture (Step 2 of the pipeline).

ingest.py (Step 1) no longer picks frame timestamps itself — it deliberately
makes no API calls, so it can't judge *which* moments in a tutorial are worth
a still. Instead it saves a per-sentence timestamped transcript and defers
frame capture here.

Workflow:
  1. Run `python ingest.py <url>` — collects transcript, no video/frames yet.
  2. Read the timestamped transcript in tutorials/<slug>.md ("## Raw Data").
     Pick moments that actually show a technique/result worth a still — not
     blind percentages of the runtime. Do this even for chapters with official
     titles: verify the real moment against the chapter's own timestamps
     instead of trusting `chapter_start + 5s`.
  3. Run this script with those timestamps:
       python select_frames.py <slug> 10 60 4:20 8:05 ...
     (accepts plain seconds or mm:ss, mixed freely)
  4. Write the Structured Notes section using the transcript + captured frames.

This reuses ingest.py's download_video_low()/extract_frames() unchanged, so
there's no duplicated yt-dlp/ffmpeg logic to drift out of sync.
"""

import re
import sys
import shutil
import argparse
import tempfile
from pathlib import Path

import ingest  # same directory — reuse download_video_low / extract_frames

SKILL_DIR     = Path(__file__).parent
TUTORIALS_DIR = SKILL_DIR / "tutorials"


def parse_timestamp(raw):
    """Accept plain seconds ('485', '485.0') or 'mm:ss' / 'h:mm:ss'."""
    if ":" not in raw:
        return float(raw)
    parts = [float(p) for p in raw.split(":")]
    seconds = 0.0
    for p in parts:
        seconds = seconds * 60 + p
    return seconds


def read_frontmatter_field(content, key):
    m = re.search(rf'^{key}:\s*(.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else None


def set_frontmatter_field(content, key, value):
    if re.search(rf'^{key}:.*$', content, re.MULTILINE):
        return re.sub(rf'^{key}:.*$', f'{key}: {value}', content, count=1, flags=re.MULTILINE)
    # Field doesn't exist yet — insert before the closing '---' of frontmatter
    end = content.index("\n---", content.index("---") + 3)
    return content[:end] + f"\n{key}: {value}" + content[end:]


def main():
    parser = argparse.ArgumentParser(
        description="Extract content-anchored frames for a collected tutorial (Step 2)"
    )
    parser.add_argument("slug", help="Tutorial slug (tutorials/<slug>.md must exist)")
    parser.add_argument("timestamps", nargs="+",
                         help="Timestamps to capture, seconds or mm:ss (e.g. 10 60 4:20 8:05)")
    parser.add_argument("--force", action="store_true",
                         help="Re-capture even if frame_status is already 'complete'")
    args = parser.parse_args()

    out_md = TUTORIALS_DIR / f"{args.slug}.md"
    if not out_md.exists():
        print(f"ERROR: {out_md} not found. Run ingest.py first.")
        sys.exit(1)

    content = out_md.read_text(encoding="utf-8")
    frame_status = read_frontmatter_field(content, "frame_status")
    if frame_status == "complete" and not args.force:
        print(f"      frame_status is already 'complete' — pass --force to re-capture.")
        sys.exit(1)
    if frame_status == "skipped" and not args.force:
        print(f"      frame_status is 'skipped' (ingested with --skip-video) — pass --force to override.")
        sys.exit(1)

    url = read_frontmatter_field(content, "url")
    if not url:
        print("ERROR: no 'url' field found in frontmatter.")
        sys.exit(1)

    timestamps = [parse_timestamp(t) for t in args.timestamps]
    out_dir = ingest.FRAMES_DIR / args.slug

    tmp = Path(tempfile.mkdtemp())
    try:
        print(f"[1/3] Downloading video (lowest quality) for {args.slug}...")
        video = ingest.download_video_low(url, tmp)

        print(f"[2/3] Extracting {len(timestamps)} content-anchored frame(s)...")
        frame_paths = ingest.extract_frames(video, timestamps, out_dir)
        print(f"      {len(frame_paths)}/{len(timestamps)} frame(s) saved to "
              f"{out_dir.relative_to(SKILL_DIR)}")

        if len(frame_paths) == 0:
            print("[SAFEGUARD] CRITICAL: 0 frames captured — check ffmpeg is in PATH "
                  "and the video downloaded correctly.")
        elif len(frame_paths) < len(timestamps):
            print(f"[SAFEGUARD] WARNING: only {len(frame_paths)}/{len(timestamps)} "
                  f"requested frames were captured.")
        else:
            print("[SAFEGUARD] All requested frames captured.")

        # Update frontmatter
        print("[3/3] Updating tutorial file...")
        content = set_frontmatter_field(content, "frame_count", str(len(frame_paths)))
        content = set_frontmatter_field(content, "frame_status", "complete")
        content = set_frontmatter_field(
            content, "frame_selection",
            "content-anchored (manual timestamps chosen from transcript, not blind percentages)"
        )

        # Replace the "not captured yet" instructional note, if still present
        content = re.sub(
            r"Frames are not captured yet\.[\s\S]*?frontmatter before you write the Structured Notes below\.",
            "Frames captured — see \"Captured Frames\" section below.",
            content,
        )

        captured_section = "\n## Captured Frames\n\n"
        for ts, fp in zip(timestamps, frame_paths):
            mm, ss = int(ts) // 60, int(ts) % 60
            captured_section += f"- [{mm}:{ss:02d}] {fp.relative_to(SKILL_DIR).as_posix()}\n"
        captured_section += "\n---\n"

        if "\n## Captured Frames\n" in content:
            content = re.sub(r"\n## Captured Frames\n.*?\n---\n", captured_section, content,
                              count=1, flags=re.DOTALL)
        else:
            content = content.replace("\n## Structured Notes",
                                       f"{captured_section}\n## Structured Notes", 1)

        out_md.write_text(content, encoding="utf-8")
        print(f"      Done. {out_md.relative_to(SKILL_DIR)} updated (not committed — "
              f"commit together with the Structured Notes once written).")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
