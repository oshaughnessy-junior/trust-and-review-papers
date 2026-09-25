# Small rules, unequal resources: an attention ecology for protocol design

**Research question.** Can a small recognition-and-correction loop support useful
work without turning initial visibility into entrenched access to scarce review?

**Bounded answer.** Capping credit and preserving exploratory access yield simple
mathematical bounds on *offered group attention*. They do not guarantee completed
coverage, accurate checks, repair capacity or equitable outcomes. A small synthetic
ecology exhibits those gaps and compares the mechanism against plain uniform
routing rather than assuming reputation machinery is necessary.

## Contribution and claim ledger

| Label | Statement | Evidence |
|---|---|---|
| D | A four-rule ecology connects offers, scarce checking, recognition and persistent repair debt | `models/ecology/ecology.py` |
| T | Capped decayed credit remains in [0,1]; softmax allocation then has a conditional ceiling | Elementary derivation below |
| T | A specified symmetric mean-field map has a local feedback threshold | Jacobian below; separate approximation, not a theorem about the simulator |
| I | Shared integer effort is conserved, exogenous offers are paired across policies and missing capacity blocks work | Ten ecology test methods plus eight correction-game methods, including independent trajectory labor sums and a closed-form payoff oracle |
| I | Exploration/credit changes need not improve group coverage or repair backlog | All 216 exploratory runs retained, including uniform baseline |
| H | Recognition and dominance incentives could promote useful checking or entrenchment in humans | No behavioral data or causal identification here |

The prior mathematical ingredients are ordinary softmax mixtures, convex updates,
finite resource accounting and queue dynamics. This manuscript applies and connects
them; it does not claim to invent these methods. The earlier dossier's local-feedback
model motivates the diagnostic. This study is standalone synthetic evidence, not a
fitted or externally validated social model. AI agents drafted and internally
critiqued it under the same orchestration; external and human review remain separate.

## Four rules, three comparison policies

Six accountable groups differ in capacity, skill coverage, submission volume and
stipulated review diligence. A large collaboration has more internal capacity and
offers but remains one group. Offers contain a required skill and a synthetic
latent defect. Reviewers are different qualified groups. Checks and independent
audits consume scarce effort; flagged or audit-discovered defects create persistent
correction work. Oldest corrections get first access to the same experts next period.

The routing alternatives are: cumulative attention reinforced by pending volume
(**prestige**); decayed capped check/correction credit with exploration (**bounded**);
and a **uniform active-group** lottery. Each uses the same reviewer selection and
cost model. Uniform routing is the serious simplicity baseline. Prestige intentionally
models both feedback and volume multiplication; the experiment cannot identify
which of those two components alone caused a difference.

The word “trust” here names a proposed interpretation of recognition, not a computed
probability that a claim is true. “Dominance” names the hypothesized advantage of
visibility feeding future access, not a demonstrated account of human motivation.
Agents do not optimize effort or voluntarily join; their stipulated diligence
creates tasks accomplished or missed. The separate coupled study addresses limited
honest/shallow/refuse responses. Neither model supplies a general cooperation theorem.

## A conditional bound, not a promised outcome

For an active group set of integer size $K\ge1$, finite score $s_i$,
$0\le\epsilon\le1$ and finite feedback strength $\beta\ge0$, bounded routing uses

$$P_i(s)=\frac{\epsilon}{K}+(1-\epsilon)
\frac{e^{\beta s_i}}{\sum_j e^{\beta s_j}}.$$

At period end, qualifying credit $r_i\ge0$ produces

$$s_i(t+1)=(1-\mu)s_i(t)+\mu\min(1,r_i(t)),\quad 0\le\mu\le1.$$

Starting in $[0,1]$, scores remain in $[0,1]$ because the update is a convex
combination of two points in that interval. Therefore, while the active set and
its declared identity partition are fixed,

$$\frac{\epsilon}{K}\le P_i\le
\frac{\epsilon}{K}+(1-\epsilon)\frac{e^\beta}{e^\beta+K-1}.$$

