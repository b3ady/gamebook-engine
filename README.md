# gamebook-engine

A reusable, theme-agnostic pipeline for Fighting Fantasy–style interactive novels: section graph as
code, an exhaustive state-space verifier, writer briefs, prose checks, style counters, coverage
playtests, and a Kindle-ready EPUB 3 + companion web Adventure Sheet + story map. Extracted from the
one-off pipeline that produced **THE LAYOVER** (`/home/claude/layover`, untouched), which is kept here as
a byte-for-byte regression fixture.

`METHOD.md` is the production playbook (stages, human gates, the quality rules). `engine/prompts/`
holds the agent briefs it uses.

## Layout

```
engine/
  __main__.py      CLI: python3 -m engine <book_dir> <command>
  config.py        book.json loader (JSON + full-line // comments), {{placeholder}} filling, file helpers
  graph.py         section model, StoryBuilder (N, L, drop, retarget, K), Book loader (story + overlays,
                   condition aliases, limit hooks)
  conditions.py    generic condition language: has: not: hidden: pass fail win lose stat:X>=n limit:X
  verify.py        structure + state-space proof + shuffled numbering        -> build/map.json
  briefs.py        per-zone writer briefs                                    -> briefs/<zone>.md
  check_prose.py   prose vs structure (tokens, lengths, effects, codewords, clichés)
  tics.py          tic counts + quotas, conditional-paragraph stats
  build_book.py    merge map + prose                                         -> build/book.json
  storymap.py      story-map HTML (generic template, or the book's own)     -> build/story-map.html
  build_epub.py    EPUB 3 + EPUBCheck                                        -> dist/<slug>.epub
  sheet.py         companion web Adventure Sheet                             -> build/sheet.html
  coverage.py      legal routes that together visit every section            -> playtest/routes.json
  render_routes.py full-prose route files for playtester agents              -> playtest/routeNN.md
  playthrough.py   waypoint playthroughs for reviewers                       -> playthroughs/<name>.md
  reference.py     NUMBER_MAP.md, STATE.md for reviewers/auditors            -> build/
  scores.py        review score table + stop rule
  cover.py         render cover HTML to 1600x2560 JPEG (playwright + Pillow)
  epubtext.py      per-section text extraction / EPUB diff
  templates/       generic storymap.html, sheet.html
  prompts/         agent briefs for every stage (see prompts/README.md)
books/
  _template/       skeleton for a new book (commented book.json, StoryBuilder story.py, prose, front matter)
  the-layover/     fixture: copies of the Layover's story.py, entity.py, prose, assets, templates, reviews
tests/
  test_layover.py  acceptance test (reproduces the Layover)
  test_template.py smoke test of the generic path
```

## Commands

```
python3 -m engine books/<slug> verify       # ISSUES must be 0
python3 -m engine books/<slug> briefs
python3 -m engine books/<slug> check [zone ...]
python3 -m engine books/<slug> tics [zone ...]
python3 -m engine books/<slug> build        # book.json + story map
python3 -m engine books/<slug> epub [--no-check]
python3 -m engine books/<slug> sheet
python3 -m engine books/<slug> coverage
python3 -m engine books/<slug> routes
python3 -m engine books/<slug> playthrough [name ...]
python3 -m engine books/<slug> numbermap | stateref | scores | cover
python3 -m engine books/<slug> all          # verify, briefs, check, build, epub, sheet
```
Exit code is non-zero when verify has issues, check finds problems, or EPUBCheck reports errors.

## Start a new book (e.g. The Night Shift)

```
cp -r books/_template books/the-night-shift
python3 -m engine books/the-night-shift all          # the skeleton verifies and builds
```
Then follow METHOD.md from stage 1. Rename the countdown stat ("Doom" in the template) in book.json,
story.py's `StoryBuilder(stats=...)` and the front matter; set `sections.count`; list zones.

## The condition language

Atoms joined with `&`: `has:X`, `not:X`, `hidden:X` (puzzle link, never printed), `pass`/`fail`,
`win`/`lose`, `stat:Name<op>n` (`>= <= > < == !=`), `limit:Name` (the stat reached its configured
limit; links made only of limit atoms are global rules and never printed). Book-specific shorthands
map through `conditions.aliases`; the Layover's map is:

| old | generic |
|---|---|
| claim3 | stat:Claim>=3 |
| claim4 | stat:Claim>=4 |
| claimlow | stat:Claim<=2 |
| claimlimit | limit:Claim |
| fearlimit | limit:Fear |
| hours6 | stat:Hours>=6 |

The verifier treats stat atoms as unknown (both branches open, an over-approximation) unless the stat
is listed in `verify.track_stats` (needs a `cap`), in which case it is searched exactly, including clock
ticks on exit→hub moves.

## Tests

```
cd /home/claude/gamebook-engine
python3 -m unittest -v tests.test_layover tests.test_template      # ~25 s
```
`test_layover` asserts: verify ISSUES 0; key→number identical to `/home/claude/layover/layover_book.json`;
`check` OK on all five zones; the EPUB passes EPUBCheck with 0 fatals/errors/warnings; per-section text
of all 200 sections and every front/back page identical to `/home/claude/layover/dist/the-layover.epub`;
plus unit tests of the condition language and alias table. Set `LAYOVER_REF` to point elsewhere.

## Requirements

- **Python 3.10+, standard library only** for everything except the two items below. No PyYAML: config
  is `book.json` with `//` comment lines.
- **Java + EPUBCheck jar** for EPUB validation (optional; found via `epubcheck.jar` in book.json,
  `$EPUBCHECK_JAR`, or a filesystem search; skipped with a note if absent).
- **Playwright (Chromium) + Pillow** only for `cover` (rendering HTML covers), as in the Layover's
  make_cover.py. Not needed for anything else.
- No cv2 is used.

## What is still Layover-specific (by design, in the fixture, not the engine)

- `books/the-layover/templates/storymap.html` and `templates/sheet.html` are the Layover's own
  hand-designed pages (airport styling, Sam/Claim/Hours wording, LV 137). The engine ships generic
  versions driven by `book.json`; new books get those unless they supply their own.
- `book.json` of the fixture carries the Layover's display names, hidden/loose flag lists, tic regexes,
  zones (explicit key lists reproducing the original brief order), sheet rows, front/back matter, and
  the 7 reviewer playthrough waypoint lists.
- `story.py` / `entity.py` are verbatim copies, with their own (identical) N/_L/_drop/_retarget helpers.
