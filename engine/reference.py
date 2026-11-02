"""Reference sheets for reviewers and auditors.

numbermap: build/NUMBER_MAP.md - printed number -> key (title). Reviews cite printed numbers;
           numbering reshuffles whenever the structure changes, so archive one map per review round
           (reviews/vN/NUMBER_MAP.md) and translate citations through it.
stateref : build/STATE.md - where each flag is gained/lost (printed numbers, in-world names) and the
           incoming links of every section with their conditions. Auditors check every section
           against every way in.
"""
from .verify import load_map
from . import conditions as C


def number_map(cfg):
    m = load_map(cfg)
    lines = ['# Printed number -> section key', '']
    lines += [f"{s['num']}: {s['key']} ({s['title']})" for s in m['sections']]
    p = cfg.path('build', 'NUMBER_MAP.md')
    write_text(p, '\n'.join(lines) + '\n')
    print('wrote build/NUMBER_MAP.md')


def state_ref(cfg):
    m = load_map(cfg)
    secs = m['sections']
    flags = sorted({f for s in secs for f in s['gain'] + s['lose']})
    out = ['# State reference (printed names; section NUMBERS as in the book)', '']
    for f in flags:
        g = [s['num'] for s in secs if f in s['gain']]
        l = [s['num'] for s in secs if f in s['lose']]
        tag = ' (hidden: never shown to the reader)' if f in cfg.hidden_flags else ''
        out.append(f'- {cfg.display(f)}{tag}: gained at {g}; lost at {l}')
    out += ['', '# Incoming links per section (num <- [(from num, condition)])']
    inc = {}
    for s in secs:
        for l in s['links']:
            if not C.is_global(l['cond']):
                inc.setdefault(l['to'], []).append((s['num'], C.describe(l['cond'], cfg.display)))
    for s in secs:
        out.append(f"{s['num']} {s['key']} ({s['kind']}) <- {inc.get(s['key'], [])}")
    write_text(cfg.path('build', 'STATE.md'), '\n'.join(out) + '\n')
    print('wrote build/STATE.md')
