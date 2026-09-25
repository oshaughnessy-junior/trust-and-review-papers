# Cross-review: economics and legal/operations drafts

**Reviewer lane:** game theory and mechanism audit, 25 September 2026. Review of `work/economics/paper.md`, `work/law/paper.md`, and `work/law/capacity_model.py`. No edits were made to those files. This is mathematical and design review, not licensed legal review or verification of legal applicability. Legal propositions retain the source and applicability limits of the legal lane.

## Ranked actionable findings

### R1 — Correct the strict stability necessity statement (material mathematical error)

**Target:** law paper §4.1, “A necessary long-run load condition is rho_N<1.”

**Finding:** Strict inequality is not universally necessary for bounded backlog. Deterministic arrivals of 40 staff-minutes and capacity of 40 each epoch, from zero backlog, have rho=1 and backlog identically zero. This counterexample runs in the submitted code. The economic draft already makes the correct distinction.

**Required correction:** State that load above one cannot be sustained under the specified accounting assumptions; strict slack is the prudent stochastic operating target and is required for conventional stable nondegenerate queue models under their assumptions. Avoid making an unrestricted theorem from a practical target. Neither <=1 nor <1 alone guarantees finite latency in the model currently written.

**Verified:** `backlog([40]*4,[40]*4)` returns `[0,0,0,0]`.

### R2 — Do not treat all refused/duplicate/rights-tagged requests as fixed overhead (material mechanism gap)

**Target:** law §4.1 overhead d and §§3–4 free rights intake; economics §§5.1–5.2 admissions.

**Finding:** The law utilization formula is an accounting identity if d contains actual overhead. As a design forecast it is unsafe when d is treated as a fixed scalar independent of attempted intake. An attacker can submit rejected duplicates or label every item “privacy emergency.” Even if each takes only t>0 staff minutes to classify, attempted rate lambda_try adds at least lambda_try*t; limiting admitted distinct cases does not cap it. Protected legal capacity H_E partitions capacity but cannot guarantee adequacy. Both drafts acknowledge unlimited distinct claims; the equally important attack does not require distinct admitted claims.

**Required correction:** Distinguish automated intake, attempted rights/ordinary triage, admitted substantive cases, and reopened cases. Make d=d(lambda_try, case sizes, classifier error, incident correlations) or explicitly a measured time series. Add a mislabeled-emergency flood fixture and report legal-lane oldest-item age. Fallback contact is an availability route, not infinite service capacity. Admission/aggregation may limit ordinary commitments, but cannot purport to extinguish applicable rights. Specific legal treatment remains for the legal reviewer.

**Counterexample:** H_N=480; four admitted cases cost 180; fixed d=30 suggests utilization .4375. Ten thousand refused items at .1 minute each add 1000 minutes, producing actual ordinary utilization at least 2.4583 if they consume that lane. If they consume the protected lane, that lane fails instead. The numbers are synthetic; the identity is deterministic.

### R3 — Input truncation can make accounting claim success after dropping workload (implementation correctness)

**Target:** `capacity_model.py`, `backlog`.

**Finding:** `zip(work, capacity)` silently drops all unpaired epochs. `backlog([40,999999],[40])` returns `[0]`, losing 999999 minutes from the reported series. Negative or nonfinite work/capacity is also accepted, and invalid appeal probabilities can pass `utilization`. These are not failures for the hardcoded current fixture arrays, but they make the exported helpers unsafe as reusable accounting models.

**Required correction:** Validate equal lengths, finite nonnegative workload/capacity, probabilities in [0,1], finite nonnegative costs, and integer nonnegative appeal depth with explicit exceptions. `assert` is not reliable runtime input validation under optimized Python. Add a mismatch rejection check and adversarial invalid-input fixtures. This is a modest code fix, not a request to expand the model into a production service.

### R4 — Make “bounded handling commitment” executable before claiming an operational bound (mechanism gap)

**Target:** law §§3–4, initial review plus one appeal and reopenings.

**Finding:** A depth cap only bounds ordinary review count per fixed case. Constant c is a model assumption, not a service guarantee: a single appeal can contain arbitrarily much evidence, and a stream of tiny genuinely new evidence updates can reopen a case indefinitely. The paper already caveats these facts, but its operational lifecycle does not yet state who controls the total budget or how bounded triage terminates without implying scientific vindication.

**Required correction:** Specify a case/epoch service envelope, explicit “unresolved at resource boundary” outcome, queued evidence updates that do not each receive immediate fresh review entitlement, maximum ordinary accepted payload/attachment work, and an exception authority for legally required handling. Record new evidence even when it cannot immediately be evaluated. Add a single-case sequential-new-evidence simulation, separate from the duplicate-case attack.

### R5 — Global assignment and noninterference claims need indirect-path tests (integration gap)

**Target:** economics §§1.1 and 7.1–7.2; law coordinate separation.

**Finding:** The economics draft correctly distinguishes payment-independent authority from attention capture. The final deployment invariant must include the path from payment to discovery, workload, nominations, eligibility evidence, and then assignments. Similarly, legal write-set separation prevents direct changes to S but cannot by itself prevent a V-only removal from changing a downstream “currently supported” display if evidence becomes unavailable. This is not necessarily wrong; it must be explicitly modeled as a derived observation, not silent historical scientific reclassification.

