# Independent-lane adversarial science review

Date: 2026-09-25. Reviewer role: science/physics adversary, separate drafting lane within the same model/operator orchestration. This is neither external peer review nor independent institutional validation.

## Verdict

**Revise before presenting an integrated protocol; retain the conditional mathematical results.** The union bound, multitype resolvent, stationary-mass bound, symmetry linearization, and covariance calculation are correct under their stated hypotheses. The science synthesis is unusually explicit about those hypotheses and does not claim empirical validation. I found no fatal algebraic error. The unresolved problem is the gap between a bounded record grammar and a functioning correction system: discoverability, currentness, dynamic workload, and shared staff are not supplied by the equations. These gaps block a claim of operational hardening, not publication as a carefully bounded research proposal.

Reviewed: `work/scientist/{paper.md,REFEREE.md,model_checks.py}`, the original `manuscripts/scientific-dynamics.md`, `models/{dynamics.py,test_dynamics.py}`, and cross-disciplinary `work/{economics,games,law}/paper.md`. Targets below are relative to the session root; line numbers refer to this review snapshot. No author files were changed.

## SCI-01 — Frozen subcriticality does not survive changing repair regimes

**Severity:** Major modeling-to-operations gap; medium revision priority for a purely conditional paper.

**Precise target:** `work/scientist/paper.md:76–90,108–114`; operational use of the spectral-radius warning in an evolving commons.

**Reproduction/derivation:** Let row-vector generations alternate between

\[
M_A=\begin{pmatrix}0&2\\0&0\end{pmatrix},\qquad
M_B=\begin{pmatrix}0&0\\2&0\end{pmatrix}.
\]

Each frozen matrix is nilpotent with spectral radius zero and would terminate after one generation. But \(M_AM_B=\operatorname{diag}(4,0)\); starting at \((1,0)\), generation \(2n\) is \((4^n,0)\). The executable fixture reaches 1,024 items at generation ten. A dashboard that re-estimates a currently subcritical matrix each epoch can therefore stay green throughout explosive alternating work.

**Consequence:** The explicitly time-homogeneous theorem remains true. It does not justify adaptive safety or an operational threshold based on successive snapshot eigenvalues. Switching calibration/inference obligations and changing policy are particularly natural here.

**Minimum repair:** Add this counterexample and state that changing regimes require analysis of products \(M_0M_1\cdots M_n\), or a justified uniform envelope. One sufficient bound is a single positive cost vector \(v\) and \(r<1\) satisfying \(M_tv\le rv\) componentwise for all admissible regimes. Then \(z_n v\le r^n z_0v\), yielding an expected aggregate weighted bound \(z_0v/(1-r)\) under the corresponding conditional expectation assumptions. Without such evidence, report workload empirically and avoid a dynamic stability badge.

**Residual risk:** A uniform envelope can be conservative or unknowable; strategic changes can leave the admissible family. Finite graphs still saturate, but may exceed available labor long before saturation.

**Verdict:** Correct stationary mathematics; dynamic assurance unestablished.

## SCI-02 — A correction cone can be perfectly accurate about the wrong graph

**Severity:** Major scientific-coverage limitation; high priority at any reliance boundary.

**Precise target:** `work/scientist/paper.md:49,53–64,128,148–154` and original scientific manuscript §6 legacy wrappers.

**Reproduction/derivation:** True claims A and B both depend on calibration C. The declared graph includes A→C but omits B→C. A C amendment gives a computed cone {A}, achieving 100% recall against declared metadata but only 50% recall against the scientific affected set {A,B}. Legacy review letters and downselected collaboration artifacts naturally omit such dependencies. The fixture implements this distinction.

**Consequence:** The word “declared” correctly limits the current definition, and the union-bound paragraph correctly refuses to assign zero missing-dependency risk. But no record mechanism discovers the omitted edge. A pilot that obtains its affected-set oracle from the same metadata it evaluates will certify an empty or incomplete cone. “Finite correction cone” must not become synonymous with complete scientific repair.

**Minimum repair:** Use two graphs in fixtures: a withheld scientific dependency oracle and the participant-declared graph. Deliberately hide an indispensable edge, include one irrelevant declared edge, and test unknown/completeness disclosure as well as cone recall. Define separate outcomes for recorded dependencies reached, true affected uses reached, and unassessable coverage. Legacy adapters must preserve incomplete-dependency status even when all fields present in the source were imported successfully.

