# The scarce resource is a warranted judgment
## An economic design for versioned computational review

**Working paper; proposed design and analytical toy models. 25 September 2026.**

**AI contribution:** drafted by a specialist agent in an orchestrated research exercise. No claim of human scientific review, legal approval, empirical validation, or production implementation is made. The mathematical propositions below are conditional statements about explicit models, not findings about reviewer behavior.

**Research question:** How can a versioned, locally governed review commons allocate scarce qualified attention without converting wealth, popularity, or internal team size into scientific authority?

**Answer supported here:** A bounded-task interface, explicit resource and uncertainty budgets, payment-independent authority, and capacity-aware allocation expose important failure modes; conditional allocation and incentive models identify design constraints, while effectiveness and fairness remain untested.

### Abstract

A publication system can make assertions arbitrarily cheap without making warranted judgments cheap. The Minimum Credible Reproducibility Protocol (MCRP) can help by making the object and scope of a review portable: a decision refers to an exact claim, evidence set, acceptance contract, release, and authorized role. It cannot create the scarce expertise needed to evaluate the object. We model a commons in which nonrival review records are produced using rival attention, compute, coordination, and dispute capacity. Under a deliberately restricted detection model, optimal attention allocation equalizes marginal expected loss reduction per review hour; the solution is an interpretable water-filling rule with an explicit residual-risk floor. A queue model shows why submission growth or agent-generated review volume can destabilize human operations despite negligible hosting costs. A limited-liability incentive model shows when random audits can induce effort and when they cannot. Counterexamples demonstrate that payment-independent trust weights do not prevent attention capture, that per-claim entitlements invite claim splitting, and that sponsor noninterference is fragile without exit capacity. These results motivate a small human protocol: offer an exact object, check a bounded question, rely within a declared scope, and amend through a versioned successor. The proposed pilot measures coverage, delay, error discovery, and displacement—not badges, favorable verdicts, or submission totals.

## 1. What is being allocated?

The existing public MCRP proposal separates provenance verification, passing specified checks, and scientific disposition. We retain that distinction. A signed record is a useful object; a signature is not a unit of scientific truth. More agents, more reviews, more pages, and more endorsements are not interchangeable with more independently useful information.

There are four relevant goods:

1. **Released knowledge and review records:** largely nonrival after legitimate publication, but costly to produce, contextualize, preserve, and correct.
2. **Qualified attention:** rival, heterogeneous, and perishable. An hour of calibration expertise cannot always substitute for an hour of statistical expertise.
3. **Operational capacity:** moderation, private-data handling, appeals, assignment, and recovery. This is scarce even when compute and storage are cheap.
4. **Institutional credibility:** an imperfectly observable consequence of behavior and accountability. It is damaged when a visible label promises more than its evidence supports.

The appropriate economic unit is a **bounded review lot**: a declared task on a frozen object, an expertise requirement, a maximum effort budget, a deliverable, and an explicit remainder. Examples include checking whether one numerical result follows from identified inputs, examining one uncertainty calculation, or recording why one stated evidence relation is inadequate. A lot need not be a tiny fragment: a whole argument can be the appropriate indivisible task.

A large collaboration may execute thousands of internal checks before one accountable person releases a bounded report. A lone author may submit the same external object using a plain form. Internal organizational size does not create extra external authority. Team size matters to resource capacity and correlated failure, not to the number of independent votes.

This is an institutional-design proposal inspired by polycentric approaches to common resources, not a deduction that an online research commons inherits their successes. Communities should be able to choose local expertise and allocation policies while exchanging records with consistent meanings. Ostrom's work supplies a reason to study such variation, not a universal recipe. [1]

### 1.1 Relation to the existing localized-trust model

This paper extends the repository's candidate formal dynamics and Trust-Domain and Review-Governance Profile (TDRG), read at repository revision `18deff4993fca5a30cc2aff2e4f6e4433c6ff391`. Those drafts already distinguish domain/topic/capability/role layers, private durable accountability, fresh public case personas, root-relative capacity gates, local restart-walk routing, explicit bridges, newcomer exploration, and resource feasibility. Those ideas are inherited design premises, not contributions invented here. TDRG remains a proposed extension outside core MCRP conformance.

