"""Coupled policy sweeps. Replicate-level uncertainty, plus auditable event traces."""
import csv
import hashlib
import json
import math
from pathlib import Path
import platform
import statistics
from simulator import Config, run, one_request_oracle
from fractions import Fraction

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results'
REPLICATES=100
METRICS=('completed_requests','unresolved_requests','relied_requests','reservation_failures','retry_attempts',
         'refuse_actors','repaired_reliances','pending_repairs','unnoticed_affected_reliances',
         'full_effort_completed_panels','true_independent_completed_panels')


def interval(values):
    mean=statistics.mean(values)
    se=statistics.stdev(values)/math.sqrt(len(values))
    return mean,mean-1.96*se,mean+1.96*se


def main():
    OUT.mkdir(exist_ok=True);rows=[]; aggregate=[]
    configs=[Config(policy=p,retry=r,clones=n,capacity=c,reserve_repair=reserve)
             for p in ('group_first','naive') for r in ('fixed_panel','reroll')
             for n in (1,10,100) for c in (3.,8.,20.) for reserve in (False,True)]
    configs += [Config(clones=100,capacity=20,hidden_control=True),
                Config(clones=100,capacity=20,reliance_filter='A_only')]
    for index,config in enumerate(configs):
        samples=[run(config,70000+j) for j in range(REPLICATES)]
        entry={'scenario':index,**config.__dict__,'replicates':REPLICATES}
        for metric in (*METRICS,'total_hours'):
            vals=[s['total_hours'] if metric=='total_hours' else s['counts'].get(metric,0) for s in samples]
            avg,lo,hi=interval(vals)
            rows.append({'scenario':index,**config.__dict__,'metric':metric,'mean':avg,'normal95_low':lo,'normal95_high':hi,'replicates':REPLICATES})
            entry[metric]=avg
        # Pooled descriptive shares are NOT accompanied by binomial CIs: requests
        # within a replicate compete for capacity and are not independent.
        for stage in ('initial','selected','reserved','completed','relied'):
            denom=sum(s['counts'].get(stage+'_panels',0) for s in samples)
            num=sum(s['counts'].get('A_'+stage+'_panels',0) for s in samples)
            entry['A_'+stage+'_share']=num/denom if denom else None
            entry[stage+'_panels_total']=denom
        aggregate.append(entry)
    with (OUT/'policy-sweep.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]),lineterminator='\n')
        writer.writeheader();writer.writerows(rows)
    traces={name:run(cfg,70017,True) for name,cfg in {
        'group_first_scarce':Config(capacity=3,clones=100),
        'naive_scarce':Config(policy='naive',capacity=3,clones=100),
        'group_first_plentiful':Config(capacity=20,clones=100),
        'hidden_control':Config(capacity=20,clones=100,hidden_control=True),
        'selective_reliance':Config(capacity=20,reliance_filter='A_only')}.items()}
    for name,result in traces.items():(OUT/(name+'.json')).write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    summary={'schema':'mcrp-coupled-experiment.v1','interpretation':'Synthetic policy comparison, no human or scientific validation',
             'scenarios':len(configs),'replicates_per_scenario':REPLICATES,'seeds':'70000..70099 reused across policies as common random numbers',
             'total_runs':len(configs)*REPLICATES,'requests_per_run':12,'sweep_rows':len(rows),
             'uncertainty':'Pointwise normal 95% intervals on replicate means; no simultaneous correction. Pooled stage shares descriptive only. No empirical behavioral uncertainty.',
             'finite_oracle':{policy:{k:str(v) for k,v in one_request_oracle(Config(retry=policy),{'A':Fraction(1),'B':Fraction(1,4),'C':Fraction(1)}).items()} for policy in ('reroll','fixed_panel')},
             'scenario_results':aggregate,'python':platform.python_version(),
             'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.glob('*.py'))},
             'csv_sha256':hashlib.sha256((OUT/'policy-sweep.csv').read_bytes()).hexdigest()}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:summary[k] for k in ('scenarios','total_runs','sweep_rows')}))

if __name__=='__main__':main()
