#!/usr/bin/env python3
"""Matched synthetic sensitivity experiments, Python standard library only."""
import csv
import hashlib
import json
import math
import platform
import random
import statistics
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def water_fill(A, a, H, lower=None):
    lower=[0.0]*len(A) if lower is None else lower[:]
    if sum(lower)>H+1e-9:
        raise ValueError('infeasible lower bounds')
    lo,hi=0.0,max(x*y for x,y in zip(A,a))
    for _ in range(100):
        eta=(lo+hi)/2
        vals=[max(l,math.log(x*y/eta)/y,0) for x,y,l in zip(A,a,lower)]
        if sum(vals)>H:
            lo=eta
        else:
            hi=eta
    vals=[max(l,math.log(x*y/hi)/y,0) for x,y,l in zip(A,a,lower)]
    assert abs(sum(vals)-H)<1e-7
    return vals


def benefit(A,a,h):
    return sum(x*(-math.expm1(-y*z)) for x,y,z in zip(A,a,h))


def poisson(rng, lam):
    cutoff=math.exp(-lam)
    product=1.0
    k=0
    while product>cutoff:
        product*=rng.random()
        k+=1
    return k-1


def mean_ci(vals):
    mean=statistics.mean(vals)
    se=statistics.stdev(vals)/math.sqrt(len(vals)) if len(vals)>1 else 0
    return {'mean':mean,'mc_se':se,'normal_approx_low':mean-1.96*se,'normal_approx_high':mean+1.96*se}


def write_csv(name,rows):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)


