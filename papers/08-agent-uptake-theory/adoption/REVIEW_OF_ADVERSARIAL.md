# Independent review of correlated-check theory

Reviewer: adoption-theory agent, 25 September 2026. Internal cross-review within
one orchestration; not external peer review. Reviewed `adversarial/manuscript.md`,
`correlated_checks.py`, and `test_correlated_checks.py`. Did not modify those files.

**Disposition:** no mathematical or implementation blocker found within the
stated synthetic scope. Nine author tests pass. Additional independent probes
verified nine latent-correlation parameter pairs, 14 heterogeneous allocation
cases comparing exact-budget optimization against all allocations costing at most
the budget, and 27 randomized decision rules on a three-transcript distribution.

## Concrete findings

1. **A1 correlation formula is correct, including its nondegeneracy restriction.**
   Direct joint-state calculation gives covariance f(1-f)(1-p)^2 and variance
   e(1-e). The resulting f(1-p)/e expression requires 0<e<1, as stated. At p=1
   the correlation is undefined, not zero; the manuscript correctly excludes it.
   The k=0 implementation returns one, consistent with the empty-intersection
   event; the theorem explicitly begins at k=1.
2. **A2 is sharp and does not yield posterior truth probabilities.** The identical
   Bernoulli construction attains the marginal upper bound. The explicit warning
   about prevalence and valid-case behavior is consequential and should remain.
3. **A3 correctly bounds a bounded randomized decision rule.** The positive-part
   proof does not require deterministic acceptance. The three-transcript probes
   supplement the author's two-transcript test. This is a statement about a pair
   of observable distributions, not proof that any particular agent platform's
   transcripts are indistinguishable; that hypothesis remains to be established.
4. **Allocation scope is narrower than the phrase 'all feasible allocations'.**
   Code enumerates allocations summing exactly to budget, whereas readers may
   understand feasible as summing at most to budget. The reported minimum is still
   correct: f+(1-f)p^k is nonincreasing in k for the admitted probability range,
   so unused budget can always be filled without increasing risk. Suggest adding
   this one-sentence justification or describing the enumeration as exact-budget.
   This is a documentation improvement, not a numerical blocker.
5. **Selective release formulas respect their distinct latent scopes.** IID fresh
   panels and a claim-level shared blind spot produce different formulas. The
   manuscript correctly refuses to infer complete attempts from service-local logs.
6. **Persisted numbers are decimal projections.** Calculations use Fractions but
   `results.json` converts them to floats. This does not damage the demonstrated
   inequalities or tests; exact numerators/denominators would make durable result
   audits easier. Avoid describing the JSON itself as lossless exact arithmetic.

## Integration challenge to both notes

Neither declared independence nor correlated-error theory supplies the adoption
model's standalone utility h. The joint experiment needs an evaluator-controlled
fault oracle, unaffected negative controls, the same input information for the
simple baseline, and total effort accounting. A higher receipt count or agreement
rate cannot stand in for fault detection, posterior correctness, or saved labor.
Conversely, fault-detection benefit does not establish willingness to integrate:
entry cost and post-support continuation must be measured separately.

The strongest combined next claim is therefore experimental: whether a versioned
reliance adapter catches specified injected failures at acceptable total cost and
whether an independent operator chooses to use it again. Neither note establishes
that empirical result yet.
