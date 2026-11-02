### B14 — Signed for  [item, Act 2, Basement]
Arrives from: B13 (Sign for it)
Beat: Her ring, wedding band worn thin. It is warm, as if just off her finger. Fill in one more field of your wristband. Note the RING.
Links (write each target as a token):
  - {B01}  "Continue"  → leads to: The Basement
Effects (state them in the text, using in-world names): Note RING; Wristband +1

### B16 — The tray  [item, Act 2, Basement]
Arrives from: B15 (Through the wire)
Beat: THEATRE 3: a watch, a hearing aid, and Mum's ring, warm. Note the RING.
Links (write each target as a token):
  - {B01}  "Continue"  → leads to: The Basement
Effects (state them in the text, using in-world names): Note RING

### B19 — 1991  [story, Act 2, Basement]
Arrives from: B18 (The mortuary)
Beat: Set piece. The fridge opens on a 1991 incubator, warm, empty, a tiny wristband taped inside: BABY OF MAUREEN. 14.3.91. 01:47. Gain 2 Fear.
Links (write each target as a token):
  - {B01}  "Continue"  → leads to: The Basement
Effects (state them in the text, using in-world names): (hidden, never mention) FIRST_BAND; Fear +2
Design note: FIRST_BAND route 1 of 2 (M03). The time 01:47 is the secret-ending number (147).

