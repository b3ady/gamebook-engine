"""Generic link-condition language.

A condition is a list of atoms joined with '&' (all must hold). Atoms:

    has:FLAG          the reader holds codeword/item FLAG
    not:FLAG          the reader does not hold FLAG
    hidden:FLAG       like has:, but the link is a puzzle: never printed as a token
    pass | fail       outcome of a test (Nerve, Fortune, ...)
    win  | lose       outcome of a fight
    stat:NAME<op>N    stat comparison, op in >= <= > < == !=   e.g. stat:Claim>=4, stat:Hours>=6
    limit:NAME        the stat has reached its configured limit (a global rule, e.g. Claim 5 -> Final Call)

A link whose atoms are all limit: atoms is a *global-rule* link: it is checked by the verifier
but never written into prose (the rules page covers it).

Old book-specific atoms (claim3, hours6, ...) are rewritten through the book's alias table
(book.json -> conditions.aliases), e.g. {"claim3": "stat:Claim>=3", "claimlimit": "limit:Claim"}.
"""
import operator, re

OUTCOMES = ('pass', 'fail', 'win', 'lose')
OPS = {'>=': operator.ge, '<=': operator.le, '>': operator.gt, '<': operator.lt, '==': operator.eq, '!=': operator.ne}
STAT_RE = re.compile(r'^stat:([A-Za-z_][\w ]*?)(>=|<=|==|!=|>|<)(-?\d+)$')


class CondError(ValueError):
    pass


def atoms(cond):
    return [a for a in (cond or '').split('&') if a]


def normalize(cond, aliases):
    """Rewrite alias atoms into the generic form. Returns None for an empty condition."""
    if not cond:
        return None
    out = []
    for a in atoms(cond):
        rep = aliases.get(a, a)
        out.extend(atoms(rep))
    return '&'.join(out) or None


def parse_atom(a):
    """-> (kind, payload). kinds: flag(op, name) | outcome | stat(name, op, n) | limit(name)."""
    if a in OUTCOMES:
        return ('outcome', a)
    if a.startswith(('has:', 'not:', 'hidden:')):
        op, f = a.split(':', 1)
        return ('flag', ('has' if op == 'hidden' else op, f))
    m = STAT_RE.match(a)
    if m:
        return ('stat', (m.group(1), m.group(2), int(m.group(3))))
    if a.startswith('limit:'):
        return ('limit', a[6:])
    raise CondError(f'unknown condition atom {a!r} (add an alias in book.json conditions.aliases?)')


def validate(cond):
    for a in atoms(cond):
        parse_atom(a)


def is_hidden(cond):
    return bool(cond) and cond.startswith('hidden:')


def is_global(cond):
    """True if the link is a global-rule link (only limit: atoms) - never printed."""
    a = atoms(cond)
    return bool(a) and all(x.startswith('limit:') for x in a)


def is_outcome(cond):
    return any(x in OUTCOMES for x in atoms(cond))


def flags_used(cond):
    return [parse_atom(a)[1][1] for a in atoms(cond) if parse_atom(a)[0] == 'flag']


def stats_used(cond):
    out = []
    for a in atoms(cond):
        k, p = parse_atom(a)
        if k == 'stat':
            out.append(p[0])
        elif k == 'limit':
            out.append(p)
    return out


def evaluate(cond, flags, stats=None, limits=None, loose=(), unknown=True, outcome=None):
    """Evaluate a condition.

    flags   : set of held flags
    stats   : {stat name: value} for stats whose value is known; others count as unknown
    limits  : {stat name: limit value} (a limit of None = dynamic/unknown)
    loose   : flags treated as unknown (both branches open)
    unknown : value returned for an atom whose truth is unknown (True = over-approximate)
    outcome : if given, the test/fight outcome actually rolled ('pass', 'fail', ...)
    """
    stats = stats or {}
    limits = limits or {}
    for a in atoms(cond):
        kind, p = parse_atom(a)
        if kind == 'outcome':
            if outcome is not None and p != outcome:
                return False
            continue
        if kind == 'flag':
            op, f = p
            if f in loose:
                if not unknown:
                    return False
                continue
            if op == 'has' and f not in flags:
                return False
            if op == 'not' and f in flags:
                return False
            continue
        if kind == 'stat':
            name, op, n = p
            if name not in stats:
                if not unknown:
                    return False
                continue
            if not OPS[op](stats[name], n):
                return False
            continue
        if kind == 'limit':
            if p not in stats or limits.get(p) is None:
                if not unknown:
                    return False
                continue
            if stats[p] < limits[p]:
                return False
    return True


def describe(cond, display=lambda f: f):
    """Human-readable condition for briefs and maps."""
    if not cond:
        return ''
    out = []
    for a in atoms(cond):
        kind, p = parse_atom(a)
        if kind == 'outcome':
            out.append({'pass': 'test passed', 'fail': 'test failed', 'win': 'fight won', 'lose': 'fight lost'}[p])
        elif kind == 'flag':
            op, f = p
            pre = 'hidden: has ' if a.startswith('hidden:') else ('has ' if op == 'has' else 'lacks ')
            out.append(pre + display(f))
        elif kind == 'stat':
            name, op, n = p
            out.append(f'{name} {op.replace(">=", "≥").replace("<=", "≤")} {n}')
        else:
            out.append(f'{p} at its limit')
    return ' and '.join(out)
