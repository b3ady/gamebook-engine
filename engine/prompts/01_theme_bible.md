# Brief: the writer's bible for {{TITLE}}

You are developing the writer's bible for **{{TITLE}}**, an interactive {{GENRE}} novel in
{{SECTION_COUNT}} numbered sections, Fighting Fantasy style: the reader is "you", plays with dice
and an Adventure Sheet, and turns to numbered sections. It will be sold as a Kindle ebook and read
mostly on phones. The premise from the author:

> {{PREMISE}}

Write `{{BOOK_DIR}}/BIBLE.md`. It is the law for every writer, reviewer and auditor that follows,
so it must be specific enough to settle arguments. Use this outline (it is the one that worked for
The Layover; keep every heading):

1. **The pitch in one breath.** The book must be two things at once: a genuinely frightening
   {{GENRE}} story **and** a human story (a relationship that can be repaired or lost). Say both.
   Every scene with the companion character should move the second story a step.
2. **Voice and prose rules.** Second person, present tense. Short paragraphs (1–4 sentences, ≤60
   words). Concrete over abstract. Every section opens anchored to where the reader just was (it must
   flow from *every* section that links to it) and ends on a hook. Choices in the reader's voice. Dialogue
   carries the relationship (subtext, jokes, things said by accident). Banned clichés (list them).
   Spelling standard. Lengths per kind: story/choice 130–280 words; tests and small consequences 80–150;
   deaths 90–170, each a complete little horror story with a final image; endings 220–420.
3. **Characters.** "You" (never physically described; what you carry, your secret, what you are bad at).
   The companion: arc in one line (e.g. cold → sharp → frightened → leaning on you → furious → forgiving
   if earned), their armour, what they won't say until late, the one line they save for the true ending.
   The dead/absent person at the centre, with one real flaw. Minor characters: one human leak each.
4. **Setting.** A real-feeling place made slightly wrong. The deadline (a time on a clock). One motif
   object per act. Gate/door/number puzzles that the fixed section numbers will use.
5. **The entity.** What it is (never stated plainly before a named late section), what it wants, how
   it is written early (one detail at a time, never named), its **rules** — 4–6, each also a survival
   tip the reader can learn and use — and the **one rule it breaks once, late**, to reset predictions
   before the finale. Its tell (the Layover's: the smile is right, the eyes are frightened; it uses your
   full name, the real person never did). It never roars or runs; politeness is the threat.
6. **Reader variants** (optional): what the reader chooses before section 1 (e.g. son / daughter /
   neither), the exact inline variant format, and the *only* sections allowed to use it (max ~6).
7. **Mechanics language (exact phrasing).** Token links `turn to {KEY}`; conditional links; tests
   ("Test your Nerve. If you succeed, turn to {X}. If you fail, turn to {Y}."); foe lines
   (`THE THING   NERVE 7   VIGOUR 7`); effects stated where they happen ("Gain 1 Fear." "Note the codeword
   TRUCE." "Cross off the VOUCHER."); global rules never linked (limit endings, stat deaths) except where
   the structure prints them; hidden puzzle links never written as tokens; lore woven into prose, never
   labelled.
8. **Motifs to weave** (5–8), and which ending pays each off.
9. **Output format for drafting agents**: `{"KEY": "text with {TOKENS}", ...}`, `\n\n` between
   paragraphs, choices as their own final paragraphs, *asterisks* for signs/announcements/handwriting,
   no headings, no numbers.

Also start `{{BOOK_DIR}}/CANON.md`: a bullet list of facts that must never contradict (ages, names,
dates, the one true account of the backstory, which line is said only once and where). Writers append
to it; reviewers check against it.

Then write a half-page **design questions** list for the author: every choice you made that changes
the book (who the companion is, the entity's nature, the tone of the true ending, the variant choice,
the countdown mechanic's name). **Stop and wait for the author's answers** before the structure stage.
