# scientific-article-writing

An Agent Skill that takes an empirical scientific article from contribution statement to submission-ready manuscript, and then through reviewer response. Built from three sources:

1. **Editorial guidance for premier journals** (LaPlaca, Lindgreen & Vanhamme, 2018) and the cognitive writing framework in Douglas (2015), via the `academic-writing` skill: contribution first, body before front matter, section dos and don'ts, and a five-dimension prose pass.
2. **The evidence-preserving mechanisms** of the `science-research-writing` skill in Yila-AI/awesome-research-skills: evidence ledger, claim-strength ladder, stage routing, output contract, and deterministic invariant checks.
3. **A structural and stylistic model of four high-impact empirical neuroscience articles** (Neuron 2017, Current Biology 2020, Nature Communications 2023, Imaging Neuroscience 2024): section moves, figure-first Results, four-beat paragraphs, limitation units, and the sentence-level voice. Stored as functions with locators, never as copied prose.

## Layout

```text
scientific-article-writing/          the installable skill (drop this folder into any skills directory)
  SKILL.md                           entry point: principles, routing, section moves, voice, audit, output contract
  references/
    evidence-contract.md             what may never change without author authorization
    workflow.md                      six phases from contribution brief to submission audit
    sections.md                      reader question, moves, don'ts, and audit for every section
    exemplar-model.md                structural model of the four exemplar articles
    style-guide.md                   sentence-level voice inherited from the exemplars
    prose-quality.md                 coherence, clarity, continuity, concision, cadence
    reporting-standards.md           statistics, sample, acquisition, availability, guidelines
    submission-checklist.md          pre-submission checklist, cover letter, reviewer response
  assets/
    contribution-brief.md            the four questions plus figure-first storyboard
    manuscript-skeleton.md           one row per paragraph, prefilled with default moves
    figure-legend-template.md
    exemplar-journal-model.json      machine-readable model, validated
  scripts/
    prose_diagnostics.py             sentence-length variance, intensifiers, nominalizations, style signals
    check_draft_invariants.py        numbers, citations, protected terms, claim-strength markers
    validate_writing_model.py        schema check for the JSON model
  agents/openai.yaml
scientific-article-writing.skill     zip package of the folder above
tests/                               unit tests for structure, model, and scripts
benchmarks/pressure-scenarios.md     five RED/GREEN scenarios for agent testing
```

## Install

Copy or unzip the `scientific-article-writing/` folder into your agent's skills directory, for example `~/.claude/skills/`. Or install the `.skill` package where your client accepts one.

## Use

```text
Use $scientific-article-writing. Here are my materials and target journal;
help me get this to a submission-ready draft.
```

The skill reads the materials, infers the contribution brief, routes by manuscript stage, and returns a draft or diagnosis, how it is organized, one author confirmation, and one next step.

## Test

```bash
python3 -m unittest discover -s tests
python3 scientific-article-writing/scripts/validate_writing_model.py scientific-article-writing/assets/exemplar-journal-model.json
```

## Rebuild the package

```bash
rm -f scientific-article-writing.skill
zip -q -r -X scientific-article-writing.skill scientific-article-writing -x '*.DS_Store' -x '*__pycache__*'
```
