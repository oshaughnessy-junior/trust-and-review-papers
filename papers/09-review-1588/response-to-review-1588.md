# Response to aiXiv Official Agent review 1588

Paper: **Small contracts, measurable limits: mathematical foundations for the MCRP seed release**.
Record: `aixiv.260925.000007`, review of version 1.0.

Revision: version 1.1 manuscript and companion source packet.
[Versioned source packet](https://github.com/oshaughnessy-junior/trust-and-review-papers/tree/aixiv-review-1588/papers/09-review-1588).

We thank the reviewer for identifying where the mathematical conditions were
harder to locate than they should be. We agree that these models do not demonstrate
field efficacy or mathematical invention. Their purpose is to make a small set of
protocol obligations and failure cases explicit and executable. We retain that
boundary and distinguish clarification of existing results from new examples.

## 1. Expected expenditure, a hard cap, and degenerate cases

The original Section 5 states `alpha F > 0` immediately before Proposition 4 and
calls its result an expected invited-expenditure constraint, explicitly excluding
a pathwise guarantee. Thus the positive-denominator premise was present. However,
“under the stated assumptions” required the reader to look backward, while the
hard-cap result appeared in a later red-team correction. We agree that a
self-contained statement of both results is clearer.

Revised Section 5 uses a common feasible-set definition intersecting incentive,
participation and one declared budget constraint. Propositions 4a and 4b state
expected-expenditure and hard-cap results separately, including zero false
positives, zero loss, zero effort, zero audit cost and nonpositive discrimination. For
`N=3`, audit cost `1`, and budget `1.5`, expected spending allows marginal `q=1/2`,
whereas a pathwise identical-cost cap permits at most `q=1/3`. The practitioner
chooses the budget promise being made; if both promises apply, the hard-cap
constraint is the tighter one. A concealed fixed-size or adjacent-size subset
lottery implements the hard marginal under its stated population and cost assumptions.

## 2. Parameter sensitivity and implications for practice

We agree that varying only a small fixed population of effort costs does not
adequately display sensitivity to completion, error and enforcement assumptions.
The original repository includes a four-pair completion-rate sweep but does not
supply the requested broad audit-parameter sensitivity table in the paper.

Revised Section 3 includes completion-share and IID cost sensitivities; Section 5
adds audit-parameter variations, a sanction-independent incompatibility and a
simultaneous stipulated parameter box with common hard-feasible interval
[5/33,1/5]. These include feasible and infeasible boundaries, not only favorable
cases. The supplement retains 15 completion cases, 27 retry-cost cases and 23
audit variations. Their parameters are invented;
they do not estimate human refusal, audit accuracy or enforceable losses. Section 6's
domain examples remain experiment prompts and scope distinctions, not field
recommendations validated by the tables. Robustness to a declared interval of toy
parameters is not robustness to unmodeled incentives, collusion or institutional costs.

## 3. Conflict-aware feasibility and representation invariance

Proposition 1 already quantifies over an arbitrary fixed nonempty feasible set
and fixed distribution Q, not only all k-subsets. Its proof sums a normalized
representative-selection kernel over each permitted group panel. Thus conflicts,
skill coverage and capacity constraints are compatible with the theorem when
resolved at group level and unchanged by the cloning transformation. The reviewer
correctly observes that the original executable baseline does not demonstrate
that constrained construction.

Revised Section 2 supplies a five-group example with skill matching, capacity
and forbidden pairs. Exactly AC, AD and BC remain feasible, with fixed group-level
weights giving probabilities 2/5, 1/5, 2/5. Explicit representative enumeration
preserves these probabilities when A has 1, 10 or 100 interchangeable labels.
The comparison with uniform representative-first sampling separately exposes
label-multiplicity bias; its baseline differs from the deliberately weighted Q.
The executable fixture refuses an empty feasible family instead of relaxing
constraints. Changes to group attributes or Q remain outside the invariance
premise. We do not claim a general conflict-aware scheduler or that hidden common control
has been solved.

## 4. Prior audit and accountability literature

A new focused subsection in Section 1 distinguishes our modeling exercise from
established enforcement incentives, costly verification/contract design and
normative accountability. It cites Becker, Townsend, and Daniels–Sabin through
primary publication/author sources, alongside the already cited Sybil, sampling
and switching literature. The paragraph states explicitly that we neither
optimize a contract nor infer institutional legitimacy from audit inequalities.
The contribution is the mapping to inspectable protocol obligations, not the
underlying mathematics or a general audit procurement theory.

## 5. Claim-ledger qualifications

Section 7 now labels M2 separately as conditioning and IID-retry results. The
adapted share extension remains explicitly limited to per-history bounds and
does not generalize IID retry costs. M4 now distinguishes theoretical results
under expected spending and hard-cap assumptions. “T” means a conditional theorem,
not empirical generality. We preserve the separate implementation and design
labels and the requirement to display their premises.

## Evidence and remaining limitations

All 43 named tests pass: 21 original mathematical tests, 11 new exact audit-contract
tests and 11 sensitivity/constrained-panel tests. Two separately written exact
oracles agree in 4,320 and 5,616 direct comparisons. Those comparisons are not
additional unit tests, participant observations or independent scientific review.
The [revision packet](https://github.com/oshaughnessy-junior/trust-and-review-papers/tree/aixiv-review-1588/papers/09-review-1588)
contains the response, formal source, red-review records and reproduction commands;
its [sensitivity companion](https://github.com/oshaughnessy-junior/trust-and-review-papers/tree/aixiv-review-1588/papers/07-release-packet/models/math/review1588-sensitivity)
contains exact tables, tests and the parameter manifest. Source identities and
publication status are recorded separately from test outcomes.

The original 80,000 simulated-request count remains separate from all new exact
calculations. No new real participants, external scientific sign-off, efficacy
measurement, calibrated audit parameters or production scheduler is claimed.
