#!/usr/bin/env python3
"""
update_index_entry.py -- rewrite ONE INDEX.md block from its own tutorial file.

    python update_index_entry.py <slug> --from-file      # new entry: fields from file
    python update_index_entry.py <slug> --set 'Tags=a, b' # set one field exactly
    python update_index_entry.py <slug> --summary        # repair a wrong Summary
    python update_index_entry.py --all --check           # report differences only

    Several slugs may be given: each is edited as its OWN block. A batch is N
    single-block edits, never one whole-file regeneration.

Use this for Mode 3 step 6 ("Update INDEX.md entry"). **Never rewrite INDEX.md
wholesale.**

WHY THIS EXISTS
    On 2026-08-20 an audit found INDEX blocks that described a *different
    tutorial* -- tutorials/liquid-sops.md (solver-free SOP liquids) was indexed
    under a molecular-visualisation course's tags and summary -- plus 95 lines
    of mojibake, plus a fully extracted tutorial whose block was still
    [PENDING]. `git blame` traced every case to the same thing: the extract step
    regenerating the WHOLE index instead of editing the one block it owned.

      8d41a61  "extract: Dash batch 6"   5 tutorials -> 174 INDEX lines rewritten,
                                         including line 1, the file's own title
      cac23a7  single-tutorial extract   INDEX.md -1031 / +72
      7233d17  4-tutorial extract        same summary line written into 3 blocks
      276a8cf  7-tutorial extract        1148 INDEX lines rewritten

    Two failure modes, one cause. Passing the entire file through an ad-hoc
    read/write damages lines nobody was editing (on Windows, PowerShell's
    Set-Content/Out-File default to the ANSI code page, and a UTF-8 -> cp1252
    round-trip produces exactly that mojibake). Regenerating many blocks at once
    lets a summary land in the wrong block -- the blast radius equals the batch
    size.

    This script makes both impossible. It touches exactly the requested blocks,
    it always reads and writes UTF-8 explicitly, and every value it writes is
    COPIED FROM THE TUTORIAL FILE -- never composed. Those blocks were corrupt
    precisely because someone once put text in them that did not come from the
    file; fixing or writing them with fresh prose repeats the original mistake.

    validate.py check #12 catches recurrence. This prevents it.

WHAT THIS TOOL IS NOT
    It is NOT a "sync INDEX from the files" tool, and building one would be a
    mistake. INDEX values are deliberately CONDENSED editorial versions of the
    frontmatter, and sometimes richer than it:

        file  houdini_version: "Houdini 22.0 (Otis Muscle and Tissue System);
                                Legacy Vellum-based muscles/tissue also..."
        INDEX Houdini Version: Houdini 22.0 (Otis system); Legacy Vellum
                               muscles/tissue also documented

        file  author: Fx Guru
        INDEX Author: Fx Guru (Arbaaj)          <- INDEX knows more

    A blanket sync would flatten the first and destroy the second. Measured over
    536 entries: a naive summary sync reported 527 "drifted" (they are curated
    paraphrases, not truncations), and a naive tag sync reported 78 when 70+ held
    the identical tag SET in different punctuation.

    So writing requires an explicit --from-file, --summary or --set, --all is
    check-only, and --check reports DIFFERENCES -- most of which are intentional
    condensation, not errors. Read them; do not bulk-apply them.
"""

import argparse
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TUTORIALS_DIR = os.path.join(HERE, "tutorials")
INDEX_PATH = os.path.join(TUTORIALS_DIR, "INDEX.md")

SUMMARY_LIMIT = 420

# Frontmatter key -> INDEX label. Skills name these differently; only the keys
# present in a given file are used, so one table serves all five.
FIELD_MAP = [
    ("url", "URL"),
    ("author", "Author"),
    ("app", "App"),
    ("houdini_version", "Houdini Version"),
    ("blender_version", "Blender Version"),
    ("ue_version", "UE Version"),
    ("version", "Version"),
]


def read(path):
    with io.open(path, encoding="utf-8-sig") as fh:
        return fh.read()


def write(path, text):
    # Explicit UTF-8, no BOM, newline="" so existing line endings are preserved
    # verbatim. This is the half that stops mojibake ever being written.
    with io.open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def frontmatter(text, key):
    m = re.search(r"^%s:\s*(.+)$" % re.escape(key), text, re.M)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def file_tags(text):
    m = re.search(r"^tags:\s*\[(.*?)\]", text, re.M | re.S)
    if not m:
        return None
    out = []
    for raw in m.group(1).split(","):
        t = raw.strip().strip('"').strip("'").strip()
        if t:
            out.append(t)
    return ", ".join(out) or None


