# Small contracts, measurable limits: mathematical foundations for the MCRP seed release

**Research prototype, 25 September 2026.** Conditional propositions and synthetic
experiments; not evidence of field efficacy. This manuscript advances the
counterexamples in dossier 06 into small executable modeling interfaces. The
results use elementary probability, constrained incentives and positive-system
bounds. The contribution is the alignment of those tools with protocol records,
not a claim to invent the underlying mathematics.

## Abstract

A protocol intended for a solo researcher, a large collaboration, a single agent
and a team of agents should not charge its participants for understanding the
internal complexity of everyone else. It should expose what can be checked at the
boundary: exact work, declared responsibility, available attention, performed
checks, and the conditions under which a reliance decision needs renewal. Four
models identify what this interface can and cannot guarantee. Sampling accountable
groups before representatives removes one representation-multiplicity incentive
under known control. Selective completion can nevertheless reverse offered-panel
bounds, while retries spend scarce attention without repairing the selection
bias. A common weighted repair envelope controls expected cascades under changing
regimes, but neither stable snapshots nor a small expected workload certify a
safe queue. Finally, an audit must fit effort incentives, participation and its
own funding constraint simultaneously. The package contains exact calculations,
independent finite enumerations, reproducible stochastic checks and deliberate
negative cases. Every positive result is paired with a premise whose failure is
observable in a toy experiment or requires a real-world investigation.

## 1. The interface as a modeling boundary

The participant-facing actions remain **offer → check → rely → amend**. They are
composable actions, not an exclusive sequence of statuses. The mathematics adds
no fifth user action. It specifies what a scheduler or experiment must record
behind those actions.

An **offer** fixes a version, bounded claim, requested check and responsible
boundary. A **check** records performed work and its limits; it is not a vote that
converts into general truth. **Rely** is a separate actor's decision for a stated
use, with observed evidence and renewal conditions. **Amend** identifies a material
change and affected uses. A large team may automate hundreds of internal checks;
that does not create hundreds of independently controlled reviewers.

The minimum experiment state therefore includes an immutable target identifier;
declared control groups and qualifications; a panel-generation policy; invitation,
refusal, completion and reliance events; actual resource debits; and a declared
dependency graph. These are inputs and records, not facts made true by a schema.
In particular, the mathematics below does not authenticate identity, discover
undeclared dependencies or grant scientific authority to a software process.

## 2. Representation invariance belongs to a distribution

Let $G$ be a fixed finite set of eligible accountable groups. Group $g$ has $m_g$
interchangeable representatives. Eligibility, capacity and conflict conditions
have already been resolved at group level. Let $\mathcal F$ be a nonempty set of
feasible $k$-group panels. We compare two policies.

**Representative-first policy.** Enumerate every feasible representative panel
with at most one member from each group, then choose uniformly. Its induced
probability of a group panel $S\in\mathcal F$ is

$$Q_m(S)=\frac{\prod_{g\in S}m_g}{\sum_{T\in\mathcal F}\prod_{h\in T}m_h}.$$

It satisfies the one-seat-per-group rule while still rewarding label multiplicity.
With $G=\{A,B,C\}$, $k=2$ and $m=(n,1,1)$,

$$\Pr(A\text{ receives a seat})=\frac{2n}{2n+1}.$$

One hundred representatives move the probability from $2/3$ to $200/201$ without
adding a group or changing the claim's scientific needs.

**Group-first policy.** Fix a distribution $Q$ on $\mathcal F$ using only
clone-invariant group attributes. Draw $S\sim Q$. Conditional on $S$, choose one
representative per group by any normalized kernel $K_m(\cdot\mid S)$ supported on
that group panel.

**Proposition 1 (pushforward invariance).** If only representative multiplicities
change, while $G$, $\mathcal F$ and $Q$ remain fixed, the distribution of selected
group panels remains $Q$.

*Proof.* For any $S$, the probability of all representative realizations mapping
to $S$ is $Q(S)\sum_xK_m(x\mid S)=Q(S)$. No summand from another group panel maps
to $S$. Consequently every statistic depending only on the group panel is
invariant. $\square$

