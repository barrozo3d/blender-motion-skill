#!/usr/bin/env python3
"""
hapax_scan.py — the corpus as arbiter (ULTIMATE_PIPELINE_PLAN.md §3.7 item 5).

A rare technical term or proper noun that appears EXACTLY ONCE across the whole
corpus, while a near neighbour appears often, is a mishear candidate. This is the
mechanised form of a check that was already being done by hand: *"Main in Black"*
was settled by grepping the corpus, where wk6-03 names the film.

⚠️ THIS DETECTOR GETS STRONGER AS THE CORPUS GROWS — the only one in the plan
that does. Every new ingest makes "appears exactly once" a sharper statement.

⚠️ AND ITS LIMIT, stated plainly because it is easy to over-trust: it CANNOT
catch a CONSISTENT mishear. This speaker's "sim" -> "seam" ran through an entire
115-lesson course, so "seam" is no hapax — it is common, and this scan sees
nothing. Consistent substitutions stay read-only territory. Nothing here replaces
the read-through.

⚠️ A hit is a REASON TO LOOK, never a verdict (§3.4: the flag list is not the
defect list). Rare terms are often simply rare and correct — a node used in one
tutorial, a plugin named once, a version string.

Usage:
    python hapax_scan.py                  # scan this skill's corpus
    python hapax_scan.py --min-ratio 20   # stricter: neighbour must be 20x commoner
    python hapax_scan.py --limit 40
    python hapax_scan.py --term Voronoi    # why was/wasn't this flagged?
"""

import argparse
import difflib
import os
import re
import sys
from collections import defaultdict

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
TUTORIALS_DIR = os.path.join(SKILL_DIR, "tutorials")

# A candidate must look like a TERM, not prose. Ordinary lowercase words are
# excluded outright: they are the corpus's bulk, they are what the language model
# already handles, and including them buries the signal.
TERM_RE = re.compile(r"\b[A-Za-z][A-Za-z0-9_.-]{3,29}\b")

# Tuned to keep this a pointer rather than a second flag storm.
MIN_TERM_LEN = 5          # shorter tokens collide constantly
DEFAULT_MIN_RATIO = 12    # neighbour must be this many times commoner
DEFAULT_CUTOFF = 0.86     # fuzzy-match threshold, hapax mode
# ⚠️ --variants needs a LOOSER cutoff than hapax mode, measured on the real
# corpus 2026-09-03. At 0.86 it misses "Odini"~"Houdini" (similarity 0.833) --
# 75 occurrences of this skill's own subject, and the case the mode was built
# for. At 0.83 it finds 14 candidates / 160 occurrences with one clear false
# positive ("Though"~"Although"). At 0.80 it collapses: "Light"~"Right",
# "Think"~"Thank", "Might"~"Right" are ordinary English, not mishears.
# 0.83 is the measured knee, not a guess.
DEFAULT_VARIANT_CUTOFF = 0.83
SUFFIX_TOLERANCE = 3      # "attributes"~"attribute" is usage, not a mishear

# Words that are technical-looking but are corpus furniture, not vocabulary.
STOPWORDS = {
    "https", "youtube", "watch", "video", "tutorial", "channel", "about",
    "there", "which", "these", "those", "their", "would", "could", "should",
    "where", "while", "after", "before", "because", "through", "between",
    "using", "makes", "make", "just", "like", "into", "onto", "with", "from",
    "this", "that", "then", "than", "have", "here", "your", "what", "when",
    "some", "more", "most", "very", "also", "into", "over", "under", "again",
    "going", "want", "need", "know", "look", "looks", "little", "really",
    "actually", "basically", "something", "everything", "anything", "different",
    "pending", "complete", "extraction", "status", "frames", "frame", "index",
    "title", "source", "author", "ingested", "duration", "section", "sections",
    "transcript", "structured", "notes", "safeguard", "report", "warning",
}


