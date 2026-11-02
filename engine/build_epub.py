"""EPUB 3 builder (Kindle-ready) from build/book.json + book.json "epub" settings.

Front/back matter pages come from config: each page is one of
    {"file", "title", "prose": "FRONT_KEY", "link_section1": true}   markdown-ish prose from prose/*.json
    {"file", "title", "sheet": true}                                  Adventure Sheet built from epub.sheet
    {"file", "title", "html": "<p>...</p>"} or {"html_file": "front/x.html"}
Optional "nav" overrides the contents label. {{placeholders}} (title, author, year, ...) are filled.
Section text: {KEY} tokens -> links, **bold**, *italic*, '*If ...,*' paragraphs -> class cond,
foe lines 'NAME   STAT n   STAT n' -> stat box, '- ' lists, # headings.
"""
import datetime, glob, html, os, re, shutil, subprocess, uuid, zipfile

from .config import read_text

from .build_book import load, checkpoints
from .config import fill

CSS = """
body { font-family: serif; line-height: 1.45; margin: 0 4%; }
h1 { text-align: center; font-size: 1.8em; margin: 2em 0 0.3em; letter-spacing: 0.08em; }
h2 { font-size: 1.3em; margin: 1.6em 0 0.6em; }
h3 { font-size: 1.1em; margin: 1.2em 0 0.4em; }
p { margin: 0 0 0.8em; text-indent: 0; }
p.choice { margin-left: 1.2em; }
p.foe { text-align: center; font-family: sans-serif; letter-spacing: 0.08em; border: 1px solid #555; padding: 0.5em; margin: 1em 15%; }
p.cond { margin-left: 0.8em; padding-left: 0.7em; border-left: 2px solid #999; }
.sec { page-break-before: always; break-before: page; }
h2.num { text-align: center; font-size: 1.7em; font-family: sans-serif; letter-spacing: 0.06em; margin: 1.4em 0 1em; }
h2.num img { height: 0.8em; width: auto; vertical-align: baseline; margin-left: 0.25em; }
.center { text-align: center; }
.small { font-size: 0.85em; }
.title-big { font-size: 2.6em; letter-spacing: 0.12em; margin-top: 3em; text-align: center; font-family: sans-serif; }
.sub { text-align: center; font-style: italic; margin-bottom: 3em; }
table.sheet { width: 100%; border-collapse: collapse; margin: 0.6em 0 1.2em; }
table.sheet td, table.sheet th { border: 1px solid #555; padding: 0.4em; vertical-align: top; text-align: left; }
table.sheet th { width: 34%; font-family: sans-serif; font-size: 0.9em; }
.box { height: 4em; }
.end { text-align: center; font-family: sans-serif; letter-spacing: 0.2em; margin-top: 2em; }
"""

COPYRIGHT = """<p class="small">Copyright © {{year}} {{author}}. All rights reserved.</p>
<p class="small">Published by {{publisher}}.</p>
<p class="small">This is a work of fiction. {{fiction_note}} Any resemblance to actual persons, living or dead, or to actual events is coincidental.</p>
<p class="small">No part of this book may be reproduced in any form without written permission from the author, except for brief quotations in a review.</p>"""

MEDIA = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.svg': 'image/svg+xml'}