Our economic extension distinguishes three operations that a routing score can otherwise obscure:

1. **Admissibility:** may this reviewer take this task under this frozen layer, conflict, privacy, and authorization policy?
2. **Capacity allocation:** which feasible tasks and reviewers receive scarce time, operational support, and compute?
3. **Disposition:** what scientific judgment does a qualified authorized human record for the exact evidence boundary?

In the model below, a local trust view constrains feasible assignments. Its personalized stationary mass is neither the detection productivity a_ij nor the error probability p_i. The latter are hypothetical latent model parameters requiring independent measurement; extracting them directly from graph centrality would assume the desired scientific result.

A practical allocator can combine private layer-specific eligibility, workload, and a disclosed exploration policy. It must not publish person-level longitudinal scores to justify its assignments: that would defeat the fresh-persona privacy model. Public accountability can disclose the scoped eligibility predicate, assignment method, aggregate capacity and concentration, and a protected audit route. A reviewer may receive a private portable service credential or selectively disclose a contribution; automatic public linkage across cases is not a default economic incentive.

The inherited formal-dynamics comparison arms A0–A4 should retain the same downstream resource allocator where feasible. Otherwise adding a capacity-aware queue only to the proposed local-trust arm would attribute a scheduling improvement to trust inference. The economic experiments below are complementary allocation tests, not evidence that the frontier gate or restart walk is validated.

## 2. A deliberately small human protocol

The user-facing loop is four verbs:

**Offer → check → rely → amend.**

Requesting, committing effort, reporting, and repairing are local workflow substeps of this shared protocol, not a competing core vocabulary.

- **Offer:** “Here is the exact claim and release. Here is the check I want, why it matters, and the evidence boundary.”
- **Check:** “I can examine this boundary within this effort window. Here are my conflicts and shared dependencies.” A reviewer may decline without losing scientific standing.
- **Rely:** “I checked X and found Y. I did not check Z.” The underlying report is attributable and version-bound. A relying party states its intended use and limits; scientific disposition is an additional authorized human action, not a consequence of consuming a report.
- **Amend:** the author narrows, corrects, rebuts, or leaves the limitation visible. Material change creates a new decision context.

A scheduler may support this loop, but an author should not have to understand a reputation market or a massive rule table to participate. A conventional referee can attach a narrative review to a frozen manuscript and add a minimal scope wrapper. Legacy acceptance remains a fact about the venue's decision; it is not silently converted into MCRP scientific acceptance.

The commons owes an honest response about capacity, not a promise to review every submission. An unreviewed record must remain visibly unreviewed. An unresolved issue may be closed administratively as “capacity unavailable” while its scientific uncertainty remains open.

## 3. Attention allocation with explicit residual risk

### 3.1 Definitions and assumptions

Consider a fixed planning period and claims indexed by i. Let:

| Symbol | Meaning | Unit |
|---|---|---|
| h_i | Qualified human effort allocated to claim i | hours |
| H | Total available effort in this period | hours |
| p_i | Prior probability of the modeled consequential error | dimensionless |
| L_i | Loss if that error remains undiscovered in the decision context | loss units |
| a_i | Detection productivity for the modeled error class | inverse hours |
| b_i | Fraction of modeled errors inaccessible to this review method | dimensionless |
| eta | Shadow value of review capacity | loss units/hour |

Use one consistent decision-loss scale within an allocation exercise; do not add dollars, citation counts, and subjective importance without a declared conversion. Cross-field comparability is a normative choice. In practice, qualitative strata may be more defensible than pretending all scientific value has a common monetary price.

Assume that the probability of detecting the modeled error after h_i hours, conditional on an error, is

\[
 d_i(h_i)=(1-b_i)(1-e^{-a_i h_i}).
\]

The expected avoided loss is

