# Brief: fine-tooth audit of {{ZONE}} ({{TITLE}})

The review rounds are over; the book is close to final. You are auditing every section in your scope
against **every way into it**. This is proofreading for a gamebook: the question for each sentence is
"is this true for every reader who can be here, holding what they can hold, having seen what they can
have seen?"

Scope: {{SCOPE}} (section keys and printed numbers; zone brief `briefs/{{ZONE}}.md`).

Read:
- `build/STATE.md` — where each codeword/item is gained and lost, and every section's incoming links with
  conditions. Use it to enumerate the paths into each section.
- `prose/*.json` for your sections **and** every section that links into them.
- `CANON.md`, `BIBLE.md` §7 (mechanics language), the rules pages (`prose/front.json`, FRONT_*).
- The EPUB renders `text` only: link labels in the structure are not printed, so findings about labels
  affect the story map only (mark them LOW).

For each problem write one bullet in `{{BOOK_DIR}}/audit/{{ZONE}}.md`, grouped under `## HIGH`, `## MED`,
`## LOW`:

    - [HIGH] §<num> <KEY>: "short quote" — the problem (which path/reader it breaks) — Fix: exact replacement text

HIGH = a reader is misled, stuck, or told something false about the game state; MED = continuity or
clarity that a careful reader notices; LOW = typos, echoes, style. Check also: conditions that are
always true or never true for the readers who can arrive; rules-page contradictions; checkpoint return
lines; numbers, times and counts that disagree across sections; typography (ellipses, dashes, quotes).

Don't report intentional design (listed by the lead): {{INTENTIONAL}}. Reply with counts per severity
and your three most serious findings.
