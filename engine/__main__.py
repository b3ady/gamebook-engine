"""CLI: python3 -m engine <book_dir> <command> [options]

Commands
  verify     structure + state-space proof + numbering      -> build/map.json
  briefs     per-zone writer briefs                         -> briefs/<zone>.md
  check      prose vs briefs (tokens, length, effects)      (exit 1 on problems)
  tics       style-tic and conditional-block counts per zone
  build      merge map + prose                              -> build/book.json, story map HTML
  storymap   story map HTML only                            -> build/<storymap.out>
  epub       EPUB 3 (then EPUBCheck if a jar is found)      -> <epub.out>
  sheet      companion web Adventure Sheet                  -> build/<web_sheet.out>
  webplay    playable web edition (book + live sheet)        -> build/play.html
  coverage   legal routes that together visit every section -> playtest/routes.json
  routes     render coverage routes for playtester agents   -> playtest/routeNN.md
  numbermap  printed number -> key map for reviewers        -> build/NUMBER_MAP.md
  stateref   flag gain/lose + incoming-link reference       -> build/STATE.md
  cover      render the cover HTML (needs playwright+Pillow) -> cover.out
  scores     review score table + stop rule                  (reviews/v*/R*.md)
  playthrough  waypoint playthroughs for reviewers           -> playthroughs/<name>.md
  all        verify, briefs, check, build, epub, sheet
"""
import os, sys

from .config import load_config

COMMANDS = ['verify', 'briefs', 'check', 'tics', 'build', 'storymap', 'epub', 'sheet', 'webplay', 'coverage', 'routes',
            'numbermap', 'stateref', 'cover', 'scores', 'playthrough', 'all']


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) < 2 or argv[1] not in COMMANDS:
        print(__doc__)
        return 2
    book_dir, cmd, rest = argv[0], argv[1], argv[2:]
    cfg = load_config(book_dir)
    rc = 0
    if cmd in ('verify', 'all'):
        from . import verify
        out = verify.run(cfg, quiet=(cmd == 'all'))
        n = len(out['report']['issues'])
        if cmd == 'all':
            print(f'verify: ISSUES {n}')
        rc |= 1 if n else 0
    if cmd in ('briefs', 'all'):
        from . import briefs
        briefs.run(cfg)
    if cmd in ('check', 'all'):
        from . import check_prose
        rc |= check_prose.run(cfg, zones=rest or None)
    if cmd == 'tics':
        from . import tics
        tics.run(cfg, zones=rest or None)
    if cmd in ('build', 'all'):
        from . import build_book, storymap
        build_book.run(cfg)
        storymap.run(cfg)
    if cmd == 'storymap':
        from . import storymap
        storymap.run(cfg)
    if cmd in ('epub', 'all'):
        from . import build_epub
        rc |= build_epub.run(cfg, validate='--no-check' not in rest)
    if cmd in ('sheet', 'all'):
        from . import sheet
        sheet.run(cfg)
    if cmd in ('webplay', 'all'):
        from . import webplay
        webplay.run(cfg)
    if cmd == 'coverage':
        from . import coverage
        coverage.run(cfg)
    if cmd == 'routes':
        from . import render_routes
        render_routes.run(cfg)
    if cmd == 'numbermap':
        from . import reference
        reference.number_map(cfg)
    if cmd == 'stateref':
        from . import reference
        reference.state_ref(cfg)
    if cmd == 'scores':
        from . import scores
        scores.run(cfg)
    if cmd == 'playthrough':
        from . import playthrough
        playthrough.run(cfg, names=rest or None)
    if cmd == 'cover':
        from . import cover
        cover.run(cfg)
    return rc


if __name__ == '__main__':
    sys.exit(main())
