"""Coverage playtest routes: a small set of legal random playthroughs that together visit every section.

Each walk follows the rules a reader follows: flags, stat changes (with floor/cap), clock ticks on
exit->hub moves, deaths send you back to the checkpoint, a stat reaching its limit ends the walk at
its limit ending, and a true stat condition ("If your Claim is 3 or more, turn to ...") is forced.
Test/fight outcomes are free choices (Story Mode). Output: playtest/routes.json.
"""
import json, os, random

from .config import write_json

from . import conditions as C
from .build_book import load, checkpoints


class Walker:
    def __init__(self, cfg, d):
        self.cfg = cfg
        self.S = {s['key']: s for s in d['sections']}
        self.start = cfg.get('sections', {}).get('start', d['sections'][0]['key'])
        self.cps = checkpoints(cfg, d['sections'])
        clock = cfg.get('clock') or {}
        self.clock, self.exits, self.hubs = clock.get('stat'), set(clock.get('exits', [])), set(clock.get('hubs', []))
        self.stats = [st for st in cfg.stats if st.get('field') or st['name'] == self.clock]
        self.limits = {st['name']: (st.get('limit') or {}).get('value') for st in cfg.stats}
        self.limit_end = {st['name']: (st.get('limit') or {}).get('ending') for st in cfg.stats}
        cv = cfg.get('coverage', {})
        self.max_steps, self.fresh_bias = cv.get('max_steps', 600), cv.get('fresh_bias', 0.85)

    def bound(self, st, v):
        lo, hi = st.get('floor'), st.get('cap')
        if lo is not None:
            v = max(lo, v)
        if hi is not None:
            v = min(hi, v)
        return v

    def walk(self, variant, seen, rng):
        S = self.S
        flags = {variant} if variant else set()
        vals = {st['name']: st.get('start', 0) for st in self.stats}
        cp, cur, prev, path = self.start, self.start, None, []
        for _ in range(self.max_steps):
            s = S[cur]
            path.append(cur)
            flags = (flags | set(s['gain'])) - set(s['lose'])
            for st in self.stats:
                if st.get('field'):
                    vals[st['name']] = self.bound(st, vals[st['name']] + (s.get(st['field']) or 0))
            if cur in self.cps:
                cp = cur
            if s['kind'] in ('ending', 'finale'):
                break
            hit = [n for n, lim in self.limits.items() if lim is not None and vals.get(n, 0) >= lim]
            if hit:
                path.append(self.limit_end[hit[0]])
                break
            if s['kind'] == 'death':
                prev, cur = cur, (cp if s['checkpoint'] == 'LAST' else s['checkpoint'])
                continue
            opts = [l for l in s['links'] if C.evaluate(l['cond'], flags, vals, self.limits, unknown=False)]
            forced = [l for l in opts if not C.is_hidden(l['cond']) and any(a.startswith('stat:') for a in C.atoms(l['cond']))]
            if forced:
                opts = forced
            if not opts:
                path.append('!STUCK')
                break
            fresh = [l for l in opts if l['to'] not in seen]
            pool = fresh if fresh and rng.random() < self.fresh_bias else opts
            l = rng.choice(pool)
            prev, cur = cur, l['to']
            if self.clock and prev in self.exits and cur in self.hubs:
                st = next(x for x in self.stats if x['name'] == self.clock)
                vals[self.clock] = self.bound(st, vals[self.clock] + 1)
        return path


def run(cfg):
    d = load(cfg)
    W = Walker(cfg, d)
    cv = cfg.get('coverage', {})
    rng = random.Random(cv.get('seed', 7))
    variants = cfg.get('variants', {}).get('flags') or [None]
    best, seen = [], set()
    stuck = set()
    while len(seen) < len(W.S) and len(best) < cv.get('max_routes', 14):
        cands = []
        for _ in range(cv.get('candidates', 400)):
            g = rng.choice(variants)
            p = W.walk(g, seen, rng)
            if '!STUCK' in p:
                stuck.add(p[-2])
                continue
            cands.append((len(set(p) - seen) - len(p) / 400, g, p))
        if not cands:
            break
        sc, g, p = max(cands, key=lambda c: c[0])
        new = len(set(p) - seen)
        if new == 0:
            break
        best.append(dict(variant=g, path=p))
        seen |= set(p)
        print(f'{len(best):2d} {g or "-":9s} {len(p):4d} sections, new {new:3d}, total {len(seen)}, ends {p[-1]}')
    # targeted rounds for stragglers (hard puzzles, low-stat gates): many more walks, keep any that hits one
    for _ in range(cv.get('extra_rounds', 3)):
        missing = set(W.S) - seen
        if not missing:
            break
        hit = None
        for _ in range(cv.get('candidates', 400) * 10):
            g = rng.choice(variants)
            p = W.walk(g, seen, rng)
            if '!STUCK' not in p and missing & set(p):
                hit = (g, p)
                break
        if not hit:
            break
        best.append(dict(variant=hit[0], path=hit[1]))
        seen |= set(hit[1])
        print(f'{len(best):2d} {hit[0] or "-":9s} {len(hit[1]):4d} sections, targeted: {sorted(missing & set(hit[1]))}, ends {hit[1][-1]}')
    missing = sorted(set(W.S) - seen)
    print('missing:', missing or 'none')
    if stuck:
        print('WARNING: walks got stuck (no legal link) at:', sorted(stuck))
    os.makedirs(cfg.path('playtest'), exist_ok=True)
    write_json(cfg.path('playtest', 'routes.json'), dict(routes=best, missing=missing, stuck=sorted(stuck)), indent=1)
    return best, missing
