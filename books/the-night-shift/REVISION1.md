# THE NIGHT SHIFT — Revision 1 (after review round 1: A 7.5, B 7.5)

Reviews: reviews/r1/A.md, reviews/r1/B.md (printed numbers; translate with reviews/r1/NUMBER_MAP.md). Also LEAD_NOTES.md. Edit prose only; the lead has made the structural changes below and regenerated briefs/*.md. Keep every {TOKEN}; never add or remove choices. Keep every "Keep" quote in the reviews. After editing, `python3 -m engine books/the-night-shift check <zone>` and `tics <zone>` must be clean.

## Structural changes already made (write them into the text)
- A34 ("I meant it") now gives SPOKE: Ros answers in her own anger ("Then say the rest") and it opens her up. No Fear. A35 ("I shouldn't have said it") gives no SPOKE, Lose 1 Fear: easier, warm, but nothing real moves.
- A06: no Fear cost now.
- W21 no longer gives MENDED (it reveals the two requests, but the mending comes later). Remove "Note the codeword MENDED" there.
- Care tempts in Fear now: A14 tea = Lose 2 Fear (no Vigour) + 1 field; H11 = Lose 2 Fear + 1 field; H10 = Lose 3 Fear, Gain 2 Vigour + 1 field. State these.
- Ros's scissors (W27, R12) only offered when at least one field is filled (choice text in the sections that link to them should say "if at least one field of your Wristband is filled").
- The Ward 0 stair door (D08) can only be tried once (the hub/zone choice that leads to it should say "if you have not already tried the door").

## Book-wide
1. **Wristband lines, exactly:** "Fill in 1 more field on your Wristband." and "Cross off 1 field on your Wristband." (capital W; name the field after a colon if the book names one, e.g. "…on your Wristband: NAME."). Death sections: one statement only (D08's WARD field IS its death's field: no second fill).
2. **Mum's requests, one canonical set** (A#3, A#2): the kitchen = the Legion kitchen at the wake, at the sink, hat still on, Ros's offer letter from her handbag; the stroke unit = second night, Mum's good hand round your wrist. Her line to Ros varies by reader exactly as B09 does ("your sister" / "your brother" / "our kid"): apply in W21, M22, R41.
3. **Tics to cut** (A#13–15, A tic counts): "unhurried/never hurries" ≤ 8 book-wide; "six years" ≤ 15; "dent in the pillow" ≤ 4; the empty-trolley tableau fully described once (A19), elsewhere a glimpse; "You're good at it / You've had the practice" only in E_KEPT, E_NIGHTSTAFF, W04; Ros's "One. Two. Three." list ≤ 3 (keep M26, R11); the hand-in-bag "stayed there" gesture ≤ 2. "If Ros is with you" blocks: one per section, and each must change something (cut reaction-shot blocks).
4. **Captioned subtext** (A#15, B#10): cut lines that explain the image (e.g. A10 "the most honest thing…", R26/R27/R10 equivalents; R30's last two explanatory sentences EXCEPT keep "She has kept the kindness and thrown the rest away." — that's a reviewer Keep; cut what follows it).
5. **Rules quoted before choices** (B#3): don't quote the Notice rule in the paragraph right before a choice unless breaking it is tempting. Let the reader remember.
6. **Okafor ×3:** rename the LPA witness in B07/B08 to "D. Hollis". Keep J. OKAFOR (rota, 1979) and Joseph Okafor (Bay 5).
7. **Day:** tonight is Thursday night into Friday morning. Fix any "Friday in November" (§77) to Thursday night.

## By zone
**act1 (A01–A38, D01, D02, FRONT_RULES):**
- A33–A35 as above. A10: cut captioned subtext.
- A11/A12: when you leave the property sack unopened, warn that what's inside goes with it (B#15).
- FRONT_RULES: under The Wristband add "At 3 or more fields, staff begin to recognise a patient." Under the Notice change "Believe them." to "Believe them, until you have a reason not to." Under Checkpoints/death: "Level 3 deaths cost no field." Confirm FRONT tokens.

**corridor (H01–H18, HL, HLD, HS):**
- H01 is re-read up to 7 times (B#1): put the "*If you have been here before,*" return block FIRST, ≤ 40 words, and make it vary by how many rounds are ticked (B#2): 1–2: the tea-bar shutter lower; 3: the porter's trolley parked outside the tea bar, made up; 4: the Sister at the hatch with your folder; 5: the corridor already on night setting, her torch at the far end. Then "Go straight to the choices." Trim the first-visit description to ≤ 170 words.
- H02/H05: "Tick one round on your Adventure Sheet." stated once, before any branching; H01 must not tell the reader to tick (no double ticks) (B#16).
- H03 "THINGS TO SAY TO BEAN" stays; see E_TRUE.
- H10, H11 as above (care pays Fear).

**oldwing (W01–W31, D03, D04):**
- W10/W11 (B#4, A#7): the walk past the round should cost: "Gain 1 Fear" for walking on (W13 — add to W13's opening if the reader came from W10). W11 must read right for the TABARD reader too ("*If you are wearing the TABARD,*" she nods you into line as staff; the "Visitors," she says fondly line only for the badge reader).
- W03 (A#9): Ros "four in a family room" → true for a reader who has known her ten minutes; reword.
- W21 per book-wide 2; remove MENDED.
- W25 vs B23 tabard (A#11): W25 keeps "It fits you better than your own coat"; name tape over the pocket; smells of Fairy Snow.

**basement (B01–B30, LOCKER, D05, D06):**
- B07/B08 witness → D. Hollis. LOCKER: add one Ros line establishing the LPA names her (A#10) so R25 lands for LOCKER readers.
- B23: vary the tabard description (no "fits you better" line).
- B30 stair arithmetic (A#12): it's one floor up to Level 1 (ground is G only on the lift panel's older buttons) — make B30 consistent with the corridor being Level 1 and the lift panel B / 1 / 3 / 5 (no G).

**maternity (M01–M29, D07, D08):**
- M03 (A#5): the birth certificate shows the date only; you have never known the minute. (B19 depends on this.)
- M13 (A#9): "Bed 3. Your bed… on Ward 9" — true only if the reader has been to Ward 9; make it conditional or reword so it's the Sister who says it and you don't yet know why.
- M09 (A#16): add one Mum line to the player: "And I kept you, which I'd no business doing."
- M22 per book-wide 2. D08 (B#5): single wristband statement; say plainly the WARD field is the one this death fills.

**act3 (R01–R41, D09, D10, D_VIGOUR, endings, E_TRUE, SECRET):**
- R05 (A#8): badge name line blank unless the reader wrote it (W06 Gary's badge has your name in a child's writing — conditional on PROMISE/Gary route); R39 ring is on your little finger (B14) — "you slide it off your little finger".
- R19→R20 (A#19): add a bridge line ("the ward has turned while your back was…") so "turn back" doesn't read as going forward; R23 choice wording likewise.
- Finale jeopardy (B#9, B#11): each wrong turn on the chart walk brings the red torch one bay nearer (say so in the text of the turn-back sections, cumulatively); at R35 before the faces step out, one last offer: all her voices say "Maureen" together and the cap lifts — then the dissolve as written (keep the wink).
- R30: keep "She has kept the kindness and thrown the rest away."; cut the sentences after it that explain.
- R35 (A#18): Mum's real A&E band time "seven o'clock last night".
- R41 per book-wide 2.
- E_ADMITTED (B#19): ends with THE END and the back-to-the-beginning line; open with a line that varies by cause only if it can be done with conditionals (fields / rounds / Fear).
- E_TRUE (A#6, A#20): fix the bad-hand contradiction (her right hand is the one that works; she lifts the left with the right); untangle "since Dad. You haven't, yet. You will, later, in the car."; add a ten-word car-park echo of Ros's phone note "THINGS TO SAY TO BEAN" (one line under the title now) before "Get in, Bean."
- Gary's mum's anorak: blue (match W06 canon).
- Glasses: brown market frames, Sellotape on the hinge (match A11 canon) — fix R-section descriptions that say tortoiseshell.
