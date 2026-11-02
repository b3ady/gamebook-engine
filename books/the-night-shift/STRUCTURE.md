# THE NIGHT SHIFT: structure summary (stage 2, for Gate 2)

200 sections, 7 endings, 10 rule deaths + 1 shared Vigour death. `verify`: **ISSUES 0**. Untracked: 366,979 states,
0 softlocks. **ROUNDS tracked exactly:** 1,618,147 states, ISSUES 0. **WRISTBAND tracked exactly:** 2,104,695
states, ISSUES 0. Tracking both together runs out of memory; each was proven separately, as the Layover's were.
The story map is `build/story-map.html` (structure only, no prose yet). Flag ledger and every way into each section:
`build/STATE.md`. Printed numbers: `build/NUMBER_MAP.md` (seed 13).

## Acts and zones

| Act | Zone (brief) | Sections | Contents |
|---|---|---|---|
| 1 | Level 3 (`act1`) | 38 | Family room 01:40 → Ros → the surgeon's question → property bag → first round (tea, the 1st field) → night setting → anomaly tutorial → **the Notice (A23, master clue)** → "Maureen?" (D01) → the porter (D02) → the funeral line → lift to Level 1 |
| 2 | Main Corridor (`corridor`) | 22 | Hub H01; first return H02 (+ Ros's scene H03/H04); second return H05 (the Sister's offer); tea bar, Lost Property (Larkvale tag), payphone, red floor line; the Maternity lift / stairs (HL/HLD/HS) |
| 2 | Old Wing (`oldwing`) | 33 | Nightingale ward of the Kept, Gary 1986, the round in unison, the chapel, the Sister's office, Ros's side room. **VISITOR'S BADGE** |
| 2 | Basement (`basement`) | 30 | Medical Records (the file, the LPA, the letter), Property (the ring, locker 179), the mortuary corridor and the 1991 incubator, linen, porters' lodge, the lift that only goes down. **MUM'S LETTER** |
| 2 | Maternity & Ward 9 (`maternity`) | 28 | 1991 register, the nurses'-station phone (Mum from tomorrow), delivery suite, Ward 9 and Mum's chair, parents' room, the WARD 0 stairwell door. **THE LAST RULE** |
| 3 | Ward 0 + endings (`act3`) | 49 | The crossing, the door, Handover 1979, the reckoning, claim-back, Bay 2 rescue, **the obs-chart walk** (anomaly loop), Bay 6, the Sister in full, the consent form, the climax, 06:00, 7 endings + D_VIGOUR |

Kinds: 93 story, 54 choice, 16 item, 8 test, 4 combat, 7 anomaly, 11 death, 7 ending.

## Critical path (the true ending)

