import itertools
import math
import random
import unittest
from fractions import Fraction
from protocol_math import (panel_distribution, inclusion, retry_summary, completion_bound, envelope,
    repair_bound, row_mul, shared_capacity, audit_interval, action_utilities, wilson,
    hard_audit_interval, blinded_audit_sample)


class PanelTests(unittest.TestCase):
    def test_clone_pushforward_invariance(self):
        reference = panel_distribution({'A':1,'B':1,'C':1,'D':1}, 2)
        for counts in itertools.product((1,2,7), repeat=4):
            actual = panel_distribution(dict(zip('ABCD', counts)), 2)
            self.assertEqual(reference, actual)

    def test_naive_matches_independent_representative_enumeration(self):
        counts = {'A':3,'B':2,'C':1}
        representatives = [(g,i) for g,n in counts.items() for i in range(n)]
        panels = [tuple(sorted((a[0],b[0]))) for a,b in itertools.combinations(representatives,2) if a[0] != b[0]]
        oracle = {p: Fraction(panels.count(p),len(panels)) for p in set(panels)}
        self.assertEqual(oracle, panel_distribution(counts, 2, 'naive'))
        self.assertEqual(inclusion(panel_distribution({'A':100,'B':1,'C':1},2,'naive'),'A'), Fraction(200,201))
        self.assertEqual(inclusion(panel_distribution({'A':100,'B':1,'C':1},2),'A'), Fraction(2,3))

    def test_hidden_control_breaks_declared_group_claim(self):
        honest = inclusion(panel_distribution({'A':1,'B':1,'C':1},2),'A')
        hidden = panel_distribution({'A1':1,'A2':1,'B':1,'C':1},2)
        any_a = sum(p for panel,p in hidden.items() if {'A1','A2'}.intersection(panel))
        self.assertGreater(any_a,honest)
        self.assertEqual(any_a,Fraction(5,6))
        self.assertEqual(hidden[('A1','A2')],Fraction(1,6))

    def test_invalid_coverage_and_counts(self):
        for counts,size in [({'A':1},2),({'A':True},1),({'A':0},1),({},1),({'A':1},True)]:
            with self.assertRaises(ValueError): panel_distribution(counts,size)


class RetryTests(unittest.TestCase):
    def test_completion_envelope_is_tight_and_monotone(self):
        bound=completion_bound(.2,.8,.3)
        self.assertAlmostEqual(bound,retry_summary(.2,.8,.3,1)['completed_risk'])
        for p,a,b in itertools.product((0,.1,.2),(0,.4,.8),(.3,.6,1)):
            actual=retry_summary(p,a,b,1)['completed_risk']
            self.assertLessEqual(actual,bound+1e-14)
        for args in ((1,.8,.3),(.2,.8,0)):
            with self.assertRaises(ValueError): completion_bound(*args)

    def test_finite_tree_oracle(self):
        # Enumerate terminal paths, separately from the geometric formula.
        p,a,b,L = .2,.8,.3,4
        result = retry_summary(p,a,b,L,2,5)
        success, cost, attempts, risk = 0.,0.,0.,0.
        frontier = [(1.,0)]
        while frontier:
            mass,used = frontier.pop()
            if used == L:
                cost += mass*used*2
                attempts += mass*used
                continue
            for category,prob,completion in [('R',p,a),('O',1-p,b)]:
                done=mass*prob*completion
                success+=done; risk+=done*(category=='R')
                cost+=done*((used+1)*2+5); attempts+=done*(used+1)
                frontier.append((mass*prob*(1-completion),used+1))
        self.assertAlmostEqual(success,result['completion_probability'])
        self.assertAlmostEqual(cost,result['expected_cost'])
        self.assertAlmostEqual(attempts,result['expected_attempts'])
        self.assertAlmostEqual(risk/success,result['completed_risk'])

    def test_bias_persists_under_retry(self):
        for L in (1,2,10,100):
            r=retry_summary(.1,1,.01,L)
            self.assertAlmostEqual(r['completed_risk'], .1/.109)
        none=retry_summary(.1,0,0,9)
        self.assertIsNone(none['completed_risk'])
        self.assertEqual(none['expected_attempts'],9)
        self.assertEqual(none['unresolved_probability'],1)

    def test_accounting_and_bounds(self):
        for p,a,b in itertools.product((0,.3,1),repeat=3):
            r=retry_summary(p,a,b,5)
            self.assertAlmostEqual(r['completion_probability']+r['unresolved_probability'],1)
            self.assertAlmostEqual(r['expected_refusals']+r['completion_probability'],r['expected_attempts'])
        for bad in (-1,True,float('nan'),1.01):
            with self.assertRaises(ValueError): retry_summary(bad,.2,.5,2)


