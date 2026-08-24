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
  11. No un-triaged promotional / no-content entries (scan_promo.py, allowlisted)
  12. INDEX block integrity — no block describing a different tutorial, no
      leftover [PENDING] fields, no mojibake
"""

import os
import re
import sys

try:
    import scan_promo
except ImportError:                       # pragma: no cover - scanner is optional
    scan_promo = None


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
    # below doesn't mistake it for the end of the Raw Data section. The heading
    # itself sometimes carries a reviewer suffix (e.g. "-- Reviewed") when Claude
    # Code has annotated it as checked, so match anything up to end-of-line there.
    raw = re.sub(r"\n## Ingest Safeguard Report[^\n]*\n.*?\n---\n", "\n", raw, flags=re.DOTALL)

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


INDEX_MOJIBAKE = re.compile(r"â€|â†|Ã[\x80-\xbf©¢­±]|Â[\xa0-\xbf]")

INDEX_BLOCK_RE = (r"### ([^\n]*)\n((?:- \*\*[^\n]*\n)*?)"
                  r"- \*\*File:\*\* tutorials/([^\s]+\.md)")


def check_index_integrity():
    """Check #12 -- the INDEX block must actually describe its own file.

    Check #2 verifies that every **File:** path exists on disk. It never asks
    whether the block DESCRIBES that file, and that gap hid real corruption:

      - tutorials/liquid-sops.md (SOP-based liquid effects, no solvers) was
        indexed with a molecular-visualisation course's tags AND summary --
        scientific-visualization, pdb, molecular, biology. SKILL.md prescribes
        grep-over-INDEX, so "surface tension" led straight to a file about
        Houdini Digital Assets. Two more entries in blender-motion shared one
        summary three ways.
      - nuke-em-all had a fully extracted tutorial whose INDEX block was still
        App/Version/Tags/Summary = [PENDING]. Check #1 only looks for PENDING
        markers inside tutorial FILES, so an unextracted index entry -- the
        actual retrieval surface -- passed silently.
      - 95 INDEX lines across two skills carried mojibake (UTF-8 decoded as
        cp1252). The tutorial files were clean in every skill, so the damage
        came from whatever wrote INDEX.md.

    All three are retrieval poisoning, the same harm as a promo entry: a
    question routed to the wrong file. All three are cheap to detect exactly.

    NOT checked: INDEX title vs file title. Those differ constantly for
    cosmetic reasons (double spaces, dash style, casing) and flagging them
    would be noise, not signal.
    """
    print("\n[4] Checking INDEX block integrity (identity, PENDING, encoding)...")
    with open(INDEX_PATH, "r", encoding="utf-8-sig") as fh:
        idx = fh.read()

    blocks = re.findall(INDEX_BLOCK_RE, idx)

    # 1. two blocks carrying the same summary -- at most one can be right
    by_summary = {}
    for _title, body, fname in blocks:
        m = re.search(r"- \*\*Summary:\*\*\s*(.+)", body)
        if m:
            by_summary.setdefault(m.group(1).strip(), []).append(fname)
    for summary, files in by_summary.items():
        if len(files) > 1:
            fail(
                f"INDEX.md: {len(files)} entries share one summary, so at most one "
                f"describes its own file ({', '.join(sorted(files))}). Rewrite the "
                f"wrong one(s) FROM THE FILE's own '### Summary' -- never compose "
                f"a summary from memory. Shared text: \"{summary[:70]}...\""
            )

    # 2. leftover placeholders in the retrieval surface
    for _title, body, fname in blocks:
        if "[PENDING" in body:
            fail(
                f"INDEX.md: entry for '{fname}' still has [PENDING] fields. If the "
                f"tutorial file is extracted, its INDEX entry was never updated "
                f"(extraction step 6) -- copy tags/summary across from the file."
            )

    # 3. mojibake
    bad = [i + 1 for i, line in enumerate(idx.split("\n")) if INDEX_MOJIBAKE.search(line)]
    if bad:
        preview = ", ".join(str(n) for n in bad[:6])
        fail(
            f"INDEX.md: {len(bad)} line(s) contain mojibake (UTF-8 read as cp1252, "
            f"e.g. an em-dash as 'a-hat-euro-quote'); first at line {preview}. Repair by "
            f"re-encoding each affected line cp1252 -> utf-8, and verify the "
            f"round-trip rather than guessing."
        )

    print(f"  {len(blocks)} blocks | {len(by_summary)} distinct summaries | "
          f"{len(bad)} mojibake line(s).")


def check_promo():
    """Check #11 -- no un-triaged promotional / no-content entries.

    Scoring lives in scan_promo.py and is imported, never duplicated: the
    scanner is the tool that was tuned against the corpus, and a second copy
    of the rules would drift from it silently.

    Fails ONLY on a candidate that is not in scan_promo.ALLOWLIST. That split
    is the whole design:

      - A candidate requires a SELF-DECLARED signal -- the extraction's own
        prose calling the entry a trailer, an ad, a course announcement.
        Structural signals (short video, thin Key Steps, few named nodes)
        corroborate but never accuse on their own, because that shape is also
        a perfectly good short-form feature tutorial, which is how most plugin
        and add-on documentation is published. Getting this wrong once meant
        flagging a 1-minute tutorial with five concrete steps as an ad.

      - ALLOWLIST is a decision record, not a mute button. Every entry carries
        a written reason (deliberate paywalled gap-filler, series intro chapter
        whose siblings are real, demoted course overview, triaged false
        positive). Adding an entry means recording a decision, and that is the
        intended way to clear this check -- not loosening the scorer.

    A new promo entry therefore fails the build; an already-triaged one does
    not. That is exactly what was missing when tutorials/noise.md sat at the
    top of every noise query for months.
    """
    print("\n[3] Checking for un-triaged promotional / no-content entries...")
    if scan_promo is None:
        print("  SKIPPED: scan_promo.py not importable from this directory.")
        return

    results = scan_promo.scan_all(TUTORIALS_DIR)
    flagged = [r for r in results
               if r["score"] >= scan_promo.CANDIDATE_THRESHOLD
               and r["self_declared"] > 0
               and not r["allowlisted"]]
    for r in flagged:
        reasons = "; ".join(h for h in r["hits"] if h.startswith("notes:")) or "see scan_promo.py --explain"
        fail(
            f"{r['file']}: looks promotional / teaches no technique "
            f"(score {r['score']}) -- {reasons}. Triage it: remove it, demote it "
            f"(fix the INDEX summary + tags), or add it to scan_promo.ALLOWLIST "
            f"with a written reason. `python scan_promo.py --explain {r['file']}`"
        )

    allowed = sum(1 for r in results
                  if r["score"] >= scan_promo.CANDIDATE_THRESHOLD and r["allowlisted"])
    print(f"  Scanned {len(results)} files | {len(flagged)} un-triaged | "
          f"{allowed} allowlisted (decisions on record).")


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


def check_readme_count():
    """Check #13 -- README's "N tutorials ingested" line vs. the real disk count.

    ingest.py::update_readme_tutorial_count() keeps that line honest, but only on
    the paths that call it, and two paths do not. The `skip` / removal path
    git-rm's a tutorial without re-running the counter (paint-me-... over-counted
    by 1 from 2026-08-14), and houdini-wand's course pipeline
    (course_transcribe.py) writes tutorial files and INDEX stubs directly --
    13 Designing Destruction lessons landed with the README still reading 536.
    Both drifts were silent for days because nothing compared the number to the
    files. Same fail-quiet contract as the writer: a reworded or absent line is a
    skip, not a failure.
    """
    print("\n[5] Checking README tutorial count against disk...")
    readme = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")
    if not os.path.isfile(readme):
        print("  No README.md -- skipped.")
        return
    with open(readme, "r", encoding="utf-8") as fh:
        content = fh.read()
    m = re.search(r"\*\*(\d+)\s*tutorials ingested\*\*", content)
    if not m:
        print("  README.md has no '**N tutorials ingested**' line -- skipped.")
        return
    claimed, actual = int(m.group(1)), len(get_tutorial_files())
    if claimed != actual:
        fail(f"README.md says '{claimed} tutorials ingested' but {actual} tutorial "
             f"file(s) are on disk -- re-run ingest.py's update_readme_tutorial_count()")
    print(f"  README claims {claimed} | disk {actual}.")


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
    check_promo()
    check_index_integrity()
    check_readme_count()

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
# The five skills (blender-motion / houdini-wand / unreal-sidekick / nuke-em-all /
# paint-me-like-your-french-substances) deliberately carry copies of the same
# ingest pipeline. Copies have historically drifted (missing UTF-8 fix, mismatched
# cookies flags), so when sibling skill dirs are present on this machine, compare
# the shared helper functions and WARN on differences. Never fails the run —
# per-skill divergence may be intentional, but it should always be a conscious choice.
SIBLING_SKILLS = ("blender-motion", "houdini-wand", "unreal-sidekick", "nuke-em-all", "paint-me-like-your-french-substances")
SHARED_FUNCS = ("slugify", "download_audio", "ytdlp_captions", "segment_by_chapters",
                "_detect_hallucination", "append_safeguard_note", "find_duplicate_by_video_id",
                # added 2026-08-19: the frame-resolution fix must not drift, and
                # this function was silently uncovered while it mattered most.
                "download_video_low", "extract_frames",
                # added 2026-08-20 (A7): the ingest-time promo hint. Its whole
                # value is in staying a WARNING -- a copy that drifts into
                # flagging needs-review would start marking short one-feature
                # plugin tutorials as advertising.
                "promo_hint_at_ingest")


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
