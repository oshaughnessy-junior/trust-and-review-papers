"""Adversarial diagnostics; do not alter author artifacts."""
import importlib.util, json, math, hashlib
from pathlib import Path
root=Path(__file__).resolve().parent
p=root/'original_allocation.py'
spec=importlib.util.spec_from_file_location('target',p); m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
out={'target_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'checks':{}}
for name,args in {
 'normal':([10,4,1],[1,.5,1],4),
 'zero_productivity':([1,1],[0,0],1),
 'mixed_zero_productivity':([1,1],[0,1],1),
 'zero_value':([0,1],[1,1],1),
 'length_mismatch':([1,100],[1],1),
 'negative_lower':([1,1],[1,1],1,[-1,-1]),
 'long_horizon':([1],[1],100),
 'subnormal_scale':([1e-200],[1e-200],1),
}.items():
 try: out['checks'][name]={'returned':m.water_fill(*args)}
 except Exception as e: out['checks'][name]={'exception':type(e).__name__,'message':str(e)}
# Correct known optimum for long_horizon is exactly h=100.
A=[1,100]; a=[1,1]; H=1
allocation=m.water_fill(A[::-1],a,H)
out['inverted_priority']={'estimated_assignment':allocation,'true_benefit':m.benefit(A,a,allocation),'uniform_benefit':m.benefit(A,a,[.5,.5]),'oracle_benefit':m.benefit(A,a,m.water_fill(A,a,H))}
# The exact utility expression needs a realized/expected loss, not its upper bound.
w,c,q,d0,d1,Fmax,Factual=10,2,.5,.8,.1,10,.1
out['penalty_cap_counterexample']={'claimed_incentive_margin':q*(d0-d1)*Fmax-c,'actual_incentive_margin':q*(d0-d1)*Factual-c,'actual_U_honest':w-c-q*d1*Factual,'actual_U_shirk':w-q*d0*Factual}
# Opportunity cost is not represented by a cash-positive campaign.
out['specialist_displacement']={'specialist_hours':4,'common_hours_required':4,'funded_campaign_hours_required':4,'joint_demand':8,'shortfall':4}
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
