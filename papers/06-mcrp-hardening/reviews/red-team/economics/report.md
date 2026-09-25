# Adversarial review: economics and allocation

25 September 2026. Same-model/operator adversarial agent review, not independent institutional review, empirical validation, legal advice, or release approval. Read economics manuscript, SCIENCE_PACKET, SOURCE_NOTES; game-theory cross-review and economic sensitivity code/results; relevant cross-expert models and interface recommendations. The reviewed economics manuscript changed during review: final observed SHA256 `738b62f3389a4f0572806dae377b94ffb599b3ec9fbfd1526c6bdc8908309f9a`; numerical source SHA256 `655dc1d9ed554ca2e9fd27c23687466bbb43e8b1f41a40023b307fe8f0b2aa18`. No author files were edited.

**Verdict:** The conditional mathematical paper is credible as an analytical design note; the optimizer is not reliable across its claimed mathematical domain. The work does not yet justify deploying optimized attention allocation or describing the mechanism as fair, incentive compatible, self-organizing, or economically sustainable. Most manuscript limitations are unusually explicit. Their explicitness is a strength, but does not substitute for resolving them in an operational recommendation.

Severity meanings: high blocks an operational or general algorithm claim; medium requires correction or retained release condition; low is precision. `checks.py` and `results.json` reproduce the adversarial numerical cases without modifying the author's outputs. Run `python3 work/red-team/economics/checks.py` from the workspace. The checks distinguish ordinary valid fixtures from deliberately invalid inputs.

## ECON-01 — High: valid water-filling instance fails the numerical implementation

**Exact target:** `work/games/economics_checks/run.py:19–28`, `water_fill`; economics §3.2 domain of positive A,a,H.

**Reproduction:** `water_fill([1],[1],100)` raises `AssertionError`. This is an especially simple valid problem: the unique optimizer is h=100. The shadow price is exp(-100). After 100 bisections on the linear interval [0,1], eta cannot be resolved below approximately 2^-100, giving only about 69.3 hours. `water_fill([1e-200],[1e-200],1)` additionally underflows the product A*a and divides by zero despite strictly positive finite inputs.

**Consequence:** The theorem is correct but the implementation is not a solver for its stated domain. Disabling assertions can turn the first failure into silent under-allocation. Existing synthetic sweep results are not thereby invalidated: their scale is narrower and their assertions passed.

**Minimal repair:** Solve for log(eta), compute log(A)+log(a), bracket adaptively in log space, and terminate with an explicit resource-residual tolerance and checked status. Alternatively implement an active-set solution. Validate scale-supported behavior with the one-lot 100-hour case and multiplication-underflow case. State supported numerical ranges if extreme parameters are deliberately rejected.

**Residual risk:** Absolute tolerances and floating-point saturation still need declared units/scales. No numerical repair estimates the latent parameters.

**Claim verdict:** EC02 proof passes; general numerical implementation claim fails. Current fixed-sweep arithmetic remains conditionally usable.

## ECON-02 — Medium: promised negative control and malformed-vector handling fail

**Exact target:** `run.py:15–33`; SCIENCE_PACKET “all-zero detection-productivity negative control.”

**Reproduction:** `water_fill([1,1],[0,0],1)` raises `ZeroDivisionError`; mixed zero productivity `[0,1]` and zero value `[0,1]` raise domain errors. `water_fill([1,100],[1],1)` silently returns a one-element allocation, dropping a task through `zip`. Negative lower bounds are accepted. The zero cases are outside the strict-positive theorem but inside the explicit experimental negative-control request; malformed lengths are programming errors that should be rejected.

**Consequence:** The experiment suite does not demonstrate its own all-zero negative control and the helper can silently alter the task population. This is not evidence of fabricated benefit: zero-productivity calls currently crash rather than claim benefit.

**Minimal repair:** Validate equal lengths, nonnegative finite inputs, nonnegative finite budget, valid lower bounds and empty-instance policy. Explicitly define treatment of zero-value/productivity tasks. For all-zero benefit, allocation is nonunique and need not expend H; return zero discretionary effort or documented lower-bound service with zero benefit. Reject unsupported inputs clearly rather than relying on assertions.

**Residual risk:** Passing input checks cannot establish scientific meaningfulness of positive parameters.

