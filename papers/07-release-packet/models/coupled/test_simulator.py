from fractions import Fraction
from itertools import combinations
import random
import unittest
from simulator import Config, Ledger, distribution, draw_panel, descendants, run, one_request_oracle


class CoupledTests(unittest.TestCase):
    def test_exact_single_request_retry_oracle(self):
        probabilities={'A':Fraction(1),'B':Fraction(1,4),'C':Fraction(1)}
        reroll=one_request_oracle(Config(),probabilities)
        fixed=one_request_oracle(Config(retry='fixed_panel'),probabilities)
        self.assertEqual(reroll['completion'],Fraction(7,8))
        self.assertEqual(reroll['expected_attempts'],Fraction(7,4))
        self.assertEqual(reroll['risky_completed_share'],Fraction(5,6))
        self.assertEqual(fixed['completion'],Fraction(23,32))
        self.assertEqual(fixed['expected_attempts'],Fraction(15,8))
        self.assertEqual(fixed['risky_completed_share'],Fraction(101,138))

    def test_runtime_deterministic_oracle_all_complete(self):
        def complete(who,request,fatigue,rng):return 'honest',True,1.,{}
        for retry in ('reroll','fixed_panel'):
            cfg=Config(requests=1,capacity=20,retry=retry)
            expected=one_request_oracle(cfg,dict.fromkeys('ABC',Fraction(1)))
            for seed in range(20):
                result=run(cfg,seed,behavior=complete)
                self.assertEqual(result['counts']['completed_requests'],expected['completion'])
                self.assertEqual(result['counts']['selection_attempts'],expected['expected_attempts'])


    def test_atomic_failed_reservation_preserves_every_person(self):
        ledger=Ledger({'A':1,'B':0})
        self.assertIsNone(ledger.reserve({'A':1,'B':1}))
        self.assertEqual(ledger.used,{'A':0.,'B':0.})
        self.assertEqual(ledger.held,{'A':0.,'B':0.})
        self.assertEqual(ledger.holds,{})

    def test_partial_use_refund_and_shared_lanes(self):
        ledger=Ledger({'A':1})
        token=ledger.reserve({'A':1})
        self.assertIsNone(ledger.reserve({'A':.1}))
        ledger.settle(token,{'A':.25},'check')
        self.assertTrue(ledger.charge({'A':.75},'repair'))
        self.assertFalse(ledger.charge({'A':.01},'appeal'))
        self.assertEqual(ledger.used['A'],1)
        self.assertEqual(ledger.held['A'],0)
        with self.assertRaises(ValueError):ledger.settle(token,{},'check')

    def test_invalid_settlement_retains_hold(self):
        ledger=Ledger({'A':1});token=ledger.reserve({'A':1})
        with self.assertRaises(ValueError):ledger.settle(token,{'A':2},'check')
        self.assertIn(token,ledger.holds)
        self.assertEqual(ledger.used['A'],0)
        ledger.settle(token,{},'check')

    def test_exact_group_probability_and_enumeration_oracle(self):
        self.assertEqual(distribution(Config(clones=1)),distribution(Config(clones=100)))
        cfg=Config(policy='naive',clones=3)
        reps=['A']*3+['B','C']
        pairs=[tuple(sorted((a,b))) for a,b in combinations(reps,2) if a!=b]
        oracle={p:Fraction(pairs.count(p),len(pairs)) for p in set(pairs)}
        self.assertEqual(distribution(cfg),oracle)
        d=distribution(Config(policy='naive',clones=100))
        self.assertEqual(sum(p for panel,p in d.items() if 'A' in panel),Fraction(200,201))

    def test_full_trace_clone_invariance_for_group_first(self):
        # Counterfactual copies map to same people; integer lottery consumes same RNG.
        for seed in range(30):
            a=run(Config(clones=1),seed,True);b=run(Config(clones=100),seed,True)
            self.assertEqual(a['counts'],b['counts'])
            self.assertEqual(a['events'],b['events'])
            self.assertEqual(a['ledger'],b['ledger'])

    def test_conservation_across_policies_capacity_and_hidden_control(self):
        for policy in ('group_first','naive'):
            for retry in ('fixed_panel','reroll'):
                for capacity in (1,3,8):
                    for hidden in (False,True):
                        r=run(Config(policy=policy,retry=retry,capacity=capacity,hidden_control=hidden),17)
                        c=r['counts']
                        self.assertEqual(c['offered_requests'],c['completed_requests']+c['unresolved_requests'])
                        self.assertLessEqual(c['relied_requests'],c['completed_requests'])
                        self.assertTrue(all(x['used']<=x['capacity']+1e-12 and abs(x['held'])<1e-12 for x in r['ledger']))

    def test_fixed_panel_retries_do_not_reroll(self):
        r=run(Config(retry='fixed_panel'),17,True)
        selected={}
        for e in r['events']:
            if e['event']=='select':selected.setdefault(e['request'],set()).add(tuple(e['panel']))
        self.assertTrue(all(len(panels)==1 for panels in selected.values()))

    def test_reliance_filter_never_upgrades_completion(self):
        r=run(Config(reliance_filter='A_only',capacity=20),5)
        self.assertTrue(all(any(g.startswith('A') for g in x['declared_groups']) for x in r['receipts']))
        self.assertLessEqual(r['counts']['relied_requests'],r['counts']['completed_requests'])
        self.assertEqual(r['counts']['A_relied_panels'],r['counts']['relied_panels'])

    def test_dependency_oracle_and_repair_do_not_renew_authority(self):
        r=run(Config(capacity=30,reserve_repair=True),21)
        self.assertGreater(r['counts']['repaired_reliances'],0)
        self.assertGreater(r['counts']['unnoticed_affected_reliances'],0)
        for receipt in r['receipts']:
            if receipt['repair']=='check_completed':self.assertEqual(receipt['currentness'],'unresolved_material_change')
        self.assertEqual(descendants(0,[(0,1),(1,2),(2,0)]),{0,1,2})

    def test_hidden_control_shares_actual_capacity(self):
        r=run(Config(hidden_control=True,capacity=8),12,True)
        self.assertEqual({x['person'] for x in r['ledger']},{'A','B','C','steward'})
        self.assertTrue(any(e.get('group')=='A2' and e.get('true_person')=='A' for e in r['events']))
        self.assertLessEqual(r['counts']['true_independent_completed_panels'],r['counts']['completed_panels'])

    def test_invalid_behavior_cannot_complete_a_refusal(self):
        def bad(who,request,fatigue,rng):return 'refuse',True,.05,{}
        with self.assertRaises(ValueError):run(Config(requests=1),1,behavior=bad)
        def overflow(who,request,fatigue,rng):return 'honest',True,2.,{}
        with self.assertRaises(ValueError):run(Config(requests=1),1,behavior=overflow)
        with self.assertRaises(ValueError):one_request_oracle(Config(),{'A':-1,'B':-1,'C':-1})

    def test_input_validation(self):
        for kwargs in ({'clones':True},{'capacity':-1},{'retry':'unknown'},{'requests':0}):
            with self.assertRaises(ValueError):Config(**kwargs)
        with self.assertRaises(ValueError):Ledger({'A':float('nan')})


if __name__=='__main__':unittest.main()
