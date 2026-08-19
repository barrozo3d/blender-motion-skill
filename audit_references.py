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
    scores 31% strict-zero (23/74) plus a stem-only review list. Treat >=30% as
    alarming -- but RANK, do not threshold: the point is which file is worst here.

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
    4. PARAMETER / SETTINGS catalogs. The corpus is built from spoken narration,
       so it can corroborate node and tool names (which presenters SAY) but not
       parameter names or default values (which they merely SHOW on screen).
       Measured in unreal-sidekick/chaos-physics.md: the workflow layer
       corroborates -- chaos 30 files, cluster 24, destruction 16 -- while the
       parameter layer does not: "sleep threshold" 0, "differential" 0,
       "substep" 2. Corroboration is simply the wrong instrument for a settings
       table; check those against vendor docs.

    The unifying point behind 1 and 4: a transcript-derived corpus systematically
    lacks anything TYPED or DISPLAYED rather than SPOKEN -- API symbols,
    parameter names, UI labels. Expect those files to score high forever.

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
import functools
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


# Lowercase words allowed inside a product name ("RBD Constraints from Rules").
NAME_CONNECTORS = {"of", "the", "a", "an", "and", "or", "to", "from", "in", "on",
                   "for", "with", "by", "per", "vs", "as", "at"}


def is_prose_fragment(term):
    """
    True if the term is a sentence fragment rather than a name.

    Reference files use **bold** for emphasis as well as for node names, so the
    extractor pulls phrases like "formally deprecated the legacy non-sparse DOP
    nodes" and "no single dedicated built-in SOP". Those can never corroborate,
    so they inflate the uncorroborated ratio with pure noise -- they were most of
    why houdini-18-vs-21-22-changes.md scored 43%.

    Heuristic: real product names are Title Case or CamelCase throughout, apart
    from small connectors. A lowercase word that is not a connector means prose.
    Also caps length -- names are short.
    """
    words = term.split()
    if len(words) > 5:
        return True
    for w in words[1:]:                      # first word may be legitimately odd
        stripped = w.strip("(),.:;-")
        if not stripped:
            continue
        if stripped.islower() and stripped not in NAME_CONNECTORS:
            return True
    return False


def context_stem(term):
    """
    Reference files write formal names with a context suffix ("Rig Doctor SOP");
    tutorials usually say the bare name ("Rig Doctor"). Exact matching therefore
    scores real nodes as zero -- `Rig Doctor SOP` finds 0 files while `Rig Doctor`
    finds 11. Return the stem so that gap is visible.

    The remainder must still be SPECIFIC, which is what stops this from hiding
    real fabrications: "Noise COP" stems to the generic single word "Noise", so
    no stem is returned and it stays at zero, exactly as it should. A stem hit is
    reported SEPARATELY and never counted as corroboration -- "Karma Render COP"
    stems to the real phrase "Karma Render" while the node itself is invented.
    Judge stem-only matches by hand.
    """
    m = re.match(r"^(.*?)\s+(SOP|DOP|LOP|VOP|COP|ROP|CHOP|TOP|node|Node)$", term)
    if not m:
        return None
    stem = m.group(1).strip()
    return stem if len(stem) >= 3 and is_specific(stem) else None


UI_PATH_SEP = re.compile(r"\s*(?:→|->|>|»|\|)\s*")


def ui_path_parts(term):
    """
    Split a UI navigation path into its components.

    Reference files describe settings as paths -- "Bloom → Intensity",
    "Exposure → Exposure Compensation" -- a notation tutorials never use
    verbatim, so exact matching scores every one as fabricated. Measured in
    unreal-sidekick's color-pipeline.md: "Bloom → Intensity" appears in 0 files
    while "Bloom" appears in 25 and "Intensity" in 83. All eight of that file's
    flagged table rows were this artifact.

    Returns the parts only when there are 2+ meaningful ones, so ordinary names
    are unaffected.
    """
    if not UI_PATH_SEP.search(term):
        return None
    parts = [p.strip() for p in UI_PATH_SEP.split(term) if len(p.strip()) >= 3]
    return parts if len(parts) >= 2 else None


