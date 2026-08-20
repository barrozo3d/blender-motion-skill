#!/usr/bin/env python3
"""
scan_promo.py -- read-only detector for promotional / no-content tutorial entries.

    python scan_promo.py                 # ranked candidate report
    python scan_promo.py --all           # every file, ranked
    python scan_promo.py --json          # machine-readable, for triage tooling
    python scan_promo.py --explain FILE  # full signal breakdown for one file

WRITES NOTHING. That is deliberate (plan batch A2): the sweep has to happen
before the gate exists, or the gate gets tuned against nothing. Batch A7 turns
this into validate.py check #11 by importing score_file() -- do not duplicate
the scoring logic there.

WHY THIS EXISTS
    tutorials/noise.md was a 1m31s course trailer that taught nothing, titled
    exactly "Noise" and tagged with eleven topics it never demonstrated. It was
    the top grep hit for any noise question and produced four consecutive wrong
    answers. Both existing content gates are LENGTH-based, and a trailer beats
    length heuristics by construction -- it is dense, fluent speech about
    material that is never shown:

        validate #8 (notes > 200 chars)   the trailer's notes were ~1,800 chars
        validate #9 (>= 3 chars/sec)      only runs at >= 180s; trailer was 91s

    Nothing asked "does this teach a technique?". That is the question here.

THE KEY INSIGHT
    The extraction pass already answers it correctly, in prose. noise.md's own
    notes said "Trailer only -- no step-by-step content"; attributes.md's say
    "This is a promotional trailer for David Tornow's paid course". The signal
    was sitting in the files the whole time with nothing acting on it. So the
    strongest signal here is not clever text analysis -- it is reading what the
    extraction already wrote.

    That is also why SELF-DECLARATION IS REQUIRED FOR A CANDIDATE. The
    structural signals (short video, thin Key Steps, few named nodes)
    CORROBORATE; they do not ACCUSE. On their own they describe a perfectly
    legitimate format -- the short-form feature tutorial, one minute long, one
    feature, five concrete steps -- which is exactly how plugin and add-on
    documentation is published. Scoring those as promo told the user their own
    plugin library was junk. An entry that fires no self-declared signal is
    reported separately as structural-only, never as a candidate.

    Corollary, and the reason this stays read-only: where the extraction pass is
    honest the score is trustworthy, and where it is not, no amount of scoring
    weight rescues it. Signal 4 (named-thing density) is the one signal that
    does not depend on the extraction's honesty, which is why it is weighted
    like a primary signal rather than a tiebreaker. Every candidate still gets
    triaged by hand (A4/A5).

PORTABILITY (A3 ports this to the other four skills verbatim)
    Nothing here is Houdini-specific. The node section is named differently in
    every skill -- "Houdini Nodes / VEX / Settings", "Nodes / Settings"
    (blender-motion), "UE Systems / Blueprints / Settings" (unreal-sidekick),
    "Nodes / Tools / Settings" (nuke-em-all), "Layers / Tools / Settings"
    (paint-me-...) -- so it is matched by shape, not by name. See
    NODE_SECTION_RE. Only ALLOWLIST is per-skill.
"""

import argparse
import json
import os
import re
import sys

TUTORIALS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tutorials")

# Score at or above which an entry is reported for hand triage. Tuned in A2 so
# both confirmed trailers clear it and the two deliberate overview-only
# gap-fillers (plan Gotcha #2) sit below it. NOT a delete threshold -- it only
# selects what a human looks at.
CANDIDATE_THRESHOLD = 50

# Entries that are deliberately thin because the source is paywalled, ingested
# on purpose to fill a documented gap. A gap-filler TEACHES (node chains,
# workflow) even without a transcript; a trailer ADVERTISES -- it names topics
# it never demonstrates. Keep each reason with its entry; A7 reuses this as the
# gate's allowlist.
ALLOWLIST = {
    # Empty: no deliberate overview-only gap-fillers are recorded for this skill.
    # Add entries only with a written reason, the way houdini-wand's two are
    # justified from KNOWLEDGE_GAPS_TODO.md. A4/A5 triage decides what belongs
    # here -- an entry is NOT allowlisted just because the scanner flagged it.
}


