# A small protocol with a finite correction cone

**Scientific synthesis and second-round design critique, 25 September 2026.** An AI drafting lane in the same orchestration and operator context as the companion papers. This is not external scientific validation.

## Abstract

The strongest case for MCRP is not a better reputation score. It is a portable boundary between evidence production and consequential reliance: a reader can discover exactly what was checked, what remains assumed, and what must be reconsidered when an input changes. We propose a single four-action interface with progressive disclosure and analyze the condition under which its correction workload remains supportable. A multitype branching model shows why a healthy average can hide a failing specialty, while a finite-network expansion distinguishes real divergent workload from double-counted paths. A simple probability argument specifies what end-to-end assurance would require without assuming independent reviewers. The resulting design principle is to minimize mandatory interaction while retaining typed authority, private accountability, and explicit uncovered scope. The proposal is falsifiable against ordinary structured review and should be rejected if its bookkeeping does not improve error detection, interpretation, or repair per total human hour.

## 1. The smallest useful promise

A useful review does not make the whole paper safe. It allows someone to say:

> For this exact release and this use, these checks were performed; these assumptions remain; this party made the decision; this change would reopen it.

This is the central scientific object: a **revisable reliance statement**. It may incorporate a normal referee letter, a numerical rerun, a calibration witness, a restricted-data attestation, or an institution's existing decision. Each preserves its own scope and authority. An author can publish a contribution without obtaining a favorable scientific disposition. A qualified authorized human remains responsible for the scientific disposition under the current profile.

Use one vocabulary throughout the research program:

**Offer → check → rely → amend.**

An offer can request work; a check can be accepted, declined, performed, or left incomplete; a reliance decision names its authorized decision-maker; an amendment changes an exact object or records a challenge. These are four views of an interaction, not four universal machine states or four exclusive sequential steps. An amendment can precede a first check, and multiple checks can proceed concurrently. Scheduling commitments and legal intake retain their own internal state machines.

The ordinary participant sees the target, requested or performed check, limits, and next action. Identity credentials, policy versions, digest details, private standing, and solver receipts remain available to the appropriate observer when relevant. Progressive disclosure does not mean invisible conditions: a material dependency, conflict, expiration, or missing capability is visible at the decision boundary.

Do not teach four incompatible sets of verbs across the specialist papers. Their local concepts are useful implementations of the shared interface, not competing protocols.

## 2. Interface compression is not assurance compression

A participant needs neither to understand a trust graph nor to audit an entire detector collaboration. The system nevertheless must distinguish:

- object identity/integrity;
- checks actually performed and their coverage;
- authorized scientific disposition;
- authorization to publish and actual public delivery;
- participation, content visibility, and identity-opening decisions.

There must be no universal green checkmark spanning those distinctions. In the simplest useful display, the scientific statement is ordinary prose: “This numerical reconstruction passed; calibration was not assessed; no scientific disposition is recorded.” Unknown is a valid output, not a software exception.

