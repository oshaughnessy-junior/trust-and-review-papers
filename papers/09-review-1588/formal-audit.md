# Formal audit and proposed clarification for review 1588

## Audit disposition

Two reviewer criticisms misread the existing scope. The original Section 5
explicitly says “For beta > alpha, F > 0, alpha F > 0” immediately before
Proposition 4; it does not purport to divide by zero. Original Proposition 1
already quantifies over an arbitrary nonempty feasible panel family and proves
pushforward invariance without assuming all k-subsets. The unconstrained
*implementation example* does not restrict that mathematical theorem.

There is nevertheless useful clarification to make. Put assumptions locally in
numbered statements; explicitly require N >= 1 and distinguish positive audit
cost from its zero-cost case. Present expected expenditure and realized hard caps
as separate contracts, not an ambiguous replacement. Add a worked constrained
panel example without claiming that panel feasibility, qualification, or control
are discovered by the theorem. Label the ledger with the model assumptions.

The existing expected helper uses floating arithmetic. Its displayed boundary
must not be described as an exact decimal certificate. The existing hard helper
has authoritative exact rational-string outputs. The new independent
`formal/audit_contract.py` uses exact arithmetic for **both** budget contracts to
clarify their relationship and exercise the degeneracies. It is a small revision
fixture, not a rewrite or independent external validation of the old runtime.

## Proposed replacement for the opening audit result in Section 5

Let N be a fixed positive number of invitations; a >= 0 the identical **actual**
cost of delivering each audit; B >= 0 its audit-only budget. Let c,R,F,u >= 0,
0 <= alpha,beta <= 1, and 0 <= q <= 1. Utilities remain

$$U_H=R-c-q\alpha F,\quad U_S=R-q\beta F,\quad U_A=u.$$

These are linear expected utilities. Audit delivery, detection discrimination,
enforceable loss, and the applicable marginal probability at the actor's
information set are premises. Reward financing and capacity outside the audit
budget are not included.

Write d=(beta-alpha)F, h=alpha F, and v=R-c-u. Two budget contracts give caps

$$q_E=\begin{cases}1,&a=0,\\\min\{1,B/(Na)\},&a>0,\end{cases}
\qquad
q_H=\begin{cases}1,&a=0,\\\min\{N,\lfloor B/a\rfloor\}/N,&a>0.\end{cases}$$

**Proposition 4a (expected-expenditure feasibility).** Under the preceding
assumptions, honest work is a weak best response against shirking and abstention,
and expected expenditure on N invitations is at most B, exactly when

$$q\in\mathcal Q_E:=\{q\in[0,q_E]:dq\ge c,\ hq\le v\}.$$

For d>0 and h>0 this is the interval

$$\frac{c}{d}\le q\le\min\{q_E,v/h\},$$

empty when the lower bound exceeds the upper. The division-free form covers all
degenerate cases: if d=0, positive effort makes it empty; if d<0, only q=0 with
c=0 can satisfy effort; if h=0, participation requires v>=0 independently of q.
Zero audit cost removes only the spending constraint, not effort or participation.

*Proof.* U_H>=U_S is dq>=c and U_H>=U_A is hq<=v. Linear expectation of N audit
indicators, each with marginal q, gives Naq expenditure without requiring their
independence. Intersect these constraints with 0<=q<=1. Conversely every point
in the intersection satisfies all three inequalities. Square.

**Proposition 4b (realized hard-cap feasibility).** Suppose instead that no
realization may cost more than B. With fixed N and identical delivered cost a,
equal marginal q is achievable by a lottery on audit subsets exactly when
q<=q_H. Therefore weak-incentive feasibility under this contract is

$$\mathcal Q_H:=\{q\in[0,q_H]:dq\ge c,\ hq\le v\}\subseteq\mathcal Q_E.$$

*Proof.* For a>0, every subset has cardinality at most
K=min(N,floor(B/a)), hence Nq=E[subset size]<=K. Conversely, for any Nq<=K,
let k=floor(Nq) and theta=Nq-k. Choose a uniformly random size-k subset with
probability 1-theta, or a uniformly random size-(k+1) subset with probability
theta. The latter branch has zero probability at an integer Nq; every positive
probability branch has cardinality at most K. Each invitation has marginal
[(1-theta)k+theta(k+1)]/N=q, and each realization respects the budget. When a=0,
every subset costs zero. Intersect with the unchanged effort/participation
constraints. Square.

