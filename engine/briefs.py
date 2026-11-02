"""Per-zone writer briefs (briefs/<zone>.md) from build/map.json.

Each section gets: heading, arrives-from list (so the opening works from every entry), beat,
link tokens with conditions, effects in in-world names, death line, lore, design notes.
"""
import os

from .config import write_text

from . import conditions as C
from .verify import load_map


def effects(s, cfg):
    e = []
    hidden = cfg.hidden_flags
    for g in s['gain']:
        e.append(('(hidden, never mention) ' if g in hidden else 'Note ') + cfg.display(g))
    for g in s['lose']:
        e.append(('(hidden) lose ' if g in hidden else 'Cross off ') + cfg.display(g))
    for st in cfg.stats:
        f = st.get('field')
        if f and s.get(f):
            e.append(f"{st['name']} {s[f]:+d}")
    return e


def zone_keys(cfg, S):
    """Zone -> ordered keys. From book.json "zones" (explicit lists, or {"zone": name}/{"act": n} filters);
    default: one zone per section 'zone' field, in story order."""
    zc = cfg.get('zones')
    if not zc:
        out = {}
        for s in S.values():
            out.setdefault(s['zone'].lower().replace(' ', '_'), []).append(s['key'])
        return out
    out = {}
    for z, spec in zc.items():
        if isinstance(spec, list):
            out[z] = [k for k in spec if k in S]
        else:
            out[z] = [k for k, s in S.items() if all(s.get(f) == v for f, v in spec.items())]
    return out


def run(cfg):
    m = load_map(cfg)
    S = {s['key']: s for s in m['sections']}
    S_ordered = {s['key']: s for s in sorted(m['sections'], key=lambda s: s['num'])}
    inl = {}
    for s in m['sections']:
        for l in s['links']:
            if not C.is_global(l['cond']):
                inl.setdefault(l['to'], []).append(s['key'])
    chk = cfg.get('check', {})
    death_end = chk.get('death_end', 'Return to {{{checkpoint}}} and choose again.')
    cost_field = chk.get('death_cost_field')
    zones = zone_keys(cfg, S_ordered)
    os.makedirs(cfg.path('briefs'), exist_ok=True)
    placed = set()
    for z, keys in zones.items():
        out = []
        for k in keys:
            s = S[k]
            placed.add(k)
            out.append(f"### {k} — {s['title']}  [{s['kind']}, Act {s['act']}, {s['zone']}]")
            out.append('Arrives from: ' + ', '.join(f"{p} ({S[p]['title']})" for p in dict.fromkeys(inl.get(k, []))))
            out.append('Beat: ' + s['beat'])
            links = [l for l in s['links'] if not C.is_global(l['cond'])]
            if links:
                out.append('Links (write each target as a token):')
                for l in links:
                    if C.is_hidden(l['cond']):
                        c = f"  [HIDDEN puzzle link, never print the token; condition: {C.describe(l['cond'], cfg.display)}]"
                    else:
                        c = f"  [condition: {C.describe(l['cond'], cfg.display)}]" if l['cond'] else ''
                    out.append(f"  - {{{l['to']}}}  \"{l['label']}\"{c}  → leads to: {S[l['to']]['title']}")
            e = effects(s, cfg)
            if e:
                out.append('Effects (state them in the text, using in-world names): ' + '; '.join(e))
            if s['test']:
                t = s['test']
                if t.get('type') == 'combat':
                    out.append(f"Foe line: {t.get('foe')}  " + '  '.join(f'{k.upper()} {v}' for k, v in t.items() if k not in ('type', 'foe')))
                else:
                    out.append(f"Test: {t.get('type')}")
            if s['kind'] == 'death':
                cost = (s.get(cost_field) or 1) if cost_field else ''
                out.append(f"Death — the warning the reader was given: {s['warn']}  End: '" +
                           death_end.format(cost=cost, checkpoint=s['checkpoint']) + "'")
            if s.get('lore'):
                out.append(f"Lore {s['lore']['id']} ({s['lore']['title']}): {s['lore']['text']}")
            if s.get('notes'):
                out.append('Design note: ' + s['notes'])
            out.append('')
        write_text(cfg.path('briefs', f'{z}.md'), '\n'.join(out))
        print(f'briefs/{z}.md', len(keys))
    missing = [k for k in S_ordered if k not in placed]
    if missing:
        print('WARNING: sections in no zone (no brief, no prose check):', ' '.join(missing))
