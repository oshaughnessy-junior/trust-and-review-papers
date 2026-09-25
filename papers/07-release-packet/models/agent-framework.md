# Executable boundary model: states, scarce work, and repair

**Research question:** Can four participant actions expose composition failures
without a universal reputation score or a large mandatory rule table?

**Bounded answer:** A small deterministic model can reject several precisely
specified mismatches and exhibit counterexamples to broader promises. It cannot
establish human usability, scientific truth, actual independence or live authority.

## Contribution and claim ledger

| Label | Claim | Evidence / limit |
|---|---|---|
| D | Offer/check/rely/amend forms a small participant API | `toy_agents/protocol.py`; proposed semantics, not adopted standard |
| T | Joint reservation enforces specified person and skill capacity | Finite-sum argument below; assumes complete correct capacity keys |
| I | Atomic panels, version mismatches, scope gaps, unknown checks, unauthorized decisions and stale renewal are handled | `toy_agents/tests/test_protocol.py`; trusted-process synthetic cases |
| T | Canonical group-first sampling is invariant to redundant labels within a group | Elementary pushforward proof below; static eligibility only |
| I | Hidden dependencies escape amendment propagation | Deliberate negative control `hidden_dependency()` |
| H | Four actions lower total human labor or improve defect detection | Unestablished; compare structured-template baseline in a human pilot |

The API is a synthesis and executable illustration of the preceding dossier,
not a claim that versioned records, graph reachability, resource reservations,
randomized panels or state machines are newly invented. Closest technical basis
is the prior bounded-reliance work summarized in the
[self-contained background](../publication/background.md).
No external interoperability, external peer review or empirical evaluation is claimed.

## Target and authority composition

Define exact target $t=(c,v,e)$ with claim ID, version and evidence identifier.
The simulator treats $e$ as an opaque fixture identifier; a cryptographic binding
would require a separately authenticated content layer. An offer gives scope
$S_o$ and declared prerequisite targets $D(t)$. A check $j$ gives scope $S_j$,
reviewer $a_j$, method, limitations, outcome and dependency-generation snapshot.

For requested scope $S_r$, selected supporting checks $J$, and minimum independent
groups $k$, the implemented coverage condition is

$$\forall s\in S_r,\quad \left|\{g(a_j):j\in J,\ s\in S_j\}\right|\ge k.$$

This is stronger than counting distinct groups across the entire panel: one group
checking calibration and another checking statistics do not provide two checks of
either. All selected checks must refer to the same offer, support the claimed scope,
and match the current declared dependency snapshot. Current overlapping contradictory
checks also block a new reliance even if omitted from $J$. This is a conservative
model choice, not a replacement for reasoned disagreement or domain adjudication.

Typed authority is a predicate $A(a,\kappa)$ for decision kind $\kappa$. The trusted
fixture registry may give scientific or publication authority separately. The
engine never infers $A$ from a support check, team size or a favorable numerical
result. It does not validate whether any real institution granted the authority.

## Reservation invariant and exact units

Let $x_{ps\ell}\in\mathbb N_0$ be effort reserved or spent by accountable capacity
key $p$, skill $s$ and task $\ell$. A valid schedule satisfies

$$\sum_{s,\ell} x_{ps\ell}\le C_p,\qquad
  \sum_\ell x_{ps\ell}\le C_{ps}.$$

For a candidate batch $b$, the ledger adds its nonnegative integer entries to the
full committed ledger, validates both inequalities, and commits the entire batch
only if every inequality holds. Therefore, by induction from the empty ledger,
every accepted sequence satisfies both bounds. A rejected batch changes nothing.
Consumption preserves its allocation; cancellation removes only unspent work.
This is a finite accounting invariant, not proof of deadlines, productivity or
honest reservations. Independent tests compare randomized batch acceptance against
a separate schedule-summing oracle, including shared skills and partially fitting
batches. A single person represented by two unknown keys breaks the premise.

`check_panel` uses a detached serial state to expose all-or-none behavior. It is
not scalable storage and supplies no concurrency, crash-recovery or distributed
atomicity guarantee. Units are synthetic effort tokens per scope skill. A real
application must price setup, supervision, audit, triage, appeals and repair in
measured compatible units and preserve commitments across epochs.

## Canonical panels and the label-multiplicity trap

Let $G$ be the static qualified, nonconflicted group set. Sample uniformly from
its $k$-subsets, then choose an eligible representative inside each chosen group.
For group panel $H$, the marginal probability is

$$P(H)=\binom{|G|}{k}^{-1}.$$

Splitting a representative into redundant labels inside a fixed group changes
only $P(\text{representatives}\mid H)$, whose sum remains one. Thus the pushforward
onto group panels is unchanged. This is conditional on correct fixed group labels
and unchanged eligibility, not Sybil resistance or a dynamic completion theorem.
The executable sampler enumerates subsets, so its cost grows combinatorially;
small toy pools only. No efficient general constrained sampler is claimed.

Negative control: for groups A, B, C and two seats, give A $m$ representatives,
B and C one each. Uniform sampling of feasible representative pairs has $2m+1$
panels; A occupies $2m$. Its probability is $2m/(2m+1)$ despite a strict one-seat
per-group rule. Group-first sampling instead gives $2/3$. The checked-in run
uses $m=100$ and 3,000 draws; exact formulas are the claim, frequencies illustrations.

Completion is a different conditioning event. If risky invitations have fraction
$q$ and complete with probability $c_R$, versus $c_S$ for others, then

$$P(R\mid\text{complete})=\frac{qc_R}{qc_R+(1-q)c_S}.$$

The demo uses $q=.1,c_R=1,c_S=.01$, giving $100/109\approx.9174$. It records all
stage denominators and charged intake. No offered-panel probability bound is
carried across capacity filtering, retries or selective completion.

## Amendments and bounded currentness

Each offered target has generation $g(t)$. A reliance stores generations of its
transitive declared prerequisite closure, including itself. Material amendment
increments the changed target generation. A downstream reliance is pending iff
its snapshot differs from the current closure snapshot. A new checked and
authorized reliance can capture the new snapshot without modifying the old one.
Offer ordering requires prerequisites already exist, so the toy dependency graph
is a finite DAG; graph-cycle negotiation and undeclared future dependencies are
outside its scope.

The currentness view also checks expiry, evidence availability and a stated
maximum observation age. This is not a statement about scientific correctness.
An undisclosed dependency is absent from the closure, so its amendment cannot
change that snapshot. The negative fixture intentionally produces
`current_under_toy_policy` when an omniscient observer knows the claim needs
reconsideration. The failure is retained in release evidence.

## Evaluation and stopping rule

Run the documented tests and deterministic scenario command before packaging.
Do not suppress a failing negative control to improve the number of green tests.
Stop any general claim at its first violated premise: missing group identity,
unknown capacity, incomplete evidence graph, absent authority or stale observation.
If a structured record plus ordinary review performs as well with lower total
human labor, retain that simpler interface. No human pilot, calibrated error model
or consequential external action occurred in these experiments.

AI assistance: this framework was drafted and checked by AI agents within the same
orchestration. The blue/red record identifies this as internal adversarial review;
human author approval and external review are separate release decisions.
