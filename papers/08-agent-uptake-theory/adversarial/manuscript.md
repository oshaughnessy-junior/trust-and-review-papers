# Agreement is a record, not an independent experiment

**MCRP theory extension; 25 September 2026. Research prototype.**

## Abstract

Agentic science makes reports cheap while leaving informative, independently
fallible observations expensive. A protocol can prevent declared aliases from
buying allocation weight without making different controllers epistemically
independent. We formalize three limits: a common blind spot produces an error
floor despite arbitrarily many checks; indistinguishable observable transcripts
cannot support discriminating certification; and selective release amplifies
false clearance across fresh attempts. An exact allocation example identifies
when method diversification helps and the independence premise it consumes.
The practical proposal is deliberately small: use the existing offer, check,
rely, amend interface, attach inspectable method and attempt records, and let a
reliance decision state which untested assumptions remain. This is a conditional
mathematical argument and synthetic demonstration, not measured science-agent
reliability or a production verifier.

## 1. Distinguish three boundaries

A **controller boundary** answers who may direct an actor. A **method family**
identifies potentially shared scientific failure causes: the same literature
corpus, learned model, calibration, simulator, specification, or computational
library. An **observation boundary** says what the relying party actually saw.
Two separately controlled agents can share every consequential scientific error.
One controller can conversely run an analytic derivation and a physical measurement
that expose different failure modes. Neither case turns a declared family label
into proof of independence.

The previous allocation theorem in `07-release-packet/manuscripts/math-foundations.md`
is valid under a fixed group map. It addresses representation weight, not the
joint distribution of check errors. The coupled toy model explicitly lacked
scientific correctness; this extension introduces a synthetic invalid-claim label
held by the evaluator, not a truth oracle available to ordinary participants.

## 2. A blind spot survives arbitrary agreement

All probabilities in this section are conditional on an **invalid claim drawn
from a specified target population**. Let $X_i=1$ mean check $i$ erroneously clears
it. Suppose a latent common blind spot $B$ occurs with probability $f$; conditional
on $B$, every check clears. Conditional on $B^c$, the checks independently clear
with probability $p$. The blind spot is drawn once per claim, not once per agent.

**Proposition A1 (common-cause floor).** For $k\ge1$,

$$q_k=P(X_1=\cdots=X_k=1)=f+(1-f)p^k.$$

For $0\le p<1$, $q_k\to f$. The marginal error is $e=f+(1-f)p$ and, when
$0<e<1$, the pairwise correlation is $f(1-p)/e$.

*Proof.* Condition on $B$. Also
$E[X_iX_j]-e^2=f(1-f)(1-p)^2$ and
$e(1-e)=e(1-f)(1-p)$; division gives the correlation. $\square$

With $f=.1,p=.2$, each check has marginal false clearance $.28$. Five checks
clear invalid work with probability $.100288$, rather than the independence
calculation $.28^5=.0017210368$. At 100 checks the true probability remains at
least $.1$, while $.28^{100}<10^{-50}$. The calculation identifies how misleading
a numeric confidence label could become; these are invented probabilities.

The floor is not an unavoidable property of all review. It follows from the
specific common-cause premise. A new physical observation capable of exposing
$B$ changes that premise and can lower the floor. Merely launching another
conversation from the same inputs may not.

**Proposition A2 (sharp bound without dependence information).** If each check's
marginal false-clear probability is at most $e$, then
$P(\bigcap_i\{X_i=1\})\le e$. No smaller uniform upper bound follows from these
marginals alone, however large $k$ becomes.

*Proof.* The intersection is a subset of each event. For sharpness let all
$X_i$ equal one Bernoulli variable with mean $e$. $\square$

This is a bound on a conditional error rate, **not** the posterior probability
that a cleared claim is invalid. The latter also requires a prevalence prior and
clearance behavior on valid claims. Neither is supplied by agreement counts.

## 3. What observable certification can distinguish

Let $P_G$ and $P_B$ be distributions of the complete transcript observable to the
relying actor in a valid and an invalid world. The transcript can contain reports,
hashes, signatures, challenge outcomes, and timing. Let $a(t)\in[0,1]$ be any
possibly randomized certification rule, and let
$\delta=\mathrm{TV}(P_G,P_B)$.

**Proposition A3 (observational limit).**

$$E_{P_B}[a]\ge E_{P_G}[a]-\delta.$$

Thus acceptance of valid work with probability at least $1-\epsilon$ entails
false acceptance at least $\max(0,1-\epsilon-\delta)$ for this pair of worlds.

*Proof for the finite fixture.* Write $d_t=P_G(t)-P_B(t)$. Since $0\le a_t\le1$,
$\sum_t a_td_t\le\sum_{d_t>0}d_t=\frac12\sum_t|d_t|=\delta$.
The same bounded-function property extends to general measurable transcripts.
$\square$

For identical transcripts, any rule that accepts all valid instances in the
pair also accepts all invalid instances. This does not prove that science is
impossible. It proves that an evidence-free change of labels cannot do the work
of a distinguishing observation. A secretly controlled account and an independent
account can be observationally identical if the system has no additional
identity evidence. Likewise, two honest independent controllers can reproduce a
shared software defect. Cryptographic integrity of the reported result alone
changes neither scientific premise.

The finite example uses $P_G=(.9,.1)$ and $P_B=(.8,.2)$, giving $\delta=.1$.
The rule accepting only the first transcript accepts valid work at $.9$ and
invalid work at $.8$, attaining the bound. This elementary application is not a
new statistical theorem; it makes the MCRP observation boundary explicit.