def page(title, body, lang='en', cls=''):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{lang}" xml:lang="{lang}">
<head><meta charset="utf-8"/><title>{html.escape(title)}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body{(' class="' + cls + '"') if cls else ''}>
{body}
</body></html>"""


class Renderer:
    def __init__(self, bykey, per_file, foe_stats):
        self.bykey, self.per_file = bykey, per_file
        st = r'\s{2,}'.join(rf'{re.escape(n)} (\d+)' for n in foe_stats)
        self.foe_names = foe_stats
        self.foe_re = re.compile(rf'^([A-Z][A-Z \-]+?)\s{{2,}}{st}$') if foe_stats else None

    def fname(self, num):
        return f'sec{(num - 1) // self.per_file + 1:02d}.xhtml'

    def href(self, key, here=None):
        n = self.bykey[key]['num']
        f = self.fname(n)
        return (f'#s{n}' if f == here else f'{f}#s{n}'), n

    def inline(self, t, here):
        t = html.escape(t, quote=False)
        t = re.sub(r'\{([A-Za-z0-9_]+)\}', lambda m: '<a href="%s">%d</a>' % self.href(m.group(1), here), t)
        t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
        t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
        return t

    def md(self, text, here=None):
        out = []
        for p in re.split(r'\n\s*\n', text.strip()):
            p = p.strip()
            if not p:
                continue
            m = re.match(r'^(#{1,3})\s+(.*)$', p)
            if m:
                lvl = len(m.group(1)) + 1
                out.append(f'<h{lvl}>{self.inline(m.group(2), here)}</h{lvl}>')
                continue
            fm = self.foe_re.match(p) if self.foe_re else None
            if fm:
                stats = ' &#160;&#160;&#183;&#160;&#160; '.join(f'{n} {fm.group(i + 2)}' for i, n in enumerate(self.foe_names))
                out.append(f'<p class="foe"><strong>{fm.group(1).strip()}</strong><br/>{stats}</p>')
                continue
            lines = [self.inline(l.strip(), here) for l in p.split('\n')]
            if all(re.match(r'^[-•]\s', l) for l in p.split('\n')):
                out.append('<ul>' + ''.join(f'<li>{l[2:]}</li>' for l in lines) + '</ul>')
                continue
            if re.match(r'^\*If [^*]+\*', p) and not ('{' in p and len(p.split()) < 40):
                out.append('<p class="cond">' + '<br/>'.join(lines) + '</p>')
                continue
            cls = ' class="choice"' if re.match(r'^(If |Turn to |Test your|Otherwise)', p) and '{' in p else ''
            out.append(f'<p{cls}>' + '<br/>'.join(lines) + '</p>')
        return '\n'.join(out)


def sheet_page(cfg, ec):
    sc = ec.get('sheet', {})
    parts = ['<h2>Adventure Sheet</h2>']
    if sc.get('digital_url'):
        parts.append(f"<h3>The digital sheet</h3>\n<p>{html.escape(sc.get('digital_text', ''), quote=False)}</p>\n"
                     f"<p class=\"center\"><a href=\"{html.escape(sc['digital_url'])}\">{html.escape(sc.get('digital_label', sc['digital_url']))}</a></p>")
        if sc.get('qr'):
            parts.append(f'<p class="center"><img src="{os.path.basename(sc["qr"])}" alt="QR code for the digital Adventure Sheet" style="width:40%;max-width:12em;height:auto"/></p>')
        parts.append('<h3>The paper sheet</h3>')
    if sc.get('paper_text'):
        parts.append(f'<p class="small">{html.escape(sc["paper_text"], quote=False)}</p>')
    rows = ''.join(f'<tr><th>{html.escape(a, quote=False)}</th><td{"" if b else " class=\"box\""}>{html.escape(b, quote=False)}</td></tr>\n' for a, b in sc.get('rows', []))
    parts.append(f'<table class="sheet">\n{rows}</table>')
    if sc.get('back_html'):
        parts.append(read_text(cfg.path(sc['back_html'])).strip())
    return fill('\n'.join(parts), cfg)


def find_epubcheck(cfg):
    jar = cfg.get('epubcheck', {}).get('jar') or os.environ.get('EPUBCHECK_JAR')
    if jar and os.path.exists(jar):
        return jar
    for pat in ('/usr/share/java/epubcheck*.jar', os.path.expanduser('~/epubcheck*/epubcheck.jar'), '/opt/epubcheck*/epubcheck.jar',
                '/tmp/**/epubcheck.jar'):
        hits = glob.glob(pat, recursive=True)
        if hits:
            return hits[0]
    try:
        out = subprocess.run(['find', '/', '-name', 'epubcheck*.jar', '-not', '-path', '/proc/*'], capture_output=True, text=True, timeout=60).stdout.split()
        return out[0] if out else None
    except Exception:
        return None


def epubcheck(path, cfg):
    jar = find_epubcheck(cfg)
    if not jar or not shutil.which('java'):
        print('EPUBCheck: not found (set epubcheck.jar in book.json or EPUBCHECK_JAR); skipped')
        return None
    r = subprocess.run(['java', '-jar', jar, path], capture_output=True, text=True)
    out = r.stdout + r.stderr
    m = re.search(r'Messages: (\d+) fatals? / (\d+) errors? / (\d+) warnings?', out)
    summary = m.group(0) if m else out.strip().splitlines()[-1:]
    print('EPUBCheck:', summary)
    for line in out.splitlines():
        if line.startswith(('ERROR', 'FATAL', 'WARNING')):
            print('  ' + line)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else (r.returncode, 0, 0)


def run(cfg, validate=True):
    book = load(cfg)
    b = cfg.get('book', {})
    ec = cfg.get('epub', {})
    lang = b.get('language', 'en')
    secs = sorted(book['sections'], key=lambda s: s['num'])
    bykey = {s['key']: s for s in secs}
    R = Renderer(bykey, ec.get('per_file', 20), ec.get('foe_stats', []))
    cps = checkpoints(cfg, secs)
    year = datetime.date.today().year
    ph = dict(year=year, title=b.get('title', ''), author=b.get('author', ''), publisher=b.get('publisher', ''),
              fiction_note=b.get('fiction_note', 'Names, characters, places and incidents are the product of the author\'s imagination.'))

    files = {}
    files['title.xhtml'] = ('Title', f"""<p class="title-big">{html.escape(b.get('title', '').upper())}</p>
