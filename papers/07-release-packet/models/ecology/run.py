"""Run paired seed perturbations, retaining failures and absolute denominators."""
from pathlib import Path
import csv
import hashlib
import json
import platform
import statistics
from .ecology import Config, simulate

REGIMES={
    'light_load':{'arrival':.15},
    'default':{},
    'overload':{'arrival':.85},
    'strong_feedback':{'reinforcement':8.,'exploration':.02},
    'high_exploration':{'exploration':.7},
    'expensive_repair':{'repair_multiplier':2.},
    'blind_common_cause':{'blind_probability':.7},
    'biased_verification':{'audit_probability':.8,'audit_bias':.95},
    'no_verification':{'audit_probability':0.},
}
METRICS=('offered','completed','completion_coverage','correct_checks_per_offer','defect_detection_fraction','accuracy_among_completed','attention_hhi','largest_attention_share','minimum_group_coverage','unresolved_offers','repair_backlog','labor','mean_queue_age')

def main():
    root=Path(__file__).parent; out=root/'results'; out.mkdir(exist_ok=True)
    rows=[]; aggregate=[]
    for regime,kwargs in REGIMES.items():
        values={}
        for seed in range(1,9):
            fingerprints=set()
            for policy in ('prestige','bounded','uniform'):
                r=simulate(Config(seed=seed,periods=80,**kwargs),policy)
                fingerprints.add(r['exogenous_offer_sha256'])
                row={'regime':regime,'seed':seed,'policy':policy,**{k:r[k] for k in METRICS}}
                row.update({f'coverage_{i}':x for i,x in enumerate(r['coverage_by_group'])})
                row.update({f'count_{k}':v for k,v in r['counters'].items()})
                rows.append(row);values[seed,policy]=r
            assert len(fingerprints)==1,'policy changed exogenous inputs'
        for policy in ('prestige','bounded','uniform'):
            summaries={k:{'mean':statistics.mean(values[s,policy][k] for s in range(1,9)),
                           'min':min(values[s,policy][k] for s in range(1,9)),
                           'max':max(values[s,policy][k] for s in range(1,9))} for k in METRICS}
            paired={k:statistics.mean(values[s,policy][k]-values[s,'uniform'][k] for s in range(1,9)) for k in METRICS}
            aggregate.append({'regime':regime,'policy':policy,'summaries':summaries,'paired_difference_from_uniform':paired})
        print(regime,flush=True)
    with (out/'sweep.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
    sources={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*.py'))}
    manifest={'schema':'mcrp-ecology/0.1','python':platform.python_version(),'seeds':list(range(1,9)),
              'periods':80,'regimes':REGIMES,'rows':len(rows),'source_sha256':sources,
              'sweep_sha256':hashlib.sha256((out/'sweep.csv').read_bytes()).hexdigest(),
              'interpretation':'Exploratory synthetic sensitivity; min/max are seed ranges, not inferential confidence intervals.',
              'aggregate':aggregate}
    (out/'summary.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
    trace=simulate(Config(seed=1,periods=80),policy='bounded',trace=True)
    (out/'example-trajectory.json').write_text(json.dumps(trace,indent=2,sort_keys=True)+'\n')

if __name__=='__main__':main()
