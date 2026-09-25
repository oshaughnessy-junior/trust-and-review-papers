# Cooperation without a truth oracle: games for version-bound scientific review

**Research draft · 25 September 2026 · proposed extension, not an adopted MCRP rule**

## Abstract

A scientific review network must make careful work worth doing without equating agreement, wealth, or institutional size with truth. MCRP supplies a useful unit of accountability: a decision about a fixed claim, contract, evidence set, and release. We model interactions around that unit rather than treating reputation as a universal score. A minimal protocol consists of a bounded offer, a scoped review, and an evidence-bearing challenge or repair. Principals may contain one human or arbitrarily complex human–agent teams; internal multiplicity does not create external independence. We derive a conditional effort incentive with imperfect monitoring, characterize its failure under short horizons and identity resets, and extend it to transferable-utility coalitions. A separate inspection game shows why unfunded audit promises are not credible. A common-mode error model quantifies why additional reviewers can add almost no assurance. The resulting proposal is deliberately limited: finance independent attention; reward inspectable contributions and timely repair; protect low-resource entry; preserve scoped disagreement; and measure the conditions under which cooperation actually survives. No universal incentive compatibility or theorem of scientific truth is claimed.

## 1. The design object

The existing public MCRP proposal distinguishes production, verification, and qualified-human scientific disposition. Its attestation context is

\[
x=(c_v,a_v,h(E),h(R),\mathrm{role},\mathrm{decision}),
\]

where the first two components are claim and acceptance-contract versions, and the next two identify the evidence set and release. The publication policy adds a distinct editorial/deployment authorization. Those separations should survive any reputation mechanism. A large number of helpful reviews cannot authorize deployment, turn an unqualified reviewer into a scientific decision maker, or establish that the claim is true.

Commons currently separates payment entitlements from contributor capability and scientific disposition. Its README describes a narrower deployed slice than the portable backend: founder moderation and shared D1 storage remain part of that slice. This paper does not treat a backend security requirement as demonstrated deployment behavior. We propose a game around these existing boundaries, not a replacement product or operational certification.

Three questions organize the model:

1. Why would a principal pay the cost of a careful review rather than generate plausible text?
2. Why would someone audit that review, and why would the audit be believed?
3. How can a newcomer participate without buying status or becoming dependent on a patron?

Cryptographic signatures answer none of these alone. They preserve a statement's attribution and integrity; incentives and institutions determine whether it was worth making honestly.

## 2. A small interaction protocol

The shared human interface is **offer, check, rely, amend**. Each action concerns a specific release and records its limits. Review and repair below are substeps of check and amend, not competing core verbs. Qualified-human reliance/disposition remains a separate visible action; checks do not imply that decision.

**Offer.** An accountable principal posts a bounded claim and evidence bundle, the questions for review, declared exclusions, a resource envelope, and a deadline. A journal submission, preprint, replication package, or collaboration's internal note can be wrapped without replacing its familiar format. Acceptance criteria are frozen before the designated verification run. Changing scope creates a new offer.

**Review.** A reviewer accepts a specific task and records what was checked, what was found, what was not checked, and relevant dependencies/conflicts. A review may support, bound, contextualize, or contradict a claim. An explicitly incomplete review is a valid contribution; pretending to have performed omitted checks is not. Independent assignment is used when independence is required. The author can suggest expertise, but cannot choose all the people whose approval will count.

**Repair.** Anyone can lodge a bounded challenge tied to an inspectable object and proposed discriminating check. The responsible principal can correct, narrow, rebut with evidence, or state that the question remains unresolved. A separate authorized person decides any disposition. Open challenges do not automatically suspend every related artifact. Operational/privacy emergencies follow the separate moderation route and need not wait for scientific adjudication.

These verbs map to richer machine records, but users should not have to learn a constitution-sized state table to perform one task. Expose only the questions relevant to the current action. The small interface is an experimental design constraint; it is not evidence that governance is simple.

### 2.1 The principal boundary

Let principal \(i\) be a human, institution, collaboration, or accountable operator of an agent team. It chooses an arbitrary internal policy \(\pi_i\): private delegation, discussion, computation, and tooling. The external mechanism observes only a scoped commitment, declared relevant dependencies, a signed result, and a reachable repair/responsibility endpoint.

The mechanism should be **representation-invariant**: replacing one principal's internal agent by 10,000 agents must not create 10,000 independent review seats, reset quotas, or multiply public trust weight. Internally diverse work may improve the result; it is still one accountable external contribution unless genuinely distinct responsible principals are established. This is a design property, not an assertion that principal identity can be proven perfectly.

