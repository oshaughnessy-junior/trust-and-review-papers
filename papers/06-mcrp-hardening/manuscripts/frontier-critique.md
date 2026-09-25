# Local influence is not assignment safety

**Formal supplement and red-team review of the existing Paper 02 model · draft**

## Question and answer

**Question.** Which controls must connect root-relative trust capacity to reviewer assignment before a local stationary-mass bound can constrain adversarial operational influence?

**Answer.** A dimensionless leakage bound must hold after all filtering and normalization, simultaneously shared capacity must prevent repeated reuse, and the final case-specific assignment distribution must preserve an explicit bound after eligibility, workload, exploration, and common-control constraints; the existing candidate lemma alone establishes none of those links.

## Existing contribution acknowledged

The canonical `papers/02-formal-dynamics/MODEL.md` already defines plural root-relative trust views, typed positive delegation, frontier capacity, layers and importer-owned bridges, forks, resource modes, exploration, and separate conduct/evidence outcomes. The accompanying TDRG draft already rejects global person scores, agreement-based standing, graph-path independence, and automatic scientific authority. These are inputs to this critique, not inventions of the present paper. The incentive model in `paper.md` adds strategic effort and monitoring assumptions to that architecture.

## 1. The candidate lemma is correct under its stated assumptions

Use \(a\in(0,1)\) for walk continuation, to avoid confusion with the audit false-positive parameter in the game paper. Let \(p=(1-a)s+aT^Tp\), \(s(X)=0\), and \(T\) be stochastic after all dangling-node and filtering rules. Suppose every row in honest region \(H\) sends at most \(e\) probability into adverse region \(X\). This is equivalent to bounding that leakage for every probability distribution supported on \(H\). Then

\[
p(X)=a\sum_{i\in H}p_iT_{iX}+a\sum_{i\in X}p_iT_{iX}
\le a[e(1-p(X))+p(X)],
\]

hence

\[
p(X)\le\frac{ae}{1-a+ae}.\tag{F1}
\]

The inequality is tight: a two-state chain with \(T_{HX}=e\) and \(T_{XX}=1\) attains equality. This is a proved statement for the specified stochastic operator, not evidence that a max-flow gate establishes its assumptions. `H` need not be morally honest; it denotes the modeled trusted side of the partition. Corruption inside it remains outside this boundary guarantee.

A measurable stationary-flux bound \(\sum_{H}p_iT_{iX}\le b\) would instead yield \(p(X)\le ab/(1-a)\), capped at one. That is a different assumption, and depends on \(p\). Do not substitute a raw edge-capacity budget for either probability quantity without a construction that connects their units.

## 2. Raw capacity disappears on normalization

Take root \(h\), adverse node \(x\), one positive edge \(h\to x\) with raw capacity \(u=10^{-6}\), and an adverse self-loop. If this edge survives admission and ordinary row normalization is used, \(T_{hx}=1\), regardless of \(u\). With restart at \(h\), \(p_x=a\). At \(a=.85\), this is .85. Mistakenly treating the raw capacity as \(e\) predicts about \(5.67\times10^{-6}\), a false guarantee by more than five orders of magnitude.

A capacity threshold might exclude this particular node. It does not solve the conceptual problem: choose any permitted capacity above that threshold; a sole outbound edge still normalizes to one. The gate must constrain retained **probability mass**, not merely an uncalibrated edge number.

One possible repair is to give every row a declared normalized budget, cap its cross-frontier transition probability at \(e_i\), and return unused probability to the source/root or a specified safe sink instead of renormalizing the surviving outgoing edges to one. A different viable repair could use substochastic transitions with explicit restart of residual mass. Both require an exact definition of frontier membership, not an oracle labeling adversaries. In deployment the frontier is a governance/control boundary, and malicious actors already inside it can evade the bound.

## 3. Per-target flow can multiply a shared budget

Let root \(h\) connect to broker \(b\) with capacity one. Let \(b\) connect to \(m\) candidates, each through a capacity-one edge. The independent max flow from \(h\) to each candidate is one. Therefore a test “candidate is eligible if its individual max flow is at least one” admits all \(m\) candidates.

But a simultaneous flow to a super-sink, with each candidate connected to it by a unit-capacity edge, has total flow at most one. The same frontier unit was reused in the independent tests. A per-target reachability/eligibility predicate and a jointly consumable influence budget are different objects.

