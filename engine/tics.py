"""Style counters: tic patterns (book.json "tics") and conditional-block stats ("cond_groups").

Quotas: book.json "tic_quotas": {"book": {tic: max}, "<zone>": {tic: max}}. Over-quota lines are
marked with !! and the command lists them at the end (it does not fail the build: tics are a
reviewer/rewriter tool, not a gate).
"""
import re

from .check_prose import load_prose
from .graph import load_book
from .briefs import zone_keys


def count(texts, pats):
    tot = {k: 0 for k in pats}
    per = {}
    for k, t in texts.items():
        for name, p in pats.items():
            n = len(re.findall(p, t, re.I))
            tot[name] += n
            if n:
                per.setdefault(name, []).append(f'{k}×{n}' if n > 1 else k)
    return tot, per


def short_paras(texts):
    return sum(1 for t in texts.values() for p in re.split(r'\n\n+', t)
               if 0 < len(p.split()) <= 4 and not p.strip().startswith(('*', '"', '{', 'If', 'Turn', '“')) and '{' not in p)


def cond_stats(texts, groups):
    """Conditional paragraphs: '*If ...,*' blocks that are not just choice lines."""
    tot = dict(cond=0, words=0, midpara=0, **{g: 0 for g in groups})
    for k, t in texts.items():
        for p in re.split(r'\n\n+', t):
            m = re.match(r'^\*?If ([^,:.*]{0,70})', p)
            if not m:
                if re.search(r'[.!?"]\s+\*If ', p):
                    tot['midpara'] += 1
                continue
            if '{' in p and len(p.split()) < 40:
                continue
            key = m.group(1).lower()
            tot['cond'] += 1
            tot['words'] += len(p.split())
            for g, needles in groups.items():
                if any(n in key for n in needles):
                    tot[g] += 1
                    break
    return tot


def run(cfg, zones=None):
    book = load_book(cfg)
    prose = load_prose(cfg)
    pats = cfg.get('tics', {})
    quotas = cfg.get('tic_quotas', {})
    zk = zone_keys(cfg, book.S)
    over = []
    book_tot = {k: 0 for k in pats}
    for z, keys in zk.items():
        texts = {k: prose[k] for k in keys if isinstance(prose.get(k), str)}
        tot, per = count(texts, pats)
        for k in tot:
            book_tot[k] += tot[k]
        if zones and z not in zones:
            continue
        print(f'== {z}')
        zq = quotas.get(z, {})
        for name in pats:
            q = zq.get(name)
            flag = ' !!' if q is not None and tot[name] > q else ''
            if flag:
                over.append(f'{z}: {name} {tot[name]} > {q}')
            print(f"{name:24s} {tot[name]:4d}{(' /' + str(q)) if q is not None else '':5s}{flag}  {' '.join(per.get(name, []))[:140]}")
        print(f"{'paras <=4 words':24s} {short_paras(texts):4d}")
        cs = cond_stats(texts, cfg.get('cond_groups', {}))
        print('conditional blocks: ' + ', '.join(f'{k} {v}' for k, v in cs.items()))
    print('== book')
    for name, n in book_tot.items():
        q = quotas.get('book', {}).get(name)
        flag = ' !!' if q is not None and n > q else ''
        if flag:
            over.append(f'book: {name} {n} > {q}')
        print(f"{name:24s} {n:4d}{(' /' + str(q)) if q is not None else ''}{flag}")
    if over:
        print('OVER QUOTA:\n  ' + '\n  '.join(over))
    return 0
