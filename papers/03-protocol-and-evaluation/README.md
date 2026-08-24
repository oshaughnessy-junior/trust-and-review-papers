# Paper 03 — Protocol and reference evaluation

Status: **private compile-ready first draft** (16 pages on 2026-08-24). It is
not approved for submission or public release.

Working title: **Plural Trust Without a Global Reviewer Score: A Conformance
Profile and Adversarial Evaluation Plan for Machine-Verifiable Scientific
Review**.

## What this draft now contains

- a primary-source-bounded novelty boundary;
- TDRG objects, typed events, local views, bridges, forks, authority separation,
  and result-promotion rules;
- a threat model with explicit trusted-operator and residual-risk language;
- a complete TM-01--TM-18 conformance/adversarial roadmap;
- a preregistrable A0--A4 comparison with H1--H6 kept as open hypotheses;
- an exact subtest-level account of the v0.1 tooling slice at full revision
  `9da0cd433147d925bac4ae1e1f94186cc4166e7b`;
- the locally rerun 11-test evidence, separated from every unimplemented
  security, privacy, identity, comparative, interoperability, and field claim;
- multiaxis reproduction resources and claim-scoped downselect modes; and
- machine-readable writing, logical-claim, citation, and claim-ledger artifacts.

## Compile

From this directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The current compiled PDF is `build/main.pdf`. Generated `build/` products are
ignored by the repository and are not manuscript sources.

## Verification

```bash
python3 ../../../../skills/scientific-writing/scripts/validate_writing_artifact.py \
  writing-packet.json logical-claims-audit.json
python3 ../../../../skills/cite-and-verify/scripts/validate_claim_ledger.py \
  claim-ledger.json
python3 ../../../../skills/read-compile-latex/scripts/summarize_errors.py \
  build/main.log
```

Bibliography and citation receipts are summarized in
`bibliography-audit.txt`, `citation-verification-report.json`, and
`verification.md`. Official web standards were manually checked at their
authoritative pages when scholarly-article indexes were inapplicable.

## Evidence boundary

The current implementation evidence is only the 11 unit tests named in Table 2
and `verification.md`. In particular, the draft does **not** assert signatures,
identity uniqueness, Sybil or collusion resistance, anonymity or unlinkability,
appeals/opening, fork reconciliation, standards round trips, A0--A4 outcomes,
field efficacy, reviewer competence, or scientific validity.

## First unmet evidence gate

**G1 scholarship remains open:** the current primary-source audit is bounded,
not a systematic or independently reviewed closest-work search. G2 also remains
open because normative schemas, the full conformance suite, estimands, thresholds,
seeds, and stop rules have not been frozen. No empirical result should be added
until those gates are closed.