def count_files(needle, docs):
    """
    Word-boundary count of files containing `needle`.

    Raw substring matching over-corroborates, and that error runs in the
    DANGEROUS direction: a term that falsely appears corroborated is a
    fabrication the audit stops reporting. Measured on the real corpora,
    "aces" matches 168 files as a substring but 13 as a word -- "surfaces"
    contains it. "Deep" 19 vs 12.
    """
    n = needle.lower()
    pat = _boundary_pat(n)
    # Cheap substring test first: regex over ~550 large documents per term is
    # ~100x slower and times out. Most documents fail the substring test, so the
    # regex only runs on the few that could actually match.
    return sum(1 for d in docs if n in d and pat.search(d))


@functools.lru_cache(maxsize=4096)
def _boundary_pat(n):
    return re.compile(r"(?<![a-z0-9])" + re.escape(n) + r"(?![a-z0-9])")


# Filename words too generic to identify a topic.
TOPIC_NOISE = {"reference", "nodes", "node", "pipeline", "guide", "overview",
               "library", "catalog", "changes", "versions", "release", "notes",
               "scripting", "theory", "tracker", "and", "vs", "for", "the"}


def topic_coverage(filename, corpus):
    """
    How many corpus files talk about this reference file's SUBJECT at all.

    Without this the ratio is uninterpretable. A file scores high either because
    it is fabricated or because the library simply never covers its topic, and
    those demand opposite responses. Measured: unreal-sidekick's
    sequencer-cinematics.md scores 0% against 155 files mentioning "sequencer",
    while lip-sync.md scores 50% against 7 mentioning "lip sync". The second
    number is not evidence of fabrication -- it is evidence of a blind spot.

    copernicus.md was catchable precisely BECAUSE coverage was high: 69 files
    discuss Copernicus, and the names were still absent.
    """
    stem = os.path.basename(filename)[:-3]
    words = [w for w in stem.split("-") if w and w.lower() not in TOPIC_NOISE]
    if not words:
        return None      # topic undeterminable from the filename -- NOT "thin"
    # A token matching most of the corpus identifies no topic -- it is the app's
    # own name. "houdini-workflow.md" matched "houdini" and reported coverage of
    # the entire 546-file library; "nuke-compositing-nodes.md" likewise. Such a
    # number silently reads as "richly covered" and would excuse a real problem.
    ceiling = max(1, int(len(corpus) * 0.8))
    usable = [w for w in words if len(w) >= 3]
    if not usable:
        return None

    # Use the LEAST-common filename token, never the most and never the literal
    # joined phrase. Both alternatives were tried and both mislead:
    #   max()  -- a generic token inflates it. lip-sync.md read 58, which was the
    #             everyday word "sync"; that promotes a blind spot into a
    #             "fabrication signature", the most dangerous direction.
    #   joined -- a filename means "topic A AND topic B", not a literal phrase.
    #             sequencer-cinematics.md read 2 for the exact phrase while
    #             "sequencer" alone appears in 155 files, which would excuse a
    #             genuinely bad file as merely uncovered.
    # The rarest token bounds how much the corpus can say about the narrower of
    # the file's two subjects, which is the honest estimate.
    counts = [c for c in (count_files(w, corpus) for w in usable) if c <= ceiling]
    if not counts:
        return None                      # every token app-generic: undeterminable
    return min(counts)


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


