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

import hashlib
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
    """Return video duration in seconds from the '**Duration:** Xm Ys' line, or 0."""
    m = re.search(r"\*\*Duration:\*\*\s+(?:(\d+)h\s*)?(?:(\d+)m\s*)?(?:(\d+)s)?", content)
    if not m:
        return 0
    hours = int(m.group(1) or 0)
    mins = int(m.group(2) or 0)
    secs = int(m.group(3) or 0)
    return hours * 3600 + mins * 60 + secs


def get_transcript_text(content):
    """Return the transcript text from the Raw Data section.

    Returns None when the file carries no transcript at all -- no Raw Data
    section, or the compact "[...raw data omitted...]" marker. Callers must
    treat None ("cannot be checked") differently from "" ("nothing was
    recovered"); check #1 counts the None files rather than skipping silently.
    """
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
    # The header may carry a hand-written suffix ("-- Reviewed", "(reviewed,
    # resolved)") added when a flagged chapter was triaged. Requiring a bare
    # newline after "Report" made the box unstrippable in those files, so its
    # closing "---" was read as the end of Raw Data and a healthy transcript
    # measured as 0 chars -- 2 files failed check #1 with full transcripts on
    # disk. Match any suffix on the header line. (E4, 2026-08-24)
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
    # Coverage counters. The transcript-health test is the most conditional check
    # in this file -- four separate paths skip it -- and until 2026-08-31 it
    # announced only one of them. A clean run therefore looked like "every file
    # was checked" when it could mean "most files were skipped".
    unverifiable = []
    skipped_not_youtube = skipped_short = exempted_ack = transcript_tested = 0
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

        if not is_youtube_source(content):
            skipped_not_youtube += 1
        if is_youtube_source(content):
            notes = get_notes_content(content)
            if len(notes) < NOTES_MIN_CHARS:
                fail(
                    f"{fname}: YouTube source but structured notes are too short "
                    f"({len(notes)} chars, minimum {NOTES_MIN_CHARS})"
                )

            duration_secs = parse_duration_secs(content)
            if duration_secs < TRANSCRIPT_MIN_DURATION_SECS:
                skipped_short += 1
            if duration_secs >= TRANSCRIPT_MIN_DURATION_SECS:
                transcript = get_transcript_text(content)
                if transcript is not None:
                    # Widened 2026-08-31. The original alternation covers only
                    # "we failed to capture it". Two further situations were found
                    # where the transcript is COMPLETE and chars/sec simply does
                    # not apply -- both stated in the file and independently
                    # verifiable, which is the standard the older phrases are held
                    # to. Loosening the threshold instead would blind the check
                    # for every file at once.
                    #   condensed   -- full timestamped transcript moved to a named
                    #                  git commit after extraction (nuke-em-all x2;
                    #                  the commits were checked, 24.7KB and 26.4KB)
                    #   no narration-- silent / music-only time-lapse (paint-me x2;
                    #                  one says so on camera, one re-transcribed at
                    #                  two model sizes returning identical output)
                    no_transcript_ack = bool(re.search(
                        r"transcript\s+(not\s+captured|not\s+available|unavailable|was\s+not\s+captured"
                        r"|could\s+not\s+be\s+captured|quality\s+degrades)"
                        r"|transcript[^.\n]{0,80}\bcondensed\b"
                        r"|\bno\s+narration\b",
                        notes, re.IGNORECASE,
                    ))
                    if no_transcript_ack:
                        exempted_ack += 1
                    if not no_transcript_ack:
                        transcript_tested += 1
                        min_expected = int(duration_secs * TRANSCRIPT_CHARS_PER_SEC)
                        if len(transcript) < min_expected:
                            fail(
                                f"{fname}: transcript appears truncated or empty -- "
                                f"{len(transcript)} chars for a {duration_secs}s video "
                                f"(expected >= {min_expected} chars at "
                                f"{TRANSCRIPT_CHARS_PER_SEC} chars/sec)"
                            )

                else:
                    # No transcript in the file at all (omitted, or no Raw Data
                    # section). check #1 cannot verify these -- count them so the
                    # exemption is a measured number rather than a silent skip.
                    unverifiable.append(fname)
    print(f"  Checked {len(files)} files.")
    # The coverage rule: say what was NOT examined, every run, even at zero.
    print(f"    transcript health tested on {transcript_tested} | not tested: "
          f"{skipped_not_youtube} non-YouTube, {skipped_short} under "
          f"{TRANSCRIPT_MIN_DURATION_SECS}s, {exempted_ack} acknowledged, "
          f"{len(unverifiable)} carry no transcript in-file")


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


