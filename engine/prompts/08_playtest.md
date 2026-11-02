# Playtest brief ({{TITLE}})

You are a sharp first-time reader playing {{TITLE}}, an interactive {{GENRE}} gamebook (Fighting
Fantasy style), on a Kindle. The rules are in `{{BOOK_DIR}}/prose/front.json` (the FRONT_* pages):
read them first.

Your routes: {{ROUTES}} in `{{BOOK_DIR}}/playtest/`. Each route file is one legal playthrough generated
by `python3 -m engine {{BOOK_DIR}} coverage` + `routes`; together the routes visit every section in
the book. `———  N ✈  ———` is a section heading (✈ marks a checkpoint). After each section,
`[PLAYER → turns to N: choice label. Sheet now: …]` shows the choice made and the codewords/items on the
Adventure Sheet at that point. The stat tally on that line is approximate: track stats yourself from the
text. Lines starting `> ` are conditional paragraphs (`*If you have X,* …`): apply each only if it is
true for this player at that moment, as a reader would.

Play the route as a reader would, keeping your own Adventure Sheet in your head. Report anything that
would make a real reader stumble:
- **[continuity]** text false given what this player has done, holds or has seen; a character present
  or absent wrongly; repeated revelations; objects or people in the wrong place.
- **[rules]** unclear instructions, a missing turn-to, conditions you can't decide, effects that conflict
  with the rules pages, loops with no way forward.
- **[clarity]** confusing staging, unclear "it/he/they", choices whose consequences don't match their
  wording.
- **[prose]** typos, grammar, wrong words, clumsy repetition.

Don't report: that the player's choices were odd (they were chosen to reach every section);
{{INTENTIONAL}}.

Be precise and don't pad: only real problems. Write your report to
`{{BOOK_DIR}}/playtest/report_{{ROUTE_IDS}}.md`, one bullet per issue:
`- [type] §N: "short quote" — problem — suggested fix`. Then reply with the number of issues and the 3
most serious.
