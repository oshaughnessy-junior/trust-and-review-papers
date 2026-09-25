import itertools
from fractions import Fraction
import unittest
from allocation import (PAIRS,balanced_assignment,null_distribution,sharp_null_test,
                        design_power,toy_potential_outcomes,missing_effect_bounds)


class DesignTests(unittest.TestCase):
    def test_assignment_balance_uniqueness_reproducibility(self):
        blocks=[[f'unit-{b}-{i}' for i in range(4)] for b in range(4)]
        a=balanced_assignment(blocks,17)
        self.assertEqual(a,balanced_assignment(blocks,17))
        for b in range(4):self.assertEqual(sum(r['arm']=='card' for r in a if r['block']==b),2)
        with self.assertRaises(ValueError):balanced_assignment([['a']*4],1)

    def test_convolution_against_independent_label_enumeration(self):
        blocks=((0,0,1,1),(0,1,1,1),(0,0,0,1))
        direct={}
        for assignment in itertools.product(PAIRS,repeat=3):
            S=sum(block[i] for block,pair in zip(blocks,assignment) for i in pair)
            direct[S]=direct.get(S,0)+1
        self.assertEqual(dict(null_distribution(tuple(sum(b) for b in blocks))),direct)
        self.assertEqual(sum(direct.values()),6**3)

    def test_test_is_exact_under_sharp_null(self):
        # For each finite null table, fraction of possible assignments rejected <=alpha.
        for blocks in (((0,0,1,1),)*2,((0,0,1,1),)*4,((0,0,0,0),(1,1,1,1))):
            result=design_power(blocks,blocks)
            self.assertLessEqual(result['power'],Fraction(1,20))
            self.assertEqual(result['average_effect'],0)

    def test_complement_symmetry_and_constant_outcomes(self):
        blocks=((0,0,1,1),(0,1,1,1));assignment=((0,1),(0,2))
        complement=tuple(tuple(i for i in range(4) if i not in pair) for pair in assignment)
        a=sharp_null_test(blocks,assignment);b=sharp_null_test(blocks,complement)
        self.assertEqual(a['difference_in_adequacy'],-b['difference_in_adequacy'])
        self.assertEqual(a['two_sided_sharp_null_p'],b['two_sided_sharp_null_p'])
        self.assertEqual(sharp_null_test(((1,1,1,1),),((0,1),))['two_sided_sharp_null_p'],1)

    def test_potential_outcome_family_effect(self):
        for benefit in range(5):
            y0,y1=toy_potential_outcomes(8,benefit)
            result=design_power(y0,y1)
            self.assertEqual(result['average_effect'],Fraction(benefit,8))
            self.assertEqual(result['assignments'],36)

    def test_missing_bounds_match_exhaustive_completions(self):
        lo,hi=missing_effect_bounds(2,3,4,1,2,4)
        values=[Fraction(2+a,4)-Fraction(1+b,4) for a in range(2) for b in range(3)]
        self.assertEqual(lo,min(values));self.assertEqual(hi,max(values))

    def test_missing_bounds_are_not_causal_effect_bounds(self):
        # All potential outcomes are unchanged: true finite-population ATE is zero.
        # Chance assignment selects the two successes in each block for treatment.
        y0=((0,0,1,1),)*2;y1=y0
        true_effect=Fraction(sum(map(sum,y1))-sum(map(sum,y0)),8)
        bounds=missing_effect_bounds(4,4,4,0,4,4)
        self.assertEqual(true_effect,0)
        self.assertEqual(bounds,(Fraction(1),Fraction(1)))
        self.assertEqual(sharp_null_test(y0,((2,3),(2,3)))['difference_in_adequacy'],1)
        self.assertGreater(sharp_null_test(y0,((2,3),(2,3)))['two_sided_sharp_null_p'],Fraction(1,20))

    def test_input_validation(self):
        with self.assertRaises(ValueError):sharp_null_test(((True,0,1,1),),((0,1),))
        with self.assertRaises(ValueError):sharp_null_test(((0,0,1,1),),((0,0),))
        with self.assertRaises(ValueError):design_power(((0,0,1,1),)*7,((0,0,1,1),)*7)
        with self.assertRaises(ValueError):missing_effect_bounds(5,3,4,1,2,4)


if __name__=='__main__':unittest.main()