This is a statement about an entire pushforward distribution, not a claim that a
cap on individual graph scores suffices. The executable baseline takes all
$k$-subsets and uniform $Q$; it does not solve general conflict-aware scheduling.
A production implementation must construct feasible panels using actual skill,
conflict, independence and capacity constraints **before** drawing, and define
what happens when the feasible set is empty. It must not silently relax coverage.

**Falsifier.** Declare two secretly controlled accounts as different groups. With
$G'=\{A_1,A_2,B,C\}$ and uniform pairs, the true controller behind $A_1,A_2$ now
receives at least one seat with probability $5/6$, and both seats with probability
$1/6$. Group-first sampling has not solved Sybil resistance. Douceur's original
analysis establishes why multiple identities undermine redundancy and why
identity certification is a substantive assumption; our toy group map supplies
that assumption rather than implementing it. [The Sybil Attack](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/)

**Meaning for participants.** An individual and a collaboration may expose the
same accountable boundary. Splitting a team into more named software processes
must not automatically buy the team more external allocation probability. Real
new expertise or independently controlled capacity may legitimately change the
feasible set; that is not the cloning transformation in Proposition 1.

## 3. Completion is a second selection mechanism

Label a panel $R$ if it belongs to a synthetic risk category. This is a model
label, not a diagnosis of any real group. Let $p=\Pr(R)$ among offers, let $a$ be
its completion probability, and let $b$ be the other category's completion
probability. Then

$$s=pa+(1-p)b,\qquad
\Pr(R\mid\mathrm{complete})=\frac{pa}{s},\quad s>0.$$

A $10\%$ offered share becomes $91.743\%$ of completed panels when $a=1$ and
$b=.01$. An offered-panel cap is therefore not a completed-panel cap.

**Proposition 2 (completion envelope).** If $p\le\epsilon<1$, $a\le u$, and
$b\ge\ell>0$, then

$$\Pr(R\mid\mathrm{complete})\le
\frac{\epsilon u}{\epsilon u+(1-\epsilon)\ell}.$$

*Proof.* The conditional fraction increases with $p$ and $a$ and decreases with
$b$ whenever its denominator is positive. Substitute the respective extrema.
The case $u=0$ has zero risky completions. $\square$

The missing premise is often the important one: humans cannot be compelled to
supply $\ell>0$ completion. Refusals may be the appropriate response to conflicts,
insufficient time, confidential material or inadequate expertise. Treating them
as misconduct would change the protocol's purpose.

### Finite retries cost attention but do not remove IID selection bias

Suppose each new attempt independently draws from the same offer distribution,
with unchanged completion probabilities. Stop at the first completion or after
$L$ attempts. Write $N_L$ for attempts actually made. For $s>0$,

$$E[N_L]=\sum_{j=0}^{L-1}(1-s)^j
=\frac{1-(1-s)^L}{s},\qquad
\Pr(\mathrm{unresolved})=(1-s)^L.$$

The probability of risky completion is
$pa\sum_{j=0}^{L-1}(1-s)^j$. Dividing by total completion probability cancels the
same sum: the risky share among completions remains $pa/s$ for every $L$.
For $s=0$, every request uses $L$ attempts and stays unresolved.

Let $c_i$ be invitation/triage cost per attempt and $c_c$ be work cost charged on
completion. Then

$$E[C_L]=c_iE[N_L]+c_c\{1-(1-s)^L\}.$$

Expected refusals equal $E[N_L]-\Pr(\mathrm{complete})$; expected retries equal
$E[N_L]-1$. These are different quantities. Standby reservations, partial work,
late cancellations and case intake require additional debits in a real ledger.
The toy costs are chosen constants, not estimated labor.

For $p=.1,a=1,b=.01,c_i=.2,c_c=2$, one attempt costs $.418$ model units on average,
with $89.1\%$ unresolved. Ten attempts cost about $2.626$, and fifty about $3.823$.
The completed-panel risk share remains $91.743\%$. The growth in completed work is
real in this model, but presenting only the completion count conceals the resource
cost and composition.

