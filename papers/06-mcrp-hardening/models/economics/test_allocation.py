import math
import unittest
from run import water_fill, benefit

class AllocationTests(unittest.TestCase):
    def test_high_budget_log_price(self):
        self.assertAlmostEqual(water_fill([1],[1],100)[0],100)
        self.assertAlmostEqual(water_fill([1e-200],[1e-200],100)[0],100)
    def test_flat_and_mixed_objective(self):
        self.assertEqual(water_fill([1,2],[0,0],100),[0,0])
        self.assertEqual(water_fill([0,2],[1,0],100,[1,2]),[1,2])
        self.assertEqual(water_fill([0,2],[1,1],100),[0,100])
    def test_invalid_inputs(self):
        for args in [([1,2],[1],1),([],[],1),([1],[-1],1),([math.nan],[1],1),([1],[1],-1),([1],[1],1,[2]),([1],[1],1,[0,0])]:
            with self.assertRaises(ValueError): water_fill(*args)
    def test_priority_reversal_negative_control(self):
        allocation=water_fill([100,1],[1,1],1)
        self.assertLess(benefit([1,100],[1,1],allocation),benefit([1,100],[1,1],[.5,.5]))
    def test_active_set_example(self):
        h=water_fill([10,4,1],[1,.5,1],4)
        self.assertAlmostEqual(sum(h),4)
        self.assertAlmostEqual(benefit([10,4,1],[1,.5,1],h),11.299328740623613)

if __name__=='__main__':unittest.main()