The upper bound follows by putting the selected score at one and all others at
zero. Strong reinforcement can make it close to one despite bounded credit. A
positive proposal floor is not a completion floor: selected work can lack an
independent specialist, sufficient indivisible capacity or a feasible audit. An
actor hidden behind multiple asserted groups also violates the fixed-group premise.
The prestige comparator multiplies weights by queued volume after its mixture,
so it does not inherit the uniform exploration floor.

## A local self-organization diagnostic

For $K\ge2$, to isolate feedback, consider the *separate* deterministic approximation in which
expected credit is exactly group attention, so $s'=(1-\mu)s+\mu P(s)$. It has a
symmetric fixed point $s_i=1/K$. On the zero-sum perturbation subspace the softmax
Jacobian acts as $(1-\epsilon)\beta/K$, giving update multiplier

$$\lambda=1-\mu+\mu(1-\epsilon)\beta/K.$$

For $0<\mu\le1$ and nonnegative $\beta$, local asymptotic stability holds when
$(1-\epsilon)\beta<K$. Equality is inconclusive by this linearization; above it,
small asymmetries grow locally. The common-score direction has multiplier $1-\mu$.
This is a local result for the stated map. The actual simulator has heterogeneous
queues, capacity filters, capped event credit, audit access and repair obligations;
it is not this symmetric system and no threshold transfer is asserted. The
calculation explains why feedback deserves testing even with a small rule set.

## Shared labor and persistent debt

A period gives each actor capacity $C_i$. The costs are two effort tokens per
invitation/intake, ten per completed check, five per independent audit and twenty
per correction (scaled in a stress regime). All draw from the same balance. Thus
for every actor-period, the implementation preserves

$$L_i^{\mathrm{intake}}+L_i^{\mathrm{check}}+L_i^{\mathrm{audit}}+L_i^{\mathrm{repair}}\le C_i.$$

That accounting bound cannot prevent queues from growing. If recognized correction
arrivals exceed feasible qualified correction completions, known debt accumulates.
A low-resource specialist may check one offer yet be unable to complete an
indivisible repair. Spare effort elsewhere does not solve that skill/size mismatch.
Tasks cannot be fractionally carried across periods in this model. This modeling
choice deliberately exposes indivisibility; it is not a recommended real scheduler.

An even more troubling case is a small correction queue with many hidden defects.
A shared blind period makes all checks support their claims. Without independent
audits, defects create no repair requests. The negative-control test gives every
offer a defect, every period blindness and no audits: some work completes, every
judgment is wrong, and repair debt remains zero. Neither throughput nor a quiet
queue should be a proxy for scientific reliability.

## Exploratory design and honest denominators

Nine regimes perturb arrival load, feedback, exploration, repair cost, common-mode
blindness, audit access bias and absence of audits. Each runs eight seeds for eighty
periods under all three policies: 216 retained runs. Exogenous offers, true defect
states and blind periods match across policies within each seed/regime, verified by
an offer-stream hash. Policies induce different processing orders and hence different
signal draws; this is not pathwise matching of every check outcome.

Outputs include all offers, checks, unresolved work, correctness among completed
checks, correct checks per offered task, defect discovery divided by all offered
defects, author-attention concentration, every group's coverage, known repair debt
and all charged labor. Capacity refusals and invitations count attempts rather than
unique offers; retrying a pending offer next period is visible in those totals.
There is no claim to include author drafting labor, routing compute or institutional
administration. Group concentration must be read beside offered volume: equal
attention shares and equal per-offer service are different objectives.

The summary reports means and minimum/maximum across seeds, with paired differences
from uniform routing. These are descriptive sensitivity results, not significance
tests, inferential confidence intervals, real-world predictions or a preregistration.
The run manifest identifies source/test and CSV hashes. Parameters are illustrative;
none is estimated from scientific communities.

## Selected numerical outcomes (synthetic implementation results)

Means over the eight retained seeds; full seed ranges and all regimes are in
`models/ecology/results/summary.json`. “Correct/offer” includes unresolved offers
in its denominator. HHI measures completed attention concentration, and debt counts
recognized correction tasks remaining after eighty periods.

