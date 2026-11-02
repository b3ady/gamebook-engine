### M25 — The parents' room  [choice, Act 2, Maternity]
Arrives from: M18 (Ward 9, 1999)
Beat: A fold-down bed, a kettle, a sign: PARENTS MAY SLEEP HERE. Ros sits on the bed and starts to unlace her boots. 'Ten minutes. I mean it.'
Links (write each target as a token):
  - {M26}  "Take her boots off her and make her stand"  → leads to: Boots
  - {M27}  "Let her have ten minutes"  → leads to: Ten minutes
Effects (state them in the text, using in-world names): (hidden, never mention) PARENTS
Design note: WARDED route 3.

### M29 — Down without it  [story, Act 2, Maternity]
Arrives from: M01 (Level 5)
Beat: Down the stairs. The beeping behind the WARD 0 door follows you a floor and stops.
Links (write each target as a token):
  - {H02}  "Back to the Main Corridor (if you do not have RETURNED)"  [condition: lacks RETURNED]  → leads to: Back on the Main Corridor
  - {H05}  "Back to the Main Corridor (if you have RETURNED but not OFFERED)"  [condition: has RETURNED and lacks OFFERED]  → leads to: An offer
  - {H01}  "Back to the Main Corridor (if you have RETURNED and OFFERED)"  [condition: has RETURNED and has OFFERED]  → leads to: The Main Corridor
Design note: Clock exit without the item.

### M22 — This week  [story, Act 2, Maternity]
Arrives from: M21 (Ros in the chair)
Beat: MENDED route 3 of 3 (Ward 9). If neither request is yet told, THE telling (see W21). Otherwise pointer. Lose 2 Fear. Codeword MENDED.
Links (write each target as a token):
  - {M20}  "Reach under the mattress (if you do not have THE LAST RULE)"  [condition: lacks THE LAST RULE]  → leads to: Under the mattress
  - {M01}  "Get up"  → leads to: Level 5
Effects (state them in the text, using in-world names): Note MENDED; (hidden, never mention) SENT; (hidden, never mention) ASKED; Fear -2

### M13 — Caught on the round  [story, Act 2, Maternity]
Arrives from: M11 (The keys)
Beat: The keys jangle and she is there, red torch, smiling. 'Can't sleep?' She checks your wristband and fills in BED. Fill in one more field of your wristband.
Links (write each target as a token):
  - {M01}  "Continue"  → leads to: Level 5
Effects (state them in the text, using in-world names): Wristband +1

### M23 — The round on Ward 9  [choice, Act 2, Maternity]
Arrives from: M18 (Ward 9, 1999)
Beat: The Kept children asleep in rows; at the far end, the red torch, coming bed by bed. One room behind is now this room.
Links (write each target as a token):
  - {M24}  "Hide behind the curtains"  → leads to: Curtains
  - {M18}  "If you are wearing the TABARD: fall in beside her and do the round"  [condition: has TABARD]  → leads to: Ward 9, 1999

### M11 — The keys  [test, Act 2, Maternity]
Arrives from: M10 (The drug cupboard)
Beat: Too many keys and footsteps that never hurry. Test your Fortune.
Links (write each target as a token):
  - {M12}  "Lucky"  [condition: test passed]  → leads to: Rule 8
  - {M13}  "Unlucky"  [condition: test failed]  → leads to: Caught on the round
Test: Fortune

### M10 — The drug cupboard  [choice, Act 2, Maternity]
Arrives from: M09 (Tomorrow)
Beat: Locked. The Sister's keys hang on a hook by the station, a big ring of them.
Links (write each target as a token):
  - {M11}  "Take the keys and try them"  → leads to: The keys
  - {M01}  "Leave it"  → leads to: Level 5

### M24 — Curtains  [story, Act 2, Maternity]
Arrives from: M23 (The round on Ward 9)
Beat: Her shadow on the curtain, the torch through it, red. She stops, and counts, and moves on. Gain 1 Fear.
Links (write each target as a token):
  - {M18}  "Continue"  → leads to: Ward 9, 1999
