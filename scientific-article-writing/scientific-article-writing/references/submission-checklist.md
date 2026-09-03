# Submission checklist and reviewer response

Run before declaring a manuscript submission-ready. Every unchecked item is a `Risk flag` or a `Next step`.

## Contribution

- [ ] The contribution is stated in one sentence in the Introduction's final paragraph.
- [ ] The Discussion demonstrates that the contribution was delivered.
- [ ] "So what?" is answered for a reader outside the sub-field.
- [ ] The work is not purely descriptive without theoretical or methodological consequence, an exact replication presented as novel, or a salami slice.

## Front matter

- [ ] Title written last; tested on uninvolved readers; no unverified `novel`, `first`, `comprehensive`; no causal verb for a non-interventional design.
- [ ] Abstract written last; follows the venue format; leads with context and gap, spends most words on specific findings, ends with a calibrated conclusion; contains no claim absent from the paper.
- [ ] Highlights and blurb, if required, contain only abstract-level claims within character limits.
- [ ] Keywords reflect essential topics, not broad terms; follow venue rules on repeating title words.

## Structure

- [ ] Introduction: territory -> known -> unresolved -> gap and stakes -> present study with predictions; at most about two pages.
- [ ] Hypotheses: non-obvious, singular, directional, framework-derived, powered.
- [ ] Methods: reproducible from the text; every parameter, version, count, and threshold present or marked for confirmation.
- [ ] Results: one claim per subsection, headers state claims, four-beat paragraphs, controls and replications reported, exploratory analyses labeled, null results visible.
- [ ] Discussion: opens with findings summary; every Introduction question answered; prior work related with specific differences; alternatives addressed; limitations as four-part units; no new terms or results.
- [ ] Conclusion: answers the question at evidence level; does not summarize; no reflexive hedging and no inflation.
- [ ] Figure legends stand alone; condition labels match the text.

## Evidence

- [ ] `check_draft_invariants.py` passes between materials and draft, or every difference is explained.
- [ ] Claim-strength markers unchanged from the author's, or every change authorized.
- [ ] Title, abstract, results, discussion, and conclusion agree on direction, magnitude, and scope.
- [ ] No exemplar or target-paper sentence reused.

## Prose

- [ ] Each paragraph opens with its governing idea.
- [ ] Subject and verb close in every sentence; nominalizations converted where the verb exists.
- [ ] Key terms repeated, not paraphrased.
- [ ] No non-quantitative intensifiers in Results, Discussion, or Conclusion.
- [ ] Sentence length varies; read-aloud pass done.
- [ ] `prose_diagnostics.py` report reviewed.

## Journal fit

- [ ] Length within limits for text, abstract, figures, tables, and references.
- [ ] Section headings and order match the venue (merged Results and Discussion, structured Methods block, separate Limitations, and so on).
- [ ] Reference style and citation format match.
- [ ] Reporting guideline for the design checked.
- [ ] Data and code availability, author contributions, funding, competing interests, and ethics statements present as supplied.
- [ ] Abbreviations defined at first use in abstract and main text.
- [ ] No excessive self-citation.

## Reviewer-proof page test

At the end of every page ask: what on this page convinces a reviewer this manuscript deserves publication? If nothing, revise the page.

## Cover letter

Three short paragraphs: the question and why it matters to this venue's readers; the core finding and what it changes; fit with the venue and any required declarations. No claims beyond the abstract.

## Responding to reviewers

Principles:

1. **Every comment gets a response**, numbered to match the review, quoting or paraphrasing the comment first.
2. **Answer, then locate.** State what was changed and where (section, page, or line), or explain why no change was made.
3. **Evidence over assertion.** A disagreement is answered with data, analysis, or literature the author supplies, not with restated opinion.
4. **Concede real problems plainly.** A limitation the reviewer identified becomes a limitation paragraph, not a defense.
5. **New analyses follow the evidence contract.** Report them with the same completeness as the original Results; label them as added at review.
6. **Tone is collegial and brief.** Thank once at the top, not per comment. No sarcasm, no flattery.
7. **Track consistency.** A change requested in one section must propagate to abstract, title, figures, and conclusion.

Response unit:

```text
Reviewer N, comment K
[Comment, quoted or condensed]

Response
[What was done or why not, with evidence]

Changes
[Section and location of each revision]
```

Do not invent analyses, citations, or results to satisfy a reviewer; if the request cannot be met with the available materials, say so and offer the strongest honest alternative.
