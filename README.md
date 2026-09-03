# Neuroscience Agent Skills

Reusable AI agent skills covering a neuroscience research lifecycle: finding
datasets, governing rigorous data analysis, capturing literature into notes,
writing up results, and funding the next project.

## Skills

| Skill | Function | Output |
|---|---|---|
| [`neuroscience-database-lookup`](neuroscience-database-lookup/SKILL.md) | Finds neuroscience datasets, data portals, educational anatomy resources, visual stimuli, and data descriptor article fallbacks across OpenNeuro, OSF, Figshare, Dryad, Harvard Dataverse, Science Data Bank, Zenodo, Scientific Data, TDBRAIN, Human Connectome Project, BRAVA, NITRC ICBM MRA, Oliva Lab, TEMCA2/FAFB, and BrainFacts 3D Brain. | Ranked dataset links, repository/access notes, DOI/accession IDs, file formats, licenses, citations, and article fallbacks when direct data links are unavailable. |
| [`scientific-research-data-analysis`](scientific-research-data-analysis/SKILL.md) | Governs hypotheses, datasets, preprocessing, exclusions, statistics, null models, permutation tests, instrument validation, provenance, result interpretation, lab journals, theory updates, and analysis audits — drafts a complete, degree-of-freedom-labeled proposal for one-pass approval, reserving upfront confirmation for the scientific target and expensive/irreversible compute. | Frozen analysis plans, data contracts, configs, validation checks, controls, result manifests, audit notes, and restrained interpretation summaries. |
| [`obsidian-literature-notes`](obsidian-literature-notes/SKILL.md) | Converts papers, PDFs, articles, web pages, pasted text, empirical studies, reviews, methods papers, and theory papers into Obsidian-compatible literature notes with rigorous, field-by-field methodology extraction. | Vault-ready Markdown with YAML frontmatter, tags, wikilinks, source metadata, structured methods, results, limitations, and reproducibility gaps. |
| [`scientific-article-writing`](scientific-article-writing/scientific-article-writing/SKILL.md) | Takes an empirical article from contribution statement to submission-ready manuscript and reviewer response — an evidence ledger that locks data, citations, and claim strength, section-by-section moves, and a voice modeled on four high-impact neuroscience exemplars. | Drafted or audited sections, a submission checklist, and a structured author-confirmation/next-step summary. |
| [`dfg-grant-writing`](dfg-grant-writing/SKILL.md) | Guides DFG (German Research Foundation) grant proposals end-to-end — eligibility and programme choice, section-by-section drafting against the current form revision, budget/module selection, and integrity rules against invented citations or unattributed text. | Section drafts, a pre-submission checklist, budget justifications, and reviewer-proofing notes anchored to the current elan form version. |

> `scientific-article-writing`'s installable folder sits one level deeper
> (`scientific-article-writing/scientific-article-writing/`); the outer folder
> also carries a `.skill` zip package, a test suite, and pressure-scenario
> benchmarks. It isn't committed to this repo yet.

## Using these skills

Each entry above is a self-contained, droppable skill folder — copy it (or
this whole repo) into your agent's skills directory, for example
`~/.claude/skills/`. Skills trigger automatically when a request matches
their `description`; read a skill's own `SKILL.md` for its exact scope and
any reference files it loads on demand.
