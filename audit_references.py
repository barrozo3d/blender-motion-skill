#!/usr/bin/env python3
"""
audit_references.py -- corroboration checker for references/*.md.

Automates the method that caught the fabricated `references/copernicus.md` on
2026-08-19: every node/term a reference file asserts is checked against this
skill's own ingested tutorial corpus. Terms the corpus has never once mentioned
are candidate confabulations.

    python audit_references.py                  # audit topic-reference files
    python audit_references.py --all            # include release-notes too
    python audit_references.py --file X.md      # one file
    python audit_references.py --self-test      # houdini-wand only, see below
    python audit_references.py --out report.txt # save the report

WHY THE DEFAULT SKIPS release-notes FILES
    A release-notes file documents features that are brand new by definition, so
    zero tutorial corroboration is EXPECTED and not evidence of fabrication.
    Their provenance is the vendor URL in `sources:` (added in batch B2). Auditing
    them by corroboration would be pure false positives. `topic-reference` files
    are the real risk surface: written from model memory with no source at all.

READING THE OUTPUT
    The headline metric is the ASSERTED ratio -- terms stated in a node-catalog
    table row or a workflow code block, which is where a reference file makes its
    confident claims. Prose mentions are counted separately because generic
    phrasing dilutes the signal. For calibration, the fabricated copernicus.md
    scores 45% asserted (33/74). Treat >=40% as alarming and >=20% as worth a
    look -- but RANK, don't threshold: the point is which file is worst here.

    Context tags rank how confidently the file asserts a term:
      [table] a node-catalog row      -- the most damning place to be wrong
      [code ] a workflow/chain block  -- ditto; this is what gets copy-pasted
      [prose] narrative mention       -- weaker claim

KNOWN FALSE-POSITIVE CLASSES -- check these before cutting anything
    1. PYTHON / SCRIPTING-API references score near the top everywhere
       (nuke-python-scripting.md 90%, substance-painter-python-scripting.md
       100%, python-unreal.md 28%). API symbols are typed, not spoken, so video
       transcripts never contain them. A high score here is expected and is NOT
       evidence of fabrication -- verify against the vendor's API docs instead.
    2. ANALYSIS-FRAMEWORK references (blender-motion's visual-deconstruction.md,
       75%) assert methodology vocabulary the author invented on purpose, not
       product node names. Judge them on usefulness, not corroboration.
    3. GENUINELY NEW features documented from official docs with no tutorial yet
       -- resolve via the `sources:` field rather than by deleting.

KNOWN LIMITATION
    Code-heavy files under-report. CODE_HINT filters out anything containing
    parens/semicolons/operators, so a file that is mostly VEX or Python (e.g.
    vex-library.md) yields very few terms and a meaningless ratio. Absence of a
    finding there is not evidence of correctness -- review those by hand.

NOT A VERDICT. Zero corroboration means "this skill has never seen it", not
"this does not exist". Verify against official docs before cutting: FIX (correct
it, add the doc URL to `sources:`), CUT (unverifiable), or KEEP (real, cite it).
"""

import argparse
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REF_DIR = os.path.join(HERE, "references")
TUT_DIR = os.path.join(HERE, "tutorials")

# Terms too generic for corroboration counting to mean anything.
STOPWORDS = {
    "true", "false", "none", "null", "yes", "no", "on", "off", "and", "or", "not",
    "int", "float", "string", "vector", "matrix", "array", "dict", "list", "bool",
    "x", "y", "z", "w", "u", "v", "r", "g", "b", "a", "rgb", "rgba", "uv", "uvs",
    "in", "out", "input", "output", "value", "name", "type", "mode", "size",
    "scale", "offset", "color", "colour", "alpha", "depth", "time", "frame",
    "min", "max", "sum", "add", "mul", "div", "sub", "if", "else", "for", "while",
}

# A term that looks like code rather than a product/node name.
CODE_HINT = re.compile(r"[(){}\[\];=<>+*/\\@$&|^%!?~]|\.py$|\.md$|\.json$|::|->|\d\.\d")

BACKTICK = re.compile(r"`([^`\n]{2,60})`")
BOLD = re.compile(r"\*\*([^*\n]{2,60})\*\*")
# "- `NodeName` -- description": a node-catalog entry in bullet form.
CATALOG_BULLET = re.compile(r"^[-*]\s+[`*]")

# Fewest asserted terms for a ratio to mean anything (see render()).
MIN_SAMPLE = 8


def is_specific(term):
    """
    True if the term looks like a real product/node NAME rather than a generic
    word. Node names across these five apps are either multi-word ("Noise COP",
    "Bake Geometry Textures") or CamelCase ("ScanlineRender", "MtlXStandardSurface").
    Bare single words -- "Karma", "EXR", "Merge", "blur" -- are ambiguous and
    corroborate trivially, so they are excluded from the headline metric only.
    They still appear in the full report.
    """
    if " " in term:
        return True
    return bool(re.search(r"[a-z][A-Z]", term))  # CamelCase


