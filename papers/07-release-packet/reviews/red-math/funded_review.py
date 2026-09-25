"""Exact audit/participation/detection oracle plus retained pre-repair failures."""
from collections import defaultdict
from dataclasses import replace
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import hashlib,importlib.util,json,math,sys,types
ROOT=Path(__file__).resolve().parent;PACKET=ROOT.parent.parent;MODEL=PACKET/'models/funded_audits/model.py'
def load(name,code=None):
    module=types.ModuleType(name);module.__file__=str(MODEL);sys.modules[name]=module
    exec(compile(code if code is not None else MODEL.read_text(),str(MODEL),'exec'),module.__dict__)
    return module
m=load('red_funded_live');old=load('red_funded_archived',(ROOT/'funded-original-model.txt').read_text())

def rational(x):return F(str(x))
def oracle_util(cfg,effort,outside,q):
    return {'honest':rational(cfg.reward)-rational(effort)-q*rational(cfg.false_positive)*rational(cfg.loss),
            'shallow':rational(cfg.reward)-q*rational(cfg.detection)*rational(cfg.loss),'refuse':rational(outside)}
def action(values):return max(('refuse','honest','shallow'),key=lambda x:values[x])

class Controlled:
    def __init__(self,flags):self.flags=iter(flags)
    def random(self):return 0. if next(self.flags) else math.nextafter(1.,0.)
    def randrange(self,n):return 0 if next(self.flags) else n-1


def enumerate_case(cfg,efforts,outside):
    N=cfg.offered_population;k=cfg.delivered_quota
    subsets=list(combinations(range(N),k));den=F(1,len(subsets));mass=F(0)
    expected=defaultdict(F);run_count=0;before_sampler=m._math.blinded_audit_sample;before_rng=m.random.Random
    try:
        for subset in subsets:
            beliefs=[F(int(i in subset)) if cfg.disclose_selection else F(cfg.promised_quota,N) for i in range(N)]
            choices=[action(oracle_util(cfg,efforts[i],outside[i],beliefs[i])) for i in range(N)]
            audited=[i for i in subset if choices[i]!='refuse']
            chances=[rational(cfg.false_positive if choices[i]=='honest' else cfg.detection) for i in audited]
            for flags in product((False,True),repeat=len(audited)):
                weight=den
                for flag,p in zip(flags,chances):weight*=p if flag else 1-p
                if not weight:continue
                m._math.blinded_audit_sample=lambda *a,chosen=list(subset),**kw:chosen
                m.random.Random=lambda *a,flags=flags,**kw:Controlled(flags)
                actual=m.run(cfg,seed=0,efforts=efforts,outside_options=outside);run_count+=1;mass+=weight
                assert actual['status'].startswith('executed')
                assert [a['action'] for a in actual['actors']]==choices
                assert actual['counts']['audited']==len(audited)
                assert actual['counts']['unused_refused_audit_slots']==k-len(audited)
                assert actual['counts']['sanctioned']==sum(flags)
                counts={a:choices.count(a) for a in ('honest','shallow','refuse')}
                for a,count in counts.items():assert actual['counts'][a if a!='refuse' else 'refused']==count
                # Independent actor cash/utility conservation and event-hour reconstruction.
                hours=defaultdict(float)
                for event in actual['events']:
                    if event['event'] in ('complete','audit'):hours[event['person']]+=event['hours']
                for row in actual['person_ledger']:
                    assert abs(hours[row['person']]-row['spent_hours'])<1e-12
                    assert row['spent_hours']<=row['reserved_hours']+1e-14
                    assert row['reserved_hours']<=row['capacity_hours']+1e-14
                assert abs(actual['tokens']['escrow_opening_total']-actual['tokens']['escrow_closing_total']-actual['tokens']['penalties_quarantined'])<1e-12
                for actor in actual['actors']:
                    i=actor['actor'];choice=choices[i]
                    utility=rational(outside[i]) if choice=='refuse' else rational(cfg.reward)-(rational(efforts[i]) if choice=='honest' else 0)-rational(cfg.loss)*actor['sanctioned']
                    assert abs(float(utility)-actor['realized_utility'])<1e-12
                    expected['utility_'+str(i)]+=weight*utility
                expected['audits']+=weight*len(audited)
                expected['honest']+=weight*counts['honest'];expected['shallow']+=weight*counts['shallow'];expected['refused']+=weight*counts['refuse']
                expected['sanctions']+=weight*sum(flags)
        assert mass==1
    finally:m._math.blinded_audit_sample=before_sampler;m.random.Random=before_rng
    return {'enumerated_nonzero_outcome_paths':run_count,'exact_expectations':{k:str(v) for k,v in expected.items()}}