def load_release_notes():
    """
    Secondary corroboration source: the release-notes references.

    Those files are `verified: partial` and cite official vendor changelog URLs,
    so a term appearing there IS corroborated -- by the vendor, not by a tutorial.
    This matters for version-delta and new-feature files, whose content comes
    from release notes and which the tutorial corpus therefore cannot confirm.
    Concretely: houdini-18-vs-21-22-changes.md asserts shelf tools like
    "Aerial Barrage" and "Ground Shockwave" that appear in ZERO tutorials but ARE
    in the H2x release notes -- scoring them as fabrication was simply the wrong
    yardstick.
    """
    docs = []
    if not os.path.isdir(REF_DIR):
        return docs
    for name in sorted(os.listdir(REF_DIR)):
        if not name.startswith("release-notes-") or not name.endswith(".md"):
            continue
        try:
            docs.append(open(os.path.join(REF_DIR, name),
                             encoding="utf-8-sig", errors="replace").read().lower())
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
            if is_prose_fragment(term):
                continue
            prev = found.get(term)
            if prev is None or rank[ctx] > rank[prev]:
                found[term] = ctx
    return found


def audit_file(path, corpus, notes):
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
        hits = count_files(needle, corpus)
        stem_hits = 0
        stem = context_stem(term)
        if hits == 0 and stem:
            s = stem.lower()
            stem_hits = count_files(s, corpus)
        if hits == 0 and stem_hits == 0:
            # UI path like "Bloom -> Intensity": corroborated when EVERY
            # component is. Reported in the review bucket, not as a hit.
            parts = ui_path_parts(term)
            if parts:
                counts = [count_files(x, corpus) for x in parts]
                if all(c > 0 for c in counts):
                    stem_hits = min(counts)
        # vendor release notes corroborate too -- see load_release_notes()
        if hits == 0:
            hits = -count_files(needle, notes)
        results.append((hits, ctx, term, stem_hits))
    results.sort(key=lambda r: (r[0] + r[3], r[0],
                                {"table": 0, "code": 1, "prose": 2}[r[1]], r[2].lower()))
    return meta, results


def render(path, meta, results, verbose, coverage=None):
    name = os.path.basename(path)
    total = len(results)
    # A term is only "uncorroborated" if BOTH the exact name and its stem
    # are absent. Stem-only hits are surfaced separately for hand review.
    zeros = [r for r in results if r[0] == 0 and r[3] == 0]
    rn_only = [r for r in results if r[0] < 0]
    stem_only = [r for r in results if r[0] == 0 and r[3] > 0]
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
    strong_zeros = [r for r in strong if r[0] == 0 and r[3] == 0]
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
        f"   topic coverage: "
        f"{'undetermined' if coverage is None else str(coverage) + ' corpus files'}"
        f"{'  <-- TOO THIN to judge by corroboration' if (coverage is not None and coverage < 15) else ''}",
        f"   all terms: {len(zeros)}/{total} ({all_ratio:.0f}%)"
        f"   |   weak (1-2 files): {len(weak)}"
        f"   |   stem-only: {len(stem_only)}"
        f"   |   release-notes-only: {len(rn_only)}",
    ]
    show = zeros if verbose else zeros[:25]
    for hits, ctx, term, _sh in show:
        lines.append(f"     [{ctx:5s}] {term}")
    if len(zeros) > len(show):
        lines.append(f"     ... and {len(zeros) - len(show)} more (use --verbose)")
    if stem_only:
        lines.append("   -- stem matches only (likely the formal-suffix"
                     " convention, verify before cutting):")
        for hits, ctx, term, sh in (stem_only if verbose else stem_only[:12]):
            lines.append(f"     [{ctx:5s}] {term}  -> stem in {sh} files")
        if len(stem_only) > 12 and not verbose:
            lines.append(f"     ... and {len(stem_only) - 12} more")
    return "\n".join(lines), ratio, len(strong_zeros), len(strong)


