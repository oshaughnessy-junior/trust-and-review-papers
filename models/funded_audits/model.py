"""Closed-loop synthetic audit delivery with frozen invitation population.

No real assets, identities, authority or sanctions. Standard library, Python3.9+.
"""
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
import importlib.util
from itertools import combinations
import math
from pathlib import Path
import random

MATH_PATH=Path(__file__).resolve().parents[1]/'math'/'protocol_math.py'
_spec=importlib.util.spec_from_file_location('funded_protocol_math',MATH_PATH)
_math=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(_math)


@dataclass(frozen=True)
class Config:
    offered_population: int = 8
    promised_quota: int = 4
    delivered_quota: int = 4
    reward: float = .6
    loss: float = 2.
    false_positive: float = .02
    detection: float = .8
    audit_token_cost: float = 1.
    audit_token_budget: float = 4.
    reward_token_budget: float = 4.8
    actor_escrow: float = 2.
    review_hours: float = 1.
    audit_hours: float = .5
    role_mode: str = 'dedicated'
    review_capacity: float = 8.
    audit_capacity: float = 2.
    shared_person_capacity: float = 6.
    disclose_selection: bool = False
    allow_broken_promise: bool = False

    def __post_init__(self):
        # Dyadic quota fractions ensure the existing float sampler represents k/N
        # exactly. These are deliberately small demonstration population sizes.
        if type(self.offered_population) is not int or self.offered_population not in (2,4,8,16):raise ValueError('population must be2,4,8,16')
        for k in (self.promised_quota,self.delivered_quota):
            if type(k) is not int or not 0<=k<=self.offered_population:raise ValueError('invalid quota')
        if self.role_mode not in ('dedicated','shared_cross','self_audit'):raise ValueError('unknown role mode')
        for name in ('reward','loss','false_positive','detection','audit_token_cost','audit_token_budget','reward_token_budget',
                     'actor_escrow','review_hours','audit_hours','review_capacity','audit_capacity','shared_person_capacity'):
            value=getattr(self,name)
            if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:raise ValueError(name)
        if max(self.false_positive,self.detection)>1 or not self.audit_token_cost or not self.review_hours or not self.audit_hours:
            raise ValueError('invalid probability or nonpositive unit cost')
        if type(self.disclose_selection) is not bool or type(self.allow_broken_promise) is not bool:raise ValueError('boolean flags required')


def exact_hours(value):
    if isinstance(value,bool) or not isinstance(value,(int,float,Fraction)):
        raise ValueError('hours must be finite nonnegative numbers')
    if isinstance(value,float) and not math.isfinite(value):raise ValueError('invalid hours')
    result=value if isinstance(value,Fraction) else Fraction(str(value))
    if result<0:raise ValueError('negative hours')
    return result


class ResourceLedger:
    """One exact decimal-rational hour ledger; no epsilon permits overspending."""
    def __init__(self, capacity):
        if not capacity or any(not isinstance(p,str) or not p for p in capacity):raise ValueError('invalid capacity keys')
        self.capacity={p:exact_hours(h) for p,h in capacity.items()}
        self.reserved={p:Fraction(0) for p in capacity};self.used={p:Fraction(0) for p in capacity}
        self.lanes=Counter();self.active=False
    def reserve_program(self,demand):
        if self.active:raise ValueError('program already reserved')
        if any(p not in self.capacity for p in demand):raise ValueError('bad demand key')
        exact={p:exact_hours(h) for p,h in demand.items()}
        if any(h>self.capacity[p] for p,h in exact.items()):return False
        self.reserved.update(exact);self.active=True;return True
    def spend(self,person,hours,lane):
        if not self.active or person not in self.capacity:raise ValueError('invalid debit')
        debit=exact_hours(hours)
        if self.used[person]+debit>self.reserved[person]:raise ValueError('debit exceeds reservation')
        self.used[person]+=debit;self.lanes[(person,lane)]+=debit
    def report(self):
        return [{'person':p,'capacity_hours':float(self.capacity[p]),'reserved_hours':float(self.reserved[p]),
                 'spent_hours':float(self.used[p]),'released_hours':float(self.reserved[p]-self.used[p]),
                 'exact_hours':{'capacity':str(self.capacity[p]),'reserved':str(self.reserved[p]),'spent':str(self.used[p])},
                 'lanes':{lane:float(h) for (who,lane),h in sorted(self.lanes.items()) if who==p}}
                for p in sorted(self.capacity)]