def main():
    a=old.ResourceLedger({'A':0});a.reserve_program({'A':0});a.spend('A',1e-12,'audit')
    tiny=old.run(old.Config(review_hours=1e-13,audit_hours=1e-13,review_capacity=0,audit_capacity=0))
    tie=old.run(old.Config(promised_quota=1,delivered_quota=1,false_positive=.1,detection=.3),efforts=[.05]*8,outside_options=[0]*8)
    refusal=old.run(old.Config(reward=.4,reward_token_budget=3.2,false_positive=0,detection=1,promised_quota=8,delivered_quota=8,audit_token_budget=8,audit_capacity=4),efforts=[.1]*8,outside_options=[.3]*8)
    original={'zero_capacity_spend':a.report(),'tiny_program_status':tiny['status'],'honest_shallow_tie_original_actions':tie['counts'],'honest_refusal_tie_original_actions':refusal['counts']}
    assert tiny['status']=='executed' and tie['counts']['shallow']==8 and refusal['counts']['honest']==8
    cases={
      'concealed':(m.Config(),[.3]*8,[.1]*8),
      'partial_refusal':(m.Config(),[.3]*8,[1]*4+[.1]*4),
      'early_disclosure':(m.Config(disclose_selection=True),[.3]*8,[.1]*8),
      'false_sanction_all_refuse':(m.Config(false_positive=.3),[.3]*8,[.1]*8),
      'certain_false_sanction':(m.Config(reward=3,reward_token_budget=24,false_positive=1,detection=1),[0]*8,[.1]*8),
      'honest_shallow_tie':(m.Config(promised_quota=1,delivered_quota=1,false_positive=.1,detection=.3),[.05]*8,[0]*8),
      'honest_refusal_tie':(m.Config(reward=.4,reward_token_budget=3.2,false_positive=0,detection=1,promised_quota=8,delivered_quota=8,audit_token_budget=8,audit_capacity=4),[.1]*8,[.3]*8),
      'shared_cross_roles':(m.Config(role_mode='shared_cross'),[.3]*8,[.1]*8),
      'no_inspections':(m.Config(promised_quota=0,delivered_quota=0),[.3]*8,[.1]*8)}
    result={'original_failures':original,'cases':{name:enumerate_case(*args) for name,args in cases.items()},'source_sha256':hashlib.sha256(MODEL.read_bytes()).hexdigest()}
    # Exact restored hour guards: no positive debit from zero; decimals sum exactly.
    ledger=m.ResourceLedger({'A':0});ledger.reserve_program({'A':0})
    try:ledger.spend('A',1e-12,'audit')
    except ValueError:pass
    else:raise AssertionError('zero-capacity overspend remains')
    decimal=m.ResourceLedger({'A':.3});assert decimal.reserve_program({'A':.3})
    for _ in range(3):decimal.spend('A',.1,'audit')
    assert decimal.report()[0]['spent_hours']==.3
    assert m.run(m.Config(review_hours=1e-13,audit_hours=1e-13,review_capacity=0,audit_capacity=0))['status']=='unavailable_before_offering'
    result['exact_hour_guards']='PASS'
    (ROOT/'funded-review-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
