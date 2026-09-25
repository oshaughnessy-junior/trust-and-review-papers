"""Pre-results design tools: block allocation and exact finite randomization.

Python 3.9+, standard library. All bundled IDs/outcomes are artificial. Tests of
sharp no-effect nulls are not exact tests of arbitrary average-effect nulls.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
import math
import random

PAIRS=tuple(combinations(range(4),2))


def balanced_assignment(blocks, seed):
    """Two of four boundary units per block get the card; others the template.

    Blocks are formed within strata before randomization. Production allocation
    concealment/registration is not implemented by a visible pseudorandom seed.
    """
    if not blocks or any(len(block)!=4 for block in blocks):raise ValueError('four-unit blocks required')
    ids=[unit for block in blocks for unit in block]
    if any(not isinstance(x,str) or not x for x in ids) or len(set(ids))!=len(ids):
        raise ValueError('unique nonempty boundary IDs required')
    rng=random.Random(seed)
    output=[]
    for index,block in enumerate(blocks):
        treated=set(rng.sample(range(4),2))
        output.extend({'boundary':unit,'block':index,'arm':'card' if i in treated else 'template'} for i,unit in enumerate(block))
    return output


def binary_blocks(blocks):
    if not blocks or any(len(b)!=4 for b in blocks):raise ValueError('four-outcome blocks required')
    if any(type(y) is not int or y not in (0,1) for block in blocks for y in block):
        raise ValueError('binary integer outcomes required')
    return tuple(tuple(b) for b in blocks)


@lru_cache(maxsize=None)
def null_distribution(block_successes):
    """Integer assignment counts for total treated successes, sharp-null outcomes.

    Each size-four block has six equiprobable allocations. Hypergeometric counts
    convolve independently across blocks; no asymptotic approximation is used.
    """
    distribution={0:1}
    for successes in block_successes:
        if type(successes) is not int or not 0<=successes<=4:raise ValueError('invalid block success count')
        one={x:math.comb(successes,x)*math.comb(4-successes,2-x)
             for x in range(3) if x<=successes and 0<=2-x<=4-successes}
        nxt=Counter()
        for a,ways in distribution.items():
            for b,other in one.items():nxt[a+b]+=ways*other
        distribution=dict(nxt)
    return tuple(sorted(distribution.items()))


@lru_cache(maxsize=None)
def _sharp_p(block_successes, treated_successes):
    total=sum(block_successes)
    observed=abs(2*treated_successes-total)
    dist=null_distribution(block_successes)
    extreme=sum(count for value,count in dist if abs(2*value-total)>=observed)
    return Fraction(extreme,6**len(block_successes))


def sharp_null_test(outcomes, treated_pairs):
    blocks=binary_blocks(outcomes)
    if len(treated_pairs)!=len(blocks) or any(tuple(sorted(pair)) not in PAIRS for pair in treated_pairs):
        raise ValueError('exactly two distinct treated positions per block required')
    S=sum(block[i] for block,pair in zip(blocks,treated_pairs) for i in pair)
    K=sum(sum(block) for block in blocks);B=len(blocks)
    return {'difference_in_adequacy':Fraction(2*S-K,2*B),
            'two_sided_sharp_null_p':_sharp_p(tuple(sorted(sum(b) for b in blocks)),S),
            'assignments':6**B}


def design_power(y0, y1, alpha=Fraction(1,20)):
    """Exact power over allowed assignments of ONE fixed potential-outcome table.

    Table is illustrative, not an estimate. Budget capped at six blocks (24 units).
    Rejection uses an exact two-sided sharp-null test on each observed outcome set.
    """
    a=binary_blocks(y0);b=binary_blocks(y1)
    if len(a)!=len(b) or len(a)>6:raise ValueError('matching tables with at most six blocks required')
    alpha=Fraction(alpha)
    if not 0<alpha<1:raise ValueError('alpha must lie in (0,1)')
    rejects=0;assignment_count=6**len(a)
    for assignment in product(PAIRS,repeat=len(a)):
        totals=[];treated=0
        for baseline,card,pair in zip(a,b,assignment):
            selected=set(pair)
            treated_sum=sum(card[i] for i in pair)
            treated+=treated_sum
            totals.append(treated_sum+sum(baseline[i] for i in range(4) if i not in selected))
        if _sharp_p(tuple(sorted(totals)),treated)<=alpha:rejects+=1
    average_effect=Fraction(sum(sum(v) for v in b)-sum(sum(v) for v in a),4*len(a))
    return {'units':4*len(a),'assignments':assignment_count,'rejections':rejects,
            'power':Fraction(rejects,assignment_count),'average_effect':average_effect}


def toy_potential_outcomes(units, benefit_units):
    """Half always adequate; upgrade specified baseline failures, round-robin.

    No harm types. This optimistic monotone family is NOT human evidence or the
    only arrangement with the same average effect. Blocks repeat 0,0,1,1 at baseline.
    """
    if type(units) is not int or units<8 or units%8 or units>24:raise ValueError('units must be 8,16,24')
    if type(benefit_units) is not int or not 0<=benefit_units<=units//2:raise ValueError('invalid benefit count')
    B=units//4;y0=[[0,0,1,1] for _ in range(B)];y1=[v[:] for v in y0]
    candidates=[(block,pos) for pos in (0,1) for block in range(B)]
    for block,pos in candidates[:benefit_units]:y1[block][pos]=1
    return y0,y1


def missing_effect_bounds(treated_success, treated_observed, treated_total,
                          control_success, control_observed, control_total):
    """Worst-case missing-outcome bounds on the realized randomized-arm contrast.

    These bound the difference between the two assigned arms' complete observed
    outcome rates. They do NOT bound finite-population causal average effects:
    randomization uncertainty and unobserved counterfactual outcomes remain even
    with no missing observations. They are not confidence intervals.
    """
    values=(treated_success,treated_observed,treated_total,control_success,control_observed,control_total)
    if any(type(x) is not int or x<0 for x in values):raise ValueError('nonnegative integer counts required')
    if not 0<=treated_success<=treated_observed<=treated_total or not 0<=control_success<=control_observed<=control_total:
        raise ValueError('inconsistent counts')
    if not treated_total or not control_total:raise ValueError('positive arm totals required')
    return (Fraction(treated_success,treated_total)-Fraction(control_success+control_total-control_observed,control_total),
            Fraction(treated_success+treated_total-treated_observed,treated_total)-Fraction(control_success,control_total))
