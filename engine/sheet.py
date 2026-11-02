"""Companion web Adventure Sheet: per-section effect data embedded in a single HTML page.

The reader types each section number; the page applies gains/losses, stat changes, checkpoints,
clock ticks, deaths and limit warnings, and rolls dice. Template: web_sheet.template (book-specific)
or engine/templates/sheet.html (generic, driven by DATA.cfg).
"""
import json, os, re

from .config import read_text, write_text

from .build_book import load, checkpoints

HERE = os.path.dirname(os.path.abspath(__file__))


def build_data(cfg, d):
    ws = cfg.get('web_sheet', {})
    S = {s['key']: s for s in d['sections']}
    num = lambda k: S[k]['num']
    hidden = cfg.hidden_flags
    cost = re.compile(ws['cost_regex'], re.I) if ws.get('cost_regex') else None
    cps = checkpoints(cfg, d['sections'])
    foe_fields = ws.get('foe_fields', ['nerve', 'vig'])
    stat_short = {st['field']: st.get('short', st['field'][0]) for st in cfg.stats if st.get('field')}
    # Layover-compatible short keys: fear->f, vig->v, claim->c
    out = {}
    for s in d['sections']:
        e = {}
        g = [x for x in s['gain'] if x not in hidden]
        l = [x for x in s['lose'] if x not in hidden]
        if g:
            e['g'] = g
        if l:
            e['l'] = l
        for f, short in stat_short.items():
            if s.get(f):
                e[short] = s[f]
        if s['kind'] == 'death':
            e['d'] = 1
            e['cp'] = None if s['checkpoint'] == 'LAST' else num(s['checkpoint'])
        if s['kind'] == 'ending':
            e['end'] = 1
        if ws.get('loop_ending') and s['key'] == ws['loop_ending']:
            e['loop'] = 1
        if s['key'] in cps:
            e['cpt'] = 1
        t = s.get('test') or {}
        if t.get('type') == 'combat':
            e['foe'] = [t['foe'].title()] + [t.get(f) for f in foe_fields]
        elif t.get('type'):
            e['test'] = t['type']
        if cost:
            costs = sorted({m.group(0)[0].upper() + m.group(0)[1:] for lk in s['links'] for m in cost.finditer(lk['label'])})
            if costs:
                e['opt'] = costs
        if s.get('lore'):
            e['lore'] = [s['lore']['id'], s['lore']['title']]
        out[s['num']] = e
    clock = cfg.get('clock') or {}
    DATA = dict(sec=out, exits=sorted(num(k) for k in clock.get('exits', [])), hubs=sorted(num(k) for k in clock.get('hubs', [])))
    # global limit endings and stat deaths (Layover template names: finalcall, vigdeath)
    limits, deaths = {}, {}
    for st in cfg.stats:
        lim = st.get('limit') or {}
        if lim.get('ending'):
            limits[st['name']] = dict(value=lim.get('value'), dynamic=lim.get('dynamic'), sec=num(lim['ending']))
        if st.get('death'):
            deaths[st['name']] = num(st['death'])
    if limits:
        DATA['finalcall'] = next(iter(limits.values()))['sec']
    if deaths:
        DATA['vigdeath'] = next(iter(deaths.values()))
    DATA['limits'], DATA['deaths'] = limits, deaths
    return DATA


def sheet_cfg(cfg):
    """The settings the generic template reads (DATA.cfg)."""
    ws = cfg.get('web_sheet', {})
    b = cfg.get('book', {})
    return dict(
        brand=ws.get('brand', b.get('title', '').upper()), tag=ws.get('tag', ''), key=ws.get('storage_key', b.get('slug', 'book') + '-sheet'),
        abilities=ws.get('abilities', []), stats=[st for st in cfg.stats], clock=cfg.get('clock'),
        variants=cfg.get('variants', {}), display=cfg.flags.get('display', {}),
        items=cfg.flags.get('items', []), codewords=cfg.flags.get('codewords', []),
        consumables=cfg.flags.get('consumables', {}), warnings=ws.get('warnings', []),
        modes=ws.get('modes', {}), combat=ws.get('combat'), loop_keep=ws.get('loop_keep', {}))


def run(cfg):
    d = load(cfg)
    ws = cfg.get('web_sheet', {})
    DATA = build_data(cfg, d)
    tpl = cfg.path(ws['template']) if ws.get('template') else os.path.join(HERE, 'templates', 'sheet.html')
    if not ws.get('template'):
        DATA['cfg'] = sheet_cfg(cfg)
    t = read_text(tpl)
    out = cfg.path('build', ws.get('out', 'sheet.html'))
    write_text(out, t.replace('__DATA__', json.dumps(DATA, separators=(',', ':'), ensure_ascii=False)))
    print('wrote', os.path.relpath(out, cfg.dir), 'sections', len(DATA['sec']), 'bytes', len(json.dumps(DATA)))
    return DATA