class RepairTests(unittest.TestCase):
    def test_arbitrary_switching_bound_by_exhaustive_sequences(self):
        family=[[[.2,.1],[.1,.4]],[[.1,.3],[.05,.2]]]
        w=[1,2]
        bound=repair_bound([1,0],family,w)
        for sequence in itertools.product(range(2), repeat=8):
            z=[1.,0.]; total=1.
            for generation,k in enumerate(sequence,1):
                z=row_mul(z,family[k]); weighted=sum(a*b for a,b in zip(z,w))
                self.assertLessEqual(weighted,.7**generation+1e-14)
                total+=weighted
            self.assertLessEqual(total,bound+1e-14)

    def test_stable_snapshots_unstable_switching(self):
        A=[[0,2],[0,0]]; B=[[0,0],[2,0]]
        self.assertEqual(row_mul(row_mul([1,0],A),A),[0,0])
        z=[1,0]
        for i in range(10): z=row_mul(z,[A,B][i%2])
        self.assertEqual(sum(z),1024)
        self.assertFalse(envelope([A,B],[1,1])['certified'])
        with self.assertRaises(ValueError): repair_bound([1,0],[A,B],[1,1])

    def test_failed_witness_does_not_prove_instability(self):
        A=[[0,2],[0,0]]
        self.assertFalse(envelope([A],[1,1])['certified'])
        self.assertTrue(envelope([A],[4,1])['certified'])

    def test_single_hour_single_ledger(self):
        rows=[('Ada','day1','review',3),('Ada','day1','audit',2),('Ada','day1','repair',4)]
        self.assertFalse(shared_capacity(rows,{('Ada','day1'):8})['feasible'])
        self.assertTrue(shared_capacity(rows,{('Ada','day1'):9})['feasible'])
        with self.assertRaises(ValueError): shared_capacity(rows,{})

    def test_input_shapes_and_nonnegative_entries(self):
        for family,w in [([[[.2]]],[0]),([[[.2,-1],[0,.2]]],[1,1]),([[[.2]]],[1,2]),([],[1])]:
            with self.assertRaises(ValueError): envelope(family,w)


class AuditTests(unittest.TestCase):
    def test_hard_cap_nonintegral_budget(self):
        expected=audit_interval(0,1,1,0,1,0,3,1,1.5)
        hard=hard_audit_interval(0,1,1,0,1,0,3,1,1.5)
        self.assertEqual(expected['maximum_audit'],.5)
        self.assertEqual(hard['maximum_audit'],1/3)
        with self.assertRaises(ValueError): blinded_audit_sample(3,.5,1,1.5,random.Random(1))
        self.assertEqual(hard_audit_interval(0,1,1,0,1,0,3,.1,.3)['maximum_audit_count'],3)

    def test_hard_endpoint_is_consumable_without_cap_tolerance(self):
        result=hard_audit_interval(0,1,1,0,1,0,6,1,5)
        self.assertEqual(result['maximum_audit_exact'],'5/6')
        for q in (result['maximum_audit'], result['maximum_audit_exact'], Fraction(5,6)):
            for seed in range(20):
                self.assertLessEqual(len(blinded_audit_sample(6,q,1,5,random.Random(seed))),5)
        with self.assertRaises(ValueError):
            blinded_audit_sample(6,'5000000000000000001/6000000000000000000',1,5,random.Random(0))

    def test_exact_singleton_feasibility_survives_float_display(self):
        result=hard_audit_interval('5/6',2,1,0,1,0,6,1,5)
        self.assertTrue(result['feasible'])
        self.assertEqual(result['minimum_audit_exact'],result['maximum_audit_exact'])
        self.assertEqual(len(blinded_audit_sample(6,result['maximum_audit_exact'],1,5,random.Random(0))),5)

    def test_fixed_size_exact_marginal_oracle(self):
        for n in range(2,8):
            for k in range(n+1):
                subsets=list(itertools.combinations(range(n),k))
                for i in range(n):
                    self.assertEqual(Fraction(sum(i in s for s in subsets),len(subsets)),Fraction(k,n))
        for seed in range(100):
            selected=blinded_audit_sample(10,.25,.1,.3,random.Random(seed))
            self.assertIn(len(selected),(2,3))
            self.assertEqual(len(selected),len(set(selected)))


    def test_interior_interval_agrees_with_utilities(self):
        result=audit_interval(.2,1,2,.02,.8,.1,100,.1,2)
        self.assertTrue(result['feasible'])
        lo,hi=result['minimum_audit'],result['maximum_audit']
        for q in (lo,(lo+hi)/2,hi):
            u=action_utilities(q,.2,1,2,.02,.8,.1)
            self.assertGreaterEqual(u['honest']+1e-12,max(u['shirk'],u['abstain']))
            self.assertLessEqual(q*100*.1,2+1e-12)
        below=action_utilities(lo/2,.2,1,2,.02,.8,.1)
        self.assertGreater(below['shirk'],below['honest'])

    def test_budget_and_participation_can_conflict(self):
        self.assertFalse(audit_interval(.2,1,2,.02,.8,.1,100,.1,1)['feasible'])
        self.assertFalse(audit_interval(.2,.3,2,.3,.8,.05,100,.1,10)['feasible'])
        self.assertFalse(audit_interval(.2,1,0,0,.8,0,1,1,1)['feasible'])

    def test_zero_effort_negative_discrimination_only_zero_audit(self):
        result=audit_interval(0,1,2,.8,.2,0,1,1,1)
        self.assertTrue(result['feasible'])
        self.assertEqual(result['maximum_audit'],0)

    def test_wilson_bounds(self):
        lo,hi=wilson(50,100)
        self.assertLess(lo,.5); self.assertGreater(hi,.5)
        self.assertEqual(wilson(0,100)[0],0)
        self.assertEqual(wilson(100,100)[1],1)
        with self.assertRaises(ValueError): wilson(101,100)


if __name__=='__main__': unittest.main()
