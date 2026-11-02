"""Merge build/map.json + prose/*.json -> build/book.json (input to epub, sheet, story map, routes)."""
import json, re

from .config import read_json, write_json

from .check_prose import load_prose
from .verify import load_map


def checkpoints(cfg, sections):
    cps = {s['checkpoint'] for s in sections if s['kind'] == 'death' and s['checkpoint'] not in (None, 'LAST')}
    return cps | set(cfg.get('sections', {}).get('checkpoints_extra', []))


def run(cfg, quiet=False):
    d = load_map(cfg)
    prose = load_prose(cfg)
    pre = cfg.get('prose', {}).get('front_prefix', 'FRONT_')
    front = {k: v for k, v in prose.items() if k.startswith(pre)}
    missing = []
    for s in d['sections']:
        s['text'] = prose.get(s['key'])
        if not s['text']:
            missing.append(s['key'])
    d['report']['checkpoints'] = sorted(checkpoints(cfg, d['sections']))
    d['front'] = front
    words = sum(len(re.sub(r'\{[^}]+\}', '', s['text'] or '').split()) for s in d['sections'])
    words += sum(len(v.split()) for v in front.values())
    d['report']['words'] = words
    d['config'] = {k: cfg.get(k) for k in ('book', 'stats', 'clock', 'flags', 'variants') if k in cfg}
    write_json(cfg.path('build', 'book.json'), d, ensure_ascii=False)
    if not quiet:
        print(f'build/book.json: {len(d["sections"])} sections, {words:,} words; missing text: {len(missing)}', missing[:20])
    return d


def load(cfg):
    import os
    p = cfg.path('build', 'book.json')
    if not os.path.exists(p):
        raise SystemExit('No build/book.json: run `build` first.')
    return read_json(p)