**Claim verdict:** Strict-positive theorem unaffected; negative-control completion is unverified; helper robustness fails.

## ECON-03 — High operational condition: a precisely optimized priority can be nearly the opposite of useful review

**Exact target:** economics §§1.1, 3.1, 3.5, E1; `economics_checks` sensitivity interpretation.

**Reproduction:** Two lots have true A=(1,100), a=(1,1), H=1. Reverse the estimated A to (100,1). Estimated water filling spends all effort on lot 1: true benefit .6321, versus 39.7404 for equal allocation and 63.2121 for the latent oracle. Increasing the second true A while maintaining reversed estimates can make the efficiency ratio arbitrarily poor. No exotic distributions or negative inputs are necessary.

**Consequence:** The most compelling equation is an oracle diagnostic, not yet an implementable rule for a scientific commons. Error probability, consequential loss, detectability, and response efficacy are not observable from trust centrality. Endogenous strategic claims of importance can exploit the same failure. Random Gaussian misspecification does not cover targeted manipulation. The manuscript already acknowledges latent parameters; the unresolved issue is what actual allocator is recommended before calibration exists.

**Minimal repair:** In the synthesis explicitly make the first pilot use declared qualitative strata and a bounded lottery/rotation, with water filling only as sensitivity analysis. If optimized allocation is proposed later, preregister estimation, evaluator separation, uncertainty sets and deliberately adversarial priority inflation. Compare against simple policies using held-out issue discovery and full human cost. Do not make a performance promise before those measurements.

**Residual risk:** Even robust optimization protects only against errors inside its chosen uncertainty set; scientific loss is normative and novel domains lack calibration data.

**Claim verdict:** Conditional optimum passes. Deployable efficiency, robustness, and broad fairness claims remain unsupported, as the paper mostly already says.

## ECON-04 — Medium: allocated hours are not completed coverage or low-resource access

**Exact target:** economics §3.5 and H3; `economics_checks/README.md` coverage threshold and reserve comparison.

**Reproduction:** At H=20, the 20% reserve distributes four hours over 20 underserved lots, so each guaranteed floor is .2 hour. The coverage diagnostic requires .25 hour. A lot receiving only its floor gets service but zero measured coverage. More importantly, a .25-hour allocation need not cover a claim requiring a full indivisible 2-hour check. Twenty minutes of onboarding can consume a nominal protected share without producing any check.

**Consequence:** “Reserve improves coverage” can flip with the reporting threshold, and effective access can remain zero despite protected time. This limitation is disclosed in the numerical README but must survive a persuasive summary. An accountable bundle denominator also requires governance over mergers, subdivisions and mixed-resource teams; there is no demonstrated neutral classifier for that denominator.

**Minimal repair:** Preserve exact hours and distinguish attempted service, completed declared checks, covered claim boundaries, and waiting time. Add setup costs and feasible minimum lots to one diagnostic; predeclare resource strata independently of payment and include bundle disputes in measured administrative cost. Acknowledge that a time-share policy and a guaranteed completed-check policy are different interventions.

**Residual risk:** Bundles can be gamed or unintentionally favor incumbents even with private accountability. Equal access does not imply equal scientific usefulness.

**Claim verdict:** Time allocation is measured; fairness and completed scientific coverage remain hypotheses.

## ECON-05 — Medium: additional campaign revenue does not identify additional specialist capacity

**Exact target:** economics §7.2 and H4; scientist §4 specialist-load example; law protected-capacity model.

**Reproduction:** A field has four independent specialist hours/week, all required by the common pool. A fully cash-funded campaign buys four hours from the same pool. Joint demand is eight hours and the shortfall remains four even if the sponsor pays a declared overhead contribution. Generic volunteer hours elsewhere cannot substitute. Before/during campaign comparison alone cannot distinguish displacement from contemporaneous changes in availability or common demand.

**Consequence:** Full accounting cost is not a feasibility certificate. Stated independence of payment and scientific authority is also compatible with sponsor influence over topic discovery, documentation quality and scarce eligibility. This is already correctly identified conceptually; H4 is too weak for a causal additionality claim.

