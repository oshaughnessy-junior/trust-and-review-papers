"""Exact, stipulated decision costs; not estimated scientific reliability."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

def frac(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)): raise ValueError('exact rational input required')
    return F(x)

def benefit(prevalence,q0,q1,a0,a1,loss,false_alarm_cost,savings,cost):
    p,q0,q1,a0,a1=map(frac,(prevalence,q0,q1,a0,a1))
    loss,false_alarm_cost,savings,cost=map(frac,(loss,false_alarm_cost,savings,cost))
    if any(not 0<=v<=1 for v in (p,q0,q1,a0,a1)):raise ValueError('probabilities must be in [0,1]')
    if min(loss,false_alarm_cost,savings,cost)<0:raise ValueError('costs and savings must be nonnegative')
    return savings+p*loss*(q0-q1)-(1-p)*false_alarm_cost*(a1-a0)-cost

def posterior(p,q,a):
    p,q,a=map(frac,(p,q,a))
    if any(not 0<=v<=1 for v in (p,q,a)):raise ValueError('probabilities must be in [0,1]')
    mass=p*q+(1-p)*(1-a)
    return None if mass==0 else p*q/mass

def robust_benefit(intervals,loss,false_alarm_cost,savings,cost):
    if len(intervals)!=5:raise ValueError('five probability intervals required')
    bounds=[]
    for pair in intervals:
        if len(pair)!=2:raise ValueError('interval requires two endpoints')
        lo,hi=map(frac,pair)
        if not 0<=lo<=hi<=1:raise ValueError('invalid interval')
        bounds.append((lo,hi))
    vals=[benefit(*v,loss,false_alarm_cost,savings,cost) for v in product(*bounds)]
    return min(vals),max(vals)

def scenarios():
    q0=F(28,100);q1=F(1,10)+F(9,10)*F(1,5)**5
    a0=F(1,50);a1=1-F(49,50)**5
    rows=[]
    for p in [F(1,1000),F(1,20)]:
        delta=benefit(p,q0,q1,a0,a1,100,5,0,F(1,5))
        rows.append(dict(prevalence=str(p),baseline_false_clear=str(q0),new_false_clear=str(q1),new_false_alarm=str(a1),net_benefit=str(delta),net_benefit_decimal=float(delta),invalid_given_clear=str(posterior(p,q1,a1))))
    return {'kind':'stipulated_exact_decision_example','not_empirical':True,'scenarios':rows}
if __name__=='__main__':
    Path(__file__).with_name('results.json').write_text(json.dumps(scenarios(),indent=2)+'\n')
