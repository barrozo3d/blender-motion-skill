#!/usr/bin/env python3
"""
validate.py -- Post-ingest integrity checker for blender-motion tutorials.

Run from the repo root:
    python validate.py

Exit 0 = all checks pass.
Exit 1 = one or more failures found (details printed to stdout).

Checks performed:
  1. No [PENDING EXTRACTION] markers in any tutorial body
  2. No extraction_status: pending in frontmatter
  3. No blender_version: "[PENDING]" in frontmatter
  4. No empty tags arrays (tags: [] or tags: [""])
  5. INDEX.md has no duplicate **File:** entries
  6. Every tutorial file on disk appears in INDEX.md exactly once
  7. Every INDEX.md file reference points to a file that exists on disk
  8. Every tutorial with a YouTube source has non-trivial structured notes (> 200 chars)
  9. YouTube videos with duration > 3 min have a non-empty transcript
     (catches failed/truncated ingest where yt-dlp or Whisper returned nothing)
  10. No PLACEHOLDER url: values in frontmatter
"""

import os
import re
import sys

TUTORIALS_DIR = os.path.join(os.path.dirname(__file__), "tutorials")
INDEX_PATH = os.path.join(TUTORIALS_DIR, "INDEX.md")

NOTES_MIN_CHARS = 200
TRANSCRIPT_CHARS_PER_SEC = 3
TRANSCRIPT_MIN_DURATION_SECS = 180  # 3 minutes

TEMPLATE_REFS = {"filename.md"}

failures = []


def fail(msg):
    failures.append(msg)
    print(f"  FAIL: {msg}")


def get_tutorial_files():
    return sorted(
        f for f in os.listdir(TUTORIALS_DIR)
        if f.endswith(".md") and f != "INDEX.md"
    )


def parse_index_refs():
    with open(INDEX_PATH, "r", encoding="utf-8-sig") as fh:
        content = fh.read()
    refs = []
    for m in re.finditer(r"\*\*File:\*\*\s+tutorials/([^\s\)]+\.md)", content):
        fname = m.group(1)
        if fname not in TEMPLATE_REFS:
            refs.append(fname)
    return refs


def get_notes_content(content):
    m = re.search(r"## Structured Notes(.+)", content, re.DOTALL)
    return m.group(1).strip() if m else ""


def is_youtube_source(content):
    m = re.search(r"^source:\s*(.+)", content, re.MULTILINE)
    if not m:
        return False
    return "youtube" in m.group(1).lower()


def parse_duration_secs(content):
    m = re.search(r"\*\*Duration:\*\*\s+(?:(\d+)h\s*)?(?:(\d+)m\s*)?(?:(\d+)s)?", content)
    if not m:
        return 0
    hours = int(m.group(1) or 0)
    mins = int(m.group(2) or 0)
    secs = int(m.group(3) or 0)
    return hours * 3600 + mins * 60 + secs


def get_transcript_text(content):
    raw_start = content.find("## Raw Data")
    if raw_start == -1:
        return None
    raw = content[raw_start:]

    notes_split = re.search(r"\n## Structured Notes", raw)
    if notes_split:
        raw = raw[:notes_split.start()]

    # The Ingest Safeguard Report box (inserted by ingest.py/select_frames.py for
    # needs-review files) ends with its own "\n---\n" divider that sits *before*
    # the real transcript — strip the whole box out first so the boundary check
    # below doesn't mistake it for the end of the Raw Data section.
    raw = re.sub(r"\n## Ingest Safeguard Report\n.*?\n---\n", "\n", raw, flags=re.DOTALL)

    boundary = re.search(r"\n---", raw)
    if boundary:
        raw = raw[:boundary.start()]

    if "[...raw data omitted" in raw:
        return None
    transcript_lines = []
    for line in raw.splitlines():
        stripped = line.strip()
        if stripped.startswith("**Transcript:**"):
            transcript_lines.append(stripped[len("**Transcript:**"):].strip())
        elif re.match(r"\[\d+:\d{2}\] ", stripped):
            # timestamped per-sentence format ("[m:ss] text") written by ingest.py
            # since the chapter-timestamp update — count the text after the stamp
            transcript_lines.append(stripped.split("] ", 1)[1])
    return " ".join(transcript_lines)


