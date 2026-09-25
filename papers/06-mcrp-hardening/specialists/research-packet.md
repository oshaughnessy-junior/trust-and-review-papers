# Research packet — bounded contestability

Date: 2026-09-25. No human or legal release approval recorded.

## Contribution table

| Category | Contribution | Status / boundary |
|---|---|---|
| Established prior art (P) | US intermediary/copyright frameworks; EU rights and notice processes; human responsibility in venue policy | Sources below; applicability remains unresolved |
| Synthesis/taxonomy (D) | Four-coordinate state separates scientific status, visibility, participation, identity opening | Composes existing MCRP/TDRG distinctions; not a claim of novel access-control theory |
| Protocol/design (D) | Small common intake; existing three appeal lanes plus operator compliance track; one ordinary appeal | Proposed pilot choices; law and material new evidence can require additional process |
| Formal result (T) | Finite-capacity impossibility; geometric appeal-workload calculation; write-set invariant | Elementary derivations under stated assumptions; no new queueing theorem claimed |
| Implementation (I) | Executable arithmetic and backlog fixtures | Toy reference model only; no Commons service implementation |
| Human-subject/field evidence (E) | None | All efficacy claims remain H |

## Consequential claim ledger

| ID | Claim | Label | Evidence / falsifier |
|---|---|---|---|
| L01 | A service action can be prevented from changing unauthorized status coordinates | D/T | Write-set definition; enforce authorization at each mutation; counterexample is any cross-coordinate write accepted |
| L02 | Unlimited distinct substantive complaints cannot have guaranteed finite-period service with finite labor and positive minimum cost | T | Paper §4.2 inequality; fails only if assumptions fail |
| L03 | Depth-bounded ordinary appeal limits per-case expected handling in the declared model | T | Geometric-series derivation; `capacity_model.py`; excludes novel reopenings and intake flood |
| L04 | Mean load below capacity does not guarantee tail latency | T | Deterministic arbitrarily large burst counterexample; no specific queue distribution assumed |
| L05 | Rights intake should not depend on subscription, paid graph access, or scientific reputation | D | Normative pilot invariant; DSA can independently impose relevant requirements when applicable |
| L06 | Content visibility is not scientific disposition | D | Existing publication policy/TDRG synthesis; state model |
| L07 | Stable prototype pseudonyms do not satisfy fresh per-case persona design | I/D | Prototype README vs TDRG §5.1; documentary comparison, not live deployment test |
| L08 | Founder-only moderation cannot furnish independent review of founder decisions without another controller | D/H | Definition of independence; real operational adequacy unmeasured |
| L09 | §230 has exceptions and does not prove blanket immunity | P | Source S1; no application conclusion |
| L10 | Copyright notice/counter-notice has distinct legal conditions and timing | P | S2–S3; full operational process requires counsel |
| L11 | EU applicability and micro/small service classification are conditional | P | S6–S7; operator facts missing |
| L12 | Opinion label is not categorical protection against factual defamation | P | S5 Court opinion; not a current jurisdiction-specific litigation analysis |
| L13 | Human legal/venue authorship differs from agent contribution attribution | P/D | S4, S8; actual rights/venue policy must be assessed |
| L14 | Bounded contestability improves retention, trust, or fairness | H | Requires human pilot with baseline and subgroup outcomes; not established here |
| L15 | Anonymity and metadata separation survive realistic attacks | H | Requires deployed threat-model testing; no guarantee from paper or queue code |
| L16 | Public record availability may be restricted without claiming the historical decision never occurred | D | Proposed projection/retention architecture; applicable obligations and sensitive identifiers require review |

## Closest-work matrix

Source checks performed 2026-09-25; this matrix compares functional features, not priority of invention.

| Closest structure | Feature already present | Proposed composition / gap | Source |
|---|---|---|---|
| MCRP publication policy | Exact release bindings, independent verifier, correction, sensitive-content removal | Extend operational case state and resource accounting | Local `_pages/publication-policy.md` |
| TDRG v0.1 draft | Three appeal lanes, scoped trust, conflict rules, threshold opening | Preserve those lanes; add separately scoped operator compliance routing and explicit appeal labor envelope | Local shared/protocol/reviewer-trust-domains-v0.1-draft.md |
| Commons prototype | Report/correction/hide, separate paid plan/capability, founder moderation | Free quota-independent rights path, independent alternate, workload ledger, persona reconciliation | Local prototype README; documented features only |
| DMCA §512 | Statutory notice/counter-notice and conditional safe harbors | Keep legally defined process distinct from ordinary scientific appeal; no substitute process proposed | S2–S3 |
| DSA notice and complaint framework | Accessible notice, reasons, conditional free internal complaint rights, abuse safeguards | Applicable-law overlay; ordinary budget cannot displace required rights | S7 |
| GDPR | Personal-data processing duties and conditional rights/research provisions | Public/private projection design avoids assuming public log immutability wins | S6 |
| ICMJE venue rules | Human responsibility and AI assistance disclosure | Export agent contribution without asserting AI author eligibility | S8 |
| ORI/institutional process | Institution-specific misconduct handling | Scoped referral rather than MCRP global misconduct jurisdiction | S9 |

## Review gates

G0: argument drafted. G1: primary legal/institutional sources checked, but not exhaustive doctrinal literature or current jurisdiction-specific counsel analysis. G2: falsifiable synthetic and human evaluation plan drafted. G3: toy deterministic arithmetic executed; no product conformance. G4: independent critique requested by parent orchestration, not yet recorded in this packet. G5: not approved.

## Reproducibility and methods boundary

`python3 capacity_model.py` emits synthetic workload JSON. No external dependencies, network, private data, or random draws. Parameters are explicit in code. Seed is not applicable. The fixtures measure arithmetic and accounting, not adjudicator behavior or legal compliance. Save Python version and output when integrating; parent repository commit supplies source identity. No model execution results should be presented as observations of actual Commons users.
