# THE NIGHT SHIFT: Round 2 review B (horror fan + game flow)

## 1. Verdict: 8/10 (prev: 7.5)

The kindness-as-weapon design is now backed by a visible cost curve, the finale finally bites (the cap lifting off at §196 is the scare the true ending lacked), and most of the sloppy r1 flow breaks are closed. What remains is mostly bookkeeping the reader cannot see: a hidden Fear clock in the chart loop, a true ending that closes silently, two reward lines that fire on an empty wristband. Would I recommend it? Yes. Based on route01 (true ending, 153 reads) and route03 (Kept, 147 reads), FRONT_RULES, BIBLE, prose/act3.json endings.

Note on the playtest: route03 reaches "Fear +14" at §106 and keeps playing. Under the printed rules Fear 12 sends you to Admitted, so that route would have ended about a third of the way through the chart loop. The harness does not enforce the limit.

## 2. r1 tracking

1. Hubs re-read in full: **Partial.** §98/§171/§87/§107/§129 now open with a return block (about 40 words, "Go straight to the choices"). But the first-time `>` block covers only paragraph one; the next three paragraphs are unmarked. Only §17 says "Otherwise:". Reads in route01: §98 ×9, §171 ×7.
2. Night Sister never escalates: **Partial.** §98 return variants (shutter, trolley, folder, torch) and the §158 torch-by-bay lines help. Rounds 3 to 5 still have no scene, and route01 sits on 3 ticks.
3. Rule quoted before choice (compliance quiz): **Fixed** for quoting (§156, §44, §46 are clean; §168 "This is a chair" and §101 "rule 6 was written in 1979 by somebody…" are tempting, which is correct). The safe option is still often the free one (§44, §46).
4. §100/§28 free pass and muddled bedside/tabard: **Partial.** §183 now charges Fear +1 for walking straight out. But §100 still offers both "with the VISITOR'S BADGE… turn to 165" and "stand at a bedside like a visitor… turn to 78", and §28 "fall in beside her and do the round. Turn to 87" still points at the hub it came from.
5. §119 Ward 0 stair door: **Fixed.** "This is the field this death fills; fill in nothing else", and the hub says "if you have not already tried the door". (Edge case in problem 11.)
6. Level 3 deaths return to §85 and Fear re-accumulates: **Still.** §178 says "Return to 85 and choose again." Route01 replays §85, §21, §94, §13, §37, §157, §99 three times, and §13 and §92 give "Lose 1 Fear" each time.
7. Cross-offs gated on filled fields: **Partial.** §16 and §144 now say "at least one field". §102 ("Cross off 1 field on your Wristband") and §29 still have no gate; route01 hits §102 with 0 fields.
8. §161 undocumented three-field penalty: **Fixed**, vaguely. FRONT_RULES now says "At 3 or more fields, staff begin to recognise a patient." It does not say a fight follows.
9. Finale has no jeopardy: **Partial, mostly Fixed.** The §158 torch variants plus the 2 Fear per fold are a real clock. The §196 offer ("Maureen" in all her voices, "The starched cap lifts off her head on its own") is the missing climax. The clock is invisible, though (problem 1).
10. §106 explains its own image: **Fixed.** It now ends "She has kept the kindness and thrown the rest away."
11. §196 dissolve too gentle: **Fixed.** Cap lifts, "Mum's eyes turn towards the voice", then the dissolve and the wink.
12. Notice "Believe them.": **Partial.** The line is now "Believe them, until you have a reason not to." Rule 1 against the VISITOR badge is half-reconciled by Gary's "That's the rule." All seven rules still print in full at §37.
13. Care has no temptation: **Partial.** Care now pays Fear (§168 "Lose 3 Fear", §95 "Lose 2 Fear"). Fear is floored at 0 and sits near 0 for the first two thirds, so the first and loudest offer (§198, "Lose 2 Fear" at Fear 0 to 1) buys nothing.
14. Fear near the limit by mid-book: **Overcorrected.** Real route01 Fear peaks around 3 before Ward 0 (drains at §95, §113, §174, §176, §29), then climbs to about 10 in the chart folds. The mid-book Fear track is now decoration, and the finale spike has no warning.
15. §127/§170 sack silently deletes items: **Partial.** §170 now states the loss ("everything in it has gone with it") but §127's choice text carries no warning before the reader commits.
16. Round tick in four places: **Fixed.** Each return section (§70, §155, §68, §24) ticks once before branching; §98 no longer ticks.
17. Obs chart not checkable: **Partial.** §126's 06:02 is a clean future time and §50's Ros handwriting is fair. §173 still says "at or before the hour on the station clock" and the hour is never printed.
18. §149/§125 choices leave no mark: **Still.** Route01 reaches §127 with a blank sheet. Only "We both do" then "ask her what she isn't saying" sets SPOKE (§120).
19. Admitted ending end-marker and cause: **Fixed.** E_ADMITTED has the three cause conditionals and THE END plus restart line. (E_KEPT has neither; problem 12.)
20. Continuity: **Mostly Fixed.** Thursday (§102, §77), D. Hollis (§153), "seven o'clock last night" (§196) and the right/left hand (§200) are all clean. Still: §139 "If you have a cup, turn to 95" is not a condition.