## 4. Buying different failure modes

Suppose method families have parameters $(f_j,p_j)$ and allocations $k_j$.
Assume their entire error processes are mutually independent conditional on
invalid work in the target population. If every check must clear, then

$$Q(k_1,\ldots,k_J)=\prod_j[f_j+(1-f_j)p_j^{k_j}],$$

with the factor for $k_j=0$ equal to one. This assumption is stronger than
separate controller ownership or different model names. Shared case difficulty
can violate it even when families have different training or implementations.

With two identical families $(.1,.2)$, a budget of six unit-cost checks has an
exact optimum at $(3,3)$: false clearance $.01149184$, compared with
$.1000576$ for $(6,0)$. The implementation exhausts all feasible integer
allocations. It does not claim that generic method diversity produces this gain.
There are no activation costs, correlated families, turnaround constraints, or
skill shortages in this example. A practitioner must measure or justify those
features before using the objective for routing.

A useful experiment therefore varies **which fault a check can expose**, not
just how many agents sign it. Physics/astronomy: inject an obsolete calibration
shared by every inference run, then add an observation or calibration check.
Biology: corrupt a sample annotation that every downstream model inherits, then
include an authorized check against the source annotation. Economics: give every
agent the same unidentified causal model, then test an identifying assumption or
independent design. Law: give agents the same outdated or inapplicable premise,
then check an authoritative source and jurisdictional scope. These are proposed
synthetic experiments, not evidence that any workflow is legally or scientifically
sufficient. They do not imply public release of sensitive underlying material.

## 5. Review shopping changes the unit of evaluation

A submitter can try fresh panels until one clears, exposing only that attempt.
For a fixed invalid claim, suppose each fresh attempt independently clears with
probability $q$. After $m$ attempts,

$$P(\text{at least one clearance})=1-(1-q)^m.$$

At $q=.1,m=50$, this is approximately $.994846$. The per-attempt performance has
not changed; the released sample has. If instead all panels inherit one common
blind spot, the IID formula fails. In the common-cause fixture with $k$ checks per
panel and fresh residual noise only, the probability is
$f+(1-f)[1-(1-p^k)^m]$ for $m\ge1$. Record the premise before using either formula.

Logs make shopping inspectable only within the observation domain. A service
cannot claim a complete attempt denominator when the submitter can run undisclosed
external checks. Externally committed challenges and preregistered evaluation
batches can define a useful bounded denominator; they do not prove that no other
attempt occurred. Refusal, crash, invalid input, and scientific failure should
remain distinct results rather than disappearing from the successful-run count.

## 6. Narrow protocol recommendation

Retain **offer → check → rely → amend**. This theory pass proposes metadata in an
experimental profile rather than a new normative schema:

- The offer names the target version, scope, and intended evaluation batch.
- A check names the actual method/artifact, known shared dependencies, and the
  observations exposed to the relying party. Family identity is explicitly declared
  or externally supported; it never silently means statistical independence.
- Reliance names the acceptance rule and untested premises. Where error behavior
  has not been calibrated, report it as uncalibrated rather than multiplying
  nominal reviewer error rates.
- Amendment invalidates the affected method or evidence dependency as well as the
  final conclusion, so shared defects can be revisited together.

The next agent challenge should compare repeated reports from one family against
checks aimed at different injected faults, under equal measured resource budgets.
Publish all in-scope attempts and predeclare which outcomes constitute detection.
Keep fault-generation seeds inaccessible to evaluated agents until evaluation
ends, and include untouched negative controls. This does not authenticate remote
agents or make a benchmark immune to leakage; it supplies a concrete empirical
question whose result could falsify the proposed benefit.

## 7. Reproduction and relation to prior work

From the repository root:

```sh
python3 -m unittest discover -s papers/08-agent-uptake-theory/adversarial -p 'test_*.py' -v
python3 papers/08-agent-uptake-theory/adversarial/correlated_checks.py
```

Nine tests independently enumerate latent states, selective-release paths, and
finite decision rules; test the sharp correlation counterexample and allocation
optimum; and reject malformed inputs. `results.json` is deterministic output.
All calculations are exact rational arithmetic internally. The experiment has
no network, service, credentials, participant data, or execution of scientific
code. The toy optimizer intentionally caps its combinatorial problem size.

Douceur's primary [Sybil analysis](https://www.microsoft.com/en-us/research/wp-content/uploads/2002/01/IPTPS2002.pdf)
shows why identity assumptions matter for redundant distributed participants.
Our separate point is that verified identity diversity still does not establish
scientific error independence. Brilliant, Knight and Leveson's
[N-version experiment](https://ntrs.nasa.gov/citations/19900041359) found correlated
failures among separately implemented programs and analyzed shared difficulty;
that result motivates, but does not estimate, our science-agent model. The
[total variation/testing relation](https://www.stat.cmu.edu/~arinaldo/36789/Oct29.pdf)
is standard; Proposition A3 is an elementary specialization with its proof given
here. Sources checked 25 September 2026. No source document is redistributed.

**Claim ledger:** A1–A3 are conditional mathematical statements; exact toy results
are implementation evidence under supplied parameters; the metadata profile and
fault-injection challenge are design proposals. No empirical adoption, calibration,
Sybil resistance, scientific certification, or governance efficacy is established.

AI drafting and internal testing were performed under one orchestration; these
are not independent external scientific reviews.