# -- section extraction -------------------------------------------------------

def read(path):
    with open(path, "r", encoding="utf-8-sig") as fh:
        return fh.read()


def get_notes(content):
    m = re.search(r"## Structured Notes(.+)", content, re.DOTALL)
    return m.group(1).strip() if m else ""


def get_subsection(content, heading_re):
    """Text of one '### <heading>' block, up to the next '###' or '---'."""
    m = re.search(heading_re, content, re.MULTILINE | re.IGNORECASE)
    if not m:
        return ""
    rest = content[m.end():]
    stop = re.search(r"\n### |\n---\s*\n", rest)
    return (rest[:stop.start()] if stop else rest).strip()


# Matched by shape, not name -- every skill names this section differently, but
# all of them pair a domain noun with Settings/Tools/Code.
NODE_SECTION_RE = r"^###\s+.*\b(?:Nodes?|Systems?|Tools?|Layers?|Settings?|Concepts?)\b.*$"
KEY_STEPS_RE = r"^###\s+Key Steps\s*$"


def is_youtube(content):
    m = re.search(r"^source:\s*(.+)", content, re.MULTILINE)
    return bool(m) and "youtube" in m.group(1).lower()


def duration_secs(content):
    m = re.search(r"\*\*Duration:\*\*\s+(?:(\d+)h\s*)?(?:(\d+)m\s*)?(?:(\d+)s)?", content)
    if not m:
        return 0
    return int(m.group(1) or 0) * 3600 + int(m.group(2) or 0) * 60 + int(m.group(3) or 0)


def get_transcript(content):
    start = content.find("## Raw Data")
    if start == -1:
        return ""
    raw = content[start:]
    split = re.search(r"\n## Structured Notes", raw)
    if split:
        raw = raw[:split.start()]
    raw = re.sub(r"\n## Ingest Safeguard Report\n.*?\n---\n", "\n", raw, flags=re.DOTALL)
    out = []
    for line in raw.splitlines():
        s = line.strip()
        if s.startswith("**Transcript:**"):
            out.append(s[len("**Transcript:**"):].strip())
        elif re.match(r"\[\d+:\d{2}\] ", s):
            out.append(s.split("] ", 1)[1])
    return " ".join(out)


# -- signals ------------------------------------------------------------------

# The extraction pass calling the entry promotional in its own prose. Strongest
# signal available: a direct statement about the source, not an inference.
# (weight, label, pattern)
SELF_DECLARED = [
    (30, "calls it a trailer", r"\btrailer\b"),
    (30, "calls it promotional/advertising", r"\bpromotional\b|\bpromo\b|\badvertis\w+"),
    (30, "says there is no technical content", r"\bno (?:technical|instructional) content\b"),
    (25, "says there is no step-by-step", r"\bno step[- ]by[- ]step\b|\bno step by step\b"),
    (20, "calls it a course overview/preview",
         r"\bcourse (?:overview|trailer|intro(?:duction)?|preview)\b"),
    (20, "says overview only", r"\boverview[- ]only\b|\bonly an overview\b"),
    (20, "says it is not a real tutorial",
         r"\bnot a (?:standalone |real |technique )*tutorial\b"),
    (15, "quotes a sign-up / enrol call", r"\bsign up\b|\benroll?\b"),
    (15, "says the source is a sales/landing page",
         r"\bsales(?:[/ -]?(?:landing )?)?page\b|\blanding page\b"),
    (15, "says nothing is taught",
         r"\bnothing is (?:taught|demonstrated|shown)\b|\bteaches nothing\b"),
]

# Calls to action are what a trailer is FOR. Checked only in the closing
# stretch, because a real tutorial can legitimately say "link in the
# description" up front.
CTA = [
    r"\bsign up\b", r"\benroll?\b", r"\bmy (?:new )?(?:class|course)\b",
    r"\blink in the description\b", r"\bhead over to\b", r"\bfor more info\b",
    r"\bcheck out the (?:course|class)\b", r"\btake that next step\b",
    r"\bavailable now at\b", r"\bjoin (?:me|us) (?:in|for)\b",
]