## 3. Ranked problems

1. **§158 / §84 / §50 / §45 (chart folds):** "Gain 2 Fear. Test your Fortune." The clock is invisible and lethal. Each wrong call is +2 Fear toward a 12 limit the page never mentions (route03 shows Fear 14). In Survival Mode each fold also burns 1 Fortune, and at 0 you are "always Unlucky", so one misread becomes a spiral. The reader cannot tell a bad fold from their own error. Fix: drop the Fortune test and alternate the Lucky and Unlucky wards by fold count. Print "Fear X of your limit" at §158. Make the fourth fold an explicit turn to E_ADMITTED, with the torch variants as its warning.
2. **§160 vs §198:** "There's a band on it… You don't remember it going on." Tea-takers already saw the band at §198 (Ros: "Since when have you had that?"). §160 then reveals it again as new, and the overlay "one of them already is" contradicts its own first paragraph. Fix: put "*If you have already seen the band,*" first in §160 and cut the reveal paragraph for them.
3. **Silent loss of the true ending (§156 sign the slip, §18, §35, §168):** route03 hits 4 fields by the Basement ("Wristband +4") and plays about 100 more sections with nothing to tell it that "the recovery room won't let a patient visit a patient". The only feedback is §106 turning to §75. Fix: add to the §98 return block, "Count your Wristband. Four filled, and the recovery room will not let you through." Add the same line to §17.
4. **§100 / §78:** "If you stand at a bedside like a visitor, hands folded, turn to 78." Route01 holds the badge, pinned since §20, takes the 78 option and still gets the WARD field. Fix: label 78 "(if you have no badge or tabard)". In §28 the TABARD option should go to §165, not §87.
5. **§102 and §29:** "Cross off 1 field on your Wristband." Both are ungated. At §102 the Mum phone call is reachable on the first Level 5 visit with 0 fields, and the text says "the plastic there is clean". Fix: "If at least one field is filled, cross off 1; otherwise Lose 2 Fear", for both.
6. **E_LOOP vs FRONT_RULES:** E_LOOP says "Rub out your Wristband, then fill in 1 field again". FRONT_RULES says keep the Wristband and cross off down to 2 fields. Pick one. I prefer the E_LOOP version ("the hospital remembers you"); change FRONT_RULES to match it.
7. **§198 / §95 / §168 (care economy):** "Lose 2 Fear" at Fear 0 is a pure cost, and a smart reader learns to take care only when Fear is high. The undo tools are also cheap: two scissors snips (§16, §144, 1 Vigour each, and Vigour is decorative), Mum's phone voice (§102) and Mum's call from Bay 6 (§29). Admitted by fields becomes nearly unreachable. Fix: make the first tea pay something real (a true line about theatre), cap undo at 2 per run, and have scissors cost 1 Fortune or a Fear point rather than Vigour.
8. **§127 / §170:** "If you can't, not yet, and you leave it zipped on the chair, turn to 170." The loss is explained only after the choice. Fix: put "(it will not be there when you turn round)" in the choice line.
9. **§178 (and every Level 3 death):** "Return to 85." The replay is two pages long and Fear is farmed at §13 and §92. Fix: return to §157 (✈) and print in the rules that Fear reverts to its checkpoint value.
10. **§102 spoils the siblings' scenes:** Mum says "I sent her, you know" and "And I kept you" to a reader who has not had the Ros conversation. Everything §174 and §153 later trade is already known, and SPOKE is bypassed. Fix: the SPOKE-less version should be a hiss and "Has your sister said owt?", with the two admissions saved for readers who hold SPOKE.
11. **§119 vs §78 (WARD field):** if WARD is already filled by §78, the door's "fill in nothing else" costs nothing. Fix: "if WARD is already filled, fill in the next empty field". Same family: the kit vs luggage-tag choice at §142 (restore 6 Vigour, which is decorative, against Lose 2 Fear) is not a choice. Give the kit a Fear or Fortune effect.
12. **E_KEPT and E_NIGHTSTAFF:** E_KEPT ends on "You are so good at it." with no THE END and no restart pointer (route03). Add both. Also: §139 "If you have a cup, turn to 95" should read "If you take a cup"; §173 should print the station clock hour; set a one-word flag at §125/§149 so §196 or §200 can echo the answer.

## 4. Keep

1. §119: "Rule 5 said Ward 0 was closed. It didn't say what to."
2. §196: the cap lifting off and "Maureen Doyle,' says Ros. 'Née Brennan.'", then the last girl's wink.
3. §29: "'Bean? Is that you making that racket?'" (Mum's voice at the worst moment, and the field going blank).
4. §200: "'Not one word,' says Ros. 'Get in, Bean.'" with the THINGS TO SAY TO BEAN echo.