def people(config,index):
    if config.role_mode=='dedicated':return 'reviewer','auditor'
    if config.role_mode=='self_audit':return 'P'+str(index%2),'P'+str(index%2)
    return 'P'+str(index%2),'P'+str(1-index%2)


def plan(config):
    N=config.offered_population;k=config.delivered_quota
    if config.role_mode=='dedicated':
        capacity={'reviewer':config.review_capacity,'auditor':config.audit_capacity}
        reservation={'reviewer':N*exact_hours(config.review_hours),'auditor':k*exact_hours(config.audit_hours)}
    else:
        capacity={p:config.shared_person_capacity for p in ('P0','P1')}
        # Reserve each person's worst case over ALL quota subsets before drawing.
        # This may reserve redundant slack but never conditions the lottery on capacity.
        reservation={p:(N//2)*exact_hours(config.review_hours)+min(k,N//2)*exact_hours(config.audit_hours) for p in capacity}
    if config.role_mode=='self_audit' and k:return None,'independent audit capacity unavailable'
    if config.promised_quota!=k and not config.allow_broken_promise:return None,'promised quota differs from delivery plan'
    if Fraction(str(config.audit_token_cost))*k>Fraction(str(config.audit_token_budget)):
        return None,'audit token budget unavailable'
    if Fraction(str(config.reward))*N>Fraction(str(config.reward_token_budget)):
        return None,'reward token budget unavailable'
    if config.actor_escrow<config.loss:return None,'fully collateralized toy loss unavailable'
    ledger=ResourceLedger(capacity)
    if not ledger.reserve_program(reservation):return None,'shared person-hour capacity unavailable'
    return ledger,None


def utilities(config,effort,outside,q):
    # Preferences are exact rational interpretations of declared decimal inputs.
    # Binary rounding must not silently override the stated tie-breaking rule.
    R,c,u,F,alpha,beta,p=(Fraction(str(v)) for v in
        (config.reward,effort,outside,config.loss,config.false_positive,config.detection,q))
    return {'honest':R-c-p*alpha*F,'shallow':R-p*beta*F,'refuse':u}


def best_response(values):return max(('refuse','honest','shallow'),key=lambda a:values[a])


def run(config=Config(),seed=1,efforts=None,outside_options=None):
    N=config.offered_population
    efforts=list(efforts) if efforts is not None else [.3]*N
    outside=list(outside_options) if outside_options is not None else [.1]*N
    if len(efforts)!=N or len(outside)!=N or any(isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<0 for v in efforts+outside):
        raise ValueError('nonnegative finite utility vectors must match offered population')
    ledger,reason=plan(config)
    common={'schema':'mcrp-funded-audit.v1','config':config.__dict__,'seed':seed,
            'offered_effort_utilities':efforts,'offered_outside_utilities':outside}
    if reason:
        return {**common,'status':'unavailable_before_offering','reason':reason,
                'counts':{'planned_population':N,'offered':0,'accepted':0,'completed':0,'audited':0,'refused':0},
                'events':[{'event':'program_unavailable','reason':reason}],
                'interpretation':'No invitations or audit promise issued by the conforming branch'}
    rng=random.Random(seed)
    actual_q=config.delivered_quota/N;promised_q=config.promised_quota/N
    selected=_math.blinded_audit_sample(N,actual_q,config.audit_token_cost,config.audit_token_budget,rng)
    selected=set(selected)
    if len(selected)!=config.delivered_quota:raise AssertionError('nonexact quota in dyadic population')
    counts=Counter(planned_population=N,offered=N,selected_audit_slots=len(selected));events=[];actors=[]
    token_audits=Fraction(0);token_rewards=Fraction(0);penalty_tokens=Fraction(0);regret=Fraction(0)
    # All choices commit before any completion or audit outcome is exposed.
    committed=[]
    for i in range(N):
        decision_q=float(i in selected) if config.disclose_selection else promised_q
        advertised=utilities(config,efforts[i],outside[i],decision_q)
        action=best_response(advertised)
        committed.append((decision_q,advertised,action))
        events.append({'event':'decision_commit','actor':i,'action':action,'decision_q':decision_q,
                       'selection_disclosed':config.disclose_selection})
    for i in range(N):
        review_person,audit_person=people(config,i)
        decision_q,advertised,action=committed[i]
        true_q=float(i in selected) if config.disclose_selection else actual_q
        actual_expected=utilities(config,efforts[i],outside[i],true_q)
        regret+=max(actual_expected.values())-actual_expected[action]
        counts[action]+=1
        record={'actor':i,'review_person':review_person,'audit_person':audit_person,'action':action,
                'decision_q':decision_q,'audit_slot_selected':i in selected,'audited':False,
                'sanctioned':False,'advertised_utilities':{k:float(v) for k,v in advertised.items()},
                'actual_expected_utilities':{k:float(v) for k,v in actual_expected.items()},
                'exact_advertised_utilities':{k:str(v) for k,v in advertised.items()},
                'closing_escrow':config.actor_escrow,'reward_received':0.}
        if action=='refuse':
            counts['refused']+=1
            counts['unused_refused_audit_slots']+=int(i in selected)
            record['realized_utility']=outside[i]
            events.append({'event':'refuse','actor':i,'selected_slot_unused':i in selected})
            actors.append(record);continue
        counts['accepted']+=1;counts['completed']+=1
        # Honest and shallow both consume a booked review slot; utility effort cost
        # is not converted into conserved human hours. No productivity benefit assumed.
        ledger.spend(review_person,config.review_hours,'review')
        token_rewards+=Fraction(str(config.reward));record['reward_received']=config.reward
        events.append({'event':'complete','actor':i,'action':action,'person':review_person,'hours':config.review_hours})
        sanctioned=False
        if i in selected:
            if review_person==audit_person:raise AssertionError('self-audit cannot execute')
            ledger.spend(audit_person,config.audit_hours,'audit')
            token_audits+=Fraction(str(config.audit_token_cost));counts['audited']+=1
            sanctioned=rng.random()<(config.false_positive if action=='honest' else config.detection)
            record['audited']=True;record['sanctioned']=sanctioned
            events.append({'event':'audit','actor':i,'person':audit_person,'hours':config.audit_hours,'sanctioned':sanctioned})
        if sanctioned:
            counts['sanctioned']+=1;counts['false_sanctions' if action=='honest' else 'detected_shallow']+=1
            penalty_tokens+=Fraction(str(config.loss));record['closing_escrow']=float(Fraction(str(config.actor_escrow))-Fraction(str(config.loss)))
        record['realized_utility']=float(Fraction(str(config.reward))-(Fraction(str(efforts[i])) if action=='honest' else 0)-Fraction(str(config.loss))*sanctioned)
        actors.append(record)
    for key in ('accepted','completed','audited','refused','honest','shallow','false_sanctions','detected_shallow','unused_refused_audit_slots','sanctioned'):counts[key]+=0
    assert counts['offered']==counts['completed']+counts['refused']
    assert counts['selected_audit_slots']==counts['audited']+counts['unused_refused_audit_slots']
    assert token_audits<=Fraction(str(config.audit_token_budget))
    assert token_rewards<=Fraction(str(config.reward_token_budget))
    assert all(row['released_hours']>=0 for row in ledger.report())
    return {**common,'status':'executed_broken_promise_negative_control' if config.promised_quota!=config.delivered_quota else 'executed',
            'promised_q_if_participating_concealed':promised_q,'delivered_selection_marginal':actual_q,
            'counts':dict(sorted(counts.items())),'actors':actors,'events':events,'person_ledger':ledger.report(),
            'tokens':{'audit_spent':float(token_audits),'audit_reserved':config.delivered_quota*config.audit_token_cost,
                      'audit_budget_remaining':float(Fraction(str(config.audit_token_budget))-token_audits),
                      'reward_spent':float(token_rewards),'reward_reserved':float(Fraction(str(config.reward))*N),
                      'reward_budget_remaining':float(Fraction(str(config.reward_token_budget))-token_rewards),'penalties_quarantined':float(penalty_tokens),
                      'escrow_opening_total':float(N*Fraction(str(config.actor_escrow))),
                      'escrow_closing_total':float(N*Fraction(str(config.actor_escrow))-penalty_tokens),
                      'penalties_recycled_into_budget':False},
            'aggregate_expected_utility_regret_under_actual_information':float(regret),
            'interpretation':'Synthetic funded delivery with fixed actors and fully collateralized token losses; no real assets, consent, identity verification, legal authority or cooperation equilibrium'}


def exact_selection_marginals(N,k):
    subsets=list(combinations(range(N),k))
    return [Fraction(sum(i in s for s in subsets),len(subsets)) for i in range(N)]