A collaboration needs a mandate identifying who may bind its decision, which claims are covered, and how that mandate expires. A principal is not necessarily a public legal name: pseudonymous participation can coexist with private capability/accountability controls. Identity disclosure, escrow, and enforcement have distinct privacy and legal costs.

## 3. An effort game with imperfect monitoring

Consider one review opportunity per period. A reviewer in good standing can perform careful work \(H\) or deviate \(D\), for example by claiming a required rerun it did not perform. Do not equate \(D\) with an unpopular scientific conclusion or an honest error.

Let:

| Symbol | Meaning |
|---|---|
| \(r\) | Current utility from honest participation, net of effort, before any erroneous sanction |
| \(g\ge0\) | Additional current utility from the specified deviation: saved effort plus any private benefit |
| \(\alpha\) | Probability honest conduct receives an adverse audit outcome |
| \(\beta\) | Probability the specified deviation receives an adverse audit outcome |
| \(F\ge0\) | Immediate utility loss after that outcome; not necessarily a monetary fine |
| \(\delta\in[0,1)\) | Effective discount factor including the chance of another interaction |
| \(V,W\) | Continuation values in good standing and after the modeled restriction |

Assume monitoring is committed and independent of the reviewer's current report beyond the modeled conduct; outcomes are observable to the parties who enforce the restriction; the reviewer cannot cheaply reset identity; and every relevant unilateral deviation has a specified \(g,\beta\). Sanctions concern provable protocol misconduct and have appeal. The permanent two-state restriction below is an analytically transparent upper-bound benchmark, not a recommendation for irreversible bans.

Honest play and a one-period deviation followed by honest play have values

\[
U_H=r-\alpha F+\delta[(1-\alpha)V+\alpha W],
\]
\[
U_D=r+g-\beta F+\delta[(1-\beta)V+\beta W].
\]

Subtracting gives the effort incentive condition

\[
\boxed{g\le(\beta-\alpha)\{F+\delta(V-W)\}.}\tag{1}
\]

This is a one-step deviation condition, not by itself an equilibrium theorem for the entire network. Given bounded discounted utilities, committed transitions, and this condition for every action at every relevant history, the usual one-step-deviation argument verifies optimality of the proposed review policy. It does not establish truthful authors, credible auditors, coalition resistance, or uniqueness.

For an absorbing restricted state with per-period utility \(r_0\),

\[
W=\frac{r_0}{1-\delta},\qquad
V-W=\frac{r-r_0-\alpha F}{1-\delta+\delta\alpha}.\tag{2}
\]

**Derivation.** Substitute the honest policy into \(V\), subtract the recursion \(W=r_0+\delta W\), collect \(V-W\), and divide by \(1-\delta(1-\alpha)\). The denominator is positive. Participation requires a separate comparison with the outside option; it cannot be inferred from (1).

Several implications follow directly. A high nominal penalty is irrelevant if careful and careless work are equally likely to be flagged. A valuable future relationship can encourage effort, but exposes honest participants to the loss caused by noisy monitoring. Raising \(F\) also depresses \(V\) when \(\alpha>0\); never plug an unaffected continuation value into a high-penalty calculation. Appeals that distinguish misconduct from error can improve \(\beta-\alpha\), potentially doing more than harsher sanctions.

### 3.1 Numerical example and counterexample

In synthetic utility units set \(r=1,r_0=0,F=0,\delta=.95,\alpha=.01,\beta=.20\). Then \(V-W=1/.0595\approx16.807\), and the right side of (1) is approximately \(3.034\). A deviation gain \(g=2\) is deterred under these assumptions.

Change only \(\beta\) to .02. The deterrence bound becomes approximately .160; the same deviation is profitable. Or retain \(\beta=.20\) and reduce \(\delta\) to .10: the bound is approximately .021. Calling a system reputation-based does not make either failure disappear. These are illustrations, not fitted estimates or measured behavior.

### 3.2 Finite horizon and repair

With a known final period, the continuation term is zero there. If \(F=0\), \(g>0\), and there is no intrinsic honesty benefit or external professional consequence, careful effort is not optimal in that final period. Under additional conditions making cooperation depend exclusively on future rewards, backward induction can unwind earlier cooperation. Real scientific communities can have continuing external relationships; the protocol must identify them rather than assuming an infinite horizon.

