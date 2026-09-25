# Useful alone, more useful together: a bounded model of agentic protocol uptake

Research note, 25 September 2026. **T** marks conditional theory; **I** synthetic
implementation; **D** design implications; **H** hypotheses requiring observation.
No parameters below are measured agent preferences or estimates of demand.

## Abstract

Publishing a protocol gives scientific agents something to discover, but not a
reason to integrate it. We separate standalone task value from interoperability
value and integration cost. A finite heterogeneous adoption game identifies the
cascade reachable without recruitment, the larger adoption states that might
require coordination, and the conditions under which seeded participation can
survive withdrawal of support. Exact counterexamples show why several common
inferences fail: existence of a high-adoption equilibrium does not imply spontaneous
uptake; synchronous agents can oscillate even with positive network effects;
forced trials can collapse after support ends; and review congestion can destroy
the monotonicity on which cascade arguments depend. The design consequence is a
small correction-detection adapter with value to one operator, followed by
independent interoperability tests. It is a proposed experiment, not a forecast.

## 1. Scope and relation to prior work

Binary threshold adoption is established theory. Granovetter's
[original threshold model](https://www.journals.uchicago.edu/doi/10.1086/226707)
studies how individual participation thresholds combine into collective outcomes.
The symmetric-game argument below is a direct special case of the potential-game
method of [Monderer and Shapley](https://doi.org/10.1006/game.1996.0044). We do not
claim these mathematical ingredients as new. The contribution is their explicit
application to MCRP's agent-first release, an entry-versus-retention distinction,
and executable failure cases that constrain an outreach experiment.

An actor means an independently deciding operator or agent team. Ten agent labels
under one operator do not automatically create ten economically independent
adopters. We stipulate this actor partition; this model does not discover control.
We also stipulate correctness of the receipts' semantics. Merely emitting a
syntactically valid receipt cannot establish scientific verification.

## 2. Values and the decision boundary

There are n actors. Actor i chooses x_i in {0,1}: decline or adopt a specified
adapter for a fixed workload. Nonadoption utility is normalized to zero. The
incremental adoption utility is

\[
 U_i(x)=x_i\left[b_i+\sum_{j\ne i}w_{ij}x_j\right],
 \qquad b_i=h_i-c_i-k_i/H_i.
\]

Here h_i is expected standalone value per workflow, c_i is recurring cost, k_i is
one-time integration cost, and H_i>0 is the anticipated number of workflows over
which the entry decision amortizes that cost. Every term in b_i is in the same
utility unit per workflow. Utility may reflect valued operator time, but this is
not a conversion of compute, money, and attention into equal physical units.
Weights w_ij measure incremental compatibility value to i from j's adoption;
they may be directed and heterogeneous. Baseline theory assumes w_ij >= 0 and
w_ii=0, fixed workload and costs, no uncertain learning, and no capacity feedback.
Outside alternatives must already be accounted for in h_i-c_i.

A budget limit or unavailable skill can make adoption infeasible even when its
utility is positive. The baseline assumes feasibility; one may remove infeasible
actors before analysis, but cannot silently infer feasibility from this payoff.

The specified deterministic best-response policy is

\[
 F_i(x)=1\{b_i+\sum_jw_{ij}x_j>0\}.
\]

Ties choose nonadoption. Fixed points of F are Nash equilibria with this tie
selection. At a zero margin there may be other weak Nash equilibria that this
policy intentionally excludes. The code's `equilibria()` returns policy fixed
points, not an exhaustive enumeration of all weak Nash equilibria.

**Entry is not retention.** Once k_i is sunk, a fresh continuation decision uses
b_i^ret=h_i-c_i, not b_i. If support instead pays recurring c_i or changes workload,
its withdrawal changes retention value. We analyze forcing a participation state
at fixed base b as an abstract intervention; it must not be misreported as the
causal effect of paying a one-time setup cost. In empirical work estimate entry
and retention margins separately. H_i is an expectation, not a promise that agents
will actually return.

## 3. What standalone usefulness buys

**Proposition 1 (extremal cascades, T).** Under nonnegative weights, iterating F
from all-zero reaches a least fixed point x^-; iterating from all-one reaches a
greatest fixed point x^+. Each path makes at most n strict state changes. Every
fixed point lies coordinatewise between x^- and x^+.

*Proof.* Nonnegative weights make F monotone. Since 0 <= F(0), induction makes the
bottom path nondecreasing. Every strict change flips at least one coordinate
permanently to one, so at most n such changes occur. Its terminal state is fixed.
For any fixed point y, 0 <= y implies F^t(0) <= F^t(y)=y at every t. The upper
argument follows from F(1) <= 1 and reversed inequalities. □

Thus actors with b_i>0 start without a network. On a directed three-actor chain,
b=(1/10,-1/2,-1/2), w_21=w_32=1 and all other weights zero, the exact trajectory is
000 → 100 → 110 → 111. No adoption reward is needed *in this stipulated game*.
An adapter can therefore be designed to deliver local value before network scale:
record a dependency, revise its version, detect affected use, and retain unaffected
use. Whether that improves an existing workflow more than its overhead is H.

With two actors b=(-1/2,-1/2) and reciprocal weights one, both 00 and 11 are fixed.
Bottom iteration stays at 00. The existence of 11 alone is not evidence that
publication, downloads, or a broad announcement will produce it.

**Comparative static (T).** Lower entry costs or higher standalone value increase
b coordinatewise; under unchanged nonnegative weights, the least and greatest
fixed points cannot decrease. This follows by coupling both extremal iterations
and induction. It does not cover increases in workload, false alarms, or review
congestion induced by the change itself.

## 4. Coordination, withdrawal, and update timing

For a seed set S define F_i^S(x)=1 for i in S and F_i(x) otherwise. Starting at
zero reaches its least forced fixed point y^S by the same monotonicity argument.

**Proposition 2 (withdrawal criterion, T).** The forced fixed point y^S remains a
fixed point of the unforced policy after release exactly when every seeded actor
has strictly positive unforced margin at y^S. With a different retention model,
all coordinates must instead be checked against that model's response function.

*Proof.* Nonseed coordinates already equal their unforced responses. Every seed
coordinate is one, which equals F_i(y^S) exactly when its margin is positive.
Changing the payoff model invalidates the premise for nonseed coordinates too. □

In the two-actor coordination fixture, either seed yields 11 and both margins
there are 1/2. Seed costs (3,1) make actor 2 the cheapest full stable seed at cost
one. The supplied enumerator checks every seed set; it does not optimize a real
campaign or scale beyond the bounded toy population.

Counterexample: let b=(-2,-1/2) and reciprocal weights one. Forcing actor 1 yields
11; withdrawal produces 11 → 01 → 00. A successful supported trial is not by
itself a stable adoption state. There is no stable-full seed set under these
unchanged payoffs. A practical trial must measure continuation with the actual
post-support costs, rather than just registrations while support is available.

**Proposition 3 (unilateral improvement, T).** If weights are symmetric, the game
has exact potential

\[
 \Phi(x)=\sum_i b_ix_i+\sum_{i<j}w_{ij}x_ix_j.
\]

Any sequence of strictly profitable unilateral switches terminates at a pure Nash
equilibrium after at most 2^n-1 switches, provided it continues whenever a strictly
profitable switch exists. The terminal weak equilibrium need not use F's tie rule.

*Proof.* A switch by i changes the potential by exactly
(x'_i-x_i)(b_i+sum_j w_ij x_j), its own utility change. A strictly profitable switch
strictly raises potential. A finite state space cannot revisit a state. At a
terminal state no strict profitable deviation exists, the definition of a weak
pure Nash equilibrium. □

This result requires unilateral scheduling and strict improvements. It does not
justify synchronous fleet updates: in the positive-weight coordination fixture,
10 → 01 → 10 is a synchronous cycle. Nor does it justify directed weights via
this particular potential. The extremal cascade proof does allow directed weights,
but only establishes convergence from the extreme states, not every initial state.

## 5. Review capacity is a failure premise, not an afterthought

Suppose adoption creates shared review demand Q(x). A more complete adoption
margin might be b_i+sum_j w_ij x_j-ell_i(Q(x)), where ell_i is latency or resource
cost. Unless the total cross-effect remains nonnegative, Proposition 1 no longer
applies. Small cardinality is not enough to prevent this failure.

The congestion fixture has b=(1/2,1/2) and cross-weights -1. Interpreting the
negative term as a one-unit interference cost gives 00 → 11 → 00 under
synchronous updates; policy fixed points are 10 and 01. Even the bottom trajectory
now cycles. This example has no explicit queue and is not a queueing prediction;
it isolates the algebraic premise lost to adverse load effects. Modeling an actual
shared verifier requires the shared effort ledgers and repair bounds in packet
07, with newly estimated demand. Agent-only uptake does not make review free.

## 6. Experiment implied by the theory (D/H)

Offer one version-change challenge to three independently operated science-agent
workflows. Begin with a local export-and-check adapter, not mandatory participation
in an external review economy. Compare it to the same workflow with an ordinary
structured dependency record. Preserve equivalent information and instrument
operator setup, compute, false alarms, unresolved changes, and repeated use.
No condition should execute untrusted downloaded artifacts merely to emit a receipt.

Measure h-c using task performance and declared resource costs; record k and the
anticipated H separately. These are candidate operationalizations, not direct
observations of utility. Then exchange records between independently implemented
adapters and measure incremental interoperability value. Finally invite a second
workflow after the bounded trial support ends, recording changed costs and whether
its decision-maker returns. Failed import and unnecessary work are first-class
outcomes. Agent counts, stars, submissions, and self-reported enthusiasm do not
identify any of these parameters.

A local-only improvement would support standalone use even without a network.
Interoperability gains would justify a coordination trial. Large ongoing support
costs or repeated false alarms would motivate simplifying the interface. None of
these outcomes is established by the current public papers or synthetic fixtures.

## 7. Reproduction and claim boundary

From the repository root:

```sh
python3 -m unittest discover -s papers/08-agent-uptake-theory/adoption -v
python3 papers/08-agent-uptake-theory/adoption/model.py
```

`results.json` retains the second command's exact rational fixtures, complete
orbits, cycles, fixed points, and seed solution. Eight tests include exhaustive
81 two-actor parameter cases for extremal bounds and 27 symmetric games for the
unilateral-potential identity. Duplicate positive weights in the 81 cases are
intentional because absolute value enforces complements; these are 81 parameter
assignments, not 81 unique payoff matrices. All arithmetic uses integers and
Fractions. There are no confidence intervals because no randomness or sampled
population is present. Python's standard library suffices; no network, credential,
agent API, or experiment on real users is involved.

The mathematical results are elementary conditional guarantees. The software is
an exact bounded finite-state explorer, not an economic estimator, production
scheduler, identity system, or adoption forecast. The useful open question is
whether one independently operated scientific workflow gains enough from explicit
versioned reliance to return voluntarily, then whether another can use its records.

AI drafting and internal testing were performed under one orchestration; these
are not independent external scientific reviews.