\[
 B_i(h_i)=p_iL_i(1-b_i)(1-e^{-a_i h_i})=A_i(1-e^{-a_i h_i}),
 \quad A_i=p_iL_i(1-b_i).
\]

This assumes detection leads to a useful correction or changed decision; otherwise multiply by a separately estimated response probability and correction efficacy. It excludes false alarms, emergent interactions between claims, reviewer learning, and adversarial adaptation. It treats parameters as fixed and known. Those assumptions are strong, visible, and testable only for bounded error classes. The model is an allocation diagnostic, not a scientific truth estimator.

### 3.2 Proposition: marginal-value allocation

For a_i>0, A_i>0, and H>0, solve

\[
 \max_{h_i\ge0}\sum_i A_i(1-e^{-a_i h_i})
 \quad\text{subject to}\quad \sum_i h_i\le H.
\]

The unique solution is

\[
 h_i^*=\frac{1}{a_i}\left[\log\frac{A_i a_i}{\eta}\right]_+,
\]

where eta>0 is selected so the effort allocations sum to H. The notation [z]_+=max(z,0).

**Proof.** Each objective term has positive first derivative A_i a_i exp(-a_i h_i) and strictly negative second derivative. The feasible simplex is compact, and the objective strictly concave, giving a unique optimizer. Since every marginal benefit is positive, the capacity constraint binds. The KKT conditions set each active marginal benefit equal to eta and each inactive initial marginal benefit no higher than eta. Solving these conditions gives the formula. The sum is continuous and strictly decreasing on the eta range relevant to H, so eta is unique. ∎

This result is standard concave resource allocation specialized to an explicit review model. Its value is interpretability, not mathematical novelty. The log argument is dimensionless because numerator and denominator both have units of loss/hour.

### 3.3 Worked example

Set H=4 hours and three hypothetical lots:

| Lot | A_i (loss units) | a_i (1/hour) | Initial marginal benefit |
|---|---:|---:|---:|
| A | 10 | 1 | 10 |
| B | 4 | 0.5 | 2 |
| C | 1 | 1 | 1 |

The optimizer leaves C unallocated. The active budget equation is log(10/eta)+2log(2/eta)=4, hence eta=exp((log(40)-4)/3)≈0.9015. This violates the assumed inactivity of C because its initial marginal benefit 1 exceeds eta. All three must therefore be active. The correct equation is log(10/eta)+2log(2/eta)+log(1/eta)=4, giving eta=exp((log(40)-4)/4)≈0.9252. Thus h≈(2.3804,1.5419,0.0778) hours. The intentionally shown active-set correction illustrates why intuitive ranking is insufficient.

The avoided loss is approximately 11.30 units. These are synthetic values, not estimated MCRP benefits. A tiny nonzero allocation may be operationally meaningless: if every task has a 15-minute setup cost or minimum lot size, the continuous solution is no longer feasible. Use discrete lots and an explicit setup-cost knapsack or mixed-integer model. Do not round each allocation upward while claiming the same optimum or budget.

### 3.4 An irreducible floor

As h_i tends to infinity, residual expected loss tends to p_i L_i b_i. More effort of the same kind cannot remove a blind spot represented by b_i. Adding another agent with the same dependencies may increase repeated checking without reducing this floor. An independent method may reduce b_i, but that improvement must be argued or measured rather than inferred from a different account name.

### 3.5 Where efficiency becomes exclusion

A known-parameter optimizer can allocate almost nothing to a new field, an unfashionable claim, or a poorly documented author. Low estimated a_i may reflect missing onboarding infrastructure rather than poor science. Estimated L_i may reflect prestige. Initial information can therefore determine who ever receives enough attention to improve the estimates.

Reserve an explicitly governed share epsilon H for a lottery or rotation among eligible, underserved lots; allocate the remainder using local priority judgments. Eligibility still requires a bounded reviewable object and safety checks. This protects exploration; it does not prove equitable access or optimal scientific discovery. An equal lottery over claims is vulnerable to fragmentation and Sybils, so conduct it over accountable submission bundles within published cohort limits, with a reviewable override route.

