import math
import unittest
from dataclasses import replace
from models.ecology.correction_game import Game,outcome,updated_scores

class CorrectionGameTests(unittest.TestCase):
    def test_author_credit_profitable_despite_social_loss(self):
        r=outcome()
        self.assertTrue(r['author_manufacture_profitable'])
        self.assertGreater(r['incremental_social_cost_proxy_if_repaired'],0)
    def test_repairer_only_blocks_author_not_coalition(self):
        r=outcome(policy='repairer_only')
        self.assertFalse(r['author_manufacture_profitable'])
        self.assertTrue(r['coalition_manufacture_profitable'])
    def test_no_credit_baseline(self):
        r=outcome(policy='no_correction_credit')
        self.assertEqual(r['author_attention_gain'],0)
        self.assertFalse(r['author_manufacture_profitable'])
        self.assertFalse(r['coalition_manufacture_profitable'])
    def test_independent_closed_form_oracle(self):
        g=Game();r=outcome(g)
        # Two rewarded actors at score mu, third zero, starting all equal.
        p=g.exploration/3+(1-g.exploration)*math.exp(g.beta*g.memory)/(2*math.exp(g.beta*g.memory)+1)
        self.assertAlmostEqual(r['manufactured_probabilities_if_repaired'][0],p)
        self.assertAlmostEqual(r['author_deviation_gain_if_repaired'],g.attention_value*(p-1/3)-g.manufacture_cost-g.author_repair_share*g.repair_units*g.effort_utility_per_unit)
    def test_capacity_and_enforcement_bounds(self):
        self.assertFalse(outcome(replace(Game(),repair_capacity=15))['author_manufacture_profitable'])
        r=outcome(replace(Game(),intent_detection_probability=.5,enforceable_loss=50))
        self.assertFalse(r['author_manufacture_profitable']);self.assertFalse(r['coalition_manufacture_profitable'])
    def test_attention_is_zero_sum(self):
        r=outcome()
        self.assertAlmostEqual(sum(r['manufactured_probabilities_if_repaired']),1)
        self.assertAlmostEqual(sum(r['clean_probabilities']),1)
        r=outcome(replace(Game(),scores=(0.,0.)),policy='repairer_only')
        self.assertAlmostEqual(r['coalition_attention_gain'],0)
    def test_pure_exploration_removes_this_reward_channel(self):
        r=outcome(replace(Game(),exploration=1))
        self.assertEqual(r['author_attention_gain'],0)
        self.assertEqual(r['coalition_attention_gain'],0)
    def test_invalid_parameters(self):
        for g in [replace(Game(),beta=-1),replace(Game(),scores=(float('nan'),0)),replace(Game(),memory=2),replace(Game(),repair_units=-1),replace(Game(),coalition_repair_share=.01)]:
            with self.assertRaises(ValueError):outcome(g)

if __name__=='__main__':unittest.main()
