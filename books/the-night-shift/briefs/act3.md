### R26 — Hers  [story, Act 3, Ward 0]
Arrives from: R25 (Her handwriting)
Beat: You let her. Her hands are shaking and her numbers are right. It costs you something you've held for six years. Gain 2 Fear.
Links (write each target as a token):
  - {R20}  "Continue"  → leads to: Bay 5
Effects (state them in the text, using in-world names): Fear +2

### E_KEPT — ENDING: Kept  [ending, Act 3, Ending]
Arrives from: R33 (The consent form), R31 (A patient can't visit a patient)
Beat: You sign. Mum is Kept, smiling, for ever. You visit every night. You are very good at it.

### R25 — Her handwriting  [choice, Act 3, Ward 0]
Arrives from: R19 (Bay 4)
Beat: Ros has the chart. 'I'm the one she named. Let me do this.' She wants to take Mum's obs herself, tonight, every hour.
Links (write each target as a token):
  - {R26}  "Let her be the one"  → leads to: Hers
  - {R27}  "Take the chart off her: you've done this for six years"  → leads to: Yours
Design note: LATE COST on the kind route: a test of MENDED. Cost both ways.

### D_VIGOUR — Spent  [death, Act 3, Ending]
Arrives from: W26 (The night porter), R03 (The porters), M15 (Theatre staff), B05 (The porter)
Beat: You sit down on the lino and can't get up. A trolley rolls toward you.
Effects (state them in the text, using in-world names): Wristband +1
Death — the warning the reader was given: Vigour is always visible on the Adventure Sheet.  End: 'Fill in 1 more field on your wristband. Return to {LAST} and choose again.'
Design note: Global rule: Vigour 0. Return to your last checkpoint.

### R08 — Lucid  [story, Act 3, Ward 0]
Arrives from: R07 (The reckoning)
Beat: Reward. From Bay 6, for one breath, Mum's real voice: 'Bean? Is that you making that racket?' A field on your wristband goes blank. Cross off one field of your wristband. Lose 2 Fear.
Links (write each target as a token):
  - {R10}  "Continue"  → leads to: Claimed back
Effects (state them in the text, using in-world names): Fear -2; Wristband -1
Design note: Mum's lucid moment (ROUNDS <=4).

### R06 — WARD 0 - CLOSED  [story, Act 3, Ward 0]
Arrives from: R03 (The porters), R05 (Eyes front), R02 (The crossing), R40 (Saturday's draw)
Beat: The doors. The one rule you have to break. You push, and they open, and the Sister cannot follow you through them; she doesn't need to. She is already at the station inside, writing.
Links (write each target as a token):
  - {R06a}  "If you have PROMISE"  [condition: has PROMISE]  → leads to: Visiting
  - {R04}  "Continue"  [condition: lacks PROMISE]  → leads to: Handover, 1979
Design note: The entity's rule broken once, late: the door she cannot follow you through, and she is already inside.

### R09 — The 05:00 round  [story, Act 3, Ward 0]
Arrives from: R07 (The reckoning)
Beat: 'You're late, love.' She fills in another field for you, kindly. Fill in one more field of your wristband.
Links (write each target as a token):
  - {R10}  "Continue"  → leads to: Claimed back
Effects (state them in the text, using in-world names): Wristband +1

### R39 — Her ring  [story, Act 3, Ward 0]
Arrives from: R33 (The consent form)
Beat: It goes on over the knuckle the way it always did, with a twist. Her hand warms. For a second her smile is her own, crooked, and her obs flicker. Lose 2 Fear.
Links (write each target as a token):
  - {R33}  "Continue"  → leads to: The consent form
Effects (state them in the text, using in-world names): (hidden, never mention) RING_ON; Fear -2
Design note: RING use. One-shot.

### R14 — Ros in Bay 2  [choice, Act 3, Ward 0]
Arrives from: R13 (Bay 2)
Beat: Ros, Kept, smiling, her wristband full.
Links (write each target as a token):
  - {R41}  "If you have SPOKE: say her name, and then say the rest (fill in one more field of your wristband)"  [condition: has SPOKE and lacks MENDED]  → leads to: The rest
  - {R15}  "Say her name"  → leads to: Found
  - {R16}  "Leave her and go on to Mum"  → leads to: The charts
Design note: Rescue route 3.

### E_LOOP — ENDING: Readmitted  [ending, Act 3, Ending]
Arrives from: R36 (Who decides)
Beat: 01:40. The family room. Ros coming through the door with her phone already out. This time, say it first. (Loop: start again from section 1 with the wristband reset to 1 field.)

### R23 — Bay 3, again  [anomaly, Act 3, Ward 0]
Arrives from: R22 (Reset)
Beat: A chart with your name in the patient box.
Links (write each target as a token):
  - {R24}  "Something is wrong - turn back"  → leads to: Bay 4, again
  - {R22}  "Nothing is wrong - walk on"  → leads to: Reset
Design note: Wrong. Correct: turn back.

### R41 — The rest  [story, Act 3, Ward 0]
Arrives from: R14 (Ros in Bay 2)
Beat: You wake her by name and then you don't stop: Bay 2, curtain drawn, the Sister writing at the station. If neither request has been told, THE telling (see W21); otherwise pointer. It takes long enough that the Sister notices: she fills in a field for you while you talk. Fill in one more field of your wristband. Cross off WARDED. Codewords HELD and MENDED.
Links (write each target as a token):
  - {R16}  "Continue"  → leads to: The charts
Effects (state them in the text, using in-world names): Note HELD; Note MENDED; (hidden, never mention) SENT; (hidden, never mention) ASKED; Cross off WARDED; Wristband +1
Design note: v2: MENDED route 4 of 4 (late, costly). Lets a Ros taken early still reach the true ending.

### R28 — Bay 5, again  [anomaly, Act 3, Ward 0]
Arrives from: R24 (Bay 4, again)
Beat: Mum's chart, but the date of birth is yours.
Links (write each target as a token):
  - {R30}  "Something is wrong - turn back"  → leads to: Bay 6
  - {R22}  "Nothing is wrong - walk on"  → leads to: Reset
Design note: Wrong. Correct: turn back -> Bay 6.

### R32 — Visitors only  [choice, Act 3, Ward 0]
Arrives from: R30 (Bay 6)
Beat: A sign on the curtain rail: VISITORS ONLY BEYOND THIS POINT. STAFF TO THE STATION. You are wearing her tabard.
Links (write each target as a token):
  - {R33}  "Take the tabard off"  → leads to: The consent form
  - {E_NIGHTSTAFF}  "Keep it on. Someone has to stay."  → leads to: ENDING: Night Staff
Effects (state them in the text, using in-world names): Cross off TABARD
Design note: Night Staff is a real temptation, not a trap.

### R19 — Bay 4  [anomaly, Act 3, Ward 0]
Arrives from: R18 (Bay 3)
Beat: A 1979 chart. The 03:00 obs are in Ros's handwriting.
Links (write each target as a token):
  - {R25}  "Something is wrong - turn back (if Ros is with you and you have MENDED)"  [condition: lacks WARDED and has MENDED]  → leads to: Her handwriting
  - {R20}  "Something is wrong - turn back (if you do not have MENDED)"  [condition: lacks MENDED]  → leads to: Bay 5
  - {R20}  "Something is wrong - turn back (if you have MENDED but Ros is on the Old Wing)"  [condition: has MENDED and has WARDED]  → leads to: Bay 5
  - {R22}  "Nothing is wrong - walk on"  → leads to: Reset
Design note: Wrong. Correct: turn back. The late cost on the kind route hangs here (R25).

### R10 — Claimed back  [choice, Act 3, Ward 0]
Arrives from: R08 (Lucid), R09 (The 05:00 round)
Beat: Fields come off only when they are claimed back.
Links (write each target as a token):
  - {R11}  "If Ros is with you: give her Mum's letter to read aloud"  [condition: lacks WARDED]  → leads to: Read aloud
  - {R12}  "If Ros is with you and you have HELD: hold out your wrist for her scissors"  [condition: lacks WARDED and has HELD]  → leads to: Snip
  - {R13}  "Go on into the ward"  → leads to: Bay 2
Design note: Wristband reckoning. One claim-back here.

### R33 — The consent form  [choice, Act 3, Ward 0]
Arrives from: R39 (Her ring), R32 (Visitors only), R30 (Bay 6)
Beat: 'Just your signature, love. Next of kin. She'll never be any worse than this.' Mum pats the bed beside her: 'Lie down with me a minute, Bean.'
Links (write each target as a token):
  - {R39}  "If you have the RING: slip it back onto her finger"  [condition: has RING and lacks RING_ON]  → leads to: Her ring
  - {E_KEPT}  "Sign"  → leads to: ENDING: Kept
  - {D10}  "Lie down beside her, just for a minute"  → leads to: Beside her
  - {R34}  "Refuse"  → leads to: Next of kin
Design note: Kept Mum says Bean here: she IS Mum; the danger is lying down beside the Kept, not her voice.

### D10 — Beside her  [death, Act 3, Ward 0]
Arrives from: R33 (The consent form)
Beat: You lie down beside her the way you did at eight. Her arm comes round you. The obs are perfect, both of you, every hour, and the night never ends.
Effects (state them in the text, using in-world names): Wristband +1
Death — the warning the reader was given: Notice rule 3: never lie down on a ward bed; the Kept are harmless unless you lie down beside them.  End: 'Fill in 1 more field on your wristband. Return to {R16} and choose again.'

### R04 — Handover, 1979  [story, Act 3, Ward 0]
Arrives from: R06 (WARD 0 - CLOSED), R06a (Visiting)
Beat: Analog document on the station desk: a night report, Ward 0, March 1979, in a young auxiliary's round hand. Bed 4 asked to be let go and the auxiliary sat with him and let him. Under it, in the Sister's hand: AUXILIARY REMOVED RULE 8 FROM THE NOTICE. NOT TO BE REPLACED.
Links (write each target as a token):
  - {R07}  "Continue"  → leads to: The reckoning
Design note: Lore: where THE LAST RULE came from. One telling.

### R31 — A patient can't visit a patient  [choice, Act 3, Ward 0]
Arrives from: R30 (Bay 6)
Beat: 'Back to bed, love. Patients can't visit patients.' She turns your wrist to show you: four fields.
Links (write each target as a token):
  - {E_KEPT}  "Sign the consent form so Mum can stay"  → leads to: ENDING: Kept
  - {E_NIGHTSTAFF}  "If you are wearing the TABARD: take the night shift instead"  [condition: has TABARD]  → leads to: ENDING: Night Staff
  - {E_ADMITTED}  "Let her tuck you in"  → leads to: ENDING: Admitted
Design note: The 4-field branch: no true ending.

### R38 — 06:00  [story, Act 3, Ward 0]
Arrives from: R35 (Let them go)
Beat: Theatre ends at 06:00. The recovery ward is just a recovery ward. Ros has your hand, or you have hers.
Links (write each target as a token):
  - {E_TRUE}  "Continue"  → leads to: ENDING: Visiting Hours
Design note: v2: the secret-ending invitation moved to the end of 200.

### R36 — Who decides  [story, Act 3, Ward 0]
Arrives from: R34 (Next of kin)
Beat: Ros says it's her, legally. You say it's you, actually. You're both right and neither of you lets go, and the monitor's line goes flat and smooth and starts again from the top.
Links (write each target as a token):
  - {E_LOOP}  "Continue"  → leads to: ENDING: Readmitted

### R18 — Bay 3  [anomaly, Act 3, Ward 0]
Arrives from: R17 (Her glasses), R22 (Reset), R16 (The charts)
Beat: A 1952 chart: temperature, pulse, BP, all normal, all in the Sister's neat hand.
Links (write each target as a token):
  - {R19}  "Nothing is wrong - walk on"  → leads to: Bay 4
  - {R22}  "Something is wrong - turn back"  → leads to: Reset
Design note: Nothing wrong. Correct: walk on.

### R37 — Alone  [story, Act 3, Ward 0]
Arrives from: R34 (Next of kin)
Beat: You read the last rule by yourself. You let her go by yourself. You are good at by yourself.
Links (write each target as a token):
  - {E_ONLYCHILD}  "Continue"  → leads to: ENDING: Only Child

### R03 — The porters  [combat, Act 3, Ward 0]
Arrives from: R02 (The crossing)
Beat: They know a patient when they see one. Two porters and a trolley made up for you. THE PORTERS  NERVE 9  VIGOUR 10.
Links (write each target as a token):
  - {R06}  "If you win"  [condition: fight won]  → leads to: WARD 0 - CLOSED
  - {D_VIGOUR}  "If your Vigour reaches 0"  [condition: fight lost]  → leads to: Spent
Foe line: THE PORTERS  NERVE 9  VIG 10
Design note: Checkpoint before this fight: R01.

### R11 — Read aloud  [story, Act 3, Ward 0]
Arrives from: R10 (Claimed back)
Beat: Ros reads it in her list voice and gets to 'love' and can't. She reads it anyway. Pointer to the letter (B07 told it). Cross off one field of your wristband.
Links (write each target as a token):
  - {R13}  "Continue"  → leads to: Bay 2
Effects (state them in the text, using in-world names): Wristband -1

### D09 — Wait for me  [death, Act 3, Ward 0]
Arrives from: R02 (The crossing)
Beat: You stop and turn. The lights go down to night setting and stay there, and the voice is very close now, and kind, and not your sister's.
Effects (state them in the text, using in-world names): Wristband +1
Death — the warning the reader was given: Notice rule 7: if the lights dim, keep walking. Ros does not call you Bean (A02).  End: 'Fill in 1 more field on your wristband. Return to {R01} and choose again.'

### R15 — Found  [story, Act 3, Ward 0]
Arrives from: R14 (Ros in Bay 2)
Beat: 'Ros.' She wakes cross. 'Did I miss it?' Cross off WARDED. Codeword HELD.
Links (write each target as a token):
  - {R16}  "Continue"  → leads to: The charts
Effects (state them in the text, using in-world names): Note HELD; Cross off WARDED

### R30 — Bay 6  [story, Act 3, Ward 0]
Arrives from: R28 (Bay 5, again), R20 (Bay 5)
Beat: Mum, Kept: smiling, colour good, obs perfect and unchanging. The Night Sister at the bedside with a consent form missing only your signature. Up close her face is every nurse who was ever kind to you - the one who held the sick bowl on Ward 9, the midwife, Mum at twenty-four in a 1979 tabard - assembled, smiling.
Links (write each target as a token):
  - {R31}  "If your wristband has 4 or more fields filled"  [condition: Wristband ≥ 4]  → leads to: A patient can't visit a patient
  - {R32}  "If you are wearing the TABARD"  [condition: Wristband ≤ 3 and has TABARD]  → leads to: Visitors only
  - {R33}  "Otherwise"  [condition: Wristband ≤ 3 and lacks TABARD]  → leads to: The consent form
Design note: The entity seen in full. WRISTBAND 4 closes the true ending here.

### R24 — Bay 4, again  [anomaly, Act 3, Ward 0]
Arrives from: R23 (Bay 3, again)
Beat: Every number normal, every time past. You look for the wrong thing and can't find it.
Links (write each target as a token):
  - {R28}  "Nothing is wrong - walk on"  → leads to: Bay 5, again
  - {R22}  "Something is wrong - turn back"  → leads to: Reset
Design note: Nothing wrong (beats readers who memorised 'turn back').

### R13 — Bay 2  [choice, Act 3, Ward 0]
Arrives from: R10 (Claimed back), R11 (Read aloud), R12 (Snip)
Beat: Bay 2's curtain is drawn. Behind it, a phone is ringing.
Links (write each target as a token):
  - {R14}  "If Ros is on the Old Wing (WARDED): open the curtain"  [condition: has WARDED]  → leads to: Ros in Bay 2
  - {R16}  "Walk on to the charts"  → leads to: The charts

### R17 — Her glasses  [story, Act 3, Ward 0]
Arrives from: R16 (The charts)
Beat: The tape at the hinge, her prescription: the numbers on the charts come sharp. Lose 1 Fear.
Links (write each target as a token):
  - {R18}  "Begin"  → leads to: Bay 3
Effects (state them in the text, using in-world names): Fear -1
Design note: Property-bag item use (GLASSES).

### R20 — Bay 5  [anomaly, Act 3, Ward 0]
Arrives from: R26 (Hers), R19 (Bay 4), R27 (Yours)
Beat: A chart from tonight. The last obs are timed 06:02.
Links (write each target as a token):
  - {R30}  "Something is wrong - turn back"  → leads to: Bay 6
  - {R22}  "Nothing is wrong - walk on"  → leads to: Reset
Design note: Wrong (a time that hasn't happened). Correct: turn back -> Bay 6.

### R05 — Eyes front  [story, Act 3, Ward 0]
Arrives from: R02 (The crossing)
Beat: You walk. The voice behind you says your name like Ros used to. You don't turn. Gain 1 Fear.
Links (write each target as a token):
  - {R06}  "Continue"  → leads to: WARD 0 - CLOSED
Effects (state them in the text, using in-world names): Fear +1

### R12 — Snip  [story, Act 3, Ward 0]
Arrives from: R10 (Claimed back)
Beat: 'Hold still.' Cross off one field of your wristband. Lose 1 Vigour.
Links (write each target as a token):
  - {R13}  "Continue"  → leads to: Bay 2
Effects (state them in the text, using in-world names): Vigour -1; Wristband -1
Design note: Scissors moment 2 of 2.

### E_ONLYCHILD — ENDING: Only Child  [ending, Act 3, Ending]
Arrives from: R37 (Alone)
Beat: You walk out alone at 06:00. Mum survives. On the Old Wing, Ros's phone keeps ringing.

### SECRET — CODA: Ward 9  [ending, Act 3, Ending]
Arrives from: E_TRUE (ENDING: Visiting Hours)
Beat: A last page after 200. 14 March 1991, 01:47 and after. Mum, thirty-six, awake at 3 a.m. on the ward with you. Nobody is on their round. The last page is her looking at you.
Design note: SECRET CODA. FIXED NUMBER 147. Reached only from 200 by the hidden number (FIRST_BAND: B19 or M03).

### R22 — Reset  [test, Act 3, Ward 0]
Arrives from: R23 (Bay 3, again), R28 (Bay 5, again), R19 (Bay 4), R18 (Bay 3), R24 (Bay 4, again), R20 (Bay 5)
Beat: The ward resets: Bay 3 again, and the round a bay nearer. Gain 2 Fear. Test your Fortune.
Links (write each target as a token):
  - {R18}  "Lucky: the ward you know"  [condition: test passed]  → leads to: Bay 3
  - {R23}  "Unlucky: a ward you don't"  [condition: test failed]  → leads to: Bay 3, again
Effects (state them in the text, using in-world names): Fear +2
Test: Fortune

### R07 — The reckoning  [story, Act 3, Ward 0]
Arrives from: R04 (Handover, 1979)
Beat: One page, read once. The Sister reads your notes back to you: every cup of tea, every name, every field. Then she checks her upside-down watch against your ROUNDS.
Links (write each target as a token):
  - {R08}  "If you have not ticked the 05:00 box"  [condition: Rounds ≤ 4]  → leads to: Lucid
  - {R09}  "If you have ticked the 05:00 box"  [condition: Rounds ≥ 5]  → leads to: The 05:00 round
Design note: ROUNDS reckoning. 6 never reaches here (Admitted at the hub).

### R02 — The crossing  [choice, Act 3, Ward 0]
Arrives from: R01 (Down)
Beat: The low point on every route. A corridor lined with the Kept from every decade, doing their obs in unison; porters' trolleys; the lights going to night setting. Behind you, Ros's voice: 'Bean, wait for me.' Ros stopped calling you Bean years ago.
Links (write each target as a token):
  - {R03}  "If your wristband has 3 or more fields filled"  [condition: Wristband ≥ 3]  → leads to: The porters
  - {R05}  "Otherwise: keep walking, eyes front, the badge on your chest"  [condition: Wristband ≤ 2]  → leads to: Eyes front
  - {R06}  "Otherwise, if Ros is with you and you have HELD: walk with her hand in yours"  [condition: Wristband ≤ 2 and lacks WARDED and has HELD]  → leads to: WARD 0 - CLOSED
  - {R40}  "Otherwise, if you have the TICKET: hold up Saturday's ticket as you walk"  [condition: Wristband ≤ 2 and has TICKET]  → leads to: Saturday's draw
  - {D09}  "Otherwise: stop and wait for the voice behind you"  [condition: Wristband ≤ 2]  → leads to: Wait for me
Design note: WRISTBAND mid-value bite (3+). D09: the tell (A02) plus Rule 7.

### R34 — Next of kin  [story, Act 3, Ward 0]
Arrives from: R33 (The consent form)
Beat: 'Then who decides, love?' she asks, and waits.
Links (write each target as a token):
  - {R35}  "If Ros is with you and you have MENDED"  [condition: lacks WARDED and has MENDED]  → leads to: Let them go
  - {R36}  "If Ros is with you and you do not have MENDED"  [condition: lacks WARDED and lacks MENDED]  → leads to: Who decides
  - {R37}  "If Ros is on the Old Wing (WARDED)"  [condition: has WARDED]  → leads to: Alone

### R40 — Saturday's draw  [story, Act 3, Ward 0]
Arrives from: R02 (The crossing)
Beat: You hold Mum's ticket up like a pass. The Kept turn their faces away from the date on it, a day that hasn't happened, and the corridor lets you through. Lose 1 Fear.
Links (write each target as a token):
  - {R06}  "Continue"  → leads to: WARD 0 - CLOSED
Effects (state them in the text, using in-world names): Fear -1
Design note: TICKET use 2 (clued at H16).

### E_NIGHTSTAFF — ENDING: Night Staff  [ending, Act 3, Ending]
Arrives from: R32 (Visitors only), R31 (A patient can't visit a patient)
Beat: Someone has to stay. You always were the one who stayed. The tabard fits.

### R16 — The charts  [choice, Act 3, Ward 0]
Arrives from: R14 (Ros in Bay 2), R41 (The rest), R15 (Found), R13 (Bay 2)
Beat: The obs chart walk. At the foot of each bay, a chart. If nothing is wrong, walk on; if something is wrong, turn back. Get it right and the ward lets you reach Bay 6.
Links (write each target as a token):
  - {R17}  "If you have Mum's GLASSES: put them on first"  [condition: has GLASSES]  → leads to: Her glasses
  - {R18}  "Begin"  → leads to: Bay 3
Design note: Anomaly-loop finale. Checkpoint.

### R06a — Visiting  [story, Act 3, Ward 0]
Arrives from: R06 (WARD 0 - CLOSED)
Beat: On the bench by the doors, a woman in a 1986 anorak with a carrier bag of comics. You tell her Gary waited. She goes up the stairs you came down. Lose 2 Fear.
Links (write each target as a token):
  - {R04}  "Continue"  → leads to: Handover, 1979
Effects (state them in the text, using in-world names): Fear -2
Design note: Pays off PROMISE (W07).

### R27 — Yours  [story, Act 3, Ward 0]
Arrives from: R25 (Her handwriting)
Beat: She lets go of the chart, and of something else. 'Right,' she says. 'Of course.' Cross off MENDED. Lose 1 Fear.
Links (write each target as a token):
  - {R20}  "Continue"  → leads to: Bay 5
Effects (state them in the text, using in-world names): Cross off MENDED; Fear -1

### E_ADMITTED — ENDING: Admitted  [ending, Act 3, Ending]
Arrives from: R31 (A patient can't visit a patient)
Beat: Your bed is made up. The Sister tucks you in. The lights go to night setting.
Design note: Global rule: five wristband fields, the 06:00 round, or Fear at its limit (Nerve + 3).

### R01 — Down  [story, Act 3, Ward 0]
Arrives from: H01 (The Main Corridor)
Beat: The lift only goes down. Past the Basement to a floor that isn't on the panel: WARD 0, the 1979 recovery ward where Mum did her first night shift. If Ros is on the Old Wing, her phone is ringing down here now.
Links (write each target as a token):
  - {R02}  "Continue"  → leads to: The crossing
Design note: FINALE GATE (book.json): entered only with the badge, the letter and the last rule. Checkpoint.

### R35 — Let them go  [story, Act 3, Ward 0]
Arrives from: R34 (Next of kin)
Beat: The true climax. Ros reads Mum's name aloud, all of it, and you hold Mum's hand; the Sister cannot read a name spoken by someone who loves her. You both read THE LAST RULE. You let her go - back to theatre, to the one-in-three. The Sister's hold breaks; her face comes apart into all the nurses it was made of, and they go off shift.
Links (write each target as a token):
  - {R38}  "Continue"  → leads to: 06:00
Design note: Every hold breaks: she cannot keep anyone who has been let go.

### E_TRUE — ENDING: Visiting Hours  [finale, Act 3, Ending]
Arrives from: R38 (06:00)
Beat: 06:02. Mum wakes and lives: groggy, rude, alive. She says the thing she asked of each of you, out loud, to both of you. You and Ros walk out to the car park together and argue about who drives. (If you have the RING / GLASSES / TICKET: you give them back.) Last lines: THE END, then one unnumbered sentence inviting the reader, if they know the minute they were born, to turn to it (no section number printed).
Links (write each target as a token):
  - {SECRET}  "If you know the minute you were born, turn to it"  [HIDDEN puzzle link, never print the token; condition: hidden: has FIRST_BAND]  → leads to: CODA: Ward 9
Design note: TRUE ENDING. FIXED NUMBER 200. Kind 'finale': an ending with one hidden link (the coda). Ros says 'Bean' here, once. Last line has a speaker, before the invitation.
