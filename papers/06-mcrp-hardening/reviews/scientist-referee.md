# Scientific referee report: promising architecture, incomplete end-to-end evidence

**25 September 2026.** Second drafting/review lane in the same model/operator orchestration. No claim of external review or independent institutional approval.

## Recommendation

Keep the scientific paper as a bounded modeling and design contribution. Do not present it as validation of the full A4 system or of human uptake. Its mathematics is sound within its assumptions; the most important remaining work connects the models to the actual assignment, correction, privacy, and human interpretation boundaries.

The compelling thesis is that a commons should make **revisable reliance** cheap enough to participate in and precise enough to repair. “A better trust graph” is a weaker and less established thesis. A finite correction cone is a particularly useful organizing concept: local modules work only while material changes can be recognized and dealt with across their boundaries.

## High-priority revisions

**S-R1. Unify the human interface.** Science proposes offer/check/rely/amend, economics request/commit/report/repair, games offer/review/repair, and law point/explain/respond/decide. Each is defensible locally, but advertising all as the minimal protocol defeats simplicity. Select one canonical interface, map the other words to specific workflows, and explicitly say the verbs are not four exclusive or sequential states. Preserve a visible authorized scientific reliance/disposition action. Do not compress this into an ambiguous approval badge.

**S-R2. Separate administrative compression from scientific work reduction.** Equation (5)'s coalescing factor is safe only if it means reduced distinct necessary work, not fewer notifications. A reused calibration check can discharge multiple obligations when its scope actually covers them. Merging ticket IDs cannot. State which quantity is modeled and evaluate recall of all affected claims after compression.

**S-R3. Add heterogeneous repair capacity.** The mean branching ratio can hide a supercritical specialty; total spare labor can coexist with an overloaded indispensable skill. `paper.md` and `model_checks.py` in this lane give a multitype resolvent and two counterexamples. This directly links the scientific cascade paper to the economics paper's complementarity and queue constraints. It is more informative than another scalar parameter sweep.

**S-R4. State the end-to-end reliance assumptions as a chain.** Exact bytes, eligible reviewer, performed check, adequate coverage, authorized disposition, correct downstream interpretation, and material-change handling are distinct dependencies. Failure at any indispensable link defeats the intended guarantee. The trust graph models one part; its mass bound is neither an epistemic risk bound nor final assignment safety. The frontier critique already provides the right assignment counterexamples. Make that relationship central in the paper rather than a caveat after the theorem.

**S-R5. Carry uncertainty through the interface.** “No check,” “outside scope,” “unresolved,” “coverage unavailable,” “restricted evidence,” and “reconsideration pending” must be valid states. Otherwise pressure for completion turns formal metadata into unjustified scientific certainty. Do not treat administrative closure or expiry as a scientific rejection or acceptance.

**S-R6. Resolve the principal adapter explicitly.** Arbitrary internal complexity is a desirable interface property. It does not replace TDRG natural-person enrollment, establish common control, or permit organizational actors to manufacture seats. Preserve authorized human accountability for the current scientific-disposition profile and mark an organization-enrollment profile as additional work.

## Mathematics and implementation checked

| Item | Finding | Required boundary |
|---|---|---|
| Science (1), imported stationary mass | Algebra correct; tight two-state construction | Every post-filter row satisfies probability ingress/egress assumptions; restart contamination modeled |
| Raw-capacity counterexample | Correct | Gate construction still unspecified; no algorithmic certification follows |
| Science (2) simplex invariance | Correct | Fixed nonnegative exploration; nonempty equal-sized groups |
| Science (3) local eigenvalue | Correct Jacobian and tangent restriction | Local result only; share/group normalization matters; critical equality unclassified |
| Science (4) equicorrelation effective count | Correct second-moment identity | No tail/correctness guarantee; common bias untouched |
| Science (5) branching workload | Correct homogeneous first-moment result | Distinct work, reachable types, finite graph effects, and type-specific capacity matter |
| Economics water filling | KKT derivation correct; active-set correction correct | Fixed known parameters, divisible effort, no setup cost or complementarity |
| Games effort condition and continuation gap | Algebra consistent | Committed monitoring; relevant deviations; bounded utility; participation separately checked |
| Games inspection equilibrium | Interior indifference conditions correct | Perfect detection, specified payoffs and parameter inequalities |
| Games common-mode error mixture | Correct for all-wrong event | Not majority error; rho here is mixture probability, not equicorrelation |
| Law load boundary | Minor overstatement | Necessary average load is ≤1; strict <1 is target slack in ordinary stochastic operation, not a universal necessary condition |

Executed `python3 -m unittest discover -s work/trust-and-review-papers/papers/06-mcrp-hardening/models -v`: all seven tests passed. The suite meaningfully tests the equations and normalization counterexample. It does not implement A0–A4, an actual assignment optimizer, bridge-cycle policy, manager tampering, privacy inference, or human behavior. This is an honest limitation, not evidence that those components fail.

Executed `python3 work/scientist/model_checks.py`: inverse and 200-generation sum agree to approximately 5.6e-17 for the stable example; hidden-specialty, unreachable-block, resource mismatch, and diamond-path fixtures passed. The model is deterministic and synthetic.

Implementation note: `assignment()` accepts finite vectors outside the simplex, while `trajectory()` validates its initial vector. The paper's conclusions concern simplex inputs. Either document the low-level helper's precondition or reject off-simplex callers before treating it as a reusable allocator. This is not a failure of the current sweeps. `stationary()` uses a fixed iteration limit, so values extremely close to alpha=1 may not converge within it; the current tested range is much milder. Do not market the helper as a general production solver.

## Missing empirical assumptions

1. **Material dependence is discoverable.** Neither a digest nor provenance automatically identifies which changes alter a scientific inference. Require explicit dependent-use links and measure missed changes.
2. **Boundary summaries preserve needed information.** Downselection can hide the phenomenon being tested. Compare to full-path fixtures where possible and name inaccessible assumptions.
3. **Observations discriminate effort from conformity.** Defect outcomes are delayed and selective; the monitor cannot be an oracle. Audit reviewer conduct separately from scientific disagreement.
4. **Public evidence and private accountability remain useful together.** Fresh personas can protect contributors while making prestige rewards and cross-case accountability harder. Selective disclosure and restricted audit need tests, not rhetorical reconciliation.
5. **Administrative burden is counted.** Simple forms can export complexity to stewards. Evaluate total labor and skill bottlenecks, not submitter clicks alone.
6. **Exit preserves useful evidence.** A fork of public records may lose private custody, standing, or access to restricted scientific inputs. Demonstrate what actually survives and what must be re-established.

## A stronger evaluation sequence

First establish that scoped records help readers interpret real checks and identify affected claims after a change. Next test coordination and capacity among a small mixed set of solo researchers and teams. Only then compare routing architectures with common downstream allocation constraints. The current staged plan broadly follows this order; keep it explicit when presenting the repository.

Predeclare useful effect sizes after a feasibility study, not by manufacturing power from arbitrary simulated rates. The key falsifier is simple: if a plain structured referee letter achieves the same scientific coverage and repair at lower total cost, prefer it and retain MCRP only as the portable record wrapper.