def self_test(corpus, notes):
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
        meta, results = audit_file(tmp, corpus, notes)
        report, ratio, zeros, total = render(tmp, meta, results, False,
                                             topic_coverage('copernicus.md', corpus))
        print(report)
        # A fabrication counts as caught if it lands in EITHER review bucket.
        # "Karma Render COP" deliberately lands in stem-only: its stem "Karma
        # Render" is a real phrase that does occur in the corpus, so strict
        # zero-matching cannot see it. That is the documented cost of stem
        # matching, and the reason stem-only is surfaced rather than silently
        # treated as corroborated.
        zero_set = {t.lower() for h, _c, t, sh in results if h == 0 and sh == 0}
        stem_set = {t.lower() for h, _c, t, sh in results if h == 0 and sh > 0}
        found = zero_set | stem_set
        expect = ["noise cop", "ramp cop", "pattern cop", "karma render cop"]
        missing = [e for e in expect if e not in found]
        print(f"\n  in zero-corroboration: "
              f"{', '.join(e for e in expect if e in zero_set) or 'none'}")
        print(f"  in stem-only review:   "
              f"{', '.join(e for e in expect if e in stem_set) or 'none'}")
        print("\n  known fabrications flagged:",
              ", ".join(e for e in expect if e in found) or "NONE")
        if missing:
            print("  MISSED:", ", ".join(missing))
        ok = not missing and ratio >= 30
        print(f"\n  RESULT: {'PASS' if ok else 'FAIL'} "
              f"(ratio {ratio:.0f}%, expected >=30% and all known names in one "
              f"of the two review buckets)")
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
    notes = load_release_notes()
    if not corpus:
        print("ERROR: no tutorials found — run from the skill directory.")
        return 1
    print(f"corpus: {len(corpus)} tutorial files + {len(notes)} release-notes refs\n")

    if args.self_test:
        return self_test(corpus, notes)

    if args.file:
        paths = [os.path.join(REF_DIR, os.path.basename(args.file))]
    else:
        paths = [os.path.join(REF_DIR, n) for n in sorted(os.listdir(REF_DIR))
                 if n.endswith(".md")]

    out, ranking = [], []
    for path in paths:
        meta, results = audit_file(path, corpus, notes)
        cls = meta.get("class", "topic-reference")
        if not args.all and not args.file and cls != "topic-reference":
            continue
        cov = topic_coverage(path, corpus)
        report, ratio, zeros, total = render(path, meta, results, args.verbose, cov)
        out.append(report)
        ranking.append((ratio, zeros, total, os.path.basename(path), cov))

    ranking.sort(reverse=True)
    summary = ["\n" + "=" * 70,
               "RANKED BY ZERO-CORROBORATION RATIO (most suspect first)",
               "  calibration: fabricated copernicus.md scores 31% strict-zero (23/74)",
               "=" * 70]
    scored = [r for r in ranking if r[2] >= MIN_SAMPLE]
    thin = [r for r in ranking if r[2] < MIN_SAMPLE]
    for ratio, zeros, total, name, cov in scored:
        # NB: not `thin` -- that name holds the low-sample file list below.
        thin_cov = cov is not None and cov < 15
        flag = "??" if thin_cov else ("!!" if ratio >= 40 else ("! " if ratio >= 20 else "  "))
        note = "  (thin coverage -- unmeasurable, verify vs docs)" if thin_cov else (
               "  (topic undetermined from filename)" if cov is None else "")
        covs = "n/a " if cov is None else f"{cov:<4d}"
        summary.append(f" {flag} {ratio:5.1f}%  {zeros:4d}/{total:<4d}  cov={covs} {name}{note}")
    if thin:
        summary.append(f"\n  too few asserted terms to score (<{MIN_SAMPLE}) "
                       f"-- review by hand, the ratio would be noise:")
        for ratio, zeros, total, name, cov in thin:
            covs = "n/a " if cov is None else f"{cov:<4d}"
            summary.append(f" ??        {zeros:4d}/{total:<4d}  cov={covs} {name}")

    text = "\n".join(out + summary)
    print(text)
    if args.out:
        open(args.out, "w", encoding="utf-8").write(text)
        print(f"\nwritten to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