The lottery must remain concealed until effort choice, or more generally preserve
the assumed q at each actor's decision information set. The theorem constructs
a distribution; it does not supply concealment, credible enforcement, authentic
independent auditors, correct detection, or delivery. Revealing selection before
action gives unaudited actors conditional q=0, so the common-q incentive argument
no longer applies to them. Variable audit costs, risk-sensitive utility or changing
N require a different model.

### Worked comparison and negative cases

For N=3, a=1 and B=3/2, q_E=1/2 while q_H=1/3. These caps do not conflict: they
answer different budget promises. Independent Bernoulli audits with q=1/2 respect
the expected budget but exceed it in half of realizations. A hard-cap lottery
with q=1/4 audits nobody with probability 1/4 and each of the three singletons
with probability 1/4, so it never spends more than one unit.

For c=2/5, R=2, F=1, alpha=0, beta=1 and u=0, expected-budget feasibility is
[2/5,1/2] but hard-budget feasibility is empty. Thus hard budgeting can change
feasibility, not just adjust a displayed endpoint. Neither contract implies that
honesty will be selected when it ties with abstention; these are weak best-response
sets, not equilibrium selection or forecasts of observed effort.

For F=0 and c>0, no audit rate creates an effort incentive. For c=0 and beta<alpha
with F>0, only q=0 weakly favors honest work over shirking. For alpha F=0,
R-c>=u remains necessary regardless of an unlimited audit budget. These cases
show why the division-free formulation is more complete than a single displayed
ratio.

## Feasible-panel clarification to add after Proposition 1

Proposition 1 applies to **any** nonempty feasible family F of group panels,
including panels constrained by declared skill coverage, conflicts, independence
and capacity, and **any** normalized Q on that family. It does not require
uniformity. The clone transformation must leave the true/declared group map,
feasible family and group-level distribution unchanged; the conditional
representative kernel only has to normalize to one for each chosen group panel.
The proof sums that kernel to one, so constraints do not alter it.

The new small constrained example constructs F from a fixed group-level fixture
and compares policies under changed representative counts. This is an
implementation illustration of a theorem already stated, not a new theorem
extending an unconstrained result. Empty F must return no feasible panel rather
than silently relax conflicts, skill coverage or requested size. If a supposedly
group-level weight or capacity changes when names are cloned, Q or F changes and
the theorem's premise fails. Hidden common control remains an independent failure.

## Claim-ledger wording

- M1: **T (fixed feasible family and group-level distribution)**; constrained as
  well as unconstrained families, subject to their construction and fixed premises.
- M2: **T (conditional completion envelope; IID retry accounting)**. The existing
  adapted completion envelope is separate and does not import IID retry costs.
- M4a: **T (expected audit expenditure)**; linear one-shot utility and known costs.
- M4b: **T (hard identical-cost cap, concealed equal-marginal lottery)**; no claim
  that the expected cap is a reservation or that concealment is implemented.

“T” names a conditional proved statement, not applicability beyond its premises.
The review's concern is addressed by visible qualifiers rather than weakening a
correct theorem into a simulation-only claim.

## Executable evidence

`formal/audit_contract.py` and `formal/test_audit_contract.py` add eleven named
exact tests. One independently compares interval membership with direct utilities
and the appropriate spending condition in **864 parameter combinations at five q
values** (4,320 checks), including alpha/beta/F/c zeros and negative discrimination.
Others enumerate hard-cap lottery outcomes and check every actor's marginal,
verify hard feasibility is a subset of expected feasibility, and retain the
expected-feasible/hard-infeasible counterexample. `formal/results.json` includes
both exact intervals and the q=1/4 lottery. No real preferences, costs or audit
outcomes are estimated.

```sh
python3 -m unittest discover -s papers/09-review-1588/formal -v
python3 papers/09-review-1588/formal/audit_contract.py
```

No original mathematical error was found in Proposition 1 or the stated
positive-denominator expected interval. The revisions improve the assumption
boundary, complete the degenerate formulation, and give the hard budget its own
necessary-and-sufficient result. They do not establish new underlying mathematics
or empirical protocol effectiveness.
