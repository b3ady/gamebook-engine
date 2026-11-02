"""Extract plain text per section (and per front/back page) from an EPUB built by this engine
(or by the original Layover pipeline). Used by the acceptance test and for diffing releases:

    python3 -m engine.epubtext a.epub b.epub      # prints differing sections
"""
import html, re, sys, zipfile


def _plain(x):
    x = re.sub(r'<img[^>]*>', '', x)
    x = re.sub(r'<br\s*/?>', ' ', x)
    x = re.sub(r'</(p|h\d|li|tr|div)>', '\n', x)
    x = re.sub(r'<[^>]+>', '', x)
    x = html.unescape(x)
    return re.sub(r'\s+', ' ', x).strip()


def sections(path):
    z = zipfile.ZipFile(path)
    out = {}
    for n in sorted(z.namelist()):
        if not re.match(r'OEBPS/sec\d+\.xhtml$', n):
            continue
        t = z.read(n).decode('utf-8')
        for m in re.finditer(r'<div class="sec"><h2 class="num" id="s(\d+)">.*?</h2>(.*?)</div>\s*(?=<div class="sec">|</body>)', t, re.S):
            out[int(m.group(1))] = _plain(m.group(2))
    return out


def pages(path):
    z = zipfile.ZipFile(path)
    out = {}
    for n in z.namelist():
        if n.startswith('OEBPS/') and n.endswith('.xhtml') and not re.match(r'OEBPS/sec\d+\.xhtml$', n):
            t = z.read(n).decode('utf-8')
            body = re.search(r'<body[^>]*>(.*)</body>', t, re.S)
            out[n[6:]] = _plain(body.group(1) if body else t)
    return out


if __name__ == '__main__':
    a, b = sections(sys.argv[1]), sections(sys.argv[2])
    diff = [n for n in sorted(set(a) | set(b)) if a.get(n) != b.get(n)]
    print(f'{len(a)} vs {len(b)} sections; {len(diff)} differ', diff[:30])
    pa, pb = pages(sys.argv[1]), pages(sys.argv[2])
    print('pages differing:', [p for p in sorted(set(pa) | set(pb)) if pa.get(p) != pb.get(p)])