### B01 — The Basement  [choice, Act 2, Basement]
Arrives from: B14 (Signed for), B16 (The tray), B19 (1991), B20 (Not here), B23 (The tabard), B15 (Through the wire), B24 (The porters' lodge), H01 (The Main Corridor), B10 (Why), B18 (The mortuary), B21 (The in-tray), B08 (The LPA), B11 (Linen services), B09 (Asked), LOCKER (Locker 179), B22 (Torn)
Beat: Return line first. Pipes, porters' corridors, signs in 1960s Helvetica: MEDICAL RECORDS, PROPERTY, MORTUARY, PORTERS. The lift only goes one way.
Links (write each target as a token):
  - {B02}  "Medical Records"  [condition: lacks RECORDS]  → leads to: Medical Records
  - {B12}  "Property"  [condition: lacks PROPERTY]  → leads to: Property
  - {B17}  "The corridor to the mortuary"  [condition: lacks MORTUARY]  → leads to: Night setting
  - {B24}  "The porters' lodge"  [condition: lacks LODGE]  → leads to: The porters' lodge
  - {B11}  "Linen services"  [condition: lacks LINEN]  → leads to: Linen services
  - {B26}  "Go back up"  → leads to: The way up
Design note: Zone junction and checkpoint. Records always yields the letter (or a fight), so no softlock.

### B13 — Sign for it  [choice, Act 2, Basement]
Arrives from: B12 (Property)
Beat: 'Just sign here, love.' He turns the ledger round.
Links (write each target as a token):
  - {B14}  "Sign"  → leads to: Signed for
  - {B15}  "Refuse and try the tray through the wire"  → leads to: Through the wire

### B30 — The stairs  [story, Act 2, Basement]
Arrives from: B26 (The way up)
Beat: Eleven flights to Level 1, the trolley's wheels a landing below the whole way. Lose 1 Vigour.
Links (write each target as a token):
  - {H02}  "Back to the Main Corridor (if you do not have RETURNED)"  [condition: lacks RETURNED]  → leads to: Back on the Main Corridor
  - {H05}  "Back to the Main Corridor (if you have RETURNED but not OFFERED)"  [condition: has RETURNED and lacks OFFERED]  → leads to: An offer
  - {H01}  "Back to the Main Corridor (if you have RETURNED and OFFERED)"  [condition: has RETURNED and has OFFERED]  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Vigour -1
Design note: Clock exit.

### B20 — Not here  [story, Act 2, Basement]
Arrives from: B18 (The mortuary)
Beat: 'Date of birth?' it asks, kindly, and you hear yourself give yours. Fill in one more field of your wristband.
Links (write each target as a token):
  - {B01}  "Continue"  → leads to: The Basement
Effects (state them in the text, using in-world names): Wristband +1
Design note: Rule 2 adjacent: answering the hospital costs a field.

### B17 — Night setting  [choice, Act 2, Basement]
Arrives from: B01 (The Basement)
Beat: The mortuary corridor. The lights go to night setting and behind you a trolley starts to roll.
Links (write each target as a token):
  - {B18}  "Keep walking"  → leads to: The mortuary
  - {D06}  "Stop and let it pass"  → leads to: Collected
Effects (state them in the text, using in-world names): (hidden, never mention) MORTUARY
Design note: Rule 7, with the empty trolley (A19 taught its cost).

### B23 — The tabard  [item, Act 2, Basement]
Arrives from: B11 (Linen services)
Beat: It fits you. It smells of Mum's washing powder from 1979, which is impossible. Gain 1 Fear. Note the TABARD.
Links (write each target as a token):
  - {B01}  "Continue"  → leads to: The Basement
Effects (state them in the text, using in-world names): Note TABARD; Fear +1
Design note: TABARD route 2 of 2 (W25).

### B03 — The slip  [story, Act 2, Basement]
Arrives from: B02 (Medical Records)
Beat: You sign. The clerk fetches it at once. Your signature stays on the slip, and the slip stays on the spike. Fill in one more field of your wristband.
Links (write each target as a token):
  - {B07}  "Continue"  → leads to: Mum's file
Effects (state them in the text, using in-world names): Wristband +1
Design note: Rule 6 broken: a field, not a death (punished gradually).

### B15 — Through the wire  [test, Act 2, Basement]
Arrives from: B13 (Sign for it), B12 (Property)
Beat: Test your Nerve.
Links (write each target as a token):
  - {B16}  "Success"  [condition: test passed]  → leads to: The tray
  - {B01}  "Failure: the wire bites; lose 2 Vigour"  [condition: test failed]  → leads to: The Basement
Test: Nerve

### B24 — The porters' lodge  [story, Act 2, Basement]
Arrives from: B01 (The Basement)
Beat: Analog document: the collections board. Tonight: OLD WING x1 (R.); WARD 0 x1 (M., BAY 6); WARD 0 x1 (VISITOR) - and a space where your name will go.
Links (write each target as a token):
  - {B01}  "Continue"  → leads to: The Basement
Effects (state them in the text, using in-world names): (hidden, never mention) LODGE; Fear +1
Design note: Lore: Ward 0 has Mum in Bay 6 and is expecting you. R. is Ros if WARDED (prose conditional).

### B06 — Terminal digit  [story, Act 2, Basement]
Arrives from: B02 (Medical Records)
Beat: 'Terminal-digit filing. God, I love it.' Ros finds it in four minutes, and is proud, and you let her be.
Links (write each target as a token):
  - {B07}  "Continue"  → leads to: Mum's file

### B12 — Property  [choice, Act 2, Basement]
Arrives from: B01 (The Basement)
Beat: A wire cage. A clerk with a ledger: 'Patients' property, staff lockers. Lockers go by the year you first came to St Bede's.' Behind him, rows of numbered lockers. If you know the year, take away 1800 and turn to that section.
Links (write each target as a token):
  - {LOCKER}  "Turn to the locker (1979 - 1800 = 179)"  [HIDDEN puzzle link, never print the token; condition: hidden: has KNOWS_1979]  → leads to: Locker 179
  - {B13}  "Ask for Maureen's ring"  → leads to: Sign for it
  - {B15}  "Reach through the wire for the tray marked THEATRE 3"  → leads to: Through the wire
Effects (state them in the text, using in-world names): (hidden, never mention) PROPERTY
Design note: Number puzzle: LOCKER is fixed at 179.

### B04 — The stacks  [test, Act 2, Basement]
Arrives from: B02 (Medical Records)
Beat: Miles of brown folders. Test your Fortune.
Links (write each target as a token):
  - {B07}  "Lucky"  [condition: test passed]  → leads to: Mum's file
  - {B05}  "Unlucky"  [condition: test failed]  → leads to: The porter
Test: Fortune

### B26 — The way up  [choice, Act 2, Basement]
Arrives from: B01 (The Basement)
Beat: The trolley is in the corridor behind you, a room back, waiting. The lift, or the stairs.
Links (write each target as a token):
  - {B29}  "Take the lift up"  → leads to: The lift
  - {B30}  "Take the stairs"  → leads to: The stairs
Design note: One-room-behind beat. Rule 4: after 03:00 the lift goes down only.

### B10 — Why  [story, Act 2, Basement]
Arrives from: B08 (The LPA)
Beat: 'Because she asked me not to. Because you'd have taken it as me leaving again.' True, and not the whole truth, and you both know it. Gain 1 Fear.
Links (write each target as a token):
  - {B01}  "Continue"  → leads to: The Basement
Effects (state them in the text, using in-world names): Fear +1
Design note: The cold route: the LPA is explained, the requests are not.

### D06 — Collected  [death, Act 2, Basement]
Arrives from: B17 (Night setting)
Beat: It doesn't pass. It stops beside you, and it is exactly the right height, and in the amber dark it is easy to lie down on it, and the ceiling tiles go by.
Effects (state them in the text, using in-world names): Wristband +1
Death — the warning the reader was given: Notice rule 7: if the lights dim to night setting, keep walking (and the trolley took you at A19 when you stopped).  End: 'Fill in 1 more field on your wristband. Return to {B01} and choose again.'

### B07 — Mum's file  [item, Act 2, Basement]
Arrives from: B03 (The slip), B06 (Terminal digit), B04 (The stacks), B05 (The porter)
Beat: Her file: the 2020 stroke, your name as carer on every page. Then a Lasting Power of Attorney for health, 2023, naming Ros. Clipped to it, an envelope in Mum's writing: For Bean. The letter: 'Because you would never let me go, love, and I couldn't make you be the one.' Note MUM'S LETTER.
Links (write each target as a token):
  - {B08}  "If Ros is with you"  [condition: lacks WARDED]  → leads to: The LPA
  - {B21}  "If Ros is on the Old Wing (WARDED)"  [condition: has WARDED]  → leads to: The in-tray
Effects (state them in the text, using in-world names): Note MUM'S LETTER
Design note: Letter route 1 of 2 (LOCKER is 2). ONE TELLING of the letter's text and the LPA. Analog document.

### B18 — The mortuary  [choice, Act 2, Basement]
Arrives from: B17 (Night setting)
Beat: Fridge doors, steel, labelled. One is labelled with your date of birth. A drawer further down is saying, politely, 'Maureen?'
Links (write each target as a token):
  - {B19}  "Open the door with your birthday on it"  → leads to: 1991
  - {B20}  "Answer the drawer: 'She's not here.'"  → leads to: Not here
  - {B01}  "Go back"  → leads to: The Basement

### B21 — The in-tray  [choice, Act 2, Basement]
Arrives from: B07 (Mum's file)
Beat: In the clerk's in-tray, a new file, still warm from the typewriter: ROSALIND. ADMITTED 02:00. OLD WING.
Links (write each target as a token):
  - {B22}  "Tear it in half"  → leads to: Torn
  - {B01}  "Leave it"  → leads to: The Basement
Design note: Rescue route 2 (Basement).

### B08 — The LPA  [choice, Act 2, Basement]
Arrives from: B07 (Mum's file)
Beat: Ros has gone white. She knew. She has known for three years.
Links (write each target as a token):
  - {B09}  "If you have SPOKE: tell her what Mum asked of you six years ago"  [condition: has SPOKE and lacks MENDED]  → leads to: Asked
  - {B10}  "Ask her why she never told you"  → leads to: Why
  - {B01}  "Put the file away and say nothing"  → leads to: The Basement

### B29 — The lift  [story, Act 2, Basement]
Arrives from: B26 (The way up)
Beat: You press G.
Links (write each target as a token):
  - {D05}  "If you have ticked the 03:00 box"  [condition: Rounds ≥ 3]  → leads to: Down only
  - {H02}  "Otherwise: the doors open on the Main Corridor (if you do not have RETURNED)"  [condition: Rounds ≤ 2 and lacks RETURNED]  → leads to: Back on the Main Corridor
  - {H05}  "Otherwise: the doors open on the Main Corridor (if you have RETURNED but not OFFERED)"  [condition: Rounds ≤ 2 and has RETURNED and lacks OFFERED]  → leads to: An offer
  - {H01}  "Otherwise: the doors open on the Main Corridor (if you have RETURNED and OFFERED)"  [condition: Rounds ≤ 2 and has RETURNED and has OFFERED]  → leads to: The Main Corridor
Design note: Clock exit. The death is fair: the Notice gave the rule, the sheet gives the time.

### B02 — Medical Records  [choice, Act 2, Basement]
Arrives from: B01 (The Basement)
Beat: A clerk behind a hatch, cardigan, 1970s glasses, smiling. 'File request? Just sign the slip.'
Links (write each target as a token):
  - {B03}  "Sign the slip"  → leads to: The slip
  - {B04}  "Search the stacks yourself"  → leads to: The stacks
  - {B06}  "If Ros is with you: let her work out the filing system"  [condition: lacks WARDED]  → leads to: Terminal digit
Effects (state them in the text, using in-world names): (hidden, never mention) RECORDS

### B11 — Linen services  [choice, Act 2, Basement]
Arrives from: B01 (The Basement)
Beat: Cages of laundered sheets, a mangle from 1890, and on a rail, staff tabards by decade. One is 1979, blue, name tape M.
Links (write each target as a token):
  - {B23}  "Take the 1979 tabard (if you do not have it)"  [condition: lacks TABARD]  → leads to: The tabard
  - {B01}  "Leave it"  → leads to: The Basement
Effects (state them in the text, using in-world names): (hidden, never mention) LINEN

### B09 — Asked  [story, Act 2, Basement]
Arrives from: B08 (The LPA)
Beat: MENDED route 2 of 3 (Records). If neither request is yet told, THE telling (both requests, see W21). Otherwise pointer. Lose 2 Fear. Codeword MENDED.
Links (write each target as a token):
  - {B01}  "Continue"  → leads to: The Basement
Effects (state them in the text, using in-world names): Note MENDED; (hidden, never mention) SENT; (hidden, never mention) ASKED; Fear -2

### LOCKER — Locker 179  [item, Act 2, Basement]
Arrives from: B12 (Property)
Beat: Mum's staff locker, 1979: a photo of the night shift (a row of young nurses; the Sister's face is a blur of all of them), her ring, warm, and a copy of the letter in its envelope. Property keeps everything. Lose 1 Fear. Note the RING and MUM'S LETTER.
Links (write each target as a token):
  - {B01}  "Continue"  → leads to: The Basement
Effects (state them in the text, using in-world names): Note RING; Note MUM'S LETTER; Fear -1
Design note: FIXED NUMBER 179. RING route 3; letter route 2. Analog document (the photo). If the reader already holds the letter, the text says it's the same envelope.

### D05 — Down only  [death, Act 2, Basement]
Arrives from: B29 (The lift)
Beat: The doors close and the lift goes down: sub-basement, foundations, the old fever pits, floors with no numbers and then floors with names on them, and one of them is yours.
Effects (state them in the text, using in-world names): Wristband +1
Death — the warning the reader was given: Notice rule 4: after 3 a.m. the lifts go down only.  End: 'Fill in 1 more field on your wristband. Return to {B01} and choose again.'

### B22 — Torn  [story, Act 2, Basement]
Arrives from: B21 (The in-tray)
Beat: It tears like skin. Somewhere above, a phone stops ringing. When you come back to the lift, Ros is sitting on the stairs in her coat, furious and confused, and very glad to see you. Cross off WARDED. Codeword HELD. Lose 2 Vigour.
Links (write each target as a token):
  - {B01}  "Continue"  → leads to: The Basement
Effects (state them in the text, using in-world names): Note HELD; Cross off WARDED; Vigour -2

### B05 — The porter  [combat, Act 2, Basement]
Arrives from: B04 (The stacks)
Beat: An empty trolley at the end of the stack, then a porter behind it. THE PORTER  NERVE 8  VIGOUR 8.
Links (write each target as a token):
  - {B07}  "If you win"  [condition: fight won]  → leads to: Mum's file
  - {D_VIGOUR}  "If your Vigour reaches 0"  [condition: fight lost]  → leads to: Spent
Foe line: THE PORTER  NERVE 8  VIG 8
Design note: Checkpoint before this fight: B01.
