# Response to domain adversarial review

Author-lane response, 2026-09-25. The original adversarial report remains separate
in `../reviews/red-domains-law/`; this document does not speak for that reviewer.

| Finding | Revision | Evidence |
|---|---|---|
| D1: unconditional zero mean is insufficient | Biology explicitly requires conditional zero mean given treatment and batch for its conditional-mean identity; the balanced binary counterexample is displayed | `test_unconditional_error_mean_does_not_supply_conditional_exogeneity` |
| D2: crossed columns do not establish causation or exact additivity | Explicit structural causal countermodel; `additive_model_identification` replaces the ambiguous scope token; average contrast, exact-additivity flag and exact additive coefficient are separate outputs | `test_same_crossed_observations_can_have_zero_causal_effect`; `test_interaction_is_not_mislabeled_as_an_exact_additive_effect` |
| D2: interaction input mislabeled | Contrasts 1 and 3 yield average 2, false exact-additivity flag and null exact additive coefficient; actual replay narrows the amended scope to arithmetic | Same interaction regression exercises both oracle and receipt engine |
| D3: federal jurisdiction qualifier omitted | Law now refers to covered federal proceedings, subject to applicability and exceptions; source ledger retains the institutional scope | Official U.S. Courts pages rechecked; no live-case opinion claimed |
| D4: final reliance can select again | Added separate finite-count example: 10 adverse of 100 completed, all 10 relied upon, hence shares 0.1→1 | `test_final_reliance_can_select_again_after_completion`; undefined zero-reliance case also tested |
| D7: novice should see a completed card | Biology adds a worked four-sentence card and interaction answer key before requesting abstract protocol fluency | Teaching proposal only; no measured onboarding effect |

All 20 domain tests pass in the regenerated run. Original working numerical cases
retain their values. The more precise scope token is a fixture-schema change,
not a claim of public wire-protocol compatibility. Original unchecked causal and
institutional premises remain outside toy-engine authority.