The seeded demonstration runs 20,000 requests per case, 80,000 in total. For the
ten-attempt case, 13,810 complete, the observed risky share is $91.665\%$, and its
pointwise nominal 95% Wilson interval is approximately $[91.193\%,92.115\%]$.
This interval describes Monte Carlo variation under the supplied Bernoulli model.
It says nothing about uncertainty in real refusal behavior. Adaptive rerolls,
learning completion rates, collusion and repeated contacts violate the IID model;
they need a new model, not reuse of these error bars.

### The denominator is part of the result

Publish eligible, invited, accepted, completed and relied-upon counts separately,
plus offered requests, excluded requests, refusal attempts, retries, outstanding
work and resource costs. The toy retry model collapses acceptance and completion
into one Bernoulli event; the protocol simulator should keep the stages distinct.
The mathematical results are intentionally not a substitute for that event log.

Inverse probability weighting can diagnose observed selection when probabilities
are known and positive, but it does not produce missing scientific checks or
restore a physical panel guarantee. The classical unequal-probability estimator
is standard statistical machinery, not a novel trust mechanism.
[Horvitz and Thompson, 1952](https://www.stat.cmu.edu/~brian/905-2008/papers/Horvitz-Thompson-1952-jasa.pdf)

## 4. Repair must survive changing regimes

Let $Z_t$ be a nonnegative row vector of outstanding repair items by type in
generation $t$. Types can mean data calibration, statistical interpretation,
software execution or a rights-handling obligation. The branching abstraction
counts work items, not unique scientific truths. Duplicate notices and reusable
checks need deduplication before interpretation as labor.

Conditional on history $\mathcal H_t$, suppose

$$E[Z_{t+1}\mid\mathcal H_t]\le Z_tM_t,$$

componentwise, where $M_t$ belongs to a declared family $\mathcal M$ and can be
chosen based on history. This premise is stronger than estimating unconditional
average offspring in a convenient sample. Suppose there is a vector $w>0$ and
$r<1$ with

$$Mw\le rw\quad\text{for every }M\in\mathcal M.$$

**Proposition 3 (common weighted repair envelope).** For deterministic initial
$Z_0=z_0$, the expected cumulative weighted work satisfies

$$E\left[\sum_{t=0}^{\infty}Z_tw\right]
\le\frac{z_0w}{1-r}.$$

*Proof.* Multiplying the conditional bound by positive $w$ gives
$E[Z_{t+1}w\mid\mathcal H_t]\le rZ_tw$. Iterated expectation yields
$E[Z_tw]\le r^tz_0w$. Sum the finite geometric bound and apply monotone
convergence to nonnegative partial sums. Independence between generations and a
fixed switching sequence are unnecessary under the conditional premise. $\square$

If $w_i$ bounds immediate work hours per type-$i$ item, the right side also bounds
expected cumulative hours. If $w$ is only a mathematical witness, its units are
abstract weighted work and must not be relabeled as human hours. A failure to find
this witness does not prove instability: even a supplied $w=(1,1)$ can fail where
another positive $w$ succeeds. Common Lyapunov methods are established stability
tools; the author's accessible survey distinguishes stable subsystems from stable
switching. [Lin and Antsaklis, author manuscript](https://www3.nd.edu/~pantsakl/Archive/Publications_Through2009/366-TAC08.pdf)

### Counterexample: snapshots pass while switching explodes

Take

$$A=\begin{pmatrix}0&2\\0&0\end{pmatrix},\qquad
B=\begin{pmatrix}0&0\\2&0\end{pmatrix}.$$

Each matrix is nilpotent, so repeating either regime alone eventually clears all
work in this linear model. Alternating $A,B$ from $z_0=(1,0)$ doubles work every
generation and produces 1,024 items in generation 10. No common positive
$r<1$ envelope exists: $2w_2\le rw_1$ and $2w_1\le rw_2$ imply $4\le r^2$.
Thus checking each snapshot's spectral radius is insufficient even before
introducing stochastic human behavior.

For the positive example, use

$$M_1=\begin{pmatrix}.2&.1\\.1&.4\end{pmatrix},\quad
M_2=\begin{pmatrix}.1&.3\\.05&.2\end{pmatrix},\quad w=(1,2)^T.$$

Both satisfy $M_jw\le .7w$. Starting with one first-type item gives an expected
cumulative weighted bound $1/(1-.7)=10/3$. Exhaustive enumeration of every
length-eight switching sequence checks the finite inequalities; a longer
alternating trajectory is included in the CSV output. These tests supplement the
proof; they do not estimate a real matrix family.

### Finite mean is not a service guarantee

A branching item that produces 50 descendants with probability $.01$ and none
otherwise has mean offspring $.5$. It is subcritical in first moment, yet its
first generation alone exceeds an eight-item capacity with probability $.01$.
For nonnegative total work $W$, the preceding expectation bound gives at most the
conservative Markov bound $\Pr(W\ge H)\le E[W]/H$, capped at one. It does not
establish deadline compliance or acceptable tails.

The capacity interface instead records commitments by **person and epoch across
all lanes**. Three hours of checking, two of audit and four of repair consume nine
hours of the same person's eight-hour day. Three separately feasible lane budgets
do not make the joint plan feasible. Skills, simultaneous appointments, legal
priority, independence and deadlines impose additional constraints. Our checker
only verifies the shared declared hour totals. Unrecorded obligations remain a
failure mode; expected future repair bounds cannot be booked as realized work.

## 5. Incentives must fit the audit and participation budget

Consider a one-shot invitation. Honest work yields reward $R$, costs $c$ and is
incorrectly sanctioned on an audit with probability $\alpha$. Shirking saves $c$
and is detected on an audit with probability $\beta$. Audit probability is $q$;
the modeled enforceable loss is $F\ge0$. Abstaining yields outside utility $u$.
Utilities are

$$U_H=R-c-q\alpha F,\qquad U_S=R-q\beta F,\qquad U_A=u.$$

For $\beta>\alpha$, $F>0$, $\alpha F>0$, honest work is a weak best response and
all $N$ invitations can reserve audit cost $a$ within budget $B$ only if

$$\frac{c}{(\beta-\alpha)F}\le q\le
\min\left\{1,\frac{B}{Na},\frac{R-c-u}{\alpha F}\right\}.$$

**Proposition 4 (one-shot feasibility).** Under the stated assumptions, this
interval is necessary and sufficient for honest work to weakly dominate both
shirking and abstention while satisfying the worst-case invited audit reservation.

*Proof.* Rearrange $U_H\ge U_S$, $U_H\ge U_A$, $Naq\le B$ and $0\le q\le1$.
All constraints are affine in $q$. Their intersection is exactly the interval.
The code handles zero audit cost, zero effort cost and zero discrimination without
dividing by zero. Negative discrimination with zero effort permits only $q=0$.
$\square$

With $c=.2,R=1,F=2,\alpha=.02,\beta=.8,u=.1,N=100,a=.1,B=2$, the interval is
approximately $[.1282,.2]$. Reducing $B$ to 1 makes it empty. Keeping ample funding
but lowering reward to $.3$ and increasing false sanctions to $.3$ can also make
it empty: $q\ge.2$ is needed for effort while $q\le.0833$ is needed to keep honest
participation worthwhile. Increasing policing without controlling false positives
can exclude contributors.

The sweep uses 102 artificial agents with two reward levels and 51 effort costs.
Each chooses the best of honest, shirk and abstain. Ties prefer abstain, then
honest, then shirk. It reports both honest share **among participants** and counts
among **all invitations**, along with realized expected audit work and full
reservation cost. The sweep is a mechanism diagnostic: its utilities are neither
survey responses nor a fit to scientists, lawyers or software agents.

This is deliberately not a whole-network equilibrium. Audit credibility,
collusion, appeal reversal, reviewer judgment, wealth constraints, repeated
identity resets and the legitimacy of imposing $F$ are outside the model. The
simpler prototype may rely on bounded recognition and loss of future assignments,
not monetary penalties. Such a loss still needs a justified valuation and a
responsible institution; a symbolic variable cannot supply either.

## 6. Four deep adaptations, one common experiment boundary

**Physics and astronomy.** Treat calibration and inference as separate repair
types. A new instrument calibration can invalidate a derived estimate without
invalidating the raw observations. A collaboration's 100 analysis processes remain
one control boundary for panel sampling. Ask whether repair notices reach the
actual downstream uses and whether the limited calibration specialists are
double-booked. The switched-matrix counterexample represents changing dependency
patterns, not a fitted astrophysical pipeline.

**Biology.** A data-use restriction can remove evidence without proving a biological
claim false. Give evidence availability, statistical checks and authorized reuse
separate records. Let wet-lab replication complete more slowly than a computational
check; the completion model demonstrates why counting only finished work can
favor an easy-to-complete category. A wet-lab refusal is not a negative scientific
verdict. Consent and restricted data do not enter a public toy fixture.

**Economics and social science.** Use offered/completed denominators to teach how
selection can create apparent institutional improvement. Vary completion rates,
setup costs and outside options; report unresolved projects and labor as outcomes.
The audit experiment shows a mechanism whose apparent integrity among remaining
participants improves while scarce contributors can leave. A substantive causal
claim requires a real identification strategy and external data, not this queue.

**Law and governance.** Treat rights response, scientific disagreement and appeal
as different authorities drawing on some of the same people's time. The capacity
checker can reject nine hours booked into eight without deciding legal priority.
The audit model's sanction must not be read as a legally enforceable fine. A timely
record, lawful recipient-specific disclosure and authorized reversal require
operator processes outside these mathematical models.

## 7. Claim ledger and reproducibility

| ID | Status | Claim and evidence | Limitation |
|---|---|---|---|
| M1 | T | Group-first pushforward invariance; proof and exact probability tests | Fixed true/declared group map, feasibility and weights |
| M2 | T | Completion conditioning and finite IID retry accounting; proof and independent path enumeration | Adaptive contact/refusal behavior omitted |
| M3 | T | Common positive envelope bounds conditional expected cumulative repair; proof | Envelope validity is an empirical/operational assumption |
| M4 | T | One-shot audit/participation/funding interval; affine inequalities | Audit and enforceable loss exogenous, no equilibrium selection |
| M5 | I | Executable synthetic implementation reproduces positive and negative cases | Floating-point toy range, no production scheduler |
| M6 | E | 80,000 seeded simulated requests with pointwise uncertainty | Simulation outcomes only, no human evidence |
| M7 | P | Keep simple participant actions while instrumenting full denominators and shared budgets | Usability and effectiveness untested |

Here T denotes a conditional theoretical result, I implementation evidence, E an
explicitly synthetic experiment and P a proposal. These labels do not confer
scientific acceptance. Seventeen unit tests include an independent representative
panel enumeration, an independent finite retry-path tree, all $2^8$ switching
sequences and utility comparisons on both sides of a feasible audit interval.
Three negative results are required demonstrations, not optional caveats: hidden
control, refusal-driven completion bias and unstable switching.

From the repository root:

```sh
python3 -m unittest discover -s papers/07-release-packet/models/math -p 'test_*.py' -v
python3 papers/07-release-packet/models/math/run_experiments.py
```

The second command writes 115 parameter-sweep rows in four CSV files and the
80,000-request Monte Carlo summary under `models/math/results/`. The manifest
records exact source/table SHA-256 digests, seeds, Python version and interval
interpretation. Standard-library Python is sufficient. No service, credential,
network access or actual author data are used. Input validation catches malformed
shapes, negative work and non-finite scalar inputs. The numerical routines are
small research references; they are not certified against overflow for every
finite IEEE-754 value or combinatorial explosion on large group populations.

The decisive next question is not whether these plots look plausible. It is
whether the full event trace preserves the stated boundary when one toy actor
refuses, splits its identity, hides a dependency or overloads a shared reviewer.
A human pilot should then compare the four-action interface with an ordinary
structured referee template under the same labor budget. If the template works
as well with less effort, retain the portable evidence records and simplify the
surrounding machinery.
