# One queue, one ledger: coupled toy agents for protocol allocation and repair

**Research experiment, 25 September 2026.** All identities, utilities, scientific
labels and dependency graphs are artificial. This is an inspectable allocation
and accounting simulation. It is not a deployed review service or an empirical
behavioral model.

## Why join the models

A clone-invariant lottery can feed a clone-biased completion population. A locally
valid invitation can consume the time required to repair yesterday's work. A
completed repair check can still lack authority to renew a reliance decision.
The first dossier showed these failures separately. This experiment makes them
compete for the **same finite person-hour ledger** so their interaction is visible.
It responds directly to the red team's request for a coupled pipeline and retains
negative outcomes as results rather than forcing every request into success.

The interface remains offer, check, rely, amend. Internally, a synthetic request
passes through selection, atomic reservation, invitations, utility-driven
responses, reported completion, a separate scoped reliance decision and a later
repair obligation. No new participant-facing verb is required. These are
simulation records; they are not authenticated protocol messages and do not
constitute conformance to the adjacent `toy_agents` runtime.

## State, people and decisions

Each independent replicate contains 12 requests in one epoch. Three actual people
A, B and C can perform the toy review skill; one steward performs intake,
reservation triage, invitations and reliance administration. Every person has a
fixed capacity of 3, 8 or 20 model hours. Repair requires A's calibration skill,
C's inference skill and steward time. Qualification is a fixed fixture predicate;
there is no learned qualification model. Money, utility and hours are different
units.

A normally has one declared group with 1, 10 or 100 interchangeable labels.
Cloning never adds a person or an hour. A deliberately incorrect-control scenario
presents A1 and A2 as different groups while debiting both to actual person A.
The simulated evaluator knows that mapping; a real operator generally does not.
This distinction lets the negative control measure false independence without
pretending that the router has solved identity discovery.

For each request, selection draws a two-group panel using either:

- **group first:** a uniform pair of declared groups;
- **naive multiplicity:** a uniform representative panel, whose group-pair weight
  is the product of its groups' representative counts.

In fixed-panel retry, the first selected pair is retained for all attempts. In
reroll retry, each attempt draws again. Both have a maximum of three attempts.
A new selection can fail capacity reservation; it still consumes triage effort.
No finite-capacity feasibility claim is made by the initial lottery.

## Atomic capacity and actual work

The ledger tracks capacity $C_p$, spent work $U_p$ and held work $H_p$ for each
person. A demand vector $d$ is reserved only if

$$U_p+H_p+d_p\le C_p\quad\text{for every person }p.$$

The operation is all-or-none: failure changes no hold. A token can be settled
once, charging actual work $0\le x_p\le d_p$ and releasing the unused reservation.
Lanes share the same capacity, so repair cannot spend an hour already consumed by
checking. This is a sequential in-memory atomicity model, not a concurrent database
transaction or a guarantee about unrecorded external commitments.

Every admitted request charges $.05$ steward hours for intake. Each attempted
reservation charges $.02$ for triage. A reserved invitation holds one hour per
selected actor and $.1$ steward hours. Actual actor work is one hour for honest
work, $.25$ for shallow work and $.05$ for refusal/response. A reliance decision
costs another $.1$ steward hours. Each repair requires $.5$ A hours, $.5$ C hours
and $.1$ steward hours. If hidden labels share person A, their demands are summed
before admission. Costs are arbitrary declared constants, not measured labor.

A reserve variant holds one A hour and one C hour during initial checking, then
releases the holds immediately before repair. It can reduce new completions to
preserve some repair opportunity. It does not guarantee repair: steward capacity
and the number of affected uses can still bind. It also cannot repair an
undiscovered dependency.

## Utility-policy toy agents

Actors choose among honest, shallow and refuse using the largest hypothetical
utility, with ties preferring refusal, then honest work. A perceived audit chance
$q=.2$, loss $F=2$, false detection $\alpha=.02$, detection $\beta=.8$ and reward
$R=.8$ give

$$U_H=R-c_p(j,U_p)-q\alpha F,\quad
U_S=R-q\beta F,\quad U_R=u_p+\xi.$$

The outside-option shock $\xi$ is uniform on $[0,.25]$. Base effort costs are
$.12,.44,.23$ for A, B and C, with request-type increments $.04(j\bmod3)$ and
fatigue increment $.012U_p$. Base outside utilities are $.05,.4,.12$.
These quantities are synthetic utility units; they do not equal hours or money.
The monitoring probability is an **exogenous belief**. No audit is delivered or
funded by this coupled experiment; the separate hard-budget audit model examines
that missing commitment assumption.

