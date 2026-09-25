"""Hypothetical local-rule attention ecology; no fitted human behavior."""
from __future__ import annotations
from dataclasses import dataclass, asdict
import math
import hashlib
import random

@dataclass(frozen=True)
class Config:
    seed: int = 1
    periods: int = 120
    arrival: float = .45
    exploration: float = .15
    reinforcement: float = 2.
    memory: float = .1
    audit_probability: float = .3
    blind_probability: float = .05
    repair_multiplier: float = 1.
    audit_bias: float = 0.

    def validate(self):
        if type(self.seed) is not int or type(self.periods) is not int or self.periods < 1:
            raise ValueError('integer seed and positive integer periods required')
        for key in ('arrival','exploration','memory','audit_probability','blind_probability','audit_bias'):
            x=getattr(self,key)
            if not math.isfinite(x) or not 0<=x<=1: raise ValueError(key)
        for key in ('reinforcement','repair_multiplier'):
            x=getattr(self,key)
            if not math.isfinite(x) or x<0: raise ValueError(key)

@dataclass(frozen=True)
class Agent:
    name: str
    capacity: int
    skills: tuple[str,...]
    volume: int
    defect_rate: float
    diligence: float

AGENTS=(Agent('large-team',40,('common','rare'),4,.2,.95),
        Agent('established',30,('common',),2,.15,.9),
        Agent('newcomer',20,('common',),1,.1,.9),
        Agent('rare-small',15,('rare',),1,.15,.9),
        Agent('low-resource',15,('common',),1,.15,.9),
        Agent('rare-newcomer',15,('rare',),1,.1,.9))

@dataclass
class Task:
    uid: int
    author: int
    skill: str
    defect: bool
    created: int


def probabilities(scores, exploration, beta):
    """Mixture with a uniform floor; stable softmax, even beta=large."""
    if not scores: return []
    if not 0<=exploration<=1 or not math.isfinite(beta) or beta<0 or any(not math.isfinite(s) for s in scores):
        raise ValueError('invalid probability inputs')
    maximum=max(scores)
    weights=[math.exp(beta*(s-maximum)) for s in scores]
    total=sum(weights)
    return [exploration/len(scores)+(1-exploration)*w/total for w in weights]


def select(rng, items, weights):
    threshold=rng.random()*sum(weights)
    for item,weight in zip(items,weights):
        threshold-=weight
        if threshold<0: return item
    return items[-1]


