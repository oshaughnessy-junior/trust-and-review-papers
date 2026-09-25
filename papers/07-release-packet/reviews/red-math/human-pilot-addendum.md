# Review of the proposed human evaluation and integrated synthesis

This is a review of a pre-results design and artificial calculations. No human experiment, consent, recruitment, approval or preregistration is established by it.

## Exact design calculations independently confirmed

`human_pilot_review.py` reconstructs the stipulated potential-outcome tables from the prose, enumerates every allowed labeled treatment allocation, and builds sharp-null reference distributions by direct labeled assignment enumeration. It does not reuse the author's hypergeometric-convolution routine. All **15** power rows match exactly. At a .50 average benefit in the artificial monotone family, the probabilities are 0 for eight boundaries, 421/1296 (about .325) for sixteen, and 5671/7776 (about .729) for twenty-four.

The eight-boundary zero-power result is correct for this two-sided exact test: its smallest complementary extreme pair already has mass 2/36>.05. The nonmonotone small-effect rejection rate at sixteen boundaries is also a valid discreteness phenomenon, not a formula error. The design keeps it rather than smoothing a misleading power curve.

The Fisher test concerns the sharp null of no effect on any unit. Its exactness does not transfer to a weak null of zero average effect with heterogeneous individual effects. The plan clearly says this and does not invent an exact average-effect confidence interval. The primary estimand's equal-boundary weighting also remains explicit; a large collaboration cannot generate extra independent observations through its membership count.

## RM-4: missingness bounds must name their target

The original naming could blur the primary finite-population causal effect with the interval obtained by filling missing outcomes in the observed treatment arms. The latter interval bounds the **realized complete-data arm mean contrast**, conditional on that allocation. It does not bound the finite-population causal average effect or supply randomization uncertainty.

Independent counterexample: in each of two blocks, set both potential-outcome vectors to (0,0,1,1), so every treatment effect is zero. Assign positions 2 and 3 to treatment in both blocks. There are no missing outcomes; the interval routine returns [1,1], whereas the finite-population causal effect is zero. This is ordinary randomization variation, not a bug in endpoint arithmetic. The exact two-sided sharp-null p-value exceeds .05 in that eight-boundary example.

The blue mathematician accepted the distinction and repaired the API docstring, README, JSON field/target warning and a regression test. The domain/legal reviewer independently raised the same concern and clarified the evaluation-plan prose. After those repairs, all eight design tests pass. The adversarial script independently enumerates all missing-outcome completions in the worked example and confirms the arithmetic endpoints -1/4 and 1/2. It retains the causal-target counterexample so the distinction cannot quietly disappear.

## Design and identification boundaries

The strong baseline receives the same evidence, versions, amendment notice and scope information. That avoids attributing an information advantage to the four-action wording. Parallel first use addresses irreversibility of learning the vocabulary; optional later crossover is not pooled into the primary effect. Blocking before allocation, concealed allocation, independent case-order scheduling and predeclared boundaries are appropriate design intentions. Published toy seeds are explicitly not concealment.

Shared team members, coaching and facilitators can create interference. The domain reviewer added a useful caveat about facilitator fatigue/support competition and the need to freeze the service regime or redefine the relevant cluster/assignment estimand. The design code does not model these effects or estimate their prevalence; actual recruitment and randomization must reflect them. Statistical correction after observation cannot create independent units that never existed.

Adequate refusal and unknown states are not automatically failures, but an interface that always refuses or labels everything unknown should not pass. The added unaffected-use control helps expose that trivial strategy. That control remains part of design planning; the exact power table is an illustrative fixed potential-outcome family and is not refitted evidence about this rubric.

Restricted-horizon person-minutes are a useful separate decision quantity. The plan keeps missing labor unmeasured rather than zero, distinguishes elapsed time from team labor, counts facilitation and unfinished work, and makes follow-up outside the horizon descriptive. It does not define a welfare optimum or provide confirmatory power for a joint adequacy/labor decision. Stakeholder-chosen margins and an analysis appropriate to the actual design remain necessary before a real confirmatory study.

## Integrated synthesis correction

The initial synthesis phrase “individually non-amplifying repair maps” was too strong for the switching example. Each nilpotent map can amplify some input in one step; it only clears work when repeatedly applied alone. A common-norm non-amplifying family could not exhibit that claimed product growth. The integrator was asked to use the precise “clear work when repeatedly applied alone” formulation. This is a wording correction to the synthesis, not a defect in the matrix example or conditional repair theorem.

The synthesis's noncomposition table is otherwise an appropriate summary. It keeps stipulated identity, actual audit delivery, authority, scientific adequacy and runtime conformance distinct. The prospective human design adds a serious test of the small interface without presenting a teaching clinic as efficacy evidence.

**Continued qualified assent:** the additional pre-results design strengthens the research seed once the missingness target and switching wording are explicit. It authorizes no human study and establishes no efficacy. The packet remains suitable for public critique as a transparent proposal with runnable failures and a strong simplicity baseline.
