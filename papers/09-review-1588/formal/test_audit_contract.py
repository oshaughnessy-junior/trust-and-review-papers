from fractions import Fraction as F
from itertools import product
import unittest
from audit_contract import cap,interval,direct_weak_best,hard_lottery

class FormalAudit(unittest.TestCase):
    def test_independent_utility_grid_all_degeneracies(self):
        # 3^3 * 2^3 * 2 * 2 = 864 parameter cases, each at five q values.
        for alpha,beta,loss,c,R,u,a,kind in product((F(0),F(1,2),F(1)),(F(0),F(1,2),F(1)),(F(0),F(1,2),F(1)),(F(0),F(1,2)),(F(1,2),F(1)),(F(0),F(1,2)),(F(0),F(1)),('expected','hard')):
            result=interval(c,R,loss,alpha,beta,u,3,a,F(3,2),kind)
            for q in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
                in_result=result is not None and result[0]<=q<=result[1]
                direct=direct_weak_best(q,c,R,loss,alpha,beta,u) and q<=cap(3,a,F(3,2),kind)
                self.assertEqual(in_result,direct)
    def test_ratio_proposition_non_degenerate(self):
        values=interval(F(1,5),1,2,F(1,50),F(4,5),F(1,10),100,F(1,10),2,'expected')
        self.assertEqual(values,(F(5,39),F(1,5)))
    def test_hard_subset_is_expected_feasible(self):
        for n,a,budget in product(range(1,5),(F(0),F(1,2),F(1)),(F(0),F(1,2),F(3,2),F(10))):
            self.assertLessEqual(cap(n,a,budget,'hard'),cap(n,a,budget,'expected'))
    def test_no_discrimination_positive_effort(self):
        for loss,alpha,beta in ((0,0,1),(1,0,0),(1,F(1,2),F(1,2)),(1,1,0)):
            self.assertIsNone(interval(1,5,loss,alpha,beta,0,3,0,0,'expected'))
    def test_negative_discrimination_zero_effort(self):
        self.assertEqual(interval(0,1,1,1,0,0,3,1,3,'hard'),(F(0),F(0)))
    def test_zero_false_positive_constant_participation(self):
        self.assertEqual(interval(F(1,2),1,1,0,1,F(1,2),3,0,0,'hard'),(F(1,2),F(1)))
        self.assertIsNone(interval(F(1,2),1,1,0,1,1,3,0,0,'expected'))
    def test_free_audit_does_not_remove_effort_or_participation(self):
        self.assertEqual(cap(3,0,0,'hard'),1)
        self.assertIsNone(interval(1,0,1,0,1,0,3,0,0,'hard'))
    def test_expected_q_half_hard_q_third(self):
        self.assertEqual(cap(3,1,F(3,2),'expected'),F(1,2))
        self.assertEqual(cap(3,1,F(3,2),'hard'),F(1,3))
        with self.assertRaises(ValueError):hard_lottery(3,F(1,2),1,F(3,2))
        # Independent Bernoulli(.5) spends above1.5 whenever >=2 audits: .5.
        exceed=sum(F(1,8) for bits in product((0,1),repeat=3) if sum(bits)>F(3,2))
        self.assertEqual(exceed,F(1,2))
    def test_mixed_hard_lottery_pathwise_and_marginals(self):
        for n in range(1,6):
            for k in range(n+1):
                for target in {F(k),max(F(0),F(k)-F(1,2))}:
                    q=target/n;law=hard_lottery(n,q,1,k)
                    self.assertEqual(sum(law.values()),1)
                    self.assertTrue(all(len(s)<=k for s in law))
                    for actor in range(n):self.assertEqual(sum(p for s,p in law.items() if actor in s),q)
    def test_budget_can_change_feasibility_not_just_endpoint(self):
        args=(F(2,5),2,1,0,1,0,3,1,F(3,2))
        self.assertEqual(interval(*args,'expected'),(F(2,5),F(1,2)))
        self.assertIsNone(interval(*args,'hard'))
    def test_invalid_inputs(self):
        for n in (0,True,1.5):
            with self.assertRaises(ValueError):cap(n,1,1,'hard')
        with self.assertRaises(ValueError):cap(3,1,1,'ambiguous')
        with self.assertRaises(ValueError):hard_lottery(3,F(-1),1,1)

if __name__=='__main__':unittest.main()
