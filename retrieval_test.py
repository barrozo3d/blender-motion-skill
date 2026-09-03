"""F1 -- does a question actually reach the right entry?

Workstreams A-E all validated the CORPUS. Nothing ever tested the ANSWER PATH.
`SKILL.md` Mode 1 says: grep `tutorials/INDEX.md` by keyword/tag/node name, then
read the matching blocks. That surface has never been measured once.

THE TEST
  * the QUERY comes from the tutorial file's own `### Core Technique`
  * the SEARCH runs against `INDEX.md`, whose blocks carry Title + Tags + Summary
  * those are different documents, written in separate passes -- so this is not
    text matched against itself

  An entry that cannot retrieve itself from its own technique cannot be
  retrieved by anyone asking about that technique.

REALISM -- and the mistake v1 made
  A person types 2-4 keywords, not a sentence. v1 picked the terms RAREST in
  INDEX, on the theory that rare == distinctive. That was wrong, and the failure
  list showed it immediately: it built queries like "pick, right, technical" and
  "simplest, happens, sloped" -- rare generic ENGLISH, not domain vocabulary.
  Nobody searches that way, so v1's misses were mostly its own artifact.

  v2 restricts candidates to DOMAIN vocabulary before ranking by rarity. A term
  qualifies if it is used as a tag anywhere in the skill, or looks like a
  technical token (hyphenated, contains a digit, or CamelCase in the source).
  Tags are curated domain terms, which makes them the corpus's own definition of
  what is worth searching for.

RANK MATTERS, not just presence. An entry sitting 40 hits down is functionally
missing, because Mode 1 says to read only the matching blocks.

HONEST LIMIT (do not overstate this test)
  Core Technique and the INDEX Summary are written by the same extraction pass
  and share an author's vocabulary. This measures whether the retrieval surface
  WORKS MECHANICALLY. It does not prove a real user's phrasing would land -- only
  F4, with real questions, can show that.

READ THE HEADLINE NUMBER CORRECTLY -- IT IS A FLOOR, NOT A CEILING
  The single-query run reports ~77% top-5 and ~204 entries that "cannot retrieve
  themselves". Both are the result of allowing exactly ONE 3-keyword query per
  entry. A real consultation greps more than once; SKILL.md Step 1 invites it.

  Run `--reachable` for the number that actually bounds the surface: can an entry
  be reached by ANY single domain term from its own Core Technique?

      reachable in top-5 by some term   1220 / 1428   85%
      reachable only deeper than 5       206 / 1428   14%
      UNREACHABLE by any of its terms      2 / 1428    0.1%

  TWO entries. Not 204. Do NOT read the single-query figure as a mandate to
  restructure INDEX.md -- that conclusion was drawn once, on 2026-08-31, and the
  reachability run retired it the same day.

LOCAL vs ONLINE -- the split, added 2026-09-03 (plan section 3.7)
  A skill's entries arrive by two different pipelines: `ingest.py` from YouTube,
  and the course scripts from local video. They write INDEX blocks through
  different code, and whether they retrieve EQUALLY well had only ever been
  asserted. The run now reports top-k per provenance, plus the gap between them,
  read from each block's own `**Source:**` line.

  ⚠️ A GAP IS NOT AUTOMATICALLY A DEFECT, AND THE FIRST ONE MEASURED WAS NOT.
  houdini-wand, 2026-09-03: local 63% top-5 (115 entries) vs online 72% (494),
  a -9 pt gap. It is mostly the local entries crowding EACH OTHER, not the
  local pipeline writing worse blocks -- of the 203 top-5 slots sitting above a
  missed local entry, 36% are held by other local entries, against an 18%
  corpus share. Twice over-represented. A course is one instructor over one
  subject, so its entries compete for the same narrow vocabulary in a way a
  grab-bag of YouTube tutorials does not.

  So: read the gap as a fact to EXPLAIN, not a regression to chase, and re-run
  that occupancy check before concluding a pipeline is at fault.

  ⚠️ Only houdini-wand and nuke-em-all have both classes today; the other three
  are effectively single-provenance, and the run says so explicitly rather than
  printing a one-sided split that would read as parity.
"""
import argparse
import collections
import io
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS_ROOT = os.path.dirname(HERE) if os.path.exists(os.path.join(HERE, 'SKILL.md')) else HERE
SKILLS = ['houdini-wand', 'blender-motion', 'unreal-sidekick', 'nuke-em-all',
          'paint-me-like-your-french-substances']

STOP = set("""the a an and or of to in for with on at by from is are was were be been being
this that these those it its as into via using use used how what when where which
your you we our i not no if then than but so can will would should could may might
one two three all any some more most other another same different new old first last
make makes making made get gets getting got set sets setting way ways thing things
step steps guide tutorial video part full quick easy simple basic advanced intro
introduction overview complete beginner beginners inside without within also just
like about after before during while each per its it's them they their there here
up down out off over under again very much many few lot lots need needs needed""".split())

TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9_.-]{2,}")


def tok(text):
    for m in TOKEN.finditer(text):
        w = m.group(0).lower().strip('.-_')
        if len(w) >= 3 and w not in STOP:
            yield w


def index_blocks(skill):
    p = os.path.join(SKILLS_ROOT, skill, 'tutorials', 'INDEX.md')
    if not os.path.exists(p):
        return {}
    s = io.open(p, encoding='utf-8-sig', errors='replace').read()
    out = {}
    for blk in s.split('\n### ')[1:]:
        m = re.search(r'\*\*File:\*\*\s*tutorials/(\S+?)\.md', blk)
        if m:
            out[m.group(1)] = blk
    return out


def core_technique(path):
    s = io.open(path, encoding='utf-8-sig', errors='replace').read()
    m = re.search(r'###\s+Core Technique\s*\n(.+?)(?=\n###|\n---|\Z)', s, re.S)
    return m.group(1).strip() if m else None



BASELINE = 'retrieval_baseline.json'


PROV_ORDER = ('local', 'online', 'other')


def provenance(block):
    """Which pipeline produced this entry: 'local' (course), 'online' (YouTube),
    or 'other' (articles, vendor docs).

    ⚠️ Read from the INDEX block's own `**Source:**` line, which is the only
    provenance marker every entry carries. `validate.py::is_youtube_source()`
    reads the same field out of the TUTORIAL file; this one reads INDEX because
    that is the document being searched, and an entry with no block is already
    counted as not-tested above.
    """
    m = re.search(r'\*\*Source:\*\*\s*(.+)', block)
    if not m:
        return 'other'
    s = m.group(1).lower()
    if 'local course' in s:
        return 'local'
    if 'youtube' in s:
        return 'online'
    return 'other'


def baseline_path(skill):
    return os.path.join(SKILLS_ROOT, skill, BASELINE)


def load_baseline(skill):
    import json
    p = baseline_path(skill)
    if not os.path.exists(p):
        return None
    try:
        with io.open(p, encoding='utf-8') as fh:
            return json.load(fh)
    except Exception:
        return None


def record_baseline(skill, r):
    """Write the reference point later runs are compared against."""
    import json
    from datetime import date
    data = {'entries': r['tested'],
            'rank1_pct': 100 * r['r1'] // max(r['tested'], 1),
            'top5_pct': 100 * r['topk'] // max(r['tested'], 1),
            'unreachable_single_query': r['absent'],
            # per-pipeline, so a future run can see WHICH side moved. Absent
            # classes are simply not written -- an empty key would read as 0%.
            'by_provenance': {k: {'entries': v['tested'], 'top5_pct': v['pct']}
                              for k, v in (r.get('by_prov') or {}).items()},
            'recorded': str(date.today())}
    with io.open(baseline_path(skill), 'w', encoding='utf-8') as fh:
        json.dump(data, fh, indent=2)
        fh.write('\n')
    return data


