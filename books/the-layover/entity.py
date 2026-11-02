"""
THE MANIFEST - the entity, its rules, its lore trail and its Claim track.
Applied on top of story.py (no new sections: the book stays at exactly 200).

Design basis (see strategy doc for sources):
- Creepiness = ambiguity of threat (McAndrew & Koehnke 2016): it is polite, helpful, never openly hostile.
- Uncanny cue: a happy mouth with frightened eyes is the eeriest face (MacDorman, Open University).
- Category violation (Carroll): one body / many people; staff / passenger; dead / waiting; overcomplete (too many hands).
- Dread beats the event (Berns 2006): a visible countdown - the Claim track spelling your name.
- Information gap (Loewenstein): ask the question first, give partial answers, split lore across runs.
- Morbid curiosity (Scrivner): learning about a threat is rewarding - every lore fragment is also a survival tip.
- Predictive processing: learnable rules, then one late rule-break to reset the reader's predictions.
"""

ENTITY = dict(
    name="The Manifest",
    early_name="the tall passenger",
    what=("The 137 passengers of flight LV 137, who waited at Gate 0 one night in 1998 until the waiting ate them. "
          "Now they stand inside one long coat, too tall, holding a handwritten sign. Their faces press against the cloth from inside. "
          "It wears the face and voice of whoever you are grieving. The smile is right. The eyes are frightened, because the people inside are still afraid."),
    wants=("Names. It completes itself by adding the names of people who never said goodbye. "
           "One seat has been empty since 1998: 1A, booked in your father's name. He never boarded. Now it wants his children instead."),
    rules=[
        ("It needs your name, given freely.", "Answering a page, signing, checking in, a voucher logged in your name: each adds a letter to its sign (the Claim track)."),
        ("It only moves when the lights flicker.", "While you watch it, it cannot move. But watching teaches it your face (+1 Claim)."),
        ("It wears whoever you miss.", "The tell: the smile is right but the eyes are frightened, and it calls you by your full name. The real person never did."),
        ("It cannot enter a place where a goodbye was said.", "The prayer room, and Floor 0 once you have said goodbye, are safe."),
        ("It is always one room behind you.", "Every return to the Atrium, it is closer. In Act 3 it is waiting at the gate."),
    ],
    breaks_rule=("Once, late in Act 3 (G26), it moves while the lights are steady - because it is wearing Sam's voice, and you want to look. "
                 "The rule-break resets the reader's predictions just before the finale."),
)

# Claim: letters of your name on its sign. At 5, turn to E_FINALCALL ('Final Call').
CLAIM_LIMIT = 5

