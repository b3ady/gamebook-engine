"""Playable web edition: one self-contained HTML page with the whole book and a live Adventure Sheet.

python3 -m engine <book_dir> webplay   -> build/play.html

Reads build/book.json (run `build` first). Section links become tappable numbers; effects recorded in the
structure (codewords, items, stat deltas, the clock) are applied automatically on arrival; tests and
fights get dice; limits raise a banner. The reader can always adjust any score by hand.
"""
import json, os, re

from .config import write_text


def run(cfg, quiet=False):
    bj = json.load(open(cfg.path('build', 'book.json')))
    secs = bj['sections']
    conf = bj.get('config', {})
    book = conf.get('book', cfg.get('book', {}))
    sc = cfg.get('sections', {})
    cps = set(sc.get('checkpoints_extra', []))
    for s in secs:
        if s['kind'] == 'death' and s.get('checkpoint') and s['checkpoint'] != 'LAST':
            cps.add(s['checkpoint'])
    stats = conf.get('stats', cfg.get('stats', []))
    data = dict(
        book=dict(title=book.get('title', ''), subtitle=book.get('subtitle', ''), author=book.get('author', '')),
        start=sc.get('start', 'A01'),
        sections={s['key']: dict(n=s['num'], k=s['kind'], t=s['text'], z=s.get('zone', ''),
                                 l=[[l['to'], l.get('cond') or ''] for l in s['links']],
                                 g=s.get('gain', []), x=s.get('lose', []),
                                 d={st['name']: s.get(st['field'], 0) for st in stats if st.get('field') and s.get(st['field'])},
                                 te=s.get('test'), cp=s.get('checkpoint'))
                  for s in secs},
        checkpoints=sorted(cps),
        stats=stats,
        clock=conf.get('clock', {}),
        flags=conf.get('flags', {}),
        variants=conf.get('variants', {}),
        front=bj.get('front', {}),
    )
    js = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    title = data['book']['title'] or 'Gamebook'
    html = TEMPLATE.replace('__TITLE__', title).replace('__DATA__', js)
    out = cfg.path('build', 'play.html')
    write_text(out, html)
    if not quiet:
        print(f'wrote build/play.html {len(html)//1024} KB')
    return out


