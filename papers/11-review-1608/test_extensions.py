import unittest
from fractions import Fraction as F
from extensions import common_w, max_common_audit, lottery_marginals, feasible_subsets


class Extensions(unittest.TestCase):
    def test_nonuniform_witness(self):
        m = (((0, 1), (0, 0)),)
        w = common_w(m, F(1, 2), F(1, 4))
        self.assertEqual(w, (F(2, 3), F(1, 3)))
        self.assertGreater(F(1, 2), F(1, 2)*F(1, 2))  # uniform w fails first row
        self.assertLessEqual(w[1], w[0]/2)

    def test_fixed_lp_failure_is_not_global_failure(self):
        m = (((0, 1), (0, 0)),)
        self.assertIsNone(common_w(m, F(1, 2), F(2, 5)))
        self.assertIsNotNone(common_w(m, F(1, 2), F(1, 4)))
        self.assertIsNone(common_w((((F(3, 4),),),), F(1, 2), F(1)))
        self.assertEqual(common_w((((F(3, 4),),),), F(4, 5), F(1)), (F(1),))

    def test_unstable_family_no_fixed_witness(self):
        self.assertIsNone(common_w((((0, 2), (0, 0)), ((0, 0), (2, 0))), F(9, 10), F(1, 100)))

    def test_multiple_regimes_certificate(self):
        family = (((F(1, 5), F(1, 10)), (F(1, 10), F(2, 5))),
                  ((F(1, 10), F(3, 10)), (F(1, 20), F(1, 5))))
        w = common_w(family, F(7, 10), F(1, 10))
        self.assertIsNotNone(w)
        for m in family:
            for i, row in enumerate(m):
                self.assertLessEqual(sum(x*y for x, y in zip(row, w)), F(7, 10)*w[i])

    def test_expected_cost_not_hard_feasibility(self):
        q, lottery = max_common_audit((2, 1), 2)
        self.assertEqual(q, F(1, 2))
        self.assertEqual(lottery_marginals((2, 1), 2, lottery), (q, q))
        self.assertLess(q, F(2, 3))  # expected expenditure alone allows 2/3
        self.assertEqual(max_common_audit((2, 2), 3)[0], F(1, 2))

    def test_nontrivial_grouped_lottery(self):
        q, lottery = max_common_audit((2, 1, 1), 2)
        self.assertEqual(q, F(1, 2))
        self.assertEqual(dict(lottery), {(0,): F(1, 2), (1, 2): F(1, 2)})

    def test_homogeneous_small_n_and_rounding(self):
        for n in range(1, 5):
            for budget in (F(0), F(1, 2), F(1), F(3, 2), F(2), F(9)):
                q, lottery = max_common_audit((1,)*n, budget)
                self.assertEqual(q, F(min(n, budget.numerator//budget.denominator), n))
                self.assertTrue(all(len(s) <= budget for s, p in lottery))

    def test_zero_and_unaffordable(self):
        self.assertEqual(max_common_audit((0, 0), 0)[0], 1)
        self.assertEqual(max_common_audit((3, 0), 2)[0], 0)
        self.assertEqual(max_common_audit((0, 1), 1)[0], 1)

    def test_thinning_any_lower_common_probability(self):
        q, lottery = max_common_audit((2, 1, 1), 2)
        mixed = tuple((s, p/3) for s, p in lottery) + (((), F(2, 3)),)
        self.assertEqual(lottery_marginals((2, 1, 1), 2, mixed), (q/3,)*3)

    def test_validation(self):
        for costs, budget in [((-1,), 1), ((1,), -1), ((1,)*5, 2), ((0.5,), 1)]:
            with self.assertRaises(ValueError):
                feasible_subsets(costs, budget)
        with self.assertRaises(ValueError):
            lottery_marginals((2, 1), 2, (((0, 1), F(1)),))
        with self.assertRaises(ValueError):
            common_w((((0, 1), (0, 0)),), F(1, 2), F(0))


if __name__ == '__main__':
    unittest.main()
