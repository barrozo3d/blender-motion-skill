"""
batch_ingest.py — Ingest a list of NEW YouTube URLs using the enhanced pipeline.

Add URLs to the URLS list below, then run:
  python batch_ingest.py
  python batch_ingest.py --skip-video       # faster, no frame extraction
  python batch_ingest.py --whisper-model small

Each tutorial is committed and pushed individually.
To re-ingest the entire existing library, use batch_reingest.py instead.
"""

import sys
import subprocess
import argparse
from pathlib import Path

SKILL_DIR     = Path(__file__).parent
INGEST_SCRIPT = SKILL_DIR / "ingest.py"

# ── Add URLs here ─────────────────────────────────────────────────────────────
URLS = [
    # "https://www.youtube.com/watch?v=...",
    # "https://youtu.be/...",
]
# ─────────────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(description="Batch ingest new tutorials")
    parser.add_argument("--skip-video", action="store_true")
    parser.add_argument("--whisper-model", default="base",
                        choices=["tiny", "base", "small", "medium", "large"])
    args = parser.parse_args()

    if not URLS:
        print("No URLs in URLS list. Add them to batch_ingest.py and re-run.")
        return

    print(f"Ingesting {len(URLS)} URL(s)...\n")
    successes, failures = [], []

    for i, url in enumerate(URLS, 1):
        print(f"\n[{i}/{len(URLS)}] {url}")
        cmd = [sys.executable, str(INGEST_SCRIPT), url,
               "--whisper-model", args.whisper_model]
        if args.skip_video:
            cmd.append("--skip-video")

        result = subprocess.run(cmd, cwd=SKILL_DIR)
        if result.returncode == 0:
            successes.append(url)
        else:
            failures.append(url)

    print(f"\n{'='*50}")
    print(f"Done — {len(successes)} succeeded, {len(failures)} failed")
    if failures:
        print("Failed:")
        for u in failures:
            print(f"  {u}")


if __name__ == "__main__":
    main()
