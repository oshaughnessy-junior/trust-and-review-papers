"""Regenerate bounded synthetic results; run from any working directory."""
from __future__ import annotations
import csv
import hashlib
import json
import platform
from pathlib import Path

from dynamics import (assignment, effective_reviewers, imported_mass, reconsideration_load,
                      stationary, trajectory)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results'


def save_csv(name, rows):
    with (OUT/name).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n")
        writer.writeheader();writer.writerows(rows)


def main():
    OUT.mkdir(exist_ok=True)
    influence=[]
    for a in [.5,.85,.95]:
        for eps in [0,.001,.01,.05,.1,.5,1]:
            p=stationary([[1-eps,eps],[0,1]],[1,0],a)[1]
            influence.append(dict(alpha=a,ingress=eps,analytic=imported_mass(a,eps),iterated=p))
    save_csv('influence.csv',influence)
    feedback=[]
    for k in [2,4,8]:
        for chi in [0,.5,1]:
            for z in [0,.1,.3]:
                for beta in [1,2,3,4,6,8,12,20]:
                    uniform=[1/k]*k;uniform[0]+=.001;uniform[1]-=.001
                    concentrated=[.9]+[.1/(k-1)]*(k-1)
                    for label,initial in [('near_uniform',uniform),('concentrated',concentrated)]:
                        x=trajectory(initial,beta,chi,z,[0]*k,steps=12000)
                        a=assignment(x,beta,chi,z,[0]*k)
                        feedback.append(dict(groups=k,beta=beta,chi=chi,exploration=z,
                            initial=label,local_eigenvalue=(1-z)*beta*chi/k-1,
                            max_share=max(x),hhi=sum(v*v for v in x),
                            residual_inf=max(abs(v-w) for v,w in zip(a,x))))
    save_csv('feedback.csv',feedback)
    save_csv('correlation.csv',[dict(reviewers=n,correlation=r,effective_n=effective_reviewers(n,r))
        for n in [1,2,5,10,20,100] for r in [0,.05,.2,.5,1]])
    save_csv('cascade.csv',[dict(branching=b,susceptibility=q,coalescing=c,
        reproduction=b*q*(1-c),expected_tickets=reconsideration_load(b,q,c))
        for b in [1,2,5,10] for q in [.05,.1,.2,.5] for c in [0,.5,.8]])
    # A numerical convergence check, not a proof of phase structure.
    x1=trajectory([.501,.499],4,1,.1,[0,0],steps=12000,dt=.02)
    x2=trajectory([.501,.499],4,1,.1,[0,0],steps=24000,dt=.01)
    result={
        'schema':'mcrp-hardening.synthetic-models.v1',
        'interpretation':'Toy analytical model checks, not observed human or agent behavior',
        'environment':{'python':platform.python_version(),'implementation':platform.python_implementation()},
        'randomness':'No stochastic draws in these sweeps; randomized tests use explicit fixed seeds',
        'sweep_rows':{'influence':len(influence),'feedback':len(feedback),'correlation':30,'cascade':48},
        'integration':{'method':'Euler convex update','steps':12000,'dt':.02,
                       'two_step_size_max_difference':max(abs(a-b) for a,b in zip(x1,x2)),
                       'step_size_check_scope':'Only K=2 beta=4 chi=1 zeta=.1 near-uniform start',
                       'max_sweep_residual':max(r['residual_inf'] for r in feedback),
                       'warning':'Finite-horizon trajectories; residuals reported, no claim all rows converged'},
        'highlight':{
            'alpha085_ingress001':imported_mass(.85,.01),
            'raw_capacity_counterexample':{'raw_edge':.001,'normalized_ingress':1,'stationary_external':.85},
            'n20_rho02_effective_n':effective_reviewers(20,.2),
            'feedback_k2_beta4_chi1_zeta01':x1,
            'cascade_b2_q02':reconsideration_load(2,.2)},
        'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'models').glob('*.py'))},
        'data_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.glob('*.csv'))}
    }
    (OUT/'manifest.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result['highlight'],indent=2))


if __name__=='__main__':main()
