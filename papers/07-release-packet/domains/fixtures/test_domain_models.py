"""Independent hand-computed expectations and adverse-boundary regressions."""
import copy
from fractions import Fraction as F
import unittest

from domain_models import (biology_model, canonical_digest, economics_model,
                           fixtures, law_model, mixture, physics_model, schedule)
from replay_receipts import hidden_dependency_control, replay_case


class DomainModels(unittest.TestCase):
    def setUp(self):
        self.cases = {c["domain"]: c for c in fixtures()["cases"]}

    def test_shared_variance_exact_hand_calculation(self):
        r = physics_model(self.cases["physics"]["evidence"])
        self.assertEqual(F(r["shared_variance"]), F(101, 400))
        self.assertEqual(F(r["mistaken_variance"]), F(29, 1600))
        self.assertEqual(r["new_amplitude"], "10")

    def test_more_repeats_cannot_remove_shared_floor(self):
        e = copy.deepcopy(self.cases["physics"]["evidence"])
        for n in (1, 16, 1000000):
            e["n"] = n
            self.assertGreaterEqual(F(physics_model(e)["shared_variance"]), F(1, 4))

    def test_zero_shared_error_recovers_independent_formula(self):
        e = copy.deepcopy(self.cases["physics"]["evidence"])
        e["shared_sd"] = "0"
        r = physics_model(e)
        self.assertEqual(r["shared_variance"], r["mistaken_variance"])

    def test_distinct_biological_explanations_are_observationally_equal(self):
        r = biology_model(self.cases["biology"]["evidence"])
        self.assertEqual(r["rss_treatment_explanation"], "4")
        self.assertEqual(r["rss_batch_explanation"], "4")
        self.assertEqual(r["crossed_within_batch_differences"], ["1", "1"])
        self.assertFalse(r["separate_effect_identified_in_confounded_design"])

    def test_unconditional_error_mean_does_not_supply_conditional_exogeneity(self):
        # Independent counterexample: balanced T=B, epsilon=T-1/2.
        conditional_errors = {t: F(t) - F(1, 2) for t in (0, 1)}
        self.assertEqual(sum(conditional_errors.values()) / 2, 0)
        self.assertTrue(all(e != 0 for e in conditional_errors.values()))

    def test_same_crossed_observations_can_have_zero_causal_effect(self):
        # SCM: observed T=U and Y=10+2B+U; do(T) leaves U unchanged.
        def structural_y(batch, latent, intervention):
            return 10 + 2 * batch + latent
        observations = [[u, b, structural_y(b, u, u)] for b in (0, 1) for u in (0, 1)]
        self.assertEqual(observations, self.cases["biology"]["evidence"]["crossed_rows"])
        causal_effects = [structural_y(b, u, 1) - structural_y(b, u, 0)
                          for b in (0, 1) for u in (0, 1)]
        self.assertEqual(sum(causal_effects) / len(causal_effects), 0)

    def test_interaction_is_not_mislabeled_as_an_exact_additive_effect(self):
        case = copy.deepcopy(self.cases["biology"])
        case["evidence"]["crossed_rows"][-1][-1] = 15
        r = biology_model(case["evidence"])
        self.assertEqual(r["crossed_within_batch_differences"], ["1", "3"])
        self.assertEqual(r["crossed_average_contrast"], "2")
        self.assertFalse(r["crossed_exact_additivity"])
        self.assertIsNone(r["crossed_additive_effect"])
        replay = replay_case(case)
        self.assertEqual(replay["amended_calculation"], "2")
        self.assertEqual(replay["amended_scope"], ["arithmetic"])

    def test_transport_changes_estimand(self):
        r = economics_model(self.cases["economics"]["evidence"])
        self.assertEqual(r["trial_effect"], "8/5")
        self.assertEqual(r["target_effect_conditional_on_transport"], "2/5")
        self.assertEqual(r["adverse_completed_share"], "100/109")

    def test_equal_completion_preserves_offered_share(self):
        e = copy.deepcopy(self.cases["economics"]["evidence"])
        e["other_completion"] = e["adverse_completion"]
        self.assertEqual(economics_model(e)["adverse_completed_share"], "1/10")

    def test_final_reliance_can_select_again_after_completion(self):
        r = economics_model(self.cases["economics"]["evidence"])["separate_reliance_example"]
        self.assertEqual(r["completed_adverse_share"], "1/10")
        self.assertEqual(r["relied_adverse_share"], "1")

    def test_no_reliance_is_undefined_not_zero_adverse_share(self):
        e = copy.deepcopy(self.cases["economics"]["evidence"])
        e["reliance_selection"]["relied_adverse"] = 0
        self.assertIsNone(economics_model(e)["separate_reliance_example"]["relied_adverse_share"])

    def test_no_completions_is_undefined_not_zero(self):
        e = copy.deepcopy(self.cases["economics"]["evidence"])
        e["other_completion"] = e["adverse_completion"] = "0"
        self.assertIsNone(economics_model(e)["adverse_completed_share"])

    def test_missing_target_support_refused(self):
        with self.assertRaisesRegex(ValueError, "support missing"):
            mixture({"A": "2"}, {"A": "0.8", "C": "0.2"})

    def test_equal_aggregate_work_different_deadline_outcomes(self):
        r = law_model(self.cases["law"]["evidence"])
        self.assertEqual(sum(j["missed"] for j in r["fifo"]), 1)
        self.assertEqual(sum(j["missed"] for j in r["deadline_order"]), 0)
        self.assertEqual(sum(j["missed"] for j in r["infeasible_earliest_first"]), 1)

    def test_scheduler_cannot_drop_a_job_to_claim_success(self):
        with self.assertRaises(ValueError):
            schedule(self.cases["law"]["evidence"]["feasible_jobs"], ["A"])

    def test_digest_stable_under_mapping_order_but_changes_with_content(self):
        self.assertEqual(canonical_digest({"a": 1, "b": 2}), canonical_digest({"b": 2, "a": 1}))
        self.assertNotEqual(canonical_digest({"a": 1}), canonical_digest({"a": 2}))

    def test_all_replays_amend_then_support_a_new_version(self):
        for case in self.cases.values():
            with self.subTest(case=case["domain"]):
                r = replay_case(case)
                self.assertEqual(r["before"], "current_under_toy_policy")
                self.assertEqual(r["after_amendment"], "reconsideration_pending")
                self.assertEqual(r["new_version"], "current_under_toy_policy")

    def test_biology_and_law_unsafe_authority_upgrades_rejected(self):
        for domain in ("biology", "law"):
            self.assertIsNotNone(replay_case(self.cases[domain])["blocked_upgrade"])

    def test_amended_receipts_bind_recomputed_domain_results(self):
        expected = {"physics": "10", "biology": "1", "economics": "2/5", "law": True}
        for domain, value in expected.items():
            self.assertEqual(replay_case(self.cases[domain])["amended_calculation"], value)

    def test_hidden_dependency_is_a_recorded_known_failure(self):
        r = hidden_dependency_control(self.cases["physics"])
        self.assertEqual(r["states"]["declared"], "reconsideration_pending")
        self.assertEqual(r["states"]["hidden"], "current_under_toy_policy")
        self.assertEqual(r["recall"], "1/2")


if __name__ == "__main__":
    unittest.main()
