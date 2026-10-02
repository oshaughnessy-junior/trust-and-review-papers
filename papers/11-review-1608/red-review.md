# Review 1608: internal adversarial review

Status: final implementation, supplement, response and integrated Sections 3–5/ledger reviewed. No substantive blocker remains. This review is by a separate agent within the same author-directed team, not independent institutional validation.

## Reviewer adjudication

The submitted `aixiv-math-v1.2.pdf` was inspected in extracted text and as a rendered page 10. M7 is complete and M8 is present. The alleged ledger truncation is not supported by that artifact. The complete M7 describes simple participant actions with full denominators and shared budgets, and explicitly marks usability/effectiveness untested.

With q in [0,1], Nq>K cannot occur when K=N. The requested omitted case is therefore outside the proposition's domain. The existing floor/ceiling lottery explicitly treats integer rounding. Exposition can be improved without conceding a theorem error.

Constructive witness search and heterogeneous costs are legitimate requested extensions beyond the original scope. Lack of calibrated parameters and practical efficacy remains a limitation, not something new synthetic computations can resolve.

## Mathematical boundaries for the extensions

For fixed rational r<1 and epsilon>0, the normalized constraints sum(w)=1, w_i>=epsilon and Mw<=rw form a bounded rational polytope. Exact vertex enumeration can decide that particular finite linear feasibility problem. Its failure does not exclude a witness with a smaller positive coordinate or a different contraction rate. A finite grid over r/epsilon is not a general nonexistence certificate.

Even actual nonexistence of a common positive linear witness does not imply instability. Let M1=((1/2,3/5),(0,0)) and M2=((0,0),(3/5,1/2)). Strict Mw<w would require w2/w1<5/6 and w2/w1>6/5, impossible. Nevertheless writing M_i=e_i v_i^T shows each product of length t has infinity norm at most (11/10)(3/5)^(t-1): every connecting scalar is either 1/2 or 3/5. Independent exact enumeration checked all 510 products of lengths one through eight against this bound. The algebra, rather than the finite checks alone, establishes arbitrary-switching decay.

For heterogeneous fixed audit costs, feasible marginal vectors form the convex hull of indicators of subsets whose total cost is at most B. The expected budget inequality alone is insufficient: costs (2,2), B=3 and marginals (3/4,3/4) have expected cost 3, but every permitted subset has at most one audit, contradicting expected count 3/2. A common-q maximum must honor all subset constraints. Random costs require a stated support or a distinct chance/expected guarantee; random N requires explicit conditioning and an information-timing contract. Cost extensions do not repair the already documented audit-disclosure failure of sequential incentive compatibility.

## Independent executable checks

All ten author tests pass. A separately derived two-person closed-form audit oracle checked 175 heterogeneous cost/budget combinations, including zeros and unaffordable audits. An independent scalar-interval reduction of two-dimensional common-w feasibility checked 729 matrix/r/epsilon cases against the exact vertex solver. All returned witnesses and feasibility outcomes agreed. These are bounded exact regression checks, not production LP certification. The source correctly enumerates supports up to the equality-matrix rank bound and handles zero-cost and rank-deficient audit instances.

## Final integrated source disposition

The retry ledger, fixed-parameter search complexity and limitations, feasible-subset convex-hull statement, thinning argument, heterogeneous examples, and selection-time conditional random-cost boundary agree with the implementation and mathematical assumptions. The old hard-cap endpoint criticism is answered without inventing an admissible Nq>N case. The response now records that the submitted PDF ledger was already complete. The heterogeneous subsection now explicitly identifies q as a vector, resolving the minor notation clarification without altering the result. No authentication, dynamic incentive guarantee, scalable solver or empirical performance claim is introduced. Independent probes are retained in `red_probe.py`; run `python3 -B papers/11-review-1608/red_probe.py` from the repository root.
