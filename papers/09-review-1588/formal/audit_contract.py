"""Exact one-shot feasibility with explicitly separate budget contracts."""
from fractions import Fraction as F
from itertools import combinations
import json


def rational(value, probability=False):
    if isinstance(value,bool) or not isinstance(value,(int,F,str)):
        raise ValueError('exact integer/Fraction/rational-string inputs required')
    value=F(value)
    if value<0 or (probability and value>1):raise ValueError('outside range')
    return value


def cap(n,a,budget,kind):
    if type(n) is not int or n<1:raise ValueError('positive integer invitation population')
    a,budget=rational(a),rational(budget)
    if kind not in ('expected','hard'):raise ValueError('explicit budget contract required')
    if a==0:return F(1)
    return min(F(1),budget/(n*a)) if kind=='expected' else F(min(n,budget//a),n)


def interval(c,R,F_loss,alpha,beta,u,n,a,budget,kind):
    c,R,F_loss,u=map(rational,(c,R,F_loss,u))
    alpha,beta=rational(alpha,True),rational(beta,True)
    lower,upper=F(0),cap(n,a,budget,kind)
    d=(beta-alpha)*F_loss; h=alpha*F_loss; v=R-c-u
    if d>0:lower=max(lower,c/d)
    elif c>0:return None
    elif d<0:upper=F(0)
    if h>0:upper=min(upper,v/h)
    elif v<0:return None
    return (lower,upper) if lower<=upper else None


def direct_weak_best(q,c,R,F_loss,alpha,beta,u):
    """Independent utility calculation for exact fixture inputs."""
    honest=R-c-q*alpha*F_loss
    shirk=R-q*beta*F_loss
    return honest>=shirk and honest>=u


def hard_lottery(n,q,a,budget):
    """Exact distribution over concealed audit sets; intended for tiny examples."""
    q=rational(q,True)
    if n>12:raise ValueError('finite subset enumeration capped at 12 actors')
    if q>cap(n,a,budget,'hard'):raise ValueError('infeasible hard marginal')
    target=n*q; low=target.numerator//target.denominator; remainder=target-low
    distribution={}
    for k,weight in ((low,1-remainder),(low+1,remainder)):
        if not weight:continue
        sets=list(combinations(range(n),k))
        for subset in sets:distribution[subset]=weight/len(sets)
    return distribution


def demo():
    params=(F(1,5),F(1),F(2),F(1,50),F(4,5),F(1,10),3,F(1),F(3,2))
    render=lambda answer:None if answer is None else [str(v) for v in answer]
    lottery=hard_lottery(3,F(1,4),1,F(3,2))
    return {'budget_example':{'N':3,'audit_cost':'1','budget':'3/2',
                             'expected_interval':render(interval(*params,'expected')),
                             'hard_interval':render(interval(*params,'hard'))},
            'hard_q_quarter_distribution':[{'audited':list(s),'probability':str(p)} for s,p in lottery.items()],
            'interpretation':'Exact weak best-response feasibility; not empirical uptake or realized honesty.'}

if __name__=='__main__':print(json.dumps(demo(),indent=2))
