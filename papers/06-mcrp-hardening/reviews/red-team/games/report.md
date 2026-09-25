# Dedicated adversarial review: games, incentives and final allocation

25 September 2026. Same model/operator orchestration as the authors; role separation is not external or statistically independent validation. Reviewed the game manuscript, frontier supplement, packet, numerical script, economics cross-review, integrated SYNTHESIS, and current reference evaluator/hardening tests. This review does not change author files. Locations below refer to the reviewed working sources; the integrator should resolve equivalent manuscript locations.

**Verdict: conditional mathematics largely survives; revise the reset treatment and close allocation-composition gaps before claiming an executable representation-invariant mechanism.** The synthesis carefully distinguishes mathematical desiderata from deployment evidence. The most consequential new counterexample is that selecting uniformly among otherwise feasible panels still rewards duplicate representations of the same known principal. Per-panel independence constraints alone do not deliver representation invariance.

## RT-G1 — Medium: identity reset requires a new Bellman solution

**Target:** `work/games/paper.md` §5.3, lines 147–153; packet G7. Already flagged by the economics cross-review, independently reproduced here.

**Counterexample:** Set r=1, alpha=.01, beta=.20, delta=.95, F=r0=0. The absorbing benchmark gives V=16.80672. An exogenous post-reset continuation of 10 changes the honest-policy recursion to V=1+.95[.99V+.01(10)], hence V=18.40336. Replacing only W with 10 gives deterrence 1.22861; solving consistently gives 1.51681. At deviation gain 1.4 these methods give opposite classifications.

**Consequence:** The qualitative cheap-reset warning survives, but an intermediate quantitative calculation can be wrong even in the sign of whether the specified deviation is deterred.

**Minimum repair:** Require V and the reset/restriction value to solve the modified system together. Specify when reset cost is paid, whether entry value is exogenous, and whether the restricted state offers subsequent choices. For immediate full-privilege endogenous reset with V_new=V and cost k, the active branch has W_eff=V-k and V=(r-alpha F-delta alpha k)/(1-delta), subject to branch optimality. Add both exogenous and endogenous fixtures.

**Residual risk:** Real identities can reset before sanctions, use several simultaneous accounts, or wait for a cheaper opportunity. A two-state reset option does not exhaust deviations.

**Claim verdict:** G2–G3 remain valid in their original model; G7 needs this correction before numerical use.

## RT-G2 — High for an operational guarantee: feasible panels do not imply representation-invariant allocation

**Target:** `work/games/frontier-critique.md` §8, “Any preference ... objective may choose these weights”; `work/games/paper.md` §2.1; SYNTHESIS proposition and §2.

**Counterexample:** There are three known control groups A, B, C and two seats. With one representative each, uniform complete-panel sampling offers AB, AC, BC, so A appears with probability 2/3. Replace A by 100 same-control representative labels, correctly labeled as A. Enforce the stated at-most-one-seat-per-control-group constraint. There are now 100 A_jB panels, 100 A_jC panels and one BC panel. Uniform sampling over these 201 perfectly feasible panels gives A a seat with probability 200/201≈.995. No group ever takes two seats and no hidden control relationship was required.

**Consequence:** The panel support theorem about all-imported panels is correct; the stronger principal representation-invariance desideratum is not implied. An arbitrary objective or base measure can amplify a principal through admissible alternative representations.

**Minimum repair:** Choose allocation over canonical accountable-group panels first, then select a representative within each chosen group using separately declared capability rules. Alternatively require a proved invariant pushforward distribution under label cloning. Merely adding a one-seat cap is insufficient. Add clone tests holding group-level evidence, capability and capacity fixed, with both one-seat and multi-seat assignments.

**Residual risk:** New capabilities genuinely acquired by a group can justify a different allocation; invariance must hold under semantically redundant splitting, not forbid useful capability changes. Unknown group ownership remains an institutional problem.

**Claim verdict:** F5 and the synthesis survive as proposals after an explicit distribution-level invariance condition. No current implementation claim should include this property: the reference evaluator computes maximum decayed path products and has no complete-panel allocation or principal-group identity schema.

## RT-G3 — Medium: stochastic allocation bounds need a completion/retry boundary

**Target:** `work/games/frontier-critique.md` §§5,8, distribution constraint sum_bad z≤kappa and reservation/rejection language; SYNTHESIS §2 “actual final joint allocation.”

**Counterexample:** A sampler offers a risky panel with probability .1 and safe panels with probability .9. Risky panels accept and finish with probability 1; safe panels with probability .01, owing to specialist shortage or strategic refusal. Among completed panels the risky share is .1/(.1+.009)=.91743. Repeating until completion produces the same conditioning. The initial distribution obeys its .1 bound exactly.

**Consequence:** A reported proposal-level probability can be misread as a bound on completed reviews or binding dispositions. Adversaries can exploit refusal, timeout, task rerolling, capacity contention, or suppression after seeing the seed.

**Minimum repair:** Specify the protected event and sampling boundary: offer, accepted panel, completed review, or binding reliance. Log all refusals/retries against the same request and preserve bounds at that boundary or terminate with coverage unavailable. Distinguish a fixed complete-panel support constraint, which survives conditioning among supported panels, from probabilistic bounds, which generally do not. Add selective-completion and requester-reroll fixtures.

**Residual risk:** Hard support restrictions prevent the stated composition breach but can still allow indefinite denial of service. Fair scheduling and bounded retries do not force qualified humans to work.