def looks_technical(tok):
    """Capitalised, ALLCAPS, or digit-bearing.

    ⚠️ A first draft required an INTERNAL capital (CamelCase), which collapsed
    the corpus to 513 terms across 614 files and found nothing — because a
    transcript is prose, and a proper noun in prose is "Houdini", not "HouDini".
    Plain capitalisation is exactly the class this scan exists for: *"Main in
    Black"* is three ordinary capitalised words. The cost is sentence-initial
    noise, which STOPWORDS and the frequency filter absorb — an ordinary word
    like "There" is common, so it lands as a NEIGHBOUR, never as a hapax."""
    if any(c.isdigit() for c in tok):
        return True
    if tok.isupper() and len(tok) >= 2:
        return True
    return tok[0].isupper()


# Real English morphology. The affix suppression is restricted to THESE rather
# than to "any short prefix/suffix", for a measured reason -- see below.
PREFIXES = ("de", "dis", "in", "im", "un", "re", "an", "al", "pre", "non", "over")
SUFFIXES = ("s", "es", "d", "ed", "ing", "er", "ers", "ly", "y", "ion", "al")


def _is_affix_variant(a, b):
    """True when one term is the other plus a REAL morphological affix.

    ⚠️ Two corrections are baked in here, both measured, and the second undid
    most of the first:

    1. A first version checked only PREFIXES, and four of six false positives
       across the five corpora were the mirror case -- "Deselect"~"Select",
       "Crease"~"Increase", "Other"~"Another". Suffixes had to be checked too.

    2. But checking ANY short suffix silently DELETED a real finding:
       "houdini".endswith("udini") is True, so "Udini" -- 40 occurrences of this
       skill's own subject with the "Ho" dropped -- was suppressed as
       morphology. It is a truncated proper noun, not a stem plus a particle.

    A generic edit-distance test cannot tell those apart. A list of actual
    English affixes can: "ho" is not one, "de"/"in"/"an" are. Precision without
    losing the case the mode exists for."""
    x, y = sorted([a.lower(), b.lower()], key=len)
    gap = len(y) - len(x)
    if gap == 0 or gap > SUFFIX_TOLERANCE:
        return False
    if y.startswith(x) and y[len(x):] in SUFFIXES:
        return True
    if y.endswith(x) and y[:gap] in PREFIXES:
        return True
    return False

def get_transcript(content):
    start = content.find("## Raw Data")
    if start == -1:
        return ""
    raw = content[start:]
    split = re.search(r"\n## Structured Notes", raw)
    if split:
        raw = raw[:split.start()]
    raw = re.sub(r"\n## Ingest Safeguard Report[^\n]*\n.*?\n---\n", "\n", raw, flags=re.DOTALL)
    out = []
    for line in raw.splitlines():
        s = line.strip()
        if s.startswith("**Transcript:**"):
            out.append(s[len("**Transcript:**"):].strip())
        elif re.match(r"\[\d+:\d{2}\] ", s):
            out.append(s.split("] ", 1)[1])
    return " ".join(out)


def get_notes(content):
    m = re.search(r"## Structured Notes(.+)", content, re.DOTALL)
    return m.group(1) if m else ""


def build_index():
    """term -> {"total": n, "notes": n, "files": {name: n}} per tutorial.

    ⚠️ `notes` is tracked separately because SEVERITY DIFFERS ENORMOUSLY, and a
    scan that conflates them misleads. Measured 2026-09-03: the Houdini mishear
    family had **145 occurrences in raw transcripts and 2 in Structured Notes**,
    and both of those two were deliberate quotations of the transcript with the
    correct reading given alongside (*'mentions "I believe in Odini 20"; UI
    matches Houdini 20-era look'*).

    A hit confined to the raw transcript is cosmetic: the transcript is a
    verbatim record of what Whisper emitted, and the extraction read-through
    already corrected it downstream. A hit in the NOTES is a real defect -- that
    is the durable knowledge the corpus is for. Report both, and never quote the
    raw count alone as if it were damage."""
    index = defaultdict(lambda: {"total": 0, "notes": 0, "files": defaultdict(int)})
    n_files = 0
    for fn in sorted(os.listdir(TUTORIALS_DIR)):
        if not fn.endswith(".md") or fn == "INDEX.md":
            continue
        path = os.path.join(TUTORIALS_DIR, fn)
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            content = fh.read()
        text = get_transcript(content)
        notes = get_notes(content)
        if not text:
            continue
        n_files += 1
        for src, is_notes in ((text, False), (notes, True)):
            for tok in TERM_RE.findall(src):
                if len(tok) < MIN_TERM_LEN or tok.lower() in STOPWORDS:
                    continue
                if not looks_technical(tok):
                    continue
                rec = index[tok]
                if is_notes:
                    rec["notes"] += 1
                else:
                    rec["total"] += 1
                    rec["files"][fn] += 1
    return index, n_files