An honest actor reports completion with probability $.95$; shallow effort reports
completion with probability $.98$. Refusal never completes. A panel completes
only when both actors report completion. This deliberately distinguishes a
finished assertion from adequate actual effort: the evaluator records whether
both worked honestly, but the decision actor does not receive that oracle.
There is no claim that a shallow check is scientifically valid or that a protocol
record discovers the lie. Actual scientific correctness is not simulated.

Independent invitation shocks permit a refusal to change on retry. Fatigue and
capacity make repeated outcomes endogenous, so the IID geometric cost formulas
from the simpler mathematical model do **not** apply here. The executable event
trace supplies observed cost and unresolved counts directly.

## Completion, scoped reliance and amendment remain different

After a reported completion, the steward either relies on every completion or,
in a negative-control condition, only on panels including A. Reliance records
name an exact toy target such as `claim-5:v1`, the scope `toy numerical decision
only`, the synthetic decision actor and the declared groups. These labels are
simulation identifiers, not cryptographic content addresses or human approvals.
Completion by itself does not issue a reliance record.

All 12 toy claims lie in a true dependency chain. The declared graph omits every
fourth edge. A material amendment to claim 0 therefore truly affects the chain
but is discoverable only through the initial declared segment. This is a known
simulation oracle for measuring missed awareness, not a proposed completeness
algorithm. A real deployment needs declared evidence and admits that some edges
may remain unknown.

Noticed affected receipts become `unresolved_material_change`. Repair can be
completed if the shared ledger has capacity. **Repair never renews reliance
automatically**: the original receipt stays unresolved until a separately
authorized new decision, which this experiment intentionally does not implement.
Undiscovered affected receipts stay locally `as_recorded`; the evaluator counts
them as unnoticed affected uses. The contrast exposes the gap between a quiet
local view and scientific currentness.

## A finite exact benchmark before stochastic policy sweeps

For a one-request, nonbinding-capacity special case, set actor completion
probabilities to $P_A=1,P_B=1/4,P_C=1$, independent across attempts. A uniform
group-pair draw gives panel completion probabilities $1/4,1,1/4$. With three
attempts, exact enumeration yields:

| Retry rule | Request completes | Expected attempts | A share among completed panels |
|---|---:|---:|---:|
| Reroll | $7/8$ | $7/4$ | $5/6$ |
| Fixed panel | $23/32$ | $15/8$ | $101/138$ |

For fixed panels, average each panel's finite geometric paths; for rerolls,
first mix the per-attempt probabilities. The policies are different even with no
strategic learning and no resource bottleneck. This oracle is exact Fraction
arithmetic and has tests against the listed rational values. An all-complete
special case is also checked against the full runtime. These special cases do
not establish exact expectations for the fatigue-dependent multi-request model.

## Results from the coupled sweep

The experiment runs 74 scenarios with 100 independent replicate seeds each:
7,400 runs and 88,800 offered toy requests. The main factorial varies lottery,
retry rule, label multiplicity, capacity and protected repair reserve. Two extra
scenarios use hidden control and selective reliance. The following values are
means or pooled descriptive shares from the specified synthetic fixture, not
forecasts of human behavior. Each row here uses 100 labels, no repair reserve.

| Lottery / retry | Hours per person | Mean completed / 12 | Mean unresolved / 12 | A share, initial panels | A share, completions | Mean actual total hours |
|---|---:|---:|---:|---:|---:|---:|
| Group first / fixed | 3 | 2.00 | 10.00 | .671 | .665 | 8.191 |
| Group first / reroll | 3 | 2.09 | 9.91 | .666 | .770 | 8.061 |
| Naive / fixed | 3 | 1.65 | 10.35 | .995 | .988 | 6.108 |
| Naive / reroll | 3 | 1.82 | 10.18 | .995 | .989 | 6.416 |
| Group first / fixed | 20 | 9.28 | 2.72 | .672 | .718 | 28.631 |
| Group first / reroll | 20 | 10.55 | 1.45 | .684 | .814 | 29.784 |
| Naive / fixed | 20 | 10.06 | 1.94 | .995 | .997 | 29.193 |
| Naive / reroll | 20 | 11.38 | .62 | .997 | 1.000 | 30.206 |