TEMPLATE = r'''<title>__TITLE__</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=Inter:wght@500;700;800&display=swap">
<style>
:root{--bg:#f3eee4;--panel:#fbf8f1;--ink:#1d2230;--muted:#5d6271;--line:#d9d1c1;--accent:#c23b26;--accent-ink:#fff;--soft:#efe6d6;--good:#2f6b3a;color-scheme:light}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#11141b;--panel:#181c25;--ink:#e8e3d8;--muted:#9aa0ad;--line:#2b303c;--accent:#e2604a;--accent-ink:#11141b;--soft:#202532;--good:#7cc48a;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#11141b;--panel:#181c25;--ink:#e8e3d8;--muted:#9aa0ad;--line:#2b303c;--accent:#e2604a;--accent-ink:#11141b;--soft:#202532;--good:#7cc48a;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:"Source Serif 4",Georgia,serif;font-size:18px;line-height:1.6}
.wrap{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:28px;max-width:1080px;margin:0 auto;padding-block:24px 80px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
@media (max-width:860px){.wrap{grid-template-columns:minmax(0,1fr)}.sheet{order:-1}}
header.top{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:8px}
.brand{font-family:Inter,sans-serif;font-weight:800;letter-spacing:.18em;font-size:13px;color:var(--muted);text-transform:uppercase}
.tools{display:flex;gap:6px;flex-wrap:wrap}
button,.btn{font:600 13px Inter,sans-serif;letter-spacing:.04em;border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:8px;padding:7px 11px;cursor:pointer}
button:hover{border-color:var(--accent)}
button.primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
main{min-width:0}
.num{font:800 46px Inter,sans-serif;letter-spacing:.04em;margin:18px 0 4px;display:flex;align-items:center;gap:12px}
.num small{font:700 12px Inter,sans-serif;letter-spacing:.2em;color:var(--muted);text-transform:uppercase}
.num .cp{font-size:22px;color:var(--accent)}
.text p{margin:0 0 .9em;max-width:65ch}
.text p.cond{border-left:3px solid var(--line);padding-left:12px;color:var(--ink)}
.text p.cond.no{opacity:.45}
.text p.choice{margin-left:0}
.text h2{font:800 20px Inter,sans-serif;margin:1.4em 0 .4em}
a.go{font:800 15px Inter,sans-serif;display:inline-block;min-width:44px;text-align:center;padding:2px 9px;margin:0 2px;border-radius:7px;background:var(--accent);color:var(--accent-ink);text-decoration:none;cursor:pointer}
a.go.off{background:transparent;color:var(--muted);border:1px dashed var(--muted)}
.foe{font:700 14px Inter,sans-serif;letter-spacing:.08em;border:1px solid var(--line);border-radius:10px;padding:10px 14px;margin:1em 0;background:var(--panel);text-align:center}
.box{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:14px 0}
.box h3{font:800 12px Inter,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin:0 0 8px}
.banner{background:var(--accent);color:var(--accent-ink);border-radius:12px;padding:12px 16px;margin:14px 0;font:600 15px Inter,sans-serif}
.banner a.go{background:var(--accent-ink);color:var(--accent)}
.dice{font:800 22px Inter,sans-serif}
.sheet{min-width:0}
.sheet .box{position:sticky;top:12px}
.stat{display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid var(--line);font:600 14px Inter,sans-serif}
.stat:last-child{border-bottom:0}
.stat .v{font:800 18px Inter,sans-serif;min-width:52px;text-align:center}
.stat .pm button{padding:2px 9px;font-size:14px}
.boxes{display:flex;gap:5px;flex-wrap:wrap;margin:4px 0 2px}
.boxes span{width:24px;height:24px;border:1.5px solid var(--ink);border-radius:5px;display:inline-flex;align-items:center;justify-content:center;font:700 10px Inter,sans-serif;cursor:pointer}
.boxes span.on{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.lbl{font:600 11px Inter,sans-serif;color:var(--muted);letter-spacing:.06em}
.chips{display:flex;flex-wrap:wrap;gap:5px;margin-top:6px}
.chip{font:700 11px Inter,sans-serif;letter-spacing:.06em;background:var(--soft);border:1px solid var(--line);border-radius:999px;padding:3px 9px}
.goto{display:flex;gap:6px;margin-top:10px}
.goto input{width:90px;font:700 15px Inter,sans-serif;padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--ink)}
.setup label{display:block;margin:6px 0;font:600 15px Inter,sans-serif;cursor:pointer}
.small{font:500 13px Inter,sans-serif;color:var(--muted)}
.log{max-height:120px;overflow:auto;font:500 12px Inter,sans-serif;color:var(--muted)}
</style>
<div class="wrap">
 <main>
  <header class="top"><div class="brand" id="brand"></div>
   <div class="tools"><button id="bBack" title="Undo the last move">Back</button><button id="bRules">Rules</button><button id="bTheme">Theme</button><button id="bNew">New game</button></div></header>
  <div id="view"></div>
 </main>
 <aside class="sheet"><div class="box" id="sheet"></div></aside>
</div>
<script>
const D = __DATA__;
const S = D.sections, NUM = {}; for (const k in S) NUM[S[k].n] = k;
const STAT = {}; D.stats.forEach(s => STAT[s.name] = s);
const KEY = 'gb-' + (D.book.title || 'book').toLowerCase().replace(/\W+/g, '-');
let st = null, hist = [], view = 'play';
const store = { get(){ try { return JSON.parse(localStorage.getItem(KEY)); } catch(e){ return null; } },
                set(v){ try { localStorage.setItem(KEY, JSON.stringify(v)); } catch(e){} } };
const $ = id => document.getElementById(id);
const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
const d6 = () => 1 + Math.floor(Math.random() * 6);
const disp = f => (D.flags.display && D.flags.display[f]) || f.replace(/_/g, ' ');
const hidden = new Set([...(D.flags.hidden || []), ...(D.flags.loose || [])]);
const shown = f => !hidden.has(f) && !(D.variants.flags || []).includes(f);
const fearLimit = () => (st.stats.Nerve || 9) + 3;
const lim = name => { const s = STAT[name]; if (!s || !s.limit) return null; return s.limit.dynamic ? fearLimit() : s.limit.value; };
const limitEnding = name => STAT[name] && STAT[name].limit && STAT[name].limit.ending;

function newState(variant, mode){
  const stats = {}, start = {};
  for (const s of D.stats){
    let v = s.start || 0;
    if (s.story !== undefined) v = mode === 'story' ? s.story : roll(s.roll);
    stats[s.name] = v; start[s.name] = v;
  }
  return {variant, mode, stats, start, flags: [variant], cur: null, prev: null, cp: D.start, log: [], tested: {}};
}
function roll(f){ const m = /(\d*)d6\+(\d+)/.exec(f || ''); if (!m) return 0; let t = +m[2]; for (let i = 0; i < (+m[1] || 1); i++) t += d6(); return t; }

function condOk(c){
  if (!c) return true;
  return c.split('&').every(p => {
    if (['pass','fail','win','lose'].includes(p)) { const r = st.tested[st.cur]; return !r || r === p || (r==='pass'&&p==='win') || (r==='fail'&&p==='lose'); }
    let m = /^(has|not|hidden):(\w+)$/.exec(p);
    if (m) return m[1] === 'not' ? !st.flags.includes(m[2]) : st.flags.includes(m[2]);
    m = /^stat:(\w+)(>=|<=|==|>|<)(\d+)$/.exec(p);
    if (m){ const v = st.stats[m[1]] || 0, n = +m[3]; return {'>=':v>=n,'<=':v<=n,'==':v==n,'>':v>n,'<':v<n}[m[2]]; }
    m = /^limit:(\w+)$/.exec(p); if (m){ const L = lim(m[1]); return L !== null && (st.stats[m[1]] || 0) >= L; }
    return true;
  });
}
function clamp(name, v){
  const s = STAT[name] || {}; if (s.floor !== undefined) v = Math.max(s.floor, v);
  if (s.cap !== undefined) v = Math.min(s.cap, v);
  if (s.max_is_start) v = Math.min(st.start[name], v);
  return v;
}
function arrive(key, from){
  const s = S[key]; if (!s) return;
  hist.push(JSON.stringify(st));
  st.prev = from || st.cur; st.cur = key; delete st.tested[key];
  for (const f of s.g) if (!st.flags.includes(f)) st.flags.push(f);
  st.flags = st.flags.filter(f => !s.x.includes(f));
  for (const n in s.d) st.stats[n] = clamp(n, (st.stats[n] || 0) + s.d[n]);
  const ck = D.clock || {};
  if (ck.stat && (ck.exits || []).includes(st.prev) && (ck.hubs || []).includes(key)) st.stats[ck.stat] = clamp(ck.stat, (st.stats[ck.stat] || 0) + 1);
  if (D.checkpoints.includes(key)) st.cp = key;
  if (s.k === 'death' && (STAT.Vigour || {}).death === key) st.stats.Vigour = st.start.Vigour;
  st.log.unshift(s.n); st.log = st.log.slice(0, 60);
  store.set({st, hist: hist.slice(-80)});
  render(); window.scrollTo({top: 0});
}

function inline(t){
  return esc(t).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/\*(.+?)\*/g, '<i>$1</i>')
    .replace(/\{([A-Z0-9_]+t?)\}/g, (m, k) => {
      const s = S[k]; if (!s) return m;
      const ls = S[st.cur].l.filter(l => l[0] === k);
      const ok = !ls.length || ls.some(l => condOk(l[1]));
      return `<a class="go${ok ? '' : ' off'}" data-k="${k}">${s.n}</a>`;
    });
}
function variantFilter(paras){
  const v = D.variants; if (!v.marker) return paras;
  const re = new RegExp(v.marker, 'i');
  return paras.map(p => {
    if (!re.test(p)) return p;
    const parts = p.split(new RegExp(v.marker.replace(/\((?!\?)/g, '(?:'), 'i'));
    const tags = [...p.matchAll(new RegExp(v.marker, 'gi'))].map(x => x[1].toLowerCase());
    let keep = parts[0];
    tags.forEach((tg, i) => { const want = v.match[st.variant]; if (want && new RegExp(want, 'i').test(tg)) keep += parts[i + 1]; });
    return keep.trim();
  }).filter(Boolean);
}
function md(text){
  let paras = variantFilter(text.split(/\n\s*\n/));
  return paras.map(p => {
    p = p.trim(); if (!p) return '';
    let m = /^(#{1,3})\s+(.*)$/.exec(p); if (m) return `<h2>${inline(m[2])}</h2>`;
    m = /^([A-Z][A-Z .'\-]+?)\s{2,}NERVE (\d+)\s{2,}VIGOUR (\d+)$/.exec(p);
    if (m) return `<div class="foe">${esc(m[1])} · NERVE ${m[2]} · VIGOUR ${m[3]}</div>`;
    const lines = p.split('\n').map(inline).join('<br>');
    if (/^\*If [^*]+\*/.test(p)) return `<p class="cond">${lines}</p>`;
    return `<p>${lines}</p>`;
  }).join('');
}

function testBox(s){
  const t = s.te; if (!t) return '';
  if (t.type === 'combat'){
    return `<div class="box"><h3>Fight: ${esc(t.foe || 'foe')}</h3><div class="small">Each round: 2 dice + Nerve, both sides; higher score wounds the other for 2 Vigour.</div>
      <div id="fight" class="small" style="margin:8px 0"></div>
      <button class="primary" id="bFight">${st.mode === 'story' ? 'Fight it out' : 'Roll a round'}</button></div>`;
  }
  const r = st.tested[st.cur];
  return `<div class="box"><h3>Test your ${t.type}</h3>
    ${r ? `<div class="dice">${r === 'pass' ? (t.type === 'Fortune' ? 'Lucky' : 'Success') : (t.type === 'Fortune' ? 'Unlucky' : 'Failure')}</div>`
        : st.mode === 'story' ? `<button class="primary" data-res="pass">${t.type === 'Fortune' ? 'Lucky' : 'Succeed'}</button> <button data-res="fail">${t.type === 'Fortune' ? 'Unlucky' : 'Fail'}</button>`
        : `<button class="primary" id="bTest">Roll two dice</button> <span class="small">(score ${st.stats[t.type]})</span>`}</div>`;
}
function limitBanner(){
  const out = [];
  for (const s of D.stats){
    const L = lim(s.name), e = limitEnding(s.name);
    if (L !== null && e && (st.stats[s.name] || 0) >= L && S[st.cur].k !== 'ending' && st.cur !== e)
      out.push(`<div class="banner">${s.name} has reached its limit (${st.stats[s.name]}/${L}). The rules send you to <a class="go" data-k="${e}">${S[e].n}</a></div>`);
  }
  return out.join('');
}
function render(){
  $('brand').textContent = D.book.title;
  if (!st) return setup();
  if (view === 'rules') return rules();
  const s = S[st.cur];
  const cp = D.checkpoints.includes(st.cur) ? '<span class="cp">✈</span>' : '';
  $('view').innerHTML = `<div class="num">${s.n} ${cp}<small>${esc(s.z || '')}</small></div>${limitBanner()}<div class="text">${md(s.t)}</div>${testBox(s)}
     ${s.k === 'ending' ? `<div class="box"><h3>The end</h3><button class="primary" id="bAgain">Begin again</button></div>` : ''}`;
  bindView(); sheet();
}
function bindView(){
  document.querySelectorAll('a.go').forEach(a => a.onclick = () => arrive(a.dataset.k));
  document.querySelectorAll('[data-res]').forEach(b => b.onclick = () => { st.tested[st.cur] = b.dataset.res; afterTest(); });
  const bt = $('bTest'); if (bt) bt.onclick = () => {
    const t = S[st.cur].te, a = d6(), b = d6(), ok = a + b <= st.stats[t.type];
    if (STAT[t.type] && STAT[t.type].test_cost) st.stats[t.type] -= STAT[t.type].test_cost;
    st.tested[st.cur] = ok ? 'pass' : 'fail'; afterTest(`${a} + ${b} = ${a + b}`);
  };
  const bf = $('bFight'); if (bf) bf.onclick = fight;
  const ba = $('bAgain'); if (ba) ba.onclick = () => { st = null; hist = []; store.set(null); render(); };
}
function afterTest(note){ store.set({st, hist}); render(); if (note){ const d = document.querySelector('.dice'); if (d) d.insertAdjacentHTML('afterend', `<div class="small">${note}</div>`); } }
let foeV = null;
function fight(){
  const t = S[st.cur].te; if (foeV === null || foeV.k !== st.cur) foeV = {k: st.cur, v: t.vig};
  const box = $('fight');
  const round = () => {
    const me = d6() + d6() + st.stats.Nerve, it = d6() + d6() + t.nerve;
    if (me > it) foeV.v -= 2; else if (it > me) st.stats.Vigour = Math.max(0, st.stats.Vigour - 2);
    box.insertAdjacentHTML('beforeend', `<div>You ${me} · ${esc(t.foe || 'it')} ${it} → its Vigour ${Math.max(0, foeV.v)}, yours ${st.stats.Vigour}</div>`);
  };
  if (st.mode === 'story'){ st.tested[st.cur] = 'win'; foeV = null; store.set({st, hist}); render(); return; }
  round();
  if (foeV.v <= 0){ st.tested[st.cur] = 'win'; foeV = null; afterTest('You win.'); }
  else if (st.stats.Vigour <= 0){ st.tested[st.cur] = 'lose'; foeV = null; afterTest('Your Vigour is gone.'); }
  else sheet();
}
function sheet(){
  const el = $('sheet');
  const rows = D.stats.map(s => {
    const v = st.stats[s.name] || 0, L = lim(s.name);
    if (s.boxes){
      const n = s.cap || L || 5;
      return `<div class="stat" style="display:block"><div style="display:flex;justify-content:space-between"><span>${s.name}</span><span class="lbl">${v}/${n}</span></div>
        <div class="boxes" data-s="${s.name}">${Array.from({length: n}, (_, i) => `<span class="${i < v ? 'on' : ''}" data-i="${i}">${i + 1}</span>`).join('')}</div></div>`;
    }
    return `<div class="stat"><span>${s.name}${L !== null ? ` <span class="lbl">limit ${L}</span>` : ''}${s.max_is_start ? ` <span class="lbl">max ${st.start[s.name]}</span>` : ''}</span>
      <span class="pm"><button data-pm="${s.name}" data-d="-1">−</button> <span class="v">${v}</span> <button data-pm="${s.name}" data-d="1">+</button></span></div>`;
  }).join('');
  const items = st.flags.filter(f => (D.flags.items || []).includes(f));
  const words = st.flags.filter(f => shown(f) && !(D.flags.items || []).includes(f));
  el.innerHTML = `<h3>Adventure Sheet</h3><div class="small">${esc(st.variant)} · ${st.mode === 'story' ? 'Story Mode' : 'Survival Mode'}</div>${rows}
    <div class="lbl" style="margin-top:10px">ITEMS</div><div class="chips">${items.map(f => `<span class="chip">${esc(disp(f))}</span>`).join('') || '<span class="small">none</span>'}</div>
    <div class="lbl" style="margin-top:10px">CODEWORDS</div><div class="chips">${words.map(f => `<span class="chip">${esc(disp(f))}</span>`).join('') || '<span class="small">none</span>'}</div>
    <div class="lbl" style="margin-top:10px">LAST ✈ CHECKPOINT</div><div><a class="go" data-k="${st.cp}">${S[st.cp].n}</a></div>
    <div class="goto"><input id="gNum" inputmode="numeric" placeholder="Turn to…"><button id="gGo">Go</button></div>
    <div class="lbl" style="margin-top:10px">TRAIL</div><div class="log">${st.log.join(' · ')}</div>`;
  el.querySelectorAll('[data-pm]').forEach(b => b.onclick = () => { const n = b.dataset.pm; st.stats[n] = clamp(n, st.stats[n] + (+b.dataset.d)); store.set({st, hist}); render(); });
  el.querySelectorAll('.boxes span').forEach(b => b.onclick = () => { const n = b.parentNode.dataset.s, i = +b.dataset.i; st.stats[n] = st.stats[n] === i + 1 ? i : i + 1; store.set({st, hist}); render(); });
  el.querySelectorAll('a.go').forEach(a => a.onclick = () => arrive(a.dataset.k));
  const go = () => { const k = NUM[+$('gNum').value]; if (k) arrive(k); else $('gNum').value = ''; };
  $('gGo').onclick = go; $('gNum').onkeydown = e => { if (e.key === 'Enter') go(); };
}
function setup(){
  const v = D.variants;
  $('view').innerHTML = `<div class="text">${md(D.front.FRONT_INTRO || '')}</div>
   <div class="box setup"><h3>${esc(v.label || 'Who are you?')}</h3>${(v.flags || ['READER']).map((f, i) => `<label><input type="radio" name="var" value="${f}" ${i ? '' : 'checked'}> ${f}</label>`).join('')}
   <h3 style="margin-top:12px">How do you want to travel?</h3>
   <label><input type="radio" name="mode" value="story" checked> Story Mode (you choose test results)</label>
   <label><input type="radio" name="mode" value="survival"> Survival Mode (the dice decide)</label>
   <div style="margin-top:12px"><button class="primary" id="bStart">Turn to section 1</button> <button id="bR2">Read the rules</button></div></div>`;
  $('sheet').innerHTML = '<h3>Adventure Sheet</h3><div class="small">Your scores appear here when you begin. Everything the book tells you to note is filled in for you; you can always adjust by hand.</div>';
  $('bStart').onclick = () => { st = newState(document.querySelector('[name=var]:checked').value, document.querySelector('[name=mode]:checked').value); hist = []; arrive(D.start); };
  $('bR2').onclick = () => { view = 'rules'; rules(); };
}
function rules(){
  $('view').innerHTML = `<div class="text">${md(D.front.FRONT_RULES || '')}</div><button class="primary" id="bBackPlay">Back to the book</button>`;
  document.querySelectorAll('#view a.go').forEach(a => a.onclick = () => { view = 'play'; if (st) arrive(a.dataset.k); else render(); });
  $('bBackPlay').onclick = () => { view = 'play'; render(); };
}
$('bBack').onclick = () => { if (hist.length){ st = JSON.parse(hist.pop()); store.set({st, hist}); view = 'play'; render(); } };
$('bRules').onclick = () => { view = view === 'rules' ? 'play' : 'rules'; view === 'rules' ? rules() : render(); };
$('bNew').onclick = () => { st = null; hist = []; store.set(null); view = 'play'; render(); };
$('bTheme').onclick = () => { const r = document.documentElement, dark = r.dataset.theme ? r.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; r.dataset.theme = dark ? 'light' : 'dark'; };
const saved = store.get(); if (saved && saved.st){ st = saved.st; hist = saved.hist || []; }
render();
</script>
'''
