# The gamebook production method

A stage-by-stage playbook for a Claude session producing a Fighting Fantasy–style interactive novel
with this engine. It is the method that took THE LAYOVER (200 sections, ~44,600 words) from premise to
an EPUBCheck-clean Kindle book, review scores 6.2 → 8.4/10 over eight rounds, then a fine-tooth audit
and a full-coverage playtest. Distilled from the Layover's BIBLE.md, CANON.md, REVISION*.md (rounds
2–8.1), audit/FIXBRIEF*.md and playtest5/BRIEF.md.

You are the **lead**. You own the structure (story.py), every brief, and every decision about what goes
to the human. Sub-agents draft, review, audit and playtest; they never change structure.

**Gates** (marked ⛔) are points where you stop and wait for the human. Never skip one: the human's
choices at these points are what make the book theirs.

Agent briefs live in `engine/prompts/` (index in its README). Commands are
`python3 -m engine books/<slug> <command>` run from the engine root.

---

## Stage 0. Set up

```
cp -r books/_template books/<slug>
```
Edit `book.json` → `book` (title, author, publisher, slug) and `sections.count`. Keep the skeleton's
story.py until stage 2 replaces it. Run `all` once to see the pipeline work end to end.

---

## Stage 1. Theme bible ⛔

Brief: `prompts/01_theme_bible.md`. Output: `BIBLE.md`, `CANON.md` seed, a design-questions list.

