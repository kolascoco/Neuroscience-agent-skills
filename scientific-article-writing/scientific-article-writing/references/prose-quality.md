# Prose quality

Based on the cognitive writing framework in Douglas (2015), *The Reader's Brain*, and the editorial guidance in LaPlaca, Lindgreen and Vanhamme (2018). Readers predict, verify, infer, and store as they read. Every sentence that breaks a prediction forces a rewind. Academic prose is engineering to reduce that cost.

Apply this file only after the content audit passes. Prose rules never change scientific content; see `evidence-contract.md`.

## Order of operations

Coherence outranks the rest. A reader who does not know the governing idea cannot be rescued by clean sentences.

```text
coherence -> clarity -> continuity -> concision -> cadence
```

## 1. Coherence: front-load at every level

- **Document.** The abstract and the Introduction's final paragraph tell the reader the whole argument before the evidence.
- **Section.** The first sentence of a section says what the section does.
- **Paragraph.** The first sentence is the topic sentence: the governing idea, then its development. In Results, the aim beat is the topic sentence; in Discussion, the claim is.
- **Breaks.** New paragraph at every shift in angle: a new implication, a different study, a contrasting view. Paragraph breaks signal cognitive transitions.
- **Distracted readers.** Reviewers read many manuscripts. Short paragraphs and visible structure let a skimmer form a correct impression.

**Test:** read only the first sentence of each paragraph. Does the argument survive?

## 2. Clarity: sentence-level

- **Subject early, verb close.** Separating subject from verb loads working memory. If a subject needs a long qualifier, move the qualifier after the verb.
- **Action verbs.** Replace nominalizations (`the implementation of`, `an examination of`, `the establishment of`) with the verb (`implemented`, `examined`, `established`).
- **Concrete subjects.** `This finding suggests` beats `The theoretical implications of this finding are that`.
- **Active by default, passive by purpose.** Use passive when the acted-upon element is the familiar information the sentence should start with, or when Methods convention prefers it. Passive is a tool, not an error.
- **No garden paths.** If the reader can parse the sentence two ways, rewrite it. Read aloud; where you stumble, so will the reviewer.

## 3. Continuity: sentence to sentence

- **Familiar to new.** Begin with what the reader already holds; end with the new information.
- **Emphasis position.** The end of the sentence is what readers retain. Put the finding there, not a qualifier.
- **Stable subjects.** Keep the same grammatical subject across sentences about the same actor. Switching subjects forces reorientation.
- **Deliberate repetition.** Repeat the key term. A synonym for a technical term forces the reader to check whether it means the same thing. Elegant variation is a defect in scientific prose.
- **Transitions that name a relation.** `However`, `therefore`, `in contrast`, `consistent with` each assert a logical relation; use one only when the relation is real. Do not rely on transitions alone to create flow.
- **Continuity can override clarity.** If flow requires passive voice, use it.

## 4. Concision: cut what competes for working memory

| Category | Cut | Replace with |
|---|---|---|
| Redundant modifiers | `completely eliminate`, `future prospects`, `past history` | drop the modifier |
| Negative constructions | `not uncommon`, `did not ignore` | `common`, `addressed` |
| Amplifiers | `very significant`, `extremely important`, `highly novel` | drop the amplifier, or give the number |
| Non-quantitative intensifiers | `dramatic`, `massive`, `enormous`, `considerably`, `substantially` | the magnitude, effect size, or nothing |
| Throat-clearing | `It is worth noting that`, `It should be mentioned that`, `As mentioned above` | delete |
| Self-mentions without work | `We believe that`, `The authors think` | state the claim; keep `we` where it marks the study's action |
| Latinate for plain | `utilise`, `facilitate`, `demonstrate` (as show) | `use`, `help`, `show` |
| Promotional adjectives | `groundbreaking`, `novel` (unverified), `remarkable`, `unprecedented` | delete or verify |

Prefer shorter, familiar words, especially verbs. Keep every technical term the field uses; concision never simplifies terminology.

## 5. Cadence: rhythm signals control

- Vary sentence length on purpose: some short (5 to 10 words), most medium (15 to 25), an occasional long one (30 or more) for a complex argument. All short reads abrupt; all long buries structure.
- Vary structure: open occasionally with a participial phrase, a subordinate clause, or an inversion. Not every sentence is subject-verb-object.
- Read the paragraph aloud before finalizing; awkward rhythm is felt even in silent reading.

## Calibration rules specific to scientific prose

- **Hedges are content.** `May`, `suggests`, `is consistent with`, and `likely` mark epistemic strength. Never cut them for concision; never add them for caution. Match the design.
- **Attention markers are rationed.** `Notably`, `critically`, `importantly`: at most once or twice per section, on the result the argument depends on.
- **Numbers stay with their comparison.** Estimate, uncertainty, and comparator in the same sentence.
- **Terminology is fixed by Methods.** Group labels, condition names, and variable names used in Methods are used unchanged everywhere.
- **Figure callouts in the sentence that makes the claim,** not appended to the paragraph.

## Paragraph diagnostic

Before finalizing each paragraph:

1. Does the first sentence state the governing idea?
2. Does each sentence begin with familiar information from the previous one?
3. Does the most important information in each sentence land at the end?
4. Are key terms repeated rather than paraphrased?
5. Is every sentence necessary, or does something exist only for the author's comfort?
6. Any intensifier without a number? Any hedge changed?
7. Read aloud: any stumble?

## Document diagnostic

1. Can a reviewer read only the first sentence of each paragraph and grasp the argument?
2. Does the abstract front-load findings?
3. Does every section open by saying what it does?
4. Are paragraphs short enough to skim?
5. At the end of each page: what on this page convinced the reviewer this deserves publication? If nothing, revise the page.

## Deterministic helper

```bash
python3 scripts/prose_diagnostics.py draft.md
```

Reports sentence-length statistics per paragraph, flagged intensifiers and promotional words, throat-clearing phrases, nominalization candidates, passive-voice candidates, hedge density, and paragraphs whose first sentence is very long. The report locates places to inspect; it does not license changes that the evidence contract forbids.
