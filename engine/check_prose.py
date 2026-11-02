"""Check prose against the structure, zone by zone.

For each section in a zone: text exists; {KEY} tokens == printed links (+ the death checkpoint);
hidden links are never printed; minimum length by kind; every visible gained flag is named
(in-world name); every stat change is stated; no raw underscore codewords; no banned cliches.
"""
import glob, json, os, re

from .config import read_json

from . import conditions as C
from .graph import load_book
from .briefs import zone_keys

TOKEN = re.compile(r'\{([A-Za-z0-9_]+)\}')


def load_prose(cfg):
    prose = {}
    for f in sorted(glob.glob(cfg.path(cfg.get('prose', {}).get('dir', 'prose'), '*.json'))):
        prose.update(read_json(f))
    return prose


def words(t):
    return len(re.sub(r'\{[^}]+\}', '', t).split())


def check_section(k, s, t, cfg, book):
    probs = []
    chk = cfg.get('check', {})
    toks = TOKEN.findall(t)
    want = [l['to'] for l in book.printed_links(s)]
    if s['kind'] == 'death' and s.get('checkpoint') not in (None, 'LAST'):
        want.append(s['checkpoint'])
    if sorted(set(toks)) != sorted(set(want)):
        probs.append(f'TOKENS {sorted(set(toks))} want {sorted(set(want))}')
    if any(l['to'] in toks for l in s['links'] if C.is_hidden(l['cond'])):
        probs.append('hidden link printed as token')
    mins = chk.get('min_words', {})
    lo = mins.get(s['kind'], mins.get('default', 0))
    w = words(t)
    if w < lo:
        probs.append(f'SHORT {w}')
    hi = chk.get('max_words', {}).get(s['kind'], chk.get('max_words', {}).get('default'))
    if hi and w > hi:
        probs.append(f'LONG {w}')
    skip = cfg.hidden_flags | set(cfg.flags.get('unstated_ok', []))
    for f in s['gain']:
        if f in skip:
            continue
        if cfg.display(f) not in t:
            probs.append(f'effect not stated: gain {cfg.display(f)}')
    if chk.get('check_lose'):
        for f in s['lose']:
            if f not in skip and cfg.display(f) not in t:
                probs.append(f'effect not stated: lose {cfg.display(f)}')
    for raw in book.all_flags:
        if ('_' in raw or cfg.display(raw) != raw) and raw in t and raw != cfg.display(raw):
            probs.append(f'underscore codeword in text: {raw}')
    for st in cfg.stats:
        f = st.get('field')
        if f and st.get('must_state') and s.get(f) and st['name'] not in t:
            probs.append(f"{st['name']} change not stated")
    for c in chk.get('cliches', []):
        if c in t.lower():
            probs.append(f'CLICHE {c}')
    return probs


def run(cfg, zones=None, quiet=False):
    book = load_book(cfg)
    book.all_flags = sorted({f for s in book.S.values() for f in s['gain'] + s['lose']} |
                            {f for s in book.S.values() for l in s['links'] for f in C.flags_used(l['cond'])})
    prose = load_prose(cfg)
    zk = zone_keys(cfg, book.S)
    total = 0
    for z, keys in zk.items():
        if zones and z not in zones:
            continue
        bad = 0
        for k in keys:
            if k not in prose or not isinstance(prose[k], str):
                print(f'[{z}] MISSING {k}')
                bad += 1
                continue
            for p in check_section(k, book.S[k], prose[k], cfg, book):
                print(f'[{z}] {k} {p}')
                bad += 1
        print(f'{z}: ' + ('OK' if not bad else f'{bad} problems'))
        total += bad
    stale = sorted(k for k in prose if k not in book.S and not k.startswith(cfg.get('prose', {}).get('front_prefix', 'FRONT_')))
    if stale and not zones:
        print('note: prose keys with no section (stale, ignored by the build):', ' '.join(stale))
    return 1 if total else 0
