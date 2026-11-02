### H04 — Deleted  [story, Act 2, Main Corridor]
Arrives from: H03 (Things to say)
Beat: 'I wrote it at Departures. Every line started with sorry and none of them were true enough.' Codeword SPOKE.
Links (write each target as a token):
  - {H01}  "Continue"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Note SPOKE
Design note: SPOKE route 3 of 4. Ros still does not call you Bean (the D09 tell holds until E_TRUE).

### H17 — Next of kin  [story, Act 2, Main Corridor]
Arrives from: H13 (The payphone)
Beat: 'Lovely.' Pen on paper down the line. On your wrist, NEXT OF KIN fills in by itself, in your own handwriting. Fill in one more field of your wristband.
Links (write each target as a token):
  - {H01}  "Continue"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Wristband +1

### HLD — Down only  [story, Act 2, Main Corridor]
Arrives from: HL (The lift up)
Beat: The lift goes down. Basement, sub-basement, a floor with no number; the doors open on the Main Corridor's own echo, and you climb back up the stairs. Gain 1 Fear.
Links (write each target as a token):
  - {H02}  "Climb back to the Main Corridor (if you do not have RETURNED)"  [condition: lacks RETURNED]  → leads to: Back on the Main Corridor
  - {H05}  "Climb back to the Main Corridor (if you have RETURNED but not OFFERED)"  [condition: has RETURNED and lacks OFFERED]  → leads to: An offer
  - {H01}  "Climb back to the Main Corridor (if you have RETURNED and OFFERED)"  [condition: has RETURNED and has OFFERED]  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Fear +1
Design note: Clock exit: costs a ROUNDS tick for using the lift after 03:00.

### H07 — An hour  [story, Act 2, Main Corridor]
Arrives from: H05 (An offer)
Beat: Ros lets herself be led, still talking about flight times. The swing doors to the Old Wing close behind them. Her phone, in her coat, begins to ring and doesn't stop. Codeword WARDED.
Links (write each target as a token):
  - {H01}  "Continue"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Note WARDED
Design note: WARDED route 1. Rescue: W28/W31, B21/B22, R14/R15.

### HS — Five flights  [story, Act 2, Main Corridor]
Arrives from: H01 (The Main Corridor)
Beat: The stairwell smells of cigarettes from 1979. Lose 1 Vigour.
Links (write each target as a token):
  - {M01}  "Continue"  → leads to: Level 5
Effects (state them in the text, using in-world names): Vigour -1

### H05 — An offer  [choice, Act 2, Main Corridor]
Arrives from: M29 (Down without it), W30 (Retreat), B30 (The stairs), HLD (Down only), W29 (One room behind), M28 (Down), B29 (The lift)
Beat: The second return. The Night Sister is waiting at the tea bar with a folded blanket. 'Your sister's dead on her feet, love. There's a bed for her on the Old Wing. And one for you. I'll ring through the minute there's news from theatre.' Codeword OFFERED.
Links (write each target as a token):
  - {H07}  "Let Ros take the bed for an hour (if Ros is with you)"  [condition: lacks WARDED]  → leads to: An hour
  - {H10}  "Take the blanket and the chair yourself"  → leads to: Blanket
  - {H06}  "Thank her, and refuse"  → leads to: Refused
Effects (state them in the text, using in-world names): Note OFFERED
Design note: The midpoint offer (fires once). WARDED route 1 of 3 (H07, W03, M27).

### H16 — Saturday  [story, Act 2, Main Corridor]
Arrives from: H08 (The tea bar)
Beat: She checks Mum's numbers against a 1979 newspaper and shakes her head: 'Not yet, duck. It's Saturday's.' She looks at the date as if it hurts her eyes. Nobody here has a Saturday. Lose 1 Fear.
Links (write each target as a token):
  - {H01}  "Continue"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Fear -1
