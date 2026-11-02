"""Generic verifier: structural checks, exhaustive state-space search, shuffled numbering.

Driven entirely by book.json (see books/_template/book.json for every field). Writes build/map.json.

State model: (section, held tracked flags, values of tracked stats). Flags that appear in some
condition are tracked unless listed in flags.loose (one-shot guards / flavour, treated as unknown,
which over-approximates and keeps the space small). Stats are untracked by default: stat
conditions then count as unknown (both branches open). List stats in verify.track_stats to
search them exactly (they need a cap; clock stats tick on exit->hub moves).
"""
import json, os, random, re, runpy

from .config import read_json, write_json
from collections import defaultdict, deque, Counter

from . import conditions as C
from .graph import load_book


def natural(s):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', str(s))]


def run(cfg, quiet=False, write=True):
    book = load_book(cfg)
    S = book.S
    sec = cfg.get('sections', {})
    vcfg = cfg.get('verify', {})
    START = sec.get('start', next(iter(S)))
    TRUE_END = sec.get('true_ending')
    TERMINAL = set(sec.get('terminal_kinds', ['ending', 'death']))
    COUNT = sec.get('count')
    ISSUES, NOTES = [], []
    issue = ISSUES.append

    # ---------- 1. structural ----------
    if COUNT and len(S) != COUNT:
        issue(f'section count {len(S)} != {COUNT}')
    for k, s in S.items():
        for l in s['links']:
            if l['to'] not in S:
                issue(f"{k}: link to missing {l['to']}")
        if s['kind'] in TERMINAL and s['links']:
            issue(f'{k}: terminal with links')
        if s['kind'] not in TERMINAL and not s['links']:
            issue(f'{k}: dead end (no links)')
        if s['kind'] == 'death':
            if not s['warn']:
                issue(f'{k}: death without a warning')
            if not s['checkpoint']:
                issue(f'{k}: death without checkpoint')
            elif s['checkpoint'] != 'LAST' and s['checkpoint'] not in S:
                issue(f"{k}: checkpoint {s['checkpoint']} does not exist")
        for c in s.get('clue') or []:
            if c not in S:
                issue(f'{k}: clue {c} does not exist')
        if s['kind'] in ('test', 'combat') and not any(C.is_outcome(l['cond']) for l in s['links']):
            issue(f'{k}: {s["kind"]} section without pass/fail (win/lose) links')
    for k in sec.get('fixed_numbers', {}):
        if k not in S:
            issue(f'fixed number for missing section {k}')

    # ---------- 2. condition logic ----------
    LOOSE = set(cfg.flags.get('loose', []))
    USED = set()
    for s in S.values():
        for l in s['links']:
            USED.update(C.flags_used(l['cond']))
    TRACK = (USED - LOOSE) | set((vcfg.get('finale_gate') or {}).get('items', []))
    NOTES.append('Tracked flags: ' + ', '.join(sorted(TRACK)))
    gained = {f for s in S.values() for f in s['gain']}
    variants = set(cfg.get('variants', {}).get('flags', []))
    never = sorted(f for f in USED - gained - variants)
    if never:
        NOTES.append('Flags tested but never gained (always false/always true): ' + ', '.join(never))

    # tracked stats
    tstats = []
    for name in vcfg.get('track_stats', []):
        st = cfg.stat(name)
        if st.get('cap') is None:
            raise SystemExit(f'track_stats: {name} needs a "cap" in book.json')
        tstats.append(st)
    TN = [st['name'] for st in tstats]
    LIMITS = {st['name']: (st.get('limit') or {}).get('value') for st in cfg.stats}
    clock = cfg.get('clock') or {}
    EXITS, HUBS = set(clock.get('exits', [])), set(clock.get('hubs', []))
    if TN:
        NOTES.append('Tracked stats: ' + ', '.join(TN))

    def clampv(st, v):
        lo = st.get('floor', 0)
        return max(lo, min(st['cap'], v))

    # flags as bitmasks (fast): bit i <-> TRACK_L[i]
    TRACK_L = sorted(TRACK)
    BIT = {f: 1 << i for i, f in enumerate(TRACK_L)}
    mask = lambda fs: sum(BIT[f] for f in set(fs) if f in BIT)
    unmask = lambda m: [f for f in TRACK_L if m & BIT[f]]
    GAIN = {k: mask(s['gain']) for k, s in S.items()}
    LOSE = {k: mask(s['lose']) for k, s in S.items()}
    TIDX = {n: i for i, n in enumerate(TN)}

    def compile_cond(cond):
        req = forb = 0
        checks = []
        for a in C.atoms(cond):
            kind, p = C.parse_atom(a)
            if kind == 'flag':
                op, f = p
                if f in LOOSE:
                    continue
                if op == 'has':
                    req |= BIT[f]
                else:
                    forb |= BIT[f]
            elif kind == 'stat' and p[0] in TIDX:
                checks.append((TIDX[p[0]], C.OPS[p[1]], p[2]))
            elif kind == 'limit' and p in TIDX and LIMITS.get(p) is not None:
                checks.append((TIDX[p], C.OPS['>='], LIMITS[p]))
        return req, forb, tuple(checks)
    LINKS = {k: [(l['to'],) + compile_cond(l['cond']) for l in s['links']] for k, s in S.items()}

    def enter(prev, key, flags, sv):
        nf = (flags | GAIN[key]) & ~LOSE[key]
        if not tstats:
            return nf, ()
        s = S[key]
        out = []
        for st, v in zip(tstats, sv):
            if st.get('field'):
                v += s[st['field']]
            if clock.get('stat') == st['name'] and prev in EXITS and key in HUBS:
                v += 1
            out.append(clampv(st, v))
        return nf, tuple(out)

    # ---------- 3. state-space search ----------
    sv0 = tuple(st.get('start', 0) for st in tstats)
    f0, sv0 = enter(None, START, 0, sv0)
    start = (START, f0, sv0)
    seen = {start}
    q = deque([start])
    edges = defaultdict(dict)   # ordered sets: deterministic reports
    while q:
        node, flags, sv = q.popleft()
        for to, req, forb, checks in LINKS[node]:
            if flags & req != req or flags & forb:
                continue
            if checks and not all(op(sv[i], n) for i, op, n in checks):
                continue
            nf, nsv = enter(node, to, flags, sv)
            nxt = (to, nf, nsv)
            edges[(node, flags, sv)][nxt] = None
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    reached = {n for n, _, _ in seen}
    for u in sorted(set(S) - reached):
        issue(f'unreachable section {u}')
    NOTES.append(f'States explored: {len(seen):,}')

    rev = defaultdict(set)
    for a, bs in edges.items():
        for b in bs:
            rev[b].add(a)
    good = {st for st in seen if S[st[0]]['kind'] in TERMINAL}
    q = deque(good)
    while q:
        st = q.popleft()
        for p in rev[st]:
            if p not in good:
                good.add(p)
                q.append(p)
    soft = [st for st in seen if st not in good]
    for st in soft[:10]:
        issue(f'softlock at {st[0]} with {unmask(st[1])}' + (f' stats {dict(zip(TN, st[2]))}' if TN else ''))
    NOTES.append(f'Softlocked states: {len(soft)}')

    gate = vcfg.get('finale_gate')
    if gate:
        for node, flags, _ in seen:
            if node == gate['section'] and not all(i in BIT and flags & BIT[i] for i in gate['items']):
                issue(f"{gate['section']} reachable without all items")
                break

    # ---------- 4. endings ----------
    endings = [k for k, s in S.items() if s['kind'] == 'ending']
    ending_ok = {e: e in reached for e in endings}
    for e, ok in ending_ok.items():
        if not ok:
            issue(f'ending {e} unreachable')

    # ---------- 5. item routes ----------
    items = gate['items'] if gate else []
    routes = {i: sorted(k for k, s in S.items() if i in s['gain']) for i in items + vcfg.get('report_routes', [])}
    for i in items:
        if len(routes[i]) < vcfg.get('item_min_routes', 1):
            issue(f"{i} has fewer than {vcfg.get('item_min_routes', 1)} routes")
    rescue = sorted(k for k, s in S.items() if vcfg.get('report_rescue') in s['lose']) if vcfg.get('report_rescue') else []

    # ---------- 6. death fairness: every clue section can precede its death ----------
    plain = defaultdict(set)
    for k, s in S.items():
        for l in s['links']:
            plain[k].add(l['to'])

    def reaches(a, b):
        seen_, q_ = {a}, deque([a])
        while q_:
            x = q_.popleft()
            if x == b:
                return True
            for y in plain[x]:
                if y not in seen_:
                    seen_.add(y)
                    q_.append(y)
        return False
    death_report = []
    shared = set(sec.get('shared_deaths', []))
    for k, s in S.items():
        if s['kind'] != 'death' or k in shared:
            continue
        for c in s['clue']:
            if c != k and not reaches(c, k):
                issue(f'{k}: clue {c} cannot precede it')
        death_report.append(dict(key=k, title=s['title'], warn=s['warn'], clue=s['clue'], checkpoint=s['checkpoint']))

    # ---------- 7. minimum stat needed to reach each ending (label-correcting) ----------
    mins = {}
    for st in cfg.stats:
        if not (st.get('report_min') and st.get('field')):
            continue
        fld, floor = st['field'], st.get('floor')
        def nxtv(v, k, fld=fld, floor=floor):
            v = v + S[k][fld]
            return max(floor, v) if floor is not None else v
        best = {start: nxtv(0, START)}
        q = deque([start])
        while q:
            stt = q.popleft()
            v = best[stt]
            for nx in edges[stt]:
                nv = nxtv(v, nx[0])
                if nv < best.get(nx, 99):
                    best[nx] = nv
                    q.append(nx)
        m = {}
        for stt, v in best.items():
            if S[stt[0]]['kind'] == 'ending':
                m[stt[0]] = min(m.get(stt[0], 99), v)
        mins[st['name']] = (fld, m)
    for chk in vcfg.get('ending_below_limit', []):
        lim = LIMITS.get(chk['stat'])
        fld, m = mins.get(chk['stat'], (None, {}))
        if lim is not None and m.get(chk['ending'], 99) >= lim:
            issue(f"{chk['ending']} needs {chk['stat']} at its limit")
    lore = defaultdict(list)
    for k, s in S.items():
        if s['lore']:
            lore[s['lore']['id']].append(k)
    for lid, ks in lore.items():
        for k in ks:
            if k not in reached:
                issue(f'lore {lid} at unreachable {k}')

    # ---------- 8. shortest true-ending route ----------
    path = []
    if TRUE_END:
        dist = {start: 1}
        prev = {}
        q = deque([start])
        goal = None
        while q:
            stt = q.popleft()
            if stt[0] == TRUE_END:
                goal = stt
                break
            for nx in edges[stt]:
                if nx not in dist:
                    dist[nx] = dist[stt] + 1
                    prev[nx] = stt
                    q.append(nx)
        stt = goal
        while stt:
            path.append(stt[0])
            stt = prev.get(stt)
        path.reverse()

    # ---------- 9. shuffled book numbers ----------
    FIXED = dict(sec.get('fixed_numbers', {}))
    total = COUNT or len(S)
    no_adj = sec.get('no_adjacent', True)

    def assign(seed):
        rnd = random.Random(seed)
        free = [n for n in range(1, total + 1) if n not in FIXED.values()]
        rnd.shuffle(free)
        num = dict(FIXED)
        for k in S:
            if k not in num:
                if not free:
                    return None
                num[k] = free.pop()
        if no_adj:
            for k, s in S.items():
                for l in s['links']:
                    if l['to'] in num and abs(num[k] - num[l['to']]) <= 1:
                        return None
        return num
    seed = sec.get('seed_start', 0)
    num = None
    if len(S) <= total:
        for _ in range(100000):
            num = assign(seed)
            if num:
                break
            seed += 1
    if not num:
        issue('could not assign numbers (too many sections, or no seed satisfies the no-adjacent rule)')
        num = {k: i + 1 for i, k in enumerate(S)}
    else:
        NOTES.append(f'Numbering seed {seed}: no choice ever points to an adjacent section number (stops readers glimpsing outcomes).')
    for k, s in S.items():
        for l in s['links']:
            if l['to'] in sec.get('hidden_targets', []) and not C.is_hidden(l['cond']):
                issue(f"{k} prints a plain link to {l['to']}")

    # ---------- book-specific extra checks (optional checks.py) ----------
    if vcfg.get('extra_checks'):
        ns = runpy.run_path(cfg.path(vcfg['extra_checks']))
        ns['check'](book, issue, NOTES)

    # ---------- report ----------
    report = dict(
        total=len(S), acts=dict(Counter(s['act'] for s in S.values())), zones=dict(Counter(s['zone'] for s in S.values())),
        kinds=dict(Counter(s['kind'] for s in S.values())), issues=ISSUES, notes=NOTES, routes=routes, rescue=rescue,
        endings={e: dict(reachable=ending_ok[e], **{f'min_{fld}': m.get(e) for fld, m in mins.values()}) for e in endings},
        lore={lid: ks for lid, ks in sorted(lore.items(), key=lambda x: natural(x[0]))},
    )
    for st in cfg.stats:
        if st.get('field') and (st.get('limit') or {}).get('value') is not None:
            report[f"{st['field']}_sources"] = sorted((k, s[st['field']]) for k, s in S.items() if s[st['field']])
    for name, spec in vcfg.get('report_overlay', {}).items():
        src = book.overlay_attr(spec['attr'], {})
        d = {k: src.get(k) for k in spec.get('keys', src.keys())}
        for k, attr in spec.get('add', {}).items():
            d[k] = book.overlay_attr(attr)
        report[name] = d
    report.update(deaths=death_report, true_path=[(k, num[k]) for k in path], true_path_len=len(path), seed=seed)

    data = []
    for k, s in S.items():
        d = dict(s)
        d['num'] = num[k]
        d['links'] = [dict(l, num=num.get(l['to'])) for l in s['links']]
        data.append(d)
    data.sort(key=lambda d: d['num'])
    out = dict(sections=data, report=report)
    if write:
        os.makedirs(cfg.path('build'), exist_ok=True)
        write_json(cfg.path('build', 'map.json'), out, indent=1, ensure_ascii=False)
    if not quiet:
        print(json.dumps({k: v for k, v in report.items() if k not in ('deaths',)}, indent=1, ensure_ascii=False))
        print('ISSUES:', len(ISSUES))
    return out


def load_map(cfg):
    p = cfg.path('build', 'map.json')
    if not os.path.exists(p):
        raise SystemExit('No build/map.json: run `verify` first.')
    return read_json(p)
