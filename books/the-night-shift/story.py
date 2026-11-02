"""
THE NIGHT SHIFT - section architecture (stage 2, structure only: no prose).

One N(...) call per section. Keys are internal; printed numbers are assigned (shuffled) by
`python3 -m engine books/the-night-shift verify`. Fixed numbers (book.json): A01=1, LOCKER=179
(Mum's 1979 staff locker: 1979 - 1800), SECRET=147 (you were born at 01:47), E_TRUE=200.

Stats (book.json): Nerve, Vigour (vig), Fortune, Fear (fear; limit Nerve+3 -> E_ADMITTED),
WRISTBAND (band; five fields NAME / DATE OF BIRTH / NEXT OF KIN / WARD / BED; 0-5; 4 closes the
true ending at R30; 5 -> E_ADMITTED), ROUNDS (clock; six boxes 01:00-06:00, the 01:00 box is
ticked before section 1; tick on every move from a zone exit to the Main Corridor; 03:00 ticked =
the lifts go down only; <=4 at the reckoning = Mum's lucid moment; 5 = one more field; 06:00 ->
E_ADMITTED).

Codewords: SPOKE (first honest exchange), HELD (you protect Ros unasked), MENDED (real
reconciliation: both private requests told), WARDED (Ros taken by the hospital), PROMISE (Gary).
Items: NOTICE (master clue), VISITOR_BADGE / MUMS_LETTER / LAST_RULE (finale gate), GLASSES,
TICKET, RING (Mum's property bag), TABARD (Night Staff ending), FIRST_AID, LUGGAGE_TAG.
Hidden knowledge: KNOWS_1979 (locker puzzle), FIRST_BAND (secret ending).
Loose one-shot guards: RETURNED, OFFERED, TEABAR, LP_USED, PHONED, NIGHTINGALE, WALKMAN, CHAPEL,
ROTA, CUT_W, RECORDS, PROPERTY, MORTUARY, LODGE, REGISTER, PHONE_M, DELIVERY, WARD9, PARENTS,
SENT, ASKED (who has heard which request: for the "one telling" rule).

Death line (book.json check.death_end): "Fill in {cost} more field on your wristband. Return to
{X} and choose again."
"""
from engine.graph import StoryBuilder

B = StoryBuilder(stats=("fear", "vig", "band"))
N, L, drop, retarget, K, S = B.N, B.L, B.drop, B.retarget, B.K, B.S

V = "D_VIGOUR"      # shared death: Vigour reaches 0 (global rule)
X = "E_ADMITTED"    # shared ending: 5 wristband fields, the 06:00 round, or Fear at its limit (global rules)

# Every return from a zone to the Main Corridor goes through the first-return scenes, once each.
# (The clock ticks on these moves: exit section -> H02/H05/H01.)
def back(label):
    return [("H02", f"{label} (if you do not have RETURNED)", "not:RETURNED"),
            ("H05", f"{label} (if you have RETURNED but not OFFERED)", "has:RETURNED&not:OFFERED"),
            ("H01", f"{label} (if you have RETURNED and OFFERED)", "has:RETURNED&has:OFFERED")]

ROUNDS6 = (X, "If you have just ticked the 06:00 box", "limit:Rounds")

# ======================================================================
# ACT 1 - LEVEL 3, THE FAMILY ROOM  (near-linear tutorial, 01:40-02:00)
# ======================================================================
A, Z = 1, "Level 3"
N("A01", A, Z, "story", "01:40",
  "The family room on Level 3. Mum has been in theatre for three hours (burst aneurysm, one in three). You have been her carer for six years; she calls you Bean. The vending machine hums a note too low. Your sister is somewhere between the airport and here.",
  [("A02", "Continue")],
  notes="Section 1. Establish: Mum, Bean, the six years, theatre ends at 06:00, the hum. Ticked ROUNDS box 01:00 is already on the sheet (the 01:00 round happened before you arrived).")
N("A02", A, Z, "choice", "Ros",
  "Ros comes through the door with a wheelie case and her phone already out: 'Right. What do we know?' She used to call you Bean too. She stopped. She says your name instead.",
  [("A03", "Hug her"), ("A04", "Give her the facts, like a handover")],
  notes="Plants the TELL used in D09: Ros does not call you Bean. She says it first in E_TRUE (CANON: said once).")
N("A03", A, Z, "story", "The hug",
  "She stiffens, then pats your back twice, as if signing off a drawing. Her coat smells of aeroplane.",
  [("A05", "Continue")])
N("A04", A, Z, "story", "Handover",
  "You give it the way you give it to GPs: times, drugs, odds. Ros types every word into her phone. Each note feels like an audit.",
  [("A05", "Continue")])
N("A05", A, Z, "choice", "The surgeon's question",
  "The surgeon, still in his paper hat, between cases: complications are possible; decisions may be needed tonight. 'Which of you makes decisions for your mother?' Ros goes very still.",
  [("A06", "'I do. I'm her carer.'"), ("A07", "'Ask her. She's the one who flew in.'"), ("A08", "'We both do.'")],
  notes="Seeds the secret: the LPA names Ros (the surgeon has seen it; Ros knows).")
N("A06", A, Z, "story", "Carer",
  "The surgeon glances at his notes and says, 'We'll talk later.' Ros looks at the floor. Something is wrong with that answer and nobody says what. Gain 1 Fear.",
  [("A09", "Continue")], fear=1)
N("A07", A, Z, "story", "Flown in",
  "It comes out the way it came out at Dad's funeral. Ros flinches, then answers the surgeon for both of you: 'We'll talk.'",
  [("A09", "Continue")])
N("A08", A, Z, "choice", "Both",
  "The surgeon nods and goes. Ros looks at you a second too long, as if there is a document in her bag with your name not on it.",
  [("A10", "Ask her what she isn't saying"), ("A09", "Leave it")])
N("A10", A, Z, "story", "What she isn't saying",
  "She doesn't tell you, but she tells you that she isn't telling you, and that it's Mum's to say, and that she's sorry. It is the most honest thing she has said to you in eight years. Codeword SPOKE.",
  [("A09", "Continue")], gain=["SPOKE"], notes="SPOKE route 1 of 4 (A10, A35, H04, W19).")
N("A09", A, Z, "choice", "Property",
  "A theatre nurse brings Mum's property bag: a clear plastic sack with her name in marker. 'Rings go to Property, love. Basement.'",
  [("A11", "Open it"), ("A12", "Leave it zipped on the chair; you can't, not yet")],
  notes="Property-bag items GLASSES and TICKET (used in the finale and endings). The RING is in the Basement (B14/B16/LOCKER).")
N("A11", A, Z, "item", "Her things",
  "Her reading glasses, mended with tape. A lottery ticket for Saturday's syndicate draw, her numbers in her handwriting. No ring. Note the GLASSES and the TICKET.",
  [("A13", "Continue")], gain=["GLASSES", "TICKET"])
N("A12", A, Z, "story", "Zipped",
  "You put it on the chair and look at it instead. When you look back from the window, the chair is empty. Gain 1 Fear.",
  [("A13", "Continue")], fear=1, notes="The hospital keeps things. Explains why some readers reach the finale without GLASSES/TICKET.")
N("A13", A, Z, "choice", "The first round",
  "Footsteps that never hurry. A nurse at the door in a starched 1970s cap, a fob watch pinned upside down, a torch with a red filter. 'Can I get you two a cup of tea? You look done in.' Her voice is the warmest thing in the building.",
  [("A14", "Accept the tea"), ("A15", "Decline politely"), ("A16", "Ask her if there's any news of Mum")],
  notes="First sight of the Night Sister. Kindness is the threat; teaches the WRISTBAND.")
N("A14", A, Z, "story", "Milk, two sugars",
  "'Just your name for the tea list, love.' You give it. The tea is perfect. On your wrist, under your sleeve, something soft and plastic that wasn't there. Fill in the NAME field of your wristband. Gain 2 Vigour.",
  [("A17", "Continue")], vig=2, band=1, notes="First WRISTBAND field: teaches that comfort accepted is written down.")
N("A15", A, Z, "story", "No thank you",
  "'Course not.' She writes something on her clipboard anyway, and smiles, and goes. Gain 1 Fear.",
  [("A17", "Continue")], fear=1)
N("A16", A, Z, "story", "Mo",
  "'Maureen? Oh, I know Mo.' She says it fondly, the way you'd say it of a colleague. 'Theatre's running late. There's a bed made up on the Old Wing if either of you wants a lie-down.' Gain 1 Fear.",
  [("A17", "Continue")], fear=1, notes="Points to the Old Wing; the bed offer is the first sight of Rule 3's temptation.")
N("A17", A, Z, "choice", "Night setting",
  "You go to find a drinkable coffee, Ros at your shoulder. Halfway down the corridor the lights drop to night setting, a dim amber, bank by bank, toward you. Ros: 'Is that normal?'",
  [("A18", "Keep walking"), ("A19", "Stop and wait for them to come back up")],
  notes="Teaches Rule 7 before the reader has the Notice: by instinct, no death. Clue for D06 and D09.")
N("A18", A, Z, "story", "Keep walking",
  "You keep walking. The dimness follows a pace behind, then gives up. At the corner the lights come back. 'Okay,' Ros says. 'That was weird.'",
  [("A20", "Continue")])
N("A19", A, Z, "story", "Stopped",
  "You stop. Something rolls past in the amber: a porter's trolley with nobody on it and nobody pushing, close enough to touch your hip. It stops at the far end and waits. Gain 2 Fear.",
  [("A20", "Continue")], fear=2, notes="First sight of the empty trolley; a cost, not a death (first offence).")
N("A20", A, Z, "anomaly", "The corridor",
  "Tutorial anomaly. The corridor described in full: the yellow line to X-ray, the green line to Outpatients, the hand-gel dispensers, the clock. The clock says 01:40. Is something wrong?",
  [("A21", "Something is wrong - turn back"), ("A22", "Nothing is wrong - keep going")],
  notes="Teaches the anomaly rule fairly (it was 01:40 when you sat down, long before). Finale R17-R26 uses the same shape on obs charts.")
N("A21", A, Z, "story", "Noticed",
  "You turn back and the clock catches up with itself: 01:58. Lose 1 Fear.",
  [("A23", "Continue")], fear=-1)
