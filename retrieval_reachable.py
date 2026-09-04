"""Is the 204 "cannot retrieve itself" figure a real ceiling, or an artifact of
allowing only ONE query?

F1 fired a single 3-keyword query per entry. A real consultation greps more than
once, and SKILL.md's Step 1 explicitly invites that ("grep it by keyword/tag").
So the number that decides whether a fix is needed is different:

    can this entry be reached AT ALL, by ANY single domain term from its own
    Core Technique, within the top 5?

If most of the 204 are reachable by some other term, the retrieval surface is
fine and the fix is unnecessary. If they are unreachable by every term they are
about, the INDEX genuinely does not describe them.

THE TWO GENUINELY UNREACHABLE ENTRIES ARE ACCEPTED, AND CHECKED (2026-09-03)
Both were read in full before being left alone. Neither is a defect, and
"fixing" either would mean writing tags that misdescribe the entry to move a
number -- which is the one thing this measurement must never cause.

  * houdini-wand/designing-destruction-wk1-12-conclusion
    Its Core Technique reads, correctly, "N/A -- recap lesson, no new
    technique." Queries here are built FROM Core Technique, so there is nothing
    distinctive to retrieve it by, and that is an accurate description of a
    week-recap lesson rather than a gap. It is reachable by browsing the course,
    which is how a recap is actually found.

  * blender-motion/daily-blender-tip-47---custom-transform-orientation
    A real technique (Custom Transform Orientation, Ctrl+Alt+Space), tagged
    `modelling, beginner`. Those tags are RIGHT: this corpus's tag vocabulary is
    deliberately COARSE -- the top terms are intermediate / procedural /
    materials / beginner / geometry-nodes -- so tags are broad categories, not
    per-feature keywords. Adding `transform-orientation` would make this the
    only entry in 1488 carrying a one-off feature tag, breaking the convention
    to satisfy a metric. Its distinctive words ("orientation", "transform")
    simply are not tags, and should not be.

So the honest reading of this script's headline is: 2 of 1488 entries (0.1%)
cannot be reached by a single term from their own Core Technique, and both have
a specific, examined reason. Do not treat that number as work outstanding.
"""
import collections, io, math, os, re, sys

# ⚠️ Was a hardcoded C:/Users/KABUM/... path -- the OTHER machine's home.
# On any other device it silently pointed nowhere and the import fell
# through to the working directory, which happened to work and would
# have failed the moment this was run from elsewhere. Derive it.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import retrieval_test as rt

TOPK = 5
tot = collections.Counter()
hard = []

for sk in rt.SKILLS:
    blocks = rt.index_blocks(sk)
    tdir = os.path.join(rt.SKILLS_ROOT, sk, 'tutorials')
    if not blocks or not os.path.isdir(tdir):
        continue
    btok = {s2: set(rt.tok(t)) for s2, t in blocks.items()}
    # ⚠️ Shared with retrieval_test, deliberately. This file used to split on
    # [,`] only: it mishandled the hash style entirely and kept the '#' prefix
    # on backtick+hash tags, so the two retrieval tools DISAGREED about what a
    # tag is while reporting on the same corpus.
    tagvocab = set()
    for txt in blocks.values():
        tagvocab |= rt.tag_terms(txt)
    df = collections.Counter()
    for terms in btok.values():
        df.update(terms)
    N = max(len(btok), 1)

    for fn in sorted(os.listdir(tdir)):
        if not fn.endswith('.md') or fn == 'INDEX.md':
            continue
        slug = fn[:-3]
        if slug not in blocks:
            continue
        ct = rt.core_technique(os.path.join(tdir, fn))
        if not ct:
            continue
        raw = list(dict.fromkeys(rt.tok(ct)))
        terms = [w for w in raw
                 if (w in tagvocab or '-' in w or any(c.isdigit() for c in w))
                 and df.get(w, 0) > 0]
        if not terms:
            terms = [w for w in raw if df.get(w, 0) > 0]
        tot['entries'] += 1
        best = None
        for q in terms:                       # try EVERY domain term on its own
            if q not in btok[slug]:
                continue
            scored = sorted(
                ((sum(1 for x in [q] if x in bt), math.log(N / df[q]), s2)
                 for s2, bt in btok.items() if q in bt),
                key=lambda x: (-x[0], -x[1], x[2]))
            pos = next((i + 1 for i, r in enumerate(scored) if r[2] == slug), None)
            if pos and (best is None or pos < best):
                best = pos
        if best is None:
            tot['unreachable'] += 1
            hard.append((sk, slug, len(terms)))
        elif best <= TOPK:
            tot['reachable_top5'] += 1
        else:
            tot['reachable_deep'] += 1

e = max(tot['entries'], 1)
print('Can an entry be reached by ANY single domain term from its Core Technique?\n')
print('  entries tested                     %5d' % tot['entries'])
print('  reachable in top-%d by some term    %5d  (%d%%)' % (TOPK, tot['reachable_top5'], 100 * tot['reachable_top5'] // e))
print('  reachable only deeper than %d       %5d  (%d%%)' % (TOPK, tot['reachable_deep'], 100 * tot['reachable_deep'] // e))
print('  UNREACHABLE by any of its own terms %5d  (%d%%)' % (tot['unreachable'], 100 * tot['unreachable'] // e))
print()
if hard:
    print('genuinely unreachable, sample:')
    for sk, slug, n in hard[:10]:
        print('   %-24s %-56s (%d terms tried)' % (sk, slug[:56], n))
    print('   ... %d total' % len(hard))