def simulate(config=Config(), policy='bounded', agents=AGENTS, trace=False):
    config.validate()
    if policy not in {'prestige','bounded','uniform'}: raise ValueError('policy')
    if len(agents)<2 or len({a.name for a in agents})!=len(agents): raise ValueError('actors')
    for a in agents:
        if type(a.capacity) is not int or a.capacity<0 or type(a.volume) is not int or a.volume<0 or not a.skills or not 0<=a.defect_rate<=1 or not 0<=a.diligence<=1:
            raise ValueError('agent')
    # Separate RNG streams keep exogenous offers/defects/blind periods matched
    # across policies. Process-dependent decisions necessarily diverge.
    arrivals=random.Random(config.seed)
    choice=random.Random(config.seed+1000003)
    signal=random.Random(config.seed+2000003)
    n=len(agents); scores=[1.]+[0.]*(n-1)
    queue=[]; repairs=[]; history=[]; offered=[0]*n; completed=[0]*n; reviewer_work=[0]*n
    counters={k:0 for k in ('correct_checks','incorrect_checks','defects_offered','defects_detected','false_alarms','audit_detected_defects','audited','repair_completed','audit_missed_capacity','refused_capacity','invitations','checks','intake_labor','check_labor','audit_labor','repair_labor','blind_periods')}
    offered_ids=[]; spent_total=[0]*n
    for tick in range(config.periods):
        remaining=[a.capacity for a in agents]; rewards=[0.]*n
        blind=arrivals.random()<config.blind_probability
        counters['blind_periods']+=blind
        for author,a in enumerate(agents):
            for _ in range(a.volume):
                if arrivals.random()<config.arrival:
                    skill=arrivals.choice(a.skills)
                    defect=arrivals.random()<a.defect_rate
                    uid=len(offered_ids); offered_ids.append((author,skill,defect,tick))
                    queue.append(Task(uid,author,skill,defect,tick)); offered[author]+=1
                    counters['defects_offered']+=defect
        # Oldest corrections get first access to the same expertise budget.
        repair_cost=max(1,math.ceil(20*config.repair_multiplier))
        unresolved=[]
        for task in repairs:
            feasible=[i for i,a in enumerate(agents) if i!=task.author and task.skill in a.skills and remaining[i]>=repair_cost]
            if feasible:
                handler=max(feasible,key=lambda i:remaining[i])
                remaining[handler]-=repair_cost; counters['repair_labor']+=repair_cost
                counters['repair_completed']+=1; rewards[handler]+=1; rewards[task.author]+=1
            else: unresolved.append(task)
        repairs=unresolved
        # At most one invitation per pending task per period. Refusals consume
        # intake when a qualified independent actor has those two units.
        pending=list(queue); processed=set()
        while pending:
            if max(remaining,default=0)<2:
                counters['refused_capacity']+=len(pending)
                break
            eligible_authors=sorted({t.author for t in pending})
            if policy=='prestige':
                # Volume multiplication is explicit: account-level attention and
                # cumulative visibility reinforce each other in this baseline.
                weights=probabilities([scores[a] for a in eligible_authors],config.exploration,config.reinforcement)
                weights=[w*sum(t.author==a for t in pending) for a,w in zip(eligible_authors,weights)]
            elif policy=='bounded':
                weights=probabilities([scores[a] for a in eligible_authors],config.exploration,config.reinforcement)
            else: weights=[1.]*len(eligible_authors)
            author=select(choice,eligible_authors,weights)
            task=next(t for t in pending if t.author==author); pending.remove(task)
            reviewers=[i for i,a in enumerate(agents) if i!=author and task.skill in a.skills and remaining[i]>=2]
            if not reviewers:
                counters['refused_capacity']+=1
                continue
            # A cheap intake attempt consumes actual capacity even when the
            # remaining check cannot be done; routing itself is costless here.
            reviewer=select(choice,reviewers,[remaining[i] for i in reviewers])
            remaining[reviewer]-=2; counters['intake_labor']+=2; counters['invitations']+=1
            if remaining[reviewer]<10:
                counters['refused_capacity']+=1
                continue
            remaining[reviewer]-=10; counters['check_labor']+=10; counters['checks']+=1
            reviewer_work[reviewer]+=1; completed[author]+=1; processed.add(task.uid)
            # Common-mode blind periods return support for every defect, while
            # ordinary checks have stipulated reviewer diligence.
            verdict_defect=False if blind else (task.defect if signal.random()<agents[reviewer].diligence else not task.defect)
            correct=verdict_defect==task.defect
            counters['correct_checks']+=correct; counters['incorrect_checks']+=not correct
            counters['defects_detected']+=verdict_defect and task.defect
            counters['false_alarms']+=verdict_defect and not task.defect
            if verdict_defect: repairs.append(task)
            if policy=='prestige': scores[author]+=1
            # Audit's truth is an idealized fixture oracle. It has real modeled
            # labor and excludes author/reviewer; access can favor established A.
            audit_p=config.audit_probability*(1-config.audit_bias if author else 1)
            if signal.random()<audit_p:
                auditors=[i for i,a in enumerate(agents) if i not in (author,reviewer) and task.skill in a.skills and remaining[i]>=5]
                if auditors:
                    auditor=max(auditors,key=lambda i:remaining[i]); remaining[auditor]-=5; counters['audit_labor']+=5; counters['audited']+=1
                    if correct: rewards[reviewer]+=1
                    if not task.defect: rewards[author]+=1
                    # A discovered false negative creates a repair obligation.
                    if task.defect and not verdict_defect:
                        repairs.append(task); counters['audit_detected_defects']+=1
                else: counters['audit_missed_capacity']+=1
        queue=[t for t in queue if t.uid not in processed]
        if policy=='bounded':
            scores=[(1-config.memory)*s+config.memory*min(1,r) for s,r in zip(scores,rewards)]
        spent=[a.capacity-r for a,r in zip(agents,remaining)]
        assert all(0<=x<=a.capacity for x,a in zip(spent,agents))
        spent_total=[a+b for a,b in zip(spent_total,spent)]
        if trace: history.append({'tick':tick,'queue':len(queue),'repair_backlog':len(repairs),'scores':scores[:],'spent':spent,'remaining':remaining})
    total=sum(offered); checked=sum(completed)
    shares=[c/checked if checked else 0 for c in completed]
    coverage=[c/o if o else None for c,o in zip(completed,offered)]
    return {'policy':policy,'config':asdict(config),'agents':[asdict(a) for a in agents],
        'offered':total,'completed':checked,'unresolved_offers':len(queue),'repair_backlog':len(repairs),
        'offered_by_group':offered,'completed_by_group':completed,'coverage_by_group':coverage,
        'reviewer_checks':reviewer_work,'effort_by_group':spent_total,
        'labor':sum(spent_total),'capacity_total':sum(a.capacity for a in agents)*config.periods,
        'completion_coverage':checked/total if total else 0,
        'defect_detection_fraction':(counters['defects_detected']+counters['audit_detected_defects'])/counters['defects_offered'] if counters['defects_offered'] else None,
        'correct_checks_per_offer':counters['correct_checks']/total if total else 0,
        'accuracy_among_completed':counters['correct_checks']/checked if checked else None,
        'attention_hhi':sum(s*s for s in shares),'largest_attention_share':max(shares,default=0),
        'minimum_group_coverage':min((x for x in coverage if x is not None),default=0),
        'mean_queue_age':sum(config.periods-t.created for t in queue)/len(queue) if queue else 0,
        'final_scores':scores,'counters':counters,'history':history,
        'exogenous_offer_sha256':hashlib.sha256(repr(offered_ids).encode()).hexdigest()}