The welfare cost of a reserve is not generically bounded by epsilon times total welfare. A reserved hour can displace the most valuable marginal hour; conversely, exploration can reveal badly underestimated value. Report realized displacement and parameter uncertainty rather than promising a free fairness improvement.

## 4. Heterogeneous expertise and indivisible evidence

Let x_ij be hours reviewer j allocates to claim i, and let a_ij represent productivity only where expertise, conflicts, and authorization permit the assignment. One extension is

\[
 B_i(x)=A_i\left(1-\exp[-\sum_j a_{ij}x_{ij}]\right),\qquad
 \sum_i x_{ij}\le H_j.
\]

This remains concave and supports reviewer-specific capacity prices. It assumes effort is substitutable after productivity weighting. That assumption fails when a claim requires both calibration and inference expertise: a perfectly reconstructed figure cannot replace a missing calibration evaluation.

A complementary model is

\[
 B_i=A_i\prod_{k=1}^{K_i}(1-e^{-a_{ik}h_{ik}}).
\]

Here every component is necessary. With two components and all initial effort zero, each single-coordinate marginal is zero. A purely greedy marginal scheduler can allocate nothing even when a coordinated bundle is valuable. The model need not be globally concave. Assign a composite lot with an accountable coordinator when evidence is complementary; do not fragment every scientific judgment into microtasks.

For team review, count total human time, coordination time, and shared dependencies. A team of twenty cannot manufacture twenty independent reports by naming twenty internal agents. Conversely, a solo reviewer should not be forced to expose private internal reasoning to obtain a portable scoped record. The boundary is inspectable evidence and responsibility, not a census of thought.

### 4.1 Feasibility has a price, and sometimes no price can buy it

The canonical resource vector separates CPU/GPU, storage, wall time, access, orchestration, operational support, human intelligence, and agent intelligence. Preserve that vector. A single dollar or effort scalar is adequate only after the feasible mode and substitution limits are declared. In particular, `record-only`, `downselect`, `witnessed`, and full-execution modes assess different boundaries; cheaper modes do not receive the scientific interpretation of a full path.

**Coverage impossibility.** Suppose a coverage contract requires at least k independently controlled eligible reviewers for one indispensable capability, but only m<k control groups possess that capability and permitted access. No feasible assignment exists, even with unlimited payments or additional identities within those groups. **Proof:** any assignment draws its distinct control groups from a set of cardinality m; its cardinality cannot reach k. ∎

This elementary result matters operationally. A sponsor cannot purchase independence by paying the same laboratory twice. The honest choices are to recruit an independently controlled capability, wait, narrow the scientific disposition, or amend the future contract visibly. The allocator cannot satisfy the original conjunction by averaging a strong score in another layer.

For a fixed feasible set, tightening a trust-frontier capacity or privacy constraint can only weakly lower the maximum of the same benefit objective because it restricts the feasible set. This is a set-inclusion result, not an argument to weaken protection: the objective omitted losses from capture and deanonymization. Report the lost coverage together with the avoided risk. Compare policies on a vector of scientific utility, privacy, inclusion, and operating cost rather than disguising the omitted values inside a single score.

## 5. Capacity, queues, and the automation paradox

### 5.1 Stability is a resource condition

Let admitted review lots arrive at rate lambda per day. Each requires a mean of s human hours, including assignment, moderation, scientific evaluation, and expected dispute handling. Let H_d denote available human hours/day. A necessary non-overload condition is rho≤1; a practical stochastic service should target strict slack:

\[
 \rho=\frac{\lambda s}{H_d}<1.
\]

Exactly rho=1 need not be unstable in a perfectly synchronized deterministic system, so strict inequality is not a universal mathematical necessity. In ordinary stochastic queues it supplies needed slack, but is not universally sufficient: incompatible specialties, priority starvation, correlated absences, and heavy-tailed disputes can destabilize subqueues. Count arrivals requiring human handling, not just published reviews.

