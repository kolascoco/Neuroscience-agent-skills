# Reporting standards

What Methods, Results, legends, and back matter must contain so that a reviewer can evaluate and a reader can replicate. Use only values the author supplies; a missing item becomes an `[author to confirm: ...]` marker, never a default.

## Statistics in prose

Report, in one sentence with the comparison:

- the test and its statistic with degrees of freedom, for example `t(36) = 2.53`, `F(1, 19) = 5.66`, `χ²(3) = 15.58`;
- the p value, exact to two or three decimals, or `p < 0.001` for very small values; never `p = 0.000`;
- an effect size when available: Cohen's d, partial eta squared, r, odds ratio, beta with SE or CI;
- uncertainty: 95% CI or SEM, stating which;
- the correction for multiple comparisons and the corrected threshold;
- assumption checks and any correction applied (sphericity, normality, non-parametric alternative).

Null results receive the same completeness. `Not significant` alone is not a result.

Report the direction and the comparator: which condition was larger, relative to what, at which time point.

## Sample reporting

- Number recruited, number excluded with reasons, number analyzed.
- Age mean and SD, sex or gender as recorded, handedness where relevant.
- Trials per condition after rejection, as mean and SD or range.
- Any per-participant tailoring (thresholds, set sizes, intensities) and its rule.

## Design reporting

- Factors and levels; within- or between-subject; counterbalancing and randomization; blinding.
- Control conditions and what each controls for.
- Prespecified versus exploratory analyses; preregistration link if any.
- Power or sample-size justification when the author supplies it; otherwise mark for confirmation.

## Acquisition reporting

Equipment with manufacturer and model; recording parameters (sampling rate, filters, reference, impedance for EEG; TR, TE, voxel size, slices, flip angle, multiband factor for MRI); targeting method and coordinates in a named space; stimulation parameters (intensity rule, pulse shape, coil type and orientation, timing relative to task); sensory or environmental controls (masking, spacer, shielding) with how their level was set.

## Preprocessing reporting

Ordered list of steps with software and version, artifact-removal methods with parameters, rejection criteria and how many items were rejected, interpolation, filtering parameters, referencing, normalization template. Cite the pipeline paper only if the author did; link the code repository if provided.

## Figures and tables

- Every figure earns one claim; the claim is the legend's first sentence.
- Axis labels with units; condition labels identical to the text.
- Error bars or shading defined; n stated; significance markers defined in the legend.
- Individual data points where the venue expects them.
- Tables for values the text cannot hold; do not repeat a table in prose.
- Supplementary figures for controls, replications, and exploratory analyses; reference each from the main text.

## Reporting guidelines by design

Point the author to the guideline that matches the design and check the manuscript against it:

| Design | Guideline |
|---|---|
| Randomized trial | CONSORT |
| Observational study | STROBE |
| Systematic review or meta-analysis | PRISMA |
| Animal research | ARRIVE |
| Diagnostic accuracy | STARD |
| Prediction model | TRIPOD |
| Neuroimaging (fMRI, MEG, EEG) | COBIDAS reports |
| Brain stimulation | Field safety and reporting checklists for TMS and tES |

## Back matter

- **Data availability:** repository, accession or DOI, access conditions; if restricted, what is available from whom.
- **Code availability:** repository URL and version or tag.
- **Author contributions:** CRediT roles or venue format.
- **Funding, competing interests, ethics, acknowledgements:** as supplied; never invented.

## Common reviewer catches

- p values without test statistics or effect sizes.
- Exclusions without counts or reasons.
- Software without versions.
- Correction method unspecified for multiple comparisons.
- A null result described as a trend.
- Figures whose condition labels differ from the text.
- Availability statements that promise more than the repositories hold.