def find_candidates(index, min_ratio, cutoff):
    """Hapax terms with a much commoner near neighbour."""
    vocab = sorted(index)
    common = [t for t in vocab if index[t]["total"] >= min_ratio]
    common_lower = {t.lower(): t for t in common}
    hapax = [t for t in vocab if index[t]["total"] == 1]

    out = []
    for term in hapax:
        matches = difflib.get_close_matches(term.lower(), list(common_lower), n=3, cutoff=cutoff)
        for m in matches:
            neighbour = common_lower[m]
            if neighbour.lower() == term.lower():
                continue
            # Morphological variants of the same word are correct usage.
            if _is_affix_variant(term, neighbour):
                continue
            n_common = index[neighbour]["total"]
            if n_common < min_ratio:
                continue
            fn = next(iter(index[term]["files"]))
            out.append({
                "term": term, "neighbour": neighbour, "neighbour_count": n_common,
                "file": fn,
                "ratio": n_common,
                "similarity": difflib.SequenceMatcher(None, term.lower(), neighbour.lower()).ratio(),
            })
            break
    out.sort(key=lambda c: (-c["similarity"], -c["ratio"]))
    return out


def find_variants(index, min_count, dominance, cutoff):
    """Terms that are NOT hapax but are near-misses of a much commoner term.

    ⚠️ THIS MODE EXISTS BECAUSE THE PLAN'S STATED LIMIT WAS TOO STRONG. §3.7 item
    5 says a consistent mishear is invisible to a hapax check, "because that
    substitution was consistent, so 'seam' is no hapax". True for the hapax mode
    — but a consistent mishear is not invisible to the CORPUS, it just is not a
    hapax. It shows up as a term appearing many times that is one edit away from
    a term appearing far more times.

    Found on the first real run: "Odini" 75x/51 files and "Udini" 40x/14 files
    against "Houdini" 1,566x. Whisper dropping the leading H from this skill's
    own subject, 115 times, in a corpus whose WHISPER_VOCAB_HINT exists
    specifically to stop that (ingest.py names "Houdini -> Odini" in its comment).

    ⚠️ Still candidates, not defects. A real term can legitimately sit one edit
    from a commoner one -- "snoise" really is a VEX function next to "noise"."""
    vocab = sorted(index)
    # ⚠️ Match against the DOMINANT terms only, never the whole vocabulary.
    # A first version searched all of it with get_close_matches(n=4) and its
    # flagship case was invisible: "odini"'s four most SIMILAR neighbours are
    # "rodini", "odinni", "odinit", "odinis" -- other rare variants of the same
    # mishear -- so "houdini" (1,566x, similarity 0.833) never entered the list
    # at any cutoff. Top-N similarity is the wrong selector when the thing you
    # are looking for is dominance. Restricting the pool fixes it and is faster.
    pool_min = max(2, min_count * dominance)
    dominant = {t.lower(): t for t in vocab if index[t]["total"] >= pool_min}
    frequent = [t for t in vocab if index[t]["total"] >= min_count]
    out = []
    for term in frequent:
        n_term = index[term]["total"]
        for cand in difflib.get_close_matches(term.lower(), list(dominant), n=3, cutoff=cutoff):
            other = dominant[cand]
            if other.lower() == term.lower():
                continue
            n_other = index[other]["total"]
            if n_other < n_term * dominance:
                continue
            if _is_affix_variant(term, other):
                continue
            out.append({
                "term": term, "count": n_term, "files": len(index[term]["files"]),
                "notes": index[term]["notes"],
                "neighbour": other, "neighbour_count": n_other,
                "similarity": difflib.SequenceMatcher(None, term.lower(), other.lower()).ratio(),
            })
            break
    out.sort(key=lambda c: -c["count"])
    return out


