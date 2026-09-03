# Workflow

Six phases. Enter at the phase that matches the manuscript stage; never skip the contribution brief.

## Phase 1: Contribution brief

Answer four questions from the materials before writing prose. Use `assets/contribution-brief.md`.

1. **What is genuinely new?** Not merely unstudied; new and consequential. Novelty alone does not justify a paper.
2. **Who cares, and why?** The theoretical stake and, where the venue expects it, the practical or clinical stake.
3. **What is the single core finding?** One sentence a reader could repeat. If there are three, the paper is either three papers or has not found its spine.
4. **Which venue and article type?** The venue sets length, abstract format, section headings, whether Results and Discussion merge, and whether highlights or a summary blurb are required.

A brief that cannot answer 1 to 3 is the first deliverable. Say so plainly; polishing prose around a missing contribution wastes the author's time and invites desk rejection.

## Phase 2: Figure-first storyboard

Strong empirical papers are organized around figures. Before the skeleton:

- list every figure and table the materials support;
- write the one-sentence claim each figure earns;
- order them so each claim sets up the next, matching the order of hypotheses if the paper is hypothesis-driven;
- mark which claims are primary, control, replication, or exploratory.

Each figure-claim pair becomes one Results subsection with a declarative header. A claim without a figure or table needs one or needs to move to supplementary. A figure without a claim is cut or merged.

## Phase 3: Skeleton

Fill `assets/manuscript-skeleton.md`: one row per paragraph with reader question, information function, supporting evidence, and status. The skeleton is where the argument is checked before sentences exist:

- the Introduction's final paragraph must promise exactly what the Results deliver;
- every question the Introduction raises must have a Discussion paragraph that answers it;
- every limitation must trace to a specific design feature and a specific claim it bounds;
- the conclusion must not exceed the strongest Results claim.

## Phase 4: Draft the body, then the front matter

Order: Methods -> Results -> Discussion -> Introduction -> Conclusion -> Abstract -> Highlights or summary blurb -> Title.

Why this order works:

- Methods exist already; writing them first fixes terminology, group labels, and analysis names for every later section.
- Results written before Discussion keep interpretation out of Results.
- Introduction written after Results promises only what was delivered.
- Abstract and title written last cannot over-promise.

When the user asks for a single section, draft it and add a `Risk flags` note listing any promise it makes elsewhere in the paper.

## Phase 5: Prose pass

Only after the content audit passes. Apply `references/prose-quality.md` paragraph by paragraph. Run `scripts/prose_diagnostics.py` on the draft for sentence-length variance, intensifiers, throat-clearing, nominalizations, and hedge density. Treat the report as a list of places to look, not as instructions to change every flagged token.

## Phase 6: Submission audit

Run `references/submission-checklist.md`. Confirm journal fit: length, abstract format and word limit, heading requirements, figure count, reference style, reporting guideline, data and code availability, author contributions, competing interests.

## Revising an existing draft

1. Reconstruct the contribution brief from the draft. If the draft does not state it, that is finding one.
2. Audit before editing: title and abstract promises against Results; Results-Discussion boundary; Introduction questions against Discussion answers; claim strength against design; visibility of null results.
3. Fix structure before sentences. Reordering paragraphs is cheaper and more valuable than polishing paragraphs that will move.
4. Then apply the prose pass.
5. Return unchanged prose that is already clear and faithful. Do not offer an optional cosmetic alternative.

## Writing order for a merged Results and Discussion

Some short-format articles merge the two sections. Keep the discipline anyway: each paragraph is either evidence or interpretation, and the interpretive sentence follows its evidence within the same paragraph. Open the merged section with a compact framing paragraph that does the Introduction's gap-and-approach work in a few sentences, then move through figure-claim pairs. Close with two or three interpretive paragraphs that relate the findings to prior work and state the bounded contribution.

## When to stop and ask

Ask one question, after delivering everything safe, when:

- two sources give different numbers for the same result;
- the design cannot be identified and the choice changes causal language;
- the Discussion needs prior literature, an interpretation, or a limitation the author has not supplied;
- the requested venue requires a structure the materials cannot fill.

Never ask the user to choose an internal mode or fill an intake form.
