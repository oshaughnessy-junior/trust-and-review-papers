import math
import random
import unittest

from dynamics import (assignment, effective_reviewers, imported_mass,
                      reconsideration_load, stationary, trajectory)


class ModelTests(unittest.TestCase):
    def test_block_formula_against_iteration(self):
        rng = random.Random(20260925)
        for _ in range(80):
            a,e,g,r = rng.random()*.98,rng.random(),rng.random(),rng.random()
            actual = stationary([[1-e,e],[g,1-g]],[1-r,r],a)[1]
            self.assertAlmostEqual(actual,imported_mass(a,e,g,r),places=10)

    def test_multinode_row_cap_bound(self):
        rng = random.Random(529)
        for _ in range(60):
            n,h,e,a = 9,4,rng.random()*.15,.85
            matrix = []
            for i in range(n):
                row=[rng.random() for _ in range(n)]
                if i<h:
                    crossing=e*rng.random()
                    hs,xs=sum(row[:h]),sum(row[h:])
                    row=[v*(1-crossing)/hs for v in row[:h]]+[v*crossing/xs for v in row[h:]]
                else:
                    row=[v/sum(row) for v in row]
                matrix.append(row)
            p=stationary(matrix,[1/h]*h+[0]*(n-h),a)
            self.assertLessEqual(sum(p[h:]),imported_mass(a,e)+1e-10)

    def test_small_raw_capacity_is_not_transition_cap(self):
        # Sole outgoing raw edge of weight .001 becomes probability 1.
        p=stationary([[0,1],[0,1]],[1,0],.85)
        self.assertAlmostEqual(p[1],.85)
        self.assertGreater(p[1],100*imported_mass(.85,.001))

    def test_feedback_stability_and_symmetry_breaking(self):
        for beta,stable in [(1,True),(4,False)]:
            x=trajectory([.501,.499],beta,1,.1,[0,0],steps=12000)
            if stable:
                self.assertLess(abs(x[0]-.5),1e-9)
            else:
                self.assertGreater(x[0],.9)
        # High routing sensitivity alone cannot reinforce x when chi=0.
        x=trajectory([.9,.1],100,0,0,[0,0])
        self.assertLess(abs(x[0]-.5),1e-9)

    def test_feedback_jacobian(self):
        k,beta,chi,zeta=4,3.7,.8,.15
        h=1e-6
        x=[1/k]*k
        xp=x[:]; xp[0]+=h; xp[1]-=h
        f0=assignment(x,beta,chi,zeta,[0]*k)
        f1=assignment(xp,beta,chi,zeta,[0]*k)
        self.assertAlmostEqual((f1[0]-f0[0])/h,(1-zeta)*beta*chi/k,places=6)

    def test_review_and_cascade_limits(self):
        self.assertEqual(effective_reviewers(100,1),1)
        self.assertEqual(effective_reviewers(100,0),100)
        self.assertAlmostEqual(reconsideration_load(2,.2),5/3)
        self.assertTrue(math.isinf(reconsideration_load(2,.6)))
        self.assertAlmostEqual(reconsideration_load(2,.6,.5),2.5)

    def test_invalid_inputs(self):
        for v in [math.nan,math.inf,-.1,1.1]:
            with self.assertRaises(ValueError): imported_mass(.85,v)
        with self.assertRaises(ValueError): stationary([[1]],[1],1)
        with self.assertRaises(ValueError): effective_reviewers(0,.5)
        with self.assertRaises(ValueError): assignment([1,1],1,.5,.1,[0,0])


if __name__ == '__main__':
    unittest.main()
