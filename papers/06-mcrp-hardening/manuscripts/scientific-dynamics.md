# Small interfaces, bounded reliance: a scientific model of MCRP

**Working paper — 25 September 2026.** AI-assisted research draft; no human
scientific endorsement, submission, or deployment is implied. Equations describe
declared models, not measured behavior of scientists or agents.

**Question.** Can a small interaction protocol support heterogeneous scientific
review communities without turning local trust into unbounded authority?

**Answer supported here.** Four public actions can carry the necessary distinctions,
but their useful operating region is constrained by attention, correlated error,
feedback, and repair capacity. We derive conditional boundaries and counterexamples;
we do not establish adoption, social efficacy, or a novel universal trust algorithm.

## Abstract

The Minimum Credible Reproducibility Protocol (MCRP) ties scientific claims and
checks to exact releases. Its trust-domain extension supplies rich machinery for
accountability, privacy, routing, and appeals. Rich machinery is not a usable human
protocol. We propose a small interface—offer, check, rely, amend—whose records are
portable across individuals, collaborations, agents, and agent teams. The human
sees the claim, scope, responsible party, evidence, and remaining uncertainty;
software carries versions, digests, role constraints, and event history. Simple
interactions can generate complex review networks, but simplicity alone does not
make their equilibria desirable. Analytical models identify three distinct failure
boundaries: normalized trust ingress, endogenous attention reinforcement, and
supercritical reconsideration workload. An equicorrelation calculation shows why
twenty nominal reviewers need not provide twenty independent checks. Reproducible
synthetic sweeps illustrate these models and include a normalization counterexample
that defeats a naive capacity defense. We propose experiments that could reject
the design in favor of ordinary structured review.

## 1. What must remain simple

The relevant unit is a **bounded reliance relation**, not a person score. Someone
offers an identified claim with evidence; someone performs a stated check; a
responsible reader or institution decides what to rely on; subsequent evidence
can amend that decision. The protocol must make those actions easy while making
their accidental conflation difficult.

| Action | Human question | Durable record |
|---|---|---|
| Offer | What exactly are you asking someone to inspect? | Claim/release, proposed scope, budget and expiry |
| Check | What did you examine, and what remains unresolved? | Evidence, method, limitations, controls and conflicts |
| Rely | Who accepts which use, under which conditions? | Scoped accountable decision, authority and expiry |
| Amend | What changed, and which earlier uses need reconsideration? | Linked challenge, correction, supersession or withdrawal |

These are interaction verbs, not four database tables or exclusive sequential
states. Amendments can precede a first check and checks may run concurrently. A check may have many
executions. An amendment may invoke an existing scientific, private-standing, or
conduct appeal. Rights-sensitive complaints remain a separate operator obligation.
The detailed TDRG machinery is an implementation profile below this interface;
it is not a questionnaire every author must answer on every submission.

Three visible statements accompany a release: **identity/integrity**, **checks
performed**, and **scientific disposition**. A fourth, delivery observation, is
needed when claiming particular bytes reached a public endpoint. No green status
automatically upgrades another. A publication authorization is not a scientific
disposition, and neither can be inferred from a transport acknowledgment.

### Composition across internal complexity

Represent each participating unit by a boundary descriptor

$$U=(\text{principal},\text{scope},\text{inputs},\text{outputs},
      \text{resource envelope},\text{control disclosures}).$$

A single author and a thousand-agent laboratory can expose the same descriptor.
The laboratory may recursively use this protocol internally. The external
contract asks what its boundary outputs support, who is accountable, and which
dependencies correlate its checks. It does not demand equal internal cognition.
Replacing the internal workflow with another that preserves every externally
observed contract field preserves the **protocol projection**. This is a
substitutability statement by definition, not a claim of scientific equivalence:
an omitted control dependency breaks its premises.

The principal descriptor is an organizational boundary adapter, not a change to
TDRG's natural-person enrollment or its qualified-human scientific-disposition
authority. A separately reviewed organizational-enrollment profile would be needed
to change those rules. Internal replication never mints independent external votes. Multiple agents
sharing an operator, model, evidence selection process, or incentive can add
coverage without supplying independent authority. The system should accept
declared lower-resource checks with appropriately narrow scope, rather than
requiring every participant to reproduce a large collaboration's infrastructure.

### Trust, prestige, and dominance

Human reviewers may respond to competence, reciprocity, prestige, obligation,
status, coercion, and curiosity. Treating refereeing as only trust and dominance
would prematurely close the model. Endorsement models already show that hierarchy
can emerge from simple feedback rules [1]. That motivates a falsifiable hypothesis:
making useful, corrigible checks visible can redirect some status incentives toward
evidence production. It does not establish that public scoring will do so. A global
leaderboard may instead reward volume, consensus, or aggressive challenges.

