### W03 — Just a minute  [story, Act 2, Old Wing]
Arrives from: W02 (The Nightingale ward)
Beat: She sits, then lies back, just for a minute. When you look round from the Kept, the bed is made and Ros is gone, and somewhere down the wing her phone begins to ring. Gain 1 Fear. Codeword WARDED.
Links (write each target as a token):
  - {W05}  "Continue"  → leads to: The Kept
Effects (state them in the text, using in-world names): Note WARDED; Fear +1
Design note: WARDED route 2 (Rule 3, broken by Ros).

### W15 — The clip  [test, Act 2, Old Wing]
Arrives from: W14 (The chapel)
Beat: The pages riffle as you reach for it. Test your Nerve.
Links (write each target as a token):
  - {W16}  "Success"  [condition: test passed]  → leads to: Unclipped
  - {W17}  "Failure"  [condition: test failed]  → leads to: Your name in the book
Test: Nerve

### W27 — Surgical scissors  [story, Act 2, Old Wing]
Arrives from: W13 (The far doors)
Beat: Ros digs the scissors out of her bag ('Don't ask'). One snip. A field drops off your wristband and the cut stings like it was skin. Cross off one field of your wristband. Lose 1 Vigour.
Links (write each target as a token):
  - {W01}  "Continue"  → leads to: The Old Wing
Effects (state them in the text, using in-world names): (hidden, never mention) CUT_W; Vigour -1; Wristband -1

### W07 — Gary's badge  [item, Act 2, Old Wing]
Arrives from: W06 (Gary, 1986)
Beat: He unclips it and gives it to you: VISITOR, St Bede's, 1986. 'It goes to whoever's visiting.' It now has your name. He settles back, smiling, and stays. Gain 1 Fear. Note the VISITOR'S BADGE. Codeword PROMISE.
Links (write each target as a token):
  - {W10}  "Continue"  → leads to: The round
Effects (state them in the text, using in-world names): Note VISITOR'S BADGE; Note PROMISE; Fear +1
Design note: Badge route 1 of 3 (moral). PROMISE pays off in Act 3 (R06a).

### W08 — Side B  [story, Act 2, Old Wing]
Arrives from: W05 (The Kept)
Beat: She gives you one earphone. A training tape: a young woman's voice reading obs, laughing at a mistake, a filthy laugh you know. 'Never let them see you're tired,' says someone else on the tape. Gain 1 Fear.
Links (write each target as a token):
  - {W05}  "Continue"  → leads to: The Kept
Effects (state them in the text, using in-world names): (hidden, never mention) WALKMAN; Fear +1
Design note: Lore: Mum's voice, 1979. The Sister learned her kindness from people like Mum.

### W17 — Your name in the book  [story, Act 2, Old Wing]
Arrives from: W15 (The clip)
Beat: The pages turn to tonight by themselves and your name is already there, in her hand. The badge stays clipped. Fill in one more field of your wristband.
Links (write each target as a token):
  - {W01}  "Continue"  → leads to: The Old Wing
Effects (state them in the text, using in-world names): Wristband +1

### W30 — Retreat  [story, Act 2, Old Wing]
Arrives from: W01 (The Old Wing)
Beat: You go back the way you came, which is shorter. Behind you, the ward lights drop to night setting.
Links (write each target as a token):
  - {H02}  "Back to the Main Corridor (if you do not have RETURNED)"  [condition: lacks RETURNED]  → leads to: Back on the Main Corridor
  - {H05}  "Back to the Main Corridor (if you have RETURNED but not OFFERED)"  [condition: has RETURNED and lacks OFFERED]  → leads to: An offer
  - {H01}  "Back to the Main Corridor (if you have RETURNED and OFFERED)"  [condition: has RETURNED and has OFFERED]  → leads to: The Main Corridor
Design note: Clock exit without the item: costs a ROUNDS tick.

### W19 — Who for  [story, Act 2, Old Wing]
Arrives from: W18 (Candles)
Beat: 'Dad. And one for you, actually. For the six years.' She says it to the candle, but she says it. Codeword SPOKE.
Links (write each target as a token):
  - {W01}  "Continue"  → leads to: The Old Wing
Effects (state them in the text, using in-world names): Note SPOKE
Design note: SPOKE route 4 of 4.

### W26 — The night porter  [combat, Act 2, Old Wing]
Arrives from: W22 (The drawer)
Beat: The porter fills the doorway with his empty trolley. He'd like to help you onto it. THE NIGHT PORTER  NERVE 7  VIGOUR 8.
Links (write each target as a token):
  - {W23}  "If you win"  [condition: fight won]  → leads to: A badge from the drawer
  - {D_VIGOUR}  "If your Vigour reaches 0"  [condition: fight lost]  → leads to: Spent
Foe line: THE NIGHT PORTER  NERVE 7  VIG 8
Design note: Checkpoint before this fight: W01.

### W09 — Waited  [story, Act 2, Old Wing]
Arrives from: W06 (Gary, 1986)
Beat: 'She didn't come either,' he says, without blame, and turns his face to the wall. Gain 1 Fear.
Links (write each target as a token):
  - {W10}  "Continue"  → leads to: The round
Effects (state them in the text, using in-world names): Fear +1

### W22 — The drawer  [test, Act 2, Old Wing]
Arrives from: W20 (The Sister's office)
Beat: Visitor badges, a whole drawer, in elastic bands by decade. Footsteps that never hurry. Test your Fortune.
Links (write each target as a token):
  - {W23}  "Lucky"  [condition: test passed]  → leads to: A badge from the drawer
  - {W26}  "Unlucky"  [condition: test failed]  → leads to: The night porter
Test: Fortune

### W20 — The Sister's office  [choice, Act 2, Old Wing]
Arrives from: W24 (The rota, 1979), W01 (The Old Wing), W23 (A badge from the drawer), W25 (The tabard)
Beat: Her office, immaculate. A desk drawer, a framed duty rota, a tabard on the back of the door. The kettle is still warm.
Links (write each target as a token):
  - {W22}  "Search the desk drawer (if you do not have the VISITOR'S BADGE)"  [condition: lacks VISITOR'S BADGE]  → leads to: The drawer
  - {W24}  "Read the duty rota"  [condition: lacks ROTA]  → leads to: The rota, 1979
  - {W25}  "Take the tabard off the hook (if you do not have it)"  [condition: lacks TABARD]  → leads to: The tabard
  - {W01}  "Leave"  → leads to: The Old Wing
Design note: Repeatable room (one-shots inside are guarded).

### W16 — Unclipped  [item, Act 2, Old Wing]
Arrives from: W15 (The clip)
Beat: It comes free. The book settles. Note the VISITOR'S BADGE.
Links (write each target as a token):
  - {W01}  "Continue"  → leads to: The Old Wing
Effects (state them in the text, using in-world names): Note VISITOR'S BADGE
Design note: Badge route 2 of 3 (nerve).

### W29 — One room behind  [story, Act 2, Old Wing]
Arrives from: W31 (Ros), W01 (The Old Wing)
Beat: Leaving the Old Wing, the round is in the ward you've just left, then the corridor, a room behind you all the way. You don't look back. Gain 1 Fear.
Links (write each target as a token):
  - {H02}  "Back to the Main Corridor (if you do not have RETURNED)"  [condition: lacks RETURNED]  → leads to: Back on the Main Corridor
  - {H05}  "Back to the Main Corridor (if you have RETURNED but not OFFERED)"  [condition: has RETURNED and lacks OFFERED]  → leads to: An offer
  - {H01}  "Back to the Main Corridor (if you have RETURNED and OFFERED)"  [condition: has RETURNED and has OFFERED]  → leads to: The Main Corridor
Effects (state them in the text, using in-world names): Fear +1
Design note: Clock exit (item held).

### W12 — Checked  [story, Act 2, Old Wing]
Arrives from: W10 (The round)
Beat: She takes your wrist on the way past, as if you were one of hers. When she lets go, WARD is filled in: OLD WING. Fill in one more field of your wristband.
Links (write each target as a token):
  - {W13}  "Continue"  → leads to: The far doors
Effects (state them in the text, using in-world names): Wristband +1

### W31 — Ros  [story, Act 2, Old Wing]
Arrives from: W28 (Ros's bed)
Beat: 'Ros.' Her eyes open on the second time. Her wristband is blank. 'Did I fall asleep? Did they ring?' Cross off WARDED. Codeword HELD.
Links (write each target as a token):
  - {W29}  "Continue (if you have the VISITOR'S BADGE)"  [condition: has VISITOR'S BADGE]  → leads to: One room behind
  - {W01}  "Continue (if you do not)"  [condition: lacks VISITOR'S BADGE]  → leads to: The Old Wing
Effects (state them in the text, using in-world names): Note HELD; Cross off WARDED; Vigour -1
Design note: Rescue counts as HELD.

### W24 — The rota, 1979  [story, Act 2, Old Wing]
Arrives from: W20 (The Sister's office)
Beat: NIGHTS, OLD WING, MARCH 1979. Sister's name rubbed out by thumbs. Auxiliary: M. - Mum's maiden name. Someone has drawn a tiny smiling face beside it.
Links (write each target as a token):
  - {W20}  "Continue"  → leads to: The Sister's office
Effects (state them in the text, using in-world names): (hidden, never mention) ROTA; (hidden, never mention) KNOWS_1979
Design note: Analog document. KNOWS_1979 route 2.

### D03 — Lights out  [death, Act 2, Old Wing]
Arrives from: W10 (The round), W28 (Ros's bed)
Beat: The sheets are cool and tight. She doesn't wake you. She tucks you in, and checks your pulse, and the obs are perfect, every hour, for ever.
Effects (state them in the text, using in-world names): Wristband +1
Death — the warning the reader was given: Notice rule 3: never lie down on a ward bed. The Kept are harmless unless you lie down beside them.  End: 'Fill in 1 more field on your wristband. Return to {W01} and choose again.'

### W10 — The round  [choice, Act 2, Old Wing]
Arrives from: W07 (Gary's badge), W09 (Waited), W05 (The Kept)
Beat: The far doors open and the round comes in: the red torch, the fob watch. Every one of the Kept holds out a wrist in unison. One empty bed has its blanket turned down.
Links (write each target as a token):
  - {W11}  "Stand at a bedside with the badge clipped on (if you have the VISITOR'S BADGE)"  [condition: has VISITOR'S BADGE]  → leads to: Passed over
  - {W11}  "Fall in behind her like staff (if you are wearing the TABARD)"  [condition: has TABARD]  → leads to: Passed over
  - {W12}  "Stand at a bedside like a visitor (if you have no badge and no tabard)"  [condition: lacks VISITOR'S BADGE and lacks TABARD]  → leads to: Checked
  - {W13}  "Keep walking for the far doors"  → leads to: The far doors
  - {D03}  "Get into the empty bed and pull up the blanket: she won't wake a sleeping patient"  → leads to: Lights out
Design note: One-room-behind set piece; the obs in unison. D03 is tempting as a hiding place.

### W14 — The chapel  [choice, Act 2, Old Wing]
Arrives from: W01 (The Old Wing)
Beat: Candles, a lectern, a visitors' book open at tonight. A VISITOR badge is clipped to its cover. A card: SIGN FOR A PRAYER TO BE SAID FOR YOUR LOVED ONE.
Links (write each target as a token):
  - {D04}  "Sign the book for Mum"  → leads to: Signed
  - {W15}  "Unclip the badge without signing (if you do not have the VISITOR'S BADGE)"  [condition: lacks VISITOR'S BADGE]  → leads to: The clip
  - {W18}  "Light a candle"  → leads to: Candles
Effects (state them in the text, using in-world names): (hidden, never mention) CHAPEL
Design note: Rule 6 temptation: a prayer for Mum.

### W18 — Candles  [story, Act 2, Old Wing]
Arrives from: W14 (The chapel)
Beat: One candle for Mum. If Ros is with you, she lights a second without saying who for. Lose 2 Fear.
Links (write each target as a token):
  - {W19}  "If Ros is with you and you do not have SPOKE: ask her who the second one is for"  [condition: lacks WARDED and lacks SPOKE]  → leads to: Who for
  - {W21}  "If Ros is with you and you have SPOKE and HELD but not MENDED: tell her why you stayed"  [condition: lacks WARDED and has SPOKE and has HELD and lacks MENDED]  → leads to: Why you stayed
  - {W01}  "Leave the chapel"  → leads to: The Old Wing
Effects (state them in the text, using in-world names): Fear -2

### W01 — The Old Wing  [choice, Act 2, Old Wing]
Arrives from: W27 (Surgical scissors), W17 (Your name in the book), W19 (Who for), W20 (The Sister's office), W16 (Unclipped), W31 (Ros), H01 (The Main Corridor), W18 (Candles), W28 (Ros's bed), W21 (Why you stayed), W13 (The far doors)
Beat: Return line first. The 1890s fever wing: tiled walls, radiators like organ pipes, the corridor longer going than coming back.
Links (write each target as a token):
  - {W02}  "The Nightingale ward"  [condition: lacks NIGHTINGALE]  → leads to: The Nightingale ward
  - {W14}  "The chapel"  [condition: lacks CHAPEL]  → leads to: The chapel
  - {W20}  "The Sister's office"  → leads to: The Sister's office
  - {W28}  "Follow the sound of Ros's phone (if you have WARDED)"  [condition: has WARDED]  → leads to: Ros's bed
  - {W29}  "Back to the Main Corridor (if you have the VISITOR'S BADGE)"  [condition: has VISITOR'S BADGE]  → leads to: One room behind
  - {W30}  "Back to the Main Corridor without it (if you do not have the VISITOR'S BADGE)"  [condition: lacks VISITOR'S BADGE]  → leads to: Retreat
Design note: Zone junction and checkpoint. The office is repeatable until the badge is held (it always yields it), so the zone can't softlock.

### W05 — The Kept  [choice, Act 2, Old Wing]
Arrives from: W03 (Just a minute), W08 (Side B), W02 (The Nightingale ward), W04 (Upright)
Beat: Patients from every decade, smiling, not dying and not recovering: a man in 1952 winceyette, a woman with a Walkman, a boy in a 1986 football kit who waves.
Links (write each target as a token):
  - {W06}  "Go to the boy (if you do not have the VISITOR'S BADGE)"  [condition: lacks VISITOR'S BADGE]  → leads to: Gary, 1986
  - {W08}  "Sit with the woman with the Walkman"  [condition: lacks WALKMAN]  → leads to: Side B
  - {W10}  "Walk on toward the far doors"  → leads to: The round
Design note: Analog lore + set piece. The Kept are harmless unless you lie down beside them (clue for D03/D10).

### W28 — Ros's bed  [choice, Act 2, Old Wing]
Arrives from: H01 (The Main Corridor), W01 (The Old Wing)
Beat: A side room. Ros asleep under a 1952 blanket, smiling her un-Ros smile. Her wristband is filled in: ROSALIND, every field. Her phone rings in her coat on the chair.
Links (write each target as a token):
  - {W31}  "Say her name, the short one only family uses"  → leads to: Ros
  - {D03}  "Lie down beside her until she wakes"  → leads to: Lights out
  - {W01}  "Leave her for now"  → leads to: The Old Wing
Design note: Rescue route 1 (also reachable from the hub once the zone is gated). The Sister cannot read a name spoken by someone who loves you.

### W23 — A badge from the drawer  [item, Act 2, Old Wing]
Arrives from: W26 (The night porter), W22 (The drawer)
Beat: You take one from the top: VISITOR, blank, waiting for a name. Note the VISITOR'S BADGE.
Links (write each target as a token):
  - {W20}  "Continue"  → leads to: The Sister's office
Effects (state them in the text, using in-world names): Note VISITOR'S BADGE
Design note: Badge route 3 of 3 (test, or fight in W26).

### W02 — The Nightingale ward  [choice, Act 2, Old Wing]
Arrives from: W01 (The Old Wing)
Beat: Thirty beds, all made, most of them full. Ros sways in the doorway: jet lag finally landing. 'I just need to sit down.'
Links (write each target as a token):
  - {W03}  "Let her sit on the empty bed by the door for a minute (if Ros is with you)"  [condition: lacks WARDED]  → leads to: Just a minute
  - {W04}  "Get your shoulder under her arm and keep her walking (if Ros is with you)"  [condition: lacks WARDED]  → leads to: Upright
  - {W05}  "Walk the ward (if you are alone)"  [condition: has WARDED]  → leads to: The Kept
Effects (state them in the text, using in-world names): (hidden, never mention) NIGHTINGALE

### W06 — Gary, 1986  [choice, Act 2, Old Wing]
Arrives from: W05 (The Kept)
Beat: Appendix, he says. His mum's visitor's badge is clipped to his locker. 'She said she'd be back at visiting. Will you tell her I waited?'
Links (write each target as a token):
  - {W07}  "Promise him"  → leads to: Gary's badge
  - {W09}  "Tell him you can't promise anything"  → leads to: Waited

### W11 — Passed over  [story, Act 2, Old Wing]
Arrives from: W10 (The round)
Beat: The torch passes over you like you are furniture. 'Visitors,' she says fondly, to nobody.
Links (write each target as a token):
  - {W13}  "Continue"  → leads to: The far doors

### W21 — Why you stayed  [story, Act 2, Old Wing]
Arrives from: W18 (Candles)
Beat: MENDED route 1 of 3 (chapel). If neither request has been told yet, this is THE telling: you tell her Mum asked you to stay ('Don't let them put me anywhere'); she tells you Mum sent her ('If you stay, your sister will let you do everything'). If one half is already known (SENT/ASKED), pointer only. Lose 2 Fear. Codeword MENDED.
Links (write each target as a token):
  - {W01}  "Continue"  → leads to: The Old Wing
Effects (state them in the text, using in-world names): (hidden, never mention) SENT; (hidden, never mention) ASKED; Fear -2
Design note: One telling: whichever MENDED scene comes first carries the full exchange; the others are gated not:MENDED.

### W25 — The tabard  [item, Act 2, Old Wing]
Arrives from: W20 (The Sister's office)
Beat: A blue 1979 auxiliary's tabard, name tape M. It fits you. Staff walk past rounds. Gain 1 Fear. Note the TABARD.
Links (write each target as a token):
  - {W20}  "Continue"  → leads to: The Sister's office
Effects (state them in the text, using in-world names): Note TABARD; Fear +1
Design note: Helps on rounds (W10, M23). Must be taken off in Act 3 (R32) or it is the Night Staff ending; forced choice at 4 fields (R31).

### W13 — The far doors  [choice, Act 2, Old Wing]
Arrives from: W12 (Checked), W10 (The round), W11 (Passed over)
Beat: Out in the tiled corridor, the ward breathing behind you.
Links (write each target as a token):
  - {W27}  "If Ros is with you and you have SPOKE: hold out your wrist for her scissors"  [condition: lacks WARDED and has SPOKE and lacks CUT_W and Wristband ≥ 1]  → leads to: Surgical scissors
  - {W01}  "Back along the corridor"  → leads to: The Old Wing
Design note: Scissors moment 1 of 2 (W27, R12).

### W04 — Upright  [story, Act 2, Old Wing]
Arrives from: W02 (The Nightingale ward)
Beat: She's heavier than she looks. 'I'm fine.' She isn't, and she lets you. Codeword HELD.
Links (write each target as a token):
  - {W05}  "Continue"  → leads to: The Kept
Effects (state them in the text, using in-world names): Note HELD
Design note: HELD route 2.

### D04 — Signed  [death, Act 2, Old Wing]
Arrives from: W14 (The chapel)
Beat: Your pen is still on the page when the prayer begins, in her voice, very softly, and it is for you, and it is the kind they say at the end.
Effects (state them in the text, using in-world names): Wristband +1
Death — the warning the reader was given: Notice rule 6: do not sign anything.  End: 'Fill in 1 more field on your wristband. Return to {W01} and choose again.'
