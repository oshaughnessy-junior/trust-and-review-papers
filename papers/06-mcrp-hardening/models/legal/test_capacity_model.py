import math
import unittest
from capacity_model import backlog, bounded_appeal_cost, utilization

class CapacityTests(unittest.TestCase):
    def test_no_silent_epoch_loss(self):
        with self.assertRaises(ValueError): backlog([40,999999],[40])
    def test_critical_deterministic_load(self):
        self.assertEqual(backlog([40]*4,[40]*4),[0]*4)
    def test_invalid_values(self):
        for x in [-1,math.inf,math.nan,True]:
            with self.assertRaises(ValueError): backlog([x],[40])
        for p in [-.1,1.1,math.nan]:
            with self.assertRaises(ValueError): bounded_appeal_cost(30,p,1)
        for depth in [-1,1.5,True]:
            with self.assertRaises(ValueError): bounded_appeal_cost(30,.5,depth)
    def test_flood_and_sequential_updates(self):
        args=dict(initial_cost=30,appeal_cost=30,appeal_probability=.5,total_capacity=600,reserved_capacity=120)
        self.assertLess(utilization(4,overhead=30,**args),1)
        self.assertGreater(utilization(4,overhead=1030,**args),1)
        self.assertEqual(backlog([90]*8,[60]*8)[-1],240)

if __name__=='__main__':unittest.main()
