---
name: scientific-article-writing
description: Use when a researcher needs to plan, draft, revise, or audit an empirical scientific article for a peer-reviewed journal, including the contribution statement, title, abstract, highlights, introduction, methods, results, discussion, limitations, conclusion, figure legends, cover letter, or a response to reviewers, from raw materials, a partial draft, or a full manuscript.
---

# Scientific Article Writing

Turn research materials into a manuscript that reviewers can accept and readers can follow. Three rules govern every deliverable:

1. **Contribution first.** A paper is an argument that one specific thing is now known. Every section either builds that argument or is cut.
2. **Evidence faithful.** The author's data, citations, limitations, and claim strength are immutable unless the author authorizes a change. Fluent prose is not permission to invent or inflate.
3. **Reader's brain last.** Once the content is right, shape every paragraph so a distracted reviewer gets the point on a skim.

The workflow, section moves, and prose rules come from three sources: editorial guidance for premier journals (LaPlaca, Lindgreen & Vanhamme, 2018), the cognitive writing framework in Douglas (2015), and a structural model of empirical articles in high-impact neuroscience venues described in `references/exemplar-model.md`. Read that model as a set of observed functions, never as sentences to reuse.

## Load only what is needed

- Always read `references/evidence-contract.md`.
- Read `references/workflow.md` when starting a paper, choosing writing order, or unsure what to produce next.
- Read `references/sections.md` for the section being written or revised.
- Read `references/exemplar-model.md` when the target is a high-impact empirical venue or the user supplies no journal.
- Read `references/style-guide.md` when drafting or revising any sentence; it carries the voice inherited from the exemplar articles.
- Read `references/prose-quality.md` before any sentence-level revision and during the final prose pass.
- Read `references/reporting-standards.md` when drafting Methods, Results, figure legends, or back matter.
- Read `references/submission-checklist.md` before declaring a draft submission-ready or when answering reviewers.
- Use `assets/contribution-brief.md`, `assets/manuscript-skeleton.md`, and `assets/figure-legend-template.md` as fill-in structures.

## First response: inspect, then act

Read everything supplied before writing. Establish privately:

- manuscript stage: idea, materials, partial draft, or full draft;
- the job: plan, draft, revise, audit, or respond to reviewers;
- the contribution brief: what is new, who cares and why, the single core finding, the target venue and article type;
- the protected facts: numbers, statistics, citations, instruments, group labels, null results, limitations, author judgments.

Infer the brief from the materials when possible and state the inference. If the target journal is unknown, use the generic high-impact empirical model and say so. Never require a form. If a missing fact would force an unsupported scientific choice, deliver every safe part first, then ask one highest-impact question.

If the contribution cannot be stated in one sentence from the materials, that is the first deliverable: a diagnosis of the contribution problem, not prose that hides it.

## Route the task

| Stage | Default path |
|---|---|
| Idea only | Contribution brief -> questions the study must answer -> materials checklist |
| Materials, no draft | Brief -> figure-first storyboard -> skeleton -> draft body sections in order -> audit |
| Partial draft | Audit against brief and evidence -> plan -> revise -> audit |
| Full draft | Audit first: title and abstract promises, results-discussion boundary, loop closure, claim strength -> revise only what the audit or user identifies |
| Reviewer comments | Response protocol in `references/submission-checklist.md` |

Write body before front matter: Methods -> Results -> Discussion -> Introduction -> Conclusion -> Abstract -> Highlights -> Title. The title and abstract advertise work that must already exist. When the user asks for one section, draft that section, but note any promise it makes that the rest of the paper must keep.

## Build the evidence ledger

Before drafting or revising, classify every consequential statement as `user_data`, `author_judgment`, `user_citation`, `structural_transition`, or `author_confirmation`. Follow `references/evidence-contract.md`.

Never silently add data, methods, mechanisms, citations, limitations, implications, or recommendations. Never silently move a claim on the strength ladder. When a conventional slot is empty, leave a labeled gap or request the author's input. Preserve null, negative, and adverse findings.

## Write by information function

Each section answers a reader question through a fixed sequence of moves. Full guidance is in `references/sections.md`; the defaults are:

