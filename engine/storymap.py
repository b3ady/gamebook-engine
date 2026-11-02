"""Story-map HTML (for the author and reviewers): build/book.json embedded in a template.

Template: book.json storymap.template (book-specific) or engine/templates/storymap.html (generic).
The template must contain the placeholder __DATA__ (and may use __TITLE__)."""
import html, json, os

from .config import read_text, write_text

from .build_book import load

HERE = os.path.dirname(os.path.abspath(__file__))


def run(cfg):
    d = load(cfg)
    sm = cfg.get('storymap', {})
    tpl_path = cfg.path(sm['template']) if sm.get('template') else os.path.join(HERE, 'templates', 'storymap.html')
    t = read_text(tpl_path)
    js = json.dumps(d, separators=(',', ':'), ensure_ascii=False).replace('</', '<\\/')
    out = cfg.path('build', sm.get('out', 'story-map.html'))
    write_text(out, t.replace('__TITLE__', html.escape(cfg.get_in('book.title', ''))).replace('__DATA__', js))
    print('wrote', os.path.relpath(out, cfg.dir), os.path.getsize(out) // 1024, 'KB')