# A named node/tool/parameter: `backticked`, a TitleCase run, or an ALLCAPS /
# mixed-case domain token (VEX, VOPs, PDG, TOPnet, HDA, UV). A real tutorial
# names many; a trailer names topics instead.
BACKTICKED = re.compile(r"`([^`\n]{2,60})`")
TITLECASE_RUN = re.compile(r"\b([A-Z][a-zA-Z0-9]+(?:[ /-][A-Z][a-zA-Z0-9]+)*)\b")
DOMAIN_TOKEN = re.compile(r"\b([A-Z]{2,}[a-z]*[A-Z0-9]*)\b")

# Words that look like node names but are prose. Trailers are full of these, and
# so are the honest "could not verify any node names" disclaimers that the
# gap-filler entries carry.
NODE_STOPWORDS = {
    "Not", "Based", "The", "This", "That", "Only", "Note", "None", "No", "All",
    "Both", "If", "It", "In", "On", "At", "As", "But", "And", "Or", "For",
    "From", "Treat", "See", "Use", "Using", "Also", "Plus", "Implied", "Likely",
    "Typically", "Would", "Could", "Should", "May", "Might", "Course", "Class",
    "Session", "Sessions", "Video", "Videos", "Lesson", "Lessons", "Chapter",
    "Chapters", "Beginner", "Intermediate", "Advanced", "Overview", "Summary",
    "Trailer", "Houdini", "Blender", "Unreal", "Nuke", "Mari", "Katana",
    "Substance", "Painter", "YouTube", "Vimeo", "Vol",
}


def count_named_things(section):
    """Distinct node/tool/parameter names asserted in the node section."""
    names = set()
    for m in BACKTICKED.finditer(section):
        names.add(m.group(1).strip().lower())
    # Strip backticked spans first so their contents are not counted twice.
    plain = BACKTICKED.sub(" ", section)
    for rx in (TITLECASE_RUN, DOMAIN_TOKEN):
        for m in rx.finditer(plain):
            tok = m.group(1).strip()
            if tok in NODE_STOPWORDS:
                continue
            names.add(tok.lower())
    return len(names)


# A course TRAILER stands alone. A course's own "what we'll cover this week"
# INTRO CHAPTER sits inside a fully-ingested series and is navigational, not
# promotional -- deleting it would punch a hole in a series whose other chapters
# are real. Both look identical to every text signal above, so separate them
# structurally: does this slug have sibling chapters?
#
# Reported as an annotation, never as a score change. The scanner does not get
# to decide that a series intro is fine -- A4/A5 does. It only makes the two
# categories distinguishable at a glance.
CHAPTER_NUM_RE = re.compile(r"-(\d{1,2})-")


def series_siblings(fname, all_names):
    """Count other tutorials sharing this file's series prefix.

    The prefix is the slug up to its first chapter-number token, so
    'module-i-week-02-01-intro-v1-1080p.md' -> 'module-i-week' and
    'designing-destruction-wk1-02-definition.md' -> 'designing-destruction-wk1'.
    Files with no chapter-number token (a standalone trailer) score 0.
    """
    slug = fname[:-3] if fname.endswith(".md") else fname
    m = CHAPTER_NUM_RE.search(slug)
    if not m:
        return 0
    prefix = slug[:m.start()]
    if not prefix or "-" not in prefix and len(prefix) < 3:
        return 0
    return sum(1 for n in all_names
               if n != fname and n[:-3].startswith(prefix + "-"))


def count_steps(section):
    """List items in Key Steps -- numbered or bulleted."""
    n = 0
    for line in section.splitlines():
        if re.match(r"^(?:[-*+]\s+|\d+[.)]\s+)", line.strip()):
            n += 1
    return n