For a fixed \(L\)-period suspension without other changes, a deterministic loss of \(r-r_0\) each restricted period has present value \((r-r_0)(1-\delta^L)/(1-\delta)\) at the start of suspension. Substituting the actual state-specific continuation gap in (1), rather than the absorbing-state expression (2), avoids overstating the deterrence of reversible restrictions. Full models must include rehabilitation, appeals, and remaining eligibility.

Correction credit is compatible with accountability. If an error is found and responsibly repaired, that event can improve evidence about responsiveness without erasing the original review error. A single scalar score cannot cleanly represent both quantities. Track competence, scope, conflicts, and repair separately.

## 4. Auditing is another game

The previous section assumes monitoring. Suppose an auditor incurs cost \(a>0\), receives no private benefit from catching shirking, and cannot be verified. Not auditing is then a strict best response. A public promise of frequent audits cannot sustain (1).

A minimal inspection game makes the missing budget explicit. A reviewer chooses shirk with probability \(x\); an inspector audits with probability \(q\). Shirking gains \(g\), and an audit detects it perfectly and imposes utility loss \(S>g\). Auditing costs \(a\); detecting shirking yields inspector benefit \(B>a\), from contracted compensation or valued prevented harm. Relative reviewer payoffs are \(0\) for honest and \(g-qS\) for shirk. Auditor payoffs are zero for no audit and \(xB-a\) for audit. The interior mixed equilibrium is

\[
q^*=g/S,\qquad x^*=a/B.\tag{3}
\]

Thus some shirking remains in this stylized inspection equilibrium. Raising sanctions reduces the required audit probability, but does not make inspection free. If \(B\le a\), the interior solution fails and auditing need not be sustained. A paid verification task must itself be inspectable; rewarding accusations creates a different false-positive game. Neither the source record nor this paper claims an implemented payment system.

The practical alternative is a modest independently funded audit pool with auditable assignment and completion records, a random component protected from author manipulation, and separate human adjudication. Funding can come from membership, institutions, grants, or bounded service payments, but must not confer scientific authority. No point bounty for each rejected claim is proposed.