def file_summary(text):
    """The tutorial's own '### Summary', truncated at a word boundary.

    Falls back to '### Core Technique' when Summary opens with a bold
    sub-header, which reads as a fragment in an index.
    """
    for heading in ("Summary", "Core Technique"):
        m = re.search(r"### %s\n(.+?)(?=\n### |\n---)" % heading, text, re.DOTALL)
        if not m:
            continue
        txt = " ".join(m.group(1).split())
        if heading == "Summary" and txt.startswith("**"):
            continue          # try Core Technique instead
        if not txt:
            continue
        if len(txt) <= SUMMARY_LIMIT:
            return txt
        return txt[:SUMMARY_LIMIT].rsplit(" ", 1)[0] + "..."
    return None


def tag_set(text):
    """Tags as a comparable set, ignoring presentation.

    The corpus renders tags three ways -- `"quoted", "list"`, `bare, list`, and
    `` `#hashtag` `` -- and INDEX blocks do not always match their file's style.
    Comparing raw strings reported 78 entries as drifted when 70+ of them held
    the identical tag SET in different punctuation. Compare meaning, not markup.
    """
    return set(
        t for t in (
            x.strip().strip('"').strip("'").strip("`").lstrip("#").strip().lower()
            for x in re.split(r"[,\s]+", text or "")
        ) if t
    )


def render_tags(tags_csv, existing_line):
    """Render tags in ONE style: comma-separated, bare.

    ⚠️ This used to preserve whatever style the block already had -- emitting
    `#tag` `#tag` for a backtick+hash block, "tag", "tag" for a quoted one. The
    intent was kind (don't churn blocks you are only lightly editing) and the
    effect was that FIVE styles became self-perpetuating: nothing could ever
    converge, because every edit re-emitted the old form.

    Measured 2026-09-03 over 1488 INDEX entries: comma 978, backtick+hash 224,
    hash 187, backtick 97. Meanwhile all 1481 TUTORIAL FILES use a single style
    (`tags: [a, b]`) with zero exceptions -- so the variation was never a corpus
    taxonomy anyone chose, only drift in a derived field.

    🔴 The cost was silent and real: each consumer of this line has to
    rediscover every style or misread part of the corpus, and one did.
    `retrieval_test.py` split on commas alone, so 508 entries -- 34%, and 100%
    of paint-me -- contributed ZERO domain vocabulary while the run printed a
    confident score. `retrieval_reachable.py` had a third, differently-wrong
    parser. Two tools disagreeing about what a tag is, on the same corpus.

    `existing_line` is kept in the signature: callers pass it, and it is the
    natural hook if a style ever has to be honoured again. It is deliberately
    unused.
    """
    tags = [t.strip().strip("`").lstrip("#").strip("`").strip('"')
            for t in tags_csv.split(",")]
    return ", ".join(t for t in tags if t)


def block_re(slug):
    return re.compile(
        r"(### [^\n]*\n(?:- \*\*[^\n]*\n)*?)- \*\*File:\*\* tutorials/"
        + re.escape(slug) + r"\.md")


def desired_fields(tut, with_summary):
    """Fields this tool is willing to write.

    Summary is EXCLUDED by default, and that is deliberate. INDEX summaries are
    curated paraphrases, not mechanical truncations of the file's own Summary --
    running a truncation over the whole corpus reported 527 of 536 entries as
    "drifted" and would have replaced 527 good hand-written summaries with worse
    machine-cut ones. That is the same wholesale-overwrite mistake this script
    exists to prevent, just automated.

    So: mechanical fields (URL, author, version, tags) are safe to sync, because
    they have exactly one correct value and it lives in the frontmatter. The
    summary is only rewritten when explicitly asked for with --summary, which is
    the repair case: a block proven to describe the wrong tutorial.
    """
    fields = {}
    tags = file_tags(tut)
    if tags:
        fields["Tags"] = tags
    if with_summary:
        summary = file_summary(tut)
        if summary:
            fields["Summary"] = summary
    for key, label in FIELD_MAP:
        val = frontmatter(tut, key)
        if val:
            fields[label] = val
    return fields