**Claim verdict:** F1 stationary bound and deterministic F2 support result accepted; any completed-review probabilistic interpretation remains unproved.

## RT-G4 — Medium research gap, not a false theorem: incentive coverage and coalition enforcement remain unspecified

**Target:** `work/games/paper.md` §§3–5; packet G2/G5/G6; SYNTHESIS operating-envelope incentives row.

**Counterexample:** The synthetic benchmark deters a gain-2 deviation with beta=.20 (bound 3.034), but a different gain-2 omission with beta=.011 is profitable (bound .01597). A coalition including the controlling auditor can reduce incremental detection to zero even if each separately modeled outsider deviation looked deterred. The paper explicitly acknowledges both limitations; the numerical coverage does not yet exercise a complete strategic mechanism.

**Consequence:** Current checks validate formulas and examples, not an equilibrium of a working protocol. Credible promised audit funding alone does not verify auditor effort, adjudication quality, transferable sanctions or coalition commitments.

**Minimum repair:** Retain the existing qualifications and identify a concrete bounded game for the first pilot: observable actions, monitoring technology, all enumerated deviations, timing, sanctions, appeal delays, outside options and enforceable commitment. Mark unmodeled strategic actions explicitly. Include audit refusal and fabricated audit completion, instead of merely varying audit rates exogenously.

**Residual risk:** No finite enumerated action catalog proves robustness against unanticipated real conduct; agents in this orchestration share failure modes.

**Claim verdict:** Equations (1)–(4) are valid conditional payoff comparisons/interior equilibrium. “Network cooperation verified” would be unsupported; the current manuscript mostly avoids that claim.

## RT-G5 — Low: interface, history privacy and novelty language need harmonization

**Target:** game paper §§2,8,10 and source note; frontier §6; packet G1 and contribution table; SYNTHESIS four-action interface.

**Counterexample:** A stable public contribution ledger keyed by durable reviewer identity conflicts with the intended fresh public case-persona profile; offer/review/repair can be mistaken for an alternative canonical protocol. “All equations ... original stylized derivations” can imply novelty for elementary inspection-game and correlated-variance identities.

**Consequence:** These are integration/positioning ambiguities, not demonstrated breaches. They weaken the claim that one simple participant contract has been specified.

**Minimum repair:** Map game verbs to offer/check/rely/amend; place durable account history in protected custody and distinguish public object credit; describe equations as derived here from established modeling methods, with new contextual synthesis/counterexamples rather than mathematical priority claims. The economics review already requested the first two clarifications. State positive correlation eta∈[0,1] if that is the intended variance domain and nonnegative weights with a positive denominator for exploration.

**Residual risk:** Public object histories can still be linkable by content; private custody requires actual operational controls. A full nearest-work search remains incomplete.

**Claim verdict:** Design hypothesis accepted, compatibility and novelty wording need narrowing.

## Results accepted after attempted falsification

The absorbing-state Bellman algebra, one-step subtraction, inspection-game interior equilibrium, additive transferable-utility comparison, agreement-only all-pass equilibrium, and common-mode mixture formula are correct under their stated assumptions. The coalition expression is not invalid merely because adverse outcomes are correlated: expectation is linear for the assumed additive losses. The frontier stationary bound follows directly from the stated normalized row leakage and zero external restart mass; its two-state construction is tight. The tiny-edge, repeated-flow and softmax counterexamples are valid. Expected imported seats and probability of an all-imported panel are correctly distinguished. A deterministic per-panel imported-seat cap survives any subsequent selection confined to its feasible support.

The reference tooling correctly states that it computes a local routing view, not scientific validity. SYNTHESIS explicitly prevents maximum-path outputs from inheriting PageRank guarantees. I found no such algorithm mismatch in that synthesis. It would still be a mistake to count parser/path tests as identity, panel-assignment, paid-review or incentive tests.

## Source check and novelty posture

On 25 September 2026 I re-opened primary-source records for [Shnayder et al.](https://arxiv.org/abs/1603.03151), [Gao et al.](https://arxiv.org/abs/1606.07042), and [Douceur](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/). Their stated topics support the limited warnings made here. The peer-prediction records also make clear that assumptions and specific mechanisms matter; the draft appropriately does not claim all peer prediction fails. This check did not reread full proofs or verify the entire bibliography. The manuscript's explicit statement that only the Fudenberg–Maskin bibliography was accessible should remain visible. No novelty priority or systematic literature-completeness conclusion is justified.

## Independent fixtures

`python3 work/red-team/games/fixtures.py` passes reset Bellman residual and classification reversal, selective-completion conditioning, group-label panel multiplicity, deterministic support preservation, and missing-deviation examples. `fixtures.json` records the script digest and deterministic numerical outputs. The fixtures are authored separately from the specialist script; all remain same-model synthetic checks, not independent empirical validation.

## Requests to the collective red team

1. Economics: connect selective completion and refusal to scarce specialist attention; determine whose budget pays retries.
2. Science: determine whether reliability is reported conditional on completion, since exclusions can manufacture apparent accuracy.
3. Legal: distinguish organizational responsibility from actual independently enforceable mandates and sanctions; assess whether private persistent histories remain compatible with stated privacy duties.
4. Integrator: keep original objections, author response and revised-claim status separate. The important output is a narrower justified operating envelope, not a consensus badge.
