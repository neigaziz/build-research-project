# Scientific methods, bias control and validation checklist

Use this as a pre-analysis and post-analysis review. It is a prompt for design-specific reasoning, not a substitute for discipline-specific standards or expert review.

## Before analysis

- [ ] The research problem, practical/scientific importance and evidence gap are explicitly stated.
- [ ] The question is answerable using observed variables, population, geography and time period in the selected data.
- [ ] The study purpose is correctly classified: descriptive, associational, predictive, causal, forecasting or exploratory.
- [ ] The unit of observation, sampling unit, target population and estimand are defined.
- [ ] Primary outcomes and exposures/predictors are operationally defined with units and coding.
- [ ] Inclusion, exclusion, censoring and duplicate rules are specified before examining headline effects.
- [ ] The model matches outcome scale, sampling design, dependence, time/spatial structure and study purpose.
- [ ] Confounding, selection, measurement and information bias are considered; causal identification assumptions are stated where relevant.
- [ ] Sample size/precision and limitations are explained.
- [ ] Missing-data, outlier, transformation, multiplicity and sensitivity plans are documented.
- [ ] Prediction workflows define leakage-safe splits and an appropriate baseline.
- [ ] Planned deviations and exploratory analyses can be distinguished from primary analyses.

## Data quality

- [ ] Source/version/licence and checksums are recorded.
- [ ] Schema, units, coding and data dictionary agree with actual files.
- [ ] Duplicates, missingness, impossible values, outliers and coverage are inspected.
- [ ] Joins and their cardinality are validated; no unexplained row multiplication occurs.
- [ ] Raw data remain immutable and cleaning decisions are logged.
- [ ] Potential sampling/selection bias, measurement changes and representativeness limits are documented.
- [ ] Privacy and data-governance risks have been assessed.

## After analysis

- [ ] The pipeline runs from a clean/restarted state and output files can be regenerated.
- [ ] Model diagnostics and convergence/warnings are reviewed.
- [ ] Effect estimates, units, denominators and uncertainty are checked.
- [ ] Sensitivity analyses and baselines are reported as planned.
- [ ] Multiplicity and exploratory inference are handled transparently.
- [ ] Prediction validation avoids leakage and reports appropriate performance/calibration.
- [ ] Causal claims do not exceed the identification design and assumptions.
- [ ] Key results are independently spot-checked or compared against a suitable external benchmark where one exists.
- [ ] Scientific plausibility is assessed with domain knowledge and source documentation.
- [ ] Failed checks, unexpected outcomes and deviations remain visible.
- [ ] Tables, figures and the final report are generated from saved analysis outputs.
- [ ] Conclusions distinguish evidence, uncertainty, interpretation and what cannot be concluded.

## Red flags requiring investigation

- An effect is implausibly large, precise or perfectly predictive.
- A model converges only after undocumented exclusions or transformations.
- Data are split randomly despite repeated observations, related subjects, sites or temporal prediction.
- Variables recorded after the outcome are used to predict it without a defensible reason.
- Statistical significance is the only criterion for choosing the model or reporting results.
- A causal claim is based only on observational correlation or covariate adjustment.
- Rows disappear after merging without accounting for them, or the join creates unexpected duplicates.
- A licence is unclear, or public download is treated as permission to redistribute.
- The report includes numbers, plots or citations that cannot be traced to saved files and sources.