N("A22", A, Z, "story", "Missed",
  "You walk on and arrive at the family-room door you just left. The clock still says 01:40; now you see it. Gain 1 Fear.",
  [("A23", "Continue")], fear=1)
N("A23", A, Z, "item", "The Notice",
  "Hiding from the next round in a linen cupboard, you find it taped inside the door: NIGHT STAFF NOTICE, ST BEDE'S, 1979. 1 Visiting hours are over; do not tell anyone you are a visitor. 2 If the Night Sister calls you by a patient's name, do not answer. 3 Never lie down on a ward bed. 4 After 3 a.m. the lifts go down only. 5 Ward 0 is closed. 6 Do not sign anything. 7 If the lights dim to night setting, keep walking. 8 is torn off. Note the NOTICE.",
  [("A24", "Continue")], gain=["NOTICE"],
  notes="MASTER CLUE SECTION (the Handbook equivalent). Every rule death points here. Reprinted on the Adventure Sheet. On every route.")
N("A24", A, Z, "choice", "Rules",
  "Ros reads it over your shoulder, frowning like it's a bad spec.",
  [("A25", "Read it aloud together"), ("A26", "Fold it into your pocket and keep moving")])
N("A25", A, Z, "story", "1979",
  "Ros reads it like a list, and somewhere around rule 5 she says, 'Mum trained here, you know. Nursing auxiliary. Seventy-nine.' You did know. You'd forgotten. Reading it together helps. Lose 1 Fear.",
  [("A26", "Continue")], fear=-1, gain=["KNOWS_1979"],
  notes="KNOWS_1979 route 1 of 3 (A25, W24, H12): the Property locker puzzle (1979 - 1800 = 179).")
N("A26", A, Z, "choice", "Maureen?",
  "The Night Sister comes back along the corridor with her red torch, smiling straight at you. 'Maureen? Maureen, love. Time for your obs.' Mum's name. Maybe there's news.",
  [("D01", "Answer her: 'That's my mum. Is there news?'"), ("A27", "Say nothing")],
  notes="Rule 2. Temptation: news of Mum. First fair death, one page after the Notice.")
N("D01", A, Z, "death", "There you are",
  "She brightens: 'There you are.' She takes your wrist to find your pulse, and keeps it, and walks you to a bed with Mum's name on the board, and you go, because she is so kind, and the obs never end.",
  [], warn="Notice rule 2: if the Night Sister calls you by a patient's name, do not answer.",
  clue=["A23"], checkpoint="A17", band=1)
N("A27", A, Z, "choice", "Ros opens her mouth",
  "You say nothing. Ros, polite to the bone, starts to answer for you both.",
  [("A28", "Put your hand over her mouth"), ("A29", "Let her answer")])
N("A28", A, Z, "story", "Hand",
  "Ros goes rigid with outrage, then understands, and stays rigid. The Sister writes something, and goes. Ros doesn't thank you; she stands nearer. Codeword HELD.",
  [("A30", "Continue")], gain=["HELD"], notes="HELD route 1 (A28, W04, M26; rescues W31, B22, R15).")
N("A29", A, Z, "story", "Ros answers",
  "'She's in theatre. We're her family.' The Sister turns the torch on Ros, delighted. You pull Ros away; her wrist is sore for no reason she can name. Lose 2 Vigour. Gain 1 Fear.",
  [("A30", "Continue")], vig=-2, fear=1)
N("A30", A, Z, "choice", "The porter",
  "At the lifts, a porter leaning on an empty trolley. Grey overall, kind face. 'Visiting, are we?'",
  [("D02", "'Yes. My mum's in theatre.'"), ("A31", "'Just waiting for someone.'"), ("A32", "Walk past him, fast")],
  notes="Rule 1. The true answer is the dangerous one.")
N("D02", A, Z, "death", "Visiting hours are over",
  "'Visiting hours are over,' he says gently, and helps you onto the trolley, because you look done in, and the ceiling tiles go by, and by.",
  [], warn="Notice rule 1: visiting hours are over; do not tell anyone you are a visitor.",
  clue=["A23"], checkpoint="A24", band=1)
N("A31", A, Z, "story", "Waiting",
  "'Aren't we all.' He nods you on. When you look back the trolley is following, one room behind, with nobody pushing it. Gain 1 Fear.",
  [("A33", "Continue")], fear=1, notes="The trolley that follows you: a recurring 'one room behind' beat.")
N("A32", A, Z, "test", "Fast",
  "Chase tutorial. The trolley's wheels speed up behind you. Test your Fortune.",
  [("A33", "Lucky", "pass"), ("A33", "Unlucky: it clips your heels; lose 2 Vigour", "fail")], test=dict(type="Fortune"))
N("A33", A, Z, "choice", "The window",
  "Waiting for the lift, Ros says to the car-park fog: 'You said someone has to actually be here. At the funeral. I've had that in my head for eight years.'",
  [("A34", "'I meant it.'"), ("A35", "'I shouldn't have said it.'")],
  notes="What broke, from Ros's side. One telling of the funeral line.")
N("A34", A, Z, "story", "Meant it",
  "Ros nods as if you've confirmed a figure. The lift arrives. Gain 1 Fear.",
  [("A36", "Continue")], fear=1)
N("A35", A, Z, "story", "Shouldn't have",
  "It isn't sorry, but it's near it. Ros breathes out for what looks like the first time since Toronto. Codeword SPOKE.",
  [("A36", "Continue")], gain=["SPOKE"], notes="SPOKE route 2 of 4.")
N("A36", A, Z, "story", "The Main Corridor",
  "The lift takes you down to Level 1. The doors open on the Main Corridor: floor lines in four colours, the WRVS tea bar shutter half up, the chapel door, the clock at 02:00. Somewhere below, a lift is going down and down. Your wristband (whether or not you've noticed it) has five fields.",
  [("H01", "Continue")],
  notes="End of Act 1. First arrival: does NOT tick ROUNDS. Rule 4 is visible here (the lift going down). States the goal via the Main Corridor hub.")

# ======================================================================
# HUB - THE MAIN CORRIDOR
# ======================================================================
A, Z = 2, "Main Corridor"
N("H01", A, Z, "choice", "The Main Corridor",
  "Return line first (the corridor is longer every time; the Sister's round is closer every time; the clock jumps to the box you have ticked). First visit: the floor lines, the tea bar, the chapel door, Lost Property, the payphone, three ways to go and one door you can't.",
  [ROUNDS6,
   ("W01", "The Old Wing (if you do not have the VISITOR'S BADGE)", "not:VISITOR_BADGE"),
   ("B01", "The Basement, by the lift (it only goes down) (if you do not have MUM'S LETTER)", "not:MUMS_LETTER"),
   ("HL", "Maternity and Ward 9, by the lift (if you do not have THE LAST RULE)", "not:LAST_RULE"),
   ("HS", "Maternity and Ward 9, by the stairs (if you do not have THE LAST RULE)", "not:LAST_RULE"),
   ("W28", "Follow the sound of Ros's phone into the Old Wing (if you have WARDED and the VISITOR'S BADGE)", "has:WARDED&has:VISITOR_BADGE"),
   ("H08", "The WRVS tea bar", "not:TEABAR"),
   ("H09", "Lost Property", "not:LP_USED"),
   ("H13", "The payphone that is ringing", "not:PHONED"),
   ("H19", "Follow the red floor line", "not:REDLINE"),
   ("R01", "Ward 0 (only if you hold the VISITOR'S BADGE, MUM'S LETTER and THE LAST RULE)", "has:VISITOR_BADGE&has:MUMS_LETTER&has:LAST_RULE")],
  notes="The one hub. Zones gated shut once their item is held. Ward 0 gated behind all three (finale gate). Global rule: ticking 06:00 here -> Admitted.")
N("H02", A, Z, "story", "Back on the Main Corridor",
  "The first return. The corridor has changed: the yellow line now runs to a door marked WARD 0. On the clock, the time of the box you've just ticked. Codeword RETURNED.",
  [ROUNDS6, ("H03", "If Ros is with you", "not:WARDED"), ("H01", "If Ros is on the Old Wing (WARDED)", "has:WARDED")],
  gain=["RETURNED"], notes="First-return scene (fires once). Clock hub.")
N("H03", A, Z, "choice", "Things to say",
  "Ros checks her phone. You see a note titled THINGS TO SAY TO BEAN. It's empty. She sees you see it.",
  [("H04", "Ask her what was on it (if you do not have SPOKE)", "not:SPOKE"), ("H01", "Leave it")],
  notes="Ros's hub scene.")
N("H04", A, Z, "story", "Deleted",
  "'I wrote it at Departures. Every line started with sorry and none of them were true enough.' Codeword SPOKE.",
  [("H01", "Continue")], gain=["SPOKE"], notes="SPOKE route 3 of 4. Ros still does not call you Bean (the D09 tell holds until E_TRUE).")
N("H05", A, Z, "choice", "An offer",
  "The second return. The Night Sister is waiting at the tea bar with a folded blanket. 'Your sister's dead on her feet, love. There's a bed for her on the Old Wing. And one for you. I'll ring through the minute there's news from theatre.' Codeword OFFERED.",
  [ROUNDS6,
   ("H07", "Let Ros take the bed for an hour (if Ros is with you)", "not:WARDED"),
   ("H10", "Take the blanket and the chair yourself"),
   ("H06", "Thank her, and refuse")],
  gain=["OFFERED"], notes="The midpoint offer (fires once). WARDED route 1 of 3 (H07, W03, M27).")
N("H06", A, Z, "story", "Refused",
  "'Course.' She writes it down. 'I'll be round.' Gain 1 Fear.",
  [("H01", "Continue")], fear=1)
N("H07", A, Z, "story", "An hour",
  "Ros lets herself be led, still talking about flight times. The swing doors to the Old Wing close behind them. Her phone, in her coat, begins to ring and doesn't stop. Codeword WARDED.",
  [("H01", "Continue")], gain=["WARDED"], notes="WARDED route 1. Rescue: W28/W31, B21/B22, R14/R15.")
N("H10", A, Z, "story", "Blanket",
  "The blanket is warm from somewhere. You sleep for no time at all. When you wake, your wristband says WARD in her neat capitals. Gain 4 Vigour. Fill in one more field of your wristband.",
  [("H01", "Continue")], vig=4, band=1)