**Residual risk:** Real scientific dependency completeness cannot generally be certified. Restricted evidence can prevent even protected evaluators from building an oracle. Quantitative reliance bounds remain unavailable in those cases.

**Verdict:** Partially recognized in the draft, but the executable end-to-end falsifier is missing; do not advertise complete propagation.

## SCI-03 — Exact-version receipts do not make downstream reliance current

**Severity:** Major protocol gap for operational use; high priority.

**Precise target:** `work/scientist/paper.md:49,128,150–152`; original scientific manuscript §1 “Rely” expiry and §6 round-trip compatibility; `work/law/paper.md` §2 coordinate separation and §5 content removal.

**Reproduction/derivation:** At t0 a downstream reader caches a valid signed reliance receipt for exact release v. At t1 a material amendment invalidates its use, or legally required removal makes indispensable evidence unavailable. At t2 an offline reader sees the same authentic receipt. The byte digest, signer, and historic disposition remain valid. Neither a correction event in another log nor preserving legal/scientific coordinate separation tells the cached reader that current reliance is unsupported. An expiry bounds the stale interval only if the client checks time and treats expired/freshness-unknown data distinctly.

**Consequence:** Immutable history and current usability must be separate projections. Legal removal should not rewrite historical scientific disposition, as law correctly says, but can still affect a present-use assessment. The danger is not an incorrect old statement; it is presenting the old statement as current assurance. This also limits backward compatibility with ordinary PDFs and repository metadata.

**Minimum repair:** Specify as-of semantics, freshness status, latest-known material-change pointer, expiry interpretation, and offline behavior for reliance views. The underlying historical disposition can remain unchanged while the use view says “freshness unknown,” “dependency unavailable,” or “reconsideration pending.” Add a replay test for an exported pre-amendment receipt and a visibility-only removal of an indispensable dependency. Promise update discoverability within stated assumptions, not guaranteed notification of all readers.

**Residual risk:** Offline copies and third-party renderers cannot be forced to refresh. High-consequence users need a declared currentness policy and may have to decline reliance when it cannot be satisfied.

**Verdict:** Record integrity supported; ongoing reliance currentness unspecified.

## SCI-04 — Separately feasible papers can allocate the same expert three times

**Severity:** Major cross-disciplinary integration gap; high priority for pilot budgeting.

**Precise target:** `work/scientist/paper.md:106–114`; `work/economics/paper.md` §§4–5, especially §5.3 maintenance; `work/games/paper.md` §§4,10 audit funding; `work/law/paper.md` §4 dedicated lane capacities.

**Reproduction/derivation:** One qualified person has eight hours. Review plans demand four, correction plans three, and dispute/audit plans two. Every separate comparison against eight passes, but combined demand is nine. Ring-fencing named lanes does not produce distinct staff. More subtly, an appeal requiring a person independent of the first decision may have zero feasible capacity even with spare aggregate hours.

**Consequence:** The science paper already defeats aggregate-versus-specialist confusion; economics explicitly says to add maintenance and operations, and law protects legal capacity. These are sound statements, but the packet lacks one joint feasible resource model to stop each subsystem from claiming the same capacity. The legal independence constraint makes this more than summing three numbers.

**Minimum repair:** Carry a single person/skill/epoch capacity ledger across initial checks, audits, correction, intake and appeal. If \(y_{j\ell}\) is person j's time in lane ℓ, enforce \(\sum_\ell y_{j\ell}\le H_j\) together with role, conflict, independence and skill constraints; count coordination and reserved standby explicitly. Add the oversubscription fixture and an appeal requiring a nonexistent independent specialist. Unavailable service remains unavailable even if all individual formulas pass.

**Residual risk:** Correlated crises, sickness, legal priorities and uncertain task sizes still defeat average plans. Small communities may be unable to offer independence at all.

**Verdict:** No contradiction in the local equations; integrated feasibility not demonstrated.

## SCI-05 — Scalar cascade factors need conditional, workload-weighted definitions