This counterexample does not show that all max-flow trust schemes fail. It identifies a currently unspecified choice in the MCRP candidate profile. The implementation must declare whether capacity is a reusable qualification witness, a simultaneously allocated routing budget, a temporal assignment budget, or something else. Only the appropriate shared-budget construction supports a total-influence statement. Scarce capacity can also exclude legitimate specialists behind one trusted broker; report that tradeoff rather than hiding it in “ineligible.”

## 4. A valid routing bound can vanish in assignment

The existing assignment model contains

\[
P(i\mid q)\propto e_{iq}\exp[\beta v_{iq}-\lambda w_i-\operatorname{cost}(\rho_{iq})].
\]

Suppose one trusted actor has routing mass \(.99\), while \(m=1000\) adverse eligible actors share total mass \(.01\) evenly. Let \(v_i=p_i\), \(\beta=1\), equal workload and resource costs. The adverse assignment share is

\[
A_X=\frac{1000\exp(.01/1000)}{\exp(.99)+1000\exp(.01/1000)}\approx.9973.
\]

The stationary mass is only .01. Softmax gives each new candidate a baseline weight near one. A total stationary-influence bound is not a total softmax-influence bound. If these are Sybils, reliable principal grouping could eliminate this particular amplification. If they are unique humans in a coalition, personhood uniqueness does not.

Uniform exploration over eligible accounts has the same population-share vulnerability. An exploration floor is an inclusion mechanism, not automatically an attack-resistance mechanism. Group-aware budgets can protect the frontier at the cost of identifying clusters and making governance judgments.

Even assignment proportional to \(p_i\) loses the original bound after case conditioning. If all trusted actors are unavailable or lack the required capability, and only adverse actors remain eligible, their conditional assignment probability is one. Workload and cost penalties can similarly alter relative weights. The safe response can be “coverage unavailable,” escalation to a different declared profile, or a lower-assurance review; it must not silently reuse the unconditional bound.

## 5. An implementable post-selection invariant

If a relying domain can designate relevant external/control cluster \(X\), it can enforce the actual invariant

\[
\sum_{i\in X}P(i\mid q,\tau)\le\kappa_q
\]

**after** every eligibility, resource, workload, exploration, and diversity transformation. This is a policy choice, not proof that the designated cluster contains all adversaries. If the constraints are infeasible, emit an uncovered-capability outcome; do not renormalize until they disappear. Include single-controller caps, aggregate bridge caps, and shared-budget accounting in the same final assignment solve.

For a panel, specify whether the bound concerns expected seats, at least one adverse seat, all-adverse composition, or a veto/deciding role. A bound on one marginal is not interchangeable with a bound on a joint panel event. Correlation between assignments can make panel risk much larger than an independent-draw calculation.

A useful receipt contains the frozen candidate set commitment, control-group evidence/unknowns, constraints, solver version, infeasibility reason if any, random seed commitment/reveal appropriate to the attack model, and the final relevant marginal/joint risk bounds under stated assumptions. Do not expose private candidate identities through an otherwise public receipt.

## 6. Human interface implication

The three verbs offer/review/repair in the companion paper compress the user experience, not the security state. A user can see “independent coverage unavailable: two candidates share the same operator” without mastering PageRank, max flow, or threshold identity opening. Complexity can remain in auditable institutional machinery while the participant's commitment stays simple.

The existing TDRG's one-enrollment-per-human profile and the proposed arbitrary-complexity principal interface require an explicit adapter. A team's agent count cannot replace its human enrollment or mint reviewer seats. Authorized natural persons can bind a collaboration's scoped mandate, with common control recorded privately as necessary. An organization profile should be separately specified if supported; do not silently reinterpret human uniqueness as organization uniqueness.

## 7. Required experiments

1. **Normalization fixture:** sole tiny outbound edge must not inherit a tiny leakage guarantee after normalization.
2. **Shared-flow fixture:** compare independent per-target flow and one simultaneous multi-target flow; certify only the latter's declared aggregate budget.
3. **Softmax fixture:** hold total adverse stationary mass fixed while varying adverse candidate count; report final assignment share.
4. **Eligibility fixture:** remove trusted candidates by capability, conflict, availability, and resource constraints; invariant either remains true or produces infeasibility.
5. **Bridge-cycle fixture:** multiple individually bounded bridges must satisfy an aggregate final bound after loops and dangling-node rules.
6. **Control fixture:** graph-disjoint accounts under one operator cannot satisfy control diversity.
7. **Legitimate broker fixture:** repeat attacks with all candidates legitimate rare specialists; measure coverage lost under the same controls.
8. **Manager fixture:** attempt post-solver reassignment, root changes, and suppressed audit receipts; demonstrate detection or clearly state trusted-manager assumptions.

