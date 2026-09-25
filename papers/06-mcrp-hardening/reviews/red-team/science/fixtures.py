"""Adversarial deterministic fixtures; no external validation or fitted behavior."""
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('science_checks',ROOT/'models/science/model_checks.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

# Each frozen environment terminates in one generation; alternating environments grow.
a=[[0.,2.],[0.,0.]]; b=[[0.,0.],[2.,0.]]
z=[1.,0.]
for generation in range(10):
    z=m.row_mul(z,a if generation%2==0 else b)
assert m.spectral_radius_2(a)==m.spectral_radius_2(b)==0
assert z==[1024.,0.]

# Declared dependency graph can have perfect self-recall and miss true dependencies.
declared={'A':{'calibration'},'B':set()}
truth={'A':{'calibration'},'B':{'calibration'}}
visible={k for k,v in declared.items() if 'calibration' in v}
affected={k for k,v in truth.items() if 'calibration' in v}
assert visible=={'A'} and affected=={'A','B'}

# Mean parent-level fractions cannot be multiplied without weighting/conditioning.
types=[(0.,0.,1.),(4.,1.,0.)] # dependents, fraction requiring work, coalesced fraction
naive=sum(t[0] for t in types)/2*sum(t[1] for t in types)/2*(1-sum(t[2] for t in types)/2)
actual=sum(n*q*(1-c) for n,q,c in types)/2
assert naive==.5 and actual==2.

# Separate lane checks can oversubscribe one expert.
capacity=8.; workloads={'review':4.,'repair':3.,'appeals':2.}
assert all(v<capacity for v in workloads.values()) and sum(workloads.values())>capacity
print(json.dumps({'switching':{'rho_a':0,'rho_b':0,'generation_10':z},
 'declared_cone':sorted(visible),'true_cone':sorted(affected),
 'naive_parent_average_R':naive,'actual_R':actual,
 'shared_capacity':capacity,'combined_demand':sum(workloads.values()),
 'all_adversarial_assertions_passed':True},indent=2))