Design note: TICKET use 1; clue for R40 (the Kept cannot look at a date that hasn't happened).

### H11 — Tea  [story, Act 2, Main Corridor]
Arrives from: H08 (The tea bar)
Beat: Strong, sweet, exactly how Mum makes it. She writes your date of birth on a paper cup without asking it. Gain 3 Vigour. Fill in one more field of your wristband.
Links (write each target as a token):
  - {H01}  "Continue"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Fear -2; Wristband +1

### H01 — The Main Corridor  [choice, Act 2, Main Corridor]
Arrives from: H04 (Deleted), M29 (Down without it), H17 (Next of kin), W30 (Retreat), B30 (The stairs), HLD (Down only), H07 (An hour), W29 (One room behind), M28 (Down), H16 (Saturday), H11 (Tea), H15 (Larkvale), H14 (First aid), H13 (The payphone), H03 (Things to say), B29 (The lift), A36 (The Main Corridor), H12 (Since the war), H06 (Refused), H10 (Blanket), H02 (Back on the Main Corridor), H18 (Rosalind)
Beat: Return line first (the corridor is longer every time; the Sister's round is closer every time; the clock jumps to the box you have ticked). First visit: the floor lines, the tea bar, the chapel door, Lost Property, the payphone, three ways to go and one door you can't.
Links (write each target as a token):
  - {W01}  "The Old Wing (if you do not have the VISITOR'S BADGE)"  [condition: lacks VISITOR'S BADGE]  → leads to: The Old Wing
  - {B01}  "The Basement, by the lift (it only goes down) (if you do not have MUM'S LETTER)"  [condition: lacks MUM'S LETTER]  → leads to: The Basement
  - {HL}  "Maternity and Ward 9, by the lift (if you do not have THE LAST RULE)"  [condition: lacks THE LAST RULE]  → leads to: The lift up
  - {HS}  "Maternity and Ward 9, by the stairs (if you do not have THE LAST RULE)"  [condition: lacks THE LAST RULE]  → leads to: Five flights
  - {W28}  "Follow the sound of Ros's phone into the Old Wing (if you have WARDED and the VISITOR'S BADGE)"  [condition: has WARDED and has VISITOR'S BADGE]  → leads to: Ros's bed
  - {H08}  "The WRVS tea bar"  [condition: lacks TEABAR]  → leads to: The tea bar
  - {H09}  "Lost Property"  [condition: lacks LP_USED]  → leads to: Lost Property
  - {H13}  "The payphone that is ringing"  [condition: lacks PHONED]  → leads to: The payphone
  - {R01}  "Ward 0 (only if you hold the VISITOR'S BADGE, MUM'S LETTER and THE LAST RULE)"  [condition: has VISITOR'S BADGE and has MUM'S LETTER and has THE LAST RULE]  → leads to: Down
Design note: The one hub. Zones gated shut once their item is held. Ward 0 gated behind all three (finale gate). Global rule: ticking 06:00 here -> Admitted.

### H15 — Larkvale  [item, Act 2, Main Corridor]
Arrives from: H09 (Lost Property)
Beat: A LARKVALE AIRWAYS luggage tag, LV 137, its passenger name scratched out. Somebody else got out of somewhere. It makes you feel better than it should. Lose 2 Fear. Note the LUGGAGE TAG.
Links (write each target as a token):
  - {H01}  "Continue"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Note LUGGAGE TAG; Fear -2
Design note: The Layover cameo. Flavour only.

### H14 — First aid  [item, Act 2, Main Corridor]
Arrives from: H09 (Lost Property)
Beat: A tin first-aid kit, St John's Ambulance. Restore 6 Vigour once, at any time. Note the FIRST-AID KIT.
Links (write each target as a token):
  - {H01}  "Continue"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Note FIRST-AID KIT

### H13 — The payphone  [choice, Act 2, Main Corridor]
Arrives from: H01 (The Main Corridor)
Beat: It's theatre, a woman's voice, clipped: 'Still in surgery. We need a next of kin for the paperwork. Is that you?'
Links (write each target as a token):
  - {H17}  "'Yes. Me.'"  → leads to: Next of kin
  - {H18}  "'My sister. Rosalind.'"  → leads to: Rosalind
  - {H01}  "Hang up"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): (hidden, never mention) PHONED
Design note: The phone hub scene. The voice is the Sister's.

### HL — The lift up  [story, Act 2, Main Corridor]
Arrives from: H01 (The Main Corridor)
Beat: You press 5 for Maternity.
Links (write each target as a token):
  - {M01}  "If you have not ticked the 03:00 box"  [condition: Rounds ≤ 2]  → leads to: Level 5
  - {HLD}  "If you have ticked the 03:00 box"  [condition: Rounds ≥ 3]  → leads to: Down only
Design note: Rule 4 bites through the clock: after 03:00 the lift goes down.

### H08 — The tea bar  [choice, Act 2, Main Corridor]
Arrives from: H01 (The Main Corridor)
Beat: The WRVS shutter is half up. A volunteer in a 1970s tabard butters toast that never runs out. 'Tea, duck?'
Links (write each target as a token):
  - {H11}  "Have a cup"  → leads to: Tea
  - {H12}  "Ask her how long she's been here"  → leads to: Since the war
  - {H16}  "If you have the TICKET: ask her to check Mum's numbers"  [condition: has TICKET]  → leads to: Saturday
Effects (state them in the text, using in-world names): (hidden, never mention) TEABAR

### H09 — Lost Property  [choice, Act 2, Main Corridor]
Arrives from: H01 (The Main Corridor)
Beat: A hatch, a bell, shelves of things from every decade. A sign: ONE ITEM PER VISITOR - and VISITOR has been crossed out and PATIENT written over it.
Links (write each target as a token):
  - {H14}  "Take the first-aid kit"  → leads to: First aid
  - {H15}  "Take the luggage tag"  → leads to: Larkvale
Effects (state them in the text, using in-world names): (hidden, never mention) LP_USED

### H03 — Things to say  [choice, Act 2, Main Corridor]
Arrives from: H02 (Back on the Main Corridor)
Beat: Ros checks her phone. You see a note titled THINGS TO SAY TO BEAN. It's empty. She sees you see it.
Links (write each target as a token):
  - {H04}  "Ask her what was on it (if you do not have SPOKE)"  [condition: lacks SPOKE]  → leads to: Deleted
  - {H01}  "Leave it"  → leads to: The Main Corridor
Design note: Ros's hub scene.

### H12 — Since the war  [story, Act 2, Main Corridor]
Arrives from: H08 (The tea bar)
Beat: 'Oh, forever.' She remembers Mo: 'Night auxiliary, seventy-nine. Filthy laugh. Tore something off a notice once and the Sister never forgave her.' Lose 1 Fear.
Links (write each target as a token):
  - {H01}  "Continue"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): (hidden, never mention) KNOWS_1979; Fear -1
Design note: KNOWS_1979 route 3. Foreshadows THE LAST RULE (Mum tore rule 8 off).

### H06 — Refused  [story, Act 2, Main Corridor]
Arrives from: H05 (An offer)
Beat: 'Course.' She writes it down. 'I'll be round.' Gain 1 Fear.
Links (write each target as a token):
  - {H01}  "Continue"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Fear +1

### H10 — Blanket  [story, Act 2, Main Corridor]
Arrives from: H05 (An offer)
Beat: The blanket is warm from somewhere. You sleep for no time at all. When you wake, your wristband says WARD in her neat capitals. Gain 4 Vigour. Fill in one more field of your wristband.
Links (write each target as a token):
  - {H01}  "Continue"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Vigour +2; Fear -3; Wristband +1

### H02 — Back on the Main Corridor  [story, Act 2, Main Corridor]
Arrives from: M29 (Down without it), W30 (Retreat), B30 (The stairs), HLD (Down only), W29 (One room behind), M28 (Down), B29 (The lift)
Beat: The first return. The corridor has changed: the yellow line now runs to a door marked WARD 0. On the clock, the time of the box you've just ticked. Codeword RETURNED.
Links (write each target as a token):
  - {H03}  "If Ros is with you"  [condition: lacks WARDED]  → leads to: Things to say
  - {H01}  "If Ros is on the Old Wing (WARDED)"  [condition: has WARDED]  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Note RETURNED
Design note: First-return scene (fires once). Clock hub.

### H18 — Rosalind  [story, Act 2, Main Corridor]
Arrives from: H13 (The payphone)
Beat: A pause, as if she can't quite read what you said. 'I'll make a note.' The line goes dead. Gain 1 Fear.
Links (write each target as a token):
  - {H01}  "Continue"  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Fear +1
Design note: She cannot read a name spoken by someone who loves you (first hint).
