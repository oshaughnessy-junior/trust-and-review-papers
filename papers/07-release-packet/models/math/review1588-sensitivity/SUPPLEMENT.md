# Sensitivity and feasible panels: response to review 1588

**Synthetic exact examples, 25 September 2026.** This supplement answers the
requests for behavioral-parameter sensitivity and a constrained panel example.
Parameters are stipulated; tables are not estimates of scientific-agent behavior,
review quality, legal enforceability, or institutional capacity. The original
manuscript's Proposition 1 already covers any fixed nonempty feasible family.
The new example exercises that premise rather than extending the theorem's scope.

## 1. Completion distortion depends on relative completion rates

For 0<p<1 and a,b>0, writing z=pa/[pa+(1-p)b] gives

\[
 \frac{z}{1-z}=\frac{p}{1-p}\frac ab,
 \qquad z>p\iff a>b.
\]

Thus the offered-to-completed odds multiplier is exactly a/b. The logarithm of
completed odds has elasticities +1 in a and -1 in b. There is no categorical
prediction that any particular real group gains share. Equal completion rates
preserve the offered share; reversing the rates reverses selection. The partial
derivatives are p(1-p)b/[pa+(1-p)b]^2 and
-pa(1-p)/[pa+(1-p)b]^2 respectively. If no positive lower bound on b can be justified,
the uniform upper bound on z can approach one despite a small positive offered p.

With p=1/10, the following exact values sample the retained 15-case factorial:

| a | b | Completed share z | Interpretation inside this fixture |
|---:|---:|---:|---|
| 1/10 | 1/100 | 10/19 | Tenfold completion odds ratio |
| 1/10 | 1/10 | 1/10 | No selection distortion |
| 1/10 | 1 | 1/91 | Reverse selection |
| 1 | 1/100 | 100/109 | Original extreme contrast |
| 1 | 1/10 | 10/19 | Same ratio, same completed share |
| 1 | 1 | 1/10 | All offers complete |

These are exact probabilities, not estimated frequencies or uncertainty intervals.
The completion envelope follows the same monotonicity: bound the unknown rate
ratio using a≤u and b≥ell>0. This does not compel anyone to complete a check or
supply a real-world lower completion bound.

Under the original IID retry premises, let T=E[N_L] and P_L be the probability
of completion. Then E[C_L]=c_i T+c_c P_L, with sensitivities
partial E[C_L]/partial c_i=T and partial E[C_L]/partial c_c=P_L. At p=.1,a=1,b=.01
and L=10, T≈6.281298 and P_L≈.684661. The retained 27-case cost factorial varies
L∈{1,10,50}, c_i∈{.02,.2,2}, and c_c∈{.2,2,20}. For L=10:

| c_i | c_c | Expected cost, rounded display |
|---:|---:|---:|
| .02 | 2 | 1.494949 |
| .2 | .2 | 1.393192 |
| .2 | 2 | 2.625583 |
| .2 | 20 | 14.949489 |
| 2 | 2 | 13.931919 |

Changing these prices changes resource conclusions, not the IID completed-share
formula. Adaptive learning, fatigue, correlated retries and partial work require
new models; the table gives no robustness guarantee when those premises change.

## 2. Auditing has distinct sensitivity bottlenecks

For this sensitivity branch only, assume N≥1, unit audit cost a_a>0, F>0,
alpha>0, beta>alpha, and all other costs nonnegative. Degenerate branches belong
to the companion general audit specification. Define

\[
 q_- = \frac{c}{(\beta-\alpha)F},\quad
 q_P=\frac{R-c-u}{\alpha F},\quad
 q_E=\min\{1,B/(Na_a)\},\quad
 q_H=\min\{N,\lfloor B/a_a\rfloor\}/N.
\]

The expected-expenditure feasible interval is [q_-,min(q_E,q_P)]; the concealed,
fixed-population identical-cost hard-cap interval is [q_-,min(q_H,q_P)]. Empty
intervals mean no q satisfies that specified regime. A hard operational cap uses
the latter; one must not intersect away the stricter condition by averaging the
two answers. Increasing F lowers both the effort threshold and participation
ceiling. More severe sanctions do not uniformly improve participation.

Use baseline c=.2,R=1,u=.1,F=2,alpha=.02,beta=.8,N=100,a_a=.1,B=2. Its hard interval
is [5/39,1/5]. The following subset summarizes 23 retained one-at-a-time rows;
all unspecified parameters remain at baseline.

| Variation | Effort lower bound | Hard upper bound | Nonempty? |
|---|---:|---:|---|
| alpha=.1 | 1/7 | 1/5 | Yes |
| alpha=.3 | 1/5 | 1/5 | Yes, one weak-indifference point |
| beta=.4 | 5/19 | 1/5 | No |
| beta=1 | 5/49 | 1/5 | Yes |
| c=.4 | 10/39 | 1/5 | No |
| F=1 | 10/39 | 1/5 | No |
| F=4 | 5/78 | 1/5 | Yes |
| a_a=.2 | 5/39 | 1/10 | No |
| B=4 | 5/39 | 2/5 | Yes |

A nonempty weak-best-response interval permits honesty to tie another action;
it does not imply that real or simulated actors choose honesty at that tie.
The model does not fund rewards, enforce sanctions, or prove audit independence.

