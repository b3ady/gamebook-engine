"""Waypoint playthroughs for reviewers: full-prose reads of chosen routes (playthroughs/<name>.md).

book.json "playthroughs": [{"name": "1_kind_true_ending", "variant": "DAUGHTER",
   "waypoints": ["A03", "A07", ...], "avoid": ["AL01", ...], "outcome": {"G32": "pass"}}]
Between waypoints the shortest legal path is found (BFS over section + flags; loose/hidden flags
ignored for de-duplication). Tests default to success unless `outcome` says otherwise; deaths are
avoided unless they are a waypoint. Design one playthrough per reader persona (kind, cold, secret,
rescue, debts, reckless, separate...) so every ending and every major codeword route is read.
"""
import os
from collections import deque

from . import conditions as C
from .config import write_text
from .build_book import load, checkpoints
from .render_routes import make_renderer


def run(cfg, names=None):
    d = load(cfg)
    S = {s['key']: s for s in d['sections']}
    start = cfg.get('sections', {}).get('start', d['sections'][0]['key'])
    side = frozenset(cfg.flags.get('loose', [])) | frozenset(cfg.hidden_flags)
    render = make_renderer(cfg, S)
    cps = checkpoints(cfg, d['sections'])

    def step(k, flags):
        s = S[k]
        return frozenset((set(flags) | set(s['gain'])) - set(s['lose']))

    def route(cur, flags, target, avoid, outcome):
        q = deque([(cur, flags)])
        prev = {(cur, flags): None}
        seen = {(cur, flags - side)}
        while q:
            node, fl = q.popleft()
            if node == target and ((node, fl) != (cur, flags) or cur == target):
                path, st = [], (node, fl)
                while st:
                    path.append(st)
                    st = prev[st]
                return path[::-1][1:] if len(path) > 1 else path
            s = S[node]
            if s['kind'] in ('ending', 'finale'):
                continue
            nexts = []
            if s['kind'] == 'death':
                nexts = [s['checkpoint']] if s['checkpoint'] != 'LAST' else []
            else:
                for l in s['links']:
                    c = l['cond']
                    if C.is_global(c) or not C.evaluate(c, fl):
                        continue
                    oc = [a for a in C.atoms(c) if a in C.OUTCOMES]
                    if oc and node in outcome and oc[0] != outcome[node]:
                        continue
                    if oc and node not in outcome and oc[0] in ('fail', 'lose'):
                        continue
                    if l['to'] != target and (l['to'] in avoid or S[l['to']]['kind'] == 'death'):
                        continue
                    nexts.append(l['to'])
            for n in nexts:
                nf = step(n, fl)
                key = (n, nf - side)
                if key in seen:
                    continue
                seen.add(key)
                st = (n, nf)
                if st not in prev:
                    prev[st] = (node, fl)
                    q.append(st)
        return None

    os.makedirs(cfg.path('playthroughs'), exist_ok=True)
    for p in cfg.get('playthroughs', []):
        if names and p['name'] not in names:
            continue
        g = p.get('variant')
        flags = step(start, frozenset({g} if g else ()))
        cur, path = start, [start]
        for w in p['waypoints']:
            if w not in S:
                print(p['name'], 'MISSING waypoint', w)
                continue
            seg = route(cur, flags, w, set(p.get('avoid', [])), p.get('outcome', {}))
            if seg is None:
                print(p['name'], 'NO ROUTE to', w, 'from', cur)
                break
            path += [k for k, _ in seg]
            cur, flags = seg[-1]
        text = [f"# PLAYTHROUGH: {p['name']}\nReader chose: {g or '-'}. Sections read: {len(path)}. Ending: {S[path[-1]]['title']}\n"]
        for k in path:
            mark = ' ✈' if k in cps else ''
            text.append(f"\n\n———  {S[k]['num']}{mark}  ———\n\n" + render(S[k]['text'], g))
        write_text(cfg.path('playthroughs', f"{p['name']}.md"), ''.join(text))
        words = sum(len((S[k]['text'] or '').split()) for k in path)
        died = [k for k in path if S[k]['kind'] == 'death']
        print(f"{p['name']}: {len(path)} sections, ~{words} words, ending {path[-1]}, deaths {died}")