def run(skill, nterms, topk, verbose):
    blocks = index_blocks(skill)
    tdir = os.path.join(SKILLS_ROOT, skill, 'tutorials')
    if not blocks or not os.path.isdir(tdir):
        return None

    btok = {slug: set(tok(txt)) for slug, txt in blocks.items()}
    bprov = {slug: provenance(txt) for slug, txt in blocks.items()}
    # the skill's own tag vocabulary = its definition of searchable domain terms
    tagvocab = set()
    for txt in blocks.values():
        m = re.search(r'\*\*Tags:\*\*\s*(.+)', txt)
        if m:
            for t in m.group(1).split(','):
                t = t.strip().lower()
                if t:
                    tagvocab.add(t)
                    tagvocab.update(p for p in t.split('-') if len(p) >= 3)
    df = collections.Counter()
    for terms in btok.values():
        df.update(terms)
    N = max(len(btok), 1)

    ranks, no_ct, no_block, misses = [], 0, 0, []
    prov_ranks = collections.defaultdict(list)
    for fn in sorted(os.listdir(tdir)):
        if not fn.endswith('.md') or fn == 'INDEX.md':
            continue
        slug = fn[:-3]
        if slug not in blocks:
            no_block += 1
            continue
        ct = core_technique(os.path.join(tdir, fn))
        if not ct:
            no_ct += 1
            continue
        # domain vocabulary only -- see the REALISM note. Rare generic English
        # is not a search term, and treating it as one manufactures misses.
        raw = list(dict.fromkeys(tok(ct)))
        techy = {w for w in raw
                 if w in tagvocab or '-' in w or any(c.isdigit() for c in w)
                 or re.search(r'[a-z][A-Z]', ct[ct.lower().find(w):][:len(w)] if w in ct.lower() else '')}
        cand = [w for w in raw if w in techy and df.get(w, 0) > 0]
        if len(cand) < nterms:      # fall back only to keep the entry testable
            cand += [w for w in raw if w not in techy and df.get(w, 0) > 0]
        cand.sort(key=lambda w: df[w])
        query = cand[:nterms]
        if not query:
            no_ct += 1
            continue
        scored = []
        for s2, terms in btok.items():
            hit = sum(1 for q in query if q in terms)
            if hit:
                idf = sum(math.log(N / df[q]) for q in query if q in terms)
                scored.append((hit, idf, s2))
        scored.sort(key=lambda x: (-x[0], -x[1], x[2]))
        pos = next((i + 1 for i, r in enumerate(scored) if r[2] == slug), None)
        ranks.append(pos)
        prov_ranks[bprov.get(slug, 'other')].append(pos)
        if pos is None or pos > topk:
            misses.append((pos, slug, query, len(scored)))

    found = [r for r in ranks if r]
    r1 = sum(1 for r in ranks if r == 1)
    rk = sum(1 for r in ranks if r and r <= topk)
    absent = sum(1 for r in ranks if r is None)
    print('%-40s tested %4d | rank1 %4d (%3d%%) | top-%d %4d (%3d%%) | NOT FOUND %3d'
          % (skill, len(ranks), r1, 100 * r1 // max(len(ranks), 1), topk, rk,
             100 * rk // max(len(ranks), 1), absent))
    # the coverage rule
    print('        not tested: %d entry with no Core Technique, %d tutorial with no INDEX block'
          % (no_ct, no_block))
    # ⚠️ THE LOCAL-vs-ONLINE SPLIT (plan §3.7). The two pipelines write INDEX
    # blocks by different routes, and the claim that they retrieve equally well
    # was only ever an assertion. Split the score and the gap is an observed
    # number that either closes or does not.
    by_prov = {}
    for name in PROV_ORDER:
        rs = prov_ranks.get(name, [])
        if not rs:
            continue
        hit = sum(1 for r in rs if r and r <= topk)
        by_prov[name] = dict(tested=len(rs), topk=hit,
                             pct=100 * hit // max(len(rs), 1))
    if len(by_prov) > 1:
        print('        by provenance:')
        for name in PROV_ORDER:
            d = by_prov.get(name)
            if d:
                print('          %-7s %4d entries | top-%d %4d (%3d%%)'
                      % (name, d['tested'], topk, d['topk'], d['pct']))
        if 'local' in by_prov and 'online' in by_prov:
            gap = by_prov['local']['pct'] - by_prov['online']['pct']
            print('          gap local-online: %+d pt' % gap)
    # the coverage rule again: say which classes this corpus does NOT contain,
    # so a single-provenance skill reads as "nothing to compare", not as parity.
    absent_prov = [n for n in PROV_ORDER if n not in by_prov]
    if absent_prov:
        print('        provenance not present in this corpus: %s%s'
              % (', '.join(absent_prov),
                 ' -- no split to measure' if len(by_prov) <= 1 else ''))
    if verbose and misses:
        print('        worst misses:')
        for pos, slug, q, n in sorted(misses, key=lambda x: (x[0] is not None, -(x[0] or 0)))[:8]:
            print('          rank %-5s %-52s q=%s (%d hits)'
                  % (pos if pos else 'NONE', slug[:52], ','.join(q), n))
    return dict(tested=len(ranks), r1=r1, topk=rk, absent=absent, misses=misses,
                by_prov=by_prov)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--terms', type=int, default=3, help='keywords per simulated query')
    ap.add_argument('--topk', type=int, default=5, help='rank considered a hit')
    ap.add_argument('--verbose', action='store_true')
    ap.add_argument('--skill')
    ap.add_argument('--record', action='store_true',
                    help='write retrieval_baseline.json for the measured skill(s)')
    ap.add_argument('--reachable', action='store_true',
                    help='the number that bounds the surface: can an entry be reached '
                         'by ANY single domain term from its Core Technique?')
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    print('F1 retrieval test -- query from Core Technique, searched against INDEX.md')
    print('(%d-keyword queries, a hit means rank <= %d)\n' % (a.terms, a.topk))
    tot = collections.Counter()
    for sk in ([a.skill] if a.skill else SKILLS):
        r = run(sk, a.terms, a.topk, a.verbose)
        if r and a.record:
            d = record_baseline(sk, r)
            print('        baseline recorded: %d entries, top-5 %d%%, rank1 %d%%'
                  % (d['entries'], d['top5_pct'], d['rank1_pct']))
        if r:
            for k in ('tested', 'r1', 'topk', 'absent'):
                tot[k] += r[k]
    print('\nCORPUS  tested %d | rank1 %d (%d%%) | top-%d %d (%d%%) | NOT FOUND %d'
          % (tot['tested'], tot['r1'], 100 * tot['r1'] // max(tot['tested'], 1),
             a.topk, tot['topk'], 100 * tot['topk'] // max(tot['tested'], 1), tot['absent']))
