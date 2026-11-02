# THE NIGHT SHIFT: structure summary (stage 2, v2 after Gate 2)

**v2 (the author's Gate 2 answers):** (1) ROUNDS starts with no box ticked: one spare hour; (2) 147 is a **coda after
200**, never instead of it; (3) the Bay 2 rescue can also give MENDED, at the cost of a field (R41); (4) Act 1 deaths
cost no wristband field; (5) Mum is Maureen "Mo" Doyle, née Brennan; tonight is a Thursday in November. The red floor
line (H19) was cut to stay at 200. The edits are a layered `v2` block at the end of story.py.

200 sections, 7 endings (6 terminal + the true ending, which links on to the coda), 10 rule deaths + 1 shared Vigour
death. `verify`: **ISSUES 0**. Untracked: 183,647 states, 0 softlocks. **ROUNDS tracked exactly:** 994,311 states,
ISSUES 0. **WRISTBAND tracked exactly:** 1,052,767 states, ISSUES 0. Tracking both together runs out of memory; each was proven separately, as the Layover's were.
The story map is `build/story-map.html` (structure only, no prose yet). Flag ledger and every way into each section:
`build/STATE.md`. Printed numbers: `build/NUMBER_MAP.md` (seed 10). Writer briefs: `briefs/<zone>.md`.

## Acts and zones

| Act | Zone (brief) | Sections | Contents |
|---|---|---|---|
| 1 | Level 3 (`act1`) | 38 | Family room 01:40 → Ros → the surgeon's question → property bag → first round (tea, the 1st field) → night setting → anomaly tutorial → **the Notice (A23, master clue)** → "Maureen?" (D01) → the porter (D02) → the funeral line → lift to Level 1 |
| 2 | Main Corridor (`corridor`) | 21 | Hub H01; first return H02 (+ Ros's scene H03/H04); second return H05 (the Sister's offer); tea bar, Lost Property (Larkvale tag), payphone; the Maternity lift / stairs (HL/HLD/HS) |
| 2 | Old Wing (`oldwing`) | 33 | Nightingale ward of the Kept, Gary 1986, the round in unison, the chapel, the Sister's office, Ros's side room. **VISITOR'S BADGE** |
| 2 | Basement (`basement`) | 30 | Medical Records (the file, the LPA, the letter), Property (the ring, locker 179), the mortuary corridor and the 1991 incubator, linen, porters' lodge, the lift that only goes down. **MUM'S LETTER** |
| 2 | Maternity & Ward 9 (`maternity`) | 28 | 1991 register, the nurses'-station phone (Mum from tomorrow), delivery suite, Ward 9 and Mum's chair, parents' room, the WARD 0 stairwell door. **THE LAST RULE** |
| 3 | Ward 0 + endings (`act3`) | 50 | The crossing, the door, Handover 1979, the reckoning, claim-back, Bay 2 rescue (late MENDED, R41), **the obs-chart walk** (anomaly loop), Bay 6, the Sister in full, the consent form, the climax, 06:00, endings + coda + D_VIGOUR |

Kinds: 93 story, 54 choice, 16 item, 8 test, 4 combat, 7 anomaly, 11 death, 6 ending, 1 finale (200).

## Critical path (the true ending)

Act 1 on any route (pass A23, the Notice); earn **SPOKE** (A10 / A35 / H04 / W19) and **HELD** (A28 / W04 / M26 / any
rescue) along the way. Main Corridor (no tick on first arrival). **Old Wing** → badge (Gary, the chapel clip, or the
office drawer) → back (01:00 ticked; Ros's scene). **Basement** → the letter (Records, or locker 179) → the lift up still
works (02:00 ticked; the Sister's offer: refuse, keep Ros). **Maternity** (lift or stairs: only 2 ticks so far) → Ward 9
→ give Ros Mum's chair → **MENDED** → the strip under the mattress (03:00 ticked).
**Ward 0**: the crossing → break rule 5 → Handover 1979 → reckoning with 3 ticks = Mum's lucid moment (−1 field) → Ros reads
the letter aloud (−1 field) → the charts (Bay 3 walk on, Bay 4 turn back: let Ros be the one, Bay 5 turn back) → Bay 6
with ≤3 fields → refuse the form → **Ros reads Mum's name, you hold her hand, you let her go** → 06:00 → **06:02,
Visiting Hours (200)** → and, if you know the minute you were born, the coda **147**.

## Mechanics

**WRISTBAND** (stat `Wristband`, field `band`, 0–5). Five fields: NAME, DATE OF BIRTH, NEXT OF KIN, WARD, BED.
- **Fills (+1):** accepting comfort or giving details: tea in the family room (A14), the Sister's blanket (H10), the
  tea bar (H11), "next of kin: me" on the payphone (H17), standing by a bed on the round (W12), failing to steal the
  chapel badge (W17), signing the Records slip (B03), signing for the ring (B14), answering the mortuary drawer (B20),
  caught on the Maternity round (M13), **the 05:00 round at the reckoning (R09)**, the late mending in Bay 2 (R41), and **every death from the Main Corridor onwards** (+1; Act 1 deaths D01/D02 cost nothing: v2).
- **Empties (−1), only when claimed back:** Ros's scissors (W27, needs SPOKE; R12, needs HELD), Mum on the phone from
  tomorrow (M09), Mum's lucid moment (R08, ROUNDS ≤ 4), Ros reading Mum's letter aloud (R11). At the reckoning you get
  R11 or R12, not both.
- **Bites:** 3+ at the crossing = the porters know a patient (R03, a fight). **4+ at Bay 6 = the true ending is closed**
  (R31: Kept / Night Staff / Admitted). **5 = Admitted** (global rule, verifier hook after every +1 section).

**ROUNDS** (clock, six boxes 01:00–06:00, **none ticked at the start**: v2). Tick on every move from a zone exit
(W29, W30, B29, B30, M28, M29, HLD) to the Main Corridor (H01/H02/H05). The first arrival from Act 1 doesn't tick.
- **3rd tick (03:00): the lifts go down only.** Taking the Basement lift up = D05; taking the lift to Maternity drops
  you to the Basement and costs another tick (HLD). Stairs always work. Since a perfect run only ticks 03:00 on its
  final return, this rule now bites **only readers who have already spent their spare hour** (one retreat or one hub
  trip to fetch Ros before their last zone). Both D05 and HLD remain reachable (proven with ROUNDS tracked). This is
  a sensible bite: it is the cost of the spare hour, and it compounds (HLD itself ticks).
- At the reckoning (R07): **≤ 4 ticks → Mum's lucid moment** (−1 field, −2 Fear); **5 ticks → one more field**.
- **6th tick → Admitted** (global rule on the three clock hubs).
- Perfect run: 3 ticks (Ward 0 at 03:00). One extra trip: 4, still lucid. Two: 5, +1 field. Three: Admitted.

**Relationship codewords:** SPOKE (4 routes) → HELD (7 routes, incl. every rescue) → **MENDED** (4 routes, each needs
SPOKE: chapel W21 also needs HELD; Records B09; Ward 9 M22; and, late and costly, **R41**: rescuing Ros in Bay 2 and
saying the rest, for one wristband field: v2). **Late cost:** at Bay 4 (R25) Ros wants to do
Mum's obs herself ("I'm the one she named"). Let her = +2 Fear; take the chart = lose MENDED.

**WARDED** (Ros taken): 3 ways (accept the Sister's bed for her H07; let her lie down on the Old Wing W03; let her nap
in the parents' room M27). **3 rescue places** (4 sections), each giving HELD: say her name in the Old Wing side room (W28 → W31; from the
hub once the zone is shut, at the cost of a tick), tear up her new file in Records (B21/B22), say her name in Ward 0
Bay 2 (R14/R15), or say her name *and the rest* (R41: also MENDED, +1 field, needs SPOKE). Not rescued at the end = Only Child.

**Items and routes**

| Item | Routes | Notes |
|---|---|---|
| VISITOR'S BADGE (gate) | W07 Gary's badge (moral: promise him; PROMISE pays off at R06a) · W16 unclip it from the chapel book (Nerve) · W23 office drawer (Fortune, or beat the night porter W26) | the office is repeatable, so the zone can't softlock |
| MUM'S LETTER (gate) | B07 Mum's file in Records (sign the slip: +1 field / search: Fortune, else the porter fight / Ros finds it) · LOCKER 179 (hidden number) | B07 is the one telling of the LPA and the letter |
| THE LAST RULE (gate) | M12 the drug cupboard after Mum's call (Fortune) · M17 the theatre staff in the delivery suite (fight or Nerve) · M20 under the mattress from Mum's chair (moral) | |
| NOTICE (master clue) | A23, on every route | reprinted on the sheet |
| GLASSES, TICKET | A11 (open the property bag) | GLASSES: −1 Fear before the charts (R17). TICKET: checked at the tea bar (H16), held up at the crossing (R40) |
| RING | B14 sign · B16 Nerve through the wire · LOCKER | slip it on her finger at Bay 6 (R39) |
| TABARD | W25 the Sister's office · B23 linen services | rounds pass you (W10, M23); at Bay 6 take it off (R32) or Night Staff |
| FIRST-AID KIT / LUGGAGE TAG | H14 / H15 (Lost Property, one item) | tag = Layover cameo, −2 Fear |
| KNOWS_1979 (hidden) | A25 Ros, W24 the rota, H12 the tea lady | 1979 − 1800 = **179** |
| FIRST_BAND (hidden) | B19 the 1991 incubator, M03 the register | born 01:47 → **147**, the coda after 200 |

## Endings

| Ending | Requires |
|---|---|
| **Visiting Hours** (true, 200) | all three items (gate) · obs charts walked right · ≤ 3 fields at Bay 6 · tabard off · refuse the form · Ros with you · MENDED (kept through R25, or earned late at R41) |
| **Ward 9** (secret coda, 147) | reached *after* 200: its last line invites the reader who knows 01:47 (B19 or M03) to turn to it. Nobody loses the true ending to find it |
| **Kept** | sign the consent form at Bay 6 (R33, or R31 at 4 fields) |
| **Night Staff** | keep the tabard on at the curtain (R32), or choose it at 4 fields (R31) |
| **Only Child** | Ros WARDED and not rescued when you refuse the form (R37) |
| **Readmitted** (loop) | Ros with you but no MENDED (or MENDED lost at R25) when you refuse the form (R36). Restart at 1 with 1 field |
| **Admitted** | 5 fields, or ticking 06:00, or Fear at Nerve + 3 (global), or "let her tuck you in" at 4 fields (R31) |

## Deaths (each returns you to a checkpoint; from the Main Corridor onwards each also fills one more field)

| Death | What kills you | Warning (rule) and clue | Back to |
|---|---|---|---|
| D01 There you are (no field) | answering "Maureen?" ("Is there news?") | Notice 2 (A23, one page earlier) | A17 |
| D02 Visiting hours are over (no field) | telling the porter you're visiting | Notice 1 (A23) | A24 |
| D03 Lights out | hiding in the empty bed on the round (W10), or lying down beside Ros (W28) | Notice 3 (A23); the Kept (W05) | W01 |
| D04 Signed | signing the chapel book for a prayer for Mum | Notice 6 (A23) | W01 |
| D05 Down only | the Basement lift up after 03:00 | Notice 4 (A23); the lift going down (A36) | B01 |
| D06 Collected | stopping in night setting in the mortuary corridor | Notice 7 (A23); the trolley at A19 | B01 |
| D07 Tucked in | lying in your old bed on Ward 9 | Notice 3 (A23) | M01 |
| D08 Closed | opening the WARD 0 stairwell door from Maternity | Notice 5 (A23) | M01 |
| D09 Wait for me | stopping for "Ros" calling "Bean" at the crossing | Notice 7 (A23); Ros doesn't call you Bean (A02) | R01 |
| D10 Beside her | lying down beside Mum at Bay 6 | Notice 3 (A23); the Kept (W05) | R16 (redo the charts) |
| D_VIGOUR Spent | Vigour 0 (four fights: W26, B05, M15, R03) | sheet | last checkpoint |

Each death offers a real temptation (news of Mum, a hiding place, a prayer, a shortcut, your sister's voice, your
mother's arm). Checkpoints come before every fight: W01, B01, M01, R01. There are also checkpoints at A01, H01 and R16.

## Gate 2 decisions (the author, 2026-11-02)

1. **Clock:** one spare hour. No box ticked at the start; the thresholds in ticks are unchanged (≤4 lucid, 5 = +1 field,
   6th = Admitted); the lifts go down after the 3rd tick.
2. **Secret:** 147 is a coda after 200 (hidden-number invitation at the end of 200).
3. **Late MENDED:** yes, at Bay 2 (R41), costing one wristband field.
4. **Deaths:** Act 1 deaths cost no field; deaths from the Main Corridor onwards cost one.
5. **Confirmed as drafted:** the late cost at R25 (Ros wants to do Mum's obs); no loop mercy at 4 fields; rule 5 is broken
   by design (the Sister is already inside Ward 0). **Names:** Maureen "Mo" Doyle, née Brennan. **Date:** a Thursday
   night in November.

Remaining wording point for writers (CANON.md, Clock): with no pre-ticked box, the reader's first tick is labelled
01:00 although the book opens at 01:40. CANON treats the boxes as the Sister's rounds and the corridor clock as the
hospital's time, not yours. If the author would rather relabel the boxes 02:00–07:00 (keeping "≤4 / 5 / 6th"), only
the sheet row and the rules page change.

## Engine gaps (worked around; engine code untouched)

- `engine/reference.py` uses `write_text` without importing it, so `numbermap` and `stateref` crash. They were run
  with the import injected at call time. It needs a one-line fix:
  `from .config import write_text`.
- Tracking ROUNDS and WRISTBAND together exceeds memory; each is proven exactly on its own.
- Links can't carry their own stat costs, so every per-option cost is its own section. The two exceptions are the
  failure labels at A32 and B15 ("lose 2 Vigour"), which follow the Layover's pattern; Vigour isn't tracked anyway.
- The clock ticks on exit→hub moves, so the 06:00 rule is a global `limit:Rounds` link on the three clock hubs. (The
  Layover's `hours6` links on exit sections can't fire under exact tracking, because the tick lands on the hub.)
- Deaths are terminal. The field each death adds, and the loop ending's "restart with 1 field", aren't modelled by
  the verifier. The rules page carries them.
- The Fear limit is dynamic (Nerve + 3), so the verifier only knows it as "possible".
- There is no OR in conditions, so R19 needs two links for "not MENDED, or MENDED but Ros is WARDED".
- **Ending with a link (the coda).** The engine forbids links from terminal kinds, so section 200 is kind
  **`finale`** (not terminal), with a single hidden link to the terminal coda 147. Consequences, all worked around in
  config: FIRST_BAND is listed as loose, so the hidden link counts as always open and 200 never looks softlocked
  for readers who never learned 01:47 (FIRST_BAND's two sources are still proven reachable); `ending_below_limit`
  checks SECRET (reachable only through 200 and adding no fields, so it is the same proof); `min_words.finale = 200`.
  **Still needed in the engine, not yet done:** (a) `build_epub` prints "THE END" only for `kind == "ending"`, so 200 needs
  it in prose or an engine change to also mark `finale`; (b) `coverage` / `playthrough` / `sheet` treat only `ending`
  as a route end, so a route reaching 200 without FIRST_BAND will look unfinished; (c) the verifier's ending report
  omits 200. A clean fix would be a `"coda_links"` allowance (terminals may carry hidden links to listed coda
  sections) or `"finale"` added to the ending kinds in those modules.
- **Death cost of 0.** `check.death_end` is one template ("Fill in {cost} more field…"), and `briefs.py` prints
  `cost or 1`, so the briefs for D01/D02 still say "Fill in 1 more field". The section notes for D01/D02 override
  this (end with "Return to {X} and choose again." only). An engine fix: a `death_end_free` template when the
  cost is 0. Writers and the prose check must follow the notes until then.
- No `entity.py` overlay (it's optional). The entity's rules and lore live in BIBLE.md, CANON.md and the section notes.
- `prose/act1.json` held the template's placeholder drafts for keys this book reuses (A01, E_TRUE…). It was emptied
  so the story map doesn't show wrong text. No prose was written.