A trusted service can reduce repetitive verification. It cannot replace the scientific endpoint's decision about whether the evidence supports the intended use. This is a design analogy to Saltzer, Reed, and Clark's end-to-end argument: functions requiring application knowledge cannot be completed solely by a lower layer. Their communication-system result does not prove this scientific design, but gives a precise reason to resist upgrading delivery or provenance into acceptance. [Saltzer, Reed, and Clark, 1984](https://web.mit.edu/saltzer/www/publications/endtoend/endtoend.pdf).

## 3. A compositional model that permits arbitrary internal complexity

Let a module expose a boundary record

\[
B=(v,C,D,K,A,U),
\]

where \(v\) identifies its release, \(C\) is the scoped claim, \(D\) the dependencies relevant to the intended use, \(K\) the checks and residual limits, \(A\) the accountable authority, and \(U\) the update route. Access restrictions apply to components; exposing a boundary does not require publishing protected evidence or civil identity.

The same record can describe one researcher or an internally elaborate collaboration. Organizational scale can change the credibility of \(K\), resource availability, and common-control dependencies; it does not change the record's grammar or multiply independent authority. An agent team acts through the currently authorized human/principal adapter. This proposal does not silently replace TDRG's natural-person enrollment with organization enrollment.

Suppose a downstream reliance depends on \(m\) indispensable boundary predicates. Let \(F_j\) be failure of predicate \(j\), including a missing material dependency. If independently justified upper bounds \(P(F_j)\le\epsilon_j\) are available under a common, specified probability model, then

\[
P(\text{at least one indispensable predicate fails})
\le\min\{1,\sum_{j=1}^m\epsilon_j\}. \tag{1}
\]

**Proof.** The failure event is a union; apply the union bound. No independence premise is needed.

Equation (1) is standard probability, not a new review metric. Its value is to show what a compositional guarantee costs: every indispensable premise needs a defensible bound, and the bound must include unmodeled-dependency risk. A probability that a theorem is correct is not supplied by its DOI, reviewer count, or routing mass. If a bound is unavailable, report an unquantified assumption rather than substitute zero. Shared systematic error can dominate all the numerical terms. Conversely, a known common event can be represented once instead of counted as independent replications.

Boundary substitutability is therefore conditional. Two internal implementations are interchangeable **for the declared external protocol observations** if they preserve the same boundary behavior. They are interchangeable for scientific reliance only if their relevant evidence and failure assumptions remain valid. The first is a representational fact; the second demands scientific work.

## 4. Repair across unequal specialties

The scalar offspring mean \(R=bq(1-c)\) in the companion science paper is informative for a homogeneous tree. It does not characterize heterogeneous scientific infrastructure.

Partition reconsideration work into \(k\) types, for example calibration, inference, software, and privacy/operations. Let

\[
M_{ab}=E[\text{new type-}b\text{ work items produced by one type-}a\text{ item}].
\]

Here an item means distinct material work after whatever legitimate deduplication the model assumes. It is not a notification. Let \(z_0\) be a row vector of initiating items, and assume a time-homogeneous multitype branching approximation with finite first moments and conditional expected offspring determined by type. Then

\[
E[z_n]=z_0M^n.
\]

If the spectral radius \(\rho(M)<1\), the expected aggregate work vector is

\[
\boxed{t=z_0(I-M)^{-1}.} \tag{2}
\]

**Proof.** Conditional expectation gives the generation recurrence. Summing yields the matrix geometric series; its convergence for \(\rho(M)<1\) gives the inverse. Independence of individual offspring is not needed for this first-moment identity if the conditional mean relation holds.

If \(\rho(M)\ge1\), a positive starting vector reaching the relevant nondecaying classes can have divergent expected total work. An unreachable supercritical block does not affect a particular root; use the root-reachable submatrix. A critical process may die out almost surely and still have infinite expected total progeny. Neither divergent expectation nor a large eigenvalue asserts that a real finite scientific graph literally creates infinitely many claims.

**A misleading average.** Consider

\[
M=\begin{pmatrix}.2&.01\\.01&1.2\end{pmatrix}.
\]

The equally weighted mean row sum is .71. A scalar approximation using it predicts \(1/(1-.71)\simeq3.45\) tickets. But the Perron root is approximately 1.20010. The second specialty is supercritical in the unbounded model and is reachable from the first. The average did not describe the reproduction of the evolving type mix.

**Stable does not mean affordable.** For

\[
M=\begin{pmatrix}.2&.1\\.05&.6\end{pmatrix},\qquad z_0=(1,0),
\]

\(\rho(M)\simeq.61213\), and \(t\simeq(1.26984,.31746)\). If type-specific effort is \(h=(1,8)^\top\) hours per item, expected cost is \(th\simeq3.80952\) hours per initial item. At two initial items/day, mean demand is approximately 2.54 type-1 hours/day and 5.08 type-2 hours/day. Capacities of 4 and 4 hours/day fail the specialist capacity condition even though total demand 7.62 is less than total capacity 8.

For independent root arrivals with mean vector \(\lambda\), define workload per type

\[
L_b=[\lambda(I-M)^{-1}]_b h_b.
\]

Necessary average feasibility is \(L_b\le H_b\) for dedicated type capacity. Strict slack is the practical stochastic target; these inequalities alone are not latency or queue-stability theorems. Substitution between skills requires an explicit feasible scheduling model.

## 5. What coalescing can and cannot save

Batching 100 notifications about a calibration defect into one message saves communication. It does not by itself save 99 scientific impact assessments. A common rerun can save scientific work only where a sound shared result actually discharges several obligations. Estimate separate coefficients for notification deduplication, reused verification work, and remaining per-reliance decisions.

In a finite acyclic dependency graph with nilpotent propagation matrix \(P\), a linear path expansion ends after depth \(D\):

\[
t=z_0\sum_{n=0}^{D}P^n.
\]

It is finite regardless of an apparent early branching rate. If two paths reach the same claim, this expression can count multiple visits. To estimate distinct affected claims, deduplicate claim/version identifiers or explicitly model the shared work; do not call the path sum a distinct-claim count. Cycles require a case policy defining what genuinely new evidence permits reopening, rather than repeatedly resending the same change.

An operational correction cone is the set of downstream reliance statements whose declared dependency boundary intersects a material change. Its size, required skills, and unresolved work are empirical quantities. A repair receipt can mark those uses as pending without promising immediate revalidation. A timeout never turns pending science into an accepted claim.

## 6. Behavioral dynamics: local simplicity is necessary, not sufficient

People can coordinate around one visible act—an inspectable useful check—while the network of acts becomes complicated. That is a plausible route to self-organization. It requires several empirical conditions:

1. Making a bounded contribution must be cheaper than learning the governance machinery.
2. A useful small contribution must retain value even if the author cannot complete the entire review.
3. A newcomer must have a reachable route to inspection without an incumbent's personal sponsorship.
4. A private or pseudonymous contribution must obtain credit without a forced public longitudinal identity.
5. Criticism must change evidence and scope more cheaply than it can create adjudication labor.

Neither a prestige score nor more transparency establishes these conditions. Public ranking can convert a correction into a dominance contest; private attribution can also hide exclusion. Offer optional selectively disclosed contribution receipts, measure outcomes, and retain protected audit rather than promising a universal motivational mechanism.

The existing feedback model correctly shows local loss of symmetry when \((1-\zeta)\beta\chi>K\). Its parameter \(\beta\) depends on the scale of shares and the definition of groups. A platform cannot read this threshold as “keep beta below K” before estimating the actual feedback map. The more portable intervention is to keep assigned opportunity separate from evidence of competence and to monitor sensitivity to initial advantage.

## 7. A bounded experiment that could reject this design

Begin with ordinary review letters and stable public/synthetic releases. Compare ordinary review, a simple claim/scope template, and the four-action progressive-disclosure interface using the same task pool and total labor budgets. Add trust routing only in a separate experimental factor. Otherwise UI structure, scheduling, and reputation effects are confounded.

A first demonstration should contain one solo author, one large collaboration adapter, and one agent-team adapter completing the same external task. Do not require equivalent internal workflows. Require preservation of scope, accountable human disposition, restricted access, unknown fields, and material-change links.

Use planted changes in a small dependency graph: shared calibration, a local numerical error, a stale artifact, an unrelated edit, and a hidden common-control reviewer pair. Predeclare the complete affected-claim set for each fixture. Measure recall and precision of correction-cone detection, missed scope, total person-minutes including stewards, specialist backlog, and time until a reader can tell that reliance is pending. Hold notification counts separate from scientific work.

Evaluate claim interpretation through concrete questions, not trust ratings: “Does this record establish calibration validity?” “Can this release support the proposed downstream use?” “Who may authorize that use?” Measure unsupported inferences and wrong authority upgrades.

Reject the richer design if the simple template provides equivalent useful coverage and repair at lower total cost. Reject a repair optimization if it lowers ticket count while missing affected claims. Reject the claimed scale invariance if large teams obtain more authority solely by exporting more internal actors. Reject a privacy claim if public receipts systematically link supposed fresh personas. A small pilot cannot prove broad uptake or legal compliance; its function is to reveal whether the interface is worth further study.

## Source and result note

The new equations are transparent applications of the union bound and matrix geometric series, not novelty claims. Numerical cases and the dedicated-capacity counterexample are reproduced by `model_checks.py` and `results.json`. The original science model's seven unit tests passed during this review. Saltzer et al.'s author-hosted PDF was opened on 2026-09-25; its title, authors, publication metadata, and end-to-end placement argument were checked. We use it as a systems-design precedent, not empirical evidence about scientific communities.


## Adversarial extension: changing regimes and hidden dependencies

The resolvent is time-homogeneous. Let MA=((0,2),(0,0)) and MB=((0,0),(2,0)). Both have spectral radius zero, yet alternating generations from (1,0) produce 1,024 items at generation ten. Snapshot subcriticality does not ensure dynamic safety. A sufficient stronger condition is one positive vector v and r<1 with M_t v <= r v for every admissible regime. Then expected weighted generation work is at most r^n z0 v and total is at most z0 v/(1-r). This conditional envelope may be unknowable or too conservative in practice.

A declared correction graph also needs a withheld scientific oracle in synthetic tests: omit a true indispensable edge and add an irrelevant one. Measure scientific affected-set recall and precision separately from reachability in the recorded graph. The boundary fixtures do this and distinguish expired/freshness-unknown receipts from historical dispositions. They demonstrate selected semantics, not dependency completeness, real refresh infrastructure or cryptographic validation.

Across lanes, enforce each person's total review, audit, repair, intake, and appeal commitments against one capacity ledger, with skill and recusal constraints. Separately feasible subsystem budgets cannot spend the same hour repeatedly.
