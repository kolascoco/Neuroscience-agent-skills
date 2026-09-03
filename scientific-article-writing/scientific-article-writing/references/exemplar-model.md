# Exemplar model: empirical articles in high-impact neuroscience venues

A structural model built from four published empirical articles by reading their sections and labeling what each paragraph does. It records functions, orders, and conventions, not sentences. Do not reproduce wording from the sources, and do not treat their claims, citations, or methods as the author's content.

Machine-readable form: `assets/exemplar-journal-model.json`. Validate with `scripts/validate_writing_model.py` after any edit.

## Sources

| Locator | Venue and type | Why included |
|---|---|---|
| 10.1016/j.neuron.2017.06.041 | Neuron, full article, hypothesis-driven fMRI with a new model | Theory-first introduction with numbered hypotheses tested in order |
| 10.1016/j.cub.2020.02.065 | Current Biology, short report, TMS plus fMRI | Merged Results and Discussion; causal design and causal language |
| 10.1038/s41467-023-36805-5 | Nature Communications, article, fMRI pattern similarity | Short conceptual abstract, exploratory analyses labeled, extended discussion |
| 10.1162/imag_a_00349 | Imaging Neuroscience, research article, TMS-EEG across three experiments | Numbered IMRaD with separate Limitations, Implications, and Conclusions; replication structure |

Confidence labels: `high` = all four papers, `medium` = three or venue-specific but consistent, `low` = one or two.

## Front matter

**Title** (high). One of three forms: a declarative finding with the design signaled by a word like "causal" only when the design is interventional; a noun phrase naming the phenomenon and its setting; or a gerund phrase naming what the paper characterizes or discovers. Ten to fifteen words. No abbreviations except field-universal ones.

**Abstract** (high). Six functions in fixed order: established context (one or two sentences) -> unresolved question, usually signaled by a contrast word -> what this study did, often opened with a locative "here" construction -> specific, directional findings naming which system did what -> a synthesizing conclusion, usually signaled by a summative adverb -> significance or implication. Length ranged from about 150 words (conceptual, few numbers) to about 300 words (numbers, n, latencies, and an explicit implications sentence). Venue determines which end of the range.

**Highlights and blurb** (medium; Cell Press venues). Four bullets, each a finding, each under the character limit. A blurb in third person naming the authors, the approach, and the main conclusion.

## Introduction

**Opening** (high). First sentence is concrete and readable by any neuroscientist: a general truth about the phenomenon, a common contrast between lab and real-life conditions, or the technique and what it produces. None of the four opened with a universal claim about importance.

**Paragraph functions in order** (high):

1. territory and why it matters;
2. what is known, synthesized by idea with grouped citations;
3. the unresolved issue, frequently framed as two competing accounts or as a known limitation of prior methods;
4. an explicit statement of what is unknown and why it matters;
5. present study: aim, approach in one to three sentences, and predictions.

**Explicit predictions** (high). All four state what pattern would support which account. Two use numbered hypotheses; Results then uses the same numbering or order. One states the prediction as a conditional: if account A, expect X; if account B, expect Y.

**Theory-first variant** (low). One paper proposes a unified theory in the Introduction with a schematic figure and six numbered requirements, then tests each in a Results subsection. Use only when the materials contain a theory of that scope.

**Length** (high). Four to seven paragraphs. The short report used two framing paragraphs inside the merged Results and Discussion.

## Methods

**Placement** (high). Full Methods after the Discussion in three of four venues; Cell Press uses a structured "STAR Methods" block with a key resources table, contact statement, subject details, method details, quantification and statistical analysis, and data and code availability.

**Participants paragraph** (high). Recruitment source; number recruited; screening criteria listed; number excluded with reasons; final n with age mean and SD and sex; ethics body; consent; safety guideline compliance for stimulation studies.

**Procedure** (high). Chronological by session, with timings in ms or s, trial counts per condition, and counterbalancing.

**Acquisition parameters** (high). Scanner or amplifier with manufacturer and model; sequence or sampling parameters listed inline; electrode or coil positioning and neuronavigation; site coordinates in a standard space.

**Preprocessing** (high). Ordered steps with software and version, artifact-removal method, rejection thresholds, interpolation, filtering parameters, referencing. Two papers cite a prior pipeline paper and link to code.