What the bible must pin down (the Layover's worked):
- **Two books at once**: a genuinely frightening genre story *and* a relationship story (estranged
  siblings, here). Every scene with the companion moves the second story a step.
- **Voice**: second person, present tense; short paragraphs for phones; concrete over abstract; each
  section anchored to wherever the reader came from and ending on a hook; humour mostly from the
  companion ("fear is sharper after a laugh"); banned clichés.
- **The entity**: what it is (unsaid until late), what it wants, 4–6 **rules that are also survival
  tips**, a tell, and **one rule broken once, late**. It is patient and polite; it never roars.
- **Mechanics language**, verbatim (tokens, tests, foe lines, effects, global rules never linked).
- Fixed facts in CANON.md (ages, dates, the single true account of the backstory, lines said only once
  and where: "Safe landings" only in the true ending).

⛔ **Gate 1 — the human approves the bible** and answers the design questions (who the companion is,
the entity's nature, the countdown's name and meaning, the tone of the true ending, reader variants).

---

## Stage 2. Structure graph + mechanics ⛔

Brief: `prompts/02_structure.md` (shape, mechanics, endings, deaths). Output: `story.py`,
`entity.py` (optional overlay), `book.json`.

Rules:
- Write the structure as N(...) calls. Every section has a **beat** (what happens, 1–3 sentences) and
  design **notes** (why it exists: "Route 2 of 2 to TRANSFER", "Clue for D06"). Writers and reviewers
  read both.
- Key item routes ≥ 2, rescue routes ≥ 2, every death warned + clued + checkpointed, a single
  rules document reachable by all (the master clue), fixed numbers for puzzles.
- Put the countdown and the clock in `book.json` → `stats` / `clock` with their limits, and their bites
  in links (`stat:Claim>=4`, `stat:Hours>=6`). Calibrate thresholds against what honest runs produce
  (stage 9's coverage tally): the Layover's HOURS was decorative for three rounds because every honest
  run landed on 4.

⛔ **Gate 2 — the human approves the structure summary** (acts, hub/zones, items and routes, endings
and what earns each, countdown/clock bites, death list).

---

## Stage 3. Verify (automated, repeat after every structural edit)

```
python3 -m engine books/<slug> verify        # must print ISSUES: 0
python3 -m engine books/<slug> numbermap     # build/NUMBER_MAP.md
python3 -m engine books/<slug> stateref      # build/STATE.md
```
The verifier proves: exact count, no dead ends, no missing targets, every section reachable in the
full (section × codeword) state space, no softlocked state, finale gate always entered with every
item, every ending reachable, death clues can precede deaths, the true ending reachable below the
track limit, hidden targets never linked plainly; then assigns shuffled numbers (no link joins adjacent
numbers). Occasionally run with `verify.track_stats` set to the clock and the track (exact, slower):
the Layover is clean with Hours tracked (4.8M states) and with Claim tracked (4.75M states).

**Numbering changes whenever structure changes.** Archive `NUMBER_MAP.md` into `reviews/vN/` at every
review round; reviewers cite printed numbers and you translate through the map of *their* round.

---

## Stage 4. Briefs

```
python3 -m engine books/<slug> briefs        # briefs/<zone>.md
```
One brief per zone (`book.json` → `zones`): for each section, arrives-from (with titles), beat, link
tokens with conditions and target titles, effects in in-world names (hidden flags marked "never
mention"), foe/test lines, the death line, lore, design note. Regenerate after every structural edit.

---

## Stage 5. Zone drafting by parallel writer agents

Brief: `prompts/03_writer_zone.md`, one agent per zone, all in parallel (Layover: 5 zones of 33–52
sections, plus front matter). Each writes `prose/<zone>.json` and runs `check` + `tics` on its zone.
Front matter (`FRONT_*` keys: premise/variant choice, how to play, rules for every mechanic) goes with
the first zone's writer.

---

## Stage 6. Automated checks (gate before any human or reviewer reads)

```
python3 -m engine books/<slug> check         # every zone prints OK
python3 -m engine books/<slug> tics          # counts, quotas (!! = over)
python3 -m engine books/<slug> build         # build/book.json + story map
python3 -m engine books/<slug> playthrough   # reviewer reads
```
`check`: tokens == printed links (+ death checkpoint), no hidden link printed, minimum lengths, every
visible gain named in-world, every stat change stated, no raw underscore codewords, no banned clichés.
Fix until clean. Then define the reviewer **playthroughs** (`book.json` → `playthroughs`): one per
reader persona — kind/true ending, cold/alone, secret ending, companion lost and rescued, debts/staff
ending, reckless/deaths/loop, separate. Every ending and every major codeword route should be read by
some reviewer.

---

## Stage 7. Five-persona review rounds (score tracking + stop rule) ⛔ when escalated

Briefs: `prompts/04_review_common.md` + one of `04_R1_developmental`, `04_R2_game_flow`,
`04_R3_prose`, `04_R4_genre_fan`, `04_R5_character`. Five agents in parallel, each with 2 playthroughs
(R1: kind + separate; others mixed so all 7 are read). Output: `reviews/vN/R1..R5.md`.

Then, as lead:
1. `python3 -m engine books/<slug> scores` — the table and the **stop rule**: stop review rounds when
   the mean ≥ 8.5 with nobody below 7.5, or when the mean gains < 0.1 in a round (plateau), or after
   10 rounds. The Layover: 6.2, 7.2, 7.5, 7.7, 7.9, 8.2, 8.4, 8.3 → plateau → audit.
2. Keep `reviews/OPEN.md`: one line per open problem, `rounds: N` = consecutive rounds raised.
   **Anything raised in 3+ rounds is a design question, not a rewrite task** (the Layover's G11
   "MARKED test is always true" was requested five times; HOURS was "decorative" three times; both
   needed a structural decision, not better prose). ⛔ **Gate 3 — put those to the human** with 2–3
   concrete options each, and their trade-offs. Record answers in the next revision brief §B.
3. Make **structural changes first**, in story.py, as a new layered block:
   `# vN STRUCTURAL EDITS (round-N reviews)` with `_K = K()`, `L(...)`, `drop`, `retarget`, new `N(...)`.
   Never edit earlier blocks; the history is the design record. Then `verify` (ISSUES 0), `briefs`,
   `numbermap`.
4. Write `REVISION<N>.md` from `prompts/05_revision_brief.md`: structure changes and what the text must
   now say; the human's decisions; a table of falsehoods to fix; prose rules **as quotas** (add regexes
   to `book.json` → `tics` and limits to `tic_quotas`); a keep list.
5. Send rewrite agents (`03_writer_zone.md`, rewrite mode) per zone. Re-run stage 6. Next round.

### The rules the Layover's eight rounds converged on (put them in every brief)

**The neutral-body rule (most important).** Main text is true for every reader who can arrive. It never
asserts the companion is there, nor that they are missing. Per-reader differences live only in
conditional paragraphs: `*If Sam is with you,* …` — at most one companion block per section (≤70 words)
and one relationship block (≤50 words, fold it into the companion block: `*If you also have TRUCE,* …`).
Never write the companion present and then retract it. Absence is felt through the missing block; lines
about absence are rare and one sentence. Sections unreachable without the companion need no block.

**Conditional format.** Condition in italics then a comma, one paragraph per block, never a condition
mid-paragraph, never a block that spills into a second paragraph; a multi-paragraph variant starts each
paragraph with its own *If …*.

**Re-reads.** Hubs and checkpoint returns are read many times: the return line comes first (≤20–30
words, "Go straight to the choices"), the first-visit text second. One hub, not a chain of hub sections.
One-shot set pieces fire once (codeword) and then gate themselves off. Completed zones can't be
re-entered (`not:ITEM` on the hub link).

**Earned warmth.** Relationship rewards are mostly words, jokes and shared knowledge, not touches or
chores (Layover quota: ≤3 touches, ≤3 chores book-wide). The kind route needs a late cost (a test of the
truce in the last act), or its arc resolves at 45% and idles.

**One telling.** Each revelation (the confession, the backstory, the accusation) is told fully once;
other routes get a pointer. A reader must never meet the same reveal twice on one route.

**Stop explaining.** The monster is not explained before its reveal section. Rules are discovered, not
listed ("No rules language" for the dying man; the corridor teaches its own rule). The narrator never
explains a stat change ("Lose 1 Fear." not "The place has rules, and you are learning them").

**Prose budget.** One simile per section; no captioned subtext; ≤1 "Not X. Y." per section; no "ever"
superlatives in narration; no "very"; paragraphs ≤60 words; dialogue is speech, not essays. Cut tics
breed substitutes ("hands" → "fingers/palm/thumb"; "warm" → "flat"): name likely substitutes in the brief
and count them too. Signature images belong to one character each (the frightened eyes: the Hostess
first, Dad's at the end, nobody else).

**Every death** ends "Add 1 to your <track>. Return to {X} and choose again." and sends the reader far
enough back to cost something. Deaths that are the obvious wrong answer to a rule printed one page
earlier are a "compliance quiz": give the choice a real temptation or a cost both ways.

**Endings** stop over-ending: after the emotional peak, three beats at most. The last line has a speaker.

---

## Stage 8. Fine-tooth audit

When the stop rule says AUDIT. Brief: `prompts/06_audit.md`, one agent per zone (Layover: 6 incl.
front matter), reading every section against every way in (`build/STATE.md`). Output:
`audit/<zone>.md` with HIGH / MED / LOW findings and exact replacement text.

As lead: sort findings into (a) **structural** — fix in story.py yourself (`# vN FINE-TOOTH AUDIT FIXES`
block: gate a hub link, add a missing exit, gate a one-shot option), `verify`, `briefs`; (b) **rejected**
(intentional design — say why); (c) **specific decisions** where you choose the wording; (d) the rest.
Then `prompts/07_fix_brief.md` to 2–3 fix agents (zones grouped), with the strict edit rules: exact
single-occurrence `str.replace` with an assert per change, never regenerate a section, never touch
tokens or conditions unless told, changelog per finding. Re-run `check`.

---

## Stage 9. Coverage playtest

```
python3 -m engine books/<slug> build
python3 -m engine books/<slug> coverage      # playtest/routes.json: legal routes covering every section
python3 -m engine books/<slug> routes        # playtest/routeNN.md with sheet lines
```
Brief: `prompts/08_playtest.md`, one agent per 2–3 routes (Layover: 13 routes, ~5 agents). They play as
readers, tracking the sheet, and report [continuity] / [rules] / [clarity] / [prose] bullets. Then a
second fix pass (stage 8's lead triage + `07_fix_brief.md`; Layover: FIXBRIEF2). If the structure
changed, re-run coverage on the new graph and spot-check the routes through the changed sections.

---

## Stage 10. Build ⛔

```
python3 -m engine books/<slug> all           # verify, briefs, check, build, epub (+EPUBCheck), sheet
python3 -m engine books/<slug> cover         # if the cover is HTML (prompts/09_cover.md)
```
- **EPUB**: must pass EPUBCheck with 0 errors / 0 warnings. Front matter from `book.json` → `epub.front`
  (premise, how to play, Adventure Sheet page with paper rows + QR to the web sheet), sections in files of
  20 with a ✈ icon on checkpoints, conditional paragraphs indented, foe stat boxes, "THE END" on endings,
  back matter (review ask, a hint at the secret ending).
- **Web Adventure Sheet** (`build/sheet.html`): host it (e.g. GitHub Pages) at the URL printed in the
  EPUB; type a section number and it applies effects, checkpoints, clock ticks, limits; dice and fights.
  Test it on a phone with a real route.
- **Story map** (`build/story-map.html`): for the author: every section, its links, conditions, effects,
  text; endings with minimum stats; the verifier report.
- **Cover**: 1600×2560, legible at thumbnail size. Show 2–3 directions first.

⛔ **Gate 4 — the human approves the final package**: EPUB on a Kindle/phone, cover, sheet URL, author
name, price/blurb. Publishing (KDP upload) is the human's action.

---

## Quick reference: who changes what

| Artifact | Changed by | When |
|---|---|---|
| BIBLE.md | lead (human approves) | stage 1; amended only by revision briefs |
| CANON.md | writers append; lead resolves conflicts | every drafting/rewrite pass |
| story.py / entity.py | **lead only**, append-only blocks per round | stage 2, after each review/audit/playtest |
| book.json | lead | any stage (quotas, zones, playthroughs) |
| briefs/*.md | generated | after every structural edit |
| prose/*.json | writer / fix agents | stages 5, 7, 8, 9 |
| reviews/vN/, audit/, playtest/ | agents | stages 7–9 |
| build/, dist/ | generated | any time |
