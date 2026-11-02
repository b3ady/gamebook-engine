# Agent prompt templates

Each file is a brief the lead session sends to a sub-agent (or uses itself) at one stage of
METHOD.md. Fill the `{{PLACEHOLDERS}}` before sending; never send a brief with one left in.
Paths are relative to the book directory (`books/<slug>/`) unless they start with `/`.

| Stage (METHOD.md) | File | Agents | Output |
|---|---|---|---|
| 1 Theme bible | `01_theme_bible.md` | 1 (or the lead) | `BIBLE.md`, `CANON.md` seed |
| 2 Structure | `02_structure.md` | lead | `story.py`, `entity.py`, `book.json` |
| 5 Zone drafting | `03_writer_zone.md` | 1 per zone, in parallel | `prose/<zone>.json` |
| 7 Review round | `04_review_common.md` + one of `04_R1..R5_*.md` | 5 in parallel | `reviews/vN/R<k>.md` |
| 7 Rewrite round | `05_revision_brief.md` (lead fills in) then `03_writer_zone.md` (rewrite mode) | 1 per zone | `REVISION<N>.md`, prose |
| 8 Fine-tooth audit | `06_audit.md` | 1 per zone (5–6) | `audit/<zone>.md` |
| 8/9 Fix pass | `07_fix_brief.md` | 2–3 (zones grouped) | prose edits, `audit/CHANGES_<name>.md` |
| 9 Coverage playtest | `08_playtest.md` | 1 per 2–3 routes | `playtest/report_<routes>.md` |
| 10 Cover | `09_cover.md` | 1 | `templates/cover.html` or a script |

Common placeholders:
`{{BOOK_DIR}}` absolute path of the book dir · `{{TITLE}}` · `{{ZONE}}` zone name from book.json ·
`{{ROUND}}` review round number (v1, v2 ...) · `{{PREV_ROUND}}` · `{{ROUTES}}` playthrough or route files ·
`{{GENRE_READER}}` who the target reader is (e.g. "a horror fan who reads on a phone at night").