# --- check #14 link parsing (widened 2026-08-31) ------------------------------
# The corpus writes cross-links three ways. Kept as module-level helpers so the
# drift checker can watch them alongside check_cross_links itself.
_LINK_MD_RE = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")
_LINK_WIKI_RE = re.compile(r"\[\[([^\]]+)\]\]", re.S)
_LINK_BULLET_RE = re.compile(r"^- .*?\(`([^`]+\.md)`\)", re.M)
_LINK_TICK_AFTER = re.compile(r"\A\s*\(`([^`]+\.md)`\)")
_LINK_RELATED_HEADINGS = ("## Related Tutorials", "## Related Entries")
# Project scaffolding is mentioned in prose and is never a cross-link target.
_LINK_SCAFFOLD = frozenset((
    "INDEX.md", "README.md", "SKILL.md", "SETUP.md", "KNOWLEDGE_GAPS_TODO.md",
    "PROMO_ENTRY_CLEANUP_PLAN.md", "CODE_OF_CONDUCT.md",
))


def _link_norm(x):
    """Collapse whitespace and case, so a wiki-link can match a title across a wrap."""
    return re.sub(r"\s+", " ", x).strip().lower()


def _collect_links(content):
    """Yield (kind, raw_target) for every cross-link in one tutorial file.

    See check_cross_links' docstring for why each form is scoped the way it is.
    """
    for m in _LINK_MD_RE.finditer(content):
        yield "markdown", m.group(2)

    for m in _LINK_WIKI_RE.finditer(content):
        after = _LINK_TICK_AFTER.match(content[m.end():m.end() + 120])
        yield ("bullet", after.group(1)) if after else ("wiki", m.group(1))

    idx = -1
    for heading in _LINK_RELATED_HEADINGS:
        if heading in content:
            idx = content.index(heading)
            break
    if idx >= 0:
        for m in _LINK_BULLET_RE.finditer(content[idx:]):
            yield "bullet", m.group(1)