def check_tutorials():
    print("\n[1] Checking tutorial files for PENDING markers, frontmatter issues, and transcript health...")
    files = get_tutorial_files()
    for fname in files:
        path = os.path.join(TUTORIALS_DIR, fname)
        with open(path, "r", encoding="utf-8-sig") as fh:
            content = fh.read()

        if "[PENDING EXTRACTION]" in content:
            fail(f"{fname}: contains [PENDING EXTRACTION] markers")

        if re.search(r"extraction_status:\s*pending", content, re.IGNORECASE):
            fail(f"{fname}: extraction_status is 'pending'")

        if re.search(r'blender_version:\s*["\']?\[?PENDING', content, re.IGNORECASE):
            fail(f"{fname}: blender_version is still a PENDING placeholder")

        if re.search(r"tags:\s*\[\s*(?:\"\"|'')?\s*\]", content):
            fail(f"{fname}: tags array is empty")

        # url must not be a PLACEHOLDER (extract step once overwrote real URLs
        # with the template value in unreal-sidekick — guarded here too)
        if re.search(r"^url:.*PLACEHOLDER", content, re.MULTILINE):
            fail(f"{fname}: url is a PLACEHOLDER — recover the real URL from git history or batch_ingest.py")

        if is_youtube_source(content):
            notes = get_notes_content(content)
            if len(notes) < NOTES_MIN_CHARS:
                fail(
                    f"{fname}: YouTube source but structured notes are too short "
                    f"({len(notes)} chars, minimum {NOTES_MIN_CHARS})"
                )

            duration_secs = parse_duration_secs(content)
            if duration_secs >= TRANSCRIPT_MIN_DURATION_SECS:
                transcript = get_transcript_text(content)
                if transcript is not None:
                    no_transcript_ack = bool(re.search(
                        r"transcript\s+(not\s+captured|not\s+available|unavailable|was\s+not\s+captured"
                        r"|could\s+not\s+be\s+captured|quality\s+degrades)",
                        notes, re.IGNORECASE,
                    ))
                    if not no_transcript_ack:
                        min_expected = int(duration_secs * TRANSCRIPT_CHARS_PER_SEC)
                        if len(transcript) < min_expected:
                            fail(
                                f"{fname}: transcript appears truncated or empty -- "
                                f"{len(transcript)} chars for a {duration_secs}s video "
                                f"(expected >= {min_expected} chars at "
                                f"{TRANSCRIPT_CHARS_PER_SEC} chars/sec)"
                            )

    print(f"  Checked {len(files)} files.")


def check_index():
    print("\n[2] Checking INDEX.md for duplicates and cross-references...")

    refs = parse_index_refs()
    disk_files = set(get_tutorial_files())

    seen = {}
    for fname in refs:
        seen.setdefault(fname, 0)
        seen[fname] += 1
    for fname, count in seen.items():
        if count > 1:
            fail(f"INDEX.md: duplicate entry for '{fname}' (appears {count} times)")

    ref_set = set(refs)

    missing_from_index = disk_files - ref_set
    for fname in sorted(missing_from_index):
        fail(f"INDEX.md: missing entry for '{fname}' (file exists on disk)")

    orphan_refs = ref_set - disk_files
    for fname in sorted(orphan_refs):
        fail(f"INDEX.md: references non-existent file '{fname}'")

    print(f"  INDEX entries: {len(ref_set)} | Disk files: {len(disk_files)}")


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("=" * 60)
    print("blender-motion validate.py")
    print("=" * 60)

    if not os.path.isdir(TUTORIALS_DIR):
        print(f"ERROR: tutorials directory not found at {TUTORIALS_DIR}")
        sys.exit(1)

    if not os.path.isfile(INDEX_PATH):
        print(f"ERROR: INDEX.md not found at {INDEX_PATH}")
        sys.exit(1)

    check_tutorials()
    check_index()

    print("\n[drift] Checking shared-script sync with sibling skills...")
    check_script_drift()

    print("\n" + "=" * 60)
    if failures:
        print(f"RESULT: FAIL -- {len(failures)} issue(s) found:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print("RESULT: PASS -- all checks clean.")
        sys.exit(0)




# ── Cross-skill script drift check (warn-only) ────────────────────────────────
# The three skills (blender-motion / houdini-wand / unreal-sidekick) deliberately
# carry copies of the same ingest pipeline. Copies have historically drifted
# (missing UTF-8 fix, mismatched cookies flags), so when sibling skill dirs are
# present on this machine, compare the shared helper functions and WARN on
# differences. Never fails the run — per-skill divergence may be intentional,
# but it should always be a conscious choice.
SIBLING_SKILLS = ("blender-motion", "houdini-wand", "unreal-sidekick")
SHARED_FUNCS = ("slugify", "download_audio", "ytdlp_captions", "segment_by_chapters",
                "_detect_hallucination", "append_safeguard_note", "find_duplicate_by_video_id")


def check_script_drift():
    import ast
    here = os.path.dirname(os.path.abspath(__file__))
    skills_root = os.path.dirname(here)
    my_name = os.path.basename(here)

    def func_sources(pyfile):
        try:
            with open(pyfile, "r", encoding="utf-8") as fh:
                src = fh.read()
            tree = ast.parse(src)
        except Exception:
            return {}
        found = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in SHARED_FUNCS:
                found[node.name] = ast.get_source_segment(src, node)
        return found

    mine = func_sources(os.path.join(here, "ingest.py"))
    warned = False
    for sib in SIBLING_SKILLS:
        if sib == my_name:
            continue
        sib_ingest = os.path.join(skills_root, sib, "ingest.py")
        if not os.path.isfile(sib_ingest):
            continue
        theirs = func_sources(sib_ingest)
        for fn in SHARED_FUNCS:
            if fn in mine and fn in theirs and mine[fn] != theirs[fn]:
                print(f"  DRIFT WARNING: ingest.py::{fn}() differs from sibling skill '{sib}' "
                      f"-- if the change was intentional, port it to all skills")
                warned = True
    if not warned:
        print("  Shared ingest.py helpers in sync with sibling skills (or no siblings installed).")


if __name__ == "__main__":
    main()