| Section | Reader question | Default moves |
|---|---|---|
| Title | What does this paper promise? | Fewest words that state the finding or question, population, and design when it changes inference |
| Abstract | Should I read this? | Context -> gap -> what was done here -> specific findings -> calibrated conclusion -> implication |
| Introduction | Why was this needed? | Territory -> what is known -> competing views or unresolved issue -> the gap and why it matters -> present study with explicit predictions |
| Methods | What exactly was done? | Participants and exclusions -> materials -> procedure in order -> acquisition -> preprocessing -> analysis and statistics -> availability |
| Results | What was found? | One claim per subsection; each paragraph: aim -> approach -> result with statistic and figure -> one-sentence takeaway |
| Discussion | What does it mean and not mean? | Findings summary -> relation to prior work -> interpretation at supported strength -> alternatives -> limitations with consequences -> implications -> bounded conclusion |
| Conclusion | What can the evidence support? | Answer the question at evidence level; no new claims, no summary of the paper |

Results headers state claims, not topics. Each Results subsection maps to one figure or table. The Discussion opens by restating the findings, closes the loop on every question the Introduction raised, and introduces no new terms.

## Write in the inherited voice

Draft in the voice of the exemplar articles, described move by move in `references/style-guide.md`:

- first-person plural, past tense for what was done, present tense for what the evidence shows;
- a concrete first sentence, then paragraphs that each end on a contrast pivot naming what is unresolved;
- the unresolved question stated as a closed set of alternatives, with conditional predictions before the design;
- Results paragraphs that open with the question (`We next asked whether`), state the reasoning (`We reasoned that if ..., then ...`), report the effect with its direction (`such that ...`, `driven by ...`), keep parallel syntax across parallel analyses, give null results their statistics, and close with one summative sentence hedged to the design;
- Discussion paragraphs that place each finding as replicated, extended, or not replicated, raise the alternative account in its own sentence and bound it, draw the claim's scope in the authors' own words, and end the paper on a principle stated with a modal verb;
- attention markers rationed to one to three per section; connectives only where the logical relation is real.

Style moves shape sentences the materials already support; they never license new content.

## Prose pass, after content is audited

Apply `references/prose-quality.md` in this order: coherence (front-load the governing idea at document, section, and paragraph level), clarity (subject and verb close and early, action verbs, concrete subjects), continuity (familiar to new, stable subjects, key term repeated not paraphrased, emphasis at sentence end), concision (cut amplifiers, throat-clearing, redundant modifiers, self-mentions), cadence (vary sentence length on purpose).

Prose rules never override the evidence contract. A hedge is semantic content; a repeated technical term is correct, not clumsy; an intensifier without a number is a defect.

## Audit every draft

Before returning text, check against the materials:

- every number, unit, statistic, sample size, time point, figure reference, and citation marker;
- every protected name, instrument, dataset, variable, and group label;
- direction of every effect, including null and adverse ones;
- association, prediction, and causation boundaries against the design;
- consistency of title, abstract, results, discussion, and conclusion;
- that no sentence from an exemplar or target paper was reused.

When local source and draft text exist, run `scripts/check_draft_invariants.py` as a first pass and `scripts/prose_diagnostics.py` on the draft; the latter also reports style signals (question-driven openers, stated reasoning, directional effect phrasing, summative closers, paragraphs ending on a statistic). Passing scripts are necessary, not sufficient; review semantics and citation scope by hand.

## Refusal boundary

Do not fabricate citations, hide null results, remove limitations, convert association into causation, or strengthen claims beyond the evidence. Explain the mismatch and offer the strongest evidence-faithful alternative.

## Red flags: stop and re-read the contract

| Thought | Reality |
|---|---|
| "The Discussion looks thin, add a standard limitation" | A limitation the author did not document is fabricated content. Ask for it. |
| "Reviewers expect a mechanism here" | Only author-supported interpretations enter the paper. Leave a labeled gap. |
| "The abstract needs a number to sound concrete" | Use supplied numbers only. A number the materials do not contain is invented. |
| "One significant and one null result means A matters more than B" | That contrast needs a direct test. Report each separately. |
| "Writing the abstract first will clarify the story" | Write the contribution brief instead. Abstract comes last. |
| "This design is basically causal" | Causal verbs need an intervention design. Observational data gets associational verbs. |
| "A synonym avoids repeating the term" | Repeated key terms reduce reader load. Synonyms add it. |
| "This sentence is fine, but a journal-style rewrite would look better" | If the prose is clear and faithful, return it unchanged. |

## Return a novice-readable result

Use this order:

1. `Draft or diagnosis` — the usable text, plan, or prioritized problems.
2. `How it is organized` — the move sequence in two or three sentences.
3. `Author confirmation` — the single decision or missing fact, or `None required`.
4. `Next step` — one action that advances evidence or author review.

Add `Risk flags` only when a real evidential, claim-strength, citation, or boundary risk exists. Never begin `Next step` with an offer; state the one thing that moves the manuscript forward.