N("H08", A, Z, "choice", "The tea bar",
  "The WRVS shutter is half up. A volunteer in a 1970s tabard butters toast that never runs out. 'Tea, duck?'",
  [("H11", "Have a cup"), ("H12", "Ask her how long she's been here"),
   ("H16", "If you have the TICKET: ask her to check Mum's numbers", "has:TICKET")],
  gain=["TEABAR"])
N("H11", A, Z, "story", "Tea",
  "Strong, sweet, exactly how Mum makes it. She writes your date of birth on a paper cup without asking it. Gain 3 Vigour. Fill in one more field of your wristband.",
  [("H01", "Continue")], vig=3, band=1)
N("H12", A, Z, "story", "Since the war",
  "'Oh, forever.' She remembers Mo: 'Night auxiliary, seventy-nine. Filthy laugh. Tore something off a notice once and the Sister never forgave her.' Lose 1 Fear.",
  [("H01", "Continue")], fear=-1, gain=["KNOWS_1979"],
  notes="KNOWS_1979 route 3. Foreshadows THE LAST RULE (Mum tore rule 8 off).")
N("H16", A, Z, "story", "Saturday",
  "She checks Mum's numbers against a 1979 newspaper and shakes her head: 'Not yet, duck. It's Saturday's.' She looks at the date as if it hurts her eyes. Nobody here has a Saturday. Lose 1 Fear.",
  [("H01", "Continue")], fear=-1, notes="TICKET use 1; clue for R40 (the Kept cannot look at a date that hasn't happened).")
N("H19", A, Z, "story", "The red line",
  "There are four floor lines, and tonight a fifth, red, that runs under the chapel door, down a stairwell, and stops at a door you can't open: WARD 0 - CLOSED. Someone has been along it with a mop. Gain 1 Fear.",
  [("H01", "Continue")], gain=["REDLINE"], fear=1, notes="Floor lines leading somewhere new. Shows the finale door (Rule 5).")
N("H09", A, Z, "choice", "Lost Property",
  "A hatch, a bell, shelves of things from every decade. A sign: ONE ITEM PER VISITOR - and VISITOR has been crossed out and PATIENT written over it.",
  [("H14", "Take the first-aid kit"), ("H15", "Take the luggage tag")], gain=["LP_USED"])
N("H14", A, Z, "item", "First aid",
  "A tin first-aid kit, St John's Ambulance. Restore 6 Vigour once, at any time. Note the FIRST-AID KIT.",
  [("H01", "Continue")], gain=["FIRST_AID"])
N("H15", A, Z, "item", "Larkvale",
  "A LARKVALE AIRWAYS luggage tag, LV 137, its passenger name scratched out. Somebody else got out of somewhere. It makes you feel better than it should. Lose 2 Fear. Note the LUGGAGE TAG.",
  [("H01", "Continue")], gain=["LUGGAGE_TAG"], fear=-2, notes="The Layover cameo. Flavour only.")
N("H13", A, Z, "choice", "The payphone",
  "It's theatre, a woman's voice, clipped: 'Still in surgery. We need a next of kin for the paperwork. Is that you?'",
  [("H17", "'Yes. Me.'"), ("H18", "'My sister. Rosalind.'"), ("H01", "Hang up")],
  gain=["PHONED"], notes="The phone hub scene. The voice is the Sister's.")
N("H17", A, Z, "story", "Next of kin",
  "'Lovely.' Pen on paper down the line. On your wrist, NEXT OF KIN fills in by itself, in your own handwriting. Fill in one more field of your wristband.",
  [("H01", "Continue")], band=1)
N("H18", A, Z, "story", "Rosalind",
  "A pause, as if she can't quite read what you said. 'I'll make a note.' The line goes dead. Gain 1 Fear.",
  [("H01", "Continue")], fear=1, notes="She cannot read a name spoken by someone who loves you (first hint).")
N("HL", A, Z, "story", "The lift up",
  "You press 5 for Maternity.",
  [("M01", "If you have not ticked the 03:00 box", "stat:Rounds<=2"),
   ("HLD", "If you have ticked the 03:00 box", "stat:Rounds>=3")],
  notes="Rule 4 bites through the clock: after 03:00 the lift goes down.")
N("HLD", A, Z, "story", "Down only",
  "The lift goes down. Basement, sub-basement, a floor with no number; the doors open on the Main Corridor's own echo, and you climb back up the stairs. Gain 1 Fear.",
  [] + back("Climb back to the Main Corridor"), fear=1,
  notes="Clock exit: costs a ROUNDS tick for using the lift after 03:00.")
N("HS", A, Z, "story", "Five flights",
  "The stairwell smells of cigarettes from 1979. Lose 1 Vigour.",
  [("M01", "Continue")], vig=-1)

# ======================================================================
# ZONE 1 - THE OLD WING  (key item: VISITOR_BADGE - 3 routes: W07 moral, W16 nerve, W23 test/combat)
# ======================================================================
Z = "Old Wing"
N("W01", A, Z, "choice", "The Old Wing",
  "Return line first. The 1890s fever wing: tiled walls, radiators like organ pipes, the corridor longer going than coming back.",
  [("W02", "The Nightingale ward", "not:NIGHTINGALE"),
   ("W14", "The chapel", "not:CHAPEL"),
   ("W20", "The Sister's office"),
   ("W28", "Follow the sound of Ros's phone (if you have WARDED)", "has:WARDED"),
   ("W29", "Back to the Main Corridor (if you have the VISITOR'S BADGE)", "has:VISITOR_BADGE"),
   ("W30", "Back to the Main Corridor without it (if you do not have the VISITOR'S BADGE)", "not:VISITOR_BADGE")],
  notes="Zone junction and checkpoint. The office is repeatable until the badge is held (it always yields it), so the zone can't softlock.")
N("W02", A, Z, "choice", "The Nightingale ward",
  "Thirty beds, all made, most of them full. Ros sways in the doorway: jet lag finally landing. 'I just need to sit down.'",
  [("W03", "Let her sit on the empty bed by the door for a minute (if Ros is with you)", "not:WARDED"),
   ("W04", "Get your shoulder under her arm and keep her walking (if Ros is with you)", "not:WARDED"),
   ("W05", "Walk the ward (if you are alone)", "has:WARDED")],
  gain=["NIGHTINGALE"])
N("W03", A, Z, "story", "Just a minute",
  "She sits, then lies back, just for a minute. When you look round from the Kept, the bed is made and Ros is gone, and somewhere down the wing her phone begins to ring. Gain 1 Fear. Codeword WARDED.",
  [("W05", "Continue")], gain=["WARDED"], fear=1, notes="WARDED route 2 (Rule 3, broken by Ros).")
N("W04", A, Z, "story", "Upright",
  "She's heavier than she looks. 'I'm fine.' She isn't, and she lets you. Codeword HELD.",
  [("W05", "Continue")], gain=["HELD"], notes="HELD route 2.")
N("W05", A, Z, "choice", "The Kept",
  "Patients from every decade, smiling, not dying and not recovering: a man in 1952 winceyette, a woman with a Walkman, a boy in a 1986 football kit who waves.",
  [("W06", "Go to the boy (if you do not have the VISITOR'S BADGE)", "not:VISITOR_BADGE"),
   ("W08", "Sit with the woman with the Walkman", "not:WALKMAN"),
   ("W10", "Walk on toward the far doors")],
  notes="Analog lore + set piece. The Kept are harmless unless you lie down beside them (clue for D03/D10).")
N("W06", A, Z, "choice", "Gary, 1986",
  "Appendix, he says. His mum's visitor's badge is clipped to his locker. 'She said she'd be back at visiting. Will you tell her I waited?'",
  [("W07", "Promise him"), ("W09", "Tell him you can't promise anything")])
N("W07", A, Z, "item", "Gary's badge",
  "He unclips it and gives it to you: VISITOR, St Bede's, 1986. 'It goes to whoever's visiting.' It now has your name. He settles back, smiling, and stays. Gain 1 Fear. Note the VISITOR'S BADGE. Codeword PROMISE.",
  [("W10", "Continue")], gain=["VISITOR_BADGE", "PROMISE"], fear=1,
  notes="Badge route 1 of 3 (moral). PROMISE pays off in Act 3 (R06a).")
N("W08", A, Z, "story", "Side B",
  "She gives you one earphone. A training tape: a young woman's voice reading obs, laughing at a mistake, a filthy laugh you know. 'Never let them see you're tired,' says someone else on the tape. Gain 1 Fear.",
  [("W05", "Continue")], gain=["WALKMAN"], fear=1,
  notes="Lore: Mum's voice, 1979. The Sister learned her kindness from people like Mum.")
N("W09", A, Z, "story", "Waited",
  "'She didn't come either,' he says, without blame, and turns his face to the wall. Gain 1 Fear.",
  [("W10", "Continue")], fear=1)
N("W10", A, Z, "choice", "The round",
  "The far doors open and the round comes in: the red torch, the fob watch. Every one of the Kept holds out a wrist in unison. One empty bed has its blanket turned down.",
  [("W11", "Stand at a bedside with the badge clipped on (if you have the VISITOR'S BADGE)", "has:VISITOR_BADGE"),
   ("W11", "Fall in behind her like staff (if you are wearing the TABARD)", "has:TABARD"),
   ("W12", "Stand at a bedside like a visitor"),
   ("W13", "Keep walking for the far doors"),
   ("D03", "Get into the empty bed and pull up the blanket: she won't wake a sleeping patient")],
  notes="One-room-behind set piece; the obs in unison. D03 is tempting as a hiding place.")
N("D03", A, Z, "death", "Lights out",
  "The sheets are cool and tight. She doesn't wake you. She tucks you in, and checks your pulse, and the obs are perfect, every hour, for ever.",
  [], warn="Notice rule 3: never lie down on a ward bed. The Kept are harmless unless you lie down beside them.",
  clue=["A23", "W05"], checkpoint="W01", band=1)
N("W11", A, Z, "story", "Passed over",
  "The torch passes over you like you are furniture. 'Visitors,' she says fondly, to nobody.",
  [("W13", "Continue")])
N("W12", A, Z, "story", "Checked",
  "She takes your wrist on the way past, as if you were one of hers. When she lets go, WARD is filled in: OLD WING. Fill in one more field of your wristband.",
  [("W13", "Continue")], band=1)