## 2. Imported influence: a theorem and its missing premise

Let a row-stochastic transition matrix $T$ route attention among actors, with
restart distribution $s$ and $0\leq\alpha<1$:

$$p=(1-\alpha)s+\alpha T^\top p.$$

Partition actors into an importer region $H$ and external region $X$. Write
$r=s(X)$. Suppose **every** $H$ row sends at most $\epsilon$ probability mass to
$X$, and every $X$ row sends at least $\gamma$ to $H$. Then, writing $x=p(X)$,

$$x\leq(1-\alpha)r+\alpha[\epsilon(1-x)+(1-\gamma)x],$$

so

$$\boxed{x\leq\frac{(1-\alpha)r+\alpha\epsilon}
 {1-\alpha+\alpha(\epsilon+\gamma)}}. \tag{1}$$

The denominator is positive. A two-state chain with rows
$(1-\epsilon,\epsilon)$ and $(\gamma,1-\gamma)$ attains equality, proving
tightness within these assumptions. The existing candidate lemma is recovered
at $r=\gamma=0$. If no minimum egress is enforceable, use $\gamma=0$; voluntary
external promises of exit do not justify a positive value. Root corruption must
be modeled through $r$ or by revising the partition. A claimed honest region that
contains an undisclosed controller is simply the wrong partition.

At $\alpha=.85$ and $\epsilon=.01$, the worst-case mass is approximately
$0.05363$. This is a bound on one routing feature, not review correctness,
admissible actor count, or final assignment probability.

**Counterexample: raw capacity is not probability.** Give an honest root one
outgoing edge to an adversary of raw capacity $10^{-3}$ and no other outgoing
edge. Row normalization makes its transition probability one. Let the adversary
self-loop. Its stationary mass is $.85$, not the $.00564$ obtained by incorrectly
substituting $10^{-3}$ for $\epsilon$. A max-flow gate may usefully constrain
admissibility, but it does not establish the row premise. The implemented
normalization must enforce it, for example by reserving the unused probability
locally instead of redistributing it across the surviving external edges.

This still leaves another boundary: a downstream assignment transformation can
destroy a graph bound. The game-theoretic companion gives examples in which many
low-mass accounts receive large aggregate assignment probability or a capacity
budget is reused independently for every candidate. The final constraint must
apply to the final joint allocation over accountable control groups.

## 3. Emergent concentration from local feedback

Consider $K$ fixed, equally sized eligible groups with opportunity shares
$x_k\geq0$, $\sum_k x_k=1$. This could coarse-grain laboratories or review
communities; it is not a license to regard freely created accounts as groups.
Let $d_k$ be a fixed external evidence signal and define

$$a_k(x)=(1-\zeta)
 \frac{\exp[\beta(\chi x_k+(1-\chi)d_k)]}
 {\sum_j\exp[\beta(\chi x_j+(1-\chi)d_j)]}+\frac{\zeta}{K},
 \qquad \dot x_k=a_k(x)-x_k. \tag{2}$$

$\zeta$ is reserved exploration, $\chi$ the fraction of routing signal that
recycles current opportunity, and $\beta$ sensitivity to that signal. Time is in
units of opportunity-memory relaxation, so every parameter in (2) is
dimensionless. This is a simplification of the earlier candidate mean-field model,
chosen to make its assumptions and failure mechanism identifiable.

The simplex is forward invariant: derivatives sum to zero and at a boundary
$\dot x_k=a_k\geq0$. When all $d_k$ agree, $x_k=1/K$ is a fixed point. Softmax
has Jacobian $(1/K)I-(1/K^2)\mathbf1\mathbf1^\top$ there. On the tangent space
$\sum_k\delta x_k=0$, every linear eigenvalue is

$$\boxed{\lambda=\frac{(1-\zeta)\beta\chi}{K}-1}. \tag{3}$$

Thus the symmetric fixed point is locally asymptotically stable when
$(1-\zeta)\beta\chi<K$ and unstable when the inequality reverses. Equality is
nonhyperbolic and the linear calculation makes no stability claim. This local
threshold does not locate every attractor or rule out bistability. Its numerical
value depends on how shares and sensitivity are normalized; changing the number
or definition of groups changes the model.

For two groups, $\beta=4$, $\chi=1$, and $\zeta=.1$, a small initial asymmetry
$(.501,.499)$ tends to approximately $(.91972,.08028)$ in the numerical integration.
At $\beta=1$ it decays. At $\chi=0$, routing depends only on fixed evidence and
$\dot x=a-x$ has a unique globally attracting allocation even for large $\beta$.
The relevant intervention is therefore not just increasing exploration: reduce
the reuse of assignment opportunity as evidence of competence. The sweep also
uses concentrated initial conditions and records residuals; finite-time endpoints
must not all be called equilibria. Its maximum residual is about $8.45\times10^{-5}$,
and the step-size comparison covers one well-separated parameter case only.

