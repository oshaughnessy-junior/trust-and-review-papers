# Conditional mathematical models

Run from the repository root with Python 3.10+ (standard library only):

```sh
python3 -m unittest discover -s papers/07-release-packet/models/math -p 'test_*.py' -v
python3 papers/07-release-packet/models/math/run_experiments.py
```

Read [math-foundations.md](../../manuscripts/math-foundations.md) for definitions,
proofs, caveats and a claim ledger. These are synthetic modeling primitives, not
an operational protocol implementation. The adjacent agent simulator supplies the
behavioral event trace; no authority or production interface is implied here.

- `panel_distribution`: exact declared-group panel probabilities; compare uniform
  group-first selection with uniform feasible representative selection.
- `retry_summary`: offered/completed selection, bounded IID retries, unresolved
  probability and resource costs.
- `envelope`, `repair_bound`: verify a supplied common positive witness and bound
  expected cumulative weighted repair under stated conditional assumptions.
- `shared_capacity`: add commitments across lanes for each person/epoch; no skill,
  deadline or legal feasibility is inferred.
- `audit_interval`, `action_utilities`: one-shot effort, participation and funded
  audit comparison; not a repeated-game or institutional equilibrium.

`results/summary.json` records hashes, seeds and all four Monte Carlo cases.
CSV sweeps contain 12 panel, 20 retry, 42 repair and 41 audit rows (115 total).
Twenty-one tests include independent finite enumeration oracles and explicit
counterexamples. Monte Carlo intervals are pointwise nominal 95%; the Monte Carlo
request count is 80,000. No intervals represent human-behavior uncertainty.

`source-map.json` distinguishes primary source verification from self-contained
new derivations and prior dossier material. No remote source is fetched at run time.

Operational non-goals include identity verification, general feasible-panel
construction, capacity scheduling, complete dependency discovery, currentness
transport, authenticated authority, legal compliance and empirical validation.
Positive finite scalar input validation does not certify all floating-point
ranges; use the supplied toy range and fail explicitly on unsupported extensions.

RM-1 repair: `audit_interval` limits expected expenditure only; `hard_audit_interval` and `blinded_audit_sample` add a fixed-population identical-cost hard count cap. Concealment and actual audit delivery are external obligations.

Hard-audit endpoints use exact rational strings (`maximum_audit_exact`, `minimum_audit_exact`); supply these or `Fraction` inputs to the sampler. Decimal floats are interpreted through their printed decimal. The float upper display rounds down and is safe for the cap, but exact fields govern singleton feasibility.

### Displaying exact audit intervals

Use the rational `minimum_audit_exact` and `maximum_audit_exact` fields for
decisions and human-facing intervals. For a singleton `[5/6, 5/6]`, convenience
float endpoints can appear reversed because the upper display is rounded down.
Do not infer feasibility by comparing those floats; the exact fields and returned
feasibility result are authoritative, and the sampler accepts rational strings.
