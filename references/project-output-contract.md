# Project output contract

## Required handover contents

- A real project directory and optionally a ZIP containing that directory.
- `README.md` with project purpose, research gap, data provenance/licences, environment, exact run steps, outputs, status and limitations.
- Research problem, aims/questions, dataset selection rationale and a pre-analysis protocol.
- Dataset register, data dictionary, raw data where lawful, processed data, checksums and cleaning log.
- Executable, traceable scripts and/or notebooks with dependencies and recorded software versions.
- Result tables, figures, logs, diagnostics and a validation matrix.
- One authoritative standalone final report file (PDF preferred; otherwise one complete alternative format).
- Citations and attribution for literature and datasets.

## Recommended folder structure

```text
project-name/
├── README.md
├── CITATION.cff
├── LICENSES/
├── environment.yml
├── research/
├── data/raw/
├── data/processed/
├── scripts/
├── notebooks/
├── results/tables/
├── results/figures/
├── results/validation/
├── logs/
└── report/final_report.pdf
```

Adapt based on the study. Do not add empty files solely to mimic this tree. If raw data cannot be retained, document the restriction and provide an authorised retrieval route.

## Required report content

1. Title, date, version and execution status.
2. Executive summary.
3. Background, importance, current evidence and specific gap.
4. Aims, questions and hypotheses.
5. Dataset sources, provenance, licences, populations, coverage and limitations.
6. Detailed step-by-step methods, including data processing and model specifications.
7. Assumptions, bias risks, ethics/privacy, missingness and generalisability.
8. Results with actual tables/figures, sample sizes, units and uncertainty.
9. Validation tests and their statuses.
10. Discussion, alternative explanations and relation to prior evidence.
11. Limitations and unresolved issues.
12. Proportionate conclusions and recommendations.
13. Reproducibility instructions and references.

## Execution status vocabulary

- `COMPLETE — EXECUTED AND VALIDATED`: all essential steps ran and no critical validation failure remains.
- `PARTIAL — EXECUTED WITH LIMITATIONS`: substantive analysis ran but some essential scope or checks remain incomplete.
- `BLOCKED — NOT EXECUTED`: a critical dependency prevented analysis.
- `DESIGN ONLY — NOT EXECUTED`: a project design/protocol exists but data analysis has not run.
