# Fix brief: {{PASS_NAME}} ({{TITLE}})

You are applying verified edits to {{TITLE}} in `{{BOOK_DIR}}`. The findings are in {{FINDINGS}}: one
bullet per finding, with a quote, the problem and a suggested fix. Section numbers are book numbers;
KEY is the source key.

## How to edit (strict)

- Section text lives in `prose/<file>.json` (key → text). Edit ONLY the files assigned to you:
  {{FILES}}.
- Use small Python scripts doing exact `str.replace` on one key, with `assert text.count(old) == 1`
  before each replace. **Never retype or regenerate a whole section.**
- Never change `{KEY}` tokens, never add or remove "turn to {X}" choices, and never change a
  conditional's *If …* condition unless this brief says so. Keep the book's spelling standard and voice.
  The suggested fixes are a guide: use them, or something equally minimal that reads better in context.
- Read the whole section and its neighbours before each edit, so the new wording is true for every
  reader who arrives there (`build/STATE.md` lists the ways in).
- Afterwards run `python3 -m engine {{BOOK_DIR}} check <zone>` for each zone you touched; it must
  print OK. If a length warning appears, trim.
- Write a changelog to `audit/CHANGES_{{NAME}}.md`, one line per finding:
  `§num KEY — applied/skipped — what changed`.

## Already handled by the lead (SKIP these findings)

{{HANDLED}}
<!-- Structural fixes go into story.py by the lead (new "# vN FIX" block, verify ISSUES 0, briefs) BEFORE
     this brief goes out; list them here so fixers don't duplicate them in prose. -->

## Rejected (SKIP)

{{REJECTED}}

## Specific decisions

{{DECISIONS}}

All other findings in your assigned reports: apply them, using judgement. If a finding is wrong once
you read the context, skip it and say why in the changelog.
