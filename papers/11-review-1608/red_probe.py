"""Separate exact oracles used in the internal red review; not external validation."""
from fractions import Fraction as F
from itertools import product
from extensions import common_w, max_common_audit, lottery_marginals


def run():
    audits = witnesses = products = 0
    half_steps = [F(x, 2) for x in range(5)]
    for a, b, budget in product(half_steps, half_steps, [F(x, 2) for x in range(7)]):
        # For two actors, either one is unaffordable, both fit, or only singletons fit.
        expected = F(0) if max(a, b) > budget else F(1) if a+b <= budget else F(1, 2)
        q, lottery = max_common_audit((a, b), budget)
        assert q == expected
        assert lottery_marginals((a, b), budget, lottery) == (q, q)
        audits += 1
    for vals, r, eps in product(product((F(0), F(1, 2), F(1)), repeat=4),
                                (F(0), F(1, 2), F(3, 4)),
                                (F(1, 10), F(1, 3), F(1, 2))):
        # Set w=(x,1-x) and intersect elementary scalar inequality intervals.
        a, b, c, d = vals
        lo, hi, feasible = eps, 1-eps, True
        for coefficient, rhs in ((a-b-r, -b), (c-d+r, r-d)):
            if coefficient > 0:
                hi = min(hi, rhs/coefficient)
            elif coefficient < 0:
                lo = max(lo, rhs/coefficient)
            elif rhs < 0:
                feasible = False
        feasible = feasible and lo <= hi
        w = common_w((((a, b), (c, d)),), r, eps)
        assert (w is not None) == feasible
        if w is not None:
            assert lo <= w[0] <= hi
        witnesses += 1
    matrices = (((F(1, 2), F(3, 5)), (0, 0)), ((0, 0), (F(3, 5), F(1, 2))))
    def multiply(a, b):
        return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    for length in range(1, 9):
        for sequence in product(matrices, repeat=length):
            matrix = ((1, 0), (0, 1))
            for item in sequence:
                matrix = multiply(matrix, item)
            assert max(map(sum, matrix)) <= F(11, 10)*F(3, 5)**(length-1)
            products += 1
    return {'audit_oracle_cases': audits, 'witness_interval_oracle_cases': witnesses,
            'stable_without_common_linear_w_products': products}


if __name__ == '__main__':
    print(run())
