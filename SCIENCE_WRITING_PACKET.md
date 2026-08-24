# Science-writing packet

Every manuscript must be auditable as a scientific argument before it is polished as prose.

## Required manuscript packet

1. One-sentence research question and one-sentence answer the paper is designed to support.
2. Contribution table separating: established prior art; synthesis or taxonomy; protocol/design choice; formal result; implementation result; human-subject or field evidence.
3. Claim ledger mapping each consequential statement to a primary source, derivation, test, dataset, or explicit open hypothesis.
4. Closest-work matrix with feature-level comparisons and dated source checks.
5. Methods/evaluation plan with baselines, negative controls, adversarial cases, uncertainty, and stopping criteria.
6. Limitations, trust boundaries, ethical risks, and plausible failure modes.
7. Reproducibility package that records source, environment, configuration, randomness, compute, data identity, and review sign-off at the level appropriate to the work.
8. Authorship and AI-assistance record approved by the human authors and compatible with venue policy.

## Claim labels

- **P — Prior work:** directly supported by cited primary literature or a normative standard.
- **D — Definition/design:** a declared protocol or modeling choice; it must not be presented as an empirical fact.
- **T — Theoretical result:** supported by a stated model and derivation or proof.
- **E — Empirical result:** supported by a versioned dataset, analysis, uncertainty statement, and reproducible run.
- **I — Implementation result:** supported by versioned code and tests; does not by itself establish scientific or social efficacy.
- **H — Hypothesis/open question:** explicitly unresolved.

## Review gates

- **G0 Argument:** the outline forms a valid chain from question through evidence to bounded conclusion.
- **G1 Scholarship:** primary sources cover the closest work; synthesis is not mislabeled as invention.
- **G2 Methods:** proposed tests could falsify the important claims and include adversarial cases.
- **G3 Artifact:** code/data/protocol versions are immutable or explicitly draft; checks run from documented commands.
- **G4 Independent review:** at least one reviewer outside the drafting lane challenges novelty, methods, and limitations.
- **G5 Human release:** authorship, ethics, licensing, fees, and submission are explicitly approved.

Automation may flag missing evidence, inconsistency, or failed tests. It cannot certify scientific validity or replace G4/G5.
