"""Smoke test: the generic path (StoryBuilder, generic sheet + story map, coverless EPUB) works on
books/_template, so a new book starts from a skeleton that verifies and builds.

    python3 -m unittest -v tests.test_template
"""
import contextlib, io, os, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.dont_write_bytecode = True

from engine.config import load_config
from engine import verify, briefs, check_prose, build_book, build_epub, sheet, storymap, coverage

BOOK = os.path.join(ROOT, 'books', '_template')


def quiet(fn, *a, **k):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rv = fn(*a, **k)
    return rv, buf.getvalue()


class TestTemplate(unittest.TestCase):
    def test_pipeline(self):
        cfg = load_config(BOOK)
        m, _ = quiet(verify.run, cfg, quiet=True)
        self.assertEqual(m['report']['issues'], [])
        self.assertEqual({s['key']: s['num'] for s in m['sections']}['A01'], 1)
        # the Doom limit hook was added after A04 (+1 Doom)
        a04 = next(s for s in m['sections'] if s['key'] == 'A04')
        self.assertIn('limit:Doom', [l['cond'] for l in a04['links']])
        quiet(briefs.run, cfg)
        rc, out = quiet(check_prose.run, cfg)
        # skeleton prose is deliberately short: only SHORT problems are allowed
        probs = [l for l in out.splitlines() if l.startswith('[')]
        self.assertTrue(probs and all(' SHORT ' in l for l in probs), out)
        quiet(build_book.run, cfg)
        quiet(storymap.run, cfg)
        rc, out = quiet(build_epub.run, cfg, validate=True)
        if 'not found' not in out:
            self.assertIn('0 fatals / 0 errors / 0 warnings', out, out)
        d, _ = quiet(sheet.run, cfg)
        self.assertEqual(len(d['sec']), cfg['sections']['count'])
        (routes, missing), _ = quiet(coverage.run, cfg)
        self.assertEqual(missing, [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