For an idealized single equivalent server with Poisson arrivals and exponential service times, let mu=H_d/s in lots/day. Mean time in system is W=1/(mu-lambda) days. With H_d=8 hours/day and s=2 hours/lot, mu=4 lots/day. At lambda=3.2, W=1.25 days; at lambda=3.8, W=5 days. These are M/M/1 illustrations, not forecasts for multi-expert volunteer review. Little's relation L=lambda W links stationary throughput, mean occupancy, and mean time under appropriate assumptions; it does not imply stability when means do not exist. [2]

### 5.2 Automation can worsen congestion

Suppose automation multiplies admissions by k and reduces mean human effort to r times baseline. Then rho_new=kr rho_old, with capacity unchanged. Starting from rho_old=0.7, doubling arrivals and reducing effort by 25% gives rho_new=1.05. Cheap production has overwhelmed expensive verification.

Compute-mediated duplication is particularly dangerous: ten superficially distinct objections may require ten moderation decisions even when they contribute one underlying issue. Deduplicate by exact target and substantive issue where possible, but permit new evidence on an existing issue. Rate limits are admission controls, not scientific judgments.

### 5.3 Version churn consumes real capacity

If n accepted records each generate relevant changes at average rate nu per day, and reassessment costs mean u hours, their maintenance load is n nu u hours/day. Add this to new-review and operations loads. A capacity plan that pays for first acceptance but omits follow-up is selling an unfunded continuing obligation.

A dependency graph can reduce the set requiring reassessment only insofar as it is complete and semantically appropriate. Not every byte change warrants a full new scientific review, but every changed bound context requires an explicit new decision or a valid scoped carry-forward procedure. Administrative effort savings cannot justify silently inheriting a stale approval.

## 6. Paying for effort without buying agreement

### 6.1 A narrow incentive proposition

Consider a reviewer choosing costly effort e=1 or shirking e=0 on a task for which an independent audit can detect specified nonperformance. The reviewer receives fixed compensation w, pays effort cost c if diligent, and is audited with probability q. Conditional on audit, nonperformance is detected with probability d_e, with d_0>d_1. A detected failure incurs the fixed loss F in payment or equivalent continuation utility, with 0≤F≤F_max under a declared liability or humane-policy cap. Equivalently F can be the same conditional expected loss under both actions, provided risk neutrality and that equality are explicit. All monetary values are in the same utility units, risk neutrality is assumed, and reputational/private motivations are held fixed. Audit commitment, audit effort, and correct execution are exogenous here; this reviewer incentive calculation does not establish that an auditor will perform the work or that funding is credible.

Expected utility is

\[
 U(e)=w-ce-q d_eF.
\]

Diligent effort is weakly preferred exactly when

\[
 q(d_0-d_1)F\ge c.
\]

**Proof.** Subtract U(0) from U(1): -c+q(d_0-d_1)F. ∎

Participation additionally requires w-c-q d_1F≥u_0, where u_0 is the outside-option payoff. Paying for effort and inducing it are separate constraints.

If limited liability or a humane policy caps F at F_max and c>(d_0-d_1)F_max, even auditing every task cannot induce effort in this model. If q=0 or d_0=d_1, the audit supplies no effort incentive. Large reputation penalties are not a costless substitute: they can deter entry, amplify mistaken sanctions, and make reviewers avoid novel or controversial claims.

An audit may check that a computation was run or a cited source examined. It cannot generally determine whether an honest scientific disagreement is “wrong.” Therefore do not fine reviewers for dissent, a negative verdict, or a claim later being revised. Use the proposition for bounded, observable process obligations, with appeals; it is not a truthfulness theorem for science.

### 6.2 Why consensus rewards are hazardous

With two reviewers paid for matching binary reports and no external check, both always reporting “pass” is an equilibrium: a unilateral deviation loses payment regardless of evidence. Stronger peer-prediction mechanisms can incentivize information under explicit signal and task assumptions, but this does not give a general scientific-truth guarantee. Foundational models study endogenous effort and multiple-task information elicitation; correlated agreement work supplies carefully delimited informed-truthfulness properties. [3,4]

