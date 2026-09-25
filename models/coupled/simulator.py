"""Coupled synthetic toy-agent workflow. One person/epoch ledger, no services.

All controls, skills, utilities and dependencies are generated fixture inputs.
The simulator's ground truth is an evaluator oracle, unavailable to a real router.
"""
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
import math
import random


@dataclass(frozen=True)
class Config:
    policy: str = 'group_first'
    retry: str = 'reroll'
    clones: int = 1
    capacity: float = 8.0
    requests: int = 12
    attempts: int = 3
    reliance_filter: str = 'all'
    hidden_control: bool = False
    reserve_repair: bool = False

    def __post_init__(self):
        if self.policy not in ('group_first','naive') or self.retry not in ('reroll','fixed_panel'):
            raise ValueError('unknown policy')
        if self.reliance_filter not in ('all','A_only'):
            raise ValueError('unknown reliance filter')
        for name in ('clones','requests','attempts'):
            x=getattr(self,name)
            if isinstance(x,bool) or not isinstance(x,int) or x<1: raise ValueError(name)
        if isinstance(self.capacity,bool) or not math.isfinite(self.capacity) or self.capacity<=0:
            raise ValueError('positive finite capacity required')
        if self.reserve_repair and self.capacity<1: raise ValueError('repair reserve needs one hour per protected person')


class Ledger:
    """Atomic holds shared by all lanes, released once with actual nonnegative use."""
    def __init__(self, capacities):
        self.capacity=dict(capacities)
        if not self.capacity or any(isinstance(v,bool) or not math.isfinite(v) or v<0 for v in self.capacity.values()):
            raise ValueError('invalid capacities')
        self.used={p:0. for p in capacities}
        self.held={p:0. for p in capacities}
        self.holds={}; self.lanes=Counter(); self.serial=0

    def reserve(self, demand):
        if any(p not in self.capacity or isinstance(v,bool) or not math.isfinite(v) or v<0 for p,v in demand.items()):
            raise ValueError('invalid demand')
        if any(self.used[p]+self.held[p]+h>self.capacity[p]+1e-12 for p,h in demand.items()): return None
        self.serial+=1; token=self.serial
        self.holds[token]=dict(demand)
        for p,h in demand.items(): self.held[p]+=h
        return token

    def settle(self, token, actual, lane):
        if token not in self.holds: raise ValueError('unknown or already settled hold')
        reserved=self.holds[token]
        if any(p not in reserved or isinstance(v,bool) or not math.isfinite(v) or v<0 or v>reserved[p] for p,v in actual.items()):
            raise ValueError('actual exceeds reservation')
        for p,h in reserved.items(): self.held[p]-=h
        for p,h in actual.items(): self.used[p]+=h; self.lanes[(p,lane)]+=h
        del self.holds[token]

    def charge(self, demand, lane):
        token=self.reserve(demand)
        if token is None:return False
        self.settle(token,demand,lane);return True

    def report(self):
        return [{'person':p,'capacity':self.capacity[p],'used':self.used[p],'held':self.held[p],
                 'remaining':self.capacity[p]-self.used[p]-self.held[p],
                 'lanes':{lane:h for (who,lane),h in sorted(self.lanes.items()) if who==p}}
                for p in sorted(self.capacity)]


def distribution(config):
    counts={'A':config.clones,'B':1,'C':1}
    if config.hidden_control: counts={'A1':config.clones,'A2':1,'B':1,'C':1}
    weights={panel:1 if config.policy=='group_first' else math.prod(counts[g] for g in panel)
             for panel in combinations(sorted(counts),2)}
    total=sum(weights.values())
    return {p:Fraction(w,total) for p,w in weights.items()}