**Analysis** (high). Outcome measure definitions with formulas when non-standard; model specification; statistical test with assumption checks, sphericity or normality corrections, multiple-comparison correction, permutation details; explicit labeling of exploratory and control analyses; rationale sentences for non-obvious choices.

**Availability** (high). Repository URLs for data and code; raw data on request where restricted.

## Results

**Organization** (high). Subsection per figure or per experiment. Headers are declarative claims in two papers, precise noun-phrase analysis names in one, and numbered experiment labels in one. Order follows the hypotheses.

**Orienting paragraph** (medium). A short first paragraph restating the design in two sentences, reporting behavioral sanity checks, and pointing to Methods and supplementary material.

**Paragraph anatomy** (high). Aim -> approach -> result with inline statistics and figure callout -> one-sentence takeaway. The takeaway is interpretive but bounded, typically introduced by a summative adverb and a hedged verb.

**Statistics inline** (high). Test statistic with degrees of freedom, p value, and effect size where available; correlations with r and p; corrected pairwise comparisons named with the correction; null results reported with the same completeness. Exact p values except when very small.

**Control and replication structure** (high). Each primary result is followed by a control analysis addressing the obvious alternative, and, where available, replication in an independent sample or experiment is reported as replication. Exploratory analyses are labeled as such.

**Cross-referencing** (high). Main figures by number and panel; supplementary figures and tables; Methods subsections by name.

**Interpretation inside Results** (high). One sentence per paragraph is standard; extended interpretation is deferred to Discussion except in the merged-format short report.

## Discussion

**Opening** (high). A findings-summary paragraph: what was done, then the main findings, sometimes enumerated. No stronger verbs than in Results.

**Relation to prior work** (high). Explicit replicated / extended / did-not-replicate statements with the specific methodological difference that explains a discrepancy.

**Interpretation and alternatives** (high). The author's account, then the alternative accounts and what argues against them; open possibilities stated as such with a proposed test.

**Limitations** (high). Each limitation is a four-part unit: the limitation, why it matters for which claim, what was done to mitigate, and what future work should do. One paper uses a separate numbered Limitations section with five items; the others fold limitations into interpretive paragraphs.

**Implications** (medium). A separate section in the methods-focused paper; a closing paragraph elsewhere. Implications for study design and for between-group comparisons are stated conditionally.

**Subheadings** (medium). Thematic subheadings in the two longest discussions.

**Conclusion** (high). One paragraph or a short section: the answer to the question, the contribution, and its scope. Two papers enumerate the reasons the conclusion holds.

## Figure legends

**Structure** (high). Title sentence that states the finding or names the content; panel-by-panel description; what error bars or shading represent; n; significance markers defined; cross-references to supplementary figures.

## Language functions observed (describe, do not copy)

The full sentence-level style inherited from these papers is in `style-guide.md`. The list below is the short form.

- Locative openers to mark the present study's action in the abstract and introduction.
- Summative adverbs to introduce the takeaway sentence after evidence.
- Contrast adverbs at paragraph or sentence start to mark a competing result or account.
- Attention markers (`notably`, `critically`, `importantly`, `of note`) used sparingly, at most once or twice per section, to flag the result that matters most for the argument.
- Hedged verbs (`suggest`, `likely reflect`, `is consistent with`, `may`) for interpretation; causal verbs (`causally establish`, `demonstrate`) only in the interventional design.
- Explicit uncertainty statements (`we cannot rule out`, `it is possible that`) paired with the test that would resolve them.
- Numbered lists inside prose to enumerate findings, reasons, or limitations.

## Exceptions and variation

- Merged Results and Discussion in short reports; Introduction compressed to two paragraphs at the section's start.
- Abstract numbers: absent in the short conceptual abstract, present in the long methods-focused abstract.
- Separate Limitations, Implications, and Conclusions headings in one venue; folded elsewhere.
- Theory-proposing Introduction in one paper only.

## Boundaries

- The model is copyright-safe: no paragraph text, phrase bank, or reusable sentence is stored.
- The model describes what these venues did, not what any venue requires. Confirm against the target journal's author guidelines.
- A paper's data, claims, citations, mechanisms, and limitations never transfer to the author's manuscript.
