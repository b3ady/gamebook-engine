"""Render the book's cover HTML to a Kindle cover (1600x2560 JPEG).

book.json: "cover": {"template": "templates/cover.html", "out": "assets/cover.jpg", "width": 1600, "height": 2560}
The template may use {{title}}, {{author}}, {{subtitle}} (and the legacy AUTHOR_NAME). Cover art is
bespoke per book (see METHOD.md stage 10): design it as HTML/SVG, then render it here.
Needs Playwright + Chromium and Pillow (the only non-stdlib dependencies in the engine).
"""
import os

from .config import fill, read_text, write_text


def run(cfg):
    cc = cfg.get('cover') or {}
    if not cc.get('template'):
        raise SystemExit('book.json has no cover.template')
    try:
        from playwright.sync_api import sync_playwright
        from PIL import Image
    except ImportError as e:
        raise SystemExit(f'cover needs playwright and Pillow: {e}')
    W, H = cc.get('width', 1600), cc.get('height', 2560)
    src = fill(read_text(cfg.path(cc['template'])), cfg).replace('AUTHOR_NAME', cfg.get_in('book.author', '').upper())
    os.makedirs(cfg.path('build'), exist_ok=True)
    tmp = cfg.path('build', '_cover.html')
    write_text(tmp, src)
    png = cfg.path('build', 'cover.png')
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': W, 'height': H})
        pg.goto('file://' + tmp)
        pg.wait_for_timeout(cc.get('wait_ms', 400))
        pg.screenshot(path=png, clip={'x': 0, 'y': 0, 'width': W, 'height': H})
        b.close()
    out = cfg.path(cc.get('out', 'assets/cover.jpg'))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    Image.open(png).convert('RGB').save(out, quality=92)
    print('wrote', os.path.relpath(out, cfg.dir), f'{W}x{H}')
