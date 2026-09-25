"""Exact synthetic certification counterexamples; no network or third-party packages."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def probability(value):
    if isinstance(value, bool):
        raise ValueError('probability must be a rational number')
    value = F(value)
    if not 0 <= value <= 1:
        raise ValueError('probability outside [0,1]')
    return value


def count(value):
    if type(value) is not int or value < 0:
        raise ValueError('count must be a nonnegative integer')
    return value


def false_clear(floor, residual, checks):
    """P(all checks pass | invalid claim), with one shared latent blind spot."""
    floor, residual, checks = probability(floor), probability(residual), count(checks)
    return floor + (1-floor) * residual**checks


def all_outcomes(floor, residual, checks):
    """Independent finite latent-state enumeration, restricted to small fixtures."""
    floor, residual, checks = probability(floor), probability(residual), count(checks)
    if checks > 16:
        raise ValueError('finite enumeration capped at 16 checks')
    masses = {}
    for bits in product((0, 1), repeat=checks):
        mass = (1-floor) * residual**sum(bits) * (1-residual)**(checks-sum(bits))
        if all(bits):
            mass += floor
        masses[bits] = mass
    return masses


def family_clear(families, allocation):
    """Multiply family risks ONLY under the explicit cross-family independence model."""
    if len(families) != len(allocation):
        raise ValueError('shape mismatch')
    result = F(1)
    for (floor, residual), checks in zip(families, allocation):
        result *= false_clear(floor, residual, checks)
    return result


def best_allocation(families, budget):
    """Exact finite optimization; one cost unit/check, no activation costs."""
    budget = count(budget)
    if budget > 16 or not 1 <= len(families) <= 5:
        raise ValueError('toy optimization size exceeded')
    candidates = (a for a in product(range(budget+1), repeat=len(families)) if sum(a) == budget)
    return min(((family_clear(families, a), a) for a in candidates), default=(F(1), ()))


def shopping(single_trial, trials):
    return 1-(1-probability(single_trial))**count(trials)


def shopping_shared(floor, residual, checks, trials):
    floor, residual = probability(floor), probability(residual)
    checks, trials = count(checks), count(trials)
    return floor + (1-floor)*shopping(residual**checks, trials) if trials else F(0)


def tv(p, q):
    p, q = tuple(map(probability, p)), tuple(map(probability, q))
    if len(p) != len(q) or sum(p) != 1 or sum(q) != 1:
        raise ValueError('normalized equal-length distributions required')
    return sum(abs(a-b) for a, b in zip(p, q))/2


def demo():
    f, p = F(1,10), F(1,5)
    rows = []
    for k in (1, 2, 5, 10, 100):
        exact = false_clear(f, p, k)
        rows.append({'checks':k, 'false_clear':float(exact), 'independence_misstatement':float(false_clear(f,p,1)**k)})
    optimum, allocation = best_allocation([(f,p), (f,p)], 6)
    return {'interpretation':'Synthetic conditional false-clear probabilities, not posterior truth probabilities.',
            'common_blindspot':rows,
            'six_check_allocation':{'allocation':allocation,'false_clear':float(optimum),
                                     'all_one_family':float(false_clear(f,p,6)),
                                     'premise':'Independent family-level blind spots; each check costs one unit.'},
            'shopping':{'single_trial':.1,'trials':50,'at_least_one_clear':float(shopping(F(1,10),50)),
                        'premise':'Independent fresh panels and all attempts counted.'},
            'transcript_indistinguishability':{'good':[.9,.1],'bad':[.8,.2],
                                               'tv':float(tv([F(9,10),F(1,10)],[F(4,5),F(1,5)])),
                                               'false_accept_lower_bound_if_good_accepts_90_percent':.8}}


if __name__ == '__main__':
    path = Path(__file__).with_name('results.json')
    path.write_text(json.dumps(demo(), indent=2)+'\n')
    print(path.name)