def score_file(path, fname=None, all_names=()):
    """Score one tutorial. Returns a dict; never writes. Imported by A7."""
    fname = fname or os.path.basename(path)
    content = read(path)
    notes = get_notes(content)
    transcript = get_transcript(content)
    node_sec = get_subsection(content, NODE_SECTION_RE)
    steps_sec = get_subsection(content, KEY_STEPS_RE)

    score = 0
    hits = []

    # 1. self-declared promo language in the extraction's own prose.
    # This is the ACCUSING signal -- everything below only corroborates it.
    declared = 0
    for weight, label, rx in SELF_DECLARED:
        if re.search(rx, notes, re.IGNORECASE):
            declared += weight
            hits.append("notes: %s (+%d)" % (label, weight))
    # Cap: many phrasings of one fact are still one fact.
    if declared > 60:
        hits.append("(self-declared subtotal %d capped at 60)" % declared)
        declared = 60
    score += declared

    # 2. short YouTube video -- the length band where validate #9 never runs
    secs = duration_secs(content)
    yt = is_youtube(content)
    if yt and 0 < secs < 180:
        w = 25 if secs < 120 else 18
        score += w
        hits.append("YouTube, %ds -- under the 180s floor where check #9 never "
                    "runs (+%d)" % (secs, w))

    # 3. a Key Steps section that does not step through anything
    nsteps = count_steps(steps_sec)
    disclaimer = bool(re.search(
        r"^\s*[-*+]?\s*\(?(?:trailer only|no step|not a step|overview only|no lesson)",
        steps_sec, re.IGNORECASE | re.MULTILINE))
    if disclaimer:
        score += 25
        hits.append("Key Steps opens with a 'no steps here' disclaimer (+25)")
    if steps_sec and nsteps <= 2:
        score += 20
        hits.append("Key Steps has only %d item(s) (+20)" % nsteps)

    # 4. low density of named nodes/tools -- names topics, not techniques
    nnamed = count_named_things(node_sec)
    if node_sec:
        if nnamed <= 4:
            score += 25
            hits.append("only %d distinct node/tool names in the node section (+25)" % nnamed)
        elif nnamed <= 8:
            score += 12
            hits.append("only %d distinct node/tool names in the node section (+12)" % nnamed)

    # 5. call to action in the closing stretch of the transcript
    cta = []
    if transcript:
        tail = transcript[int(len(transcript) * 0.85):]
        for rx in CTA:
            if re.search(rx, tail, re.IGNORECASE):
                cta.append(rx)
        if cta:
            w = min(10 * len(cta), 20)
            score += w
            hits.append("call to action in the closing 15%% of transcript: "
                        "%d phrase(s) (+%d)" % (len(cta), w))

    return {
        "file": fname,
        "score": score,
        "hits": hits,
        "duration_secs": secs,
        "youtube": yt,
        "named_things": nnamed,
        "key_steps": nsteps,
        "cta_phrases": len(cta),
        "self_declared": declared,
        "series_siblings": series_siblings(fname, all_names),
        "allowlisted": fname in ALLOWLIST,
        "allowlist_reason": ALLOWLIST.get(fname, ""),
    }


# -- report -------------------------------------------------------------------

def tutorial_files(d):
    return sorted(f for f in os.listdir(d) if f.endswith(".md") and f != "INDEX.md")