Group-first runs with 1 and 100 labels are **identical event for event** under a
shared seed, including resource debits and repair outcomes. That stronger fixture
property follows because multiplicity changes neither the lottery nor the agent
behavior or person map. Thirty seeds test this full-trace invariance. Changing
actual capacity, qualification or true control would change the premises.

The naive rule's lower work expenditure in scarce conditions is not efficiency:
it overloads the commonly selected A and leaves other capacity unusable for
those panels. It completes fewer requests and leaves more unresolved. In
plentiful conditions, naive selection can complete more reported panels because
A more often accepts; that is still a heavily concentrated population. Completion
counts alone would reward a different objective than representative opportunity.

Rerolling increases completion in these examples, but it also shifts the completed
population. With plentiful capacity, group-first offers put A in roughly two
thirds of initial panels while reroll completions include A about $.814$ of the
time. A separate reliance filter can raise the share to one without changing any
completed check. Neither outcome violates the fixed-set group theorem; each is a
new selection stage.

Repair creates another stark tradeoff. In the plentiful group-first/reroll case,
an average 3.48 known affected uses receive repair checks, while 7.07 affected
uses remain **unnoticed** because of missing declared dependencies. In the scarce
case, no repairs complete and about two noticed uses per run await capacity.
Even completed repair checks do not clear the reliance state. More available
hours cannot reconstruct the hidden chain edge by itself.

The full output contains 888 metric rows with pointwise normal 95% intervals on
replicate means. Requests inside one replicate compete for the same capacity, so
they are not treated as independent Bernoulli samples. Pooled stage shares are
reported descriptively without a misleading binomial interval. Common random
seeds across policies permit paired future analyses, but no paired confidence
claim is made here. Intervals address finite simulation variation, not utility
misspecification, behavioral uncertainty or human adoption.

## Accounting identities and falsifiable boundaries

Every trace separates request-level stages from attempt and actor counts:

$$\mathrm{offered\ requests}=\mathrm{completed\ requests}+\mathrm{unresolved\ requests},$$

$$\mathrm{invited\ actors}=\mathrm{accepted\ actors}+\mathrm{refusing\ actors},$$

$$\mathrm{affected\ relied\ uses}=\mathrm{unnoticed}+\mathrm{pending\ repair}+\mathrm{repair\ checked}.$$

Intake or capacity rejection remains an unresolved request in this experiment;
there is no terminal withdrawal state. A request may receive several refused or
failed attempts, so refusal counts are not substituted for unresolved counts.
Completed-but-not-relied requests are explicit. Actual hours and holds are exposed
for each person and lane. At termination, every hold is settled or released.

Fourteen tests check atomic failure, settlement bounds, double-settlement rejection,
shared lanes, independent panel enumeration, clone-invariant complete traces,
policy/capacity/control accounting, fixed-panel preservation, selective reliance,
hidden control sharing actual capacity and the absence of automatic renewal after
repair. Every positive behavioral interpretation remains conditional on synthetic
utilities and the chosen order of operations.

## What each community can change

A physics/astronomy group can replace the toy chain with a calibration-to-inference
graph and expose how scarce instrument experts constrain correction. A biology
group can make completion delay and evidence accessibility depend on replication
or data-use authority without treating refusal as a negative scientific verdict.
Economics and social-science groups can replace the synthetic utility function,
compare exclusion and welfare objectives, and investigate whether repeated
invitations impose unequal costs. Legal scholars can add deadline and recusal
constraints; the current hour ledger makes no claim of legal scheduling adequacy.

The human entry point is to inspect one trace, identify one assumption that would
be wrong in the participant's field, and propose a counterexample. The agent
entry point is to substitute a behavior function or graph and run the accounting
tests immediately. Neither path requires accepting a universal trust score.

## Reproduce

```sh
python3 -m unittest discover -s papers/07-release-packet/models/coupled -p 'test_*.py' -v
python3 papers/07-release-packet/models/coupled/run_experiments.py
```

Standard-library Python is sufficient. `results/summary.json` contains settings,
seeds, source/table hashes and aggregate results. Five full JSON traces expose
individual actions and ledger balances. The CSV is a plotting surface, not an
empirical dataset. The model uses no credentials, network access, real research
participants or private data. Primary mathematical context and source verification
are in `math-foundations.md` and its `models/math/source-map.json`; the coupled
simulation is a new local fixture responding to `reviews/red-math/report.md`.
