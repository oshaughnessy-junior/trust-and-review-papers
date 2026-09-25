# Paper 02 — Formal dynamics of localized trust domains

Working title: **Trust Without a Global Score: Localized, Typed, and Forkable Reviewer Networks**

Status: compile-ready private theory/model first draft. The manuscript is not submission-ready and contains no analytical, simulation, pilot, or field result.

## Contents

- `main.tex`: full manuscript, including definitions, candidate propositions, planned evaluation, no-go regimes, and explicit evidence gates;
- `references.bib`: paper-local primary/canonical bibliography;
- `writing-packet.json`: scientific-writing scope and evidence record;
- `logical-claims-audit.json`: rhetorical and logical-strength audit;
- `claim-ledger.json`: consequential-claim support ledger;
- `OUTLINE.md`, `MODEL.md`, and `CLAIMS.md`: upstream design inputs;
- `VERIFICATION.md`: compile, bibliography, semantic-artifact, and visual-QA record.

## Compile

From this directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The repository ignores `build/` and generated PDFs.

## Claim posture

The document distinguishes:

- definitions and design choices;
- candidate propositions that remain proof obligations;
- open hypotheses about feedback, localization, and trade-offs;
- planned simulations and their preregistered observables; and
- actual results, of which there are currently none.

The first unmet evidence gate is a checked analytical result or informative counterexample. Candidate Proposition 1 needs a proof or counterexample under the exact bridge transition semantics; Candidate Proposition 2 needs machine-readable dependency semantics and deterministic replay. The feedback model also needs state-space, stability, and finite-size analysis. No comparative policy claim is allowed until faithful A0–A4 implementations have been run on identical frozen inputs.
