# Scientific-writing structural review

Date: 2026-08-24  
Disposition: **credible private outline program; no paper is submission-ready**

The persistent `science-writer` gateway request and its embedded fallback timed out without producing edits or a report. To avoid falsely recording an agent review, this assessment was performed by directly applying the shared `scientific-writing` and `cite-and-verify` skills. A later independent science-writer close read remains required at G4.

## Program-level assessment

The sequence has a coherent dependency chain: conceptual consolidation → formal result → protocol/evaluation → independent-actor pilot → software paper after maturity. The outlines consistently separate design choices from results and include stop conditions. The main weakness is evidentiary, not structural: primary-source support checks, theory/simulation outputs, protocol test coverage, and human evidence remain incomplete.

Machine-readable artifacts are in `science-writing/`:

- `writing-packet.json` records audience, evidence packets, constraints, excluded claims, and human questions.
- `claim-ledger.json` blocks five consequential program claims at their present evidence strength.
- `logical-claims-audit.json` distinguishes program implications, hypotheses, local implementation observations, and paper descriptions.

## Per-paper gates

| Paper | G0 argument | G1 scholarship | G2 methods | G3 artifact | G4 independent review | G5 human release | Disposition |
|---|---|---|---|---|---|---|---|
| 01 Design map | pass for outline | pending primary-source gap audit | proposed worked cases and falsifiers | outline artifacts present | pending | pending | begin source-verified drafting only after G1 |
| 02 Formal dynamics | pass for model outline | pending focused theory audit | blocked on proof/counterexample and deterministic A0–A4 simulations | model specification only | pending | pending | research program, not results paper |
| 03 Protocol/evaluation | pass for outline | partial; closest-work refresh pending | full TM-01–TM-18 roadmap; current implementation covers a bounded subset | v0.1 local prototype and tests, not archived | pending | pending | draft methods after test artifact IDs stabilize |
| 04 Sociotechnical pilot | pass as preregistration outline | pending sociotechnical/ethics literature expansion | blocked on ethics, independent control, recruitment, and preregistration | no study artifact | pending | pending | no results language admissible |
| 05 Software | not applicable | not started | not applicable | maturity gate not met | pending | pending | correctly deferred |

## Concrete next evidence

1. Paper 01: primary-source identity and sentence-level support ledger; standards crosswalk; two end-to-end worked cases with explicit claim coverage.
2. Paper 02: prove, refute, or narrow the candidate bound; freeze deterministic simulations and public/synthetic inputs; report negative regimes.
3. Paper 03: version schemas and fixtures; close the current TM subset with immutable run artifacts; implement or explicitly defer the remaining privacy/governance claims.
4. Paper 04: expand primary literature; obtain ethics/IRB determination; define independent domain control and adverse-event governance before recruitment.
5. Paper 05: wait for release, archive, maintainers, documentation, tests, external users, and meaningful human design evidence.

## Human questions

- Who accepts authorship responsibility for each article and what AI-assistance disclosure will be used?
- Does the design-map synthesis have enough standalone value to lead, or should the sequence wait for the formal result?
- Which venues remain no-fee or RIT-covered for the exact article type at submission time?
- What privacy, appeal, and management-power failures would stop a pilot even if routing metrics improve?