def check_cross_links():
    """Check #14 -- tutorial cross-links point at files that exist.

    Nothing has ever validated these. A1 found 9 inbound links to a file that was
    about to be deleted and validate.py would have passed with all 9 dangling
    (finding #8); A7 was the slot for this check and shipped the promo gate
    instead. When it was finally measured (E5) there were 7 broken links -- none
    from the A6 removals, which came out clean, but hand-written links whose slug
    never matched a file ("a - b" slugified to "a---b" where ingest.py writes
    "a-b"). Cheap to break, invisible without a check.

    WIDENED 2026-08-31. The v1 regex matched `[Text](file.md)` only, and the
    corpus writes links three ways -- so it saw 1,378 links and was blind to
    1,217 more (47%). unreal-sidekick writes `## Related Entries` with `[[slug]]`
    wiki-links in 352 of its 353 files, so its ENTIRE cross-link graph was
    unvalidated. Seven genuinely broken links were hiding there, and every one of
    them is an inbound link to a file A6 deleted -- exactly the failure mode
    finding #8 named and this check was built to stop. It did not stop it,
    because the removal happened in the one format the check could not read.

    The three forms, each matched against an observed convention:

        markdown  [Text](file.md)        whole file    the only form v1 saw
        wiki      [[slug]] / [[Title]]   whole file    unreal, houdini
        bullet    - Text (`file.md`)     Related only  nuke-em-all, paint-me, unreal

    Two scoping decisions worth keeping:

    * The backtick form is scoped to the Related section. Tutorial prose
      legitimately mentions `KNOWLEDGE_GAPS_TODO.md` and friends in backticks,
      and a whole-file scan reports those as broken links.
    * A wiki-link followed on the same line by a backticked filename resolves
      against THAT filename. houdini writes `[[Truncated Title]] (`real-slug.md`)`
      -- the wiki text is prose, the backtick is the target. Resolving the prose
      produced a false positive on the first pass.

    Wiki-links resolve by slug OR by title (frontmatter `title:`, else the H1),
    because the two skills using them chose different conventions: unreal writes
    slugs, houdini writes titles. Targets in `references/` resolve against the
    references directory -- a link to a reference file that does not exist is
    just as broken, and one such link was misreported as broken on an earlier
    pass precisely because references were not consulted.
    """
    print("\n[6] Checking tutorial cross-links resolve...")
    tut_files = set(get_tutorial_files())
    ref_dir = os.path.join(os.path.dirname(__file__), "references")
    ref_files = set()
    if os.path.isdir(ref_dir):
        ref_files = {f for f in os.listdir(ref_dir)
                     if f.endswith(".md") and f not in _LINK_SCAFFOLD}

    titles = {}
    for d, names in ((TUTORIALS_DIR, tut_files), (ref_dir, ref_files)):
        for f in names:
            try:
                with open(os.path.join(d, f), "r", encoding="utf-8-sig") as fh:
                    text = fh.read()
            except OSError:
                continue
            m = re.search(r"^title:\s*(.+)$", text, re.M)
            if m:
                titles.setdefault(_link_norm(m.group(1).strip().strip("\"'")), f)
            m2 = re.search(r"^#\s+(.+)$", text, re.M)
            if m2:
                titles.setdefault(_link_norm(m2.group(1)), f)

    counts = {"markdown": 0, "wiki": 0, "bullet": 0}
    for fname in sorted(tut_files):
        with open(os.path.join(TUTORIALS_DIR, fname), "r", encoding="utf-8-sig") as fh:
            content = fh.read()
        seen = set()
        for kind, target in _collect_links(content):
            if (kind, target) in seen:
                continue
            seen.add((kind, target))
            counts[kind] += 1
            base = target.split("/")[-1].strip()
            if kind in ("markdown", "bullet"):
                if base in _LINK_SCAFFOLD:
                    continue
                ok = base in tut_files or base in ref_files
            else:
                cand = base[:-3] if base.endswith(".md") else base
                ok = (cand + ".md" in tut_files or cand + ".md" in ref_files
                      or _link_norm(cand) in titles)
            if not ok:
                fail(f"{fname}: {kind} link to '{base[:70]}' but no such tutorial "
                     f"or reference exists")
    total = sum(counts.values())
    print(f"  {total} cross-link(s) checked "
          f"({counts['markdown']} markdown, {counts['wiki']} wiki, {counts['bullet']} bullet).")

REFERENCE_REQUIRED_KEYS = ("class", "verified", "sources", "last_verified")


