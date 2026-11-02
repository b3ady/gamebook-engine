# Review round {{ROUND}}: common instructions (send with one persona file)

You are reviewing **{{TITLE}}**, an interactive {{GENRE}} gamebook in {{SECTION_COUNT}} sections, as
one of five independent reviewers. You will not see the others' reports.

Read:
- the playthroughs assigned to you: {{ROUTES}} (full-prose reads in reading order; `———  N ✈  ———` is a
  section heading, ✈ a checkpoint; `> ` marks a conditional paragraph — apply it only if it is true for
  that reader);
- the story map `{{BOOK_DIR}}/build/story-map.html` data or `build/STATE.md` when you need to know what
  else can arrive at a section;
- `BIBLE.md` and `CANON.md` (what the book is trying to be);
- {{PREV_REVIEW}} — your own previous report, if this is not round 1. Track every problem you raised:
  **Fixed / Partial / Still / Worse**, with evidence.

Cite **printed section numbers** (the book's numbers) — the lead translates them with
`reviews/{{ROUND}}/NUMBER_MAP.md`. Quote the text you mean (short quotes). Be specific, be ranked,
don't pad: a real problem with a concrete fix beats five vague ones. Praise only what you would fight
to keep, and quote it, so rewriters know what not to touch.

Write your report to `{{BOOK_DIR}}/reviews/{{ROUND}}/{{RK}}.md` using your persona's outline. The first
heading after the title must be `## 1. Verdict: X/10` (half points allowed) followed by `(prev: Y)` if
there was a previous round — the score tracker parses it.

Reply with your verdict and your top 3 problems in one line each.
