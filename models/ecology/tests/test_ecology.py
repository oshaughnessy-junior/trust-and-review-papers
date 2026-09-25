import math
import unittest
from models.ecology.ecology import Config, Agent, AGENTS, probabilities, simulate

class EcologyTests(unittest.TestCase):
    def test_softmax_floor_and_shift_invariance(self):
        for beta in (0,1,1000):
            p=probabilities([0,.2,1],.15,beta)
            q=probabilities([13,13.2,14],.15,beta)
            self.assertAlmostEqual(sum(p),1)
            self.assertTrue(all(x>=.05-1e-15 for x in p))
            for a,b in zip(p,q):self.assertAlmostEqual(a,b)
    def test_uniform_endpoints(self):
        self.assertEqual(probabilities([1,9,20],1,10),[1/3]*3)
        self.assertEqual(probabilities([1,9,20],0,0),[1/3]*3)
    def test_invalid_inputs(self):
        for config in (Config(periods=0),Config(arrival=-.1),Config(audit_bias=2),Config(reinforcement=float('nan'))):
            with self.assertRaises(ValueError):simulate(config)
    def test_budget_conservation_independent_trajectory_sum(self):
        r=simulate(Config(seed=14,periods=15),trace=True)
        recomputed=[sum(h['spent'][i] for h in r['history']) for i in range(len(AGENTS))]
        self.assertEqual(recomputed,r['effort_by_group'])
        for h in r['history']:
            for a,spent,left in zip(AGENTS,h['spent'],h['remaining']):
                self.assertEqual(spent+left,a.capacity);self.assertGreaterEqual(left,0)
        c=r['counters']
        self.assertEqual(r['labor'],sum(c[k] for k in ('intake_labor','check_labor','audit_labor','repair_labor')))
        self.assertEqual(r['offered'],r['completed']+r['unresolved_offers'])
        self.assertEqual(r['completed'],c['correct_checks']+c['incorrect_checks'])
    def test_exogenous_streams_match_under_all_policies(self):
        r=[simulate(Config(seed=3,periods=15),policy) for policy in ('prestige','bounded','uniform')]
        self.assertEqual(len({x['exogenous_offer_sha256'] for x in r}),1)
        self.assertEqual(len({x['counters']['defects_offered'] for x in r}),1)
    def test_no_capacity_no_completed_work(self):
        agents=tuple(Agent(a.name,0,a.skills,a.volume,a.defect_rate,a.diligence) for a in AGENTS)
        r=simulate(Config(periods=5,arrival=1),agents=agents)
        self.assertEqual(r['labor'],0);self.assertEqual(r['completed'],0)
        self.assertEqual(r['offered'],r['unresolved_offers'])
    def test_zero_offers(self):
        r=simulate(Config(periods=10,arrival=0))
        self.assertEqual(r['labor'],0);self.assertEqual(r['offered'],0)
        self.assertIsNone(r['accuracy_among_completed'])
    def test_bounded_score_invariant(self):
        r=simulate(Config(seed=10,periods=50,memory=.7),trace=True)
        for row in r['history']:self.assertTrue(all(0<=s<=1 for s in row['scores']))
    def test_blind_common_cause_negative_control(self):
        agents=tuple(Agent(a.name,a.capacity,a.skills,a.volume,1,1) for a in AGENTS)
        r=simulate(Config(periods=10,arrival=.1,blind_probability=1,audit_probability=0),agents=agents)
        self.assertGreater(r['completed'],0)
        self.assertEqual(r['accuracy_among_completed'],0)
        self.assertEqual(r['counters']['defects_detected'],0)
        self.assertEqual(r['repair_backlog'],0) # Quiet repair queue conceals all misses.
    def test_reproducibility(self):
        self.assertEqual(simulate(Config(periods=7)),simulate(Config(periods=7)))

if __name__=='__main__':unittest.main()
