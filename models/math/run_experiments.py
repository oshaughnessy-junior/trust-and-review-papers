"""Rebuild exact fixtures, parameter sweeps and seeded Monte Carlo diagnostics."""
import csv
import hashlib
import json
import math
from pathlib import Path
import platform
import random
import statistics
from protocol_math import (panel_distribution, inclusion, retry_summary, row_mul,
    envelope, repair_bound, shared_capacity, audit_interval, action_utilities, wilson, hard_audit_interval)

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results'


def dump_csv(name, rows):
    with (OUT/name).open('w', newline='') as stream:
        writer=csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)


def simulate_retry(p,a,b,limit,seed,n=20000):
    rng=random.Random(seed)
    completed=risky=attempts=0
    costs=[]
    for _ in range(n):
        used=0; done=False
        for _ in range(limit):
            used+=1
            category=rng.random()<p
            if rng.random() < (a if category else b):
                done=True; risky+=int(category); completed+=1
                break
        attempts+=used
        costs.append(.2*used+2*done)
    exact=retry_summary(p,a,b,limit,.2,2)
    cost_se=statistics.stdev(costs)/math.sqrt(n)
    return {'seed':seed,'requests':n,'attempts':attempts,'retries':attempts-n,
            'completed':completed,'unresolved':n-completed,'refused_attempts':attempts-completed,
            'risky_completed':risky,'completion_rate':completed/n,
            'completion_wilson_95':wilson(completed,n),
            'risky_among_completed':risky/completed if completed else None,
            'risky_among_completed_wilson_95':wilson(risky,completed) if completed else None,
            'mean_cost':statistics.mean(costs),'mean_cost_standard_error':cost_se,
            'mean_cost_normal_95':[statistics.mean(costs)-1.96*cost_se,statistics.mean(costs)+1.96*cost_se],
            'exact':exact}


def main():
    OUT.mkdir(exist_ok=True)
    clone_rows=[]
    for copies in (1,2,5,10,100,1000):
        for policy in ('naive','group_first'):
            p=inclusion(panel_distribution({'A':copies,'B':1,'C':1},2,policy),'A')
            clone_rows.append({'A_representatives':copies,'policy':policy,'A_inclusion':float(p),'exact':str(p)})
    dump_csv('clone-invariance.csv',clone_rows)
    retry_rows=[]
    for a,b in ((1,1),(1,.5),(1,.01),(.1,1)):
        for limit in (1,2,5,10,50):
            retry_rows.append({'risk_completion':a,'other_completion':b,'max_attempts':limit,
                               **retry_summary(.1,a,b,limit,.2,2)})
    dump_csv('completion-retry.csv',retry_rows)
    mc=[simulate_retry(.1,a,b,L,seed) for a,b,L,seed in
        ((1,.01,1,25101),(1,.01,10,25102),(1,.01,50,25103),(1,1,10,25104))]
    bad=[[[0,2],[0,0]],[[0,0],[2,0]]]
    good=[[[.2,.1],[.1,.4]],[[.1,.3],[.05,.2]]]
    repair_rows=[]
    for name,family,w in [('snapshot_stable_switching_bad',bad,[1,1]),('common_envelope',good,[1,2])]:
        z=[1.,0.]; total=sum(x*y for x,y in zip(z,w)); r=envelope(family,w)['factor']
        repair_rows.append({'case':name,'generation':0,'type0':z[0],'type1':z[1],'weighted':total,'cumulative_weighted':total,'geometric_envelope':1.})
        for generation in range(1,21):
            z=row_mul(z,family[(generation-1)%2]); weighted=sum(x*y for x,y in zip(z,w)); total+=weighted
            repair_rows.append({'case':name,'generation':generation,'type0':z[0],'type1':z[1],'weighted':weighted,'cumulative_weighted':total,'geometric_envelope':r**generation})
    dump_csv('repair-switching.csv',repair_rows)
    audit_rows=[]
    for index in range(41):
        q=index/40
        counts={'honest':0,'shirk':0,'abstain':0}
        # Synthetic fixed population: two reward levels, 51 evenly spaced costs.
        # Ties choose abstain, then honest, then shirk; no fitted participant data.
        for reward in (.35,1.0):
            for i in range(51):
                cost=i/50
                utilities=action_utilities(q,cost,reward,2,.1,.8,.1)
                action=max(('abstain','honest','shirk'),key=lambda a:utilities[a])
                counts[action]+=1
        participants=counts['honest']+counts['shirk']
        audit_rows.append({'q':q,'invitations':102,**counts,
                           'participants':participants,'honest_share_participants':counts['honest']/participants if participants else None,
                           'expected_audit_hours':participants*q*.1,
                           'expected_audit_hours_all_invited':102*q*.1})
    dump_csv('audit-participation.csv',audit_rows)
    results={
        'schema':'mcrp-release-math.v1','interpretation':'Synthetic conditional examples, no empirical validation',
        'panel':{'clone_rows':len(clone_rows),'declared_control_required':True,'hidden_control_A_seat_probability':'5/6','baseline_A_seat_probability':'2/3'},
        'completion_monte_carlo':mc,
        'repair':{'bad_family':bad,'bad_common_weight_test':envelope(bad,[1,1]),
                  'good_family':good,'weights':[1,2],'good_common_weight_test':envelope(good,[1,2]),
                  'good_total_expected_weight_bound':repair_bound([1,0],good,[1,2]),
                  'rare_burst':{'offspring_zero_probability':.99,'offspring_50_probability':.01,'mean_offspring':.5,
                                'first_generation_exceeds_8_probability':.01,
                                'warning':'Mean subcriticality is not a pathwise capacity bound or deadline guarantee'}},
        'shared_capacity':shared_capacity([('Ada','day1','check',3),('Ada','day1','audit',2),('Ada','day1','repair',4)],{('Ada','day1'):8}),
        'audit':{'expected_budget_case':audit_interval(.2,1,2,.02,.8,.1,100,.1,2),
                 'hard_budget_case':hard_audit_interval(.2,1,2,.02,.8,.1,100,.1,2),
                 'nonintegral_hard_budget':hard_audit_interval(0,1,1,0,1,0,3,1,1.5),
                 'underfunded_case':audit_interval(.2,1,2,.02,.8,.1,100,.1,1),
                 'participation_conflict':audit_interval(.2,.3,2,.3,.8,.05,100,.1,10)},
        'counts':{'clone_rows':len(clone_rows),'retry_rows':len(retry_rows),'repair_rows':len(repair_rows),'audit_rows':len(audit_rows)},
        'reproducibility':{'python':platform.python_version(),'random_generator':'stdlib random.Random Mersenne Twister',
            'Monte_Carlo_requests':80000,'confidence':'Pointwise nominal 95% Wilson binomial intervals; normal mean-cost intervals; no simultaneous or human-behavior inference',
            'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.glob('*.py'))},
            'table_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.glob('*.csv'))}}}
    (OUT/'summary.json').write_text(json.dumps(results,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'results':str(OUT),'counts':results['counts'],'Monte_Carlo_requests':80000}))


if __name__=='__main__': main()
