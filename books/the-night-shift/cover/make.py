"""Cover v2: two-ink risograph-style print. The too-tall passenger, head out of frame, holds an arrivals name card hand-lettered THE LAYOVER."""
import math, random, sys, os
random.seed(179)
AUTHOR = (sys.argv[1] if len(sys.argv) > 1 else 'Corvin Wake').upper()
W, H = 1600, 2560
PAPER, INK, RED, CARD = '#ece3cf', '#1b2130', '#e0482f', '#f8f4ea'

# --- hand-marker alphabet (strokes in a 100x140 box) ---
def oval(cx=50, cy=70, rx=50, ry=70, n=22):
    return [(cx + rx*math.cos(2*math.pi*i/n - math.pi/2), cy + ry*math.sin(2*math.pi*i/n - math.pi/2)) for i in range(n+1)]
G = {
 'T': [[(0,2),(100,0)], [(50,0),(52,140)]],
 'H': [[(2,0),(0,140)], [(100,0),(98,140)], [(0,72),(100,68)]],
 'E': [[(98,2),(2,0),(0,140),(100,138)], [(0,70),(78,68)]],
 'L': [[(2,0),(0,140),(96,138)]],
 'A': [[(0,140),(50,0),(100,140)], [(22,88),(80,86)]],
 'Y': [[(0,0),(50,72)], [(100,2),(50,72),(48,140)]],
 'O': [oval()],
 'V': [[(0,0),(50,140),(100,2)]],
 'N': [[(0,140),(2,0),(98,140),(100,0)]],
 'I': [[(50,0),(50,140)]],
 'S': [[(96,18),(70,2),(30,2),(4,22),(6,52),(40,68),(80,78),(98,104),(92,128),(62,140),(24,138),(0,118)]],
 'F': [[(98,2),(2,0),(0,140)], [(0,70),(78,68)]],
 'G': [[(50+50*math.cos(a),70+70*math.sin(a)) for a in [math.radians(t) for t in range(-40,-360,-20)]]+[(100,82),(58,80)]],
 'R': [[(0,140),(2,0),(62,0),(88,14),(96,38),(86,60),(62,72),(2,72)], [(48,72),(100,140)]],
}
def jit(p, a=3.0): return (p[0] + random.uniform(-a, a), p[1] + random.uniform(-a, a))
def word(text, x, y, scale, sw, color, tilt=0.0, gap=34):
    out = []; cx = x
    for ch in text:
        if ch == ' ': cx += 60*scale; continue
        for stroke in G[ch]:
            pts = [jit(p) for p in stroke]
            d = 'M' + ' L'.join(f'{cx+px*scale:.1f},{y+py*scale + (cx-x)*tilt:.1f}' for px, py in pts)
            out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')
            # second, thinner pass: the pen going over itself
            d2 = 'M' + ' L'.join(f'{cx+px*scale+random.uniform(-2,2):.1f},{y+py*scale+(cx-x)*tilt+random.uniform(-2,2):.1f}' for px, py in pts)
            out.append(f'<path d="{d2}" fill="none" stroke="{color}" stroke-width="{sw*0.55:.1f}" stroke-linecap="round" opacity=".55"/>')
        cx += (100 + gap)*scale
    return '\n'.join(out), cx

def wobble(points, a=6):
    return ' '.join(f'{x+random.uniform(-a,a):.1f},{y+random.uniform(-a,a):.1f}' for x, y in points)


# --- red layer: hospital floor lines running away, and the torch ---
red = []
vpx, vpy = 800, 1500
for i in (-3, -1, 1, 3):
    xb = 800 + i*260
    red.append(f'<path d="M{vpx + i*14},{vpy} L{xb:.0f},{H}" stroke="{RED}" stroke-width="{20 if abs(i)==1 else 9}" fill="none"/>')
y, step = vpy + 30, 30
while y < H:
    yy = y + random.uniform(-3, 3)
    red.append(f'<path d="M0,{yy:.0f} L{W},{yy+random.uniform(-4,4):.0f}" stroke="{RED}" stroke-width="3" fill="none" opacity=".5"/>')
    step *= 1.4; y += step
red.append(f'<rect x="0" y="0" width="{W}" height="{vpy-10}" fill="{RED}" opacity=".14"/>')
# the torch's red cone, falling across the floor towards you
red.append(f'<path d="M1150,1080 L1600,1900 L1600,2440 L1240,2440 Z" fill="{RED}" opacity=".55"/>')
red.append(f'<circle cx="1150" cy="1080" r="34" fill="{RED}"/>')

# --- ink layer: the Night Sister ---
ink = []
# dress, navy, long; shoulders square
dress = [(560,560),(1040,560),(1110,700),(1120,1100),(1180,2150),(980,2210),(800,2190),(620,2210),(420,2150),(480,1100),(490,700)]
ink.append(f'<polygon points="{wobble(dress,4)}" fill="{INK}"/>')
# head: a dark oval. Her face is never described.
ink.append(f'<ellipse cx="800" cy="420" rx="118" ry="140" fill="{INK}"/>')
ink.append(f'<polygon points="{wobble([(740,540),(860,540),(870,600),(730,600)],2)}" fill="{INK}"/>')
# arm out to the right holding the torch
ink.append(f'<polygon points="{wobble([(1040,600),(1110,700),(1170,1060),(1120,1090),(1040,800)],3)}" fill="{INK}"/>')
ink.append(f'<rect x="1120" y="1040" width="60" height="90" rx="10" fill="{INK}" transform="rotate(-18 1150 1085)"/>')
# other arm straight down
ink.append(f'<polygon points="{wobble([(490,700),(560,640),(520,1300),(450,1300)],3)}" fill="{INK}"/>')
# legs and plain black shoes
for lx in (720, 840):
    ink.append(f'<polygon points="{wobble([(lx,2190),(lx+40,2190),(lx+36,2350),(lx+6,2350)],1.5)}" fill="{INK}"/>')
    ink.append(f'<path d="M{lx-20},2366 Q{lx+20},2330 {lx+64},2366 Z" fill="{INK}"/>')

