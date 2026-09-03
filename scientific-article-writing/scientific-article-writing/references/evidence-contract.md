# Evidence contract

The author's materials are the authority. Drafting, revising, and polishing never change scientific content unless the author supplies evidence and explicitly authorizes the change.

This contract adapts the Evidence-Preserving Draft Contract and Claim-Strength Contract from [Yila-AI/awesome-research-skills](https://github.com/Yila-AI/awesome-research-skills). Credit them if you reuse this file.

## Ledger

Before writing, classify each consequential statement:

| Source type | Meaning | Handling |
|---|---|---|
| `user_data` | A result, number, procedure, or observation in the materials | Preserve exactly |
| `author_judgment` | An interpretation, mechanism, or implication the author stated | Preserve at stated strength |
| `user_citation` | A cited proposition the author supplied | Keep attached to its proposition |
| `structural_transition` | Connective prose with no scientific content | Free to write |
| `author_confirmation` | Something the section conventionally needs but the materials lack | Label the gap; do not fill it |

Keep the ledger private unless the user asks how a statement was sourced. Use `[author to confirm: ...]` markers only where a visible gap helps more than omission.

## Tier 1: exact-token invariants

Preserve unless the author explicitly corrects them:

- integers, decimals, ranges, percentages, signs, dates, time points, latencies, frequencies;
- units, doses, intensities, thresholds, voxel sizes, sampling rates;
- sample sizes, recruited versus analyzed counts, exclusion counts, group labels;
- test statistics, degrees of freedom, p values, confidence intervals, effect sizes, correction methods;
- instrument, software, atlas, dataset, model, task, and stimulus names and versions;
- in-text citations, citation groups, figure, table, and supplementary references.

## Tier 2: semantic invariants

Preserve:

- who did what to whom, with which comparator, on which outcome;
- direction of every effect and the visibility of null, negative, and adverse results;
- association versus prediction versus contribution versus causation;
- observed result versus author interpretation versus prior literature;
- exploratory versus confirmatory, prespecified versus post hoc;
- scope: sample, setting, species, task, time window, stimulation site, validation status;
- limitations, exceptions, and the reach of the conclusion.

## Claim-strength ladder

```text
is consistent with / may suggest
< is associated with / relates to / correlates with
< predicts
< contributes to
< affects / modulates / leads to
< causes / demonstrates that / establishes
```

Field conventions vary the exact order, but a draft never moves a claim silently in either direction. Causal verbs require a design that manipulates the cause, such as stimulation, lesion, pharmacology, or randomized intervention. Observational or correlational designs stop at association or prediction unless the author authorizes otherwise and the field accepts it.

Hedges are content. Preserve or query changes to `may`, `might`, `could`, `suggests`, `appears`, `likely`, `is consistent with`, `did not`, `only`, `within this sample`, `at this site`, and `under these conditions`. Do not add hedges mechanically; match the design and analysis.

## What is never added silently

- results, analyses, or numbers absent from the materials;
- methods detail filled in from field defaults;
- mechanisms, alternative explanations, or confounders the author did not name;
- citations, including ones that "must exist";
- limitations invented to satisfy a convention;
- implications, recommendations, or future studies the author did not propose;
- a contrast between two variables inferred from one significant and one non-significant test;
- target-paper or exemplar language, arguments, or field assumptions.

A design label authorizes only its direct boundary. Cross-sectional data permit "causality cannot be inferred"; they do not permit a specific reverse-causality story. Absence of a control condition permits "we cannot rule out X" only when the author names X.

## Null and adverse findings

- Keep every null result with its outcome, comparison, time point, and statistic.
- Do not relabel non-significant as a trend unless the author does.
- Do not drop a finding because it complicates the story; complicating findings are often the ones reviewers check first.

## Authorization protocol

When a stronger, weaker, or additional claim may be scientifically appropriate:

1. show the current evidence-faithful wording;
2. name the proposed movement on the ladder or the proposed addition;
3. state what evidence or author judgment would justify it;
4. wait for explicit authorization before changing the manuscript.

## Conflicting sources

When tables, figures, prose, and notes disagree, quote both versions, say what is blocked, continue with unaffected content, and ask which source is authoritative. Do not choose silently, insert `[A or B]`, or invent a table reference.

## Deterministic first pass

For local text, run:

```bash
python3 scripts/check_draft_invariants.py case.json
```

with a JSON case containing `source`, `draft`, and `protected_terms`. The script compares numbers, citation markers, protected terms, and claim-strength markers. It cannot judge negation, comparator direction, citation scope, or limitation reach; audit those by hand every time.
