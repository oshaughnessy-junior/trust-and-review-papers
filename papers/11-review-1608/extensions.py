"""Bounded exact illustrations of standard finite linear-program geometry.

All inputs are asserted toy quantities, not learned resource or identity facts.
No solver dependency; deliberate small dimension caps prevent accidental scale claims.
"""
from fractions import Fraction as F
from itertools import combinations


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, F)):
        raise ValueError('use integer or Fraction inputs')
    return F(x)


def unique_solution(rows, rhs, columns):
    """Exact possibly overdetermined linear system; None unless uniquely soluble."""
    a = [[rational(x) for x in row] + [rational(b)] for row, b in zip(rows, rhs)]
    pivots = []
    top = 0
    for col in range(columns):
        pivot = next((i for i in range(top, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[top], a[pivot] = a[pivot], a[top]
        scale = a[top][col]
        a[top] = [x / scale for x in a[top]]
        for i in range(len(a)):
            if i != top:
                scale = a[i][col]
                a[i] = [x - scale*y for x, y in zip(a[i], a[top])]
        pivots.append(col)
        top += 1
    if any(not any(row[:columns]) and row[-1] for row in a):
        return None
    if len(pivots) != columns:
        return None
    answer = [F(0)] * columns
    for row, col in enumerate(pivots):
        answer[col] = a[row][-1]
    return tuple(answer)


def common_w(matrices, r, epsilon):
    """Return fixed-(r,epsilon) normalized witness or None; NOT global instability."""
    r, epsilon = rational(r), rational(epsilon)
    matrices = tuple(tuple(tuple(rational(x) for x in row) for row in m) for m in matrices)
    if not 1 <= len(matrices) <= 4:
        raise ValueError('one to four matrices required')
    n = len(matrices[0])
    if not 1 <= n <= 4 or not 0 <= r < 1 or not 0 < epsilon <= F(1, n):
        raise ValueError('bounded dimension, contractive r and positive epsilon required')
    if any(len(m) != n or any(len(row) != n or any(x < 0 for x in row) for row in m) for m in matrices):
        raise ValueError('nonnegative square equal-sized matrices required')
    constraints = []
    for m in matrices:
        for i, row in enumerate(m):
            constraints.append((tuple(x - (r if i == j else 0) for j, x in enumerate(row)), F(0)))
    for i in range(n):
        constraints.append((tuple(F(-1 if i == j else 0) for j in range(n)), -epsilon))
    # Compact polytope sum(w)=1: any nonempty instance has a vertex.
    for active in combinations(constraints, n - 1):
        rows = [tuple(F(1) for _ in range(n))] + [a for a, _ in active]
        rhs = [F(1)] + [b for _, b in active]
        w = unique_solution(rows, rhs, n)
        if w is not None and all(sum(x*y for x, y in zip(a, w)) <= b for a, b in constraints):
            return w
    return None


def feasible_subsets(costs, budget):
    costs, budget = tuple(rational(x) for x in costs), rational(budget)
    if not 1 <= len(costs) <= 4 or min(costs) < 0 or budget < 0:
        raise ValueError('one to four nonnegative costs and nonnegative budget required')
    return tuple(tuple(i for i in range(len(costs)) if mask & (1 << i))
                 for mask in range(1 << len(costs))
                 if sum(costs[i] for i in range(len(costs)) if mask & (1 << i)) <= budget)


def lottery_marginals(costs, budget, lottery):
    allowed = set(feasible_subsets(costs, budget))
    marginal = [F(0)] * len(costs)
    total = F(0)
    for subset, probability in lottery:
        probability = rational(probability)
        if tuple(subset) not in allowed or probability < 0:
            raise ValueError('invalid subset or probability')
        total += probability
        for i in subset:
            marginal[i] += probability
    if total != 1:
        raise ValueError('probabilities must sum to one')
    return tuple(marginal)


def max_common_audit(costs, budget):
    """Exact small LP optimum and certificate lottery for equal marginal auditing."""
    subsets = feasible_subsets(costs, budget)
    n = len(costs)
    # sum lambda=1; sum lambda*(1{i in S}-1{0 in S})=0 for i=1..n-1.
    # Every nonempty bounded feasible LP has an optimal basic solution supported
    # on at most rank(A)<=n columns, including degenerate/lower-rank instances.
    best = F(-1)
    best_lottery = None
    for k in range(1, min(n, len(subsets)) + 1):
        for support in combinations(subsets, k):
            rows = [[1]*k] + [[int(i in s)-int(0 in s) for s in support] for i in range(1, n)]
            weights = unique_solution(rows, [1]+[0]*(n-1), k)
            if weights is None or min(weights) < 0:
                continue
            q = sum(p for s, p in zip(support, weights) if 0 in s)
            if q > best:
                best = q
                best_lottery = tuple((s, p) for s, p in zip(support, weights) if p)
    assert best_lottery is not None  # Empty subset always supplies q=0.
    assert lottery_marginals(costs, budget, best_lottery) == (best,)*n
    return best, best_lottery


def examples():
    witness = common_w((((0, 1), (0, 0)),), F(1, 2), F(1, 4))
    result = {'witness': [str(x) for x in witness], 'r': '1/2',
              'heterogeneous': []}
    for costs, budget in [((2, 1), 2), ((2, 1, 1), 2), ((2, 2), 3), ((0, 0), 0)]:
        q, lottery = max_common_audit(costs, budget)
        result['heterogeneous'].append({'costs': costs, 'budget': budget, 'q': str(q),
            'lottery': [{'subset': s, 'probability': str(p)} for s, p in lottery]})
    return result


if __name__ == '__main__':
    import json
    print(json.dumps(examples(), indent=2))
