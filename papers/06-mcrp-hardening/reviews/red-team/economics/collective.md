# Collective-round economics position

25 September 2026. Reviewed the revised integrated `SYNTHESIS.md`, `protocol/minimal-profile.md`, README, relevant revised specialist sections, all four original adversarial reports, and fixed economic solver. This is a second same-model/operator critique, not external validation. References below are to `papers/06-mcrp-hardening/` in the candidate repository unless stated otherwise.

## Agreed core after cross-disciplinary deliberation

The dossier is defensible as a conditional research synthesis and synthetic test package. It is not a deployed publication institution, an empirically effective mechanism, or verified independent governance. The integrated main now says this clearly. The useful proposal is a portable, scoped reliance boundary with a small participant interface, simple constrained assignment first, and explicit responsibility for amendment. More mathematical machinery should earn its additional human cost against the structured-template baseline.

The key joint result is a **conjunction of feasibility constraints**, not one scalar trust score: a scientifically appropriate check must also have qualified labor, actual independence where required, authorized decisions, usable evidence, currentness under a stated policy, and lawful handling. None of the separate equations supplies the others. Four action labels compress interaction; they do not remove these constraints.

The games adversary and I specifically agree that retries, refusals, re-invitations and tied-up reservations belong in the same person/skill/epoch budget. Reporting a fair distribution at the offer boundary does not establish fairness among completed reviews. Group-panel allocation must freeze group-level evidence, eligibility and resources under redundant label cloning; selecting representatives first and summing their weights can reintroduce amplification.

The science adversary and I agree that a newcomer reserve protects **conditional opportunity**, not guaranteed scientifically sufficient service. Supervision requires scarce qualified hours too. If feasible independent coverage is absent, report unavailable or permit an explicitly narrower nonbinding contribution. No scientific argument justifies an unconditional completed-check entitlement. Both peers agree that invitation/eligibility and completion denominators must be reported because declining difficult cases can manufacture apparent accuracy and speed.

## Status of my original findings against the revised candidate

| Finding | Current disposition |
|---|---|
| ECON-01 valid one-lot solver failure | Reproduced as fixed; remaining numerical range limits are explicit failures, below |
| ECON-02 zeros and malformed vectors | Fixed for tested cases, including flat objective with unused budget |
| ECON-03 latent/oracle priority estimates | Main now explicitly chooses conservative random assignment and treats optimization as diagnostic; operational calibration remains research-only |
| ECON-04 hours versus completed coverage | Numerical README retains limitation; add explicit denominators to main pilot paragraph |
| ECON-05 sponsor additionality | Main explicitly says additional capacity must replace no common expertise; H4 before/during remains descriptive, not causal |
| ECON-06 expected penalty semantics | Fixed in integrated economics; audit commitment exogenous |
| ECON-07 reserve stock versus flow | Integrated economics now defines period net reserve contribution; resolved |

## Fixed solver verification and residual limits

Executed `python3 -m unittest discover -s work/trust-and-review-papers/papers/06-mcrp-hardening/models/economics -p 'test_*.py' -v`: all five tests passed. Additional independent calls are recorded in `work/red-team/economics/integrated-results.json`.

- Standard worked example returns approximately `(2.3803652295,1.5418546341,.0777801365)` and totals four hours.
- `([1],[1],100)` returns `[100]`.
- Multiplication-underflow input `([1e-200],[1e-200],1)` returns `[1]`.
- All-zero productivity returns zero effort; mixed zero productivity allocates to the productive task.
- Flat objective with lower bounds `[.2,.3]` and H=1 returns those bounds, correctly leaving .5 unused.
- Mismatched vectors and negative lower bounds now raise explicit `ValueError`.

The fixed solver does not cover every positive finite floating-point parameter combination. With A=(1,1), a=(1e-100,1e-100), H=1 it raises `ArithmeticError` rather than returning the exact mathematical (.5,.5); the fixed 200 log-price bisections do not resolve the required tiny difference. With a=(1e308,1e308), H=10 it explicitly rejects an unrepresentable shadow-price range. These are **fail-closed limitations**, not erroneous accepted answers and not invalidation of the completed ordinary-range sweep. Do not describe the helper as a universal solver. A documented numerical failure status is adequate for this dossier; unrestricted production use would need better scale-aware stopping/bracketing and numerical conditioning work.