These fixtures test statements about algorithms. They do not establish that real-world control groups are fully observable, that reviewers are competent, or that humans will adopt the protocol.

## 8. A concrete final joint-allocation profile

A small implementable correction is **choose only from feasible complete panels**, then randomize within that set. It is stronger and clearer than filtering candidates separately and assuming that later normalization preserves a guarantee.

For frozen request q, enumerate (or solve for) panels P in a feasible family F_q. Every panel must independently satisfy: requested expertise coverage; conflicts and resource limits; at most one seat per declared responsible control group where independence is required; and a declared aggregate frontier/import limit. For example, for a k-seat panel and declared imported set X, require

\[
|P\cap X|\le b_q<k \quad\text{for every }P\in F_q.\tag{F2}
\]

An allocation distribution z_P must satisfy

\[
z_P\ge0,\quad\sum_{P\in F_q}z_P=1.
\]

Any preference, workload, exploration or price-independent priority objective may choose these weights. Since every supported panel satisfies (F2), randomization and subsequent normalization **within F_q** cannot produce an all-imported panel. The result is deterministic under the declared membership, not merely an expected-seat bound. If F_q is empty, return “independent coverage unavailable”; do not relax the bound silently. If b_q>0, the guarantee says nothing about one imported reviewer influencing others or an insider already on the trusted side.

For more graded policy, constrain the final distribution directly: sum_{P:bad_q(P)} z_P <= kappa_q, where bad_q is a precisely defined panel event (all seats imported, a decisive role imported, or loss of control diversity). An expected-seat constraint E|P∩X|<=b is a different weaker guarantee. It yields P(all k imported)<=b/k by Markov's inequality, not zero, unless a per-panel bound is enforced.

**Shared capacity interpretation.** If frontier capacities are intended as consumable assignment reliance, define their unit as seats or reliance units per epoch, rather than raw trust-edge weights. Let f_{e,P} denote the declared charge for realizing panel P through route e. Admit a batch of panels only if their **joint realized** charge sum_P n_P f_{e,P} <= u_e for every edge e, and reserve charges atomically before issuing assignments. A single root–broker unit then cannot pay for seven concurrent independent reviewer seats. If capacities instead mean reusable eligibility evidence, say so and make no inference of total assignment influence from them. For a randomized batch, constraints on expected charge alone allow realized overspending; use feasible whole-batch sampling or reservation/rejection that preserves the declared final distribution and logs failures.

The path charges and group labels are normative policy inputs, not observations of virtue. Unknown controlling relationships remain unknown; they cannot be certified independent by this solver. A corrupt root, false group label, captured decision maker, insufficient capacity, or forged event can defeat the institutional assumptions. Enforcing the cap can exclude an entirely legitimate imported specialty. Publish coverage loss and allow prospective policy revision with a new version; do not claim the unchanged contract was satisfied.


## 9. Adversarial refinements: representation and completion

A feasible support is not a representation-invariant sampling measure. With control groups A,B,C and two seats, uniform group-panel sampling gives A probability 2/3. If A exposes 100 redundant same-control labels and one instead samples uniformly over label panels, A receives a seat with probability 200/201, despite enforcing one seat per group. Sample canonical accountable-group panels first, then choose qualified representatives; alternatively prove invariance of the pushed-forward distribution under semantically redundant labels. Genuine capability changes need not preserve probabilities. Hidden common control remains outside that proof.

Specify whether a probabilistic bound applies to offered, accepted, completed, or relied-upon panels. A risky offer fraction of .1, risky completion 1, and safe completion .01 yields risky completed fraction .1/(.1+.009)=.91743. Refusals, deadlines, requester rerolls and all retries stay attached to the same request. A hard per-panel support restriction survives conditioning within that support; a mere distributional probability bound does not. Stop with coverage unavailable when the promised boundary cannot be preserved. No scheduler can compel qualified volunteers to finish. These are proposed corrections, not implemented production features.