**Minimal repair:** Report counterfactual capacity by indispensable capability/control group, observed common-pool service and queue age, and maintenance obligations. Label before/during results descriptive. For a causal claim, stagger campaigns or use a justified comparison with measured demand/capacity changes. Campaign admission must fail when additive capacity cannot be supplied under the declared contract; financial solvency alone is insufficient.

**Residual risk:** Reviewer substitution, multi-institution control and opportunity cost are partly private and difficult to measure. No lightweight sponsor metric establishes independence.

**Claim verdict:** Sponsor-lottery counterexample passes. Additionality and sustainability unproved; do not soften this into “funded campaigns solve scarcity.”

## ECON-06 — Medium, corrected during review: penalty ceiling is not expected imposed loss

**Exact target:** initial economics §6.1 “loses at most F,” followed by exact utility. Latest observed §6.1 now defines fixed F or equal conditional expected loss bounded by F_max and makes audit commitment exogenous.

**Reproduction of original issue:** q=.5, d0=.8, d1=.1, c=2, ceiling Fmax=10 gives a claimed incentive margin +1.5. If actual loss is .1, the margin is -1.965; with w=10, honest utility is 7.995 and shirking utility 9.96. A penalty ceiling alone cannot provide a sufficient deterrence conclusion.

**Minimal repair and status:** The latest author's wording makes precisely the required repair. Participation remains a separate condition and false-positive sanctions remain explicitly costly. The game paper correctly asks who pays and motivates the auditor.

**Residual risk:** Real action-dependent appeal/penalty distributions require q[d0 E(F|0,flag)-d1 E(F|1,flag)] rather than a common F. Endogenous audit avoidance and enforcement costs remain outside the simple model.

**Claim verdict:** EC09 passes after observed revision; do not reopen as an outstanding manuscript error.

## ECON-07 — Low: reserve contribution is a flow; reserve balance is a stock

**Exact target:** economics §7.1 “and reserves R. Required revenue is C=...+R,” compared with §7.3 reserve balance B.

**Reproduction:** A service maintains a $1,000 reserve balance unchanged over twelve months. Adding that balance to every month's required revenue charges $12,000 of reserve accumulation although desired accumulation was zero. This is an interpretive accounting counterexample, not a claim the author used those values.

**Minimal repair:** Define R as the period's planned net reserve contribution, and B as opening liquid reserve stock. State cash budget and donated-resource accounting separately. Allow negative net reserve contributions only as explicit planned drawdowns.

**Residual risk:** Accounting values for donated expertise need not equal replacement cost or recruiting feasibility.

**Claim verdict:** Budget identity valid after units/flow clarification; no measured business case exists.

## Cross-expert coherence and positive checks

- The initial economics vocabulary differed from scientist/law. Latest observed economics now adopts **offer → check → rely → amend** and treats request/commit/report/repair as substeps. This resolves a real usability contradiction; the four verbs remain an interface hypothesis, not a proof of simple governance.
- Economics scalar-hour allocation is an explicitly restricted model. Scientist's dedicated-specialty example and law's protected-rights capacity mean aggregate rho<1 cannot be promoted to an operational sufficiency claim. The present manuscripts now preserve that distinction.
- Economics recommends paid bounded work and audits; games shows an audit promise is not self-enforcing. No contradiction if synthesis keeps audit financing/credibility as an additional assumption, rather than multiplying the two conditional results into a universal incentive theorem.
- Economics public recognition attaches to scoped objects/selective credentials, consistent with scientist and law's fresh-persona limitation. Public durable league tables would contradict all three and should not appear as an implementation shortcut.
- Water-filling KKT proof, dimensional log ratio, worked example (11.2993287406 loss units), model-specific residual floor, complementarity counterexample, cardinality coverage impossibility, sponsor-lottery expectation and conditional B/g runway all pass this review.
- No new general mathematical theorem or empirical benefit is demonstrated. The persuasive contribution is making incompatible objectives and finite operational capacity explicit around a portable review boundary. Preserve that as the paper's strongest defensible claim.

## Synthesis release recommendation

Keep the papers as private analytical working drafts. Repair ECON-01/02 before calling the numerical helper reusable; qualify or close ECON-03/04/05 at the prototype recommendation boundary; apply the small ECON-07 wording fix. Retain the observed resolution of ECON-06. The collected adversaries should next examine whether the assembled main report accidentally upgrades these conditional results into a deployable solution.