Effects (state them in the text, using in-world names): Fear +1

### M28 — Down  [story, Act 2, Maternity]
Arrives from: M01 (Level 5)
Beat: Down the stairs with the strip of card in your pocket. Behind you, on Ward 9, the round, a room behind you all the way down. Gain 1 Fear.
Links (write each target as a token):
  - {H02}  "Back to the Main Corridor (if you do not have RETURNED)"  [condition: lacks RETURNED]  → leads to: Back on the Main Corridor
  - {H05}  "Back to the Main Corridor (if you have RETURNED but not OFFERED)"  [condition: has RETURNED and lacks OFFERED]  → leads to: An offer
  - {H01}  "Back to the Main Corridor (if you have RETURNED and OFFERED)"  [condition: has RETURNED and has OFFERED]  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Fear +1
Design note: Clock exit (item held).

### M12 — Rule 8  [item, Act 2, Maternity]
Arrives from: M11 (The keys)
Beat: Behind the controlled drugs, a strip of laminated card: 8. LET THEM GO. On the back, in biro, a filthy little doodle and M., 1979. Note THE LAST RULE.
Links (write each target as a token):
  - {M01}  "Continue"  → leads to: Level 5
Effects (state them in the text, using in-world names): Note THE LAST RULE
Design note: LAST_RULE route 1 of 3 (puzzle/test).

### M18 — Ward 9, 1999  [choice, Act 2, Maternity]
Arrives from: M23 (The round on Ward 9), M24 (Curtains), M27 (Ten minutes), M01 (Level 5), M26 (Boots)
Beat: The children's ward as it was when you were eight: the bed by the window, the hard chair beside it where Mum slept for a week.
Links (write each target as a token):
  - {M19}  "Sit in the chair"  → leads to: The chair
  - {D07}  "Lie down in your old bed"  → leads to: Tucked in
  - {M23}  "Walk the ward"  → leads to: The round on Ward 9
  - {M25}  "If Ros is with you: the parents' room"  [condition: lacks WARDED and lacks PARENTS]  → leads to: The parents' room
Effects (state them in the text, using in-world names): (hidden, never mention) WARD9
Design note: Relationship beat zone. D07 temptation: your own bed.

### M21 — Ros in the chair  [story, Act 2, Maternity]
Arrives from: M19 (The chair)
Beat: Ros's side of 1999: she was twelve and at home with Dad, making the tea and telling everyone it was fine. She has never sat in this chair. She sits.
Links (write each target as a token):
  - {M22}  "If you have SPOKE but not MENDED: tell her what this week was like for you"  [condition: has SPOKE and lacks MENDED]  → leads to: This week
  - {M20}  "Reach under the mattress (if you do not have THE LAST RULE)"  [condition: lacks THE LAST RULE]  → leads to: Under the mattress
  - {M01}  "Get up"  → leads to: Level 5

### M15 — Theatre staff  [combat, Act 2, Maternity]
Arrives from: M14 (The delivery suite), M16 (Slip past)
Beat: THEATRE STAFF  NERVE 8  VIGOUR 9.
Links (write each target as a token):
  - {M17}  "If you win"  [condition: fight won]  → leads to: Pinned
  - {D_VIGOUR}  "If your Vigour reaches 0"  [condition: fight lost]  → leads to: Spent
Foe line: THEATRE STAFF  NERVE 8  VIG 9
Design note: Checkpoint before this fight: M01.

### M09 — Tomorrow  [story, Act 2, Maternity]
Arrives from: M08 (The phone)
Beat: Set piece. Mum's voice, groggy, rude, alive: 'Bean? It's tomorrow here. Don't ask.' She says your name and a field on your wristband goes blank. If you do not know it yet, she asks whether Ros ever told you she sent her (SENT: told once here, pointer elsewhere). 'The bit I tore off is in the drug cupboard, love.' Cross off one field of your wristband.
Links (write each target as a token):
  - {M10}  "Continue"  → leads to: The drug cupboard
