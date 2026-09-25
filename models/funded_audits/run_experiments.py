"""Small fully specified audit-delivery sweep; no human behavioral estimates."""
import csv
from dataclasses import replace
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
from model import Config,run,exact_selection_marginals,MATH_PATH

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results'


def main():
    OUT.mkdir(exist_ok=True)
    cases={
        'no_audit':Config(promised_quota=0,delivered_quota=0),
        'concealed_funded':Config(),
        'partial_refusal_unused_slots':Config(),
        'broken_promise':Config(delivered_quota=1,allow_broken_promise=True),
        'corrected_disclosure_of_delivery_probability':Config(promised_quota=1,delivered_quota=1),
        'selection_disclosed_before_effort':Config(disclose_selection=True),
        'false_positive_exclusion':Config(false_positive=.3),
        'shared_cross_roles':Config(role_mode='shared_cross'),
        'insufficient_shared_capacity':Config(role_mode='shared_cross',shared_person_capacity=5),
        'self_audit_unavailable':Config(role_mode='self_audit'),
        'insufficient_collateral':Config(actor_escrow=1)}
    rows=[];aggregates=[]
    for name,cfg in cases.items():
        runs=[run(cfg,seed,outside_options=[1]*4+[.1]*4 if name=='partial_refusal_unused_slots' else None) for seed in range(60,80)]
        for result in runs:
            row={'case':name,'seed':result['seed'],'status':result['status']}
            for metric in ('offered','honest','shallow','refused','completed','audited','unused_refused_audit_slots','false_sanctions','detected_shallow'):
                row[metric]=result['counts'].get(metric,0)
            row['audit_tokens_spent']=result.get('tokens',{}).get('audit_spent',0)
            row['expected_utility_regret']=result.get('aggregate_expected_utility_regret_under_actual_information',0)
            rows.append(row)
        aggregates.append({'case':name,'config':cfg.__dict__,'runs':len(runs),'status':runs[0]['status'],
                           'counts_across_runs':{key:sum(r['counts'].get(key,0) for r in runs) for key in ('offered','honest','shallow','refused','completed','audited','false_sanctions','detected_shallow')},
                           'audit_token_spend_across_runs':sum(r.get('tokens',{}).get('audit_spent',0) for r in runs),
                           'expected_utility_regret_per_run':runs[0].get('aggregate_expected_utility_regret_under_actual_information')})
        (OUT/(name+'.json')).write_text(json.dumps(runs[0],indent=2,allow_nan=False)+'\n')
    with (OUT/'audit-delivery.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
    summary={'schema':'mcrp-funded-audit-sweep.v1','cases':len(cases),'runs':len(rows),'seeds':'60..79 per case',
             'interpretation':'Deterministic configured finite sweep with seeded audit detection. Aggregate detection counts are descriptive toy outcomes; no empirical uncertainty or behavioral inference.',
             'exact_selection_marginals':{'N8_k4':[str(x) for x in exact_selection_marginals(8,4)],'N8_k1':[str(x) for x in exact_selection_marginals(8,1)]},
             'case_results':aggregates,'python':platform.python_version(),
             'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.glob('*.py'))},
             'imported_math_sha256':hashlib.sha256(MATH_PATH.read_bytes()).hexdigest(),
             'csv_sha256':hashlib.sha256((OUT/'audit-delivery.csv').read_bytes()).hexdigest()}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'cases':len(cases),'runs':len(rows)}))

if __name__=='__main__':main()
