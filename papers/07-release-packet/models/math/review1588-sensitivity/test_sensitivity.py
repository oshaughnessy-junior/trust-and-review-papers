import unittest
from fractions import Fraction as F
from itertools import product,permutations,combinations
from sensitivity import *

class SensitivityTests(unittest.TestCase):
    def test_completion_odds_and_direction(self):
        for p,a,b in product((F(1,10),F(1,2)),(F(1,10),F(1,2),F(1)),(F(1,100),F(1,10),F(1))):
            share=completion(p,a,b,3,0,0)['risk_share']
            self.assertEqual(share/(1-share),p/(1-p)*a/b)
            self.assertEqual(share>p,a>b)
    def test_finite_paths_independent_oracle(self):
        p,a,b=F(1,10),F(1),F(1,100);s=p*a+(1-p)*b
        for L in range(1,6):
            paths=[(n,(1-s)**(n-1)*s) for n in range(1,L+1)]
            unresolved=(1-s)**L
            expected=sum(n*w for n,w in paths)+L*unresolved
            r=completion(p,a,b,L,F(1,5),F(2))
            self.assertEqual(expected,r['attempts'])
            self.assertEqual(r['cost'],F(1,5)*expected+F(2)*sum(w for n,w in paths))
    def test_undefined_and_extreme_completion(self):
        self.assertIsNone(completion(F(1,10),0,0,4,1,2)['risk_share'])
        self.assertEqual(completion(F(1,10),1,0,4,1,2)['risk_share'],1)
        self.assertEqual(completion(F(1,10),0,1,4,1,2)['risk_share'],0)
    def test_audit_interval_matches_utilities_on_grid(self):
        for alpha,beta,c,loss in product((F(1,50),F(3,10)),(F(2,5),F(4,5)),(F(1,10),F(2,5)),(F(1),F(4))):
            r=audit(alpha=alpha,beta=beta,c=c,F_loss=loss)
            for q in (F(i,20) for i in range(21)):
                honest=1-c-q*alpha*loss;shirk=1-q*beta*loss
                economic=honest>=shirk and honest>=F(1,10)
                self.assertEqual(r['effort_lower']<=q<=r['hard_upper'], economic and q<=F(1,5))
    def test_fractional_expected_budget_not_hard(self):
        r=results()['fractional_budget']
        self.assertEqual(r['effort_lower'],F(4,9));self.assertEqual(r['expected_upper'],F(1,2));self.assertEqual(r['hard_upper'],F(1,3))
        self.assertTrue(r['expected_feasible']);self.assertFalse(r['hard_feasible'])
    def test_sanction_independent_conflict(self):
        for loss in (F(1),F(2),F(8)):
            r=audit(R=F(2,5),alpha=F(3,10),F_loss=loss)
            self.assertEqual(r['participation_effort_margin'],F(-1,100))
            self.assertFalse(r['hard_feasible']);self.assertGreater(r['effort_lower'],r['participation_upper'])
    def test_common_robust_interval(self):
        r=results()['robust_box'];self.assertEqual(r['common_hard_lower'],F(5,33));self.assertEqual(r['common_hard_upper'],F(1,5))
        for c,al,be,f in product((F(1,10),F(3,20),F(1,5)),(F(1,100),F(1,40),F(1,25)),(F(7,10),F(4,5),F(9,10)),(F(2),F(5,2),F(3))):
            interval=audit(c=c,alpha=al,beta=be,F_loss=f)
            self.assertLessEqual(interval['effort_lower'],F(5,33));self.assertGreaterEqual(interval['hard_upper'],F(1,5))
    def test_panel_filters(self):
        groups=panel_fixture();conflicts=(frozenset({'A','B'}),frozenset({'C','D'}))
        panels=feasible(groups,('calibration','inference'),conflicts)
        self.assertEqual(panels,(('A','C'),('A','D'),('B','C')))
        # Independent ordered skill assignment, then pair deduplication.
        assignments={tuple(sorted((x.name,y.name))) for x,y in permutations(groups,2)
                     if 'calibration' in x.skills and 'inference' in y.skills and x.capacity and y.capacity
                     and frozenset((x.name,y.name)) not in conflicts}
        self.assertEqual(set(panels),assignments)
    def test_weighted_pushforward_explicit_representatives(self):
        groups=panel_fixture();panels=feasible(groups,('calibration','inference'),(frozenset({'A','B'}),frozenset({'C','D'})))
        q=distribution(groups,panels)
        self.assertEqual(q,{('A','C'):F(2,5),('A','D'):F(1,5),('B','C'):F(2,5)})
        for multiplicity in (1,10,100):
            counts={g.name:multiplicity if g.name=='A' else 1 for g in groups}
            pushed={s:F(0) for s in panels}
            for panel in panels:
                realizations=list(product(*(range(counts[g]) for g in panel)))
                for _ in realizations:pushed[panel]+=q[panel]/len(realizations)
            self.assertEqual(pushed,q)
        naive=distribution(groups,panels,{g.name:10 if g.name=='A' else 1 for g in groups})
        self.assertEqual(sum(v for p,v in naive.items() if 'A' in p),F(20,21))
    def test_empty_feasible_refuses(self):
        groups=panel_fixture();panels=feasible(groups,('unknown-skill',),())
        self.assertEqual(panels,());self.assertIsNone(distribution(groups,panels))
    def test_invalid(self):
        for kwargs in ({'alpha':0},{'F_loss':0},{'audit_cost':0},{'N':0},{'beta':F(1,100)}):
            with self.assertRaises(ValueError):audit(**kwargs)
        with self.assertRaises(ValueError): completion(True,1,1,1,0,0)
        with self.assertRaises(ValueError): feasible(panel_fixture(),('calibration',),(frozenset({'A','unknown'}),))

if __name__=='__main__':unittest.main()
