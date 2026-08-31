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
"""
import collections, io, math, os, re, sys

sys.path.insert(0, r'C:/Users/KABUM/.claude/skills/houdini-wand')
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
    tagvocab = set()
    for txt in blocks.values():
        m = re.search(r'\*\*Tags:\*\*\s*(.+)', txt)
        if m:
            for t in re.split(r'[,`]', m.group(1)):
                t = t.strip().lower()
                if t:
                    tagvocab.add(t)
                    tagvocab.update(p for p in t.split('-') if len(p) >= 3)
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