def draw_panel(config,rng):
    dist=distribution(config)
    # Exact integer-weight draw: avoid clone-dependent roundoff or expanded lists.
    denominator=math.lcm(*(p.denominator for p in dist.values()))
    ticket=rng.randrange(denominator)
    for panel,p in dist.items():
        ticket-=p.numerator*(denominator//p.denominator)
        if ticket<0:return panel
    raise AssertionError('unreachable draw')


def person(group): return 'A' if group.startswith('A') else group

def risky(panel): return any(person(g)=='A' for g in panel)


def choose_action(who, request, fatigue, rng):
    """Hypothetical best response. Outside option varies by invitation.

    No real audit mechanism is run in this simulator; q is an exogenous perceived
    monitoring belief. Hypothetical utility units are not ledger hours.
    """
    reward=.8; q=.2; loss=2; alpha=.02; beta=.8
    effort={'A':.12,'B':.44,'C':.23}[who]+.04*(request%3)+.012*fatigue
    outside={'A':.05,'B':.4,'C':.12}[who]+rng.uniform(0,.25)
    utilities={'honest':reward-effort-q*alpha*loss,'shallow':reward-q*beta*loss,'refuse':outside}
    action=max(('refuse','honest','shallow'),key=lambda x:utilities[x])
    if action=='refuse': return action,False,.05,utilities
    complete=rng.random()<(.95 if action=='honest' else .98)
    return action,complete,(1. if action=='honest' else .25),utilities


def descendants(root, edges):
    seen={root}; queue=[root]
    for current in queue:
        for src,dst in edges:
            if src==current and dst not in seen:seen.add(dst);queue.append(dst)
    return seen


def run(config=Config(), seed=1, trace=False, behavior=None):
    rng=random.Random(seed)
    behavior = choose_action if behavior is None else behavior
    ledger=Ledger({p:config.capacity for p in ('A','B','C','steward')})
    repair_hold=ledger.reserve({'A':1.,'C':1.}) if config.reserve_repair else None
    events=[]; receipts=[]; counts=Counter(); reached={k:set() for k in ('eligible','selected','reserved','invited','accepted','completed','relied')}
    def event(kind,**fields):
        if trace:events.append({'sequence':len(events),'event':kind,**fields})
    for request in range(config.requests):
        counts['offered_requests']+=1
        target=f'claim-{request}:v1'; event('offer',request=request,target=target,scope='synthetic numerical check')
        if not ledger.charge({'steward':.05},'intake'):
            counts['intake_capacity_rejections']+=1;event('intake_capacity_unavailable',request=request);continue
        reached['eligible'].add(request)
        fixed=None
        for attempt in range(config.attempts):
            counts['selection_attempts']+=1
            if attempt: counts['retry_attempts']+=1
            if fixed is None or config.retry=='reroll': panel=draw_panel(config,rng)
            else: panel=fixed
            if fixed is None:
                fixed=panel;counts['initial_panels']+=1;counts['A_initial_panels']+=int(risky(panel))
            reached['selected'].add(request)
            counts['selected_panels']+=1;counts['A_selected_panels']+=int(risky(panel))
            event('select',request=request,attempt=attempt,panel=panel)
            if not ledger.charge({'steward':.02},'reservation_triage'):
                counts['triage_capacity_rejections']+=1;break
            demand=Counter({'steward':.1})
            for group in panel:demand[person(group)]+=1.
            token=ledger.reserve(dict(demand))
            if token is None:
                counts['reservation_failures']+=1;event('reservation_failed',request=request,attempt=attempt,panel=panel);continue
            counts['reserved_panels']+=1;counts['A_reserved_panels']+=int(risky(panel));reached['reserved'].add(request)
            counts['invited_panels']+=1;counts['invited_actors']+=len(panel);reached['invited'].add(request)
            actual=Counter({'steward':.1});outcomes=[]
            for group in panel:
                who=person(group)
                action,done,hours,utilities=behavior(who,request,ledger.used[who],rng)
                if action not in ('honest','shallow','refuse') or not isinstance(done,bool) or (action=='refuse' and done):
                    raise ValueError('inconsistent behavior action/completion')
                if isinstance(hours,bool) or not isinstance(hours,(int,float)) or not math.isfinite(hours) or not 0<=hours<=1:
                    raise ValueError('behavior must fit one-hour reservation')
                actual[who]+=hours
                counts[action+'_actors']+=1
                counts['accepted_actors']+=int(action!='refuse');counts['completed_actors']+=int(done)
                outcomes.append((group,action,done))
                event('actor_response',request=request,attempt=attempt,group=group,true_person=who,action=action,reported_complete=done,hours=hours,utilities=utilities)
            ledger.settle(token,dict(actual),'check_and_invitation')
            accepted=all(action!='refuse' for _,action,_ in outcomes)
            completed=all(done for _,_,done in outcomes)
            if accepted:counts['accepted_panels']+=1;reached['accepted'].add(request)
            if not completed:counts['incomplete_panels']+=1;continue
            counts['completed_panels']+=1;counts['A_completed_panels']+=int(risky(panel));reached['completed'].add(request)
            # Completion is a report. Latent honest effort and true control are evaluation-only.
            full_effort=all(action=='honest' for _,action,_ in outcomes)
            independent=len({person(g) for g in panel})==2
            counts['full_effort_completed_panels']+=int(full_effort)
            counts['true_independent_completed_panels']+=int(independent)
            relies=config.reliance_filter=='all' or risky(panel)
            if relies:
                if ledger.charge({'steward':.1},'reliance'):
                    counts['relied_panels']+=1;counts['A_relied_panels']+=int(risky(panel));reached['relied'].add(request)
                    receipts.append({'request':request,'target':target,'scope':'toy numerical decision only','decision_actor':'synthetic steward',
                                     'declared_groups':list(panel),'oracle_full_effort':full_effort,'oracle_independent':independent,
                                     'currentness':'as_recorded','repair':'not_affected'})
                    event('rely',request=request,target=target,scope='toy numerical decision only')
                else:counts['reliance_capacity_rejections']+=1
            else:counts['completed_not_selected_for_reliance']+=1
            break
    # A material root change affects a true chain. Every fourth edge is omitted
    # from the declared graph; the oracle can measure missed awareness.
    true_edges=[(i-1,i) for i in range(1,config.requests)]
    declared_edges=[edge for edge in true_edges if edge[1]%4!=0]
    actual_affected=descendants(0,true_edges);known_affected=descendants(0,declared_edges)
    if repair_hold is not None:ledger.settle(repair_hold,{},'repair_reserve_release')
    event('amend',target='claim-0:v1',known_affected=sorted(known_affected))
    for receipt in receipts:
        if receipt['request'] not in actual_affected:continue
        counts['oracle_affected_reliances']+=1
        if receipt['request'] not in known_affected:
            counts['unnoticed_affected_reliances']+=1;receipt['repair']='undiscovered_dependency';continue
        counts['noticed_affected_reliances']+=1
        receipt['currentness']='unresolved_material_change'
        token=ledger.reserve({'A':.5,'C':.5,'steward':.1})
        if token is None:
            counts['pending_repairs']+=1;receipt['repair']='capacity_unavailable'
            event('repair_pending',request=receipt['request']);continue
        ledger.settle(token,{'A':.5,'C':.5,'steward':.1},'repair')
        counts['repaired_reliances']+=1;receipt['repair']='check_completed'
        # Repair work alone is not authorized renewal; the receipt stays unresolved.
        event('repair_check',request=receipt['request'],renewal_required=True)
    for stage,ids in reached.items():counts[stage+'_requests']=len(ids)
    counts['unresolved_requests']=config.requests-counts['completed_requests']
    counts['completed_without_reliance']=counts['completed_requests']-counts['relied_requests']
    counts['still_unresolved_reliances']=counts['noticed_affected_reliances']
    required=('reservation_failures','refuse_actors','retry_attempts','completed_panels','relied_panels','pending_repairs',
              'unnoticed_affected_reliances','repaired_reliances','noticed_affected_reliances','oracle_affected_reliances')
    for name in required:counts[name]+=0
    assert counts['offered_requests']==counts['completed_requests']+counts['unresolved_requests']
    assert counts['invited_actors']==counts['accepted_actors']+counts['refuse_actors']
    assert counts['oracle_affected_reliances']==counts['unnoticed_affected_reliances']+counts['pending_repairs']+counts['repaired_reliances']
    assert not ledger.holds
    assert all(row['remaining']>=-1e-10 for row in ledger.report())
    return {'config':config.__dict__,'seed':seed,'counts':dict(sorted(counts.items())),
            'ledger':ledger.report(),'receipts':receipts,'events':events,
            'graphs':{'true_edges':true_edges,'declared_edges':declared_edges},
            'total_hours':sum(ledger.used.values()),
            'limitation':'Synthetic utilities, declared controls, known toy skills; no authenticated authority, real audit delivery, independent review, human calibration or live currentness.'}


def one_request_oracle(config, completion_by_person):
    """Exact no-capacity-binding independent-completion special case.

    Enumerates each initially selected panel's geometric paths for fixed retry;
    reroll mixes each attempt. Does not model default utility-dependent behavior.
    """
    dist=distribution(config)
    probabilities={p:Fraction(completion_by_person[p]) for p in 'ABC'}
    if any(not 0<=v<=1 for v in probabilities.values()):raise ValueError('invalid probability')
    completion={panel:math.prod(probabilities[person(g)] for g in panel) for panel in dist}
    if any(not 0<=v<=1 for v in completion.values()):raise ValueError('invalid probability')
    L=config.attempts
    if config.retry=='reroll':
        success=sum(dist[p]*completion[p] for p in dist)
        risk=sum(dist[p]*completion[p] for p in dist if risky(p))
        attempts=sum((1-success)**j for j in range(L))
        complete=success*attempts;risky_complete=risk*attempts
    else:
        attempts=complete=risky_complete=Fraction(0)
        for panel,prob in dist.items():
            per=sum((1-completion[panel])**j for j in range(L))
            attempts+=prob*per
            mass=prob*completion[panel]*per
            complete+=mass;risky_complete+=mass*int(risky(panel))
    return {'completion':complete,'unresolved':1-complete,'expected_attempts':attempts,
            'risky_completed_share':risky_complete/complete if complete else None}
