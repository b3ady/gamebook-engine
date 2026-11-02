### A01 — Arrival  [story, Act 1, Opening]
Arrives from: 
Beat: Establish the place, the companion, the clock and the wrongness in one image.
Links (write each target as a token):
  - {A02}  "Continue"  → leads to: The cupboard
Design note: Section 1.

### A03 — Torch  [item, Act 1, Opening]
Arrives from: A02 (The cupboard), A04 (Dark)
Beat: You take the torch. Note the TORCH.
Links (write each target as a token):
  - {A05}  "Continue"  → leads to: The door marked 0
Effects (state them in the text, using in-world names): Note TORCH

### D_VIGOUR — Spent  [death, Act 1, Opening]
Arrives from: A06 (The thing in the corridor)
Beat: Global rule: Vigour 0.
Death — the warning the reader was given: Vigour 0 (rules page).  End: 'Add 1 to your Doom. Return to {LAST} and choose again.'

### A05 — The door marked 0  [choice, Act 1, Opening]
Arrives from: A03 (Torch)
Beat: The rules page said: never open a door marked 0.
Links (write each target as a token):
  - {D01}  "Open the door marked 0"  → leads to: Behind the door
  - {A06}  "Walk past it"  → leads to: The thing in the corridor
  - {E_LOST}  "Sit down and wait for morning"  → leads to: ENDING: Waiting

### E_DOOM — ENDING: Taken  [ending, Act 1, Opening]
Arrives from: 
Beat: Global rule: Doom 5 or Fear at its limit.

### A06 — The thing in the corridor  [combat, Act 1, Opening]
Arrives from: A05 (The door marked 0)
Beat: Combat. THE THING   NERVE 7   VIGOUR 7
Links (write each target as a token):
  - {E_TRUE}  "If you win"  [condition: fight won]  → leads to: ENDING: Morning
  - {D_VIGOUR}  "If your Vigour reaches 0"  [condition: fight lost]  → leads to: Spent
Foe line: THE THING  NERVE 7  VIG 7

### A02 — The cupboard  [choice, Act 1, Opening]
Arrives from: A01 (Arrival)
Beat: A first real choice with a visible cost and an invisible one.
Links (write each target as a token):
  - {A03}  "Take the torch"  → leads to: Torch
  - {A04}  "Leave it and keep moving"  → leads to: Dark

### D01 — Behind the door  [death, Act 1, Opening]
Arrives from: A05 (The door marked 0)
Beat: A complete little horror story with a final image.
Effects (state them in the text, using in-world names): Doom +1
Death — the warning the reader was given: Rule: never open a door marked 0.  End: 'Add 1 to your Doom. Return to {A05} and choose again.'

### A04 — Dark  [story, Act 1, Opening]
Arrives from: A02 (The cupboard)
Beat: Without light, something learns your name. Gain 1 Fear. Add 1 to your Doom.
Links (write each target as a token):
  - {A03}  "Go back for the torch"  → leads to: Torch
Effects (state them in the text, using in-world names): Fear +1; Doom +1

### E_LOST — ENDING: Waiting  [ending, Act 1, Opening]
Arrives from: A05 (The door marked 0)
Beat: A quiet, sad ending.

### E_TRUE — ENDING: Morning  [ending, Act 1, Opening]
Arrives from: A06 (The thing in the corridor)
Beat: The true ending.