def _frontmatter(text):
    """Return the leading YAML block, or None if the file has none.

    Deliberately line-based. Splitting on the string "---" looks equivalent and
    is not: several tutorial filenames contain a triple dash
    ("...-houdini---free-lesson.md"), so a sources: list holding one of them cuts
    the frontmatter short and the file reads as missing keys it plainly has.
    That false positive was produced while building this very check (B6).
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return None


def check_reference_provenance():
    """Check #15 -- every references/*.md carries the B2 provenance frontmatter.

    B2 gave all 95 reference files a provenance header so a reader can tell
    ingested knowledge from model memory; nothing enforced it afterwards, so the
    next hand-written reference would silently arrive without one.

    verified: no is REPORTED, never failed. Those files are legitimate -- they
    are model-memory references that honestly say so, and B4/B5 annotated rather
    than deleted them. Counting them keeps the number visible.
    """
    print("\n[7] Checking reference provenance (B2 headers)...")
    ref_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "references")
    if not os.path.isdir(ref_dir):
        print("  No references/ directory -- skipped.")
        return
    files = sorted(f for f in os.listdir(ref_dir) if f.endswith(".md"))
    unverified = []
    for fname in files:
        with open(os.path.join(ref_dir, fname), "r", encoding="utf-8-sig") as fh:
            fm = _frontmatter(fh.read())
        if fm is None:
            fail(f"references/{fname}: no frontmatter block -- needs the B2 provenance header")
            continue
        missing = [k for k in REFERENCE_REQUIRED_KEYS if not re.search(rf"^{k}:", fm, re.M)]
        if missing:
            fail(f"references/{fname}: provenance header missing {', '.join(missing)}")
        if re.search(r"^verified:\s*no\b", fm, re.M):
            unverified.append(fname)
    note = f" | {len(unverified)} marked 'verified: no' (model memory -- not a failure)" if unverified else ""
    print(f"  {len(files)} reference file(s) checked.{note}")
    # The coverage rule: this check reads frontmatter only. It never reads the
    # BODY of a reference file, which is where copernicus.md's invented content
    # lived -- B2 headers say a source was recorded, not that it says this.
    print(f"    not examined: the body of any reference file -- provenance headers only")


def check_frame_provenance():
    """Check #16 -- frame citations in Structured Notes resolve to captured frames.

    D2's mechanism. Extractions already cite frames organically -- 117 files carry
    719 `frame_NNN` references across the five skills -- but nothing checked that
    a cited frame exists. A claim attributed to `frame_012` in a file that
    captured 8 frames is a claim traced to nothing.

    Checked against the file's OWN record (`frame_count`), never against the
    filesystem: frames are gitignored and device-local, so a machine that has not
    downloaded them is not evidence of absence. That is also what makes this
    survive frame deletion, which the images themselves do not.

    Frames are 0-indexed, so a valid citation satisfies index < frame_count.
    """
    print("\n[8] Checking frame provenance in Structured Notes...")
    files = get_tutorial_files()
    citing = citations = 0
    no_notes = no_citations = 0
    for fname in files:
        with open(os.path.join(TUTORIALS_DIR, fname), "r", encoding="utf-8-sig") as fh:
            content = fh.read()
        if "## Structured Notes" not in content:
            no_notes += 1
            continue
        notes = content.split("## Structured Notes")[-1]
        cited = {int(x) for x in re.findall(r"frame_(\d{3})", notes)}
        if not cited:
            no_citations += 1
            continue
        citing += 1
        citations += len(re.findall(r"frame_(\d{3})", notes))
        m = re.search(r"^frame_count:\s*(\d+)", content, re.M)
        if not m:
            fail(f"{fname}: cites frame_{max(cited):03d} but has no frame_count in frontmatter")
            continue
        count = int(m.group(1))
        over = sorted(i for i in cited if i >= count)
        if over:
            shown = ", ".join(f"frame_{i:03d}" for i in over[:4])
            fail(f"{fname}: cites {shown} but frame_count is {count} "
                 f"(frames are 0-indexed -- either the citation or the count is wrong)")
    print(f"  {citations} frame citation(s) across {citing} file(s).")
    # The coverage rule. This check only ever sees files that DO cite a frame,
    # so on its own a clean result says nothing about the rest -- which is the
    # population check #17 exists to watch.
    print(f"    not examined: {no_citations} file(s) cite no frame in their notes"
          f"{f', {no_notes} have no Structured Notes' if no_notes else ''}"
          f" -- see check #17")



# PROMOTED 2026-08-31: the backlog reached zero, so population A now gates.
# It was False from D3 because the check would have landed with 60 pre-existing
# violations across three skills, and a gate that fails on arrival gets ignored
# rather than fixed (plan Gotcha #1: gate LAST). 60 -> 8 over the intervening
# batches; the last 8 were cleared by making their records TRUE rather than by
# inventing data -- frame_count synced to disk and the frames listed WITHOUT
# timestamps, since none was ever recorded and inventing one is the
# moment-choosing D0 rules out. Those frames are 256x144 and are cited nowhere
# in any Structured Notes, because they ground nothing.
GATE_ORPHAN_FRAMES = True



RETRIEVAL_RECHECK_EVERY = 50


def check_retrieval_decay():
    """Check #18 -- re-measure retrieval every 50 ingests, and compare.

    F1 (2026-08-31) established that retrieval quality tracks corpus size: 92-95%
    top-5 in the two smallest libraries against 71% in the two largest. A summary
    that was distinctive at 97 entries stops being distinctive at 584. Nothing was
    watching that, and a one-off measurement does not help -- the number only means
    something next to the previous one.

    Silent until the library grows RETRIEVAL_RECHECK_EVERY entries past the
    recorded baseline, then re-runs and prints the movement. 50 is roughly one
    ingest batch here, so it fires per batch rather than per file.

    WARN-ONLY. Nothing had a baseline when this shipped, so gating would have
    failed all five on arrival -- Gotcha #1, gate LAST.
    """
    print("\n[10] Checking retrieval quality against its baseline...")
    skill = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
    try:
        import retrieval_test as rtst
    except Exception as exc:
        print(f"  not run: retrieval_test.py unavailable ({exc.__class__.__name__})")
        return
    base = rtst.load_baseline(skill)
    now = len(get_tutorial_files())
    if not base:
        print(f"  no baseline recorded -- run: python retrieval_test.py "
              f"--skill {skill} --record")
        return
    grown = now - base.get('entries', 0)
    if grown < RETRIEVAL_RECHECK_EVERY:
        print(f"  baseline {base['entries']} entries, top-5 {base['top5_pct']}% "
              f"({base.get('recorded','?')}) | +{grown} since -- re-measures at "
              f"+{RETRIEVAL_RECHECK_EVERY}")
        return
    # run() prints its own report; silence it so validate's output stays one voice
    import contextlib, io as _io
    with contextlib.redirect_stdout(_io.StringIO()):
        r = rtst.run(skill, 3, 5, False)
    if not r:
        print("  not run: measurement returned nothing")
        return
    top5 = 100 * r['topk'] // max(r['tested'], 1)
    delta = top5 - base['top5_pct']
    arrow = "unchanged" if delta == 0 else ("UP %d pt" % delta if delta > 0 else "DOWN %d pt" % -delta)
    print(f"  +{grown} entries since baseline -- re-measured.")
    print(f"    top-5 {base['top5_pct']}% @ {base['entries']} entries  ->  "
          f"{top5}% @ {r['tested']}   ({arrow})")
    if delta <= -5:
        print(f"    NOTE: retrieval fell {-delta} points as the library grew. "
              f"Expected as a corpus scales; worth knowing, not automatically a defect.")
    print(f"    re-record when reviewed: python retrieval_test.py --skill {skill} --record")


def check_orphan_frames():
    """Check #17 -- frames that exist but are documented nowhere (plan batch D3).

    Two populations, deliberately judged differently, because D3 as originally
    specified ("flag any tutorials/frames/<slug>/ containing images whose .md has
    no Captured Frames section") contradicted D2. D2 checks the file's OWN record
    and never the filesystem, because frames are gitignored and DEVICE-LOCAL --
    a machine that never downloaded them is not evidence of absence. A purely
    filesystem check would be the first one whose result differs per machine,
    passing here and failing on the other device with neither being wrong.

    So:

      A) RECORD-ONLY, machine-independent -- `frame_count > 0` but the file cites
         no `frame_NNN.jpg` anywhere. The record contradicts itself identically on
         every machine, so this is the half that can legitimately gate.

      B) FILESYSTEM -- `tutorials/frames/<slug>/` holds images the .md never
         references. This is the true "orphan" D3 was named for, but it is
         device-local and must NEVER gate. Reported so the population stays
         visible, the same way check #1 prints transcript-less tutorials.

    Measured 2026-08-25 across the five skills, counting BOTH citation forms:
    A = 59 (unreal 57, houdini 1, nuke 1), B = 109 (unreal 57, blender 49,
    houdini 2, nuke 1). Counting only the `.jpg` form gave A = 60 / B = 110
    and falsely flagged the very pair D2 repaired. Note that
    the original wording would have flagged 286 files in unreal-sidekick alone,
    because it assumed one frame-reference format; the older
    `### Title [12:34]` + `**Frame:**` form is equally valid.
    """
    print()
    print("[9] Checking for orphaned / undocumented frames...")
    files = get_tutorial_files()
    claim_no_doc = []
    for fname in files:
        path = os.path.join(TUTORIALS_DIR, fname)
        with open(path, "r", encoding="utf-8-sig") as fh:
            content = fh.read()
        m = re.search(r"^frame_count:\s*(\d+)", content, re.M)
        if not m or int(m.group(1)) == 0:
            continue
        # Both conventions count as documentation: the "## Captured Frames"
        # path form (frame_007.jpg) AND D2's citation form ([frame_007],
        # no extension). Matching only the first falsely flagged the very
        # pair D2 fixed -- the same one-format assumption that made the
        # original D3 spec flag 286 unreal files.
        if not re.search(r"frame_\d{3}", content):
            claim_no_doc.append((fname, int(m.group(1))))

    frames_root = os.path.join(TUTORIALS_DIR, "frames")
    orphan_dirs = []
    if os.path.isdir(frames_root):
        for slug in sorted(os.listdir(frames_root)):
            d = os.path.join(frames_root, slug)
            if not os.path.isdir(d):
                continue
            imgs = [f for f in os.listdir(d) if re.match(r"frame_\d{3}\.jpg$", f)]
            if not imgs:
                continue
            md = os.path.join(TUTORIALS_DIR, slug + ".md")
            if not os.path.exists(md):
                orphan_dirs.append((slug, len(imgs), "no .md at all"))
                continue
            with open(md, "r", encoding="utf-8-sig") as fh:
                if not re.search(r"frame_\d{3}", fh.read()):
                    orphan_dirs.append((slug, len(imgs), "documented nowhere"))

    if claim_no_doc:
        msg = (f"{len(claim_no_doc)} file(s) declare frame_count > 0 but document "
               f"no frame")
        if GATE_ORPHAN_FRAMES:
            for fname, n in claim_no_doc:
                fail(f"{fname}: frame_count is {n} but the file cites no "
                     f"frame at all (neither frame_NNN.jpg nor [frame_NNN])")
        else:
            print(f"  A (record): {msg} -- advisory, not gating yet.")
            for fname, n in claim_no_doc[:5]:
                print(f"      {fname} (frame_count: {n})")
            if len(claim_no_doc) > 5:
                print(f"      ... and {len(claim_no_doc) - 5} more")
    else:
        print("  A (record): none -- every file claiming frames documents at "
              "least one.")
        if not GATE_ORPHAN_FRAMES:
            print("      Backlog is clear: set GATE_ORPHAN_FRAMES = True to gate this.")

    if orphan_dirs:
        total = sum(n for _, n, _ in orphan_dirs)
        print(f"  B (disk):   {len(orphan_dirs)} frame dir(s) holding {total} image(s) "
              f"the .md never references.")
        print("      Device-local (frames are gitignored) -- never gates, and absence "
              "here is not absence on the other machine.")
    else:
        print("  B (disk):   none on this device.")

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
    check_cross_links()
    check_reference_provenance()
    check_frame_provenance()
    check_orphan_frames()
    check_retrieval_decay()

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
                "promo_hint_at_ingest",
                # added 2026-08-24 (E3): the drift checker was watching
                # download_audio() -- the symptom -- while the player-client
                # choice that DICTATES it was invisible. Watch the cause too.
                "_ytdlp_cmd",
                # added 2026-08-24 (D4b): vendor-doc ingest made this
                # consequential -- it decides how much of a doc page is
                # kept and whether navigation chrome crowds it out.
                "fetch_article")

# Recorded intentional divergences. A difference listed here is a decision, not
# drift -- but each is PINNED to the two source variants it was reviewed against
# (sha256[:12] of the function source). Edit either side and the pin stops
# matching, so it reverts to a warning that has to be re-reviewed. An allowlist
# that cannot notice its own subject changing is exactly how this program's false
# positives got their authority -- see PROMO_ENTRY_CLEANUP_PLAN.md finding #2.
RECORDED_DIVERGENCE = {
    "ingest.py::_ytdlp_cmd": {
        "skill": "nuke-em-all",
        "variants": {"b1cd077e6b86", "98c7dfa4f458"},
        "reason": ("nuke-em-all forces the web_embedded player client -- android's "
                   "single muxed itag-18 stream was dying mid-download under "
                   "YouTube's SABR experiment. The other four still work on "
                   "android (verified 2026-08-24), so they were deliberately left "
                   "alone rather than migrated on a working path."),
    },
    "ingest.py::download_audio": {
        "skill": "nuke-em-all",
        "variants": {"cb91e7e62b2c", "0d76f56266c8"},
        "reason": ("consequence of the _ytdlp_cmd split, not an independent edit: "
                   "web_embedded exposes separate audio-only DASH streams, so "
                   "-f bestaudio/best is required there or an unqualified -x "
                   "resolves to bestvideo+bestaudio and downloads a full video "
                   "track just to discard it."),
    },
}


# E5: the drift watch used to cover ingest.py only -- the *pipeline* was
# guarded while the *gate* was not. That is how four skills sat on a broken
# transcript parser (E4) while blender-motion had the fix, with no run ever
# saying so. Watch the checkers too.
WATCHED_FILES = {
    "ingest.py": SHARED_FUNCS,
    "validate.py": ("get_transcript_text", "get_notes_content",
                    "parse_duration_secs", "is_youtube_source",
                    "get_tutorial_files", "parse_index_refs",
                    # added 2026-08-31: check #14 was blind to 47% of the
                    # corpus's links for months because its regex knew one of
                    # three forms. The widened parser is the thing that must
                    # not drift back -- a copy that quietly loses the wiki or
                    # bullet branch re-blinds the check without failing anything.
                    "check_cross_links", "_collect_links", "_link_norm"),
    "scan_promo.py": ("score_file", "get_transcript", "get_notes",
                      "duration_secs", "count_steps", "count_named_things",
                      "series_siblings"),
}


def _srchash(src):
    """Short content hash of a function's source, for pinning recorded divergences."""
    return hashlib.sha256(src.encode("utf-8")).hexdigest()[:12]


