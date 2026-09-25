from fractions import Fraction as F
from itertools import product
import unittest
from correlated_checks import false_clear, all_outcomes, family_clear, best_allocation, shopping, shopping_shared, tv


class Counterexamples(unittest.TestCase):
    def test_latent_enumeration(self):
        for f,p,k in product((F(0),F(1,10),F(1)), (F(0),F(1,5),F(1)), range(7)):
            masses = all_outcomes(f,p,k)
            self.assertEqual(sum(masses.values()), 1)
            self.assertEqual(masses[(1,)*k], false_clear(f,p,k))

    def test_distribution_free_bound_is_sharp(self):
        for e in (F(0),F(1,10),F(1)):
            masses = all_outcomes(e,0,5)
            for i in range(5):
                self.assertEqual(sum(m for bits,m in masses.items() if bits[i]),e)
            self.assertEqual(masses[(1,)*5],e)

    def test_no_checks_is_no_evidence(self):
        self.assertEqual(false_clear(F(1,10),F(1,5),0),1)
        self.assertEqual(family_clear([(F(1,10),F(1,5))],[0]),1)

    def test_clone_floor_does_not_vanish(self):
        self.assertGreaterEqual(false_clear(F(1,10),F(1,5),100),F(1,10))
        self.assertLess(false_clear(F(1,10),F(1,5),1)**100,F(1,10**50))

    def test_diversification_optimum(self):
        families=[(F(1,10),F(1,5))]*2
        risk,a=best_allocation(families,6)
        self.assertEqual(a,(3,3))
        self.assertEqual(risk,F(17956,1562500))
        self.assertLess(risk,false_clear(F(1,10),F(1,5),6))

    def test_shopping_independent_paths(self):
        q=F(1,10)
        for n in range(7):
            enumerated=sum(q**sum(bits)*(1-q)**(n-sum(bits)) for bits in product((0,1),repeat=n) if any(bits))
            self.assertEqual(enumerated,shopping(q,n))
        self.assertGreater(shopping(q,50),F(99,100))

    def test_shared_blindspot_attempts(self):
        f,p=F(1,10),F(1,5)
        self.assertEqual(shopping_shared(f,p,2,0),0)
        self.assertEqual(shopping_shared(f,p,2,1),false_clear(f,p,2))
        for trials in range(1,5):
            residual=sum(p**(2*sum(bits))*(1-p**2)**(trials-sum(bits)) for bits in product((0,1),repeat=trials) if any(bits))
            self.assertEqual(shopping_shared(f,p,2,trials),f+(1-f)*residual)
        self.assertLess(shopping_shared(f,p,2,5),shopping(false_clear(f,p,2),5))

    def test_tv_certification_bound_all_rules(self):
        good=(F(9,10),F(1,10)); bad=(F(4,5),F(1,5))
        for accept in product((F(0),F(1,2),F(1)),repeat=2):
            difference=sum((g-b)*a for g,b,a in zip(good,bad,accept))
            self.assertLessEqual(difference,tv(good,bad))
        self.assertEqual(tv(good,bad),F(1,10))
        self.assertEqual(tv(good,good),0)

    def test_invalid_input(self):
        for f,p,k in ((-1,0,2),(0,2,2),(0,0,-1),(0,0,True),(0,0,1.5)):
            with self.assertRaises(ValueError):false_clear(f,p,k)
        with self.assertRaises(ValueError):tv([F(1,2)],[1])
        with self.assertRaises(ValueError):family_clear([(0,0)],[])

if __name__=='__main__':unittest.main()
