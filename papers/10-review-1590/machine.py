"""Finite sequential toy event machine. Supplied roles/outcomes are assertions."""
from fractions import Fraction as F
from itertools import combinations
import copy, random

PANELS=tuple(combinations(('A','B','C'),2))

def rat(x):
    if type(x) is int or isinstance(x,F): return F(x)
    raise ValueError('Exact rational required')

def repair_bound(matrices, weights, initial):
    weights=tuple(rat(w) for w in weights);initial=tuple(rat(z) for z in initial)
    matrices=tuple(tuple(tuple(rat(v) for v in row) for row in m) for m in matrices)
    n=len(weights)
    if not n or len(initial)!=n or any(rat(w)<=0 for w in weights) or any(rat(z)<0 for z in initial):raise ValueError('Invalid workload/witness')
    if not matrices:raise ValueError('Empty envelope family')
    factors=[]
    for m in matrices:
        if len(m)!=n or any(len(row)!=n for row in m):raise ValueError('Matrix shape')
        for i,row in enumerate(m):
            if any(rat(v)<0 for v in row):raise ValueError('Negative offspring')
            factors.append(sum(v*w for v,w in zip(row,weights))/weights[i])
    r=max(factors)
    if r>=1: return {'certified':False,'r':r,'bound':None}
    return {'certified':True,'r':r,'bound':sum(z*w for z,w in zip(initial,weights))/(1-r)}