MCRP should initially compensate a bounded completed task or reserved expertise window independent of verdict, expose the deliverable, and sample process audits. Neither a fixed fee nor an audit makes the system automatically incentive compatible. Fixed fees can invite low effort; completion metrics can favor easy claims; error bounties can reward exaggerated attacks. Replication incentives have been studied in connection with overturn bias, a warning against treating contradiction counts as quality. [5]

Field evidence that deadlines and payments can affect review turnaround does not establish that they improve scientific validity or transfer unchanged to voluntary commons. Chetty, Saez, and Sándor's referee experiment is a relevant primary study, not a parameter estimate for MCRP. [6]

## 7. Financing and the two routes to capture

### 7.1 A transparent budget identity

For one period, let fixed infrastructure and administration cost F_0, human service hours H_j at accounting rates w_j, compute jobs g_k at unit costs c_k, and planned net reserve contribution R during the period (a flow, distinct from opening liquid reserve balance B). Required revenue is

\[
 C=F_0+\sum_j w_jH_j+\sum_k c_kg_k+R.
\]

Donated labor lowers cash outlay, not resource consumption. Report both. Supporter convenience tools and pooled sponsorship can fund this budget while scientific participation remains free. Expensive compute or honoraria require explicit campaign budgets; do not hide them inside unlimited low-price memberships. No historical vendor price or private planning estimate is treated here as a current quote.

Define disposition D=f(E,Q,P), depending on release evidence E, qualified authority Q, and adopted policy P. A required formal invariant is that changing payment status alone does not change D or qualification. This is necessary but insufficient.

### 7.2 Counterexample: visibility capture without paid verdicts

There are 100 admissible unsponsored lots, and a sponsor submits 100 equally eligible lots. A neutral lottery allocates 20 review slots. Expected unsponsored allocation falls from 20 to 10, although every individual trust calculation ignores money and reviewers remain honest. Additional submissions changed the denominator.

Thus “payment never changes trust weight” does not guarantee payment-independent opportunity. A sponsor can also buy better documentation, faster execution, or publicity; those may improve real evidence while still widening opportunity gaps. MCRP need not prohibit all resource advantages. It must distinguish funded production from scientific authority and measure displacement in the common queue.

A proposed guardrail is a common pool with published capacity plus separately funded campaign capacity. Campaign contributions pay the full marginal scientific and operational burden and a declared contribution to shared capacity. If campaign work displaces common expertise, its accounting cost must include that opportunity cost. Separate labels alone do not create extra reviewers.

### 7.3 Counterexample: exit threats defeat formal noninterference

An operator owes C per month, receives g from its largest sponsor, has no alternative income surplus, and holds liquid reserve B. If that sponsor withdraws, runway against the resulting deficit is B/g months, assuming other costs and revenues remain unchanged. With B=0, even an excellent noninterference clause leaves immediate survival pressure.

Funding concentration, recusal, portable exports, credible replacement sponsors, and reserves therefore matter to epistemic independence. A desirable reserve target depends on credible replacement time, not a magical universal number. Report the largest sponsor's revenue share and the modeled loss-of-sponsor runway. This is an organizational risk model; it predicts pressure, not inevitable misconduct.

## 8. Fragmentation, status, and scarce recognition

Suppose each claim receives one guaranteed hour. An author can split an argument into k claims and receive k hours. The allocation rule rewards representation choices rather than scientific need. A per-person rule instead penalizes large legitimate collaborations and is vulnerable to identity multiplication. There is no costless perfect denominator.

Use bounded submission bundles, a declared responsible party, deduplicated dependencies, and community-specific allocation budgets. Keep the budget assignment appealable. Avoid claiming Sybil resistance merely because accounts are pseudonymous or verified.

