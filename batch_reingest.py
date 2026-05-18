"""
batch_reingest.py — Re-ingest all tutorials in INDEX.md using the enhanced pipeline.

Reads every URL from tutorials/INDEX.md, runs ingest.py for each one, and overwrites
the existing tutorial files with Whisper transcription, chapter segmentation,
multi-pass Claude extraction, and auto cross-linking.

Each tutorial is committed and pushed individually — so if the run is interrupted,
everything processed so far is already on GitHub.

Usage:
  python batch_reingest.py                       # full pipeline (slow, ~15-20 hrs)
  python batch_reingest.py --skip-video          # no frames, transcript+Claude only (~4-5 hrs)
  python batch_reingest.py --whisper-model small # better accuracy, slower Whisper
  python batch_reingest.py --skip-video --start 10  # resume from tutorial #10

Estimated time (RTX 5070, GPU Whisper, base model):
  --skip-video:   ~4-5 minutes per tutorial  ->  ~4-5 hours for 58 tutorials
  full pipeline:  ~20-25 minutes per tutorial -> ~20 hours for 58 tutorials

After this script finishes, tell Claude Code: "extract all pending tutorials"
and it will read each raw file + frames and do the full extraction pass.
"""

import re
import sys
import time
import subprocess
import argparse
from pathlib import Path
from datetime import datetime, timedelta

SKILL_DIR     = Path(__file__).parent
TUTORIALS_DIR = SKILL_DIR / "tutorials"
INDEX_FILE    = TUTORIALS_DIR / "INDEX.md"
INGEST_SCRIPT = SKILL_DIR / "ingest.py"
LOG_FILE      = SKILL_DIR / "batch_reingest.log"


def extract_urls_from_index():
    """Pull all URLs from INDEX.md, preserving order."""
    content = INDEX_FILE.read_text(encoding="utf-8")
    # Match "**URL:** <url>" anywhere in line (handles "- **URL:** ..." format)
    urls = []
    for line in content.splitlines():
        m = re.search(r"\*\*URL:\*\*\s*(https?://\S+)", line)
        if m:
            url = m.group(1).strip()
            urls.append(url)
    return urls


def log(msg, file=None):
    ts = datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    if file:
        file.write(line + "\n")
        file.flush()


def eta(elapsed_sec, done, total):
    if done == 0:
        return "?"
    avg = elapsed_sec / done
    remaining = avg * (total - done)
    return str(timedelta(seconds=int(remaining)))


def main():
    parser = argparse.ArgumentParser(description="Re-ingest all tutorials with the enhanced pipeline")
    parser.add_argument("--skip-video", action="store_true",
                        help="Skip video download and frame extraction (faster)")
    parser.add_argument("--whisper-model", default="base",
                        choices=["tiny", "base", "small", "medium", "large"])
    parser.add_argument("--start", type=int, default=1,
                        help="Start from tutorial number N (1-based, for resuming)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print URLs that would be processed, then exit")
    args = parser.parse_args()

    urls = extract_urls_from_index()
    total = len(urls)

    print(f"\n{'='*60}")
    print(f"  blender-motion — Batch Re-ingest")
    print(f"  {total} tutorials found in INDEX.md")
    print(f"  Mode: {'--skip-video (transcript + Claude only)' if args.skip_video else 'full pipeline (with frames + vision)'}")
    print(f"  Whisper model: {args.whisper_model}")
    if args.start > 1:
        print(f"  Resuming from tutorial #{args.start}")
    print(f"{'='*60}\n")

    if args.dry_run:
        for i, url in enumerate(urls, 1):
            print(f"  {i:3d}. {url}")
        print(f"\nTotal: {total} URLs — dry run, nothing executed.")
        return

    successes = []
    failures  = []
    start_time = time.time()

    with open(LOG_FILE, "w", encoding="utf-8") as logf:
        log(f"Batch reingest started — {total} tutorials", logf)
        log(f"skip-video={args.skip_video}  whisper={args.whisper_model}", logf)

        for i, url in enumerate(urls, 1):
            if i < args.start:
                continue

            elapsed = time.time() - start_time
            done_so_far = len(successes) + len(failures)
            eta_str = eta(elapsed, done_so_far, total - args.start + 1)

            log(f"[{i}/{total}] ETA {eta_str} — {url}", logf)

            cmd = [sys.executable, str(INGEST_SCRIPT), url,
                   "--whisper-model", args.whisper_model]
            if args.skip_video:
                cmd.append("--skip-video")

            try:
                result = subprocess.run(
                    cmd,
                    cwd=SKILL_DIR,
                    timeout=1800,   # 30 min max per tutorial
                    capture_output=False  # let output flow through so user can watch
                )
                if result.returncode == 0:
                    successes.append(url)
                    log(f"  OK ({i}/{total})", logf)
                else:
                    failures.append((url, f"exit code {result.returncode}"))
                    log(f"  FAIL exit={result.returncode}", logf)
            except subprocess.TimeoutExpired:
                failures.append((url, "timeout after 30 min"))
                log(f"  FAIL timeout", logf)
            except Exception as e:
                failures.append((url, str(e)))
                log(f"  FAIL {e}", logf)

        # Summary
        elapsed_total = time.time() - start_time
        log(f"\n{'='*60}", logf)
        log(f"Done in {timedelta(seconds=int(elapsed_total))}", logf)
        log(f"Succeeded: {len(successes)}/{total}", logf)
        log(f"Failed:    {len(failures)}/{total}", logf)
        if failures:
            log("Failed URLs:", logf)
            for url, err in failures:
                log(f"  {url}  ({err})", logf)
        log(f"Full log: {LOG_FILE}", logf)


if __name__ == "__main__":
    main()
