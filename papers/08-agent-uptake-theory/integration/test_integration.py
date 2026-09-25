import unittest
from fractions import Fraction as F
from itertools import product
from model import benefit,posterior,robust_benefit,scenarios

class IntegrationTests(unittest.TestCase):
    def test_direct_loss_enumeration(self):
        p=F(1,5);q0=F(1,3);q1=F(1,6);a0=F(1,20);a1=F(1,10)
        old=p*q0*100+(1-p)*a0*5
        new=p*q1*100+(1-p)*a1*5+F(2,3)
        self.assertEqual(benefit(p,q0,q1,a0,a1,100,5,0,F(2,3)),old-new)
    def test_negative_and_positive(self):
        rows=scenarios()['scenarios'];self.assertLess(F(rows[0]['net_benefit']),0);self.assertGreater(F(rows[1]['net_benefit']),0)
    def test_no_change_pays_cost(self):
        self.assertEqual(benefit(F(1,2),F(1,3),F(1,3),0,0,100,5,0,2),-2)
    def test_posterior_requires_base_rate(self):
        self.assertEqual(posterior(F(1,10),F(1,5),0),F(1,46));self.assertIsNone(posterior(0,0,1))
    def test_interval_extrema_cover_grid(self):
        box=[(F(0),F(1))]*5;lo,hi=robust_benefit(box,100,5,1,2)
        for point in product([F(0),F(1,2),F(1)],repeat=5):
            value=benefit(*point,100,5,1,2);self.assertLessEqual(lo,value);self.assertLessEqual(value,hi)
    def test_point_interval(self):
        v=[F(1,10),F(1,2),F(1,5),F(0),F(1,20)]
        x=benefit(*v,100,5,0,1);self.assertEqual(robust_benefit([(z,z) for z in v],100,5,0,1),(x,x))
    def test_invalid(self):
        for bad in [True,float('nan'),.1]:
            with self.assertRaises(ValueError):posterior(bad,0,0)
        with self.assertRaises(ValueError):robust_benefit([(1,0)]*5,1,1,0,0)
if __name__=='__main__':unittest.main()