def load_corpus():
    """Lowercased text of every ingested tutorial (INDEX.md included)."""
    docs = []
    if not os.path.isdir(TUT_DIR):
        return docs
    for name in sorted(os.listdir(TUT_DIR)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(TUT_DIR, name)
        try:
            docs.append(open(path, encoding="utf-8-sig", errors="replace").read().lower())
        except OSError:
            continue
    return docs


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    meta = {}
    for line in text[3:end].split("\n"):
        m = re.match(r"^([a-z_]+):\s*(.*)$", line.strip())
        if m:
            meta[m.group(1)] = m.group(2).strip()
    return meta


def extract_terms(text):
    """{term: context} where context is table | code | prose (strongest wins)."""
    rank = {"table": 3, "code": 2, "prose": 1}
    found = {}
    in_code = False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if stripped.startswith("#") or stripped.startswith("> "):
            pass
        # A "catalog" assertion is a node-list entry. Two formats in the wild:
        # a markdown table row (houdini-wand, unreal-sidekick style) and a
        # bullet led by a backticked name (nuke-em-all, paint-me style:
        # "- `RotoPaint` -- combined roto shapes + paint strokes"). Both are the
        # file confidently cataloguing a node, so both weigh the same. Missing
        # the bullet form emptied the metric in two whole skills.
        if in_code:
            ctx = "code"
        elif stripped.startswith("|") or CATALOG_BULLET.match(stripped):
            ctx = "table"
        else:
            ctx = "prose"

        candidates = BACKTICK.findall(line)
        if not in_code:
            candidates += BOLD.findall(line)
        # inside a fence the whole line is asserted, backticks or not
        if in_code and not candidates and stripped and not stripped.startswith(("#", "//")):
            candidates += re.findall(r"\b([A-Z][A-Za-z0-9]*(?: [A-Z][A-Za-z0-9]*){0,3})\b", line)

        for raw in candidates:
            term = " ".join(raw.split()).strip(" .,:;")
            if len(term) < 3 or term.lower() in STOPWORDS:
                continue
            if CODE_HINT.search(term):
                continue
            if term.isdigit():
                continue
            prev = found.get(term)
            if prev is None or rank[ctx] > rank[prev]:
                found[term] = ctx
    return found


def audit_file(path, corpus):
    text = open(path, encoding="utf-8-sig", errors="replace").read()
    meta = parse_frontmatter(text)
    body = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            body = text[end + 4:]

    terms = extract_terms(body)
    results = []
    for term, ctx in terms.items():
        needle = term.lower()
        hits = sum(1 for d in corpus if needle in d)
        results.append((hits, ctx, term))
    results.sort(key=lambda r: (r[0], {"table": 0, "code": 1, "prose": 2}[r[1]], r[2].lower()))
    return meta, results


def render(path, meta, results, verbose):
    name = os.path.basename(path)
    total = len(results)
    zeros = [r for r in results if r[0] == 0]
    weak = [r for r in results if 1 <= r[0] <= 2]

    # HEADLINE = terms asserted in a node-catalog table row or a workflow code
    # block, where a reference file makes its confident claims. Prose mentions
    # are excluded as noisy section words.
    #
    # No specificity filter here, deliberately. An earlier version also required
    # terms to be multi-word or CamelCase, which is a HOUDINI-SHAPED assumption
    # ("Bake Geometry Textures"). Nuke and Substance node names are single
    # Titlecase words -- Merge, Grade, Roto, Premult -- so that filter emptied
    # the metric entirely in those skills and every file scored a meaningless
    # 0.0%. The specific-only ratio is still reported as a secondary signal.
    strong = [r for r in results if r[1] in ("table", "code")]
    strong_zeros = [r for r in strong if r[0] == 0]
    ratio = (len(strong_zeros) / len(strong) * 100) if strong else 0.0

    spec = [r for r in strong if is_specific(r[2])]
    spec_zeros = [r for r in spec if r[0] == 0]
    spec_ratio = (len(spec_zeros) / len(spec) * 100) if spec else 0.0
    all_ratio = (len(zeros) / total * 100) if total else 0.0

    # Below this many asserted terms a percentage is noise, not signal: 1/1
    # reads as a screaming 100%. Such files are reported but never flagged, so
    # the triage batches are not sent chasing a denominator of two.
    if len(strong) < MIN_SAMPLE:
        flag = "??"
    else:
        flag = "!!" if ratio >= 40 else ("! " if ratio >= 20 else "  ")
    lines = [
        f"\n{flag} === {name} "
        f"(class: {meta.get('class', '?')}, verified: {meta.get('verified', '?')}) ===",
        f"   ASSERTED (table/code): {len(strong_zeros)}/{len(strong)} uncorroborated "
        f"({ratio:.0f}%)   [multi-word/CamelCase only: {len(spec_zeros)}/{len(spec)} "
        f"= {spec_ratio:.0f}%]",
        f"   all terms: {len(zeros)}/{total} ({all_ratio:.0f}%)"
        f"   |   weak (1-2 files): {len(weak)}",
    ]
    show = zeros if verbose else zeros[:25]
    for hits, ctx, term in show:
        lines.append(f"     [{ctx:5s}] {term}")
    if len(zeros) > len(show):
        lines.append(f"     ... and {len(zeros) - len(show)} more (use --verbose)")
    return "\n".join(lines), ratio, len(strong_zeros), len(strong)


def self_test(corpus):
    """
    Recover the pre-quarantine copernicus.md and prove the tool flags it.

    houdini-wand only -- it pins a commit in this repo. In the sibling skills it
    reports that it cannot recover the file and exits; that is expected, not a
    failure of the tool.
    """
    print("SELF-TEST: recovering pre-B1 references/copernicus.md from git history\n")
    try:
        blob = subprocess.run(
            ["git", "-C", HERE, "show", "e1683a1^:references/copernicus.md"],
            capture_output=True, text=True, check=True, encoding="utf-8",
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"  could not recover the old file: {exc}")
        return 1

    tmp = os.path.join(HERE, "_selftest_copernicus.md")
    open(tmp, "w", encoding="utf-8").write(blob)
    try:
        meta, results = audit_file(tmp, corpus)
        report, ratio, zeros, total = render(tmp, meta, results, verbose=False)
        print(report)
        found = {t.lower() for h, _, t in results if h == 0}
        expect = ["noise cop", "ramp cop", "pattern cop", "karma render cop"]
        missing = [e for e in expect if e not in found]
        print("\n  known fabrications flagged:",
              ", ".join(e for e in expect if e in found) or "NONE")
        if missing:
            print("  MISSED:", ", ".join(missing))
        ok = not missing and ratio >= 40
        print(f"\n  RESULT: {'PASS' if ok else 'FAIL'} "
              f"(ratio {ratio:.0f}%, expected >=40% and all known names flagged)")
        return 0 if ok else 1
    finally:
        os.remove(tmp)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="include release-notes files")
    ap.add_argument("--file", help="audit a single reference file")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--verbose", action="store_true", help="list every zero term")
    ap.add_argument("--out", help="also write the report here")
    args = ap.parse_args()

    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    corpus = load_corpus()
    if not corpus:
        print("ERROR: no tutorials found — run from the skill directory.")
        return 1
    print(f"corpus: {len(corpus)} ingested tutorial files\n")

    if args.self_test:
        return self_test(corpus)

    if args.file:
        paths = [os.path.join(REF_DIR, os.path.basename(args.file))]
    else:
        paths = [os.path.join(REF_DIR, n) for n in sorted(os.listdir(REF_DIR))
                 if n.endswith(".md")]

    out, ranking = [], []
    for path in paths:
        meta, results = audit_file(path, corpus)
        cls = meta.get("class", "topic-reference")
        if not args.all and not args.file and cls != "topic-reference":
            continue
        report, ratio, zeros, total = render(path, meta, results, args.verbose)
        out.append(report)
        ranking.append((ratio, zeros, total, os.path.basename(path)))  # zeros,total are strong

    ranking.sort(reverse=True)
    summary = ["\n" + "=" * 70,
               "RANKED BY ZERO-CORROBORATION RATIO (most suspect first)",
               "  calibration: fabricated copernicus.md scores 45% asserted (33/74)",
               "=" * 70]
    scored = [r for r in ranking if r[2] >= MIN_SAMPLE]
    thin = [r for r in ranking if r[2] < MIN_SAMPLE]
    for ratio, zeros, total, name in scored:
        flag = "!!" if ratio >= 40 else ("! " if ratio >= 20 else "  ")
        summary.append(f" {flag} {ratio:5.1f}%  {zeros:4d}/{total:<4d}  {name}")
    if thin:
        summary.append(f"\n  too few asserted terms to score (<{MIN_SAMPLE}) "
                       f"-- review by hand, the ratio would be noise:")
        for ratio, zeros, total, name in thin:
            summary.append(f" ??        {zeros:4d}/{total:<4d}  {name}")

    text = "\n".join(out + summary)
    print(text)
    if args.out:
        open(args.out, "w", encoding="utf-8").write(text)
        print(f"\nwritten to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