| Regime | Policy | Correct/offer | Defects found | HHI | Lowest group coverage | Repair debt |
|---|---|---:|---:|---:|---:|---:|
| Default | Prestige | .914 | .887 | .241 | .990 | 17.38 |
| Default | Bounded | .906 | .896 | .241 | .980 | 18.00 |
| Default | Uniform | .900 | .881 | .241 | .983 | 18.88 |
| Overload | Prestige | .693 | .697 | .303 | .552 | 31.00 |
| Overload | Bounded | .682 | .652 | .207 | .613 | 19.75 |
| Overload | Uniform | .687 | .613 | .183 | .486 | 15.50 |
| Expensive repair | Prestige | .903 | .888 | .242 | .968 | 37.62 |
| Expensive repair | Bounded | .896 | .891 | .242 | .968 | 38.00 |
| Expensive repair | Uniform | .899 | .880 | .240 | .981 | 38.38 |
| Common blindness | Prestige | .863 | .492 | .241 | .992 | 8.00 |
| Common blindness | Bounded | .856 | .478 | .241 | .989 | 7.88 |
| Common blindness | Uniform | .861 | .483 | .241 | .989 | 7.12 |

Under overload, uniform routing has the lowest concentration but also the lowest
minimum per-group coverage; bounded routing improves that coverage metric while
slightly reducing correct checks per offer relative to uniform. Total charged
labor is similar: 10,404 tokens for bounded versus 10,373 for uniform out of 10,800
available. This is a tradeoff, not domination by the proposed mechanism.

Known debt persists even under default load because the large team's rare-skill
repairs require a different qualified actor; its small rare-skill peers each have
fifteen tokens, below an indivisible twenty-token repair. Uniform or prestige
routing cannot create the missing independent repair capacity. Doubling repair
cost raises debt for every policy. Under common blindness, the lower debt is
misleading: fewer than half of all offered defects are found, even while correct
checks per offer remain above .85 because most offers are nondefective.

## The missing incentive bridge: manufacturing work to earn correction credit

The adversarial replication exposed a structural gap: in a no-audit fixture, an
all-clean population finishes with total recognition about .042, while an
all-defective population finishes around 1.344 after 22 completed repairs. This is
an implementation counterexample about the reward rule. The agents in the ecology
cannot choose their defect rates, so those numbers do not establish strategic
behavior or an equilibrium. They motivate an explicit deviation model instead of
a verbal claim that correction rewards induce cooperation.

`models/ecology/correction_game.py` compares **clean work** with **deliberately
manufacturing one correctable defect and obtaining a completed repair**. It uses
the actual bounded score update and allocation function from the ecology. Let
$q^0$ be the next allocation vector after clean work, $q^1$ after manufactured
and repaired work, and $V$ the utility value of one full unit of future attention.
The two actions concern the same final corrected claim: the manufactured path
adds no assumed scientific value. Let $c$ be manufacture cost, $h$ repair effort,
$\ell$ utility cost per effort token, $\theta_A$ the repair cost share borne by the
author, $d$ the probability that intent to manufacture is established, and $F$ a
credible enforceable loss conditional on that finding. The one-step deviation gain is

$$\Delta U_A=V(q^1_A-q^0_A)-c-\theta_A h\ell-dF.$$

Within this risk-neutral one-step model, manufacturing a successfully repaired
defect is strictly preferred **if and only if** independent repair is feasible
and $\Delta U_A>0$. Equality means indifference. This is a comparison of two
specified actions, not a complete action set, participation model or repeated-game
equilibrium. An infeasible repair blocks this particular path; it does not prove
that other misconduct is unprofitable. Intent detection $d$ is a separate strong
assumption: finding an ordinary error does not establish deliberate manufacture,
and ordinary check accuracy cannot be substituted for $d$.

For an author–repairer coalition $C=\{A,R\}$, the corresponding comparison is