N("W13", A, Z, "choice", "The far doors",
  "Out in the tiled corridor, the ward breathing behind you.",
  [("W27", "If Ros is with you and you have SPOKE: hold out your wrist for her scissors", "not:WARDED&has:SPOKE&not:CUT_W"),
   ("W01", "Back along the corridor")],
  notes="Scissors moment 1 of 2 (W27, R12).")
N("W27", A, Z, "story", "Surgical scissors",
  "Ros digs the scissors out of her bag ('Don't ask'). One snip. A field drops off your wristband and the cut stings like it was skin. Cross off one field of your wristband. Lose 1 Vigour.",
  [("W01", "Continue")], gain=["CUT_W"], band=-1, vig=-1)
N("W14", A, Z, "choice", "The chapel",
  "Candles, a lectern, a visitors' book open at tonight. A VISITOR badge is clipped to its cover. A card: SIGN FOR A PRAYER TO BE SAID FOR YOUR LOVED ONE.",
  [("D04", "Sign the book for Mum"),
   ("W15", "Unclip the badge without signing (if you do not have the VISITOR'S BADGE)", "not:VISITOR_BADGE"),
   ("W18", "Light a candle")],
  gain=["CHAPEL"], notes="Rule 6 temptation: a prayer for Mum.")
N("D04", A, Z, "death", "Signed",
  "Your pen is still on the page when the prayer begins, in her voice, very softly, and it is for you, and it is the kind they say at the end.",
  [], warn="Notice rule 6: do not sign anything.", clue=["A23"], checkpoint="W01", band=1)
N("W15", A, Z, "test", "The clip",
  "The pages riffle as you reach for it. Test your Nerve.",
  [("W16", "Success", "pass"), ("W17", "Failure", "fail")], test=dict(type="Nerve"))
N("W16", A, Z, "item", "Unclipped",
  "It comes free. The book settles. Note the VISITOR'S BADGE.",
  [("W01", "Continue")], gain=["VISITOR_BADGE"], notes="Badge route 2 of 3 (nerve).")
N("W17", A, Z, "story", "Your name in the book",
  "The pages turn to tonight by themselves and your name is already there, in her hand. The badge stays clipped. Fill in one more field of your wristband.",
  [("W01", "Continue")], band=1)
N("W18", A, Z, "story", "Candles",
  "One candle for Mum. If Ros is with you, she lights a second without saying who for. Lose 2 Fear.",
  [("W19", "If Ros is with you and you do not have SPOKE: ask her who the second one is for", "not:WARDED&not:SPOKE"),
   ("W21", "If Ros is with you and you have SPOKE and HELD but not MENDED: tell her why you stayed", "not:WARDED&has:SPOKE&has:HELD&not:MENDED"),
   ("W01", "Leave the chapel")], fear=-2)
N("W19", A, Z, "story", "Who for",
  "'Dad. And one for you, actually. For the six years.' She says it to the candle, but she says it. Codeword SPOKE.",
  [("W01", "Continue")], gain=["SPOKE"], notes="SPOKE route 4 of 4.")
N("W21", A, Z, "story", "Why you stayed",
  "MENDED route 1 of 3 (chapel). If neither request has been told yet, this is THE telling: you tell her Mum asked you to stay ('Don't let them put me anywhere'); she tells you Mum sent her ('If you stay, your sister will let you do everything'). If one half is already known (SENT/ASKED), pointer only. Lose 2 Fear. Codeword MENDED.",
  [("W01", "Continue")], gain=["MENDED", "SENT", "ASKED"], fear=-2,
  notes="One telling: whichever MENDED scene comes first carries the full exchange; the others are gated not:MENDED.")
N("W20", A, Z, "choice", "The Sister's office",
  "Her office, immaculate. A desk drawer, a framed duty rota, a tabard on the back of the door. The kettle is still warm.",
  [("W22", "Search the desk drawer (if you do not have the VISITOR'S BADGE)", "not:VISITOR_BADGE"),
   ("W24", "Read the duty rota", "not:ROTA"),
   ("W25", "Take the tabard off the hook (if you do not have it)", "not:TABARD"),
   ("W01", "Leave")],
  notes="Repeatable room (one-shots inside are guarded).")
N("W22", A, Z, "test", "The drawer",
  "Visitor badges, a whole drawer, in elastic bands by decade. Footsteps that never hurry. Test your Fortune.",
  [("W23", "Lucky", "pass"), ("W26", "Unlucky", "fail")], test=dict(type="Fortune"))
N("W23", A, Z, "item", "A badge from the drawer",
  "You take one from the top: VISITOR, blank, waiting for a name. Note the VISITOR'S BADGE.",
  [("W20", "Continue")], gain=["VISITOR_BADGE"], notes="Badge route 3 of 3 (test, or fight in W26).")