This is an analytical toy counterexample to the belief that benign local actions
guarantee fair aggregate behavior. It is not an empirical model of prestige and
not a novelty claim for reinforcement or softmax bifurcations. A pilot must estimate
whether the feedback channel exists before fitting its parameters. Delayed,
censored defect confirmations may provide less exogenous evidence than the model
assumes.

## 4. More agents need not mean more independent evidence

If $n$ scalar review errors each have variance $\sigma^2$ and equal pairwise
correlation $\rho\in[0,1]$, then

$$\operatorname{Var}(\bar e)=\frac{\sigma^2}{n}[1+(n-1)\rho],
 \qquad n_{\mathrm{eff}}=\frac{n}{1+(n-1)\rho}. \tag{4}$$

This follows by summing the $n$ variance and $n(n-1)$ covariance terms and matching
the result to $\sigma^2/n_{\mathrm{eff}}$. At $n=20$, $\rho=.2$, the variance-equivalent
sample size is $4.17$; as $n\to\infty$ it approaches $1/\rho=5$. Shared systematic
bias is not removed by this calculation and can dominate variance. For unequal
errors, use the declared covariance model and $w^\top\Sigma w$, not a reviewer
count. Nothing here estimates an actual LLM correlation or probability of truth.

The protocol implication is practical: pay for different checks, evidence sources,
control groups, and approaches before paying for additional copies of the same
check. Human and agent resources are complementary dimensions, not interchangeable
tokens. Control independence is an inspectable structural condition; statistical
independence is a stronger hypothesis requiring data.

## 5. The repair process can become supercritical

An amendment can open reconsideration of dependent claims. In a branching-process
idealization, each ticket reaches a mean $b$ new dependents; a fraction $q$ needs
work; a fraction $c$ of candidate tickets is coalesced before becoming new work.
Define q as the candidate-edge-weighted probability that scientific work is required, and c as the conditional fraction of that required work genuinely discharged through reuse. Then

$$R=bq(1-c).$$

These must be conditional count ratios, not products of separately parent-averaged fractions. With correlated degree, severity and reuse, estimate mean offspring directly by type; naive products of averages can reverse the regime classification.

If offspring counts have this mean, expected total tickets, including the initiating
ticket, are

$$E[N]=\sum_{j\geq0}R^j=\frac{1}{1-R}\quad(R<1). \tag{5}$$

For $R\geq1$ this unbounded-tree expectation diverges. Actual finite dependency
graphs saturate and contain overlapping paths, so this is an early-warning model,
not a prediction of literally infinite requests. Coalescing must preserve affected
claim identifiers and safety work; it may batch notifications or reuse a common
calibration check, but cannot quietly dismiss distinct material dependencies.

For root amendments arriving at rate $\nu$ and mean reviewer cost $h$ per ticket,
the idealized steady workload is $\nu h/(1-R)$ reviewer-hours per time unit. With
repair capacity $H$, stability needs $\nu h/(1-R)<H$ in addition to $R<1$.
This yields a coupled operating boundary: sufficiently many scientifically useful
dependencies can overwhelm repair even when every individual check is cheap.
The multitype companion, *A small protocol with a finite correction cone*, supplies
a stronger warning: a mean row sum of $.71$ can coexist with a spectral radius
above $1.2$, and total spare labor can hide a failing specialty. Scalar $R$ is
therefore not an operational admission rule. Notification coalescing and reduction
of distinct scientific work require separate accounting; only the latter belongs
in $c$ when equation (5) is interpreted as reviewer workload.

The first pilot should therefore expose pending/stale reliance, merge duplicate
work, prioritize material consequences, and never silently promise instantaneous
global revalidation.

## 6. Backward compatibility without inherited authority

Authors should start with a DOI or arXiv version, a repository commit, a normal
review letter, and one claim-specific scope statement. Adapters can attach MCRP
metadata; missing fields remain unknown. Legacy review text should not be parsed
into synthetic approvals a reviewer never gave.

W3C PROV provides established provenance concepts [2]; COAR Notify defines
notification patterns for requests, acknowledgments, and results [3]. Our mapping
is an interface proposal, not a tested claim of conformance. A COAR review
announcement may identify an available check; it does not establish that MCRP's
identity, authority, evidence, and exact-release requirements were satisfied.
Compatibility testing must preserve version identity, typed decisions, unknown
fields, correction links, and access boundaries in a round trip.

