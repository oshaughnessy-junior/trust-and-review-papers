# Closed-loop funded audit toy

Read [funded-audits.md](../../manuscripts/funded-audits.md).

```sh
python3 -m unittest discover -s papers/07-release-packet/models/funded_audits -p 'test_*.py' -v
python3 papers/07-release-packet/models/funded_audits/run_experiments.py
```

Python3.9+ standard library only. Eighteen tests,11 scenarios,20 seeds each,
220 run rows and11 complete illustrative traces. The existing math sampler is
imported; its digest is recorded alongside local source hashes.

Fixed ex-ante offers, concealed hard quota, all decisions committed before audit,
actual detection and fully collateralized toy losses. Refused selected slots are
unused; no silent quota redistribution. Separate token audit/reward budgets and
one person-hour ledger across review/audit roles. Shared roles audit another
person's work, never their own. Preflight capacity/independence/funding failures
return unavailable before offering; broken promises appear only under an explicit
negative-control flag.

Selection inclusion probability is k/N; executed-audit fraction among participants
is random and can differ per run. Its conditional marginal requires behavior
independent of concealed selection. No actual funds, sanctions, authenticated
identities or deployment authority exist. This is a standalone behavior/resource
model, not a replacement for the protocol runtime or a cooperation equilibrium.

Red review found that the first floating-hour ledger allowed positive work within a $10^{-12}$ tolerance above zero capacity. The repaired ledger uses exact decimal-rational reservation/debit arithmetic with no overspending tolerance. Regression tests reject positive tiny work against zero capacity and verify that .1 plus .2 exactly fills .3. The original source is preserved in `models/funded_audits/results/model-before-exact-ledger.txt`.

The red review also exposed binary-floating tie reversals between honest/shallow and honest/refusal utilities. Preferences now use exact decimal-rational arithmetic internally; output includes the exact advertised utilities. Regression tests preserve the specified refusal-first, then honest, then shallow tie rule. Token rewards and losses enter utility at a stipulated one-to-one marginal conversion, not an inferred welfare measure.
