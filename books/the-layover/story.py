"""
THE LAYOVER - full section architecture.
Each section: key, act, zone, kind, title, beat (what happens), links, effects.
Keys are internal; book numbers are assigned (shuffled) by build.py.

Link: (target, label, condition)
  condition: None | "has:X" | "not:X" | "has:X&not:Y" ... | "pass"/"fail" (test) | "win"/"lose" (combat) | "hidden:..." (computed, not printed)
Effects (fx): gain/lose flags, fear +/-, vig +/-.
"""

S = []
def N(key, act, zone, kind, title, beat, links, gain=(), lose=(), fear=0, vig=0,
      test=None, warn=None, clue=None, checkpoint=None, notes=None):
    S.append(dict(key=key, act=act, zone=zone, kind=kind, title=title, beat=beat,
                  links=[dict(to=l[0], label=l[1], cond=(l[2] if len(l) > 2 else None)) for l in links],
                  gain=list(gain), lose=list(lose), fear=fear, vig=vig, test=test,
                  warn=warn, clue=clue or [], checkpoint=checkpoint, notes=notes))

V = "D_VIGOUR"   # shared death: Vigour reaches 0
F = "E_FINALCALL" # shared ending: Fear reaches its limit

# ======================================================================
# ACT 1 - DELAYED  (near-linear opening, then the rules of the place)
# ======================================================================
A, Z = 1, "Gate 14"
N("A01", A, Z, "story", "11:52pm",
  "Gate 14. You and Sam, the sibling you haven't spoken to in three years, are flying home for your father's funeral. Flight LV 137. Sam sits two seats away, earbuds in. The board flickers.",
  [("A02", "Continue")], notes="Section 1. Establish grief, estrangement, flight number LV 137 (secret-ending key).")
N("A02", A, Z, "choice", "Delayed",
  "LV 137 flips to DELAYED - no new time. Sam: 'Typical.' The first words in three years.",
  [("A03", "Suggest getting food together"), ("A04", "Stay at the gate and call your aunt")])
N("A03", A, Z, "story", "Last orders",
  "The only open kiosk. The cashier never blinks. Your receipt is dated 1987. Sam laughs at it, then stops laughing.",
  [("A05", "Continue")])
N("A04", A, Z, "story", "No signal",
  "No signal. One notification: a voicemail from Dad, timestamped tomorrow, 05:59. You don't play it.",
  [("A05", "Continue")], fear=1, notes="Plants the 05:59 deadline.")
N("A05", A, Z, "choice", "1:04am",
  "A chime. 'Passengers are thanked for their patience.' Everyone stands at once and walks toward Exit too fast. Sam has fallen asleep.",
  [("A06", "Follow the crowd to the exit"), ("A07", "Stay with Sam")])
N("A06", A, Z, "story", "The first loop",
  "The exit corridor bends, a walkway hums - and you step out at Gate 14. Your bag is where you left it. The crowd is gone.",
  [("A08", "Continue")], fear=1)
N("A07", A, Z, "story", "Lights out",
  "You watch the terminal die zone by zone, lights clicking off toward you. Sam wakes as the last bank goes dark.",
  [("A08", "Continue")])
N("A08", A, Z, "choice", "Gate 0",
  "The sign above you no longer says 14. It says 0. Sam is on their feet, shaking. 'Where is everyone?'",
  [("A09", "Hold Sam's arm and keep your voice calm"), ("A10", "Tell Sam to stop overreacting")])
N("A09", A, Z, "story", "Truce",
  "Sam lets you. For a moment you are both kids again. Sam whispers: 'I saw Dad's name on the board.' Codeword TRUCE.",
  [("A11", "Continue")], gain=["TRUCE"], notes="First route to TRUCE (second: O27).")
N("A10", A, Z, "story", "Distance",
  "Sam walks off ten paces and stands with their back to you. A soft chime sounds from somewhere above. You follow.",
  [("A11", "Continue")])
N("A11", A, Z, "choice", "Ground Staff",
  "A woman in an immaculate uniform. Name badge: HOSTESS. Her smile doesn't move when she speaks. 'Complimentary voucher?'",
  [("A12", "Accept the voucher"), ("A13", "Refuse politely"), ("A14", "Ask how to get out")])
N("A12", A, Z, "item", "Valid until departure",
  "VALID UNTIL DEPARTURE. DO NOT LEAVE THE TERMINAL. She taps her tablet. You are logged.",
  [("A15", "Continue")], gain=["VOUCHER"])
N("A13", A, Z, "story", "Noted",
  "She keeps smiling and types something. Your name appears on a screen behind her, then vanishes.",
  [("A15", "Continue")], fear=1)
N("A14", A, Z, "story", "Airside",
  "'All passengers must remain airside until boarding. The Handbook is very clear.' She walks away without footsteps.",
  [("A15", "Continue")], notes="Points the reader to the Handbook.")
N("A15", A, Z, "item", "The Handbook",
  "Under a seat: a laminated booklet, IRREGULAR OPERATIONS HANDBOOK. Rule 1: Do not look at staff when the lights flicker. 2: Never answer the Announcer. 3: Never ride a walkway that runs backwards. 4: Do not eat or drink airside after midnight. 5: Gate 00 does not exist. 6: Do not sleep airside. 7: If something is wrong, turn back. The last page is torn out.",
  [("A16", "Continue")], gain=["HANDBOOK"],
  notes="MASTER CLUE SECTION. Every rule-based death in the book points back here. Printed again as a tear-out on the adventure sheet.")
N("A16", A, Z, "choice", "Rules",
  "Sam reads over your shoulder.",
  [("A17", "Read it aloud together"), ("A18", "Pocket it and keep moving")])
N("A17", A, Z, "story", "Rule 0",
  "Scratched into the back cover, in biro: RULE 0 - IT KEEPS THE ONES WHO WON'T LET GO. Sam goes quiet. Reading it together helps, somehow.",
  [("A18", "Continue")], fear=-1, notes="Thematic thesis. Clue for D06.")
N("A18", A, Z, "choice", "Flicker",
  "The lights stutter. Something tall in a uniform walks past the far gates.",
  [("A19", "Watch it"), ("A20", "Shut your eyes")])
N("A19", A, Z, "story", "You looked",
  "Its face is too long and it is already looking at you. A pressure behind your eyes. Lose 2 Vigour, gain 2 Fear.",
  [("A21", "Continue")], vig=-2, fear=2, clue=["A15"],
  notes="Rule 1 broken: punished gradually, not with death (first offence).")
N("A20", A, Z, "story", "Footsteps",
  "Footsteps pass close enough to feel. Sam's hand finds yours in the dark.",
  [("A21", "Continue")])
N("A21", A, Z, "anomaly", "Tutorial anomaly",
  "The gate area, described in full: rows of seats, a cleaning cart, the gate clock - its second hand ticks backwards. Is something wrong?",
  [("A22", "Something is wrong - turn back"), ("A23", "Nothing is wrong - keep going")],
  notes="Teaches the anomaly mechanic with an easy, fair example (Rule 7).")
N("A22", A, Z, "story", "Noticed",
  "You turn back and the clock ticks forwards again. You are learning the place. Lose 1 Fear.",
  [("A24", "Continue")], fear=-1)
N("A23", A, Z, "story", "Missed",
  "The corridor folds and you are back where you started. Gain 1 Fear. The clock still ticks backwards; now you see it.",
  [("A24", "Continue")], fear=1)
N("A24", A, Z, "choice", "Paging",
  "The PA: 'Passenger ...' and it says your name. Calmly. Kindly. 'Please make yourself known.'",
  [("D01", "Answer: 'I'm here'"), ("A25", "Say nothing")])
N("D01", A, Z, "death", "Paged",
  "The voice comes from everywhere at once, then from inside your mouth. You are made known.",
  [], warn="Handbook Rule 2: Never answer the Announcer.", clue=["A15"], checkpoint="A24")
N("A25", A, Z, "choice", "Sam's name",
  "The Announcer pages Sam. Sam's lips start to move.",
  [("A26", "Cover Sam's mouth"), ("A27", "Let Sam answer")])
N("A26", A, Z, "story", "Silence",
  "Sam freezes, then understands. If you have TRUCE, Sam squeezes your hand. If not, Sam shoves you off, furious, but silent.",
  [("A28", "Continue")])
N("A27", A, Z, "story", "Marked",
  "'Here,' Sam says. Every light goes out. You drag Sam behind a pillar; something heavy passes. Lose 3 Vigour. Codeword MARKED.",
  [("A28", "Continue")], gain=["MARKED"], vig=-3, notes="Consequence pays off in Act 3 (G10-G13).")
N("A28", A, Z, "choice", "One light",
  "Far off, one desk is lit.",
  [("A29", "Go to the Information desk"), ("A30", "Go to the airline service desk")])
N("A29", A, Z, "item", "Terminal map",
  "Unmanned. A touchscreen map: THE CONCOURSE, DUTY-FREE & FOOD COURT, THE AIRPORT HOTEL. Gate 0 pulses at the centre.",
  [("A31", "Continue")], gain=["MAP"])
N("A30", A, Z, "story", "The Delayed",
  "A grey passenger, half grown into the chair. 'To board you need three things. The true pass. The papers. The last page.' Its eyes close.",
  [("A31", "Continue")], notes="States the Act 2 goal plainly (fairness).")
N("A31", A, Z, "choice", "Breathe",
  "Sam is shaking.",
  [("A32", "Sit down and rest a while"), ("A33", "Keep moving")])
