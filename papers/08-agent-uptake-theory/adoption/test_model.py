import unittest
from fractions import Fraction as F
from itertools import product
from model import Game, fixtures

class ExactTests(unittest.TestCase):
    def test_exhaustive_two_actor_extrema(self):
        # Independent direct inequalities versus dynamics over 81 exact games.
        for a,b,w,v in product((F(-1,2),F(0),F(1,2)),repeat=4):
            g=Game((a,b),((0,abs(w)),(abs(v),0)))
            fixed=[x for x in product((0,1),repeat=2)
                   if x==(int(a+abs(w)*x[1]>0),int(b+abs(v)*x[0]>0))]
            lo,lc=g.orbit((0,0)); hi,hc=g.orbit((1,1))
            self.assertEqual(len(lc),1); self.assertEqual(len(hc),1)
            self.assertLessEqual(len(lo),3); self.assertLessEqual(len(hi),3)
            for e in fixed:
                self.assertTrue(all(l<=x<=h for l,x,h in zip(lc[0],e,hc[0])))

    def test_potential_equals_unilateral_gain(self):
        for a,b,w in product((F(-1),F(0),F(2)),repeat=3):
            g=Game((a,b),((0,w),(w,0)))
            for state in g.states():
                for i in range(2):
                    changed=list(state); changed[i]=1-state[i]
                    gain=(1-2*state[i])*g.margins(state)[i]
                    self.assertEqual(g.potential(changed)-g.potential(state),gain)

    def test_standalone_cascade(self):
        path,cycle=fixtures()['standalone'].orbit((0,0,0))
        self.assertEqual(path,[(0,0,0),(1,0,0),(1,1,0),(1,1,1)])
        self.assertEqual(cycle,[(1,1,1)])

    def test_synchronous_mixed_cycle(self):
        self.assertEqual(fixtures()['coordination'].orbit((1,0))[1],[(1,0),(0,1)])

    def test_seed_and_retention(self):
        self.assertEqual(fixtures()['coordination'].cheapest_stable_full_seed((3,1)),(1,(1,)))
        g=fixtures()['no_retention']
        self.assertEqual(g.orbit((0,0),(0,))[1],[(1,1)])
        self.assertEqual(g.orbit((1,1))[1],[(0,0)])
        self.assertIsNone(g.cheapest_stable_full_seed((1,1)))

    def test_congestion_breaks_bottom_convergence(self):
        g=fixtures()['congestion']
        self.assertEqual(g.orbit((0,0))[1],[(0,0),(1,1)])
        self.assertEqual(g.equilibria(),[(0,1),(1,0)])

    def test_zero_tie(self):
        self.assertEqual(Game((0,),((0,),)).response((1,)),(0,))

    def test_invalid(self):
        with self.assertRaises(ValueError): Game((1,),((1,),))
        with self.assertRaises(ValueError): Game((float('nan'),),((0,),))
        with self.assertRaises(ValueError): Game((1,1),((0,),))
        with self.assertRaises(ValueError): fixtures()['congestion'].cheapest_stable_full_seed((1,1))
        for costs in ((float('nan'),1),(1.0,1),(True,1)):
            with self.assertRaises(ValueError): fixtures()['coordination'].cheapest_stable_full_seed(costs)
        with self.assertRaises(ValueError): fixtures()['coordination'].potential((1,))
        with self.assertRaises(ValueError): fixtures()['coordination'].potential((1,2))

if __name__=='__main__': unittest.main()