Act 1 on any route (pass A23, the Notice); earn **SPOKE** (A10 / A35 / H04 / W19) and **HELD** (A28 / W04 / M26 / any
rescue) along the way. Main Corridor (no tick on first arrival). **Old Wing** → badge (Gary, the chapel clip, or the
office drawer) → back (02:00 ticked; Ros's scene). **Basement** → the letter (Records, or locker 179) → lift up while it
still goes up, or the stairs (03:00 ticked; the Sister's offer: refuse, keep Ros). **Maternity by the stairs** (the lift
goes down after 03:00) → Ward 9 → give Ros Mum's chair → **MENDED** → the strip under the mattress (04:00 ticked).
**Ward 0**: the crossing → break rule 5 → Handover 1979 → reckoning at 04:00 = Mum's lucid moment (−1 field) → Ros reads
the letter aloud (−1 field) → the charts (Bay 3 walk on, Bay 4 turn back: let Ros be the one, Bay 5 turn back) → Bay 6
with ≤3 fields → refuse the form → **Ros reads Mum's name, you hold her hand, you let her go** → 06:00 → **06:02,
Visiting Hours (200)**, or **147** if you know the minute you were born.

## Mechanics

**WRISTBAND** (stat `Wristband`, field `band`, 0–5). Five fields: NAME, DATE OF BIRTH, NEXT OF KIN, WARD, BED.
- **Fills (+1):** accepting comfort or giving details: tea in the family room (A14), the Sister's blanket (H10), the
  tea bar (H11), "next of kin: me" on the payphone (H17), standing by a bed on the round (W12), failing to steal the
  chapel badge (W17), signing the Records slip (B03), signing for the ring (B14), answering the mortuary drawer (B20),
  caught on the Maternity round (M13), **the 05:00 round at the reckoning (R09)**, and **every death** (+1).
- **Empties (−1), only when claimed back:** Ros's scissors (W27, needs SPOKE; R12, needs HELD), Mum on the phone from
  tomorrow (M09), Mum's lucid moment (R08, ROUNDS ≤ 4), Ros reading Mum's letter aloud (R11). At the reckoning you get
  R11 or R12, not both.
- **Bites:** 3+ at the crossing = the porters know a patient (R03, a fight). **4+ at Bay 6 = the true ending is closed**
  (R31: Kept / Night Staff / Admitted). **5 = Admitted** (global rule, verifier hook after every +1 section).

**ROUNDS** (clock, six boxes 01:00–06:00; the 01:00 box is ticked before section 1). Tick on every move from a zone
exit (W29, W30, B29, B30, M28, M29, HLD) to the Main Corridor (H01/H02/H05). The first arrival from Act 1 doesn't tick.
- 03:00 ticked: the lifts go down only. Taking the Basement lift up = D05; taking the lift to Maternity drops you to the
  Basement and costs another tick (HLD). Stairs always work.
- At the reckoning (R07): **≤ 04:00 → Mum's lucid moment** (−1 field, −2 Fear); **05:00 → one more field**.
- Ticking **06:00 → Admitted** (global rule on the three clock hubs).
- A perfect run (three zones, no retreats) arrives at 04:00. One extra trip (a retreat, the lift after 03:00, or
  fetching Ros from the Old Wing via the hub) means 05:00; two extra trips mean Admitted. See question 1.

**Relationship codewords:** SPOKE (4 routes) → HELD (6 routes, incl. every rescue) → **MENDED** (3 routes, each needs
SPOKE and Ros present: chapel W21 also needs HELD; Records B09; Ward 9 M22). **Late cost:** at Bay 4 (R25) Ros wants to do
Mum's obs herself ("I'm the one she named"). Let her = +2 Fear; take the chart = lose MENDED.

**WARDED** (Ros taken): 3 ways (accept the Sister's bed for her H07; let her lie down on the Old Wing W03; let her nap
in the parents' room M27). **3 rescues**, each giving HELD: say her name in the Old Wing side room (W28 → W31; from the
hub once the zone is shut, at the cost of a tick), tear up her new file in Records (B21/B22), say her name in Ward 0
Bay 2 (R14/R15). Not rescued at the end = Only Child.

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
| FIRST_BAND (hidden) | B19 the 1991 incubator, M03 the register | born 01:47 → **147** |

## Endings

| Ending | Requires |
|---|---|
| **Visiting Hours** (true, 200) | all three items (gate) · obs charts walked right · ≤ 3 fields at Bay 6 · tabard off · refuse the form · Ros with you · MENDED (kept through R25) |
| **Ward 9** (secret, 147) | as above, plus the hidden 01:47 (B19 or M03): at R38 "turn to the time you were born" |
| **Kept** | sign the consent form at Bay 6 (R33, or R31 at 4 fields) |
| **Night Staff** | keep the tabard on at the curtain (R32), or choose it at 4 fields (R31) |
| **Only Child** | Ros WARDED and not rescued when you refuse the form (R37) |
| **Readmitted** (loop) | Ros with you but no MENDED (or MENDED lost at R25) when you refuse the form (R36). Restart at 1 with 1 field |
| **Admitted** | 5 fields, or ticking 06:00, or Fear at Nerve + 3 (global), or "let her tuck you in" at 4 fields (R31) |

## Deaths (each fills one more field and returns you to a checkpoint)

| Death | What kills you | Warning (rule) and clue | Back to |
|---|---|---|---|
| D01 There you are | answering "Maureen?" ("Is there news?") | Notice 2 (A23, one page earlier) | A17 |
| D02 Visiting hours are over | telling the porter you're visiting | Notice 1 (A23) | A24 |
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

## Open design questions for the author

1. **How hard the ROUNDS clock bites.** With the 01:00 box pre-ticked (so the boxes match the bible's 01:00–06:00), a
   perfect run reaches Ward 0 at 04:00, one extra trip at 05:00 (+1 field), and two extra trips mean Admitted. That's
   strict but it is a real cost. **(a)** keep it; **(b)** start unticked (perfect = 03:00, Admitted needs three extra
   trips: gentler, but the Layover's HOURS shows this risks being decorative); **(c)** keep it, but make the Old Wing
   rescue via the hub free (no tick).
2. **Where the secret ending sits.** Now: a hidden link at R38, only on the true route, so 147 *replaces* 200. Options:
   **(a)** keep it; **(b)** make it a coda after the true ending ("If you know the minute you were born…" at the end
   of 200); **(c)** a separate branch from the register at M03 (a dream at 01:47 that ends the night early).
3. **MENDED needs Ros beside you mid-book.** A reader whose sister is taken early and only rescued in Ward 0 (R15)
   can't reach the true ending (rescue gives HELD, not MENDED). Intended (the "say it first" loop), or should R15
   offer a short MENDED exchange if you have SPOKE?
4. **The late cost (R25).** Now: Ros wants to take Mum's obs herself. Alternative: the Sister offers *Ros* the pen
   as the LPA holder, and you must let her refuse. That would be stronger, but it doubles up with the consent form at
   R33. Which do you want?
5. **Deaths fill a field.** The bible says fields fill when you die, so five deaths mean Admitted, and with comforts
   it is fewer. Keep (deaths matter), or deaths cost a field only after Act 1?
6. **Four fields.** Now: Kept, Night Staff (with the tabard) or Admitted. Should Readmitted (the loop) also be offered
   there as a mercy route back to 01:40?
7. **Rule 5 is broken by design.** The reader must open WARD 0 to finish. The entity's late rule-break is that the
   Sister can't follow you through the door, but she's already inside (R06). Does that work for you, or do you want
   a different late rule-break (e.g. she reads a loved name once, at R02)?
8. **Names and dates.** Mum's maiden name and surname (the "M." tape; the full name Ros reads at R35), and tonight's
   date (the TICKET's "Saturday" assumes a weeknight).

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
- No `entity.py` overlay (it's optional). The entity's rules and lore live in BIBLE.md, CANON.md and the section notes.
- `prose/act1.json` held the template's placeholder drafts for keys this book reuses (A01, E_TRUE…). It was emptied
  so the story map doesn't show wrong text. No prose was written.