Repeated games admit multiple equilibria. Patient actors can preserve mutual assistance, mutual rubber-stamping, or exclusionary clubs. The classic repeated-game literature motivates attention to equilibrium selection; it is not a proof that a scientific review platform selects the good equilibrium. [Fudenberg and Maskin (1986), verified bibliographic record](https://economics.mit.edu/people/faculty/drew-fudenberg/publications).

## 5. Coalitions, Sybils, and identity resets

### 5.1 Coalition condition

Let coalition \(C\) share transferable utility and coordinate authors, reviewers, and possibly an auditor. Let \(G_C\) be its incremental deviation gain. Let \(\Delta p_i(C)\) be the change in principal \(i\)'s probability of an adverse outcome under the joint deviation, and \(L_i=F_i+\delta_i(V_i-W_i)\). If those losses are additive and all continuation effects are included, a necessary condition against that joint deviation is

\[
\boxed{G_C\le\sum_{i\in C}\Delta p_i(C)L_i.}\tag{4}
\]

This is sufficient for that specified coalition comparison under the stated additive transferable-utility assumptions, not for all coalitions or coalition-proof equilibrium. Correlated enforcement does not invalidate linearity of expected additive losses, but nonlinear coalition value or joint continuation states requires a joint-value calculation. Insider control may make every \(\Delta p_i(C)\) nearly zero. Bribes can allocate gains so that individual-looking incentives appear satisfied while the coalition profits.

A prototype must therefore test reviewer assignment, hidden/shared principals, reciprocal review rings, auditor capture, and promotion capture, not merely author/self-review separation. Random selection from a pool with coalition share \(f\) has all-captured probability \(f^k\) only for independent draws with replacement from a stable pool. Without replacement it is a hypergeometric ratio. Endogenous qualification, correlated operators, or adversarial entry defeats that calculation.

### 5.2 Sybil invariance

If an actor can obtain \(m\) equivalent identities at cost \(c_s\) each and each gains expected influence benefit \(b_s\), multiplying identities pays whenever \(b_s>c_s\). A signed account is not proof of an independent person. Douceur's original analysis demonstrates why redundancy is vulnerable to identity multiplication absent additional assumptions or trusted identity arrangements. [Douceur (2002)](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/).

Do not promise a costless, globally open, perfectly Sybil-resistant system. Use bounded influence per established responsible unit where feasible, independent eligibility checks, and representation-invariance tests. Identity checks can exclude vulnerable participants and introduce central power; their privacy and appeal costs are part of the design.

### 5.3 Whitewashing and the newcomer dilemma

If a restricted principal can re-enter at value \(V_{new}\) after utility cost \(k\), its continuation is at least

\[
W_{eff}=\max\{W,V_{new}-k\}.
\]

Use \(V-W_{eff}\) in (1), but recompute \(V\) and \(W_{eff}\) jointly: when honest reviewers can receive false-positive sanctions, the reset option changes their value too. For an exogenous continuation \(C=W_{eff}\) available immediately after the outcome, \(V=[r-\alpha F+\delta\alpha C]/[1-\delta(1-\alpha)]\). With the earlier parameters and \(C=10\), this is 18.40336, giving deterrence 1.51681 rather than 1.22861 from incorrectly reusing the absorbing-state value. For immediate full-privilege reset costing \(k\), the active branch \(W_{eff}=V-k\) instead gives \(V=(r-\alpha F-\delta\alpha k)/(1-\delta)\), subject to reset being optimal. These extensions still omit preemptive resets and simultaneous accounts. If re-entry is free and newcomers immediately receive incumbent privileges, \(V_{new}=V\) and the reputation loss vanishes. Penalizing all new identities instead burdens honest newcomers.

The proposed compromise is graduated **scope**, not public humiliation or purchased status: anyone can submit a bounded evidence contribution; high-consequence authority requires independently checked capability. Reserve a fixed, auditable share of review attention for new principals; let successful narrow checks establish a track record; support nonmonetary qualification and appeals. Keep authors' ability to be read separate from reviewers' ability to bind a scientific disposition. No mechanism can eliminate both identity-reset incentives and entry costs without additional information or institutions.

## 6. Agreement is an unsafe objective

Suppose two reviewers are paid \(b>0\) for matching reports and acquire independent evidence at cost \(c>0\). A common convention to report “passes” without looking yields matching reports at zero effort. A unilateral costly investigation cannot improve on perfect agreement and may reduce it, so the convention is a Nash equilibrium. This elementary counterexample does not say all peer-prediction designs fail. Sophisticated designs make specific assumptions about signal distributions, multiple tasks, and permissible strategies. Those assumptions require testing before they are transferred to heterogeneous scientific claims. [Shnayder et al. (2016)](https://arxiv.org/abs/1603.03151).

Low-cost shared signals can support uninformative equilibria; selective ground-truth checks may offer a simpler alternative in the settings studied by Gao, Wright, and Leyton-Brown. Our proposal takes only the design warning, not their mechanism's guarantees. [Gao et al. (2016)](https://arxiv.org/abs/1606.07042).

Rewarding disagreement instead is also unsafe: it invites contrarian spam. Reward completed, inspectable tasks and calibrated uncertainty where outcomes are meaningfully observable. Record dissent without converting its frequency into authority. The lack of scientific ground truth is not repaired by calling majority opinion ground truth.

## 7. Common-mode error and arbitrary internal complexity

Let a shared failure mode occur with probability \(\rho\) and make all \(k\) reviewers wrong. Otherwise, reviewers independently err with probability \(p\). Under this explicitly stylized mixture,

\[
P(\text{all wrong})=\rho+(1-\rho)p^k.\tag{5}
\]

For \(\rho=.10,p=.10,k=3\), the probability is .1009, not .001. Adding arbitrarily many reviewers leaves a floor of .10. This is not a calibrated estimate of LLM error, and it applies to unanimous error rather than an unspecified majority rule.

If numerical assessment errors have common variance \(\sigma^2\) and pairwise correlation \(\eta\in[0,1]\),

\[
\operatorname{Var}(\bar e)=\frac{\sigma^2}{k}[1+(k-1)\eta],
\qquad k_{eff}=\frac{k}{1+(k-1)\eta}.
\]

This second-moment diagnostic is not a tail-probability guarantee. Both models explain why a large internal team is not automatically equivalent to several independent laboratories. Declare relevant shared operators, models, training/data dependencies, tools, and infrastructure at an appropriate public granularity. Sensitive details can be held under restricted review; unexplained independence must remain unestablished.

Common training does not imply identical conclusions; different brands do not establish independence. Independence is a tested property of failure patterns and accountability boundaries, not a label earned by separate API calls.

## 8. Status, trust, and capture

Trust can economize attention, and status can motivate useful work. These are hypotheses about behavior, not a universal reduction of human refereeing to two drives. Prestige and dominance should not be conflated: voluntary deference for useful expertise and coercive control make different predictions. Formal prestige models offer mechanisms by which useful leadership could support cooperation, with specific assumptions; they do not validate a platform ranking system. [Henrich, Chudek, and Boyd (2015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4633849/).

In MCRP, prestige could attach to a well-scoped check that survives scrutiny, a reusable negative result, or a prompt correction. The design should avoid rewarding absolute volume, rhetorical certainty, personal attacks, or proximity to stewards. Credit for repair must not allow staged error-and-correction cycles to farm rewards. The appropriate object is a contribution ledger with contextual interpretation, not a universal numerical virtue score.

Durable actor histories remain in protected domain-account custody under TDRG. Public credit attaches to review objects and case personas; selectively disclosed credentials need their own privacy profile. A stable public person-keyed ledger would defeat the intended case-persona separation, and prose can still create linkability even without a stable key.

Consider reviewer selection with allocation probability

\[
P_i=(1-\varepsilon)\frac{w_i}{\sum_jw_j}+\varepsilon\frac{1}{N},\quad0<\varepsilon\le1.
\]

Assume \(w_i\ge0\) and \(\sum_jw_j>0\); if all weights vanish, use a declared uniform fallback. This mixture illustrates exploitation of track records and exploration of eligible newcomers. For \(T\) independent stationary opportunities, principal \(i\)'s chance of never being sampled is \((1-P_i)^T\). It does not establish fair outcomes: the eligible pool may already be captured, opportunities differ in value, and entry can be manipulated. Apply exploration within capability-appropriate strata, report wait times, and audit steward decisions. Qualification needs a route independent of current incumbents' personal approval.

Publicly funded or free discovery matters because paying for graph navigation, while formally distinct from trust, can still improve access to influential work and allies. Measure whether entitlements change exposure, review assignment, or promotion outcomes. A clean database separation between plan and capability is necessary but insufficient to establish equal opportunity.

No quantity of cryptography prevents a coalition from defining weak criteria, excluding competent outsiders, and faithfully attesting to its own rules. Portability of records and competing evaluators can lower exit costs; they can also fragment standards and enable forum shopping. Compatibility means preserving a journal's or institution's own authority while making evidence portable, not imposing global consensus.

## 9. Empirical program and rejection criteria

Start with synthetic seeded flaws whose detection and repair can be scored without adjudicating unsettled science. Keep deployment authority disabled for these experiments. Run at least three conditions: unstructured review, the minimal scoped protocol, and the scoped protocol plus independently assigned spot checks. Hold review budgets and task difficulty distributions constant.

Measure defect detection, unsupported acceptance, honest false-positive accusations, person-minutes per resolved issue, time to repair, unresolved backlog, newcomer assignment delay, and concentration by responsible principal. Record budget consumed by reviews and audits separately. A smaller backlog achieved by silently discarding difficult claims is not a success.

Predeclare which differences matter operationally, uncertainty intervals, stopping rules, and the smallest pilot exposure. Power calculations need baseline rates obtained from a bounded preliminary study; this paper invents none. Fail or revise the design if the scoped condition increases formal completion while leaving material-error detection unchanged, if audit costs erase saved effort, or if low-resource entrants systematically receive no actionable review.

Use adversarial strategies, not only cooperative agents: cheap plausible reviews; reciprocal approval rings; hidden shared operators; innocent disagreement punished as misconduct; end-of-participation extraction; identity reset; challenge floods; staged correction credit; promotion capture; and common-mode tool/data failures. Instrument actual behavior rather than accepting a model's claim that it acted independently. Human-participant studies require appropriate ethical review and consent; simulations cannot validate human uptake.

## 10. What follows, and what does not

The defensible claim is conditional: fixing the object of review can make responsibility, incentives, and correction inspectable. Cooperation then requires enough distinguishability between careful and careless conduct, enough continuing value or immediate compensation, credible audit funding, and realistic control of identity and coalition power. Those are measurable constraints, not implementation details to hide behind a badge.

The smallest promising system therefore offers a fixed object, asks for one bounded check, and makes repair useful. Complex scientific collaborations can inhabit that interface without exporting their entire internal bureaucracy. Whether those simple interactions produce a healthy institution remains an empirical question.

## Source and derivation note

The equations are derived here using established modeling methods; elementary identities are not claims of mathematical priority. The contextual synthesis and counterexamples are the proposed contribution. They are not claims that the cited literature proved MCRP effective. Primary-source web records were checked on 25 September 2026. Bibliographic verification of Fudenberg–Maskin used the author's MIT publication list; the linked PDF failed retrieval and no detailed theorem statement is attributed to unread text. The other citations link original research or author-hosted research records. The repository inputs were the two public MCRP posts, publication-policy v0.1, Commons prototype README, and the sibling backend-core threat model. Their scopes and limitations are preserved.