def main():
    ap = argparse.ArgumentParser(description="Corpus hapax mishear scan (plan §3.7 item 5)")
    ap.add_argument("--variants", action="store_true",
                    help="find CONSISTENT mishears: repeated terms one edit from a far commoner term")
    ap.add_argument("--min-count", type=int, default=3,
                    help="--variants: minimum occurrences to report (default 3)")
    ap.add_argument("--dominance", type=int, default=8,
                    help="--variants: neighbour must be this many times commoner (default 8)")
    ap.add_argument("--min-ratio", type=int, default=DEFAULT_MIN_RATIO,
                    help=f"neighbour must appear at least this many times (default {DEFAULT_MIN_RATIO})")
    ap.add_argument("--cutoff", type=float, default=None,
                    help=f"fuzzy similarity threshold (default {DEFAULT_CUTOFF} hapax, "
                         f"{DEFAULT_VARIANT_CUTOFF} --variants)")
    ap.add_argument("--limit", type=int, default=25, help="max candidates to print")
    ap.add_argument("--term", help="explain one term's counts instead of scanning")
    args = ap.parse_args()
    if args.cutoff is None:
        args.cutoff = DEFAULT_VARIANT_CUTOFF if args.variants else DEFAULT_CUTOFF

    if not os.path.isdir(TUTORIALS_DIR):
        print(f"ERROR: {TUTORIALS_DIR} not found")
        return 2

    index, n_files = build_index()
    print(f"Corpus: {n_files} tutorial(s) with a transcript, {len(index)} distinct technical term(s).")

    if args.term:
        rec = index.get(args.term)
        if not rec:
            near = difflib.get_close_matches(args.term, list(index), n=5, cutoff=0.7)
            print(f"'{args.term}' does not appear as a technical term. Near: {near}")
            return 0
        print(f"'{args.term}': {rec['total']} in raw transcripts across {len(rec['files'])} file(s), "
              f"{rec['notes']} in Structured Notes")
        for fn, n in sorted(rec["files"].items(), key=lambda kv: -kv[1])[:10]:
            print(f"    {n:3d}  {fn}")
        return 0

    if args.variants:
        vs = find_variants(index, args.min_count, args.dominance, args.cutoff)
        total = sum(v["count"] for v in vs)
        print(f"Consistent-variant candidates: {len(vs)} term(s), {total} occurrence(s)\n")
        for v in vs[:args.limit]:
            sev = (f"  🔴 {v['notes']} IN NOTES" if v["notes"]
                   else "  (raw transcript only — cosmetic)")
            print(f"  '{v['term']}' x{v['count']} in {v['files']} file(s)"
                  f"  ~  '{v['neighbour']}' x{v['neighbour_count']}  (sim {v['similarity']:.2f}){sev}")
        if len(vs) > args.limit:
            print(f"\n  ... {len(vs) - args.limit} more (raise --limit)")
        print(f"\n  not examined: terms appearing fewer than {args.min_count} times "
              f"(use the default hapax mode for those), and any variant whose")
        print(f"  neighbour is under {args.dominance}x commoner.")
        print("  ⚠️ Candidates, not defects: a real term can sit one edit from a commoner one.")
        print("  ⚠️ 'raw transcript only' means the extraction read-through already absorbed it —")
        print("     the transcript is a verbatim record, the NOTES are the durable knowledge.")
        return 0

    cands = find_candidates(index, args.min_ratio, args.cutoff)
    hapax_total = sum(1 for t in index if index[t]["total"] == 1)
    print(f"Hapax terms (appear exactly once): {hapax_total}")
    print(f"Candidates (hapax with a >={args.min_ratio}x commoner near neighbour): {len(cands)}\n")

    for c in cands[:args.limit]:
        print(f"  '{c['term']}' ~ '{c['neighbour']}' "
              f"(sim {c['similarity']:.2f}, neighbour seen {c['neighbour_count']}x)")
        print(f"      once in: {c['file']}")
    if len(cands) > args.limit:
        print(f"\n  ... {len(cands) - args.limit} more (raise --limit)")

    print("\n  not examined: terms shorter than "
          f"{MIN_TERM_LEN} chars, all-lowercase prose, and anything appearing 2+ times.")
    print("  ⚠️ A CONSISTENT mishear is invisible here by construction -- if the same")
    print("     wrong word was produced every time, it is common, not hapax.")
    print("  ⚠️ These are candidates, not defects. Rare terms are usually just rare.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
