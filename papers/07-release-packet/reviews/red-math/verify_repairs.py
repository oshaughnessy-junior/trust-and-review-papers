"""Independent verification of exact audit endpoints and completion accounting."""
from pathlib import Path
from fractions import Fraction as F
import itertools,json,random,sys,hashlib
ROOT=Path(__file__).resolve().parent;PACKET=ROOT.parent.parent
sys.path.insert(0,str(PACKET/'models/math'));sys.path.insert(0,str(PACKET/'models/coupled'));sys.path.insert(0,str(PACKET))
from protocol_math import hard_audit_interval,blinded_audit_sample
from toy_agents.scenarios import completion_bias
from simulator import Ledger

def main():
    endpoints=0
    for n in range(1,31):
        for k in range(n+1):
            interval=hard_audit_interval(0,1,0,0,0,0,n,1,k)
            assert interval['feasible'] and F(interval['maximum_audit_exact'])==F(k,n)
            for representation in (interval['maximum_audit_exact'],interval['maximum_audit'],F(k,n)):
                for seed in range(5):
                    selected=blinded_audit_sample(n,representation,1,k,random.Random(seed))
                    assert len(selected)<=k and len(set(selected))==len(selected)
                    if representation!=interval['maximum_audit']:assert len(selected)==k
            endpoints+=1
    # Singleton interval remains feasible in exact fields despite rounded float displays.
    singleton=hard_audit_interval(5,5,6,0,1,0,6,1,5)
    assert singleton['feasible']
    assert singleton['minimum_audit_exact']==singleton['maximum_audit_exact']=='5/6'
    assert len(blinded_audit_sample(6,singleton['maximum_audit_exact'],1,5,random.Random(0)))==5
    utilitychecks=0
    for c,R,loss,alpha,beta,u in itertools.product((F(0),F(1,5)),(F(1,5),F(1)),(F(0),F(2)),(F(0),F(1,5)),(F(0),F(4,5)),(F(0),F(1,10))):
        result=hard_audit_interval(c,R,loss,alpha,beta,u,3,F(1,10),F(1,5))
        lo=None if result['minimum_audit_exact'] is None else F(result['minimum_audit_exact']);hi=F(result['maximum_audit_exact'])
        for q in (F(i,12) for i in range(13)):
            honest=R-c-q*alpha*loss;shirk=R-q*beta*loss
            direct=honest>=shirk and honest>=u and q<=F(2,3)
            interval=lo is not None and lo<=q<=hi
            assert direct==interval;utilitychecks+=1
    # One exact rational step above cap must fail, never be hidden in tolerance.
    try:blinded_audit_sample(6,F(5,6)+F(1,10**12),1,5,random.Random(1))
    except ValueError:pass
    else:raise AssertionError('above-cap audit accepted')
    c=completion_bias()['counts'];assert c['offered']==c['completed']+c['unresolved'] and c['unresolved']==8956
    ledger=Ledger({'A':0});holds=[ledger.reserve({'A':0}) for _ in range(3)]
    denied=0
    for token in holds:
        try:ledger.settle(token,{'A':1e-12},'probe')
        except ValueError:denied+=1
    ledger_fixed=denied==3 and ledger.used['A']==0
    result={'RM1':'expected-cost semantics and hard-count scheme separately stated','RM2':'8956 unresolved; accounting reconciles','RM3':'exact interval endpoints consumable; strict above-cap rejection',
      'exact_endpoint_cases':endpoints,'independent_utility_inequality_checks':utilitychecks,'singleton_interval':singleton,'coupled_zero_hold_repair_confirmed':ledger_fixed,
      'source_sha256':{str(p.relative_to(PACKET)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (PACKET/'models/math/protocol_math.py',PACKET/'models/coupled/simulator.py')}}
    (ROOT/'repair-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
