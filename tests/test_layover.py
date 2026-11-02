"""Acceptance test: the engine reproduces THE LAYOVER.

    cd /home/claude/gamebook-engine && python3 -m unittest -v tests.test_layover
    (or: python3 -m pytest tests/)

Reference implementation (read only): $LAYOVER_REF, default /home/claude/layover.
Checks:
  1. verify: ISSUES 0, and key -> number identical to the shipped layover_book.json
  2. check: every zone prints OK
  3. epub: EPUBCheck 0 fatals / 0 errors / 0 warnings, and per-section text (and every front/back
     page) identical to the shipped dist/the-layover.epub
plus unit tests of the generic condition language and the alias table.
"""
import contextlib, io, json, os, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.dont_write_bytecode = True

from engine.config import load_config, read_json
from engine import verify, check_prose, build_book, build_epub, epubtext, conditions as C

BOOK = os.path.join(ROOT, 'books', 'the-layover')
REF = os.environ.get('LAYOVER_REF', '/home/claude/layover')


def quiet(fn, *a, **k):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rv = fn(*a, **k)
    return rv, buf.getvalue()


class TestLayover(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg = load_config(BOOK)
        cls.map, _ = quiet(verify.run, cls.cfg, quiet=True)

    def test_1_verify_no_issues(self):
        self.assertEqual(self.map['report']['issues'], [])
        notes = ' '.join(self.map['report']['notes'])
        self.assertIn('Softlocked states: 0', notes)

    def test_2_numbering_identical(self):
        ref = read_json(os.path.join(REF, 'layover_book.json'))
        want = {s['key']: s['num'] for s in ref['sections']}
        got = {s['key']: s['num'] for s in self.map['sections']}
        self.assertEqual(got, want)

    def test_3_check_all_zones_ok(self):
        rc, out = quiet(check_prose.run, self.cfg)
        self.assertEqual(rc, 0, out)
        zones = list(self.cfg['zones'])
        for z in zones:
            self.assertIn(f'{z}: OK', out)

    def test_4_epub_valid_and_text_identical(self):
        quiet(build_book.run, self.cfg)
        rc, out = quiet(build_epub.run, self.cfg, validate=True)
        built = self.cfg.path(self.cfg['epub']['out'])
        if 'EPUBCheck: not found' in out:
            print('\n  (EPUBCheck jar or java not found: validation skipped)')
        else:
            self.assertIn('0 fatals / 0 errors / 0 warnings', out, out)
            self.assertEqual(rc, 0)
        a = epubtext.sections(built)
        b = epubtext.sections(os.path.join(REF, 'dist', 'the-layover.epub'))
        self.assertEqual(len(a), self.cfg['sections']['count'])
        self.assertEqual(sorted(a), sorted(b))
        diff = [n for n in a if a[n] != b[n]]
        self.assertEqual(diff, [], f'sections whose text differs: {diff[:20]}')
        pa, pb = epubtext.pages(built), epubtext.pages(os.path.join(REF, 'dist', 'the-layover.epub'))
        self.assertEqual({p: pa.get(p) for p in pb}, pb)

    def test_5_check_catches_broken_prose(self):
        from engine.graph import load_book
        book = load_book(self.cfg)
        book.all_flags = []
        prose = check_prose.load_prose(self.cfg)
        k = 'A02'
        bad = prose[k].replace('{' + book.S[k]['links'][0]['to'] + '}', '{A99}', 1)
        probs = check_prose.check_section(k, book.S[k], bad, self.cfg, book)
        self.assertTrue(any('TOKENS' in p for p in probs))


class TestConditions(unittest.TestCase):
    ALIASES = load_config(BOOK)['conditions']['aliases']

    def test_aliases(self):
        n = lambda c: C.normalize(c, self.ALIASES)
        self.assertEqual(n('claim3'), 'stat:Claim>=3')
        self.assertEqual(n('claim4&has:MARKED'), 'stat:Claim>=4&has:MARKED')
        self.assertEqual(n('hidden:TRANSFER&not:FORGOT&claimlow'), 'hidden:TRANSFER&not:FORGOT&stat:Claim<=2')
        self.assertEqual(n('claimlimit'), 'limit:Claim')
        self.assertEqual(n('fearlimit'), 'limit:Fear')
        self.assertEqual(n('hours6'), 'stat:Hours>=6')
        self.assertIsNone(n(None))

    def test_evaluate(self):
        ev = C.evaluate
        self.assertTrue(ev('has:A&not:B', {'A'}))
        self.assertFalse(ev('has:A&not:B', {'A', 'B'}))
        self.assertTrue(ev('stat:Claim>=4', set(), {'Claim': 4}))
        self.assertFalse(ev('stat:Claim>=4', set(), {'Claim': 3}))
        self.assertTrue(ev('stat:Claim>=4', set()))                      # unknown stat: over-approximate
        self.assertFalse(ev('stat:Claim>=4', set(), unknown=False))
        self.assertTrue(ev('limit:Claim', set(), {'Claim': 5}, {'Claim': 5}))
        self.assertFalse(ev('limit:Claim', set(), {'Claim': 4}, {'Claim': 5}))
        self.assertTrue(ev('has:LOOSEFLAG', set(), loose={'LOOSEFLAG'}))
        self.assertFalse(ev('pass', set(), outcome='fail'))
        self.assertTrue(C.is_global('limit:Claim'))
        self.assertFalse(C.is_global('limit:Claim&has:X'))
        self.assertTrue(C.is_hidden('hidden:X&stat:Claim<=2'))
        with self.assertRaises(C.CondError):
            C.validate('claim3')                                       # un-aliased legacy atom


if __name__ == '__main__':
    unittest.main(verbosity=2)
