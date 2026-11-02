"""
<TITLE> - section architecture.

One N(...) call per section. Keys are internal (A01, C12, D03, E_TRUE ...); printed numbers are
assigned by `python3 -m engine <book> verify` (shuffled; fixed numbers in book.json).

N(key, act, zone, kind, title, beat, links, gain=(), lose=(), test=None, warn=None, clue=(),
  checkpoint=None, notes=None, **stats)
  kind   : story | choice | item | test | combat | anomaly | death | ending
  links  : [(to, label), (to, label, cond)]   cond: has:X / not:X / hidden:X / pass / fail / win / lose /
           stat:Doom>=3 / limit:Doom, joined with & ; aliases from book.json
  stats  : the stat fields declared in StoryBuilder(stats=...) and book.json (fear=1, vig=-2, doom=1)
  test   : {"type": "Nerve"} / {"type": "Fortune"} / {"type": "combat", "foe": "THE THING", "nerve": 7, "vig": 7}
  death  : needs warn (the rule/clue the reader was given), clue (keys of sections that gave it, each must be
           able to precede the death) and checkpoint (key to return to, or "LAST" = last checkpoint)

Revision rounds: never rewrite the N() calls above a round marker. Append a block per round:

    # ======================================================================
    # vN STRUCTURAL EDITS (round-N reviews)
    # ======================================================================
    _K = K()
    _K["C11"]["links"] = L(("C13", "If you have TRUCE", "has:TRUCE"), ("C14", "Otherwise", "not:TRUCE"))
    retarget("C15", "C18"); drop("C15")
    N("G48", 3, "Gate", "anomaly", ...)          # new sections are appended

so every structural decision stays readable, in order, with the review round that caused it.
"""
from engine.graph import StoryBuilder

B = StoryBuilder(stats=("fear", "vig", "doom"))
N, L, drop, retarget, K, S = B.N, B.L, B.drop, B.retarget, B.K, B.S

V = "D_VIGOUR"   # shared death: Vigour reaches 0 (global rule)
X = "E_DOOM"     # shared ending: Doom or Fear reaches its limit (global rule)

# ======================================================================
# ACT 1 - skeleton (replace with the real structure; keep the shapes)
# ======================================================================
A, Z = 1, "Opening"
N("A01", A, Z, "story", "Arrival",
  "Establish the place, the companion, the clock and the wrongness in one image.",
  [("A02", "Continue")], notes="Section 1.")
N("A02", A, Z, "choice", "The cupboard",
  "A first real choice with a visible cost and an invisible one.",
  [("A03", "Take the torch"), ("A04", "Leave it and keep moving")])
N("A03", A, Z, "item", "Torch",
  "You take the torch. Note the TORCH.",
  [("A05", "Continue")], gain=["TORCH"])
N("A04", A, Z, "story", "Dark",
  "Without light, something learns your name. Gain 1 Fear. Add 1 to your Doom.",
  [("A03", "Go back for the torch")], fear=1, doom=1)
N("A05", A, Z, "choice", "The door marked 0",
  "The rules page said: never open a door marked 0.",
  [("D01", "Open the door marked 0"), ("A06", "Walk past it"), ("E_LOST", "Sit down and wait for morning")])
N("D01", A, Z, "death", "Behind the door",
  "A complete little horror story with a final image.",
  [], warn="Rule: never open a door marked 0.", clue=["A01"], checkpoint="A05", doom=1)
N("A06", A, Z, "combat", "The thing in the corridor",
  "Combat. THE THING   NERVE 7   VIGOUR 7",
  [("E_TRUE", "If you win", "win"), (V, "If your Vigour reaches 0", "lose")],
  test=dict(type="combat", foe="THE THING", nerve=7, vig=7))
N("E_TRUE", A, Z, "ending", "ENDING: Morning", "The true ending.", [])
N("E_LOST", A, Z, "ending", "ENDING: Waiting", "A quiet, sad ending.", [])
N(X, A, Z, "ending", "ENDING: Taken", "Global rule: Doom 5 or Fear at its limit.", [])
N(V, A, Z, "death", "Spent", "Global rule: Vigour 0.", [], warn="Vigour 0 (rules page).", checkpoint="LAST")