A simultaneous, stipulated uncertainty box gives a stronger sensitivity statement
than one-at-a-time rows: c∈[.1,.2], alpha∈[.01,.04], beta∈[.7,.9], F∈[2,3], with
other baseline quantities fixed. The lower bound increases with c and alpha and
decreases with beta and F. The participation upper bound decreases with c, alpha,
and F throughout this box, where R-c-u>0. Therefore checking these endpoints gives
one common hard-feasible interval for every point in the box:

\[
 \bigcap_\theta[q_-(\theta),\min(q_H,q_P(\theta))]=[5/33,1/5].
\]

Sixteen corners and 81 interior/grid points are checked exactly. This is an
assumption-conditional robust region, not a confidence region for actual behavior.

### A sanction-independent incompatibility

Within the positive-discrimination branch,

\[
 q_-\le q_P\iff c\alpha\le(R-c-u)(\beta-\alpha).
\]

F cancels. If the right side is too small, no sanction magnitude repairs the
honest-participation/effort conflict, even with unlimited audit funding. Set
R=.4,c=.2,u=.1,alpha=.3,beta=.8: right minus left equals -.01. F=1,2,8 all remain
infeasible. Raising F can relieve a funding-limited threshold while leaving this
separate conflict unchanged. Detection quality, reward, outside option, and effort
are distinct levers in the stipulated model; none is an institutional recommendation.

For the review's fractional budget example, set N=3,a_a=1,B=1.5 and choose
c=.4,F=1,alpha=.1,beta=1,R=2,u=.1. Then q_-=4/9, q_E=1/2, q_H=1/3. The expected
interval [4/9,1/2] is nonempty; the hard interval [4/9,1/3] is empty. This is a
change of budget semantics, not contradictory answers to one feasibility question.

## 3. A skill-, conflict-, and capacity-filtered panel distribution

A single two-task review requires one calibration and one inference assignment.
Each selected group supplies one unit of work and can fill at most one task.
Declared group attributes are:

| Group | Skills | Available units | Fixed group weight |
|---|---|---:|---:|
| A | calibration | 1 | 1 |
| B | inference | 1 | 1 |
| C | calibration, inference | 1 | 2 |
| D | inference | 1 | 1 |
| E | calibration | 0 | 1 |

A–B and C–D are forbidden conflict pairs. The constructor enumerates pairs,
rejects conflicts and zero capacity, and requires a matching of distinct groups
to the two skill tasks. This yields exactly

\[
 \mathcal F=\{\{A,C\},\{A,D\},\{B,C\}\}.
\]

A–B and C–D fail conflicts; B–D fails calibration coverage; all E panels fail
capacity. A–C and B–C use C for different roles, never two units simultaneously.
Choose Q(S) proportional to the product of fixed group weights. Then
Q(AC)=2/5, Q(AD)=1/5, Q(BC)=2/5 and A's inclusion probability is 3/5.
Uniform Q is also possible and would give each feasible panel probability 1/3.
Neither weighting choice is asserted to be fair or scientifically optimal.

After drawing S, choose an interchangeable representative within each group by a
normalized conditional kernel. Enumerating the uniform kernel with 1,10,100
representatives of A reproduces the same Q exactly. In contrast, uniform sampling
among feasible representative panels gives A inclusion 2/3 at one label and
20/21 at ten labels. That comparison uses uniform representative selection; its
one-label baseline differs from the intentionally weighted Q and is reported
separately. Label multiplication changes neither skill, declared capacity, group
weight nor the conflict relation in this experiment.

The additional premise is not that Q must be uniform: the group attributes,
feasible family and Q must remain unchanged under the specified relabeling. Within-
group representatives must remain interchangeable for the assigned role. If a
new representative brings real new skill or independent capacity, or hidden common
control is uncovered, those premises change and invariance is not the appropriate
comparison. The group/control map is supplied, not authenticated.

If no matching panel exists, the constructor returns no distribution and the
request remains unassigned; it does not relax conflicts or coverage. This is a
one-panel feasibility calculation. It does not reserve capacity transactionally,
schedule multiple concurrent requests, infer competence or settle conflicts.

## 4. Reproduction and insertion guidance

From the repository root:

```sh
python3 -m unittest discover -s papers/07-release-packet/models/math/review1588-sensitivity -p 'test_*.py' -v
python3 papers/07-release-packet/models/math/review1588-sensitivity/sensitivity.py
```

`results.json` retains rational strings for all 15 completion rows, 27 retry-cost
rows, 23 audit rows, three sanction-conflict examples, the 16-corner box summary,
the fractional-budget case, and constrained distributions. Eleven named tests
include independent finite retry paths, direct utility comparisons, an independent
ordered skill-matching oracle and explicit representative pushforwards. Standard
library only; there are no estimated behavioral parameters or scientific agents.

Suggested manuscript integration: add the constrained example after Proposition 1;
add the completion and cost sensitivity summary after the IID retry example; add
audit tables, robust box and sanction incompatibility after the reconciled audit
propositions. Keep the companion general audit definitions authoritative for zero
alpha/F/cost and nonpositive discrimination. Label every new table synthetic.
