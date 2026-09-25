"""Independent labeled-allocation enumeration; no author null-distribution reuse."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations,product
from pathlib import Path
import csv,hashlib,json,sys
ROOT=Path(__file__).resolve().parent;PACKET=ROOT.parent.parent
sys.path.insert(0,str(PACKET/'models/human_pilot'))
from allocation import missing_effect_bounds
PAIRS=tuple(combinations(range(4),2))

@lru_cache(None)
def label_histogram(success_totals):
    # Reconstruct canonical labeled outcomes and enumerate every allowed allocation.
    blocks=[tuple([1]*k+[0]*(4-k)) for k in success_totals]
    outcomes_per_block=[tuple(sum(block[i] for i in pair) for pair in PAIRS) for block in blocks]
    return Counter(sum(sums) for sums in product(*outcomes_per_block))

@lru_cache(None)
def rejection_region(totals):
    hist=label_histogram(totals);K=sum(totals);den=sum(hist.values())
    return frozenset(S for S in hist if F(sum(v for t,v in hist.items() if abs(2*t-K)>=abs(2*S-K)),den)<=F(1,20))

def independent_power(units,benefit):
    blocks=units//4
    y0=[[0,0,1,1] for _ in range(blocks)];y1=[x[:] for x in y0]
    # Construct table specified in prose, independently of author constructor.
    positions=[(b,i) for i in (0,1) for b in range(blocks)]
    for b,i in positions[:benefit]:y1[b][i]=1
    rejected=0
    for assignment in product(PAIRS,repeat=blocks):
        observed=[tuple(y1[b][i] if i in assignment[b] else y0[b][i] for i in range(4)) for b in range(blocks)]
        totals=tuple(sorted(map(sum,observed)))
        treated=sum(observed[b][i] for b,pair in enumerate(assignment) for i in pair)
        rejected+=treated in rejection_region(totals)
    return F(rejected,6**blocks)

def main():
    records=[]
    for row in csv.DictReader((PACKET/'models/human_pilot/results/finite-power.csv').open()):
        n,benefit=int(row['units']),int(row['benefit_units'])
        actual=independent_power(n,benefit)
        assert actual==F(row['power_exact'])
        records.append({'units':n,'benefit_units':benefit,'exact_power':str(actual)})
    # Counterexample to interpreting complete-data realized contrast as causal bound.
    y0=y1=((0,0,1,1),(0,0,1,1))
    causal_effect=F(sum(map(sum,y1))-sum(map(sum,y0)),8)
    bounds=missing_effect_bounds(4,4,4,0,4,4)
    assert causal_effect==0 and bounds==(F(1),F(1))
    # Independent brute-force all ways to fill missing records agrees with armcontrast bounds.
    possible=[]
    for t in product((0,1),repeat=1):
        for c in product((0,1),repeat=2):possible.append(F(2+sum(t),4)-F(1+sum(c),4))
    assert (min(possible),max(possible))==missing_effect_bounds(2,3,4,1,2,4)
    result={'interpretation':'Exact enumeration of artificial potential outcomes, no actual human study',
            'power_rows_independently_matched':len(records),'rows':records,'cached_labeled_null_patterns':label_histogram.cache_info().currsize,
            'missing_bound_counterexample':{'true_finite_population_effect':str(causal_effect),'realized_complete_data_armcontrast_bounds':[str(x) for x in bounds],'reason':'Potential outcomes differ across units, not treatment; actual realized arm contrast has randomization error.'},
            'missing_completion_enumeration':{'lower':str(min(possible)),'upper':str(max(possible))},
            'source_sha256':hashlib.sha256((PACKET/'models/human_pilot/allocation.py').read_bytes()).hexdigest()}
    (ROOT/'human-pilot-review-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