def check_script_drift():
    import ast
    here = os.path.dirname(os.path.abspath(__file__))
    skills_root = os.path.dirname(here)
    my_name = os.path.basename(here)

    def func_sources(pyfile, wanted):
        try:
            with open(pyfile, "r", encoding="utf-8") as fh:
                src = fh.read()
            tree = ast.parse(src)
        except Exception:
            return {}
        found = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in wanted:
                found[node.name] = ast.get_source_segment(src, node)
        return found

    warned = False
    noted = set()
    for pyfile, wanted in WATCHED_FILES.items():
        mine = func_sources(os.path.join(here, pyfile), wanted)
        for sib in SIBLING_SKILLS:
            if sib == my_name:
                continue
            sib_path = os.path.join(skills_root, sib, pyfile)
            if not os.path.isfile(sib_path):
                continue
            theirs = func_sources(sib_path, wanted)
            for fn in wanted:
                if fn not in mine or fn not in theirs or mine[fn] == theirs[fn]:
                    continue
                key = f"{pyfile}::{fn}"
                rec = RECORDED_DIVERGENCE.get(key)
                if (rec and rec["skill"] in (my_name, sib)
                        and {_srchash(mine[fn]), _srchash(theirs[fn])} == rec["variants"]):
                    if key not in noted:
                        print(f"  RECORDED DIVERGENCE: {pyfile}::{fn}() differs in "
                              f"'{rec['skill']}' by decision -- {rec['reason']}")
                        noted.add(key)
                    continue
                print(f"  DRIFT WARNING: {pyfile}::{fn}() differs from sibling skill "
                      f"'{sib}' -- if the change was intentional, port it to all skills")
                warned = True
    if not warned:
        extra = f" ({len(noted)} recorded divergence(s) noted above)" if noted else ""
        print(f"  Shared helpers in sync with sibling skills"
              f" (or no siblings installed).{extra}")


if __name__ == "__main__":
    main()
