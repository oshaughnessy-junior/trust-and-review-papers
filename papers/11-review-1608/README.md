# Review 1608: constructive, bounded extensions

These are exact synthetic illustrations of established linear-program geometry,
not new stability or mechanism-design theorems. The existing four-action machine
is unchanged. No empirical accuracy, calibrated costs, authentication or strategic
commitment is supplied.

## Common positive repair witness

For a finite family of nonnegative rational n-by-n matrices, fixed rational
0<=r<1 and 0<epsilon<=1/n, solve

    sum(w)=1, w_i>=epsilon, (M-rI)w<=0 for every M.

This compact polytope is empty or has a vertex. The standard-library implementation
enumerates n-1 active inequalities alongside normalization, solves exactly, and
checks every constraint. Dependent active sets are skipped. The normalization
hyperplane plus n-1 independent active inequalities suffices even for a
lower-dimensional feasible polytope. There are at most binomial(m*n+n,n-1)
candidates; Gaussian elimination costs O(n^3) rational arithmetic operations per
candidate, plus O(m*n^2) verification. Bit complexity also depends on input sizes.
The executable deliberately caps n and m at four. This enumeration is combinatorial,
not a practical large-system LP solver.

`None` certifies emptiness only for the supplied r **and epsilon**. It neither
rules out another positive witness nor proves instability. With rational finite
inputs, any strictly positive contractive witness implies one for some rational
r<1 and some rational epsilon>0 after normalization; increasing r and decreasing
epsilon gives a search procedure that eventually finds such a witness when one
exists, but has no finite universal stopping certificate when none exists.
One may instead solve the fixed-r LP with w_i>=1, avoiding the epsilon restriction;
it is equivalent to existence of a positive witness at that r by scaling. A
standard LP implementation can handle that unbounded feasible region.

Example M=((0,1),(0,0)), r=1/2: uniform weights fail, but w=(2/3,1/3)
passes. epsilon=2/5 rejects this fixed-r problem, while epsilon=1/4 succeeds.
A test also distinguishes failure at r=1/2 from success at r=4/5 for M=(3/4).
The established switching-explosive pair remains an unsuccessful search fixture.
All numbers are stipulated, not estimated from repairs.

## Heterogeneous deterministic audit costs

For a fixed cohort with costs kappa_i>=0 and budget B, let S_B contain exactly the
subsets whose summed costs are at most B. An achievable marginal vector q is
exactly a convex combination of their indicator vectors. Thus expected spending
sum(kappa_i*q_i)<=B is necessary but insufficient for hard feasibility. With equal
utilities, maximize common marginal t subject to sum(lambda)=1, lambda>=0, and
sum(lambda_S*1{i in S})=t for each i. Any smaller nonnegative common marginal is
obtained by mixing an optimum lottery with the empty subset. Intersect that
interval with the unchanged effort/participation inequalities; an ex-ante
probability still does not imply conditional incentive compatibility after
selection or audit outcomes are disclosed.

Our finite solver eliminates t by equating other marginals to marginal zero.
Its equality matrix has n rows including normalization. An optimal basic solution
exists with at most rank(A)<=n support columns. We enumerate supports of sizes
one through n and solve the possibly overdetermined system exactly, retaining
nonnegative solutions. This includes rank-deficient and zero-cost cases. At most
2^n subsets and sum_{k=1}^n binomial(2^n,k) supports are considered. It is deliberately
limited to n<=4, not an efficient procurement algorithm.

For costs(2,1),B=2 only singletons or the empty set fit. The maximum common
marginal is 1/2, achieved by half-probability singleton audits, while expected
spending alone permits 2/3. For costs(2,1,1),B=2, audit {0} or {1,2} each with
probability 1/2. The retained JSON includes both and degenerate fixtures.
`lottery_marginals` verifies the exhibited pathwise budget and marginal certificate;
optimality additionally follows from exhaustive basic-support enumeration.

These fixtures assume deterministic actual delivered costs. Random costs need
another declared contract: robust support-bounded subsets, a joint almost-sure
support condition, an explicitly stated chance constraint, or only an expected
budget. If a selected audit retains an unbounded positive cost tail conditional on
selection-time information, it cannot ensure a finite hard cap without an external
cap. Marginal unboundedness alone does not imply this conditional premise. Likewise, a random cohort requires a policy conditional on its realized
size; a realized cap with an unknown/unbounded cohort cannot be replaced by plugging
E[N] into a fixed-cohort formula. Selection correlated with cost or information
changes the applicable probabilities and incentives.

## Reproduction and attribution

From repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s papers/11-review-1608 -p 'test_*.py' -v
PYTHONDONTWRITEBYTECODE=1 python3 papers/11-review-1608/extensions.py
```

Ten internal tests cover exact witness certificates, fixed-parameter search
failures, heterogeneous lotteries, homogeneous rounding, zero-cost and unaffordable
cases, thinning and validation. These tests are finite implementation checks.

Original code, JSON fixtures and synthetic results are MIT; original prose is
CC BY 4.0, under the [release-packet terms](../07-release-packet/LICENSE.md)
and [MIT text](../07-release-packet/LICENSES/MIT.txt). Attribution: MCRP contributors,
maintained by oshaughnessy-junior; substantial drafting, implementation and internal
adversarial review by Codex agents under the corresponding human maintainer.
Cited works retain their rights. This does not imply independent validation.
