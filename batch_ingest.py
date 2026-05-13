"""
Batch ingest multiple YouTube URLs into the Blender Motion skill.
Does ONE git commit + push at the end instead of one per video.

Usage: python batch_ingest.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from ingest import fetch_youtube, build_tutorial_markdown, update_index, slugify, TUTORIALS_DIR, INDEX_FILE, SKILL_DIR
import subprocess
from pathlib import Path

URLS = [
    "https://youtu.be/Y0zAZnbBcQU",
    "https://youtu.be/SybPYdsd_DI",
    "https://youtu.be/MS1z9diLUOI",
    "https://youtu.be/RQvTplfsz8k",
    "https://youtu.be/ENnEYoUpFfU",
    "https://youtu.be/WbrjlYM0Qno",
    "https://youtu.be/qrYmDg0HpYI",
    "https://youtu.be/csvduOcQpIw",
    "https://youtu.be/QJhiYYf6qJI",
    "https://youtu.be/_7N7emOvDko",
    "https://youtu.be/upUPrc35DYw",
    "https://youtu.be/SCz1tmOVmFw",
    "https://youtu.be/NwYZ1QKQhx0",
    "https://youtu.be/IzSRBH8CDTo",
    "https://youtu.be/KnYGp58REUk",
    "https://youtu.be/Kep7URnyXgU",
    "https://youtu.be/IgpUXXg2Vbs",
    "https://youtu.be/DvMyxyMG0Mk",
    "https://youtu.be/iW6WF8guDMY",
    "https://youtu.be/FYJb10NIMH8",
    "https://youtu.be/-QbetK8c1As",
    "https://youtu.be/4ULxB4PzbAc",
    "https://youtu.be/ZBZ26xQ9Pnk",
    "https://youtu.be/Fec4BhDFBUo",
    "https://youtu.be/erICwexR7Iw",
    "https://youtu.be/Vqe4jBf3wx4",
    "https://www.youtube.com/live/7FdfSKOkzXg",
    "https://youtu.be/JU70u6cJZqI",
    "https://youtu.be/PgRax5MeZgY",
    "https://youtu.be/EvWAcSA86fw",
    "https://youtu.be/8wFnzrRz0Xg",
    "https://www.youtube.com/live/z-fKQtlQPw0",
    "https://youtu.be/1hKAkCP-tFQ",
    "https://youtu.be/0lBaaCMpZGs",
    "https://youtu.be/ZmoL0Wa5n0Y",
    "https://youtu.be/QHJXi25OczQ",
    "https://youtu.be/RU3VO-qb91o",
    "https://youtu.be/YOx9me2MnGA",
    "https://youtu.be/U5y1Krd-ykk",
    "https://youtu.be/vemW4ceygRg",
    "https://youtu.be/KhBaHDvIamw",
    "https://youtu.be/9Fvw8HlWHpo",
    "https://youtu.be/rbPOL9ibooY",
    "https://youtu.be/TTGcr-45jCE",
    "https://youtu.be/2MKKuHcni1U",
    "https://youtu.be/XOLuYDLYEgI",
    "https://youtu.be/965bgIUHoxA",
    "https://youtu.be/tj6ZZYO5qPY",
]

saved_files = []
failed = []

print(f"Ingesting {len(URLS)} videos...\n")

for i, url in enumerate(URLS, 1):
    print(f"[{i}/{len(URLS)}] {url}")
    try:
        data = fetch_youtube(url)
        title = data["title"]
        slug = slugify(title)
        filename = f"{slug}.md"
        output_path = TUTORIALS_DIR / filename

        md = build_tutorial_markdown(data)
        output_path.write_text(md, encoding="utf-8")
        update_index(title, url, filename, "YouTube", data["author"])
        saved_files.append(str(output_path))
        print(f"    OK  {title[:60]}")
    except Exception as e:
        print(f"    ERR {e}")
        failed.append((url, str(e)))

print(f"\n--- Done: {len(saved_files)} saved, {len(failed)} failed ---")

if failed:
    print("\nFailed URLs:")
    for url, err in failed:
        print(f"  {url}: {err}")

# Single git commit + push
if saved_files:
    print("\nCommitting and pushing to GitHub...")
    try:
        subprocess.run(["git", "add", "tutorials/"], cwd=SKILL_DIR, check=True)
        subprocess.run(
            ["git", "commit", "-m", f"ingest: batch of {len(saved_files)} tutorials"],
            cwd=SKILL_DIR, check=True
        )
        subprocess.run(["git", "push"], cwd=SKILL_DIR, check=True)
        print("Pushed to GitHub.")
    except Exception as e:
        print(f"Push failed: {e}. Run 'git push' manually.")