**Required correction:** Add a metamorphic fixture changing plan/payment while holding the frozen evidence, policy and eligibility inputs fixed, plus a causal allocation experiment allowing payment-funded submissions and time changes. For legal state, test V-only changes leave historical S unchanged, while a separate evidence-availability observation can open reconsideration without silently deciding it. The distinction belongs in one integration paragraph rather than a new rule table.

### R6 — Clarify the effort model's penalty semantics (minor precision)

**Target:** economics §6.1, “loses at most F” followed by U(e)=w-ce-qd_eF.

**Finding:** The exact utility formula assumes loss F when triggered (or an action-independent conditional expected loss F), not merely a maximum. If F is only a ceiling and actual penalties are tiny, the displayed sufficient incentive conclusion fails. The F_max impossibility conclusion remains valid as a bound.

**Required correction:** Define F as the modeled realized/conditional expected utility loss, bounded above by F_max. For action-dependent loss distributions, use q(d_0 E[F|0,flag]-d_1 E[F|1,flag]) >= c. Keep the simpler constant-loss proposition if desired. Also say that enforcement and audit funding are exogenous here and refer to the companion inspection game for credibility.

## Claim-by-claim audit verdicts

| Draft claim | Verdict | Direct reasoning / required scope |
|---|---|---|
| Economics water-filling optimum | **Pass, conditional** | Strict concavity, binding finite capacity and positive A_i,a_i yield unique h; KKT and active-set treatment correct |
| Economics numeric example | **Pass** | eta=.9251678148440968; h=(2.3803652295,1.5418546341,.0777801365); benefit=11.2993287406 |
| Economics residual floor | **Pass, model-specific** | p_i L_i[1-d_i(h)] tends to p_i L_i b_i; not general irreducible scientific error |
| Economics heterogeneous substitution | **Pass, conditional** | Exponential of negative linear dose preserves concavity; productivity is not trust centrality |
| Economics complementarity counterexample | **Pass** | For K=2 at origin each single-coordinate derivative is zero but joint positive allocation has positive benefit |
| Economics coverage impossibility | **Pass** | Required distinct groups k exceeds available m; simple cardinality proof |
| Economics capacity tightening weakly lowers same optimum | **Pass** | Set inclusion, provided objective and all other conditions held fixed; omitted safety costs explicitly acknowledged |
| Economics queue non-overload and M/M/1 | **Pass, conditional** | .7*2*.75=1.05; W values correct; hypotheses/critical deterministic exception included |
| Economics audit inequality | **Pass after R6 wording** | Direct subtraction correct for fixed/expected F; participation separately identified |
| Economics consensus equilibrium | **Pass, minor phrasing** | Changing to nonmatching report loses reward; acquiring information then still reporting pass does not lose reward but wastes positive cost |
| Economics sponsor lottery | **Pass** | Hypergeometric expectation 20*(100/200)=10; no identity fraud required |
| Economics sponsor runway | **Pass, conditional** | B/g assumes initially balanced budget, no replacement surplus and unchanged other flows; no prediction of misconduct |
| Economics fairness and pilot benefits | **Open hypotheses** | No empirical benefits claimed; preserve this boundary in synthesis |
| Law strict rho<1 necessity | **Fail as stated** | R1 deterministic critical-load counterexample |
| Law bounded geometric appeal expectation | **Pass, conditional** | Sum c*p^j; deterministic c(K+1) bound only with per-node c bound and at most one child per level |
| Law branching total expectation | **Pass, conditional** | Linearity of expectation gives sum m^j for stationary offspring mean; not deterministic bound |
| Law unbounded finite-resource impossibility | **Pass** | A*epsilon > H construction; may need epsilon for substantive human review, since automated receipts need not have this lower bound |
| Law priority knapsack | **Pass as definition** | Chosen normative objective, no claim optimal social welfare or guaranteed legal compliance |
| Law workload recursion | **Pass, scoped accounting** | Work-conserving aggregate lane, all staff-minute arrivals represented; does not capture skill-specific constraints or deadlines |
| Law coordinate separation | **Pass as access-control invariant** | Requires actual authorization implementation and derived-view tests; no proof of social independence |
| Law legal applicability/obligations | **Outside this audit's verification scope** | Primary-source legal lane and qualified review remain responsible; do not convert this mathematical review into legal clearance |
| Law capacity script current numbers | **Pass for hardcoded valid inputs** | Input-validation and truncation failures remain R3 |
| Law bounded-process human benefit | **Open hypothesis** | No evidence that users find four verbs sufficient or trust outcomes more |

## Review disposition

The economic mathematical core is suitable for integration after the narrow F wording fix. The legal mathematical core requires R1 correction. R2–R5 are important implementation/evaluation conditions; they should be resolved in the prototype specification or retained as explicit open gaps. Neither draft establishes mechanism-wide incentive compatibility, legal clearance, or field efficacy.