$$\Delta U_C=V\sum_{i\in C}(q^1_i-q^0_i)-c-\theta_C h\ell-dF,$$

where $\theta_C\ge\theta_A$ is their joint internalized share and transfers inside
the coalition cancel. The model assumes a common attention valuation solely to
keep this counterexample small. Distinct declared control groups can still
coordinate; declaration-level independence is not coalition-proofness.

Three allocation-credit choices are retained: credit author **and** repairer;
credit only the independent repairer; and no allocation credit for correction.
Default parameters are three equal zero-score groups, $\epsilon=.15$, $\beta=4$,
$\mu=.4$, $V=100$, $c=1$, $h=20$, $\ell=1$, $\theta_A=\theta_C=.1$, and no
intent detection. Independent repair capacity is twenty tokens. Clean work has
zero verified credit in this no-audit fixture. This last premise is explicit and
important: an exogenous clean-author-credit sensitivity is also supplied under
the result key `verified_clean_baseline`. It does not replay a complete ecology
audit, which can also credit the checker and consumes additional audit labor.

| Correction-credit choice | Author deviation gain | Coalition deviation gain | Added social-cost proxy |
|---|---:|---:|---:|
| Author and repairer | +7.27 | +17.54 | 26 |
| Repairer only | −19.11 | +13.11 | 26 |
| No correction allocation credit | −3.00 | −3.00 | 26 |

These values use the exact softmax, not a linearized benefit. Repairer-only credit
removes this author's unilateral gain but leaves a profitable coordinated path.
The no-credit baseline removes this channel under the stated utility function;
it is **not** asserted optimal, since willingness to perform genuine repairs,
intrinsic motives and useful recognition are absent from this one-step comparison.
Full exploration removes this attention reward channel. Full cost internalization,
credible intent detection, verified clean-work credit and insufficient independent
repair capacity are separate retained sensitivity cases.

The descriptive social-cost proxy is $c+h\ell+H$, with $H=5$ for temporary harm;
attention transfer is excluded as a social benefit because the opportunity pool
is fixed. This is an assumed common utility scale, not measured scientific welfare.
A twenty-token repair also consumes the entire modeled available repair capacity,
leaving none for another case. Costs borne by a shared sponsor or volunteer pool
still exist even if a strategic coalition does not internalize them. The default
coalition includes the credited repairer yet bears only ten percent of the cost;
this assumes substantial externalization or compensation. If the repairer bears
the full private effort cost without an offset, the coalition share must reflect
that, as in the full-internalization sensitivity.

The scalar capacity comparison is for one case. It does not reserve capacity
across repeated calls or provide a multi-case schedule; the separate coupled
simulator supplies the stateful shared-ledger experiment.

The design consequence is not to punish ordinary corrections or treat disclosed
mistakes as misconduct. An honest author who repairs a claim has made information
more useful and should retain a safe correction path. Distinguish recognizing
responsible conduct from automatically increasing scarce review priority whenever
repair volume rises. Whether to credit independent repair, baseline clean work,
or neither in allocation requires testing with genuine repair participation and
collusion incentives; no choice here has earned an institutional recommendation.

## Interpretation and failure of mitigation

The retained runs should decide how much additional mechanism is worth exploring.
Do not select only the regime in which bounded credit looks best. Uniform routing
can match or exceed it, high exploration can change little when skill constraints
bind, and expensive repair can defeat every allocation policy. Audit access bias
can turn “verified credit” into a proxy for privileged access. Even idealized audits
cannot help when independent expertise or capacity is absent.

A human-facing protocol can retain four simple actions while machines expose these
resource and uncertainty states. But complexity inside the institution has not been
abolished: someone must establish accountable control, decide check scope, supply
independent auditing and carry correction duties. The model helps locate those
burdens; it does not prove that people will accept them.

Before a pilot, compare a plain structured-template interface and uniform routing
against the additional credit mechanism under matched total labor. A finding of
no material advantage is a reason to omit the mechanism. Keep portable receipts,
explicit unknowns and inspectable correction paths even if recognition feedback
fails its test.