def allocation_experiment():
    rows=[]
    scenarios=['known','noise_05','noise_10','noise_20','biased_underserved','blindspot_ignored']
    n,seeds=80,30
    for seed in range(seeds):
        rng=random.Random(42000+seed)
        potential=[rng.lognormvariate(0,1) for _ in range(n)]
        a=[rng.lognormvariate(-.2,.5) for _ in range(n)]
        noiseA=[rng.gauss(0,1) for _ in range(n)]
        noisea=[rng.gauss(0,1) for _ in range(n)]
        for scenario in scenarios:
            b=[.8 if scenario=='blindspot_ignored' and i<n//4 else .1 for i in range(n)]
            A=[v*(1-blind) for v,blind in zip(potential,b)]
            sigma=.5 if scenario=='noise_05' else 1 if scenario=='noise_10' else 2 if scenario=='noise_20' else 0
            observed_A=[v*math.exp(sigma*z) for v,z in zip(A,noiseA)]
            observed_a=[v*math.exp(sigma*z) for v,z in zip(a,noisea)]
            if scenario=='biased_underserved':
                for i in range(n//4):
                    observed_A[i]*=.2
                    observed_a[i]*=.5
            if scenario=='blindspot_ignored':
                observed_A=potential[:]
            for H in [20,80]:
                oracle=water_fill(A,a,H)
                policies={'uniform':[H/n]*n,'estimated_waterfill':water_fill(observed_A,observed_a,H),
                          'reserve_20':water_fill(observed_A,observed_a,H,[.2*H/(n//4) if i<n//4 else 0 for i in range(n)]),
                          'latent_oracle':oracle}
                oracle_benefit=benefit(A,a,oracle)
                uniform_benefit=benefit(A,a,policies['uniform'])
                assert oracle_benefit+1e-8>=uniform_benefit
                for policy,h in policies.items():
                    value=benefit(A,a,h)
                    assert value<=oracle_benefit+1e-7
                    rows.append({'scenario':scenario,'hours':H,'seed':seed,'policy':policy,'true_avoided_loss':value,
                        'paired_gain_vs_uniform':value-uniform_benefit,'regret_vs_latent_oracle':oracle_benefit-value,
                        'lots_at_least_quarter_hour':sum(v>=.25-1e-9 for v in h),
                        'underserved_hours':sum(h[:n//4]),'irreducible_floor':sum(v*blind for v,blind in zip(potential,b))})
    write_csv('allocation.csv',rows)
    summaries=[]
    for scenario in scenarios:
        for H in [20,80]:
            for policy in ['uniform','estimated_waterfill','reserve_20','latent_oracle']:
                sub=[r for r in rows if r['scenario']==scenario and r['hours']==H and r['policy']==policy]
                summaries.append({'scenario':scenario,'hours':H,'policy':policy,'seeds':seeds,
                    'paired_gain_vs_uniform':mean_ci([r['paired_gain_vs_uniform'] for r in sub]),
                    'mean_regret':statistics.mean(r['regret_vs_latent_oracle'] for r in sub),
                    'mean_underserved_hours':statistics.mean(r['underserved_hours'] for r in sub),
                    'mean_lots_covered':statistics.mean(r['lots_at_least_quarter_hour'] for r in sub)})
    return rows,summaries


def queue_experiment():
    rows=[]
    H,days,seeds=8,365,30
    # Pareto(scale=.5, shape=1.5) clipped at 8, expectation via integrated tail.
    mean_appeal=.5 + .5**1.5*(2*(.5**(-.5)-8**(-.5)))
    for rho in [.5,.7,.9]:
        for multiplier in [1,2,4]:
            for reduction in [1,.75,.5]:
                lam=rho*H/2*multiplier
                estimated_service=2*reduction+.1*mean_appeal
                for seed in range(seeds):
                    rng=random.Random(71000+seed)
                    stream=[]
                    for day in range(days):
                        tasks=[]
                        for _ in range(poisson(rng,lam)):
                            cost=rng.expovariate(1/(2*reduction))
                            if rng.random()<.1:
                                cost+=min(8,.5*rng.paretovariate(1.5))
                            tasks.append(cost)
                        stream.append(tasks)
                    for policy in ['unbounded','one_day_reservation']:
                        backlog=peak=work=completed=0.0
                        admitted=rejected=attempted=0
                        series=[]
                        for tasks in stream:
                            attempted+=len(tasks)
                            take=len(tasks) if policy=='unbounded' else min(len(tasks),max(0,math.floor((H-backlog)/estimated_service)))
                            admitted+=take;rejected+=len(tasks)-take
                            arrived=sum(tasks[:take]);work+=arrived
                            service=min(H,backlog+arrived);completed+=service
                            backlog=max(0,backlog+arrived-H)
                            peak=max(peak,backlog);series.append(backlog)
                        assert math.isclose(work,completed+backlog,abs_tol=1e-7)
                        rows.append({'baseline_primary_load':rho,'arrival_multiplier':multiplier,'primary_cost_multiplier':reduction,
                            'policy':policy,'seed':seed,'expected_total_load':lam*estimated_service/H,
                            'attempted':attempted,'admitted':admitted,'rejected':rejected,
                            'final_backlog_hours':backlog,'peak_backlog_hours':peak,
                            'mean_backlog_hours':statistics.mean(series),'admitted_actual_hours':work,
                            'completed_hours':completed,'last_quarter_drift_hours_per_day':(series[-1]-series[-92])/91})
    write_csv('queues.csv',rows)
    summaries=[]
    for rho in [.5,.7,.9]:
        for m in [1,2,4]:
            for r in [1,.75,.5]:
                for policy in ['unbounded','one_day_reservation']:
                    sub=[x for x in rows if x['baseline_primary_load']==rho and x['arrival_multiplier']==m and x['primary_cost_multiplier']==r and x['policy']==policy]
                    summaries.append({'baseline_primary_load':rho,'arrival_multiplier':m,'primary_cost_multiplier':r,'policy':policy,'seeds':seeds,
                        'expected_total_load':sub[0]['expected_total_load'],'final_backlog_hours':mean_ci([x['final_backlog_hours'] for x in sub]),
                        'mean_rejected':statistics.mean(x['rejected'] for x in sub),
                        'mean_completed_hours':statistics.mean(x['completed_hours'] for x in sub),
                        'mean_admitted':statistics.mean(x['admitted'] for x in sub)})
    return rows,summaries


def main():
    # Analytic active-set example validates the numerical optimizer.
    h=water_fill([10,4,1],[1,.5,1],4)
    assert abs(benefit([10,4,1],[1,.5,1],h)-11.299328740623613)<1e-9
    allocation,summaryA=allocation_experiment()
    queues,summaryQ=queue_experiment()
    report={'status':'synthetic sensitivity runs complete; deterministic assertions passed',
      'environment':{'python':platform.python_version(),'dependencies':'standard library only'},
      'scope':'No empirical reviewer behavior, legal compliance, calibrated utility, or validated superiority claim',
      'configuration':{'allocation':{'n':80,'seeds':list(range(42000,42030)),'H':[20,80],'potential_lognormal':[0,1],'productivity_lognormal':[-.2,.5],
      'baseline_blindspot':.1,'ignored_blindspot_underserved':.8,'underserved_fraction':.25,'reserve_fraction':.2,'coverage_threshold_hours':.25},
      'queue':{'seeds':list(range(71000,71030)),'days':365,'capacity_hours_day':8,'arrival':'Poisson; lambda=baseline_primary_load*8/2*arrival_multiplier',
      'primary_service':'Exponential mean 2*primary_cost_multiplier hours','appeal_probability':.1,'appeal_hours':'min(8, .5*Pareto(shape=1.5))',
      'admission':'one-day estimated work reservation, subtracting actual current backlog; rejected tasks not queued'}},
      'uncertainty':'Across-seed standard errors and descriptive normal-approximate intervals; not simultaneous confidence coverage or population inference',
      'rows':{'allocation':len(allocation),'queues':len(queues)},'allocation_summary':summaryA,'queue_summary':summaryQ,
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'data_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.glob('*.csv'))}}
    (ROOT/'results.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'status':report['status'],'rows':report['rows']}))

if __name__=='__main__':main()
