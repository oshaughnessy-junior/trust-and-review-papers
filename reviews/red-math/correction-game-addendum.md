# Review of the correction-credit deviation bridge

The original ecology vulnerability remains reproducible. The blue lane has now added an explicit one-step choice between clean work and manufacturing a defect followed by successful repair. This is useful progress beyond a purely verbal warning: it exposes exactly which private reward and externalized-cost assumptions make the adverse choice profitable.

## Independent evidence

`correction_game_review.py` independently reconstructed all 18 case/policy outcomes with direct exponential normalization, score updates and utility differences. Every recorded probability and payoff matched to less than 1e-12. All eight author tests passed.

The default author-and-repairer credit rule gives author deviation gain +7.269752 and coalition gain +17.539505. Repairer-only credit gives author gain -19.108451 while coalition gain remains +13.108451. No allocation credit gives -3 for both. These are conditional utility differences under an assumed valuation of attention, not calibrated welfare estimates. The ordinary defect-detection process must not be substituted for the separately assumed probability of proving intentional manufacture.

Full private cost internalization removes the positive default coalition gain (it becomes about -0.460495). Exogenous clean-author credit removes the unilateral gain, but the author-and-repairer coalition can still gain about +1.431053. This retained sensitivity is useful: apparently intuitive mitigations do not all solve the same problem. Nothing here establishes that suppressing correction credit is optimal or that genuine repair effort will then be supplied.

## Interpretation clarifications

1. **Clean-credit baseline.** The case labeled `verified_clean_baseline` grants exogenous author credit. It does not replay the full ecology audit workflow, which can also credit a correct checker and consumes audit labor. Describe this as a clean-author-credit sensitivity, not a complete funded verification intervention. The same update/allocation formula is reused, but the whole ecology process is not composed into this two-action game.
2. **Repair capacity.** The scalar test h<=available capacity is a one-case feasibility calculation. Subtracting h once correctly gives the remaining capacity for that case. It is not a stateful multi-case shared ledger or a schedule. Repeated independent calls do not reserve actual common capacity. The coupled simulator supplies a separate shared-ledger demonstration.
3. **Coalition cost.** The default coalition contains the credited repairer but internalizes only 10% of repair cost. This deliberately assumes substantial externalization or compensation, for example an institutional budget or subcontracted effort. If the repairer's entire effort disutility is borne privately and no offset exists, the coalition share must reflect that; the full-internalization sensitivity illustrates the difference. Attention, effort tokens and utility remain separate units until the specified conversion factor is applied.
4. **Completion and attribution.** Profitable-if-feasible is conditional on the manufactured defect being successfully repaired and credited. The model has no stochastic failure path, limited-liability collection, alternative misconduct, detection-cost budget or repeated strategic learning. Its two-action comparison should not be promoted to incentive compatibility of the protocol.
5. **Social cost proxy.** The 26-unit quantity deliberately assumes a common utility scale and includes manufacture, full repair effort and temporary harm. It is a descriptive proxy, not comprehensive scientific welfare. Zero-sum redistribution of future attention is not counted as new social value.

These are interpretive boundaries rather than new defects in the payoff arithmetic. The manuscript already states many of them explicitly. The research seed remains publishable with this narrow framing, and the original adversarial example should remain beside the added game.

## Audit display note

The exact audit API now correctly preserves a singleton feasible interval [5/6,5/6]. Its convenience float lower and upper endpoints can display in reversed order because the upper endpoint is conservatively rounded down. Exact fields remain authoritative and the sampler accepts them. Render user-facing intervals from the rational strings; never infer feasibility by re-comparing the convenience floats. This documented numerical distinction is sufficient for the research interface and does not require weakening any budget comparison.

## Updated assent

The mathematical reviewer continues to assent to the curated research seed, now including the one-step correction game. No new blocking arithmetic defect was found. This addition strengthens the packet by making an incentive vulnerability executable while retaining its premises and the simple uniform-allocation baseline.