<p class="sub">{html.escape(b.get('subtitle', ''))}</p>
<p class="center">{html.escape(b.get('author', ''))}</p>
<p class="center small">{html.escape(b.get('publisher', '').upper())}</p>""")
    files['copyright.xhtml'] = ('Copyright', fill(ec.get('copyright_html', COPYRIGHT), cfg, **{k: html.escape(str(v), quote=False) for k, v in ph.items()}))

    def matter(spec):
        if spec.get('prose'):
            body = R.md(fill(book['front'][spec['prose']], cfg, **ph), spec['file'])
            if spec.get('link_section1'):
                body = body.replace('section 1', f'<a href="{R.fname(1)}#s1">section 1</a>')
        elif spec.get('sheet'):
            body = sheet_page(cfg, ec)
        elif spec.get('html_file'):
            body = fill(read_text(cfg.path(spec['html_file'])), cfg, **ph)
        else:
            body = fill(spec.get('html', ''), cfg, **ph)
        files[spec['file']] = (spec['title'], body)

    front_specs, back_specs = ec.get('front', []), ec.get('back', [])
    for spec in front_specs:
        matter(spec)

    icon = ec.get('checkpoint_icon')
    groups = {}
    for s in secs:
        groups.setdefault(R.fname(s['num']), []).append(s)
    for f, ss in groups.items():
        parts = []
        for s in ss:
            n = s['num']
            mark = f' <img src="{os.path.basename(icon)}" alt="(checkpoint)"/>' if (icon and s['key'] in cps) else ''
            body = R.md(s['text'] or '', f)
            if s['kind'] == 'ending':
                body += '\n<p class="end">' + html.escape(ec.get('end_marker', 'THE END')) + '</p>'
            parts.append(f'<div class="sec"><h2 class="num" id="s{n}">{n}{mark}</h2>\n{body}\n</div>')
        files[f] = (f"Sections {ss[0]['num']}–{ss[-1]['num']}", '\n'.join(parts))
    for spec in back_specs:
        matter(spec)

    order = ['title.xhtml', 'copyright.xhtml'] + [s['file'] for s in front_specs] + sorted(groups) + [s['file'] for s in back_specs]
    nav_items = [(s['file'], s.get('nav', s['title'])) for s in front_specs] + \
                [(g, ('Begin: sections ' if g == R.fname(1) else 'Sections ') + f"{groups[g][0]['num']}–{groups[g][-1]['num']}") for g in sorted(groups)] + \
                [(s['file'], s.get('nav', s['title'])) for s in back_specs]
    first = front_specs[0]['file'] if front_specs else R.fname(1)

    out = cfg.path(ec.get('out', f"dist/{b.get('slug', 'book')}.epub"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    uid = 'urn:uuid:' + str(uuid.uuid5(uuid.NAMESPACE_URL, f"{b.get('slug', 'book')}-{b.get('author', '')}"))
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    T = html.escape(b.get('title', ''))
    nav = page('Contents', '<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>' +
               ''.join(f'<li><a href="{h}">{html.escape(t)}</a></li>' for h, t in nav_items) + '</ol></nav>' +
               f'<nav epub:type="landmarks" hidden=""><ol>{"<li><a epub:type=\"cover\" href=\"cover.xhtml\">Cover</a></li>" if ec.get("cover") else ""}<li><a epub:type="toc" href="nav.xhtml">Contents</a></li><li><a epub:type="bodymatter" href="{first}">Start</a></li></ol></nav>', lang)
    ncx = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1"><head><meta name="dtb:uid" content="{uid}"/></head>
<docTitle><text>{T}</text></docTitle><navMap>""" + ''.join(
        f'<navPoint id="n{i}" playOrder="{i + 1}"><navLabel><text>{html.escape(t)}</text></navLabel><content src="{h}"/></navPoint>'
        for i, (h, t) in enumerate(nav_items)) + '</navMap></ncx>'

    images = []   # (path on disk, name in book, id, props)
    cover = cfg.path(ec['cover']) if ec.get('cover') else None
    if cover:
        images.append((cover, 'cover' + os.path.splitext(cover)[1], 'coverimg', ' properties="cover-image"'))
    if icon:
        images.append((cfg.path(icon), os.path.basename(icon), 'cpicon', ''))
    for i, p in enumerate(ec.get('images', [])):
        images.append((cfg.path(p), os.path.basename(p), f'img{i}', ''))
    for p, *_ in images:
        if not os.path.exists(p):
            raise SystemExit(f'epub: missing image {p}')
    manifest = ['<item id="css" href="style.css" media-type="text/css"/>',
                '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>']
    for p, name, iid, props in images:
        manifest.append(f'<item id="{iid}" href="{name}" media-type="{MEDIA[os.path.splitext(name)[1].lower()]}"{props}/>')
    spine = ['<itemref idref="nav"/>']
    if cover:
        manifest.append('<item id="coverpage" href="cover.xhtml" media-type="application/xhtml+xml"/>')
        spine.insert(0, '<itemref idref="coverpage" linear="yes"/>')
    for i, f in enumerate(order):
        manifest.append(f'<item id="f{i}" href="{f}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="f{i}"/>')
    subjects = ''.join(f'<dc:subject>{html.escape(s)}</dc:subject>\n' for s in b.get('subjects', []))
    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{lang}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{uid}</dc:identifier>
