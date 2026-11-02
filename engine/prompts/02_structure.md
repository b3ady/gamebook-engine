# Brief: the section graph for {{TITLE}}

Read `{{BOOK_DIR}}/BIBLE.md` and `CANON.md`. Build the book's structure as code:
`{{BOOK_DIR}}/story.py` (N(...) calls through `engine.graph.StoryBuilder`; see `books/_template/story.py`),
an optional overlay `entity.py` (beats/lore/stat values for the entity layer, applied on top), and
`book.json` (copy `books/_template/book.json`; every field is commented).

## Shape that worked (The Layover, 200 sections)

- **Act 1 (≈20%)**: near-linear tutorial. Teaches every mechanic once, fairly: a test, a fight or
  chase, a codeword, an item, an anomaly ("is something wrong? turn back / keep going"), the first
  death (warned by a rule the reader has just read), the countdown track's first tick. The master
  clue section (the rules document) is reachable by everyone.
- **Hub + zones (≈50%)**: one hub section (short, escalating on each return, never re-read word for
  word) and 3 zones. Each zone yields one **key item** with **≥2 routes** to it (moral / nerve / combat /
  puzzle), contains one "one room behind you" monster beat, one analog document (lore), one death, one
  relationship beat. Zone exits tick the **clock** on return to the hub. Once a zone's item is held,
  gate the hub link so the zone can't be replayed (`not:ITEM`).
- **Finale (≈25%)**: the crossing (the low point on every route), the gate (every finale item required:
  `finale_gate`), a one-page reckoning of debts (settled inline, read once), the countdown reckoning,
  an anomaly corridor that teaches its own rule, the entity seen in full, then endings.
- **Endings (6–8)**: true, secret (hidden link + fixed number puzzle), sad, separate, taken/limit,
  loop (restart with a reduced track), and a "you became staff" ending. Each must be reachable
  (`verify` proves it) and the true ending must be reachable below the track's limit.
- **Deaths (≈10)**: each has `warn` (the rule the text gave), `clue` (sections that taught it; each must
  be able to precede the death), a `checkpoint` far enough back to cost something, and costs one tick
  of the track. Plus one shared stat death (`LAST` checkpoint).

## Mechanics

- **Stats**: Nerve/Vigour/Fortune (Fighting Fantasy) + Fear (limit = Nerve + 3) + a **countdown track**
  (Layover: Claim, 5 letters of your name on its sign; 4 closes the true ending, 5 = Final Call) + a
  **clock** (hours ticked at hub returns; 6 closes the gate). Bites must be real: give the track a
  mid-value consequence and a late reckoning that can lower it once.
- **Codewords**: relationship codewords (warmth earned mid-book, testable late — a late cost on the
  kind route), debts (settled at the reckoning), knowledge (puzzle answers), rescue (the companion can
  be taken and rescued ≥2 ways, and rescuing counts). Keep one-shot "already done" guards and flavour
  flags in `flags.loose` and `flags.hidden`.
- **Conditions**: `has:` `not:` `hidden:` `pass` `fail` `win` `lose` `stat:Track>=3` `limit:Track`. Order
  links so a stat bite comes first ("If your Claim is 4 or more, turn to …", then "Otherwise").
- **Fixed numbers**: section 1, the true ending (last number), puzzle answers (Layover: safe code
  1952 − 1800 = 152; flight number 137 → secret ending).

## Rules the verifier enforces (run `python3 -m engine {{BOOK_DIR}} verify` until ISSUES 0)

exact section count · no missing targets · no dead ends · terminals have no links · every death warned,
clued and checkpointed · every section reachable in the full state space · no softlocked state · finale
gate always entered with all items · every ending reachable · ≥N routes per finale item · clue sections
can precede their deaths · true ending reachable below the track limit · hidden targets never linked
plainly · shuffled numbering with no link between adjacent numbers.

Also try `verify.track_stats: ["Hours"]` and `["Claim"]` once (slower, exact) to prove the clock and
track bites never trap a reader.

## Deliverables

story.py, entity.py, book.json, a 1-page **structure summary** for the author (acts, hub, zones,
items and their routes, endings and what earns each, the countdown and clock bites, the death list),
and the verify report. **Stop for the author's approval** before briefs and drafting.
