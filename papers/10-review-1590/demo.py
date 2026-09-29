"""One complete fixture, exact analytic accounting, and retained negative branches."""
from fractions import Fraction as F
from dataclasses import asdict
import json,random,copy
from machine import Machine,PANELS,repair_bound
M=(((F(1,4),F(1,4)),(F(0),F(1,2))),((F(1,2),F(0)),(F(1,4),F(1,4))))

def run():
    m=Machine()
    m.apply('offer-1','offer',actor='author',target='mean@v1',scope='three synthetic values only',dependencies=('data@v1',),seed=0)
    # Fixed latent completion coins, separate from the audit planner, before reports.
    coins=random.Random(0)
    all_outcomes=['passed' if (coins.randrange(4)<(4 if panel==('A','B') else 1)) else 'refused'
                  for panel in m.offers['mean@v1']['panels']]
    for i,outcome in enumerate(all_outcomes):
        if m.offers['mean@v1']['phase']!='open':break
        e=m.apply('check-'+str(i),'check',actor='verifier',target='mean@v1',scope='three synthetic values only',representatives=m.planned_representatives('mean@v1'),outcome=outcome,evidence='synthetic-evidence:'+str(i))
    m.apply('rely-1','rely',actor='decision-maker',target='mean@v1',scope='three synthetic values only',check_seq=e['seq'])
    m.apply('amend-1','amend',actor='author',changed='data@v1',successor='data@v2',matrices=M,weights=(F(1),F(1)))
    rejected=[]
    def reject(name,fn):
        before=copy.deepcopy(m.__dict__)
        try:fn()
        except ValueError as e:rejected.append({'case':name,'reason':str(e),'state_unchanged':m.__dict__==before})
        else:raise AssertionError('Expected refusal: '+name)
    reject('stale-reliance',lambda:m.apply('rely-old','rely',actor='decision-maker',target='mean@v1',scope='three synthetic values only',check_seq=e['seq']))
    reject('replayed-event',lambda:m.apply('amend-1','rely',actor='decision-maker',target='mean@v1',scope='three synthetic values only',check_seq=e['seq']))
    reject('expected-budget-is-not-hard-cap',lambda:m.apply('bad-offer','offer',actor='author',target='mean@v2',scope='toy',dependencies=('data@v2',),audit_q=F(1,2),audit_budget=F(3,2)))
    p,a,b=F(1,3),F(1),F(1,4);s=p*a+(1-p)*b
    attempts=sum((1-s)**j for j in range(3));finished=1-(1-s)**3
    return {'status':'one synthetic accounting example, not an incentive equilibrium or science validation',
            'analytic':{'group_panel_law':{'AB':F(1,3),'AC':F(1,3),'BC':F(1,3)},
                        'risk_category':'AB panel only','p':p,'a':a,'b':b,'per_attempt_completion':s,
                        'IID_expected_attempts':attempts,'IID_completion_by_three':finished,'IID_completed_risk_share':p*a/s,
                        'IID_expected_check_work':F(1,10)*attempts+finished,
                        'ex_ante_expected_audit_work':F(1,3)*attempts,
                        'audit_utility_lower':F(1,8),'audit_hard_upper':F(1,3),
                        'common_repair_bound':F(2),'repair_is_reserved':False},
            'precommitted_fixture_outcomes':all_outcomes,'events':m.events,'actual_work':m.spent,
            'actual_attempts':m.offers['mean@v1']['attempt'],'current_reliances':m.reliances,'rejected':rejected,
            'negative_premises':{'hidden_lineage':'absent edges cannot be discovered',
                'sequential_incentives':'a disclosed first-slot audit leaves later conditional q=0; ex-ante IC does not extend',
                'unstable_switching':repair_bound((((0,2),(0,0)),((0,0),(2,0))),(F(1),F(1)),(F(1),F(0)))}}
if __name__=='__main__':print(json.dumps(run(),indent=2,default=lambda x:str(x) if isinstance(x,F) else None))