Recognition is another scarce resource: everyone can receive a badge, but a badge useful to readers must distinguish contributions. Status competition may mobilize effort and also encourage conspicuous attacks, performative certainty, or citation clubs. Proposed recognition should describe observable work—scope completed, correction responsiveness, reproducible evidence supplied—without collapsing those dimensions into a universal rank. Compare like tasks, include denominators, and do not penalize a reviewer whose difficult unresolved result was scientifically useful.

An accountable review object and a private, selectively disclosable service credential can be portable capital; they should not expire merely because a contributor cannot afford a subscription. Under TDRG, public recognition attaches to the review object or case persona, while durable actor-level history remains in protected custody. A service that publishes a permanent public reviewer profile is using a different privacy profile and must say so. Paid navigation features should leave the underlying relationships usable through an accessible free representation.

## 9. Computational experiments that can fail the design

All numerical experiments below are synthetic. Save parameters and seeds, report the full sweep, and avoid calling simulated error detection “real scientific accuracy.”

### E1: allocation under misspecification

Generate n=200 lots with A_i from a lognormal distribution and a_i from a second lognormal distribution; record the exact parameterization. Compare equal allocation, initial-marginal greedy discrete lots, exact continuous water filling, and a policy reserving epsilon in {0,0.1,0.25} for underserved exploration. Set H in {50,100,200} hours. Perturb observed log(A_i) and log(a_i) with zero-mean Gaussian noise of standard deviation sigma in {0,0.5,1}. Run 100 independent seeds and evaluate using the latent generating values. Report true avoided loss, coverage, worst-group coverage, and displacement. Add a deliberately biased estimate for one underserved group. **Failure criterion:** the recommended practical policy repeatedly loses both true benefit and underserved coverage relative to equal allocation; investigate before recommending it.

### E2: arrival growth and hidden operations

A discrete-event or daily workload simulation should sweep baseline load rho in {0.5,0.7,0.9}, arrival multiplier k in {1,2,4}, and human-cost multiplier r in {1,0.75,0.5}. Add appeal probability z in {0,0.05,0.2} and appeal service cost sampled from an explicit heavy-tailed distribution truncated at a declared maximum. Simulate 365 days with 100 seeds. Report backlog growth, oldest unresolved item, rejected admissions, appeal delay, and total labor. Compare capacity-aware admission against unbounded admission. **Failure criterion:** supposedly stable settings develop persistent specialist or appeal backlogs; mean total workload was an insufficient capacity metric.

### E3: sponsor and splitting attacks

Hold 100 unsponsored bundles fixed; add 0–400 sponsored bundles. Compare a single neutral lottery, separate genuinely additive campaign capacity, and per-bundle capped common allocation. Repeat when sponsored capacity draws 0%, 25%, 50%, or 100% of its hours from the existing reviewer pool. Then let one author split one bundle into 1, 5, or 20 claims. Report expected unsponsored review hours and per-responsible-party concentration. **Failure criterion:** claimed payment neutrality masks falling common-pool opportunity or fragmentation increases entitlement.

### E4: bounded audit feasibility

Plot the region q(d_0-d_1)F≥c over explicit hypothetical grids. Include false-positive audit rates, capped penalties, participation constraints, and audit labor. Optimize neither on simulated sincerity nor on agreement. **Failure criterion:** feasible incentives require more audit labor than the reviewed task, or penalties unacceptable under the service's participation policy. In that region prefer trusted professional relationships, narrower obligations, or admit that the incentive problem is unsolved.

## 10. A falsifiable human pilot

Recruit a bounded voluntary cohort working on public or synthetic releases and obtain any applicable institutional review determination before treating participation as human-subject research. Predeclare assignment, exclusions, outcome coding, handling of conflicts, and escalation. The protocol being tested is modest: whether versioned bounded requests produce useful independently inspectable work at tolerable human cost.

**H1: bounded scope reduces completion cost.** Randomize eligible review requests to a standard narrative invitation or a bounded lot wrapper, preserving the same substantive target. Measure invitation acceptance, completion, actual time, and expert-coded missed material issues. Cost reduction without preserved issue coverage is not success.