def update_one(idx, slug, check, with_summary, from_file, overrides):
    """Return (idx, changed_labels, error)."""
    path = os.path.join(TUTORIALS_DIR, slug + ".md")
    if not os.path.isfile(path):
        return idx, [], "no such tutorial file"
    m = block_re(slug).search(idx)
    if not m:
        return idx, [], "no INDEX block"

    tut = read(path)
    body = m.group(1)
    changed = []
    # In --check we always derive the file's values so there is something to
    # compare; writing still requires an explicit --from-file/--summary/--set.
    wanted = (desired_fields(tut, with_summary)
              if (from_file or with_summary or check) else {})
    wanted.update(overrides)
    for label, value in wanted.items():
        line_re = re.compile(r"- \*\*%s:\*\*[^\n]*\n" % re.escape(label))
        current = line_re.search(body)
        if not current:
            continue          # only fields the block already has
        current_line = current.group(0)
        if label == "Tags":
            # ⚠️ This used to `continue` whenever the tag SETS matched, so a
            # block keeping the same tags in a different punctuation style
            # was never rewritten. Together with a style-preserving
            # render_tags that made the corpus's five styles permanent:
            # nothing could converge, because every edit either skipped or
            # re-emitted the old form. The `current_line == new_line` test
            # below is the correct guard -- it still suppresses genuine
            # no-ops while letting a pure style change through.
            new_line = "- **Tags:** %s\n" % render_tags(value, current_line)
        else:
            new_line = "- **%s:** %s\n" % (label, value)
        if current_line == new_line:
            continue
        changed.append(label)
        if not check:
            body = line_re.sub(lambda _m: new_line, body, count=1)
    if changed and not check:
        idx = idx[:m.start(1)] + body + idx[m.end(1):]
    return idx, changed, None


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slugs", nargs="*", help="tutorial slug(s), without .md")
    ap.add_argument("--all", action="store_true", help="every tutorial on disk")
    ap.add_argument("--check", action="store_true",
                    help="report drift, write nothing")
    ap.add_argument("--from-file", action="store_true",
                    help="write the mechanical fields (tags/url/author/version) "
                         "from the tutorial file. For NEW entries; see 'WHAT THIS "
                         "TOOL IS NOT' before using it on curated ones")
    ap.add_argument("--set", action="append", default=[], metavar="LABEL=VALUE",
                    help="set one INDEX field explicitly, e.g. --set 'Tags=a, b'")
    ap.add_argument("--summary", action="store_true",
                    help="ALSO rewrite the Summary from the file. Repair only -- "
                         "INDEX summaries are curated, not mechanical truncations")
    args = ap.parse_args()

    slugs = list(args.slugs)
    if args.all:
        slugs = [f[:-3] for f in sorted(os.listdir(TUTORIALS_DIR))
                 if f.endswith(".md") and f != "INDEX.md"]
    if not slugs:
        ap.error("give at least one slug, or --all")
    if args.all and not args.check:
        ap.error("--all is check-only: this tool never bulk-rewrites INDEX.md. "
                 "That is the failure it exists to prevent.")
    if not (args.check or args.from_file or args.summary or args.set):
        ap.error("nothing to do: pass --from-file, --summary, --set or --check")

    overrides = {}
    for pair in args.set:
        if "=" not in pair:
            ap.error("--set expects LABEL=VALUE, got %r" % pair)
        k, v = pair.split("=", 1)
        overrides[k.strip()] = v.strip()

    idx = read(INDEX_PATH)
    original = idx
    touched = errors = 0
    for slug in slugs:
        slug = slug[:-3] if slug.endswith(".md") else slug
        idx, changed, err = update_one(idx, slug, args.check,
                                       args.summary, args.from_file, overrides)
        if err:
            errors += 1
            print("  ERROR %s: %s" % (slug, err))
        elif changed:
            touched += 1
            print("  %s %s: %s" % ("would update" if args.check else "updated",
                                   slug, ", ".join(changed)))

    if args.check:
        print("\n%d entr%s DIFFER from their file(s); nothing written."
              % (touched, "y" if touched == 1 else "ies"))
        if touched:
            print("Most differences are intentional editorial condensation, not "
                  "errors\n(the INDEX is deliberately terser, and sometimes knows "
                  "more).\nRead them individually; never bulk-apply.")
    elif idx != original:
        write(INDEX_PATH, idx)
        print("\n%d entr%s rewritten in INDEX.md (only those blocks)."
              % (touched, "y" if touched == 1 else "ies"))
    else:
        print("\nNothing to change.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
