# Brief: write the {{ZONE}} sections of {{TITLE}}

You are one of {{N_WRITERS}} writers drafting **{{TITLE}}** in parallel, one zone each. Yours is
**{{ZONE}}**: the sections listed in `{{BOOK_DIR}}/briefs/{{ZONE}}.md`.

Read first, in this order: `BIBLE.md` (the law), `CANON.md` (facts you must not contradict),
`briefs/{{ZONE}}.md` (your sections), then skim the neighbouring zones' briefs for every section
listed in your "Arrives from" lines. {{REVISION_BRIEFS}}

## Each section

- **Main text must be true for every reader who can arrive.** Check the "Arrives from" list and the
  link conditions into the section. Never assert something only some readers did, hold or saw.
  Per-reader differences go in conditional paragraphs only.
- **Conditional paragraphs**: start with the condition in italics and a comma — `*If Sam is with you,* he…`
  — one paragraph each, never a condition mid-paragraph, never a block that runs on into a second
  paragraph. At most one companion block per section (≤70 words) and one relationship block (≤50 words);
  fold the relationship clause into the companion block where you can (`*If you also have TRUCE,* …`).
  If a section can't be reached without the companion, write them into the main text with no block.
- **Absence**: the reader without the companion feels it because the block is missing and the main
  text is about one person. Lines about the absence itself are rare (≤2 per zone) and one sentence.
- **Re-reads**: hubs and checkpoint sections are read many times. Give them a short return line first
  (`*If you have been here before,* … Go straight to the choices.`, ≤20–30 words).
- **Links**: write every link in the brief exactly once as `{KEY}`; invent none; never write a number;
  hidden links are puzzles with no token, exactly as the brief describes.
- **Effects** are stated where they happen, with in-world names: "Gain 1 Fear." "Note the codeword TRUCE."
  The narrator never explains a stat change.
- **Deaths** end with the brief's exact death line. **Endings** earn their length.
- Opening line anchored to where the reader just was; closing line a hook before the choices.

## Style budget (from the bible and every revision brief so far)

One simile per section. No captioned subtext (delete the line that explains a gesture). At most one
"Not X. Y." per section. No "ever" superlatives in narration. No "very". Paragraphs ≤60 words. No
clichés from the bible's list. Respect the tic quotas in `book.json` (`tic_quotas`) and do not invent
substitute tics (a new repeated gesture in place of a cut one counts against you).

## Output and checks

Write `{{BOOK_DIR}}/prose/{{ZONE}}.json`: `{"KEY": "text", ...}` for every section in your brief.
Then run, and fix until clean:

    python3 -m engine {{BOOK_DIR}} check {{ZONE}}
    python3 -m engine {{BOOK_DIR}} tics {{ZONE}}

Reply with: sections written, total words, the check result, your tic table, and any cross-zone
problem you noticed (a fact a neighbouring zone must match; a brief that contradicts the bible). Add new
facts you established to the end of CANON.md under a `## {{ZONE}}` heading.

## Rewrite mode (review rounds)

When this brief is sent with a revision brief (`REVISION<N>.md`): change only what the revision brief
and your zone's review notes require; keep every line reviewers quoted as working; keep every token;
report before → after counts for whatever the revision brief asks you to count.