**H2: visible limits prevent overinterpretation.** Randomize readers to a generic “reviewed” label or a scoped record stating the checked boundary. Ask which downstream statements are warranted. The intended effect is fewer unwarranted inferences, not higher trust ratings.

**H3: a reserve improves opportunity.** Within ethics and capacity constraints, randomize otherwise comparable queues to allocation with or without a disclosed exploration reserve. Measure review coverage by prespecified resource stratum, total useful findings, and waiting time. Small pilots estimate feasibility and variance; they cannot substantiate broad fairness claims.

**H4: funded campaigns add capacity.** Measure reviewer hours supplied, common-pool hours displaced, moderation/appeal burden, and unreviewed residual work before and during a campaign. A financial surplus with a worsening common queue is not successful additionality.

**H5: repair is cheaper than restarting.** Compare time to reevaluate a changed release with and without an explicit dependency-change summary, using equivalent seeded changes. Measure missed affected claims as well as speed. A fast but incomplete carry-forward is a failure.

Do not power the pilot using invented effect sizes. Use a feasibility stage to estimate recruitment, attrition, outcome variability, and specialist capacity; then register a confirmatory design if warranted. Publish null results and stopping reasons. No claimed benefit in this paper depends on these hypotheses already being true.

## 11. The boundary of the proposal

The mechanism cannot make all worthy science receive attention, infer independent judgment from identity counts, equate reviewer agreement with truth, or remove domination from a social institution. It can make allocation and responsibility inspectable: who asked for what, who accepted which burden, what was checked, what remained unknown, which resources paid for it, and how correction changes the record.

A viable MCRP commons would sell convenience and funded capacity while preserving free scientific participation and portable evidence. Its central scarce product would remain a qualified person's bounded, revisable judgment. The decisive test is whether that product becomes more useful per unit of total human effort without exporting costs or excluding the least resourced contributors.

## References

[1] Elinor Ostrom. *Beyond Markets and States: Polycentric Governance of Complex Economic Systems*. Nobel Prize lecture, 2009; published in *American Economic Review* 100(3), 641–672, 2010. [Primary lecture page](https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/lecture/?lbw=1).

[2] John D. C. Little. “A Proof for the Queuing Formula: L = λW.” *Operations Research* 9(3), 383–387, 1961. [Publisher record](https://doi.org/10.1287/opre.9.3.383).

[3] Anirban Dasgupta and Arpita Ghosh. *Crowdsourced Judgement Elicitation with Endogenous Proficiency*. 2013. [Author preprint](https://arxiv.org/abs/1303.0799).

[4] Victor Shnayder, Arpit Agarwal, Rafael Frongillo, and David C. Parkes. *Informed Truthfulness in Multi-Task Peer Prediction*. 2016. [Author preprint](https://arxiv.org/abs/1603.03151).

[5] Sebastian Galiani, Paul Gertler, and Mauricio Romero. *Incentives for Replication in Economics*. NBER Working Paper 23576, 2017. [Primary working-paper record](https://www.nber.org/papers/w23576).

[6] Raj Chetty, Emmanuel Saez, and László Sándor. *What Policies Increase Prosocial Behavior? An Experiment with Referees at the Journal of Public Economics*. NBER Working Paper 20290, 2014. [Primary working-paper record](https://www.nber.org/papers/w20290).


## Adversarial integration note

Allocated time, attempted service, completed declared checks and scientifically covered scope are different outcomes. The numerical quarter-hour diagnostic measures only time allocation. Before/during campaign comparisons are descriptive; causal capacity additionality needs a justified counterfactual, such as a staggered design with measured capability-specific demand and supply. Full-cost payment does not establish additive expertise. Newcomer access remains conditional on feasible supervision and the same shared capacity ledger. The implemented water-filling helper is a sensitivity tool with a declared numerical domain; extreme finite scales can fail explicitly. No allocation-efficiency deployment claim follows.
