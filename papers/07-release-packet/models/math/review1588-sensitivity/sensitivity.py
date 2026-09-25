"""Exact synthetic sensitivity and conflict-aware panels; no behavioral fitting."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from dataclasses import dataclass
import json


def exact(x, lower=F(0), upper=None):
    if isinstance(x,bool) or not isinstance(x,(int,F)):
        raise ValueError('Use exact int/Fraction inputs')
    if x<lower or (upper is not None and x>upper): raise ValueError('Out of range')
    return F(x)


def completion(p,a,b,L,ci,cc):
    p,a,b=(exact(x,upper=F(1)) for x in (p,a,b));ci,cc=exact(ci),exact(cc)
    if type(L) is not int or L<1:raise ValueError('Positive retry count required')
    s=p*a+(1-p)*b
    attempts=sum((1-s)**j for j in range(L))
    finished=1-(1-s)**L
    return {'completion_probability':finished,'attempts':attempts,
            'risk_share':p*a/s if s else None,'unresolved':1-finished,
            'cost':ci*attempts+cc*finished}


def audit(c=F(1,5),R=F(1),F_loss=F(2),alpha=F(1,50),beta=F(4,5),
          u=F(1,10),N=100,audit_cost=F(1,10),B=F(2)):
    c,R,F_loss,u,audit_cost,B=map(exact,(c,R,F_loss,u,audit_cost,B))
    alpha,beta=(exact(v,upper=F(1)) for v in (alpha,beta))
    if type(N) is not int or N<1 or not (F_loss>0 and audit_cost>0 and alpha>0 and beta>alpha):
        raise ValueError('Sensitivity branch requires N>=1, a,F,alpha>0 and beta>alpha')
    lower=c/((beta-alpha)*F_loss)
    participation=(R-c-u)/(alpha*F_loss)
    expected_cap=min(F(1),B/(N*audit_cost))
    hard_cap=F(min(N,B//audit_cost),N)
    ehi=min(expected_cap,participation);hhi=min(hard_cap,participation)
    return {'effort_lower':lower,'participation_upper':participation,
            'expected_cap':expected_cap,'hard_cap':hard_cap,
            'expected_upper':ehi,'hard_upper':hhi,
            'expected_feasible':lower<=ehi,'hard_feasible':lower<=hhi,
            'participation_effort_margin':(R-c-u)*(beta-alpha)-c*alpha}

@dataclass(frozen=True)
class Group:
    name: str
    skills: frozenset
    capacity: int
    weight: F = F(1)
    def __post_init__(self):
        if not isinstance(self.name,str) or not self.name or type(self.skills) is not frozenset:
            raise ValueError('Named group and immutable skills required')
        if type(self.capacity) is not int or self.capacity<0:raise ValueError('Integer capacity required')
        if exact(self.weight)<=0:raise ValueError('Positive invariant group weight required')


def feasible(groups, required, conflicts):
    """One unit task per skill, distinct group assignees, capacity/conflict prefilter."""
    if not groups or len({g.name for g in groups})!=len(groups):raise ValueError('Unique groups required')
    if type(required) is not tuple or not required or len(set(required))!=len(required):raise ValueError('Unique skill tasks required')
    names={g.name for g in groups}
    if any(type(pair) is not frozenset or len(pair)!=2 or not pair<=names for pair in conflicts):raise ValueError('Known symmetric conflict pairs required')
    panels=[]
    for selected in combinations(groups,len(required)):
        if any(g.capacity<1 for g in selected):continue
        if any(frozenset((a.name,b.name)) in conflicts for a,b in combinations(selected,2)):continue
        if not any(all(skill in g.skills for skill,g in zip(required,assignment)) for assignment in permutations(selected)):continue
        panels.append(tuple(sorted(g.name for g in selected)))
    return tuple(sorted(panels))


def distribution(groups, panels, multiplicity=None):
    """None=>group weights; counts=>representative-first feasible multiplicity."""
    if not panels:return None
    weights={g.name:g.weight for g in groups}
    if multiplicity is not None:
        if set(multiplicity)!=set(weights) or any(type(v) is not int or v<1 for v in multiplicity.values()):raise ValueError('Positive exact representative counts required')
        weights=multiplicity
    masses={panel:F(1) for panel in panels}
    for panel in panels:
        for name in panel:masses[panel]*=weights[name]
    total=sum(masses.values())
    return {panel:value/total for panel,value in masses.items()}


def panel_fixture():
    return (Group('A',frozenset({'calibration'}),1),
            Group('B',frozenset({'inference'}),1),
            Group('C',frozenset({'calibration','inference'}),1,F(2)),
            Group('D',frozenset({'inference'}),1),
            Group('E',frozenset({'calibration'}),0))


def results():
    completions=[]
    for a,b in product((F(1,10),F(1,2),F(1)),(F(1,1000),F(1,100),F(1,10),F(1,2),F(1))):
        completions.append({'a':a,'b':b,**completion(F(1,10),a,b,10,F(1,5),F(2))})
    costs=[{'L':L,'ci':ci,'cc':cc,**completion(F(1,10),F(1),F(1,100),L,ci,cc)}
           for L,ci,cc in product((1,10,50),(F(1,50),F(1,5),F(2)),(F(1,5),F(2),F(20)))]
    audits=[]
    sweep={'alpha':(F(1,100),F(1,50),F(1,10),F(3,10)),
           'beta':(F(1,10),F(2,5),F(4,5),F(1)),
           'c':(F(1,20),F(1,5),F(2,5),F(4,5)),
           'F_loss':(F(1,2),F(1),F(2),F(4),F(8)),
           'audit_cost':(F(1,20),F(1,10),F(1,5)), 'B':(F(1),F(2),F(4))}
    for field,values in sweep.items():
        for value in values:audits.append({'varied':field,'value':value,**audit(**{field:value})})
    conflict=[{'F':f,**audit(R=F(2,5),alpha=F(3,10),F_loss=f)} for f in (F(1),F(2),F(8))]
    box=[audit(c=c,alpha=al,beta=be,F_loss=f) for c,al,be,f in product((F(1,10),F(1,5)),(F(1,100),F(1,25)),(F(7,10),F(9,10)),(F(2),F(3)))]
    groups=panel_fixture();panels=feasible(groups,('calibration','inference'),(frozenset({'A','B'}),frozenset({'C','D'})))
    def serial(d):return {'+'.join(k):v for k,v in d.items()} if d is not None else None
    return {'synthetic_exact_not_empirical':True,'completion_sensitivity':completions,'retry_cost_sensitivity':costs,
            'audit_one_at_time':audits,'sanction_cannot_fix_conflict':conflict,
            'robust_box':{'corner_count':len(box),'common_hard_lower':max(r['effort_lower'] for r in box),'common_hard_upper':min(r['hard_upper'] for r in box)},
            'fractional_budget':audit(c=F(2,5),F_loss=F(1),alpha=F(1,10),beta=F(1),N=3,audit_cost=F(1),B=F(3,2),R=F(2)),
            'panels':{'feasible':panels,'group_weighted':serial(distribution(groups,panels)),
                       'representative_one_each':serial(distribution(groups,panels,{g.name:1 for g in groups})),
                       'representative_A_ten':serial(distribution(groups,panels,{g.name:10 if g.name=='A' else 1 for g in groups})),
                       'empty_required_skill':distribution(groups,feasible(groups,('unknown-skill',),()))}}

if __name__=='__main__':print(json.dumps(results(),indent=2,default=lambda x:str(x) if isinstance(x,F) else None))