**Severity:** Moderate parameterization ambiguity; not a refutation of equation (5).

**Precise target:** Original `manuscripts/scientific-dynamics.md:206–226`; `models/dynamics.py:reconsideration_load`; scientist referee's correct warning about notification versus work coalescing.

**Reproduction/derivation:** Half of parent tickets have (B,Q,C)=(0,0,1); half have (4,1,0). Multiplying parent-averaged values gives \(E[B]E[Q](1-E[C])=2(.5)(.5)=.5\), falsely subcritical. Actual mean offspring is \(E[BQ(1-C)]=2\). The code's input contract permits both interpretations. The paper expressly says “if offspring counts have this mean,” so the conditional geometric-series theorem is safe.

**Consequence:** Plugging unweighted survey or dashboard averages into b,q,c can reverse the regime classification. High-degree, hard-to-coalesce calibration defects are exactly where the quantities may correlate.

**Minimum repair:** Define q as the candidate-edge-weighted probability that work is required and c as the conditional fraction of that required work genuinely discharged/coalesced, so bq(1−c) is a chain-rule count, or estimate offspring means directly by type. State that separately averaged parent fractions cannot be multiplied without additional assumptions. Preserve the distinction between communication deduplication and scientific work reuse.

**Residual risk:** Definitions do not solve missing offspring or biased observation of expensive unfinished cases.

**Verdict:** Equation correct given stipulated mean; estimation recipe needs tightening.

## SCI-06 — The competing “minimal protocols” remain unreconciled

**Severity:** Moderate editorial/interface integration defect.

**Precise target:** Scientist §1 canonical offer/check/rely/amend; economics §2 request/commit/report/repair; games §2 offer/review/repair; law §1 point/explain/respond/decide.

**Reproduction:** A reader who follows each paper's claimed human interface encounters three versus four actions, with an explicit reliance action present only in science. They must infer whether committing to work or reporting a check authorizes disposition. The scientist referee already raised this; it remains open in the reviewed author snapshots.

**Consequence:** The claim of a simple shared interaction vocabulary is not yet reflected in the delivered packet. Complexity has been renamed, not demonstrated to be hidden safely.

**Minimum repair:** Canonicalize the common vocabulary and label specialist verbs as subordinate workflow views. Show one worked solo-author case and one collaboration case with the same visible actions, including decline, incomplete check, unavailable capacity and unresolved amendment. Do not equate the four actions with sequential/exclusive states.

**Residual risk:** Unified names do not establish usability or low steward workload. Only measured interpretation and total labor can do that.

**Verdict:** Straightforward revision; no need for a larger rule table.

## Checks and non-findings

- Executed `python3 -m unittest discover -s work/trust-and-review-papers/papers/06-mcrp-hardening/models -p test_dynamics.py -v`: all seven tests passed.
- Executed `python3 work/red-team/science/fixtures.py`: alternating-regime, hidden-dependency, factor-estimation and shared-capacity assertions passed.
- Manually checked the 2×2 inverse, first-moment recurrence, union bound, equicorrelation variance and local tangent-space Jacobian. No algebraic discrepancy identified.
- No new novelty claim is warranted. The source papers themselves correctly identify these as standard tools applied to a proposal.
- “More diverse checks” is a hypothesis, not an assurance guarantee: organizational control independence need not remove a shared wrong scientific premise. The papers already acknowledge this and should retain that limitation in synthesis.
- The scientist's `REFEREE.md` labels law's strict-load statement a remaining minor overstatement, but the reviewed law paper already distinguishes necessary ≤1 from operational slack <1. Reconcile revision chronology; do not carry that obsolete criticism into the final issue ledger.

## Questions for collective red-team deliberation

1. Does the assembled report explicitly distinguish historic disposition, current reliance, and dependency availability after legal removal?
2. Is “simple protocol” supported by at least one coherent worked trace with unknowns and failed capacity, or only four verbs?
3. Does the final resource model debit the same experts once across review, audit, correction and appeal?
4. Are claims limited to conditional analysis and executable synthetic falsifiers, or does “hardening” silently imply live assurance, interoperability or human uptake?
5. Can a founder/operator-controlled collection of agent reports ever be described as independent validation? It cannot; independence here is only adversarial task separation.
