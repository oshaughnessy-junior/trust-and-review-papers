"""Generate pre-results artificial assignments and exact design sensitivity."""
import csv
import hashlib
import json
from pathlib import Path
import platform
from allocation import balanced_assignment,design_power,toy_potential_outcomes,missing_effect_bounds,sharp_null_test

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'


def main():
    OUT.mkdir(exist_ok=True)
    blocks=[[f'{stratum}-toy-{i}' for i in range(4)] for stratum in ('novice','collaboration_delegate')]
    allocation=balanced_assignment(blocks,9252026)
    (OUT/'mock-allocation.json').write_text(json.dumps({'status':'ARTIFICIAL NOT A REAL STUDY ALLOCATION','seed':9252026,'records':allocation},indent=2)+'\n')
    rows=[]
    for units in (8,16,24):
        for benefit in (0,units//8,units//4,3*units//8,units//2):
            y0,y1=toy_potential_outcomes(units,benefit)
            result=design_power(y0,y1)
            rows.append({'units':units,'baseline_adequacy':.5,'benefit_units':benefit,
                         'effect':float(result['average_effect']),'effect_exact':str(result['average_effect']),
                         'power':float(result['power']),'power_exact':str(result['power']),
                         'assignments':result['assignments'],'rejections':result['rejections']})
    with (OUT/'finite-power.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
    thresholds=[]
    for n in (8,16,24):
        candidates=[r for r in rows if r['units']==n and r['power']>=.8]
        thresholds.append({'units':n,'smallest_tested_effect_reaching_80_percent_power':min(r['effect'] for r in candidates) if candidates else None,
                           'meaning':'Coarse-grid threshold under ONE optimistic fixed potential-outcome family; not an empirical MDE or recommended study size'})
    mock=sharp_null_test(((0,0,1,1),(0,1,1,1)),((0,1),(0,2)))
    bounds=missing_effect_bounds(2,3,4,1,2,4)
    summary={'schema':'mcrp-pre-results-design.v1','status':'No human study conducted, approved or registered',
             'power_method':'Exact enumeration of all balanced block assignments under specified fixed binary potential outcomes; two-sided sharp-null rejection alpha=.05',
             'rows':len(rows),'thresholds':thresholds,'mock_statistic':{k:str(v) for k,v in mock.items()},
             'missing_outcome_realized_arm_contrast_bounds':[str(x) for x in bounds],
             'missing_bounds_target':'Complete observed rate contrast between realized assigned arms; not finite-population causal ATE bounds or confidence intervals',
             'uncertainty':'No Monte Carlo error. Strong model uncertainty; exact sharp-null p-values do not give exact average-effect confidence intervals.',
             'python':platform.python_version(),'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.glob('*.py'))},
             'csv_sha256':hashlib.sha256((OUT/'finite-power.csv').read_bytes()).hexdigest()}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({'rows':len(rows),'thresholds':thresholds}))

if __name__=='__main__':main()
