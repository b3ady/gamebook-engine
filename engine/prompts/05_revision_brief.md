# {{TITLE}}: Round {{N}} brief

<!-- The lead writes this after reading all five reviews of the previous round. Turn notes into RULES
     writers can apply and checks can count. Keep it under ~5 pages. Delete these comments. -->

Round {{N_PREV}} averaged **{{MEAN}}** ({{SCORES}}). The reviews are in `reviews/v{{N_PREV}}/R1–R5.md`
and cite v{{N_PREV}} printed numbers; translate them with `reviews/v{{N_PREV}}/NUMBER_MAP.md`. All earlier
briefs still apply, as do CANON.md and the neutral-body rule. Where they conflict, this brief wins.

## A. Structure (already made and verified; briefs are regenerated)

<!-- Every structural change goes into story.py as a new "# vN STRUCTURAL EDITS" block FIRST, then
     `verify` (ISSUES 0), `briefs`, `numbermap`. Here, list each change and what the prose must do. -->
1. **{{CHANGE}}.** What changed in the graph. What each affected section's text must now say.

## B. Design decisions made by the author

<!-- Questions escalated by the stop rule (raised 3+ rounds) and the author's answers. -->

## C. Bugs: text false for some readers

| Section | Fix |
|---|---|
| KEY | what is false, for whom (path), and the fix |

## D. Prose rules this round

<!-- Convert R3's counts into quotas (per zone or book-wide) and add them to book.json tic_quotas
     with regexes in "tics", so `tics` can enforce them. Name the substitutes in advance. -->

| Tic | Limit |
|---|---|

## E. Keep

Every line the reviewers quoted under "What works". Do not reintroduce cut tics.

## F. Checks

- `python3 -m engine {{BOOK_DIR}} check <zone>` prints OK
- `python3 -m engine {{BOOK_DIR}} tics <zone>` is within quotas
- Report what you changed, plus the counts this brief asks for (before → after).