# paper-coloured details over the ink: winged cap, apron, buckle, fob watch upside down
paper = []
cap = [(660,330),(800,262),(940,330),(1010,300),(960,370),(800,350),(640,370),(590,300)]
paper.append(f'<polygon points="{wobble(cap,3)}" fill="{CARD}"/>')
apron = [(640,820),(960,820),(1010,2060),(590,2060)]
paper.append(f'<polygon points="{wobble(apron,4)}" fill="{CARD}"/>')
paper.append(f'<polygon points="{wobble([(660,620),(940,620),(960,820),(640,820)],3)}" fill="{CARD}"/>')
paper.append(f'<rect x="560" y="830" width="480" height="34" fill="{INK}"/>')
paper.append(f'<rect x="760" y="822" width="80" height="50" rx="6" fill="{CARD}" stroke="{INK}" stroke-width="8"/>')
paper.append(f'<circle cx="910" cy="700" r="20" fill="{INK}"/><path d="M910,700 L910,688" stroke="{CARD}" stroke-width="4"/>')

# --- the wristband: the title, written in by hand ---
cx0, cy0, cw, ch = 150, 1330, 1300, 300
card = [f'<g transform="rotate(-3 800 1480)">',
        f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" rx="40" fill="{CARD}" stroke="{INK}" stroke-width="6"/>',
        f'<rect x="{cx0+cw-170}" y="{cy0}" width="170" height="{ch}" rx="40" fill="{RED}" opacity=".85"/>']
for k in range(3):
    card.append(f'<circle cx="{cx0+cw-85}" cy="{cy0+70+k*80}" r="16" fill="{CARD}"/>')
t1, _ = word('THE', 230, 1372, 0.62, 13, INK, tilt=0.003, gap=36)
t2, _ = word('NIGHT SHIFT', 230, 1462, 0.74, 17, INK, tilt=-0.004, gap=22)
card += [t1, t2]
card.append(f'<text x="230" y="1612" font-family="Inter Display, Inter, sans-serif" font-weight="800" font-size="26" letter-spacing="5" fill="{RED}">WARD 0 · BED __ · NEXT OF KIN __</text>')
card.append('</g>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <filter id="rough" x="-5%" y="-5%" width="110%" height="110%">
    <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="7"/>
  </filter>
  <filter id="ink" x="-5%" y="-5%" width="110%" height="110%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3" result="g"/>
    <feColorMatrix in="g" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -0.5 1.9" result="speck"/>
    <feComposite in="SourceGraphic" in2="speck" operator="in"/>
  </filter>
  <filter id="paper">
    <feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="3" seed="11"/>
    <feColorMatrix type="matrix" values="0 0 0 0 0.35  0 0 0 0 0.3  0 0 0 0 0.22  0 0 0 0.13 0"/>
  </filter>
</defs>
<rect width="{W}" height="{H}" fill="{PAPER}"/>
<g style="mix-blend-mode:multiply" transform="translate(6,-4)" filter="url(#ink)"><g filter="url(#rough)">{''.join(red)}</g></g>
<g filter="url(#ink)"><g filter="url(#rough)">{''.join(ink)}</g></g>
<g filter="url(#rough)">{''.join(paper)}</g>
<g filter="url(#rough)">{''.join(card)}</g>
<rect x="0" y="2440" width="{W}" height="{H-2440}" fill="{PAPER}"/>
<rect width="{W}" height="{H}" filter="url(#paper)"/>
</svg>'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;background:{PAPER}}}
.c{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:"Inter Display",Inter,sans-serif;color:{INK}}}
.c svg{{position:absolute;inset:0}}
.top{{position:absolute;left:0;right:0;top:70px;text-align:center;font-weight:700;font-size:34px;letter-spacing:.3em;color:{INK};mix-blend-mode:normal}}
.bot{{position:absolute;left:0;right:0;bottom:22px;text-align:center}}
.tag{{margin-top:18px;font-size:30px;letter-spacing:.5em;opacity:.7}}
.sub{{font-weight:700;font-size:38px;letter-spacing:.38em;color:{INK}}}
.auth{{margin-top:0;font-weight:900;font-size:74px;letter-spacing:.2em;color:{INK}}}
</style></head><body><div class="c">{svg}
<div class="top">AN INTERACTIVE HORROR NOVEL<div class="tag">YOU CHOOSE. IT WAITS.</div></div>
<div class="bot"><div class="auth">{AUTHOR}</div></div>
</div></body></html>'''
open('/home/claude/gamebook-engine/books/the-night-shift/cover/cover.html', 'w').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
    pg.goto('file:///home/claude/gamebook-engine/books/the-night-shift/cover/cover.html'); pg.wait_for_timeout(600)
    pg.screenshot(path='/home/claude/gamebook-engine/books/the-night-shift/cover/cover.png'); b.close()
from PIL import Image
im = Image.open('/home/claude/gamebook-engine/books/the-night-shift/cover/cover.png').convert('RGB'); im.save('/home/claude/gamebook-engine/books/the-night-shift/cover/cover.jpg', quality=92)
im.resize((400, 640)).save('/home/claude/gamebook-engine/books/the-night-shift/cover/thumb.png')
print('ok')