N("A32", A, Z, "story", "Dad",
  "Sam talks. Dad was born in 1952, 'the year the old terminal opened, he used to say.' Sam was with him at the end. You weren't. Gain 2 Vigour.",
  [("A34", "Continue")], vig=2, gain=["KNOWS_CODE"], notes="Clue 1 of 2 for the hotel safe (1952). Emotional core for Dark Copers.")
N("A33", A, Z, "choice", "The walkway",
  "A moving walkway hums down the corridor ahead. It is running backwards.",
  [("D02", "Step onto it"), ("A34", "Walk beside it")])
N("D02", A, Z, "death", "Carried back",
  "It takes you gently, all the way back - past Gate 14, past the night, past the years.",
  [], warn="Handbook Rule 3: never ride a walkway that runs backwards; the text says it runs backwards.", clue=["A15", "A33"], checkpoint="A33")
N("A34", A, Z, "choice", "Unclaimed",
  "A baggage carousel starts by itself. A suitcase unzips from the inside.",
  [("A35", "Fight what crawls out"), ("A36", "Run")])
N("A35", A, Z, "combat", "The Unclaimed",
  "Combat tutorial.", [("A37", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")],
  test=dict(type="combat", foe="THE UNCLAIMED", nerve=7, vig=7))
N("A36", A, Z, "test", "Run",
  "Test your Fortune.", [("A37", "Lucky", "pass"), ("A37", "Unlucky: lose 2 Vigour", "fail")],
  test=dict(type="Fortune"))
N("A37", A, Z, "story", "Sam's bag",
  "Sam's backpack lies torn open. The passport is gone. 'They took my passport.' Sam's voice cracks.",
  [("A38", "Continue")], notes="Motivates the Hotel quest.")
N("A38", A, Z, "story", "The Atrium",
  "The central Atrium. The great departures board lists cities that don't exist. One line holds steady: LV 137 - FINAL BOARDING - GATE 0 - 05:59.",
  [("H01", "Continue")], notes="End of Act 1. Deadline and goal on screen.")

# ======================================================================
# HUB - THE ATRIUM
# ======================================================================
A, Z = 2, "Atrium"
N("H01", A, Z, "hub", "The Atrium (hub)",
  "The board, the three corridors, the silence. Where now?",
  [("C01", "The Concourse and Gates"),
   ("F01", "Duty-Free and the Food Court"),
   ("O01", "The Airport Hotel"),
   ("H04", "The Lost & Found desk", "not:LF_USED"),
   ("G43", "Gate 0 (only if you hold the boarding pass, the passport and the last page)", "has:BOARDING_PASS&has:PASSPORT&has:LAST_PAGE")],
  notes="Hub. Key items can be found in any order. Gate 0 is locked behind all three.")
N("H02", A, Z, "story", "Back in the Atrium",
  "The Atrium has changed while you were gone. Count the escalators; there is one more than before.",
  [("H05", "Continue", "not:ECHO"), ("H03", "Continue", "has:ECHO&not:OFFERED"), ("H01", "Continue", "has:ECHO&has:OFFERED")])
N("H05", A, Z, "story", "The board updates",
  "The board flips through every city, then settles: 05:59 is a little closer. Codeword ECHO.",
  [("H11", "Continue", "not:SAM_TAKEN"), ("H01", "Continue", "has:SAM_TAKEN")], gain=["ECHO"])
N("H11", A, Z, "choice", "We're fine",
  "Sam's phone, nearly dead. He scrolls to three years of texts: every one from him says 'We're fine.' He admits it now: they were meant to keep you away. The night you left, at a gate like this one, he told you not to bother coming back.",
  [("H12", "Tell him you should have come anyway"), ("H01", "Tell him he never asked you to")],
  notes="Sam's share of the blame; origin of the estrangement. Owning it gives TRUCE (route 3).")
N("H12", A, Z, "story", "Anyway",
  "You say it. Sam puts the phone face down on his knee, the way you did at Gate 14. Codeword TRUCE.",
  [("H01", "Continue")], gain=["TRUCE"])
N("H03", A, Z, "choice", "An offer",
  "The Announcer, softly, just to you: 'Leave Sam with us and you may board now. No questions.'",
  [("AL01", "Accept"), ("H06", "Refuse")], gain=["OFFERED"], notes="Plays exactly once (codeword OFFERED). The midpoint.")
N("H06", A, Z, "story", "Refused",
  "'Then we'll wait together.' Gain 1 Fear.",
  [("H01", "Continue"), (F, "If your Fear has reached its limit", "fearlimit")], fear=1)
N("AL01", A, Z, "choice", "Alone",
  "You walk toward Gate 0. Behind you, Sam is calling your name.",
  [("H01", "Turn back"), ("E_ALONE", "Keep walking")])
N("H04", A, Z, "choice", "Lost & Found",
  "Shelves of lost things from every decade. A sign: ONE ITEM PER PASSENGER.",
  [("H07", "Take the torch"), ("H08", "Take the first-aid kit"), ("H09", "Take the luggage tag that has your name on it")],
  gain=["LF_USED"])
N("H07", A, Z, "item", "Torch", "A heavy torch. It shows things as they are.", [("H01", "Continue")], gain=["TORCH"])
N("H08", A, Z, "item", "First aid", "Restore 6 Vigour once, at any time.", [("H01", "Continue")], gain=["FIRST_AID"])
N("H09", A, Z, "item", "Transfer tag",
  "TRANSFER. Underneath, handwritten: 'Your connection is your flight number.' Codeword TRANSFER.",
  [("H01", "Continue")], gain=["TRANSFER"], notes="Route 1 of 2 to TRANSFER (secret ending).")

# ======================================================================
# ZONE 1 - THE CONCOURSE & GATES   (key item: BOARDING_PASS - 4 routes)
# ======================================================================
Z = "Concourse"
N("C01", A, Z, "choice", "The Concourse",
  "Gates in both directions, numbered out of order. 23, 6, 41, 6.",
  [("C02", "Head toward the low-numbered gates"), ("C10", "Follow the sign for 'Gates 00'")])
N("C02", A, Z, "choice", "Waiting",
  "Every seat is taken by the Delayed, motionless. One old man turns his head.",
  [("C03", "Talk to him"), ("C06", "Sneak past")])
N("C03", A, Z, "choice", "Walter",
  "Walter has waited since 1998. His daughter was meeting him at arrivals. 'If you get out, tell her I tried.'",
  [("C04", "Promise him"), ("C05", "Refuse - you can't promise anything")])
N("C04", A, Z, "item", "A promise",
  "He presses his boarding pass into your hand. 'A pass takes the name of whoever holds it.' It now reads your name. He settles into the chair, and stays. Gain 1 Fear. Codeword PROMISE.",
  [("C09", "Continue")], gain=["PROMISE", "BOARDING_PASS"], fear=1, notes="Pass route A (moral).")
N("C05", A, Z, "story", "His grip",
  "His fingers lock round your wrist until Sam prises them off. Lose 2 Vigour.",
  [("C06", "Continue")], vig=-2)
N("C06", A, Z, "choice", "Gate desk",
  "A Ground Staff member types at a gate desk. Above, a TV plays the news with no sound.",
  [("C07", "Approach the desk"), ("C19", "Watch the TV"), ("C37", "Read what the printer behind the desk is printing", "not:READ_INCIDENT"), ("C10", "Keep walking")])
N("C37", A, Z, "item", "Incident report",
  "A dot-matrix printer chatters out a 1998 Larkvale incident report: crew names scratched out except one, MARGARET (purser); a note that during the delay 'crew member read the passenger list aloud; subject remained stationary for the duration'; and a reference to a previous irregular operation, 1987, 'see attached' - nothing attached.",
  [("C10", "Continue")], gain=["READ_INCIDENT"], notes="Analog document. Plants the unstated rule (it can't move while its sign is read aloud) used in G43, and the 1987 thread.")
N("C19", A, Z, "story", "1998",
  "Grainy news: 'Flight LV 137 lost over...' The same flight number as yours. The anchor turns and looks at the camera. Gain 1 Fear.",
  [("C10", "Continue")], fear=1, notes="Lore: the flight number matters (secret ending foreshadow).")
N("C07", A, Z, "choice", "Boarding pass, please",
  "'Boarding pass, please.' You don't have one.",
  [("C08", "Bluff"), ("C10", "Back away")])
N("C08", A, Z, "test", "Bluff", "Test your Nerve.",
  [("C32", "Success", "pass"), ("C30", "Failure", "fail")], test=dict(type="Nerve"))
N("C32", A, Z, "item", "Printed", "She prints a pass in your name. Seat 0A. Her smile widens a little too far.",
  [("C09", "Continue")], gain=["BOARDING_PASS"], notes="Pass route B (nerve).")
N("C30", A, Z, "combat", "Ground Staff", "She stands. She keeps standing.",
  [("C31", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")], test=dict(type="combat", foe="GROUND STAFF", nerve=8, vig=8))
N("C31", A, Z, "item", "Torn from the printer", "You rip the half-printed pass from the machine.",
  [("C09", "Continue")], gain=["BOARDING_PASS"], notes="Pass route C (combat).")
N("C09", A, Z, "story", "Concourse cleared", "The pass is warm in your pocket. Codeword CLEARED_C.",
  [("C35", "Head back toward the Atrium")], gain=["CLEARED_C"])
N("C35", A, Z, "choice", "One room behind",
  "Halfway back, the gate you just left goes dark behind you, then the one before it. The breathing is in the room you've just walked out of. Gain 1 Fear.",
  [("H02", "Turn and watch the doorway until you reach the Atrium (add 1 to your Claim: it learns your face)"), ("H02", "Shut your eyes, take Sam's hand if you can, and walk (gain 1 more Fear)")],
  fear=1, notes="Cashes in rule 5 (one room behind) mid-book. Option costs written into the text.")
N("C10", A, Z, "choice", "Gates 00",
  "The windows show no night - only white. Out on the apron, a man in Dad's coat is waving you over. Sam goes very still; at the jet bridge door, Sam hesitates and won't touch the handle.",
  [("C11", "Go to the window"), ("C12", "Pull Sam away"), ("D03", "Open the jet bridge door at Gate 00")])
N("D03", A, Z, "death", "The long bridge",
  "The jet bridge goes on and on. When you look back the door is a pinprick. You keep walking. You are still walking.",
  [], warn="Handbook Rule 5: Gate 00 does not exist. Sam refuses to touch the door.", clue=["A15", "C10"], checkpoint="C10")
N("C11", A, Z, "story", "The window",
  "It is him. The glass is freezing. Sam is crying. Gain 2 Fear.",
  [("C13", "If Sam is with you and you have TRUCE", "has:TRUCE&not:SAM_TAKEN"), ("C14", "If Sam is with you and you do not have TRUCE", "not:TRUCE&not:SAM_TAKEN"), ("C15", "If you have SAM_TAKEN", "has:SAM_TAKEN")], fear=2)
N("C12", A, Z, "story", "Not now",
  "'You never let me grieve,' Sam snaps. You keep walking anyway.",
  [("C15", "Continue")])
N("C13", A, Z, "choice", "Together",
  "Sam leans against you. This is the moment, if there is one.",
  [("C16", "Tell Sam why you never came to the hospital (only if you do not already have TOLD)", "not:TOLD"), ("C15", "Say nothing")])
N("C16", A, Z, "story", "The truth",
  "You were afraid to watch him die, so you let Sam do it alone. Sam doesn't forgive you, not yet, but holds on. Lose 2 Fear. Codeword TOLD.",
  [("C18", "Continue")], gain=["TOLD"], fear=-2, notes="Route 1 of 2 to TOLD (second: F29).")
N("C14", A, Z, "test", "Sam runs",
  "Sam bolts for the Gate 00 door. Test your Fortune.",
  [("C15", "Lucky - you catch Sam", "pass"), ("C17", "Unlucky", "fail")], test=dict(type="Fortune"))
N("C15", A, Z, "story", "Onward", "You keep moving through the Concourse.", [("C18", "Continue")])
N("C17", A, Z, "story", "Taken",
  "The door slams. A moment later Sam's voice comes from the PA, very small. Codeword SAM_TAKEN.",
  [("C18", "Continue")], gain=["SAM_TAKEN"], notes="Rescue routes: O16, O18 (hotel) or G41 (Act 3).")
N("C18", A, Z, "hub", "Concourse junction", "Corridors branch.",
  [("C26", "The prayer room", "not:PRAYED"), ("C29", "The smoking lounge", "not:SMOKED"),
   ("C33", "A child crying near Gate 9", "not:CHILD"), ("H02", "Back to the Atrium")])
N("C26", A, Z, "story", "Prayer room",
  "Quiet. Sam lights a candle for Dad. (If Sam was taken, a candle is already burning, still warm.) Lose 2 Fear.",
  [("C18", "Continue")], gain=["PRAYED"], fear=-2)
N("C29", A, Z, "test", "Smoking lounge",
  "A glass box full of smoke in human shapes. Something is written on a cigarette packet inside. Test your Fortune.",
  [("C27", "Lucky", "pass"), ("C18", "Unlucky: you breathe it in and lose 2 Vigour", "fail")], gain=["SMOKED"], test=dict(type="Fortune"))
N("C27", A, Z, "item", "Transfer",
  "The packet reads: TRANSFER PASSENGERS - YOUR CONNECTION IS YOUR FLIGHT NUMBER. Codeword TRANSFER.",
  [("C18", "Continue")], gain=["TRANSFER"], notes="Route 2 of 2 to TRANSFER.")
N("C33", A, Z, "choice", "Lost child",
  "A small child: 'I can't find my mum.' Under the lights, the child casts no shadow.",
  [("C34", "Kneel down to help"), ("C18", "Back away")], gain=["CHILD"])
N("C34", A, Z, "story", "Lure",
  "Its face opens like a zip. You tear free and run. Lose 3 Vigour, gain 1 Fear.",
  [("C18", "Continue")], vig=-3, fear=1, clue=["C33"], notes="Punished gradually; the missing shadow was the warning.")

# ======================================================================
# ZONE 2 - DUTY-FREE & THE FOOD COURT   (key item: LAST_PAGE - 5 routes)
# ======================================================================
Z = "Duty-Free"
N("F01", A, Z, "choice", "Duty-Free",
  "Perfume in the air: home, and hospital, at once.",
  [("F02", "The Duty-Free shop"), ("F15", "The Food Court"), ("F33", "The till at the closed kiosk by the arch", "not:TILL")])
N("F33", A, Z, "item", "Till roll",
  "A till roll spooled across the floor. The same order, rung up again and again: two cheese toasties, a tea, a hot chocolate. 14/03/1987. 23/11/1998. Tonight. Always 23:58.",
  [("F01", "Continue")], gain=["TILL"], notes="Analog document: the 1987 thread; your order from A03 has been placed before.")
N("F02", A, Z, "choice", "The shop",
  "Mirrored pillars. Your reflection moves a fraction of a second late.",
  [("F03", "Try a perfume tester"), ("F04", "Study the mirror"), ("F28", "Look at the newspapers"), ("F08", "Try the stockroom door")])
N("F03", A, Z, "story", "Aftershave",
  "Dad's aftershave. You're nine years old in the back of his car. Gain 1 Fear.",
  [("F05", "Continue")], fear=1)
N("F05", A, Z, "choice", "Sunglasses",
  "Sam (if Sam is with you) tries on ridiculous sunglasses and laughs - the first real laugh tonight. Gain 2 Vigour.",
  [("F29", "Tell Sam the truth about the hospital (only if Sam is with you and you do not already have TOLD)", "not:TOLD&not:SAM_TAKEN"), ("F08", "Laugh along and move on")], vig=2)
N("F29", A, Z, "story", "Said it",
  "In the middle of Duty-Free, of all places. Sam takes off the sunglasses and listens. Lose 2 Fear. Codeword TOLD.",
  [("F08", "Continue")], gain=["TOLD"], fear=-2, notes="Route 2 of 2 to TOLD.")
N("F28", A, Z, "story", "Tomorrow's paper",
  "Tomorrow's date. Page four: two siblings missing after an overnight delay. Your photo. Gain 1 Fear.",
  [("F02", "Continue")], fear=1, gain=["READ_PAPER"])
N("F04", A, Z, "anomaly", "The mirror",
  "You blink. Your reflection doesn't. Its lips are moving.",
  [("F06", "It's wrong - turn away"), ("F07", "It's just tired eyes - lean closer"), ("D05", "Touch the glass")])
N("D05", A, Z, "death", "Swapped",
  "Cool glass, then cool everything. You watch yourself walk away with Sam.",
  [], warn="The reflection lags (F02) and fails to blink; Rule 7: if something is wrong, turn back.", clue=["A15", "F02", "F04"], checkpoint="F04")
N("F06", A, Z, "story", "Message",
  "In the fog of your breath, letters appear on the glass: BEHIND THE WHISKY. Lose 1 Fear.",
  [("F08", "Continue")], fear=-1, notes="Clue for the stockroom route.")
N("F07", A, Z, "combat", "Your reflection", "It reaches out of the glass.",
  [("F06", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")], test=dict(type="combat", foe="REFLECTION", nerve=7, vig=6))
N("F08", A, Z, "choice", "STAFF ONLY",
  "The stockroom door.",
  [("F09", "Sneak in"), ("F10", "Knock")])
N("F09", A, Z, "test", "Sneak", "Test your Fortune.", [("F11", "Lucky", "pass"), ("F12", "Unlucky", "fail")], test=dict(type="Fortune"))
N("F10", A, Z, "choice", "Break room",
  "Staff sit facing the wall. The lights begin to flicker.",
  [("F11", "Keep your eyes down and tiptoe past"), ("F12", "Look at them")], notes="Rule 1 again, now with a cost.")
N("F11", A, Z, "item", "Stockroom",
  "Boxes labelled with passenger names. Yours holds your childhood things. Behind the whisky: a torn page, taped to the wall.",
  [("F14", "Continue")], gain=["LAST_PAGE"], notes="Last page route A.")
N("F12", A, Z, "choice", "Caught",
  "'Shoplifting is a serious matter.'",
  [("F13", "Fight"), ("F24", "Flee")])
N("F13", A, Z, "combat", "Ground Staff", "",
  [("F11", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")], test=dict(type="combat", foe="GROUND STAFF", nerve=8, vig=8))
N("F24", A, Z, "test", "Flee", "Test your Fortune.",
  [("F15", "Lucky", "pass"), ("F30", "Unlucky", "fail")], test=dict(type="Fortune"))
N("F30", A, Z, "story", "Clawed", "Nails drag down your back. Lose 4 Vigour.", [("F15", "Continue")], vig=-4)
N("F14", A, Z, "story", "The last page",
  "Rule 8: A pass carries every name its holder loves, once every debt is settled. Below, smaller: Transfer passengers - turn to your flight number. Codeword CLEARED_F.",
  [("H02", "Return to the Atrium")], gain=["CLEARED_F"],
  notes="Explains the Act 3 one-pass problem AND the secret-ending instruction.")
N("F15", A, Z, "choice", "The Food Court",
  "A Chef behind a counter, serving an endless queue of the Delayed. The food smells perfect. Sam's stomach growls.",
  [("F16", "Eat"), ("F17", "Don't eat"), ("F18", "Hand over your voucher", "has:VOUCHER"), ("F27", "Rest in the sleep pods by the windows")])
N("F16", A, Z, "choice", "Delicious",
  "It is the best thing you've ever tasted. Gain 4 Vigour. Codeword FED. The Chef slides a second plate across.",
  [("D04", "Eat the second plate"), ("F19", "Push it away")], gain=["FED"], vig=4, notes="FED is a debt settled in Act 3 (G06).")
N("D04", A, Z, "death", "Seated",
  "Halfway through, you realise you can't stand up. You don't want to. There's always more.",
  [], warn="Handbook Rule 4 (no eating after midnight); Sam says 'Don't'; the queue is the Delayed.", clue=["A15", "F15"], checkpoint="F16")
N("F17", A, Z, "story", "Hungry", "Your head swims. Lose 1 Vigour.", [("F19", "Continue")], vig=-1)
N("F18", A, Z, "item", "Voucher customer",
  "'Ah. A voucher customer.' He wraps your order in paper - the torn last page. 'Don't eat the sandwich.'",
  [("F20", "Continue")], gain=["LAST_PAGE"], lose=["VOUCHER"], notes="Last page route B: rewards accepting the voucher in A12.")
N("F19", A, Z, "choice", "A trade",
  "'You want the page. Everybody does. What will you give me?'",
  [("F21", "The memory of Dad's voice"), ("F22", "Blood"), ("F23", "Nothing")])
N("F21", A, Z, "item", "Forgotten",
  "He takes it. You try to remember how Dad said your name and can't. You have the page. Codeword FORGOT.",
  [("F20", "Continue")], gain=["FORGOT", "LAST_PAGE"], notes="Route C. FORGOT blocks the secret ending - a real price.")
N("F22", A, Z, "item", "Paid in full", "A small cut, a large cup. Lose 4 Vigour. You have the page.",
  [("F20", "Continue")], gain=["LAST_PAGE"], vig=-4, notes="Route D.")
N("F23", A, Z, "test", "Nothing",
  "Every one of the Delayed turns its head. Run. Test your Nerve.",
  [("F25", "Success", "pass"), ("F31", "Failure", "fail")], test=dict(type="Nerve"))
N("F31", A, Z, "story", "Hands", "Grey hands catch at you. Lose 3 Vigour.", [("F25", "Continue")], vig=-3)
N("F25", A, Z, "item", "Kitchen",
  "Freezers labelled by year. Inside one: a staff uniform with your name on it. The page is frozen to the door.",
  [("F20", "Continue")], gain=["LAST_PAGE"], notes="Route E. Foreshadows the Ground Crew ending.")
N("F20", A, Z, "story", "Out", "You leave the Food Court with the page.", [("F14", "Read it")])
N("F27", A, Z, "choice", "Sleep pods",
  "Soft blue light. Sam is exhausted: 'Ten minutes. Please.'",
  [("D09", "Lie down for ten minutes"), ("F15", "Refuse and keep Sam moving")])
N("D09", A, Z, "death", "Ten minutes",
  "You wake at the gate. The board says DELAYED. It is 11:52pm. Your hair is grey.",
  [], warn="Handbook Rule 6: Do not sleep airside.", clue=["A15"], checkpoint="F27")

# ======================================================================
# ZONE 3 - THE AIRPORT HOTEL   (key item: PASSPORT - 5 routes; Sam rescue)
# ======================================================================
Z = "Hotel"
N("O01", A, Z, "choice", "Hotel lobby",
  "A skybridge to the airport hotel. The carpet pattern repeats, and repeats.",
  [("O02", "Ring the bell at reception"), ("O31", "Read the guest book on the desk", "not:GUESTBOOK"), ("O08", "Go to the lifts"), ("O12", "Take the stairs"), ("O26", "The hotel bar", "not:BAR")])
N("O31", A, Z, "item", "Guest book",
  "A leather guest book. Every line the same night, 23/11/1998, in 137 hands. Near the top, a signature in a captain's confident loop: 'Capt. R.' Your father was Ray. The Night Manager's pen is still warm.",
  [("O02", "Ring the bell"), ("O08", "Go to the lifts")], gain=["GUESTBOOK"], notes="Analog document; seeds the open question of who the Announcer is (deliberately unresolved).")
N("O02", A, Z, "choice", "Night Manager",
  "Very tall. No reflection in the brass. 'Checking in?'",
  [("O03", "Check in"), ("O05", "Ask about lost passports"), ("O08", "Leave")])
N("O03", A, Z, "item", "Room 1952",
  "A key card: ROOM 1952. 'Checkout by six. You'll want to be well rested.' Codeword CHECKED_IN.",
  [("O08", "Continue")], gain=["ROOM_KEY", "CHECKED_IN", "KNOWS_CODE"],
  notes="Clue 2 of 2 for the safe. 'Well rested' warns of D07. CHECKED_IN is a debt in Act 3.")
N("O05", A, Z, "choice", "Lost property",
  "'Lost property is kept in the safe. The code is the year someone you lost was born.'",
  [("O06", "Try the safe"), ("O08", "Leave")])
N("O06", A, Z, "choice", "The safe",
  "A keypad. If you know the year, subtract 1800 and turn to that section. If you don't, guess.",
  [("SAFE", "Enter the year (computed: 1952 - 1800 = 152)", "hidden:KNOWS_CODE"), ("O07", "Guess")],
  notes="Classic number puzzle. SAFE is fixed at section 152.")
N("SAFE", A, Z, "item", "Unlocked",
  "Sam's passport - and Dad's old wristwatch, stopped at 05:59.",
  [("O19", "Continue")], gain=["PASSPORT"], notes="Passport route A. FIXED NUMBER 152.")
N("O07", A, Z, "choice", "Alarm",
  "A siren. The Night Manager unfolds from behind the desk.",
  [("O20", "Fight"), ("O08", "Run for the lifts")])
N("O08", A, Z, "choice", "The lifts",
  "The buttons run from 0 to a number too long to read.",
  [("O30", "Floor 4", "not:LIFT_SEEN"), ("O09", "Floor 4", "has:LIFT_SEEN"), ("O10", "Floor 0"), ("O15", "Basement laundry")])
N("O30", A, Z, "choice", "The lift comes back",
  "On Floor 4 the lift doors close behind you, then the numbers start climbing again. Something below has called it. The doors open on the floor you just left: it is inside, folded to fit. The corridor lights begin to flicker. Gain 1 Fear.",
  [("O09", "Hold its gaze until the doors close (add 1 to your Claim)"), ("O09", "Shut your eyes and back away down the corridor (gain 2 more Fear)")],
  gain=["LIFT_SEEN"], fear=1, notes="Second 'one room behind' encounter; uses the flicker rule again.")
N("O09", A, Z, "choice", "Corridor",
  "Identical doors. TV static behind all of them.",
  [("O11", "Room 1952", "has:ROOM_KEY"), ("O13", "Knock on a random door", "not:KNOCKED"), ("O27", "The ice machine", "not:ICE"), ("O08", "Back to the lifts")])
N("O10", A, Z, "choice", "Floor 0",
  "Dad's hospital room, exactly. The monitor beeps. Someone is in the bed. Sam (if present) whispers: 'That's not him. Don't.'",
  [("O14", "Sit with him"), ("O09", "Leave")])
N("O14", A, Z, "choice", "His voice",
  "It speaks in his voice. 'Stay a while. You didn't, last time.'",
  [("O16", "If you have TOLD: say goodbye properly", "has:TOLD"), ("O17t", "If you do not: test your Nerve", "not:TOLD")])
N("O16", A, Z, "item", "Goodbye",
  "You say it. The thing in the bed sighs and goes still, and lets go of the passport. If Sam was taken, Sam is asleep in the visitor's chair; you wake them. Lose 3 Fear.",
  [("O19", "Continue")], gain=["PASSPORT"], lose=["SAM_TAKEN"], fear=-3, notes="Passport route B; rescue route 1 (rescue does not itself grant TRUCE here; the goodbye does the work). Rewards TOLD.")
N("O17t", A, Z, "test", "Grab it", "Test your Nerve.",
  [("O17", "Success", "pass"), ("D06", "Failure", "fail")], test=dict(type="Nerve"))
N("O17", A, Z, "item", "Snatched", "You grab the passport from the bedside table and run. Gain 2 Fear.",
  [("O19", "Continue")], gain=["PASSPORT"], fear=2, notes="Passport route C.")
N("D06", A, Z, "death", "Visiting hours",
  "You sit back down. Just for a minute. Visiting hours never end on Floor 0.",
  [], warn="Rule 0 (A17): it keeps the ones who won't let go; Sam warns you; you were offered 'Leave'.", clue=["A17", "O10"], checkpoint="O10",
  notes="Fair: a safe 'Leave' option existed and a Nerve test gives a chance.")
N("O11", A, Z, "choice", "Room 1952",
  "Turned-down bed. On the pillow: Sam's passport. If Sam was taken, Sam is asleep in the bed.",
  [("O18", "Take the passport (and wake Sam) and go"), ("D07", "Lie down for a minute first")])
N("O18", A, Z, "item", "Checked", "Passport in hand. If Sam was here, Sam is awake and holding your sleeve.",
  [("O19", "Continue")], gain=["PASSPORT"], lose=["SAM_TAKEN"], notes="Passport route D; rescue route 2. If Sam was taken, waking him is coming back for him: the text tells you to note TRUCE.")
N("D07", A, Z, "death", "Turndown service",
  "The mattress is so soft. Somewhere a cart squeaks to a stop outside the door.",
  [], warn="Rule 6: Do not sleep airside; the Manager said 'well rested'.", clue=["A15", "O03"], checkpoint="O11")
N("O12", A, Z, "anomaly", "Stairwell",
  "Floor signs as you descend: 3, 2, 1, 1.",
  [("O08", "That's wrong - turn back"), ("O15", "Keep going down"), ("O08", "Shine the torch: the signs are wrong", "has:TORCH")])
N("O13", A, Z, "test", "Random door", "Your childhood bedroom. Test your Fortune.",
  [("O22", "Lucky", "pass"), ("O23", "Unlucky", "fail")], gain=["KNOCKED"], test=dict(type="Fortune"))
N("O22", A, Z, "item", "Under the bed", "Your old first-aid tin. (Restore 6 Vigour once.)", [("O09", "Continue")], gain=["FIRST_AID"])
N("O23", A, Z, "story", "Under the bed", "Something under the bed catches your wrist. Lose 3 Vigour.", [("O09", "Continue")], vig=-3)
N("O27", A, Z, "choice", "Ice machine",
  "The ice cubes have teeth in them. Sam (if present) grabs your arm, shaking.",
  [("O28", "Hold Sam until it passes"), ("O09", "Shake Sam off and keep going")], gain=["ICE"], fear=1)
N("O28", A, Z, "story", "Held",
  "Neither of you says anything. You don't need to. Codeword TRUCE (if you didn't have it already).",
  [("O09", "Continue")], gain=["TRUCE"], notes="Second route to TRUCE - a redemption chance for readers who chose coldly in A08.")
N("O15", A, Z, "choice", "Laundry",
  "Endless tumbling machines full of uniforms. Staff folding.",
  [("O24", "Steal a uniform"), ("O25", "Hide in a laundry cart")])
N("O24", A, Z, "item", "Uniform", "It fits perfectly. Gain 1 Fear.", [("O25", "Continue")], gain=["UNIFORM"], fear=1,
  notes="Helps in G09; must be removed in G36 or you get the Ground Crew ending.")
N("O25", A, Z, "story", "Overheard",
  "Wheeled up to the lobby in the dark, you hear the Manager: 'Guests are always found where they sleep.'",
  [("O01", "Continue")], notes="Clue: Sam (if taken) is in Room 1952.")
N("O26", A, Z, "choice", "Hotel bar",
  "A bartender pours a drink and slides it over. 'On the house.'",
  [("O29", "Drink it"), ("O01", "Leave it")], gain=["BAR"])
N("O29", A, Z, "story", "On the house", "Warmth spreads through you. Gain 3 Vigour. Codeword FED.", [("O01", "Continue")], gain=["FED"], vig=3,
  notes="Rule 4 broken: a debt, not a death.")
N("O19", A, Z, "story", "Hotel cleared",
  "The skybridge back to the terminal. If you checked in, a voice calls after you: 'Checkout by six.' Codeword CLEARED_O.",
  [("H02", "Return to the Atrium")], gain=["CLEARED_O"])
N("O20", A, Z, "combat", "Night Manager", "",
  [("O21", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")], test=dict(type="combat", foe="NIGHT MANAGER", nerve=9, vig=10))
N("O21", A, Z, "item", "The ledger", "Tucked in his ledger: Sam's passport.", [("O19", "Continue")], gain=["PASSPORT"], notes="Passport route E.")

# ======================================================================
# ACT 3 - FINAL BOARDING
# ======================================================================
A, Z = 3, "Gate 0"
N("G43", A, Z, "choice", "The crossing",
  "05:00. The Atrium goes dark. The tall passenger stands between you and Gate 0, under the departures board, sign held high. The lights begin to flicker.",
  [("D10", "Run for Gate 0 in the dark"),
   ("G01", "Shut your eyes and walk, holding Sam (only if you have TRUCE and Sam is with you; gain 2 Fear)", "has:TRUCE&not:SAM_TAKEN"),
   ("G01", "Read the names on its sign aloud as you pass (only if you have READ_INCIDENT)", "has:READ_INCIDENT"),
   ("G01", "Walk with your eyes on it the whole way (add 1 to your Claim)")],
  notes="The low point before Act 3 on every route, and a set piece that pays off the unstated rule from C37.")
N("D10", A, Z, "death", "In the dark",
  "You run. The lights stutter, and in each dark beat it is nearer, until in one of them it isn't in front of you any more.",
  [], warn="Rule 1: it moves when the lights flicker - running in the dark gives it every flicker.", clue=["A15", "G43"], checkpoint="G43")
N("G01", A, Z, "story", "Gate 0",
  "05:00. Gate 0 is real, and lit. The Hostess waits at the desk.",
  [("G26", "Continue", "has:SAM_TAKEN"), ("G32", "Continue", "not:SAM_TAKEN")])
N("G26", A, Z, "choice", "Sam's voice",
  "Sam's voice comes from the Gate 00 jet bridge across the hall: 'Don't leave me here.'",
  [("H01", "Go back and search the hotel"), ("G41", "Follow the voice with your eyes on the floor"), ("D08", "Run straight into Gate 00"), ("E_ALONE", "Board alone")])
N("G41", A, Z, "test", "Eyes down",
  "Rule 1 and Rule 5 both scream at you. Test your Nerve.",
  [("G42", "Success", "pass"), ("D08", "Failure", "fail")], test=dict(type="Nerve"))
N("G42", A, Z, "story", "Found",
  "Sam is curled up just inside the door, which is not a jet bridge at all but a storage cupboard. You drag them out before it remembers what it is.",
  [("G32", "Continue")], lose=["SAM_TAKEN"], gain=["TRUCE"], notes="Rescue route 3. Coming back for him counts: TRUCE.")
N("D08", A, Z, "death", "Gate 00",
  "There is no Gate 00. There is no you, either.",
  [], warn="Handbook Rule 5.", clue=["A15"], checkpoint="G26")
N("G32", A, Z, "test", "The queue",
  "The Delayed rise from every seat and form a queue to the desk. Test your Nerve to push through.",
  [("G02", "Success", "pass"), ("G33", "Failure", "fail")], test=dict(type="Nerve"))
N("G33", A, Z, "story", "Crushed", "The queue presses. Lose 3 Vigour before you reach the desk.", [("G02", "Continue")], vig=-3)
N("G02", A, Z, "choice", "One pass",
  "Beep. 'Two passengers. One pass.'",
  [("G03", "Give Sam the pass"), ("G04", "Keep it"), ("G05", "Read her the last page")])
N("G03", A, Z, "story", "Sam's turn",
  "You hold out the pass.",
  [("G05", "If you have TRUCE: Sam refuses to go without you", "has:TRUCE"), ("E_GROUNDCREW", "If not: Sam takes it", "not:TRUCE")])
N("G04", A, Z, "choice", "For one",
  "'Boarding for one.' The jet bridge opens. Sam doesn't say a word.",
  [("G02", "Turn back"), ("E_ALONE", "Walk on")])
N("G05", A, Z, "story", "Rule 8",
  "'...once every debt is settled.' The Hostess smiles properly for the first time. 'Then let's settle them.'",
  [("G06", "Continue")])
N("G06", A, Z, "story", "The ledger",
  "The Hostess opens a ledger and runs her finger down your debts, one line at a time.",
  [("G07", "If you have FED", "has:FED"),
   ("G09", "If you do not have FED but have CHECKED_IN", "not:FED&has:CHECKED_IN"),
   ("G11", "If you have neither FED nor CHECKED_IN, but have MARKED", "not:FED&not:CHECKED_IN&has:MARKED"),
   ("G14", "If you have none of these", "not:FED&not:CHECKED_IN&not:MARKED")],
  notes="One looping ledger section replaces three routing sections; every settlement returns here.")
N("G07", A, Z, "choice", "The bill",
  "The Chef appears with a bill.",
  [("G28", "Pay with your voucher", "has:VOUCHER"), ("G27", "Give it back")])
N("G28", A, Z, "story", "Paid", "He tears up the bill.", [("G06", "Continue")], lose=["FED", "VOUCHER"])
N("G27", A, Z, "story", "Returned", "It comes back up, all of it. Lose 3 Vigour.", [("G06", "Continue")], lose=["FED"], vig=-3)
N("G09", A, Z, "choice", "Checkout",
  "The Night Manager, with a pen. 'Your real name, please.'",
  [("G29", "Return the key and sign", "has:ROOM_KEY"), ("G30", "Flash the staff uniform", "has:UNIFORM")])
N("G29", A, Z, "story", "Checked out", "Your name goes into the ledger beside a thousand others. Gain 1 Fear.",
  [("G06", "Continue")], lose=["CHECKED_IN", "ROOM_KEY"], fear=1)
N("G30", A, Z, "story", "Colleague", "He nods to you as one of his own. That should worry you.",
  [("G06", "Continue")], lose=["CHECKED_IN"])
N("G11", A, Z, "choice", "Paged again",
  "The Announcer calls Sam's name. Sam answered once. Sam starts walking toward Gate 00.",
  [("G06", "If you have TRUCE: hold Sam and say his name, louder", "has:TRUCE"), ("G31", "Grab Sam")], lose=["MARKED"])
N("G31", A, Z, "test", "Hold on", "Test your Nerve.", [("G06", "Success", "pass"), ("G12", "Failure", "fail")], test=dict(type="Nerve"))
N("G12", A, Z, "choice", "The Announcer",
  "Sam slips free. Between you and Gate 00 stands the Announcer: a uniform with a PA speaker where the face should be.",
  [("G13", "Fight it")])
N("G13", A, Z, "combat", "The Announcer", "",
  [("G06", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")],
  test=dict(type="combat", foe="THE ANNOUNCER", nerve=9, vig=12))
N("G14", A, Z, "story", "Settled",
  "'All debts settled.' The Hostess stamps both of your names onto the one pass.",
  [("G34", "Continue", "has:PROMISE"), ("G38", "Continue", "not:PROMISE")])
N("G34", A, Z, "story", "Walter",
  "The PA handset at the desk rings. You know who it is. You lift it and say his daughter's name, and that he tried. Lose 2 Fear.",
  [("G38", "Continue")], fear=-2, notes="Pays off PROMISE.")
N("G38", A, Z, "story", "Final call",
  "'Final call for flight LV 137.' Sam's hand finds yours.",
  [("G36", "Continue", "has:UNIFORM"), ("G15", "Continue", "not:UNIFORM")])
N("G36", A, Z, "choice", "The uniform",
  "The jet bridge door won't open for staff.",
  [("E_GROUNDCREW", "If you have FORGOT: the uniform will not come off", "has:FORGOT"),
   ("G15", "Take the uniform off", "not:FORGOT"), ("E_GROUNDCREW", "Keep it on. You would never have to leave anywhere again", "not:FORGOT")], lose=["UNIFORM"],
  notes="Ground Crew is now earned: forced if you sold Dad's voice, tempting otherwise.")
N("G15", A, Z, "choice", "The jet bridge",
  "The jet bridge, described feature by feature. Rule 7: if something is wrong, turn back; if nothing is, walk on. Three clean walks and it lets you through.",
  [("G16", "Begin"), ("G37", "Shine the torch first", "has:TORCH")])
N("G37", A, Z, "story", "Torchlight",
  "In torchlight the bridge's seams show. You'll see the wrongness more clearly. Lose 1 Fear.",
  [("G16", "Begin")], fear=-1)
N("G16", A, Z, "anomaly", "Bridge walk 1", "Carpet, windows, the hum of the aircraft. Everything as it should be.",
  [("G17", "Keep walking"), ("G19", "Turn back")])
N("G17", A, Z, "anomaly", "Bridge walk 2", "Dad's coat, hanging on a hook that wasn't there.",
  [("G18", "Turn back"), ("G19", "Keep walking")])
N("G18", A, Z, "anomaly", "Bridge walk 3", "The Larkvale poster family - mother, father, two children waving at the window - has no faces.",
  [("G20", "Turn back"), ("G19", "Keep walking")])
N("G19", A, Z, "choice", "Reset",
  "The bridge resets. Gain 2 Fear.",
  [("G16", "Walk it again"), (F, "If your Fear has reached its limit", "fearlimit")], fear=2)
N("G20", A, Z, "choice", "The aircraft door",
  "In the doorway, wearing his coat and his face, stands Dad.",
  [("G21", "Tell the truth, out loud, to him"), ("G22", "Attack it"), ("G23", "Walk past it")])
N("G21", A, Z, "story", "Said aloud", "",
  [("G24", "If you have TOLD", "has:TOLD"),
   ("G24", "If you do not have TOLD but have TRUCE: Sam hears it for the first time, and stays", "not:TOLD&has:TRUCE"),
   ("G25", "If you have neither", "not:TOLD&not:TRUCE")])
N("G25", A, Z, "story", "Alone with it",
  "'You let me do it alone,' Sam says, and walks back up the bridge.",
  [("E_SEPARATE", "Continue")])
N("G22", A, Z, "combat", "The thing in Dad's coat", "",
  [("G23", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")], test=dict(type="combat", foe="THE PASSENGER", nerve=10, vig=14),
  notes="Winning the fight doesn't resolve grief: it leads to the Loop ending.")
N("G23", A, Z, "story", "Walked past",
  "'See you on the return flight,' it says.",
  [("E_LOOP", "Continue")])
N("G24", A, Z, "story", "Seats 0A and 0B",
  "You sit. Sam leans on your shoulder. If you have TRANSFER and never gave away Dad's voice, you know what to do with your flight number.",
  [("SECRET", "Turn to your flight number", "hidden:TRANSFER&not:FORGOT"), ("G40", "Otherwise, continue")])
N("G40", A, Z, "story", "Takeoff",
  "The aircraft pushes back. Out of the window the terminal is just a terminal, empty and ordinary.",
  [("G39", "Continue", "has:PROMISE"), ("E_ARRIVAL", "Continue", "not:PROMISE")])
N("G39", A, Z, "story", "Arrivals",
  "At arrivals, an old woman holds a sign with Walter's name. You tell her.",
  [("E_ARRIVAL", "Continue")])

# ---------------- ENDINGS -----------------
N("E_ARRIVAL", 3, "Ending", "ending", "ENDING: Arrival (true ending)",
  "Dawn. You land. At the funeral, Sam stands next to you, and leans. Section 200.", [],
  notes="FIXED NUMBER 200.")
N("SECRET", 3, "Ending", "ending", "ENDING: Connection (secret)",
  "In seat 1A a man turns round. He has your father's voice, and it is him. You both get to say it. Then he gets off, and you take off.", [],
  notes="FIXED NUMBER 137. Never linked; reached only by the flight-number instruction.")
N("E_SEPARATE", 3, "Ending", "ending", "ENDING: Separate Seats",
  "You both get home. Rows apart on the plane; the far side of the coffin at the funeral. The voicemail stays unplayed because he won't sit next to you to hear it.", [])
N("E_ALONE", 3, "Ending", "ending", "ENDING: Alone",
  "You land. Sam's seat is empty. At the funeral you stand by yourself and keep checking your phone.", [])
N("E_GROUNDCREW", 3, "Ending", "ending", "ENDING: Ground Crew",
  "Sam boards. The uniform fits you perfectly. You'll be very good at smiling.", [])
N("E_LOOP", 3, "Ending", "ending", "ENDING: Delayed Indefinitely",
  "The board flips back. 11:52pm. DELAYED. Sam sits two seats away. Start again from section 1 - but something has changed.", [])
N(F, 3, "Ending", "ending", "ENDING: Final Call (Fear limit)",
  "The Announcer's voice is the only thing you can hear. Then it is your voice.", [],
  notes="Global rule: turn here whenever Fear reaches its limit (Nerve + 3).")
N(V, 3, "Ending", "death", "Vigour gone",
  "You sit down on the carpet and can't get up. A cleaning cart rolls toward you.", [],
  warn="Vigour is always visible on the adventure sheet.", checkpoint="LAST",
  notes="Global rule: Vigour 0. Story Mode readers restart at their last checkpoint section.")

# ======================================================================
# v3 STRUCTURAL EDITS (round-3 reviews)
# ======================================================================
_K = {s["key"]: s for s in S}
def _L(*links): return [dict(to=l[0], label=l[1], cond=(l[2] if len(l) > 2 else None)) for l in links]
def _drop(key):
    S.remove(_K.pop(key))
def _retarget(old, new):
    for s in S:
        for l in s["links"]:
            if l["to"] == old: l["to"] = new

# 1. Sam's arc: Act 1 earns THAW, not TRUCE. TRUCE now comes mid-book (H12, O28, G42).
_K["A09"]["gain"] = ["THAW"]
_K["A09"]["beat"] = _K["A09"]["beat"].replace("Codeword TRUCE.", "Codeword THAW.")
_K["A09"]["notes"] = "THAW: a first softening. TRUCE is earned later (H12, O28, G42)."
_K["C11"]["links"] = _L(("C13", "If Sam is with you and you have TRUCE", "has:TRUCE&not:SAM_TAKEN"),
                        ("C13", "If Sam is with you and you have THAW", "has:THAW&not:TRUCE&not:SAM_TAKEN"),
                        ("C14", "If Sam is with you and you have neither", "not:TRUCE&not:THAW&not:SAM_TAKEN"),
                        ("C18", "If you have LOST", "has:SAM_TAKEN"))
# CARE: acts of care for Sam count, not only words.
_K["A27"]["gain"] = ["MARKED", "CARE"]
_K["F17"]["gain"] = ["CARE"]
_K["F17"]["beat"] = "You don't eat, and you catch Sam's wrist before he does. Your head swims. Lose 1 Vigour. Codeword CARE."
_K["H11"]["links"] = _L(("H12", "Tell him you should have come anyway"),
                        ("H12", "If you have CARE: give him your own phone and say nothing", "has:CARE"),
                        ("H13", "Tell him he never asked you to"))
N("H13", 2, "Atrium", "story", "He didn't",
  "Sam answers the charge. 'No. I didn't.' He flinches at his own line from three years ago, owns it, and does not apologise. No codeword: the door stays half open.",
  [("H01", "Continue")], notes="Gives the reader's side its reply (R5).")

# 2. Hub: H02 goes straight to the choices on later visits (no H01 re-read).
_K["H02"]["links"] = _L(("H05", "Continue", "not:ECHO"), ("H03", "Continue", "has:ECHO&not:OFFERED"),
    ("C01", "The Concourse", "has:ECHO&has:OFFERED"), ("F01", "Duty-Free and the Food Court", "has:ECHO&has:OFFERED"),
    ("O01", "The hotel", "has:ECHO&has:OFFERED"),
    ("H04", "The information desk", "has:ECHO&has:OFFERED&not:LF_USED"),
    ("G43", "Gate 0 (only if you hold all three)", "has:ECHO&has:OFFERED&has:BOARDING_PASS&has:PASSPORT&has:LAST_PAGE"))

# 3. Claim bites: Claim 3+ is called to account at the ledger.
_K["G06"]["links"].insert(0, dict(to="G44", label="If your Claim is 3 or more and you do not have SIGNED", cond="claim3&not:SIGNED"))
N("G44", 3, "Gate 0", "choice", "Your name, nearly",
  "The Hostess turns the ledger round. At the bottom, your name, most of it, in the tall passenger's hand. It has to be settled before you board. Codeword SIGNED.",
  [("G06", "If you have TRUCE: Sam reads your name aloud with you, and you cross off 2 letters of Claim", "has:TRUCE"),
   ("G06", "If you have CARE: Sam takes the pen and crosses it out himself; cross off 2 letters of Claim", "not:TRUCE&has:CARE"),
   ("G45", "Otherwise: let the airport take something else instead", "not:TRUCE&not:CARE")],
  gain=["SIGNED"], notes="Claim consequence (R1/R2/R4).")
N("G45", 3, "Gate 0", "story", "Something else",
  "She takes the sound of how he said your name. You try to remember it and can't. Cross off 2 letters of Claim. Codeword FORGOT.",
  [("G06", "Continue")], gain=["FORGOT"])

# 4. Fights become chases with a cost.
_K["A35"].update(kind="test", test=dict(type="Nerve"),
                 links=_L(("A37", "Success: you outrun it", "pass"), ("A37", "Failure: lose 4 Vigour and add 1 to your Claim", "fail")))
_K["F13"].update(kind="test", test=dict(type="Nerve"),
                 links=_L(("F11", "Success: you get past them", "pass"), ("F11", "Failure: lose 4 Vigour and gain 1 Fear", "fail")))

# 5. Checkpoints further back (deaths cost a re-read, not just a re-pick).
for d, cp in {"D01": "A21", "D02": "A31", "D03": "C01", "D05": "F02", "D04": "F15", "D09": "F15", "D07": "O09"}.items():
    _K[d]["checkpoint"] = cp

# 6. Merges to stay at 200: C15, F20, G12.
_retarget("C15", "C18"); _drop("C15")
_retarget("F20", "F14"); _drop("F20")
_retarget("G12", "G13"); _drop("G12")
_K["C14"]["links"] = _L(("C18", "Success", "pass"), ("C17", "Failure", "fail"))

# ======================================================================
# v3.1 FIX PASS (round-3 reviews)
# ======================================================================
_K = {s["key"]: s for s in S}
# CARE rewards stopping Sam answering the page (A26), not letting him (A27).
_K["A27"]["gain"] = ["MARKED"]
_K["A26"]["gain"] = list(_K["A26"]["gain"]) + ["CARE"]
# Crossing: CARE also lets you walk Sam across blind; a Nerve-test option for every reader (the LOST trap).
_K["G43"]["links"] = _L(("D10", "Run for Gate 0 in the dark"),
    ("G01", "Shut your eyes and walk, holding Sam (only if you have TRUCE and Sam is with you; gain 2 Fear)", "has:TRUCE&not:SAM_TAKEN"),
    ("G01", "Shut your eyes and walk, holding Sam (only if you have CARE but not TRUCE, and Sam is with you; gain 3 Fear)", "has:CARE&not:TRUCE&not:SAM_TAKEN"),
    ("G01", "Read the names on its sign aloud as you pass (only if you have INCIDENT)", "has:READ_INCIDENT"),
    ("G46", "Stand still and wait for the lights to hold"),
    ("G01", "Walk with your eyes on it the whole way (add 1 to your Claim)"))
N("G46", 3, "Gate 0", "test", "Steady",
  "You wait in the dark while it comes closer with every flicker, until the lights hold for a breath and you walk. Test your Nerve.",
  [("G01", "Success", "pass"), ("D10", "Failure", "fail")], test=dict(type="Nerve"),
  notes="A Claim-free crossing for every reader, at the risk of D10 (fixes the LOST-route Final Call trap).")
# Ledger: fold G09 into G06; checkout clears SIGNED so a name signed after the reckoning is caught.
_K["G06"]["links"] = _L(("G44", "If your Claim is 3 or more and you do not have SIGNED", "claim3&not:SIGNED"),
    ("G07", "If you have FED", "has:FED"),
    ("G29", "If you do not have FED, but have CHECKED IN and the ROOM KEY", "not:FED&has:CHECKED_IN&has:ROOM_KEY"),
    ("G30", "If you do not have FED, but have CHECKED IN and the UNIFORM", "not:FED&has:CHECKED_IN&has:UNIFORM"),
    ("G11", "If you have neither FED nor CHECKED IN, but have MARKED", "not:FED&not:CHECKED_IN&has:MARKED"),
    ("G14", "If you have none of these", "not:FED&not:CHECKED_IN&not:MARKED"))
_drop("G09")
_K["G29"]["lose"] = ["CHECKED_IN", "ROOM_KEY", "SIGNED"]
_K["G29"]["beat"] = "The Night Manager, with a pen: 'Your real name, please.' You sign. Your name goes into the ledger beside a thousand others, and Sam sees it go in. Cross off SIGNED. Gain 1 Fear."
_K["G30"]["beat"] = "The Night Manager, with a pen, asks for your real name; you flash the staff uniform instead. " + _K["G30"]["beat"]
# v4: "Pull Sam away" only makes sense with Sam present.
for _l in _K["C10"]["links"]:
    if _l["to"] == "C12": _l["cond"] = "not:SAM_TAKEN"
# v4: G26's "search the hotel again" was a dead loop; the rescue is the way.
_K["G26"]["links"] = [l for l in _K["G26"]["links"] if l["to"] != "H01"]

# ======================================================================
# v5 STRUCTURAL EDITS (round-4 reviews)
# ======================================================================
_K = {s["key"]: s for s in S}
# 1. One Atrium hub: H02 is merged into H01. Zone exits route the one-time beats (H05, H03) themselves.
_TRIG = [("H05", "If you do not have RETURNED", "not:ECHO"), ("H03", "If you have RETURNED but not HEARD", "has:ECHO&not:OFFERED"),
         ("H01", "If you have RETURNED and HEARD", "has:ECHO&has:OFFERED")]
for _k in ("O19", "F14", "C18"):
    _keep = [l for l in _K[_k]["links"] if l["to"] != "H02"]
    _back = [l for l in _K[_k]["links"] if l["to"] == "H02"]
    _lab = _back[0]["label"] if _back else "Back to the Atrium"
    _K[_k]["links"] = _keep + _L(*[(t, f"{_lab} ({c})", cond) for t, c, cond in _TRIG])
for _l in _K["C35"]["links"]:
    if _l["to"] == "H02": _l["to"] = "H01"
_drop("H02")
_K["H01"]["notes"] = "The one Atrium hub (H02 merged in): return line first, the tall passenger's position by key items held, then the choices."
# 2. CARE for holding on at Gate 00.
for _l in _K["G31"]["links"]:
    if _l["cond"] == "pass": _l["to"] = "G47"
N("G47", 3, "Gate 0", "story", "Held",
  "You hold on. The page pulls at Sam's marked hand like a tide and you don't let it have him. Note the codeword CARE.",
  [("G06", "Continue")], gain=["CARE"], notes="Round-4 R5: the hardest act of care earns CARE.")
# 3. Crossing: failing the Nerve test costs Fear, not a death; G42's rescue takes a letter off.
for _l in _K["G46"]["links"]:
    if _l["cond"] == "fail": _l.update(to="G43", label="Failure: gain 2 Fear and turn back to the crossing")
_K["G42"]["beat"] += " Cross off 1 letter of your Claim."
# 4. G44 costs: TRUCE crosses off 1; CARE crosses off 2 but the sign takes Sam's hand (to G11).
_K["G44"]["links"] = _L(("G06", "If you have TRUCE: Sam reads your name aloud with you; cross off 1 letter of Claim and gain 1 Fear", "has:TRUCE"),
    ("G11", "If you have CARE: Sam takes the pen and crosses it out; cross off 2 letters of Claim, but the ink goes into his hand", "not:TRUCE&has:CARE"),
    ("G45", "Otherwise: let the airport take something else instead", "not:TRUCE&not:CARE"))
# 5. Checkout can be refused.
_K["G29"]["links"] = _L(("G06", "Sign: add 1 to your Claim and cross off SIGNED"), ("G06", "Refuse: slide the key back and keep your name; lose 3 Vigour"))
_K["G29"]["kind"] = "choice"

# ======================================================================
# v6 STRUCTURAL EDITS (round-5 reviews)
# ======================================================================
_K = {s["key"]: s for s in S}
# 1. Ledger queue shortened: G07 settles inline (G27/G28 merged); G29 takes the uniform option (G30 merged).
_K["G07"]["links"] = _L(("G06", "If you have the VOUCHER: pay with it; cross off FED and the VOUCHER", "has:VOUCHER"),
                        ("G06", "Give it back: lose 3 Vigour and cross off FED"))
_K["G07"]["lose"] = ["FED"]
_drop("G27"); _drop("G28")
_K["G29"]["links"] = _L(("G06", "Sign: add 1 to your Claim"),
                        ("G06", "Refuse: slide the key back and keep your name; lose 3 Vigour"),
                        ("G06", "If you have the UNIFORM: flash it, one of his own; gain 1 Fear", "has:UNIFORM"))
_K["G29"]["lose"] = ["CHECKED_IN", "ROOM_KEY"]
for _l in _K["G06"]["links"]:
    if _l["to"] == "G29": _l.update(cond="not:FED&has:CHECKED_IN", label="If you do not have FED, but have CHECKED IN")
_K["G06"]["links"] = [l for l in _K["G06"]["links"] if l["to"] != "G30"]
_drop("G30")
# 2. The jet bridge stops being a memory test: a failed walk tests Fortune; unlucky readers get a different bridge.
_K["G19"].update(kind="test", test=dict(type="Fortune"),
    links=_L(("G16", "Lucky: the bridge you know", "pass"), ("G48", "Unlucky: a bridge you don't", "fail"),
             ("E_FINALCALL", "If your Fear has reached its limit", "fearlimit")))
N("G48", 3, "Gate 0", "anomaly", "Second bridge 1",
  "The bridge again, but not the same one. The hum has stopped. Everything else is as it should be, and the silence is the wrong thing.",
  [("G19", "Keep walking"), ("G49", "Turn back")], notes="Wrong: the hum is gone. Correct: turn back.")
N("G49", 3, "Gate 0", "anomaly", "Second bridge 2",
  "Carpet, rail, windows, the bend, the hum. You look for the wrong thing and can't find it. It is the most frightening walk of the night.",
  [("G50", "Keep walking"), ("G19", "Turn back")], notes="Nothing is wrong. Correct: keep walking (beats readers who memorised 'turn back').")
N("G50", 3, "Gate 0", "anomaly", "Second bridge 3",
  "In the window, your reflection walks a half-step behind you. Sam's (if he is with you) doesn't.",
  [("G19", "Keep walking"), ("G20", "Turn back")], notes="Wrong: your reflection lags. Correct: turn back.")
# 3. Claim decides the secret ending.
for _l in _K["G24"]["links"]:
    if _l["to"] == "SECRET": _l["cond"] = "hidden:TRANSFER&not:FORGOT&claimlow"

# ======================================================================
# v7 STRUCTURAL EDITS (round-6 reviews)
# ======================================================================
_K = {s["key"]: s for s in S}
# HOURS bites: the sixth tick means the gate has closed.
for _k in ("C18", "C35", "F14", "O19"):
    _K[_k]["links"].insert(0, dict(to="E_FINALCALL", label="If you have just ticked your sixth hour", cond="hours6"))
# G44: the TRUCE discount no longer costs unavoidable Fear; it costs Sam something instead.
_K["G44"]["links"][0].update(label="If you have TRUCE: Sam reads your name aloud with you, and the sign says his once in return; cross off 2 letters of Claim")
# v7: Walter can only be met once he has given you his pass.
for _l in _K["C02"]["links"]:
    if _l["to"] == "C03": _l.update(cond="not:PROMISE", label="Talk to the old man (if you have not already promised him)")

# ======================================================================
# v8 STRUCTURAL EDITS (user's design choices after round 7)
# ======================================================================
_K = {s["key"]: s for s in S}
# 1. One-page reckoning: G06 settles food and checkout inline, then chains Claim -> MARKED -> Settled. No ledger re-reads.
_drop("G07"); _drop("G29")
_K["G06"]["links"] = _L(
    ("G44", "If your Claim is 3 or more", "claim3"),
    ("G11", "Otherwise, if you have MARKED", "has:MARKED"),
    ("G14", "Otherwise", "not:MARKED"))
_K["G06"]["lose"] = ["FED", "CHECKED_IN", "ROOM_KEY"]
_K["G06"]["notes"] = "One-page reckoning: every debt is settled inline (FED: voucher or 3 Vigour; CHECKED IN: sign for 1 Claim or refuse for 3 Vigour, or flash the UNIFORM for 1 Fear), then the Claim reckoning, then MARKED, then Settled. Read once."
# Everything that used to return to the ledger now continues down the chain instead.
_K["G44"]["links"] = _L(
    ("G45", "If your Claim is 4 or more: the ink won't take; there is too much of you on the sign", "claim4"),
    ("G11", "If you have TRUCE and MARKED: Sam reads your name aloud with you, and the sign says his once in return; cross off 2 letters of Claim", "has:TRUCE&has:MARKED"),
    ("G14", "If you have TRUCE but not MARKED: Sam reads your name aloud with you, and the sign says his once in return; cross off 2 letters of Claim", "has:TRUCE&not:MARKED"),
    ("G11", "If you have CARE but not TRUCE: Sam crosses it out and the ink goes into his hand; cross off 2 letters of Claim", "not:TRUCE&has:CARE"),
    ("G45", "Otherwise: let the airport take something else instead", "not:TRUCE&not:CARE"))
_K["G45"]["links"] = _L(("G11", "If you have MARKED", "has:MARKED"), ("G14", "Otherwise", "not:MARKED"))
for _k in ("G11", "G47", "G13"):
    for _l in _K[_k]["links"]:
        if _l["to"] == "G06": _l["to"] = "G14"
# 2. Claim 4 bars the true ending: the airport keeps you.
_K["G24"]["links"].insert(0, dict(to="E_GROUNDCREW", label="If your Claim is 4 or more", cond="claim4"))
# 3. The kind route pays late: on the bridge, the coat calls Sam; fail and you lose the TRUCE.
_K["G17"]["links"] = _L(("G51", "Turn back (if you have TRUCE)", "has:TRUCE"), ("G18", "Turn back (if you do not have TRUCE)", "not:TRUCE"), ("G19", "Keep walking"))
N("G51", 3, "Gate 0", "test", "The coat",
  "Sam has his hand flat on Dad's coat on the hook, and it is warm, and he will not take it away. Test your Nerve to wait it out with him.",
  [("G18", "Success: he lets go himself", "pass"), ("G52", "Failure", "fail")], test=dict(type="Nerve"),
  notes="Late cost on the kind route (R1): the truce can be lost here.")
N("G52", 3, "Gate 0", "story", "Let go",
  "You lift his hand off the sleeve yourself. He lets you, and doesn't look at you for the rest of the bridge. Cross off TRUCE. Gain 1 Fear.",
  [("G18", "Continue")], lose=["TRUCE"], fear=1)
# Claim 4+: nothing can be crossed out; the chain continues with your name intact.
_K["G44"]["links"] = _L(
    ("G11", "If your Claim is 4 or more and you have MARKED: the ink won't take; there is too much of you on the sign", "claim4&has:MARKED"),
    ("G14", "If your Claim is 4 or more and you do not have MARKED: the ink won't take; there is too much of you on the sign", "claim4&not:MARKED"),
) + [l for l in _K["G44"]["links"] if not (l["cond"] or "").startswith("claim4")]
# v8: holding Sam's hand across the dark costs less than before.
for _l in _K["G43"]["links"]:
    if "TRUCE and Sam" in _l["label"]: _l["label"] = _l["label"].replace("gain 2 Fear", "gain 1 Fear")
    if "CARE but not TRUCE" in _l["label"]: _l["label"] = _l["label"].replace("gain 3 Fear", "gain 2 Fear")

# ======================================================================
# v8.1 PRE-BUILD FIXES (round-8 reviews)
# ======================================================================
_K = {s["key"]: s for s in S}
# G51 becomes a real choice, not a dice roll (R5).
_K["G51"].update(kind="choice", test=None, links=_L(
    ("G18", "Wait with him, however long it takes (gain 2 Fear)"),
    ("G52", "Lift his hand off the coat yourself")))
_K["G51"]["beat"] = "Sam has his hand flat on Dad's coat on the hook, and it is warm, and he will not take it away. Every flicker, the bridge gets longer. Choose."
# Claim reckoning removes ONE letter, never two, so a higher Claim can't finish lower than a lesser one (R2).
for _l in _K["G44"]["links"]:
    _l["label"] = _l["label"].replace("cross off 2 letters of Claim", "cross off 1 letter of Claim")
_K["G44"]["gain"] = []      # SIGNED was never used again (R1)
_K["G45"]["beat"] = _K["G45"]["beat"].replace("Cross off 2 letters of Claim", "Cross off 1 letter of Claim")

# ======================================================================
# v9 FINE-TOOTH AUDIT FIXES (structural)
# ======================================================================
_K = {s["key"]: s for s in S}
for _l in _K["H01"]["links"]:
    if _l["to"] == "F01": _l.update(cond="not:LAST_PAGE", label="Duty-Free and the Food Court (if you do not yet have the last page)")
    if _l["to"] == "O01": _l.update(cond="not:PASSPORT", label="The Airport Hotel (if you do not yet have the passport)")
for _l in _K["O02"]["links"]:
    if _l["to"] == "O03": _l.update(cond="not:CHECKED_IN", label="Check in (if you have not already)")
_K["O08"]["links"].append(dict(to="O01", label="Step back out into the lobby", cond=None))
for _l in _K["F02"]["links"]:
    if _l["to"] == "F28": _l.update(cond="not:READ_PAPER", label="Look at the newspapers (if you have not already)")
_K["C10"]["links"].append(dict(to="C18", label="Turn your back on the window and walk away", cond=None))
for _l in _K["C06"]["links"]:
    if _l["to"] == "C07": _l.update(cond="not:BOARDING_PASS", label="Approach the desk (if you do not have a boarding pass)")

# v9.1 coverage-playtest fixes (structural)
_K = {s["key"]: s for s in S}
_K["C35"]["links"] = _L(
    ("E_FINALCALL", "If you have just ticked your sixth hour", "hours6"),
    ("H05", "Back to the Atrium (watch the doorway: add 1 to your Claim; or walk blind: gain 1 Fear) - if you do not have RETURNED", "not:ECHO"),
    ("H03", "Back to the Atrium (watch the doorway: add 1 to your Claim; or walk blind: gain 1 Fear) - if you have RETURNED but not HEARD", "has:ECHO&not:OFFERED"),
    ("H01", "Back to the Atrium (watch the doorway: add 1 to your Claim; or walk blind: gain 1 Fear) - if you have RETURNED and HEARD", "has:ECHO&has:OFFERED"))
for _l in _K["H05"]["links"]:
    if _l["to"] == "H01": _l.update(cond="has:SAM_TAKEN", label="Otherwise")
for _l in _K["O15"]["links"]:
    if _l["to"] == "O24": _l.update(cond="not:UNIFORM", label="Steal a uniform (if you do not already have one)")
for _l in _K["H04"]["links"]:
    if _l["to"] == "H09": _l.update(cond="not:TRANSFER", label="Take the luggage tag that has your name on it (if you do not have TRANSFER)")
