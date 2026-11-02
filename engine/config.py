"""Book configuration: <book_dir>/book.json (JSON with full-line // comments allowed)."""
import json, os, re


class Config(dict):
    """A dict with attribute access for top-level keys and a few helpers."""

    def __init__(self, data, book_dir):
        super().__init__(data)
        self.dir = os.path.abspath(book_dir)

    def path(self, *parts):
        return os.path.join(self.dir, *parts)

    def get_in(self, dotted, default=None):
        cur = self
        for p in dotted.split('.'):
            if not isinstance(cur, dict) or p not in cur:
                return default
            cur = cur[p]
        return cur

    # ---- convenience views -------------------------------------------------
    @property
    def stats(self):
        """List of stat dicts: {name, field?, floor?, cap?, start?, limit?, report_min?, must_state?}."""
        return self.get('stats', [])

    def stat(self, name):
        for s in self.stats:
            if s['name'].lower() == name.lower():
                return s
        raise KeyError(f'unknown stat {name!r} (declare it under "stats" in book.json)')

    @property
    def stat_fields(self):
        """Section fields that carry per-section stat deltas (e.g. fear, vig, claim)."""
        return [s['field'] for s in self.stats if s.get('field')]

    @property
    def flags(self):
        return self.get('flags', {})

    def display(self, flag):
        return self.flags.get('display', {}).get(flag, flag)

    @property
    def hidden_flags(self):
        return set(self.flags.get('hidden', []))


def strip_comments(text):
    return '\n'.join(l for l in text.splitlines() if not l.lstrip().startswith('//'))


def load_config(book_dir):
    p = os.path.join(book_dir, 'book.json')
    if not os.path.exists(p):
        raise SystemExit(f'No book.json in {book_dir}')
    try:
        data = json.loads(strip_comments(read_text(p)))
    except json.JSONDecodeError as e:
        raise SystemExit(f'book.json: {e}')
    return Config(data, book_dir)


def fill(template, cfg, **extra):
    """Replace {{placeholders}} with config values (title, author, ... or dotted paths) and extras."""
    vals = dict(extra)

    def rep(m):
        k = m.group(1).strip()
        if k in vals:
            return str(vals[k])
        v = cfg.get_in(k)
        if v is None:
            v = cfg.get_in('book.' + k)
        return '' if v is None else str(v)
    return re.sub(r'\{\{([^}]+)\}\}', rep, template)


# ---- small file helpers (always close files; UTF-8) ----
def read_text(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def write_text(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def read_json(p):
    return json.loads(read_text(p))


def write_json(p, obj, **kw):
    kw.setdefault('ensure_ascii', False)
    write_text(p, json.dumps(obj, **kw))
