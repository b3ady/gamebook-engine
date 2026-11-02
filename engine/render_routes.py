"""Render playtest/routes.json as full-prose route files for playtester agents (playtest/routeNN.md).

Each file shows the sections in reading order with printed numbers (✈ = checkpoint), variant
paragraphs resolved for the route's reader, conditional paragraphs set off with '> ', and after
each section a [PLAYER -> turns to N: label. Sheet now: ...] line.
"""
import json, os, re

from .config import write_text, read_json

from .build_book import load, checkpoints


def make_renderer(cfg, S):
    var = cfg.get('variants', {})
    marker = re.compile(var['marker'], re.I) if var.get('marker') else None
    match = {k: re.compile(v, re.I) for k, v in var.get('match', {}).items()}

    def vkey(label):
        for k, rx in match.items():
            if rx.search(label.strip()):
                return k
        return None

    def render(text, variant):
        out = []
        for p in re.split(r'\n\n+', text or ''):
            if marker and marker.search(p):
                parts = marker.split(p)
                keep = parts[0]
                for i in range(1, len(parts), 2):
                    if vkey(parts[i]) == variant:
                        keep += parts[i + 1]
                p = keep.strip()
                if not p:
                    continue
            p = re.sub(r'\{([A-Za-z0-9_]+)\}', lambda m: str(S[m.group(1)]['num']), p)
            if re.match(r'^\*If [^*]+\*', p) and not (re.search(r'turn to \d', p) and len(p.split()) < 40):
                p = '> ' + p
            out.append(p)
        return '\n\n'.join(out)
    return render


def run(cfg):
    d = load(cfg)
    S = {s['key']: s for s in d['sections']}
    render = make_renderer(cfg, S)
    cps = checkpoints(cfg, d['sections'])
    hidden = cfg.hidden_flags | set(cfg.get('variants', {}).get('flags', []))
    fields = [(st['name'], st['field']) for st in cfg.stats if st.get('field')]
    data = read_json(cfg.path('playtest', 'routes.json'))
    for i, r in enumerate(data['routes'], 1):
        g, p = r['variant'], r['path']
        fl = {g} if g else set()
        tally = {n: 0 for n, _ in fields}
        out = [f"# ROUTE {i}\nReader: {g or '(no variant)'}. Story Mode (you choose test outcomes). {len(p)} sections.\n"]
        for j, k in enumerate(p):
            s = S[k]
            fl = (fl | set(s['gain'])) - set(s['lose'])
            for n, f in fields:
                tally[n] += s.get(f) or 0
            mark = ' ✈' if k in cps else ''
            out.append(f"\n\n———  {s['num']}{mark}  ———\n\n" + render(s['text'], g))
            if j + 1 < len(p):
                nxt = p[j + 1]
                lab = [l['label'] for l in s['links'] if l['to'] == nxt]
                how = lab[0] if lab else ('(death: back to checkpoint)' if s['kind'] == 'death' else '(global rule)')
                sheet = sorted(cfg.display(x) for x in fl if x not in hidden)
                stats = ', '.join(f'{n} {v:+d}' for n, v in tally.items() if v)
                out.append(f"\n\n[PLAYER → turns to {S[nxt]['num']}: {how}. Sheet now: {', '.join(sheet) or '—'}"
                           + (f"; stat changes from book data so far ≈ {stats}" if stats else '') + ']')
        write_text(cfg.path('playtest', f'route{i:02d}.md'), ''.join(out))
        print(f'playtest/route{i:02d}.md', len(p), 'sections', sum(len((S[k]['text'] or '').split()) for k in p), 'words')