# Section updates: beat rewrites, lore fragments, Claim changes.
# lore = (id, short title, text, what question it opens or answers)
U = {
"A01": dict(beat="Gate 14, 11:52pm. You and Sam, the sibling you haven't spoken to in three years, are flying home for your father's funeral. Flight LV 137. At the far end of the concourse, a very tall passenger is holding up a name sign. It's too far away to read."),
"A07": dict(beat="You watch the terminal die zone by zone, lights clicking off toward you. In the last lit gate, the tall passenger is still holding its sign. When the lights go, Sam wakes. When they come back, it is two gates closer."),
"A11": dict(beat="A woman in an immaculate uniform, a 1990s cut. Name badge: HOSTESS. Her smile is perfect. Her eyes are terrified. 'Complimentary voucher? I'll just need your name.'",
            notes="Uncanny cue from the research: happy mouth, frightened eyes. First appearance of the tell."),
"A12": dict(beat="You give your name. She types it, and somewhere a printer starts. VALID UNTIL DEPARTURE. DO NOT LEAVE THE TERMINAL. Add 1 to your Claim.", claim=1,
            notes="First Claim. Teaches that giving your name has a cost."),
"A15": dict(lore=("L1", "The Handbook's cover", "IRREGULAR OPERATIONS HANDBOOK - LV 137 CREW - EDITION 1998. Why would tonight's flight have a crew handbook from 1998?", "Opens: what happened in 1998?"),
            beat="Under a seat: a laminated booklet. IRREGULAR OPERATIONS HANDBOOK - LV 137 CREW - EDITION 1998. Rule 1: Do not look at the passenger when the lights flicker. 2: Never answer the Announcer; never give your name. 3: Never ride a walkway that runs backwards. 4: Do not eat or drink airside after midnight. 5: Gate 00 does not exist. 6: Do not sleep airside. 7: If something is wrong, turn back. The last page is torn out."),
"A17": dict(beat="Scratched into the back cover, in biro: RULE 0 - IT KEEPS THE ONES WHO NEVER SAID GOODBYE. And beneath it, in different handwriting: IT CAN'T COME WHERE ONE WAS SAID. Sam goes quiet. Lose 1 Fear.",
            lore=("L2", "Rule 0", "It keeps the ones who never said goodbye - and it can't come where one was said.", "Survival tip: safe rooms exist. Opens: goodbye to whom?")),
"A18": dict(beat="The lights stutter. In the dark between flickers, the tall passenger has crossed half the concourse. It is facing you."),
"A19": dict(beat="You look. It's too tall because it's more than one person: faces press out through the cloth of its coat. Too many hands hold the sign. The sign has names on it, crossed out, dozens of them - and at the bottom, the first letter of yours, fresh. Lose 2 Vigour, gain 2 Fear, add 1 to your Claim.",
            claim=1, lore=("L3", "The sign", "It is taller than one person should be. Its sign is a list of names, and yours has started.", "Opens: whose names, and what is it? Survival tip: looking feeds it."),
            notes="Exclusive with A20: a reader who keeps their eyes shut never sees this. Split lore drives replays."),
"A20": dict(beat="You keep your eyes shut. Something passes close enough to feel: many breaths, slightly out of time. Sam's hand finds yours in the dark."),
"A24": dict(beat="The PA, calm and kind, in a voice you almost recognise: 'Passenger...' and it says your full name. 'Please make yourself known.'"),
"A27": dict(beat="'Here,' Sam says. Every light goes out, and in the dark you hear a pen scratching. You drag Sam behind a pillar while something heavy passes. Lose 3 Vigour. Codeword MARKED."),
"A30": dict(beat="A grey passenger, half grown into the chair. 'To board you need three things. The true pass. The papers. The last page.' Its eyes open. 'And when it wears someone you love, look at the eyes. The eyes are us.'",
            lore=("L4", "The eyes", "When it wears someone you love, look at the eyes.", "Survival tip: how to spot its disguise. Deliberately unexplained."),
            notes="Exclusive with A29 (map)."),
"A32": dict(beat="Sam talks. Dad was born in 1952, 'the year the old terminal opened.' Then: 'Did you know he never flew again after '98? He was booked on a trip and turned round at the gate. Said he had to get home to us.' Sam was with him at the end. You weren't. Gain 2 Vigour.",
            lore=("L5", "Dad's flight", "In 1998 Dad was booked on a flight, turned back at the gate, and never flew again.", "Opens: which flight? (The reader may already suspect.)"),
            notes="Exclusive with A33."),
"A38": dict(beat="The central Atrium. The great departures board lists cities that don't exist. One line holds steady: LV 137 - FINAL BOARDING - GATE 0 - 05:59. Under STATUS, it says: AWAITING 2 PASSENGERS."),

"H02": dict(beat="The Atrium has changed while you were gone: one more escalator than before. On the board, AWAITING 2 PASSENGERS. The tall passenger is standing at the far end of the Atrium, closer than last time. It is holding its sign a little higher."),
"H05": dict(beat="The board flips through every city, then settles: 05:59 is a little closer. Beside it, a flight-tracker screen shows the terminal from above: two dots for you and Sam, and a third dot, always one room behind. Codeword ECHO.",
            lore=("L6", "Three dots", "It is always one room behind you.", "Survival tip: keep moving; it follows, it doesn't lead.")),
"H03": dict(beat="The Announcer, softly, just to you, in your father's voice: 'Leave Sam with us and you may board now.' It uses your full name. He never did."),
"H09": dict(beat="TRANSFER. Underneath, handwritten: 'Your connection is your flight number. Seat 1A has been held since 1998.' Codeword TRANSFER.",
            lore=("L7", "Seat 1A", "Seat 1A has been held since 1998.", "Opens: held for whom?")),

"C02": dict(beat="Every seat is taken by the Delayed, motionless, in clothes from 1998. One old man turns his head."),
"C03": dict(beat="Walter has waited since 1998. He was on LV 137. 'The captain kept saying a short delay. By three in the morning people stopped asking. By four, they started... joining up.' His daughter was meeting him at arrivals. 'If you get out, tell her I tried.'",
            lore=("L8", "Walter", "LV 137's passengers waited so long they started 'joining up'. He won't say into what.", "Half-answers: what it is made of. Opens: why is it still here?")),
"C10": dict(beat="The windows show no night - only white. Out on the apron, a man in Dad's coat is waving you over. Even from here you can see he is smiling. Even from here you can see his eyes are wrong. At the jet bridge door, Sam won't touch the handle."),
"C11": dict(beat="It is him, almost. He says your full name through the glass. The glass is freezing. Sam is crying. Gain 2 Fear, add 1 to your Claim.", claim=1),
"C19": dict(beat="Grainy news from 1998: 'Flight LV 137 was found at its gate this morning, doors closed. None of its 137 passengers have been located.' The anchor turns slowly and looks straight out of the screen. Gain 1 Fear.",
            lore=("L9", "1998 broadcast", "LV 137 never left the gate. Its 137 passengers vanished.", "Answers: what happened in 1998.")),
"C26": dict(beat="Quiet. A sign on the door: A PLACE FOR GOODBYES. Sam lights a candle for Dad. (If Sam was taken, a candle is already burning, still warm.) Through the frosted glass you see the tall shape stop outside, and not come in. Lose 2 Fear.",
            notes="Demonstrates Rule 0 in action: a safe room. Rewarding the reader who learned L2."),
"C32": dict(beat="She prints a pass. 'Name?' You give it. Seat 0A. Her smile widens a little too far. Add 1 to your Claim.", claim=1),

"F11": dict(beat="Boxes labelled with passenger names. Yours holds your childhood things. Behind the whisky: a torn page, taped to the wall - and pinned beneath it, a yellowed passenger manifest for LV 137. Every name is crossed out except one, beside which someone has written DID NOT BOARD: your father's.",
            lore=("L10", "The manifest", "Dad was booked on LV 137 in 1998, seat 1A. He did not board.", "Answers: why it wants your family.")),
"F22": dict(beat="He wants it written in blood: your name, on his order pad. Lose 4 Vigour, add 1 to your Claim. You have the page.", claim=1),
"F25": dict(beat="Freezers labelled by year. In 1998: a staff uniform with your name on it, and a yellowed LV 137 passenger manifest. Every name is crossed out except your father's: DID NOT BOARD. The page you need is frozen to the door.",
            lore=("L10", "The manifest", "Dad was booked on LV 137 in 1998, seat 1A. He did not board.", "Answers: why it wants your family.")),
"F28": dict(beat="Tomorrow's paper. Page four: TWO MORE MISSING AT GATE 0. 'Their names bring the total to 139.' Your photo. Gain 1 Fear.",
            lore=("L11", "139", "The count goes up. 137 in 1998; tonight, two more.", "Opens: who else has it taken since?")),

"O03": dict(beat="'Name for the booking?' You give it. A key card: ROOM 1952. 'Checkout by six. You'll want to be well rested.' Codeword CHECKED_IN. Add 1 to your Claim.", claim=1),
"O14": dict(beat="It speaks in his voice: 'Stay a while. You didn't, last time.' It calls you by your full name. The eyes are frightened."),
"O16": dict(beat="You say goodbye to him, the real him, not the thing in the bed. The room goes quiet in a way that feels like a door closing. The thing lets go of the passport. If Sam was taken, Sam is asleep in the visitor's chair; you wake them. Nothing can come into this room now. Lose 3 Fear."),
"O25": dict(beat="Wheeled through the dark, you overhear two of the staff. 'Captain says the seat's been empty twenty-eight years.' 'Children'll do. Guests are always found where they sleep.'",
            lore=("L12", "The empty seat", "It has waited 28 years to fill Dad's seat. It will take his children instead.", "Answers: what it wants.")),

"G01": dict(beat="05:00. Gate 0 is real, and lit. The Hostess waits at the desk, smiling, terrified. Behind the glass, the tall passenger stands at the head of the jet bridge with its sign held high. You can read most of your name."),
"G20": dict(beat="In the aircraft doorway, in his coat, with his face, stands Dad. Up close you can see the others pressing out through the coat: 137 faces, all of them frightened. Dad's face is on top. It smiles perfectly. 'Come and sit with me,' it says, and uses your full name.",
            lore=("L13", "Up close", "The face on top is Dad's. All the others are the passengers of LV 137, still afraid.", "Answers: what it is. Opens: can they be freed?")),
"G26": dict(beat="The lights are steady - and still it moves. It never moves in the light. Sam's voice comes from inside its coat, from the Gate 00 jet bridge across the hall: 'Don't leave me here.'",
            notes="The single rule-break. Predictive-processing research: a late violated expectation resets the reader's threat model before the finale."),
"G29": dict(beat="Your real name, in the ledger, beside 137 others. Add 1 to your Claim. Gain 1 Fear.", claim=1,
            notes="Settling the hotel debt costs a letter: a real trade-off near the end."),

"C37": dict(lore=("L15", "Incident report", "1998: a crew member read the passenger list aloud and the subject stayed still. A previous irregular operation in 1987 - 'see attached'. Nothing attached.", "Opens: 1998 wasn't the first time? Survival tip, unstated: it can't move while its names are read aloud.")),
"O31": dict(lore=("L16", "Guest book", "137 signatures, one night in 1998, and a captain's loop: 'Capt. R.'", "Opens: who is the Announcer? Never answered.")),
"F33": dict(lore=("L17", "Till roll", "Your order from tonight, rung up in 1987, 1998 and now. Always 23:58.", "Opens: what happened in 1987, and why does it know what you'd order?")),
"H11": dict(notes="Origin of the estrangement and Sam's share of the blame (reviewers' missing beats)."),
"SECRET": dict(beat="Seat 1A. A man turns round. Not the thing - him. He came back for the seat he never took. 'I turned round at the gate in '98 because of you two. Let me do it properly this time.' You say goodbye. He sits. Across the terminal, 137 people stand up out of one long coat, and walk to their flight. Dawn.",
               lore=("L14", "Connection", "Dad fills his own seat, completing the manifest and freeing the 137.", "The full truth - only here.")),
"E_FINALCALL": dict(title="ENDING: Final Call",
               beat="'Final call for passenger...' and it reads your full name, perfectly. Your name is the last on the sign. You walk to Gate 0 smiling, terrified.",
               notes="Global rule: turn here when Claim reaches 5 OR Fear reaches its limit."),
"E_GROUNDCREW": dict(beat="Sam boards. The 1998 uniform fits you perfectly. Your smile is right. Your eyes, you notice in the glass, are frightened."),
"E_ALONE": dict(beat="You land. Sam's seat is empty. On the arrivals board, a status you can't stop seeing: LV 137 - AWAITING 1 PASSENGER."),
"E_LOOP": dict(beat="The board flips back. 11:52pm. DELAYED. Sam sits two seats away. At the far end of the concourse, a tall passenger is holding up a sign. This time you can read it. Start again from section 1."),
}