def scan_all(d=TUTORIALS_DIR):
    names = tutorial_files(d)
    results = [score_file(os.path.join(d, f), f, names) for f in names]
    results.sort(key=lambda r: (-r["score"], r["file"]))
    return results


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="read-only promo/no-content scanner")
    ap.add_argument("--all", action="store_true", help="report every file, ranked")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--explain", metavar="FILE", help="full breakdown for one file")
    ap.add_argument("--threshold", type=int, default=CANDIDATE_THRESHOLD)
    ap.add_argument("--dir", default=TUTORIALS_DIR)
    args = ap.parse_args()

    if args.explain:
        path = args.explain
        if not os.path.isfile(path):
            path = os.path.join(args.dir, os.path.basename(args.explain))
        r = score_file(path, all_names=tutorial_files(args.dir))
        print("%s  score %d" % (r["file"], r["score"]))
        print("  duration %ds | youtube %s | named node/tool terms %d | "
              "key steps %d | tail CTA phrases %d | series siblings %d | "
              "self-declared %d"
              % (r["duration_secs"], r["youtube"], r["named_things"],
                 r["key_steps"], r["cta_phrases"], r["series_siblings"],
                 r["self_declared"]))
        if r["self_declared"] == 0 and r["score"] >= CANDIDATE_THRESHOLD:
            print("  STRUCTURAL-ONLY: the extraction never called this "
                  "promotional. Not a candidate -- most likely a short-form "
                  "feature tutorial. Default KEEP.")
        if r["allowlisted"]:
            print("  ALLOWLISTED: %s" % r["allowlist_reason"])
        for h in r["hits"]:
            print("  - %s" % h)
        if not r["hits"]:
            print("  - no signals fired")
        return 0

    results = scan_all(args.dir)

    if args.json:
        print(json.dumps(results, indent=2))
        return 0

    over = [r for r in results if r["score"] >= args.threshold]
    # Structural signals corroborate; they do not accuse. An entry that scores
    # on short-duration / thin-steps / few-names alone is most often a
    # short-form feature tutorial, not promo -- report it, but not as a
    # candidate. See the module docstring.
    flagged = [r for r in over if r["self_declared"] > 0]
    structural = [r for r in over if r["self_declared"] == 0]
    shown = results if args.all else flagged
    scores = [r["score"] for r in results]
    allow_hit = [r for r in flagged if r["allowlisted"]]

    print("=" * 72)
    print("scan_promo.py -- promotional / no-content candidates (READ-ONLY)")
    print("=" * 72)
    print("scanned %d tutorials in %s" % (len(results), args.dir))
    print("threshold %d | %d candidate(s) (%d allowlisted) | %d structural-only"
          % (args.threshold, len(flagged), len(allow_hit), len(structural)))
    if scores:
        srt = sorted(scores)
        print("score distribution: max %d | p95 %d | median %d | zero-score %d"
              % (srt[-1], srt[int(len(srt) * 0.95) - 1], srt[len(srt) // 2],
                 scores.count(0)))
    print()

    for r in shown:
        tag = "  [ALLOWLISTED]" if r["allowlisted"] else ""
        print("%4d  %s%s" % (r["score"], r["file"], tag))
        if r["series_siblings"]:
            print("        * SERIES INTRO? %d sibling chapter(s) share this slug "
                  "prefix -- likely a course's own intro, not a standalone "
                  "trailer. Removing it holes a real series." % r["series_siblings"])
        for h in r["hits"]:
            print("        - %s" % h)
        if r["allowlisted"]:
            print("        REASON: %s" % r["allowlist_reason"])
        print()

    if not shown:
        print("no candidates at this threshold.")

    if structural and not args.all:
        print("=" * 72)
        print("STRUCTURAL-ONLY -- scored at or above threshold but the extraction")
        print("never called this promotional. NOT candidates.")
        print("=" * 72)
        print("These fired only corroborating signals: short video, thin Key Steps,")
        print("few named nodes. That is also the exact shape of a legitimate")
        print("short-form feature tutorial -- one minute, one feature, a handful of")
        print("concrete steps -- which is how most plugin and add-on documentation")
        print("is published. Default KEEP. Look here only for an entry that is BOTH")
        print("structurally empty AND teaches nothing.")
        print()
        for r in structural:
            print("%4d  %s  (key steps %d, named terms %d)"
                  % (r["score"], r["file"], r["key_steps"], r["named_things"]))
        print()

    print("-" * 72)
    print("This tool WRITES NOTHING and DECIDES NOTHING. Every candidate above")
    print("needs hand triage: REMOVE (pure promo) / DEMOTE (real content, oversold")
    print("tags) / KEEP (false positive or deliberate gap-filler). Record the")
    print("decisions in PROMO_ENTRY_CLEANUP_PLAN.md Findings -- batches A4/A5.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
