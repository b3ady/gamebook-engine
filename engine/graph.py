"""Section model, the story-building helpers, and loading a book's story modules.

A section is a dict:
    key, act, zone, kind (story|choice|test|combat|item|anomaly|death|ending), title, beat,
    links [{to, label, cond}], gain [flags], lose [flags], <stat fields e.g. fear, vig, claim>,
    test (None | {type: 'Nerve'|'Fortune'|'combat', foe?, ...}), warn, clue [keys], checkpoint, notes,
    lore (None | {id, title, text, opens})

A book's story.py builds a list S with N(...) calls, then may apply layered edit blocks
(revision rounds) with L / drop / retarget / K. New books use StoryBuilder:

    from engine.graph import StoryBuilder
    B = StoryBuilder(stats=("fear", "vig", "claim"))
    N, L, drop, retarget, K, S = B.N, B.L, B.drop, B.retarget, B.K, B.S

The Layover's story.py predates the engine and defines its own identical helpers; the loader
accepts any module that leaves a list of section dicts in a variable (default name S).
"""
import copy, runpy, sys
from collections import OrderedDict

from . import conditions as C


def make_links(links):
    """(to, label[, cond]) tuples -> link dicts."""
    return [dict(to=l[0], label=l[1], cond=(l[2] if len(l) > 2 else None)) for l in links]


class StoryBuilder:
    """Helpers for writing story.py. Every edit is recorded in order so revision rounds stay layered."""

    def __init__(self, stats=('fear', 'vig')):
        self.S = []
        self.stat_fields = tuple(stats)

    def N(self, key, act, zone, kind, title, beat, links, gain=(), lose=(), test=None, warn=None,
          clue=None, checkpoint=None, notes=None, **stats):
        unknown = set(stats) - set(self.stat_fields)
        if unknown:
            raise TypeError(f'{key}: unknown stat field(s) {sorted(unknown)}; declare them in StoryBuilder(stats=...)')
        d = dict(key=key, act=act, zone=zone, kind=kind, title=title, beat=beat, links=make_links(links),
                 gain=list(gain), lose=list(lose))
        for f in self.stat_fields:
            d[f] = stats.get(f, 0)
        d.update(test=test, warn=warn, clue=list(clue or []), checkpoint=checkpoint, notes=notes)
        self.S.append(d)
        return d

    L = staticmethod(lambda *links: make_links(links))

    def K(self):
        """Fresh key -> section index (call again after adding/dropping sections)."""
        return {s['key']: s for s in self.S}

    def drop(self, key):
        self.S[:] = [s for s in self.S if s['key'] != key]

    def retarget(self, old, new):
        for s in self.S:
            for l in s['links']:
                if l['to'] == old:
                    l['to'] = new

    # the Layover's spelling of the same helpers
    _L = L

    def _drop(self, key):
        self.drop(key)

    def _retarget(self, old, new):
        self.retarget(old, new)

    def link(self, key, to, label, cond=None, first=False):
        s = self.K()[key]
        l = dict(to=to, label=label, cond=cond)
        s['links'].insert(0, l) if first else s['links'].append(l)


def _run(path):
    import os
    sys.dont_write_bytecode = True
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if root not in sys.path:
        sys.path.insert(0, root)          # so a book's story.py can `from engine.graph import StoryBuilder`
    return runpy.run_path(path, run_name='__book__')


class Book:
    """A loaded book: config + ordered sections + overlay namespaces."""

    def __init__(self, cfg):
        self.cfg = cfg
        st = cfg.get('story', {})
        mod = _run(cfg.path(st.get('module', 'story.py')))
        raw = mod[st.get('list', 'S')]
        self.S = OrderedDict((s['key'], copy.deepcopy(s)) for s in raw)
        self.overlay_ns = []
        for ov in st.get('overlays', []):
            ns = _run(cfg.path(ov['module']))
            self.overlay_ns.append((ov, ns))
            self._apply_overlay(ov, ns)
        self._normalize()
        self._hooks()

    # ------------------------------------------------------------------
    def _apply_overlay(self, ov, ns):
        U = ns[ov.get('dict', 'U')]
        lore_fields = ov.get('lore_fields', ['id', 'title', 'text', 'opens'])
        copy_fields = ov.get('fields')          # None = copy every field given
        set_fields = ov.get('reset_fields', [])  # fields set to their default when a key is overlaid but omits them
        for k, u in U.items():
            if k not in self.S:
                raise SystemExit(f'overlay {ov["module"]}: unknown section {k}')
            s = self.S[k]
            for f, v in u.items():
                if copy_fields is not None and f not in copy_fields and f != 'lore' and f not in set_fields:
                    continue
                if f == 'lore':
                    s['lore'] = dict(zip(lore_fields, v)) if isinstance(v, (list, tuple)) else v
                else:
                    s[f] = copy.deepcopy(v)
            for f in set_fields:
                if f not in u:
                    s[f] = 0

    def _normalize(self):
        aliases = self.cfg.get('conditions', {}).get('aliases', {})
        for s in self.S.values():
            for f in self.cfg.stat_fields:
                s.setdefault(f, 0)
            s.setdefault('lore', None)
            s.setdefault('clue', [])
            for f in ('test', 'warn', 'checkpoint', 'notes'):
                s.setdefault(f, None)
            for l in s['links']:
                l['cond'] = C.normalize(l['cond'], aliases)
                try:
                    C.validate(l['cond'])
                except C.CondError as e:
                    raise SystemExit(f'{s["key"]} -> {l["to"]}: {e}')

    def _hooks(self):
        """Limit hooks: after any section that raises a stat with a limit, add the global-rule link."""
        terminal = set(self.cfg.get('sections', {}).get('terminal_kinds', ['ending', 'death']))
        for st in self.cfg.stats:
            lim = st.get('limit') or {}
            if not (st.get('field') and lim.get('hook_label') and lim.get('ending')):
                continue
            for s in self.S.values():
                if s[st['field']] > 0 and s['kind'] not in terminal:
                    s['links'].append(dict(to=lim['ending'], label=lim['hook_label'], cond=f'limit:{st["name"]}'))

    # ------------------------------------------------------------------
    def overlay_attr(self, name, default=None):
        for _, ns in self.overlay_ns:
            if name in ns:
                return ns[name]
        return default

    def printed_links(self, s):
        """Links the prose must carry as tokens (not hidden, not global-rule)."""
        return [l for l in s['links'] if not C.is_hidden(l['cond']) and not C.is_global(l['cond'])]

    def incoming(self, include_global=False):
        inl = {}
        for s in self.S.values():
            for l in s['links']:
                if include_global or not C.is_global(l['cond']):
                    inl.setdefault(l['to'], []).append(s['key'])
        return inl


def load_book(cfg):
    return Book(cfg)