# Every death now costs a letter: the sign grows each time you die.
for _d in ["D01","D02","D03","D04","D05","D06","D07","D08","D09","D10"]:
    U.setdefault(_d, {})["claim"] = 1

U.setdefault("D10", {})["claim"] = 2

# G45 crosses off 2 Claim letters in the text only (negative values break min-Claim search)
_l = list(U["G20"]["lore"]); _l[2] = "The face on top is Dad's. Under it, more faces than you can count, all of them frightened."; U["G20"]["lore"] = tuple(_l)

U.pop("H02", None)
U["D10"]["claim"] = 1
U.setdefault("G29", {})["claim"] = 0
U["G29"]["beat"] = "The Night Manager turns the hotel ledger round: 137 names from one night in 1998, and a space for yours. Sign it (add 1 to your Claim) or refuse and pay in Vigour. Sam watches either way."
U["G29"]["beat"] = "The Night Manager turns the hotel ledger round: 137 names from one night in 1998, and a space for yours. Sign it (add 1 to your Claim), refuse and pay in Vigour, or, if you wear the uniform, be one of his own. Sam watches either way."
_l = list(U["F33"]["lore"]); _l[2] = "An order rung up in 1987, 1998 and tonight. Always 23:58."; U["F33"]["lore"] = tuple(_l)

for _k in ("G07", "G29"): U.pop(_k, None)
U.setdefault("G06", {})["beat"] = "The Hostess opens a ledger and settles your night line by line: the food, the room, the hand, and at the bottom, your name. Read once."