N("W26", A, Z, "combat", "The night porter",
  "The porter fills the doorway with his empty trolley. He'd like to help you onto it. THE NIGHT PORTER  NERVE 7  VIGOUR 8.",
  [("W23", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")],
  test=dict(type="combat", foe="THE NIGHT PORTER", nerve=7, vig=8), notes="Checkpoint before this fight: W01.")
N("W24", A, Z, "story", "The rota, 1979",
  "NIGHTS, OLD WING, MARCH 1979. Sister's name rubbed out by thumbs. Auxiliary: M. - Mum's maiden name. Someone has drawn a tiny smiling face beside it.",
  [("W20", "Continue")], gain=["ROTA", "KNOWS_1979"], notes="Analog document. KNOWS_1979 route 2.")
N("W25", A, Z, "item", "The tabard",
  "A blue 1979 auxiliary's tabard, name tape M. It fits you. Staff walk past rounds. Gain 1 Fear. Note the TABARD.",
  [("W20", "Continue")], gain=["TABARD"], fear=1,
  notes="Helps on rounds (W10, M23). Must be taken off in Act 3 (R32) or it is the Night Staff ending; forced choice at 4 fields (R31).")
N("W28", A, Z, "choice", "Ros's bed",
  "A side room. Ros asleep under a 1952 blanket, smiling her un-Ros smile. Her wristband is filled in: ROSALIND, every field. Her phone rings in her coat on the chair.",
  [("W31", "Say her name, the short one only family uses"),
   ("D03", "Lie down beside her until she wakes"),
   ("W01", "Leave her for now")],
  notes="Rescue route 1 (also reachable from the hub once the zone is gated). The Sister cannot read a name spoken by someone who loves you.")
N("W31", A, Z, "story", "Ros",
  "'Ros.' Her eyes open on the second time. Her wristband is blank. 'Did I fall asleep? Did they ring?' Cross off WARDED. Codeword HELD.",
  [("W29", "Continue (if you have the VISITOR'S BADGE)", "has:VISITOR_BADGE"),
   ("W01", "Continue (if you do not)", "not:VISITOR_BADGE")],
  gain=["HELD"], lose=["WARDED"], notes="Rescue counts as HELD.")
N("W29", A, Z, "story", "One room behind",
  "Leaving the Old Wing, the round is in the ward you've just left, then the corridor, a room behind you all the way. You don't look back. Gain 1 Fear.",
  [] + back("Back to the Main Corridor"), fear=1, notes="Clock exit (item held).")
N("W30", A, Z, "story", "Retreat",
  "You go back the way you came, which is shorter. Behind you, the ward lights drop to night setting.",
  [] + back("Back to the Main Corridor"), notes="Clock exit without the item: costs a ROUNDS tick.")

# ======================================================================
# ZONE 2 - THE BASEMENT  (key item: MUMS_LETTER - 3 routes: B07 via B03/B04/B05/B06, LOCKER)
# ======================================================================
Z = "Basement"
N("B01", A, Z, "choice", "The Basement",
  "Return line first. Pipes, porters' corridors, signs in 1960s Helvetica: MEDICAL RECORDS, PROPERTY, MORTUARY, PORTERS. The lift only goes one way.",
  [("B02", "Medical Records", "not:RECORDS"),
   ("B12", "Property", "not:PROPERTY"),
   ("B17", "The corridor to the mortuary", "not:MORTUARY"),
   ("B24", "The porters' lodge", "not:LODGE"),
   ("B11", "Linen services", "not:LINEN"),
   ("B26", "Go back up")],
  notes="Zone junction and checkpoint. Records always yields the letter (or a fight), so no softlock.")
N("B02", A, Z, "choice", "Medical Records",
  "A clerk behind a hatch, cardigan, 1970s glasses, smiling. 'File request? Just sign the slip.'",
  [("B03", "Sign the slip"), ("B04", "Search the stacks yourself"),
   ("B06", "If Ros is with you: let her work out the filing system", "not:WARDED")],
  gain=["RECORDS"])
N("B03", A, Z, "story", "The slip",
  "You sign. The clerk fetches it at once. Your signature stays on the slip, and the slip stays on the spike. Fill in one more field of your wristband.",
  [("B07", "Continue")], band=1, notes="Rule 6 broken: a field, not a death (punished gradually).")
N("B04", A, Z, "test", "The stacks",
  "Miles of brown folders. Test your Fortune.",
  [("B07", "Lucky", "pass"), ("B05", "Unlucky", "fail")], test=dict(type="Fortune"))
N("B05", A, Z, "combat", "The porter",
  "An empty trolley at the end of the stack, then a porter behind it. THE PORTER  NERVE 8  VIGOUR 8.",
  [("B07", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")],
  test=dict(type="combat", foe="THE PORTER", nerve=8, vig=8), notes="Checkpoint before this fight: B01.")
N("B06", A, Z, "story", "Terminal digit",
  "'Terminal-digit filing. God, I love it.' Ros finds it in four minutes, and is proud, and you let her be.",
  [("B07", "Continue")])
N("B07", A, Z, "item", "Mum's file",
  "Her file: the 2020 stroke, your name as carer on every page. Then a Lasting Power of Attorney for health, 2023, naming Ros. Clipped to it, an envelope in Mum's writing: For Bean. The letter: 'Because you would never let me go, love, and I couldn't make you be the one.' Note MUM'S LETTER.",
  [("B08", "If Ros is with you", "not:WARDED"), ("B21", "If Ros is on the Old Wing (WARDED)", "has:WARDED")],
  gain=["MUMS_LETTER"],
  notes="Letter route 1 of 2 (LOCKER is 2). ONE TELLING of the letter's text and the LPA. Analog document.")
N("B08", A, Z, "choice", "The LPA",
  "Ros has gone white. She knew. She has known for three years.",
  [("B09", "If you have SPOKE: tell her what Mum asked of you six years ago", "has:SPOKE&not:MENDED"),
   ("B10", "Ask her why she never told you"),
   ("B01", "Put the file away and say nothing")])
N("B09", A, Z, "story", "Asked",
  "MENDED route 2 of 3 (Records). If neither request is yet told, THE telling (both requests, see W21). Otherwise pointer. Lose 2 Fear. Codeword MENDED.",
  [("B01", "Continue")], gain=["MENDED", "SENT", "ASKED"], fear=-2)
N("B10", A, Z, "story", "Why",
  "'Because she asked me not to. Because you'd have taken it as me leaving again.' True, and not the whole truth, and you both know it. Gain 1 Fear.",
  [("B01", "Continue")], fear=1, notes="The cold route: the LPA is explained, the requests are not.")
N("B21", A, Z, "choice", "The in-tray",
  "In the clerk's in-tray, a new file, still warm from the typewriter: ROSALIND. ADMITTED 02:00. OLD WING.",
  [("B22", "Tear it in half"), ("B01", "Leave it")], notes="Rescue route 2 (Basement).")
N("B22", A, Z, "story", "Torn",
  "It tears like skin. Somewhere above, a phone stops ringing. When you come back to the lift, Ros is sitting on the stairs in her coat, furious and confused, and very glad to see you. Cross off WARDED. Codeword HELD. Lose 2 Vigour.",
  [("B01", "Continue")], gain=["HELD"], lose=["WARDED"], vig=-2)
N("B12", A, Z, "choice", "Property",
  "A wire cage. A clerk with a ledger: 'Patients' property, staff lockers. Lockers go by the year you first came to St Bede's.' Behind him, rows of numbered lockers. If you know the year, take away 1800 and turn to that section.",
  [("LOCKER", "Turn to the locker (1979 - 1800 = 179)", "hidden:KNOWS_1979"),
   ("B13", "Ask for Maureen's ring"),
   ("B15", "Reach through the wire for the tray marked THEATRE 3")],
  gain=["PROPERTY"], notes="Number puzzle: LOCKER is fixed at 179.")
N("LOCKER", A, Z, "item", "Locker 179",
  "Mum's staff locker, 1979: a photo of the night shift (a row of young nurses; the Sister's face is a blur of all of them), her ring, warm, and a copy of the letter in its envelope. Property keeps everything. Lose 1 Fear. Note the RING and MUM'S LETTER.",
  [("B01", "Continue")], gain=["RING", "MUMS_LETTER"], fear=-1,
  notes="FIXED NUMBER 179. RING route 3; letter route 2. Analog document (the photo). If the reader already holds the letter, the text says it's the same envelope.")
N("B13", A, Z, "choice", "Sign for it",
  "'Just sign here, love.' He turns the ledger round.",
  [("B14", "Sign"), ("B15", "Refuse and try the tray through the wire")])
N("B14", A, Z, "item", "Signed for",
  "Her ring, wedding band worn thin. It is warm, as if just off her finger. Fill in one more field of your wristband. Note the RING.",
  [("B01", "Continue")], gain=["RING"], band=1)
N("B15", A, Z, "test", "Through the wire",
  "Test your Nerve.",
  [("B16", "Success", "pass"), ("B01", "Failure: the wire bites; lose 2 Vigour", "fail")], test=dict(type="Nerve"))
N("B16", A, Z, "item", "The tray",
  "THEATRE 3: a watch, a hearing aid, and Mum's ring, warm. Note the RING.",
  [("B01", "Continue")], gain=["RING"])
N("B17", A, Z, "choice", "Night setting",
  "The mortuary corridor. The lights go to night setting and behind you a trolley starts to roll.",
  [("B18", "Keep walking"), ("D06", "Stop and let it pass")],
  gain=["MORTUARY"], notes="Rule 7, with the empty trolley (A19 taught its cost).")
N("D06", A, Z, "death", "Collected",
  "It doesn't pass. It stops beside you, and it is exactly the right height, and in the amber dark it is easy to lie down on it, and the ceiling tiles go by.",
  [], warn="Notice rule 7: if the lights dim to night setting, keep walking (and the trolley took you at A19 when you stopped).",
  clue=["A23", "A19"], checkpoint="B01", band=1)
N("B18", A, Z, "choice", "The mortuary",
  "Fridge doors, steel, labelled. One is labelled with your date of birth. A drawer further down is saying, politely, 'Maureen?'",
  [("B19", "Open the door with your birthday on it"), ("B20", "Answer the drawer: 'She's not here.'"), ("B01", "Go back")])
N("B19", A, Z, "story", "1991",
  "Set piece. The fridge opens on a 1991 incubator, warm, empty, a tiny wristband taped inside: BABY OF MAUREEN. 14.3.91. 01:47. Gain 2 Fear.",
  [("B01", "Continue")], fear=2, gain=["FIRST_BAND"],
  notes="FIRST_BAND route 1 of 2 (M03). The time 01:47 is the secret-ending number (147).")
N("B20", A, Z, "story", "Not here",
  "'Date of birth?' it asks, kindly, and you hear yourself give yours. Fill in one more field of your wristband.",
  [("B01", "Continue")], band=1, notes="Rule 2 adjacent: answering the hospital costs a field.")
N("B11", A, Z, "choice", "Linen services",
  "Cages of laundered sheets, a mangle from 1890, and on a rail, staff tabards by decade. One is 1979, blue, name tape M.",
  [("B23", "Take the 1979 tabard (if you do not have it)", "not:TABARD"), ("B01", "Leave it")],
  gain=["LINEN"])
N("B23", A, Z, "item", "The tabard",
  "It fits you. It smells of Mum's washing powder from 1979, which is impossible. Gain 1 Fear. Note the TABARD.",
  [("B01", "Continue")], gain=["TABARD"], fear=1, notes="TABARD route 2 of 2 (W25).")
N("B24", A, Z, "story", "The porters' lodge",
  "Analog document: the collections board. Tonight: OLD WING x1 (R.); WARD 0 x1 (M., BAY 6); WARD 0 x1 (VISITOR) - and a space where your name will go.",
  [("B01", "Continue")], gain=["LODGE"], fear=1,
  notes="Lore: Ward 0 has Mum in Bay 6 and is expecting you. R. is Ros if WARDED (prose conditional).")
N("B26", A, Z, "choice", "The way up",
  "The trolley is in the corridor behind you, a room back, waiting. The lift, or the stairs.",
  [("B29", "Take the lift up"), ("B30", "Take the stairs")],
  notes="One-room-behind beat. Rule 4: after 03:00 the lift goes down only.")
N("B29", A, Z, "story", "The lift",
  "You press G.",
  [("D05", "If you have ticked the 03:00 box", "stat:Rounds>=3")] + [
   (t, l, "stat:Rounds<=2&" + c) for t, l, c in back("Otherwise: the doors open on the Main Corridor")],
  notes="Clock exit. The death is fair: the Notice gave the rule, the sheet gives the time.")
N("D05", A, Z, "death", "Down only",
  "The doors close and the lift goes down: sub-basement, foundations, the old fever pits, floors with no numbers and then floors with names on them, and one of them is yours.",
  [], warn="Notice rule 4: after 3 a.m. the lifts go down only.", clue=["A23", "A36"], checkpoint="B01", band=1)
N("B30", A, Z, "story", "The stairs",
  "Eleven flights to Level 1, the trolley's wheels a landing below the whole way. Lose 1 Vigour.",
  [] + back("Back to the Main Corridor"), vig=-1, notes="Clock exit.")

# ======================================================================
# ZONE 3 - MATERNITY & WARD 9  (key item: LAST_RULE - 3 routes: M12 test, M17 combat/nerve, M20 moral)
# ======================================================================
Z = "Maternity"
N("M01", A, Z, "choice", "Level 5",
  "Return line first. Maternity on the left, Ward 9 (children's) on the right, the nurses' station between. The stairwell door here says WARD 0 - CLOSED, and behind it a monitor is beeping in Mum's rhythm.",
  [("M02", "The delivery register", "not:REGISTER"),
   ("M08", "The nurses' station, where a phone is ringing", "not:PHONE_M"),
   ("M14", "The delivery suite", "not:DELIVERY"),
   ("M18", "Ward 9", "not:WARD9"),
   ("D08", "Open the door marked WARD 0"),
   ("M28", "Back down to the Main Corridor (if you have THE LAST RULE)", "has:LAST_RULE"),
   ("M29", "Back down without it (if you do not have THE LAST RULE)", "not:LAST_RULE")],
  notes="Zone junction and checkpoint. Delivery and Ward 9 always yield THE LAST RULE (or a fight), so no softlock.")
N("D08", A, Z, "death", "Closed",
  "Behind the door, Mum's monitor, and stairs going down to it. You take them two at a time. The door shuts behind you, and the stairs keep going, and so does the beeping, never nearer.",
  [], warn="Notice rule 5: Ward 0 is closed (it can be opened only with the badge, the letter and the last rule, from the Main Corridor).",
  clue=["A23"], checkpoint="M01", band=1)
N("M02", A, Z, "choice", "The register",
  "The 1991 delivery register on a desk, open, a pen in the gutter.",
  [("M03", "Turn to March 1991"), ("M04", "Turn to tonight's page")], gain=["REGISTER"])
N("M03", A, Z, "story", "Baby of Maureen",
  "Analog document. 14.3.91, 01:47. Mother: Maureen, 36. Baby: 7lb 2oz. Taped beside it, the first wristband you ever wore: BABY OF MAUREEN, 01:47. Lose 1 Fear.",
  [("M01", "Continue")], fear=-1, gain=["FIRST_BAND"],
  notes="FIRST_BAND route 2 of 2. Secret ending number: 01:47 -> 147.")
N("M04", A, Z, "story", "Tonight",
  "Under ADMISSIONS, tonight's date and your name, in pencil, waiting for ink. You rub it out with your thumb until the paper goes thin. Gain 1 Fear.",
  [("M01", "Continue")], fear=1)
N("M08", A, Z, "choice", "The phone",
  "The nurses' station phone, cream plastic, ringing and ringing.",
  [("M09", "Answer it"), ("M01", "Let it ring")], gain=["PHONE_M"])
N("M09", A, Z, "story", "Tomorrow",
  "Set piece. Mum's voice, groggy, rude, alive: 'Bean? It's tomorrow here. Don't ask.' She says your name and a field on your wristband goes blank. If you do not know it yet, she asks whether Ros ever told you she sent her (SENT: told once here, pointer elsewhere). 'The bit I tore off is in the drug cupboard, love.' Cross off one field of your wristband.",
  [("M10", "Continue")], band=-1, gain=["SENT"],
  notes="Someone who loves you says the true thing: a field comes off. The proof that it is really Mum is the field coming off, not the word: the Sister can say 'Bean' (she does, in Ros's voice, at R02), but nothing she says frees you.")
N("M10", A, Z, "choice", "The drug cupboard",
  "Locked. The Sister's keys hang on a hook by the station, a big ring of them.",
  [("M11", "Take the keys and try them"), ("M01", "Leave it")])
N("M11", A, Z, "test", "The keys",
  "Too many keys and footsteps that never hurry. Test your Fortune.",
  [("M12", "Lucky", "pass"), ("M13", "Unlucky", "fail")], test=dict(type="Fortune"))
N("M12", A, Z, "item", "Rule 8",
  "Behind the controlled drugs, a strip of laminated card: 8. LET THEM GO. On the back, in biro, a filthy little doodle and M., 1979. Note THE LAST RULE.",
  [("M01", "Continue")], gain=["LAST_RULE"], notes="LAST_RULE route 1 of 3 (puzzle/test).")
N("M13", A, Z, "story", "Caught on the round",
  "The keys jangle and she is there, red torch, smiling. 'Can't sleep?' She checks your wristband and fills in BED. Fill in one more field of your wristband.",
  [("M01", "Continue")], band=1)
N("M14", A, Z, "choice", "The delivery suite",
  "Theatre staff in paper masks round an empty delivery bed, waiting. Behind the masks, nothing. One has a strip of card pinned to its gown.",
  [("M15", "Fight them for it"), ("M16", "Slip past and take it"), ("M01", "Back out")], gain=["DELIVERY"])
N("M15", A, Z, "combat", "Theatre staff",
  "THEATRE STAFF  NERVE 8  VIGOUR 9.",
  [("M17", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")],
  test=dict(type="combat", foe="THEATRE STAFF", nerve=8, vig=9), notes="Checkpoint before this fight: M01.")
N("M16", A, Z, "test", "Slip past",
  "Test your Nerve.",
  [("M17", "Success", "pass"), ("M15", "Failure: they turn", "fail")], test=dict(type="Nerve"))
N("M17", A, Z, "item", "Pinned",
  "The strip of card: 8. LET THEM GO. Note THE LAST RULE.",
  [("M01", "Continue")], gain=["LAST_RULE"], notes="LAST_RULE route 2 of 3 (combat/nerve).")
N("M18", A, Z, "choice", "Ward 9, 1999",
  "The children's ward as it was when you were eight: the bed by the window, the hard chair beside it where Mum slept for a week.",
  [("M19", "Sit in the chair"), ("D07", "Lie down in your old bed"),
   ("M23", "Walk the ward"),
   ("M25", "If Ros is with you: the parents' room", "not:WARDED&not:PARENTS")],
  gain=["WARD9"], notes="Relationship beat zone. D07 temptation: your own bed.")
N("D07", A, Z, "death", "Tucked in",
  "It fits you. It shouldn't. Someone tucks the blanket under the mattress the way Mum did, tight, and says goodnight, and isn't Mum.",
  [], warn="Notice rule 3: never lie down on a ward bed.", clue=["A23"], checkpoint="M01", band=1)
N("M19", A, Z, "choice", "The chair",
  "From the chair you can see what she saw for a week: the bed, the window, and something folded under the mattress edge.",
  [("M20", "Reach under the mattress (if you do not have THE LAST RULE)", "not:LAST_RULE"),
   ("M21", "If Ros is with you: give her the chair", "not:WARDED"),
   ("M01", "Get up")])
N("M20", A, Z, "item", "Under the mattress",
  "A strip of laminated card, folded small: 8. LET THEM GO. Mum put it there in 1999. Note THE LAST RULE.",
  [("M01", "Continue")], gain=["LAST_RULE"], notes="LAST_RULE route 3 of 3 (moral: sitting where she sat).")
N("M21", A, Z, "story", "Ros in the chair",
  "Ros's side of 1999: she was twelve and at home with Dad, making the tea and telling everyone it was fine. She has never sat in this chair. She sits.",
  [("M22", "If you have SPOKE but not MENDED: tell her what this week was like for you", "has:SPOKE&not:MENDED"),
   ("M20", "Reach under the mattress (if you do not have THE LAST RULE)", "not:LAST_RULE"),
   ("M01", "Get up")])
N("M22", A, Z, "story", "This week",
  "MENDED route 3 of 3 (Ward 9). If neither request is yet told, THE telling (see W21). Otherwise pointer. Lose 2 Fear. Codeword MENDED.",
  [("M20", "Reach under the mattress (if you do not have THE LAST RULE)", "not:LAST_RULE"),
   ("M01", "Get up")], gain=["MENDED", "SENT", "ASKED"], fear=-2)
N("M23", A, Z, "choice", "The round on Ward 9",
  "The Kept children asleep in rows; at the far end, the red torch, coming bed by bed. One room behind is now this room.",
  [("M24", "Hide behind the curtains"),
   ("M18", "If you are wearing the TABARD: fall in beside her and do the round", "has:TABARD")])
N("M24", A, Z, "story", "Curtains",
  "Her shadow on the curtain, the torch through it, red. She stops, and counts, and moves on. Gain 1 Fear.",
  [("M18", "Continue")], fear=1)
N("M25", A, Z, "choice", "The parents' room",
  "A fold-down bed, a kettle, a sign: PARENTS MAY SLEEP HERE. Ros sits on the bed and starts to unlace her boots. 'Ten minutes. I mean it.'",
  [("M26", "Take her boots off her and make her stand"), ("M27", "Let her have ten minutes")],
  gain=["PARENTS"], notes="WARDED route 3.")
N("M26", A, Z, "story", "Boots",
  "'You are unbelievable,' she says, and laces them again, and stands, and leans on you for one second. Codeword HELD.",
  [("M18", "Continue")], gain=["HELD"], notes="HELD route 3.")
N("M27", A, Z, "story", "Ten minutes",
  "You make two teas. When you turn round the bed is folded away and the room smells of 1952 blanket. Her phone is ringing on the Old Wing. Codeword WARDED.",
  [("M18", "Continue")], gain=["WARDED"], notes="WARDED route 3.")
N("M28", A, Z, "story", "Down",
  "Down the stairs with the strip of card in your pocket. Behind you, on Ward 9, the round, a room behind you all the way down. Gain 1 Fear.",
  [] + back("Back to the Main Corridor"), fear=1, notes="Clock exit (item held).")
N("M29", A, Z, "story", "Down without it",
  "Down the stairs. The beeping behind the WARD 0 door follows you a floor and stops.",
  [] + back("Back to the Main Corridor"), notes="Clock exit without the item.")

# ======================================================================
# ACT 3 - WARD 0 & RECOVERY
# ======================================================================
A, Z = 3, "Ward 0"
N("R01", A, Z, "story", "Down",
  "The lift only goes down. Past the Basement to a floor that isn't on the panel: WARD 0, the 1979 recovery ward where Mum did her first night shift. If Ros is on the Old Wing, her phone is ringing down here now.",
  [("R02", "Continue")], notes="FINALE GATE (book.json): entered only with the badge, the letter and the last rule. Checkpoint.")
N("R02", A, Z, "choice", "The crossing",
  "The low point on every route. A corridor lined with the Kept from every decade, doing their obs in unison; porters' trolleys; the lights going to night setting. Behind you, Ros's voice: 'Bean, wait for me.' Ros stopped calling you Bean years ago.",
  [("R03", "If your wristband has 3 or more fields filled", "stat:Wristband>=3"),
   ("R05", "Otherwise: keep walking, eyes front, the badge on your chest", "stat:Wristband<=2"),
   ("R06", "Otherwise, if Ros is with you and you have HELD: walk with her hand in yours", "stat:Wristband<=2&not:WARDED&has:HELD"),
   ("R40", "Otherwise, if you have the TICKET: hold up Saturday's ticket as you walk", "stat:Wristband<=2&has:TICKET"),
   ("D09", "Otherwise: stop and wait for the voice behind you", "stat:Wristband<=2")],
  notes="WRISTBAND mid-value bite (3+). D09: the tell (A02) plus Rule 7.")
N("R03", A, Z, "combat", "The porters",
  "They know a patient when they see one. Two porters and a trolley made up for you. THE PORTERS  NERVE 9  VIGOUR 10.",
  [("R06", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")],
  test=dict(type="combat", foe="THE PORTERS", nerve=9, vig=10), notes="Checkpoint before this fight: R01.")
N("R05", A, Z, "story", "Eyes front",
  "You walk. The voice behind you says your name like Ros used to. You don't turn. Gain 1 Fear.",
  [("R06", "Continue")], fear=1)
N("R40", A, Z, "story", "Saturday's draw",
  "You hold Mum's ticket up like a pass. The Kept turn their faces away from the date on it, a day that hasn't happened, and the corridor lets you through. Lose 1 Fear.",
  [("R06", "Continue")], fear=-1, notes="TICKET use 2 (clued at H16).")
N("D09", A, Z, "death", "Wait for me",
  "You stop and turn. The lights go down to night setting and stay there, and the voice is very close now, and kind, and not your sister's.",
  [], warn="Notice rule 7: if the lights dim, keep walking. Ros does not call you Bean (A02).",
  clue=["A23", "A02"], checkpoint="R01", band=1)
N("R06", A, Z, "story", "WARD 0 - CLOSED",
  "The doors. The one rule you have to break. You push, and they open, and the Sister cannot follow you through them; she doesn't need to. She is already at the station inside, writing.",
  [("R06a", "If you have PROMISE", "has:PROMISE"), ("R04", "Continue", "not:PROMISE")],
  notes="The entity's rule broken once, late: the door she cannot follow you through, and she is already inside.")
N("R06a", A, Z, "story", "Visiting",
  "On the bench by the doors, a woman in a 1986 anorak with a carrier bag of comics. You tell her Gary waited. She goes up the stairs you came down. Lose 2 Fear.",
  [("R04", "Continue")], fear=-2, notes="Pays off PROMISE (W07).")
N("R04", A, Z, "story", "Handover, 1979",
  "Analog document on the station desk: a night report, Ward 0, March 1979, in a young auxiliary's round hand. Bed 4 asked to be let go and the auxiliary sat with him and let him. Under it, in the Sister's hand: AUXILIARY REMOVED RULE 8 FROM THE NOTICE. NOT TO BE REPLACED.",
  [("R07", "Continue")], notes="Lore: where THE LAST RULE came from. One telling.")
N("R07", A, Z, "story", "The reckoning",
  "One page, read once. The Sister reads your notes back to you: every cup of tea, every name, every field. Then she checks her upside-down watch against your ROUNDS.",
  [("R08", "If you have not ticked the 05:00 box", "stat:Rounds<=4"),
   ("R09", "If you have ticked the 05:00 box", "stat:Rounds>=5")],
  notes="ROUNDS reckoning. 6 never reaches here (Admitted at the hub).")
N("R08", A, Z, "story", "Lucid",
  "Reward. From Bay 6, for one breath, Mum's real voice: 'Bean? Is that you making that racket?' A field on your wristband goes blank. Cross off one field of your wristband. Lose 2 Fear.",
  [("R10", "Continue")], band=-1, fear=-2, notes="Mum's lucid moment (ROUNDS <=4).")
N("R09", A, Z, "story", "The 05:00 round",
  "'You're late, love.' She fills in another field for you, kindly. Fill in one more field of your wristband.",
  [("R10", "Continue")], band=1)
N("R10", A, Z, "choice", "Claimed back",
  "Fields come off only when they are claimed back.",
  [("R11", "If Ros is with you: give her Mum's letter to read aloud", "not:WARDED"),
   ("R12", "If Ros is with you and you have HELD: hold out your wrist for her scissors", "not:WARDED&has:HELD"),
   ("R13", "Go on into the ward")],
  notes="Wristband reckoning. One claim-back here.")
N("R11", A, Z, "story", "Read aloud",
  "Ros reads it in her list voice and gets to 'love' and can't. She reads it anyway. Pointer to the letter (B07 told it). Cross off one field of your wristband.",
  [("R13", "Continue")], band=-1)
N("R12", A, Z, "story", "Snip",
  "'Hold still.' Cross off one field of your wristband. Lose 1 Vigour.",
  [("R13", "Continue")], band=-1, vig=-1, notes="Scissors moment 2 of 2.")
N("R13", A, Z, "choice", "Bay 2",
  "Bay 2's curtain is drawn. Behind it, a phone is ringing.",
  [("R14", "If Ros is on the Old Wing (WARDED): open the curtain", "has:WARDED"),
   ("R16", "Walk on to the charts")])
N("R14", A, Z, "choice", "Ros in Bay 2",
  "Ros, Kept, smiling, her wristband full.",
  [("R15", "Say her name"), ("R16", "Leave her and go on to Mum")], notes="Rescue route 3.")
N("R15", A, Z, "story", "Found",
  "'Ros.' She wakes cross. 'Did I miss it?' Cross off WARDED. Codeword HELD.",
  [("R16", "Continue")], gain=["HELD"], lose=["WARDED"])
N("R16", A, Z, "choice", "The charts",
  "The obs chart walk. At the foot of each bay, a chart. If nothing is wrong, walk on; if something is wrong, turn back. Get it right and the ward lets you reach Bay 6.",
  [("R17", "If you have Mum's GLASSES: put them on first", "has:GLASSES"), ("R18", "Begin")],
  notes="Anomaly-loop finale. Checkpoint.")
N("R17", A, Z, "story", "Her glasses",
  "The tape at the hinge, her prescription: the numbers on the charts come sharp. Lose 1 Fear.",
  [("R18", "Begin")], fear=-1, notes="Property-bag item use (GLASSES).")
N("R18", A, Z, "anomaly", "Bay 3",
  "A 1952 chart: temperature, pulse, BP, all normal, all in the Sister's neat hand.",
  [("R19", "Nothing is wrong - walk on"), ("R22", "Something is wrong - turn back")],
  notes="Nothing wrong. Correct: walk on.")
N("R19", A, Z, "anomaly", "Bay 4",
  "A 1979 chart. The 03:00 obs are in Ros's handwriting.",
  [("R25", "Something is wrong - turn back (if Ros is with you and you have MENDED)", "not:WARDED&has:MENDED"),
   ("R20", "Something is wrong - turn back (if you do not have MENDED)", "not:MENDED"),
   ("R20", "Something is wrong - turn back (if you have MENDED but Ros is on the Old Wing)", "has:MENDED&has:WARDED"),
   ("R22", "Nothing is wrong - walk on")],
  notes="Wrong. Correct: turn back. The late cost on the kind route hangs here (R25).")
N("R25", A, Z, "choice", "Her handwriting",
  "Ros has the chart. 'I'm the one she named. Let me do this.' She wants to take Mum's obs herself, tonight, every hour.",
  [("R26", "Let her be the one"), ("R27", "Take the chart off her: you've done this for six years")],
  notes="LATE COST on the kind route: a test of MENDED. Cost both ways.")
N("R26", A, Z, "story", "Hers",
  "You let her. Her hands are shaking and her numbers are right. It costs you something you've held for six years. Gain 2 Fear.",
  [("R20", "Continue")], fear=2)
N("R27", A, Z, "story", "Yours",
  "She lets go of the chart, and of something else. 'Right,' she says. 'Of course.' Cross off MENDED. Lose 1 Fear.",
  [("R20", "Continue")], lose=["MENDED"], fear=-1)
N("R20", A, Z, "anomaly", "Bay 5",
  "A chart from tonight. The last obs are timed 06:02.",
  [("R30", "Something is wrong - turn back"), ("R22", "Nothing is wrong - walk on")],
  notes="Wrong (a time that hasn't happened). Correct: turn back -> Bay 6.")
N("R22", A, Z, "test", "Reset",
  "The ward resets: Bay 3 again, and the round a bay nearer. Gain 2 Fear. Test your Fortune.",
  [("R18", "Lucky: the ward you know", "pass"), ("R23", "Unlucky: a ward you don't", "fail")],
  test=dict(type="Fortune"), fear=2)
N("R23", A, Z, "anomaly", "Bay 3, again",
  "A chart with your name in the patient box.",
  [("R24", "Something is wrong - turn back"), ("R22", "Nothing is wrong - walk on")], notes="Wrong. Correct: turn back.")
N("R24", A, Z, "anomaly", "Bay 4, again",
  "Every number normal, every time past. You look for the wrong thing and can't find it.",
  [("R28", "Nothing is wrong - walk on"), ("R22", "Something is wrong - turn back")],
  notes="Nothing wrong (beats readers who memorised 'turn back').")
N("R28", A, Z, "anomaly", "Bay 5, again",
  "Mum's chart, but the date of birth is yours.",
  [("R30", "Something is wrong - turn back"), ("R22", "Nothing is wrong - walk on")], notes="Wrong. Correct: turn back -> Bay 6.")
N("R30", A, Z, "story", "Bay 6",
  "Mum, Kept: smiling, colour good, obs perfect and unchanging. The Night Sister at the bedside with a consent form missing only your signature. Up close her face is every nurse who was ever kind to you - the one who held the sick bowl on Ward 9, the midwife, Mum at twenty-four in a 1979 tabard - assembled, smiling.",
  [("R31", "If your wristband has 4 or more fields filled", "stat:Wristband>=4"),
   ("R32", "If you are wearing the TABARD", "stat:Wristband<=3&has:TABARD"),
   ("R33", "Otherwise", "stat:Wristband<=3&not:TABARD")],
  notes="The entity seen in full. WRISTBAND 4 closes the true ending here.")
N("R31", A, Z, "choice", "A patient can't visit a patient",
  "'Back to bed, love. Patients can't visit patients.' She turns your wrist to show you: four fields.",
  [("E_KEPT", "Sign the consent form so Mum can stay"),
   ("E_NIGHTSTAFF", "If you are wearing the TABARD: take the night shift instead", "has:TABARD"),
   (X, "Let her tuck you in")],
  notes="The 4-field branch: no true ending.")
N("R32", A, Z, "choice", "Visitors only",
  "A sign on the curtain rail: VISITORS ONLY BEYOND THIS POINT. STAFF TO THE STATION. You are wearing her tabard.",
  [("R33", "Take the tabard off"), ("E_NIGHTSTAFF", "Keep it on. Someone has to stay.")], lose=["TABARD"],
  notes="Night Staff is a real temptation, not a trap.")
N("R33", A, Z, "choice", "The consent form",
  "'Just your signature, love. Next of kin. She'll never be any worse than this.' Mum pats the bed beside her: 'Lie down with me a minute, Bean.'",
  [("R39", "If you have the RING: slip it back onto her finger", "has:RING&not:RING_ON"),
   ("E_KEPT", "Sign"), ("D10", "Lie down beside her, just for a minute"), ("R34", "Refuse")],
  notes="Kept Mum says Bean here: she IS Mum; the danger is lying down beside the Kept, not her voice.")
N("R39", A, Z, "story", "Her ring",
  "It goes on over the knuckle the way it always did, with a twist. Her hand warms. For a second her smile is her own, crooked, and her obs flicker. Lose 2 Fear.",
  [("R33", "Continue")], gain=["RING_ON"], fear=-2, notes="RING use. One-shot.")
N("D10", A, Z, "death", "Beside her",
  "You lie down beside her the way you did at eight. Her arm comes round you. The obs are perfect, both of you, every hour, and the night never ends.",
  [], warn="Notice rule 3: never lie down on a ward bed; the Kept are harmless unless you lie down beside them.",
  clue=["A23", "W05"], checkpoint="R16", band=1)
N("R34", A, Z, "story", "Next of kin",
  "'Then who decides, love?' she asks, and waits.",
  [("R35", "If Ros is with you and you have MENDED", "not:WARDED&has:MENDED"),
   ("R36", "If Ros is with you and you do not have MENDED", "not:WARDED&not:MENDED"),
   ("R37", "If Ros is on the Old Wing (WARDED)", "has:WARDED")])
N("R35", A, Z, "story", "Let them go",
  "The true climax. Ros reads Mum's name aloud, all of it, and you hold Mum's hand; the Sister cannot read a name spoken by someone who loves her. You both read THE LAST RULE. You let her go - back to theatre, to the one-in-three. The Sister's hold breaks; her face comes apart into all the nurses it was made of, and they go off shift.",
  [("R38", "Continue")], notes="Every hold breaks: she cannot keep anyone who has been let go.")
N("R36", A, Z, "story", "Who decides",
  "Ros says it's her, legally. You say it's you, actually. You're both right and neither of you lets go, and the monitor's line goes flat and smooth and starts again from the top.",
  [("E_LOOP", "Continue")])
N("R37", A, Z, "story", "Alone",
  "You read the last rule by yourself. You let her go by yourself. You are good at by yourself.",
  [("E_ONLYCHILD", "Continue")])
N("R38", A, Z, "story", "06:00",
  "Theatre ends. The recovery ward is just a recovery ward. Ros has your hand, or you have hers. If you know the minute you were born, turn to that section (01:47 is 147).",
  [("SECRET", "Turn to the time you were born", "hidden:FIRST_BAND"), ("E_TRUE", "Otherwise, wait")],
  notes="Secret-ending instruction (FIRST_BAND: B19 or M03).")

# ---------------- ENDINGS -----------------
A, Z = 3, "Ending"
N("E_TRUE", A, Z, "ending", "ENDING: Visiting Hours",
  "06:02. Mum wakes and lives: groggy, rude, alive. She says the thing she asked of each of you, out loud, to both of you. You and Ros walk out to the car park together and argue about who drives. (If you have the RING / GLASSES / TICKET: you give them back.)",
  [], notes="TRUE ENDING. FIXED NUMBER 200. Last line has a speaker.")
N("SECRET", A, Z, "ending", "ENDING: Ward 9",
  "14 March 1991. Mum, thirty-six, awake at 3 a.m. on the ward with you. Nobody is on their round. The last page is her looking at you.",
  [], notes="SECRET ENDING. FIXED NUMBER 147. Never linked plainly.")
N("E_KEPT", A, Z, "ending", "ENDING: Kept",
  "You sign. Mum is Kept, smiling, for ever. You visit every night. You are very good at it.",
  [])
N(X, A, Z, "ending", "ENDING: Admitted",
  "Your bed is made up. The Sister tucks you in. The lights go to night setting.",
  [], notes="Global rule: five wristband fields, the 06:00 round, or Fear at its limit (Nerve + 3).")
N("E_NIGHTSTAFF", A, Z, "ending", "ENDING: Night Staff",
  "Someone has to stay. You always were the one who stayed. The tabard fits.",
  [])
N("E_ONLYCHILD", A, Z, "ending", "ENDING: Only Child",
  "You walk out alone at 06:00. Mum survives. On the Old Wing, Ros's phone keeps ringing.",
  [])
N("E_LOOP", A, Z, "ending", "ENDING: Readmitted",
  "01:40. The family room. Ros coming through the door with her phone already out. This time, say it first. (Loop: start again from section 1 with the wristband reset to 1 field.)",
  [])
N(V, A, Z, "death", "Spent",
  "You sit down on the lino and can't get up. A trolley rolls toward you.",
  [], warn="Vigour is always visible on the Adventure Sheet.", checkpoint="LAST", band=1,
  notes="Global rule: Vigour 0. Return to your last checkpoint.")

# ======================================================================
# v2 STRUCTURAL EDITS (Gate 2: the author's answers, 2026-11-02)
# ======================================================================
_K = K()

# 1. Clock: one spare hour. ROUNDS starts with NO box ticked (book.json start 0). A perfect run (three zone
#    returns) reaches Ward 0 having ticked 03:00. Thresholds in ticks are unchanged: <=4 at the reckoning = lucid
#    moment (R08), 5 = one more field (R09), the 6th tick = Admitted (hubs). The lift rule still keys on the 3rd
#    tick (stat:Rounds>=3), so it now bites only readers who made at least one extra trip before their last zone
#    (or who use the lift after the third return, which no longer happens on a perfect run).
_K["A01"]["notes"] = ("Section 1. Establish: Mum, Bean, the six years, theatre ends at 06:00, the hum. No ROUNDS box is "
                      "ticked yet (v2: the author gave the reader one spare hour).")
_K["A36"]["beat"] = _K["A36"]["beat"].replace("the clock at 02:00", "the corridor clock, stopped, waiting for the first round")
_K["A36"]["notes"] = ("End of Act 1. First arrival: does NOT tick ROUNDS. Rule 4 is visible here (the lift going down). "
                      "The corridor clock shows the box most recently ticked (none yet).")

# 2. Secret ending becomes a CODA after the true ending. The reader never trades 200 for 147.
#    The engine forbids links from terminal kinds, so 200 is kind "finale" (non-terminal) with one hidden link to
#    147, the terminal coda. FIRST_BAND is loose in book.json so the hidden link counts as always open (no
#    softlock at 200 for readers who never learned 01:47; for them the book simply ends). See STRUCTURE.md, Engine gaps.
_K["R38"]["links"] = L(("E_TRUE", "Continue"))
_K["R38"]["beat"] = "Theatre ends at 06:00. The recovery ward is just a recovery ward. Ros has your hand, or you have hers."
_K["R38"]["notes"] = "v2: the secret-ending invitation moved to the end of 200."
_K["E_TRUE"].update(kind="finale", links=L(("SECRET", "If you know the minute you were born, turn to it", "hidden:FIRST_BAND")))
_K["E_TRUE"]["beat"] = (_K["E_TRUE"]["beat"] + " Last lines: THE END, then one unnumbered sentence inviting the reader, "
                        "if they know the minute they were born, to turn to it (no section number printed).")
_K["E_TRUE"]["notes"] = ("TRUE ENDING. FIXED NUMBER 200. Kind 'finale': an ending with one hidden link (the coda). "
                         "Ros says 'Bean' here, once. Last line has a speaker, before the invitation.")
_K["SECRET"]["title"] = "CODA: Ward 9"
_K["SECRET"]["beat"] = ("A last page after 200. 14 March 1991, 01:47 and after. Mum, thirty-six, awake at 3 a.m. on the ward "
                        "with you. Nobody is on their round. The last page is her looking at you.")
_K["SECRET"]["notes"] = "SECRET CODA. FIXED NUMBER 147. Reached only from 200 by the hidden number (FIRST_BAND: B19 or M03)."

# 3. Late MENDED: the Bay 2 rescue can also mend things, at a cost, if you have already SPOKE.
_K["R14"]["links"] = L(("R41", "If you have SPOKE: say her name, and then say the rest (fill in one more field of your wristband)", "has:SPOKE&not:MENDED"),
                       ("R15", "Say her name"),
                       ("R16", "Leave her and go on to Mum"))
N("R41", 3, "Ward 0", "story", "The rest",
  "You wake her by name and then you don't stop: Bay 2, curtain drawn, the Sister writing at the station. If neither request "
  "has been told, THE telling (see W21); otherwise pointer. It takes long enough that the Sister notices: she fills in a field "
  "for you while you talk. Fill in one more field of your wristband. Cross off WARDED. Codewords HELD and MENDED.",
  [("R16", "Continue")], gain=["HELD", "MENDED", "SENT", "ASKED"], lose=["WARDED"], band=1,
  notes="v2: MENDED route 4 of 4 (late, costly). Lets a Ros taken early still reach the true ending.")

# To stay at 200: the red floor line (H19, flavour) is cut; M01 and D08 already show the WARD 0 door.
_K["H01"]["links"] = [l for l in _K["H01"]["links"] if l["to"] != "H19"]
drop("H19")

# 4. Deaths in Act 1 do not fill a wristband field; from the Main Corridor onwards they do.
for _d in ("D01", "D02"):
    _K[_d]["band"] = 0
    _K[_d]["notes"] = ("v2: Act 1 death, no wristband field. End with 'Return to {%s} and choose again.' only "
                       "(the book-wide death line's 'Fill in 1 more field' does not apply here)." % _K[_d]["checkpoint"])

# ======================================================================
# v3: round-1 review fixes (lean review: A 7.5, B 7.5)
# ======================================================================
_K = {s["key"]: s for s in B.S} if hasattr(B, "S") else _K
# Anger is the engine, not a sin: owning the funeral line also opens Ros up; being her carer costs nothing.
_K["A34"]["gain"] = list(set(_K["A34"].get("gain", []) + ["SPOKE"])); _K["A34"]["fear"] = 1
_K["A06"]["fear"] = 0
# MENDED is not available a third of the way in: the Old Wing telling reveals the requests but doesn't mend.
_K["W21"]["gain"] = [g for g in _K["W21"]["gain"] if g != "MENDED"]
# Care must tempt: it pays in Fear (the stat that matters), and still costs a field.
_K["A14"].update(vig=0, fear=-2); _K["H11"].update(vig=0, fear=-2); _K["H10"].update(vig=2, fear=-3)
# Ros's scissors need something to cut.
for _s in S:
    for _l in _s["links"]:
        if _l["to"] in ("W27", "R12"):
            _l["cond"] = (_l["cond"] + "&" if _l["cond"] else "") + "stat:Wristband>=1"
# The Ward 0 stair door is a lesson, not a trap to repeat.
_K["D08"]["gain"] = list(set(_K["D08"].get("gain", []) + ["TRIED_DOOR"]))
for _s in S:
    for _l in _s["links"]:
        if _l["to"] == "D08":
            _l["cond"] = (_l["cond"] + "&" if _l["cond"] else "") + "not:TRIED_DOOR"
# Owning it opens Ros up (SPOKE); taking it back is easier but doesn't (a little comfort, no SPOKE).
_K["A35"]["gain"] = [g for g in _K["A35"]["gain"] if g != "SPOKE"]; _K["A35"]["fear"] = -1
_K["A34"]["fear"] = 0