Effects (state them in the text, using in-world names): (hidden, never mention) SENT; Wristband -1
Design note: Someone who loves you says the true thing: a field comes off. The proof that it is really Mum is the field coming off, not the word: the Sister can say 'Bean' (she does, in Ros's voice, at R02), but nothing she says frees you.

### M02 — The register  [choice, Act 2, Maternity]
Arrives from: M01 (Level 5)
Beat: The 1991 delivery register on a desk, open, a pen in the gutter.
Links (write each target as a token):
  - {M03}  "Turn to March 1991"  → leads to: Baby of Maureen
  - {M04}  "Turn to tonight's page"  → leads to: Tonight
Effects (state them in the text, using in-world names): (hidden, never mention) REGISTER

### M14 — The delivery suite  [choice, Act 2, Maternity]
Arrives from: M01 (Level 5)
Beat: Theatre staff in paper masks round an empty delivery bed, waiting. Behind the masks, nothing. One has a strip of card pinned to its gown.
Links (write each target as a token):
  - {M15}  "Fight them for it"  → leads to: Theatre staff
  - {M16}  "Slip past and take it"  → leads to: Slip past
  - {M01}  "Back out"  → leads to: Level 5
Effects (state them in the text, using in-world names): (hidden, never mention) DELIVERY

### D08 — Closed  [death, Act 2, Maternity]
Arrives from: M01 (Level 5)
Beat: Behind the door, Mum's monitor, and stairs going down to it. You take them two at a time. The door shuts behind you, and the stairs keep going, and so does the beeping, never nearer.
Effects (state them in the text, using in-world names): (hidden, never mention) TRIED_DOOR; Wristband +1
Death — the warning the reader was given: Notice rule 5: Ward 0 is closed (it can be opened only with the badge, the letter and the last rule, from the Main Corridor).  End: 'Fill in 1 more field on your wristband. Return to {M01} and choose again.'

### M27 — Ten minutes  [story, Act 2, Maternity]
Arrives from: M25 (The parents' room)
Beat: You make two teas. When you turn round the bed is folded away and the room smells of 1952 blanket. Her phone is ringing on the Old Wing. Codeword WARDED.
Links (write each target as a token):
  - {M18}  "Continue"  → leads to: Ward 9, 1999
Effects (state them in the text, using in-world names): Note WARDED
Design note: WARDED route 3.

### M19 — The chair  [choice, Act 2, Maternity]
Arrives from: M18 (Ward 9, 1999)
Beat: From the chair you can see what she saw for a week: the bed, the window, and something folded under the mattress edge.
Links (write each target as a token):
  - {M20}  "Reach under the mattress (if you do not have THE LAST RULE)"  [condition: lacks THE LAST RULE]  → leads to: Under the mattress
  - {M21}  "If Ros is with you: give her the chair"  [condition: lacks WARDED]  → leads to: Ros in the chair
  - {M01}  "Get up"  → leads to: Level 5

### M17 — Pinned  [item, Act 2, Maternity]
Arrives from: M15 (Theatre staff), M16 (Slip past)
Beat: The strip of card: 8. LET THEM GO. Note THE LAST RULE.
Links (write each target as a token):
  - {M01}  "Continue"  → leads to: Level 5
Effects (state them in the text, using in-world names): Note THE LAST RULE
Design note: LAST_RULE route 2 of 3 (combat/nerve).

### M04 — Tonight  [story, Act 2, Maternity]
Arrives from: M02 (The register)
Beat: Under ADMISSIONS, tonight's date and your name, in pencil, waiting for ink. You rub it out with your thumb until the paper goes thin. Gain 1 Fear.
Links (write each target as a token):
  - {M01}  "Continue"  → leads to: Level 5
Effects (state them in the text, using in-world names): Fear +1

### M08 — The phone  [choice, Act 2, Maternity]
Arrives from: M01 (Level 5)
Beat: The nurses' station phone, cream plastic, ringing and ringing.
Links (write each target as a token):
  - {M09}  "Answer it"  → leads to: Tomorrow
  - {M01}  "Let it ring"  → leads to: Level 5
Effects (state them in the text, using in-world names): (hidden, never mention) PHONE_M

### M01 — Level 5  [choice, Act 2, Maternity]
Arrives from: M22 (This week), M13 (Caught on the round), HS (Five flights), M10 (The drug cupboard), M12 (Rule 8), M21 (Ros in the chair), M14 (The delivery suite), M19 (The chair), M17 (Pinned), HL (The lift up), M04 (Tonight), M08 (The phone), M03 (Baby of Maureen), M20 (Under the mattress)
Beat: Return line first. Maternity on the left, Ward 9 (children's) on the right, the nurses' station between. The stairwell door here says WARD 0 - CLOSED, and behind it a monitor is beeping in Mum's rhythm.
Links (write each target as a token):
  - {M02}  "The delivery register"  [condition: lacks REGISTER]  → leads to: The register
  - {M08}  "The nurses' station, where a phone is ringing"  [condition: lacks PHONE_M]  → leads to: The phone
  - {M14}  "The delivery suite"  [condition: lacks DELIVERY]  → leads to: The delivery suite
  - {M18}  "Ward 9"  [condition: lacks WARD9]  → leads to: Ward 9, 1999
  - {D08}  "Open the door marked WARD 0"  [condition: lacks TRIED_DOOR]  → leads to: Closed
  - {M28}  "Back down to the Main Corridor (if you have THE LAST RULE)"  [condition: has THE LAST RULE]  → leads to: Down
  - {M29}  "Back down without it (if you do not have THE LAST RULE)"  [condition: lacks THE LAST RULE]  → leads to: Down without it
Design note: Zone junction and checkpoint. Delivery and Ward 9 always yield THE LAST RULE (or a fight), so no softlock.

### M26 — Boots  [story, Act 2, Maternity]
Arrives from: M25 (The parents' room)
Beat: 'You are unbelievable,' she says, and laces them again, and stands, and leans on you for one second. Codeword HELD.
Links (write each target as a token):
  - {M18}  "Continue"  → leads to: Ward 9, 1999
Effects (state them in the text, using in-world names): Note HELD
Design note: HELD route 3.

### M03 — Baby of Maureen  [story, Act 2, Maternity]
Arrives from: M02 (The register)
Beat: Analog document. 14.3.91, 01:47. Mother: Maureen, 36. Baby: 7lb 2oz. Taped beside it, the first wristband you ever wore: BABY OF MAUREEN, 01:47. Lose 1 Fear.
Links (write each target as a token):
  - {M01}  "Continue"  → leads to: Level 5
Effects (state them in the text, using in-world names): (hidden, never mention) FIRST_BAND; Fear -1
Design note: FIRST_BAND route 2 of 2. Secret ending number: 01:47 -> 147.

### D07 — Tucked in  [death, Act 2, Maternity]
Arrives from: M18 (Ward 9, 1999)
Beat: It fits you. It shouldn't. Someone tucks the blanket under the mattress the way Mum did, tight, and says goodnight, and isn't Mum.
Effects (state them in the text, using in-world names): Wristband +1
Death — the warning the reader was given: Notice rule 3: never lie down on a ward bed.  End: 'Fill in 1 more field on your wristband. Return to {M01} and choose again.'

### M16 — Slip past  [test, Act 2, Maternity]
Arrives from: M14 (The delivery suite)
Beat: Test your Nerve.
Links (write each target as a token):
  - {M17}  "Success"  [condition: test passed]  → leads to: Pinned
  - {M15}  "Failure: they turn"  [condition: test failed]  → leads to: Theatre staff
Test: Nerve

### M20 — Under the mattress  [item, Act 2, Maternity]
Arrives from: M22 (This week), M21 (Ros in the chair), M19 (The chair)
Beat: A strip of laminated card, folded small: 8. LET THEM GO. Mum put it there in 1999. Note THE LAST RULE.
Links (write each target as a token):
  - {M01}  "Continue"  → leads to: Level 5
Effects (state them in the text, using in-world names): Note THE LAST RULE
Design note: LAST_RULE route 3 of 3 (moral: sitting where she sat).