<dc:title>{T}</dc:title>
<dc:creator>{html.escape(b.get('author', ''))}</dc:creator>
<dc:publisher>{html.escape(b.get('publisher', ''))}</dc:publisher>
<dc:language>{lang}</dc:language>
{subjects}<dc:description>{html.escape(b.get('description', b.get('subtitle', '')))}</dc:description>
<meta property="dcterms:modified">{now}</meta>
{'<meta name="cover" content="coverimg"/>' if cover else ''}
</metadata>
<manifest>{''.join(manifest)}</manifest>
<spine toc="ncx">{''.join(spine)}</spine>
</package>"""

    with zipfile.ZipFile(out, 'w') as z:
        z.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        D = zipfile.ZIP_DEFLATED
        z.writestr('META-INF/container.xml', '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>', compress_type=D)
        z.writestr('OEBPS/content.opf', opf, compress_type=D)
        z.writestr('OEBPS/nav.xhtml', nav, compress_type=D)
        z.writestr('OEBPS/toc.ncx', ncx, compress_type=D)
        z.writestr('OEBPS/style.css', CSS + ec.get('extra_css', ''), compress_type=D)
        if cover:
            z.writestr('OEBPS/cover.xhtml', page('Cover', f'<div style="text-align:center"><img src="{images[0][1]}" alt="Cover" style="max-width:100%;height:auto"/></div>', lang), compress_type=D)
        for p, name, *_ in images:
            z.write(p, f'OEBPS/{name}')
        for f in order:
            t, body = files[f]
            z.writestr(f'OEBPS/{f}', page(t, body, lang), compress_type=D)
    print('wrote', os.path.relpath(out, cfg.dir), os.path.getsize(out) // 1024, 'KB')
    if validate:
        res = epubcheck(out, cfg)
        if res and any(res):
            return 1
    return 0