## Remaining precise edits to the integrated main

1. **SYNTHESIS “What to build and test next”, pilot metrics:** Add “Report eligible offers, invitations, refusals, retries and completions as separate denominators; report both total and conditional-on-completion outcomes.” Refused work is already mentioned; these explicit units prevent comparing selected easy completions with an unselected conventional arm.
2. **Minimal profile “A simple default allocation policy”:** After reserved newcomer/supervised-review budget, add “The reserve is conditional on feasible qualified supervision; supervisor effort and tied-up reservations share the common capacity ledger. It does not guarantee a completed check when coverage is unavailable.” This is a clarification of existing feasible-coverage semantics, not a demand for another rule table.
3. **Economic results scope / solver README:** State that unsupported numerical scales produce explicit exceptions and the reported sweep only establishes behavior on recorded inputs. No claim of complete floating-point-domain coverage.
4. **Economics H4:** Label before/during campaign measurements descriptive; any causal additionality claim needs a design controlling common demand and qualified capacity changes. The integrated main already uses cautious language, so this is a specialist-methods precision change.
5. **Main pilot plan:** Treat routing, interface and staffing as separate experimental factors, as already proposed, and count all standby/supervision/retry handling rather than only completed tasks. Do not require the paper to solve the entire human study now.

None of these requires discarding the analytical draft. Items 1–3 should be applied before making the final collective statement; item 4 can remain a clearly recorded research-design condition if no causal claim is made.

## Blocking versus research-only issues

**Blocks a live or guaranteed operational claim:** no authenticated end-to-end event lifecycle yet; unestablished group identity and distribution-preserving completed-panel scheduler; no demonstrated joint deadline/capacity controller; no implemented and enforceable independent appeal route; no live freshness guarantee or downstream recipient controls; missing jurisdiction/operator facts. These are not cured by passing Python fixtures.

**Does not block a bounded research dossier:** unknown human uptake, uncalibrated scientific loss/productivity, whether prestige motivates good correction, optimal reserve size, causal sponsorship additionality, and a complete novelty search. The manuscript must retain these as open questions rather than claims. The simple baseline and adversarial examples are useful despite these unknowns.

**Numerical software boundary:** original correctness failures are resolved on regression cases. Extremely scaled finite inputs still explicitly fail; retaining that boundary is acceptable for the synthetic package.

## Peer responses and disagreement record

- **Games:** Accepted its selective-completion objection, representation-invariant group base measure, and need to recompute reset values. The integrated reset equation and panel qualification now address the manuscript errors. We jointly reject a guaranteed newcomer service interpretation when independent supervision is unavailable. No substantive disagreement remains between our lanes on these points.
- **Science:** Accepted hidden-dependency and changing-regime counterexamples. The currentness reference view demonstrates semantics under trusted fixtures, not event authorization or live propagation. We jointly require full selection/completion denominators and conditional newcomer access. No disagreement remains on allowing this bounded analytical dossier while withholding operational assurance.
- **Law:** Read all six objections and observed revised counter-notice, deadline and stop-policy language. I agree that financial resources cannot buy an independent adjudicator where authority/access/reversal is missing, and that protected rights intake can be reachable while infeasible to process. I attempted direct peer messages twice; tool returned “agent thread limit reached.” Sent the position to the root for relay, so do not falsely record direct legal-lane assent pending its response.

A possible unresolved institutional disagreement is how much burden a minimum pilot should take on before accepting any public material. Economics favors a deliberately narrow public/synthetic-artifact service that does not promise funded adjudication it cannot supply. Legal applicability still must be determined for what that service actually does; reducing promises does not cancel duties. This is a launch-scope decision needing concrete operator facts, not a disagreement resolvable through abstract equations.

## Proposed collective language

“The revised dossier supports a scoped protocol proposal, elementary conditional constraints and reproducible synthetic counterexamples. Adversarial review found and prompted corrections to numerical allocation, reset values, representation-sensitive sampling, currentness semantics and operational accounting. It does not establish calibrated allocation, incentive-compatible cooperation, legal clearance, independent governance or field effectiveness. Proceed with the smallest synthetic end-to-end lifecycle and matched simple baselines; retain unavailable and unresolved outcomes wherever required resources, authority or currentness are missing.”

I assent to that statement subject to preserving the recorded residual issues and avoiding a collective-review badge that implies external independence.