class Machine:
    def __init__(self, capacity=F(20), counts=None):
        self.capacity=rat(capacity)
        if self.capacity<0:raise ValueError('Negative capacity')
        self.counts=counts or {'A':1,'B':1,'C':1}
        if set(self.counts)!=set('ABC') or any(type(v) is not int or v<1 for v in self.counts.values()):raise ValueError('Counts')
        self.counts=dict(self.counts)
        self.offers={};self.events=[];self.seen=set();self.retired=set();self.introduced=set();self.spent=F(0);self.held=F(0);self.reliances=[]

    def apply(self, request, action, **data):
        if not isinstance(request,str) or not request or request in self.seen or len(self.events)>=64:raise ValueError('Event identity/limit')
        before=copy.deepcopy(self.__dict__)
        try:
            methods={'offer':self._offer,'check':self._check,'rely':self._rely,'amend':self._amend}
            if action not in methods:raise ValueError('Unknown action')
            payload=methods[action](**data)
            event={'seq':len(self.events)+1,'request':request,'action':action,**payload,
                   'spent_after':self.spent,'held_after':self.held}
            self.events.append(event);self.seen.add(request)
            if self.spent+self.held>self.capacity:raise ValueError('Shared work capacity violated')
            return copy.deepcopy(event)
        except Exception:
            self.__dict__=before
            raise

    def _offer(self, actor, target, scope, dependencies, seed=4, audit_q=F(1,3), audit_budget=F(1)):
        if actor!='author' or not all(isinstance(x,str) and x for x in (target,scope)) or target in self.offers or len(self.offers)>=8:raise ValueError('Offer identity/authority')
        if type(dependencies) is not tuple or any(not isinstance(d,str) or not d for d in dependencies) or len(set(dependencies))!=len(dependencies):raise ValueError('Dependencies')
        if any(d in self.retired or (d in self.offers and self.offers[d]['phase']!='ready') for d in dependencies):raise ValueError('Stale or unchecked declared dependency')
        if target in self.retired:raise ValueError('Retired target')
        if type(seed) is not int:raise ValueError('Seed')
        q,B=rat(audit_q),rat(audit_budget);N=3;a=F(1)
        # Fixed synthetic utility: c=.1,R=1,u=0,alpha=.05,beta=.85,F=1.
        if not 0<=q<=1 or B<0 or F(1,10)>q*F(4,5) or 1-F(1,10)-q*F(1,20)<0:raise ValueError('Audit incentive preflight')
        if N*q>min(N,B//a):raise ValueError('Hard audit cap preflight')
        max_audits=(N*q).__ceil__()
        reserve=F(33,10)+max_audits*a
        if self.spent+self.held+reserve>self.capacity:raise ValueError('Insufficient reserved work')
        rng=random.Random(seed)
        plans=[PANELS[rng.randrange(3)] for _ in range(N)]
        # Representative draws use a separate stream, so aliases cannot perturb Q.
        aliases=random.Random(seed+10000)
        representatives=[tuple(g+':'+str(aliases.randrange(self.counts[g])) for g in p) for p in plans]
        count=(N*q).__floor__();fraction=N*q-count
        count+=int(rng.randrange(fraction.denominator)<fraction.numerator)
        selected=set(rng.sample(range(N),count))
        self.offers[target]={'scope':scope,'dependencies':dependencies,'phase':'open','attempt':0,
                            'panels':plans,'representatives':representatives,'audits':selected,
                            'hold':reserve,'audit_spent':F(0),'audit_budget':B,'last_check':None}
        self.held+=reserve
        return {'actor':actor,'target':target,'scope':scope,'dependencies':dependencies,'panel_law':'uniform-AB-AC-BC',
                'incentive_scope':'ex-ante fixed actions only; not sequential incentive compatibility',
                'max_attempts':N,'audit_q':q,'audit_budget':B,'reservation':reserve}

    def planned_representatives(self,target):
        o=self.offers[target]
        if o['phase']!='open':raise ValueError('Not open')
        return tuple(o['representatives'][o['attempt']])

    def _close(self,o):
        self.held-=o['hold'];o['hold']=F(0)

    def _check(self, actor, target, scope, representatives, outcome, evidence, audit_clear=True):
        if actor!='verifier' or target not in self.offers:raise ValueError('Check authority/target')
        o=self.offers[target];i=o['attempt']
        if o['phase']!='open' or scope!=o['scope'] or representatives!=o['representatives'][i]:raise ValueError('Check state/scope/panel')
        if outcome not in ('refused','failed','passed') or type(audit_clear) is not bool:raise ValueError('Outcome')
        if not isinstance(evidence,str) or not evidence:raise ValueError('Evidence reference required')
        completed=outcome!='refused';audited=i in o['audits']
        charge=F(1,10)+int(completed)+int(audited)
        if charge>o['hold']:raise ValueError('Reservation exceeded')
        self.spent+=charge;self.held-=charge;o['hold']-=charge
        o['audit_spent']+=int(audited)
        if o['audit_spent']>o['audit_budget']:raise ValueError('Audit cap exceeded')
        o['attempt']+=1;o['last_check']=len(self.events)+1
        if completed:
            o['phase']='ready' if outcome=='passed' and (not audited or audit_clear) else 'failed'
            self._close(o)
        elif o['attempt']==3:
            o['phase']='exhausted';self._close(o)
        return {'actor':actor,'target':target,'scope':scope,'panel':o['panels'][i],
                'representatives':representatives,'attempt':i+1,'outcome':outcome,
                'evidence':evidence,'audit_executed':audited,'audit_clear':audit_clear if audited else None,
                'work_charge':charge,'phase':o['phase']}

    def _rely(self, actor, target, scope, check_seq):
        if actor!='decision-maker' or target not in self.offers:raise ValueError('Reliance authority/target')
        o=self.offers[target]
        if o['phase']!='ready' or scope!=o['scope'] or type(check_seq) is not int or check_seq!=o['last_check']:raise ValueError('Reliance check binding')
        row={'target':target,'scope':scope,'actor':actor,'check_seq':check_seq,'current':True}
        self.reliances.append(row)
        return copy.deepcopy(row)

    def _amend(self, actor, changed, successor, matrices, weights):
        if actor!='author' or not isinstance(changed,str) or not changed or not isinstance(successor,str) or not successor or successor==changed or changed in self.retired:raise ValueError('Amend authority/identity')
        known=set(self.offers)|self.retired|self.introduced|{d for o in self.offers.values() for d in o['dependencies']}
        if successor in known:raise ValueError('Successor identity already exists')
        self.introduced.add(successor)
        affected={t for t,o in self.offers.items() if t==changed or changed in o['dependencies']}
        while True:
            expanded=affected|{t for t,o in self.offers.items() if set(o['dependencies'])&affected}
            if expanded==affected:break
            affected=expanded
        try:
            bound=repair_bound(matrices,weights,(F(len(affected)),F(0)))
        except ValueError:
            bound={'certified':False,'r':None,'bound':None,'reason':'invalid supplied envelope'}
        self.retired.add(changed)
        for t in affected:
            o=self.offers[t];self._close(o);o['phase']='pending-amendment'
        for row in self.reliances:
            if row['target'] in affected:row['current']=False
        return {'actor':actor,'changed':changed,'successor':successor,'affected':tuple(sorted(affected)),
                'repair_plan':bound,'repair_reserved':0,'meaning':'reassessment-required-not-refutation'}