For large collaborations, a module boundary can expose a witnessed execution or
downselected artifact. The check states what is inspectable and what remains
trusted. There is no requirement that an individual reproduce an entire detector
or compute cluster to contribute a useful local check. Conversely, a laptop check
of a rendered figure does not inherit a collaboration's calibration assurance.

## 7. Evaluation that could reject the proposal

Use identical synthetic claim tasks in three interface conditions: ordinary
review letter; structured claim/evidence template; four-action interface. Hold
reviewer pools, evidence, and time budgets constant. Only then vary optional trust
routing. This separates value from record structure, routing, and new interface
complexity. The old A0–A4 routing comparison remains a later experiment rather
than a claimed result of our small sweeps.

Plant missing dependencies, stale versions, correlated wrong evidence, hidden
common control, valid minority objections, and a correct low-resource check.
Record defects found, false findings, scope comprehension, correction latency,
reviewer-hours, newcomer delay, and dropout by participant type. Disagreement
with the author is not a defect label. Include independent adjudication of planted
fixtures and retain unresolved cases rather than forcing consensus.

Measure the interaction overhead separately from verification: field count,
time to first useful check, requests for clarification, and mistaken upgrades of
integrity into scientific endorsement. A protocol that reduces one cost by moving
unmeasured effort to stewards has not demonstrated efficiency.

The pilot cannot proceed from these synthetic calculations alone. Its ethics,
privacy, jurisdiction, recruitment, and human-release decisions remain open.
Before recruitment, preregister task selection, subgroup denominators, exclusions,
and adverse-event thresholds. Reject additional trust machinery if a structured
template matches its scientific utility at lower cost. Reject the four-action UI
if reviewers cannot reliably distinguish what a check actually authorizes.

## Contribution and claim ledger

| ID | Type | Claim | Evidence and boundary |
|---|---|---|---|
| S1 | D | Four actions expose the intended boundary | Design; usability untested |
| S2 | T | Equation (1) bounds imported stationary mass | Proof above; row premise required |
| S3 | T/I | Small raw capacity does not imply small normalized influence | Two-state counterexample and executable test |
| S4 | T | Equation (3) is the symmetric local stability threshold | Jacobian derivation; fixed equal groups only |
| S5 | I | Stated numerical trajectories and table values | `results/manifest.json`, code and tests; synthetic |
| S6 | T | Equation (4) is variance-equivalent independent count | Covariance identity; no actual correlation estimate |
| S7 | T | Equation (5) is expected branching workload | Geometric series; unbounded-tree model |
| S8 | H | Scoped status incentives improve review behavior | Requires consented comparative pilot |
| S9 | H | Interface and adapters improve adoption | No adoption or interoperability evidence |

## Closest work and limitations

| Prior work | Established contribution | Relationship here |
|---|---|---|
| Kawakatsu et al. [1] | Generative endorsement dynamics and hierarchy transitions | Closest dynamics precedent; our scalar/group simplification is illustrative |
| Personalized restart walks and capacity-based trust | Observer-relative routing and bounded trust mechanisms | Existing TDRG prior art; (1) is a model lemma, not a new reputation algorithm |
| W3C PROV [2] | Interchangeable provenance representation | MCRP must reuse vocabulary rather than invent provenance |
| COAR Notify [3] | Repository/service notifications | Transport mapping does not grant epistemic authority |

The models omit learning curves, evolving identities, strategic budgets, real
error dependence, variable review quality, and legal coercion. The specialist
companions address incentives and operational constraints but do not calibrate
these omissions away. We have not shown a successful A4 policy, anonymity,
cryptographic implementation, external interoperability, or scientific accuracy.
The defensible contribution is a smaller proposed interface plus explicit failure
boundaries and a reproducible research agenda.

## References and source checks

1. M. Kawakatsu, P. S. Chodrow, N. Eikmeier, D. B. Larremore,
   *Emergence of Hierarchy in Networked Endorsement Dynamics*, PNAS 118(16),
   2021. DOI: [10.1073/pnas.2015188118](https://doi.org/10.1073/pnas.2015188118).
   [Author preprint](https://arxiv.org/abs/2007.04448), title, authors, journal
   identity and abstract checked 2026-09-25. We cite its stated scope, not a
   claimed replication of its results.
2. W3C, [PROV Overview](https://www.w3.org/TR/prov-overview/), Working Group
   Note, 30 April 2013. Overview and recommendation/document distinction checked
   2026-09-25.
3. COAR, [Notify Protocol 1.0.1](https://coar-notify.net/specification/1.0.1/).
   Required payload properties and pattern list checked 2026-09-25.
