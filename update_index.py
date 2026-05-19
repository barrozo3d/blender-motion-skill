"""
update_index.py — Update INDEX.md entries from extracted tutorial files.
Reads each tutorial's frontmatter (blender_version, tags) and Summary section,
then patches the matching INDEX.md entry.
"""

import re
from pathlib import Path

SKILL_DIR = Path(__file__).parent
TUTORIALS_DIR = SKILL_DIR / "tutorials"
INDEX_FILE = TUTORIALS_DIR / "INDEX.md"


def parse_tutorial(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")

    # --- frontmatter ---
    fm_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    version, tags_raw = "Not specified", []
    if fm_match:
        fm = fm_match.group(1)
        v = re.search(r'^blender_version:\s*"?([^"\n]+)"?', fm, re.M)
        if v:
            version = v.group(1).strip().strip('"')
        t = re.search(r'^tags:\s*\[([^\]]*)\]', fm, re.M)
        if t:
            tags_raw = [x.strip().strip('"') for x in t.group(1).split(",") if x.strip()]

    # --- Summary section ---
    summary_match = re.search(r"### Summary\n(.*?)(?=\n###|\n---|\Z)", text, re.DOTALL)
    summary = ""
    if summary_match:
        raw = summary_match.group(1).strip()
        # take first two sentences / up to 300 chars
        sentences = re.split(r'(?<=[.!?])\s+', raw)
        summary = " ".join(sentences[:2])[:350]
        if len(raw) > 350:
            summary = summary.rstrip(".") + "..."

    tags_str = ", ".join(tags_raw) if tags_raw else "Not specified"
    return version, tags_str, summary


def update_index():
    index_text = INDEX_FILE.read_text(encoding="utf-8", errors="ignore")
    changed = 0

    for tut_file in sorted(TUTORIALS_DIR.glob("*.md")):
        if tut_file.name == "INDEX.md":
            continue

        version, tags_str, summary = parse_tutorial(tut_file)

        # Find the matching entry in INDEX.md by file name
        rel = f"tutorials/{tut_file.name}"
        # Look for the block containing this file reference
        pattern = rf'(\*\*File:\*\* {re.escape(rel)})'
        if not re.search(pattern, index_text):
            continue

        # Find the block: from the line with File: backwards to the ### heading
        # Strategy: find the entry block and patch [PENDING] fields
        def replace_pending_version(m):
            block = m.group(0)
            block = re.sub(
                r'\*\*Blender Version:\*\* \[PENDING\]',
                f'**Blender Version:** {version}',
                block
            )
            block = re.sub(
                r'\*\*Tags:\*\* \[PENDING\]',
                f'**Tags:** {tags_str}',
                block
            )
            if summary:
                block = re.sub(
                    r'\*\*Summary:\*\* \[PENDING EXTRACTION\]',
                    f'**Summary:** {summary}',
                    block
                )
            return block

        # Match the entry block (from ### Title down to the File: line)
        entry_pattern = rf'(###[^\n]+\n(?:.*\n)*?.*?{re.escape(rel)}[^\n]*)'
        new_text, n = re.subn(entry_pattern, replace_pending_version, index_text)
        if n:
            index_text = new_text
            changed += 1

    INDEX_FILE.write_text(index_text, encoding="utf-8")
    print(f"Updated {changed} entries in INDEX.md")


if __name__ == "__main__":
    update_index()
