"""Two-type first-moment checks. Standard library only; no fitted behavior."""
import hashlib
import json
import math
from pathlib import Path
import platform


def spectral_radius_2(m):
    a,b=m[0]; c,d=m[1]
    if any(not math.isfinite(x) or x<0 for row in m for x in row):
        raise ValueError('Nonnegative finite offspring means required')
    # Perron root of nonnegative two-by-two matrix.
    return (a+d+math.sqrt((a-d)**2+4*b*c))/2


def total_2(z,m):
    if spectral_radius_2(m)>=1:
        raise ValueError('Global resolvent formula requires subcritical matrix')
    a,b=m[0]; c,d=m[1]
    det=(1-a)*(1-d)-b*c
    return [(z[0]*(1-d)+z[1]*c)/det,
            (z[0]*b+z[1]*(1-a))/det]


def row_mul(z,m):
    return [sum(z[i]*m[i][j] for i in range(len(z))) for j in range(len(z))]


def generations(z,m,n):
    total=z[:]
    for _ in range(n):
        z=row_mul(z,m)
        total=[x+y for x,y in zip(total,z)]
    return total


def main():
    hidden=[[.2,.01],[.01,1.2]]
    stable=[[.2,.1],[.05,.6]]
    t=total_2([1.,0.],stable)
    numerical=generations([1.,0.],stable,200)
    assert max(abs(a-b) for a,b in zip(t,numerical))<1e-12
    assert spectral_radius_2(hidden)>1
    avg=sum(sum(row) for row in hidden)/2
    assert avg<1
    workload=[2*t[0],2*t[1]*8]
    assert sum(workload)<8 and workload[1]>4
    # A reachable-submatrix restriction matters: a root in the first block
    # cannot reach a disconnected second supercritical block.
    disconnected=[[.2,0.],[0.,1.2]]
    unreach=generations([1.,0.],disconnected,200)
    assert abs(unreach[0]-1.25)<1e-12 and unreach[1]==0
    # Diamond DAG: root -> left,right -> same downstream claim.
    # Path expansion counts downstream twice, while distinct IDs count once.
    diamond=[[0.,1.,1.,0.],[0.,0.,0.,1.],[0.,0.,0.,1.],[0.,0.,0.,0.]]
    path_counts=generations([1.,0.,0.,0.],diamond,4)
    assert path_counts==[1.,1.,1.,2.]
    result={
        'schema':'mcrp-scientist-second-round.v1',
        'interpretation':'Synthetic first-moment counterexamples; no human calibration',
        'environment':{'python':platform.python_version()},
        'hidden_specialty':{'offspring_matrix':hidden,'mean_row_sum':avg,
            'naive_scalar_total':1/(1-avg),'spectral_radius':spectral_radius_2(hidden)},
        'stable_specialties':{'offspring_matrix':stable,'spectral_radius':spectral_radius_2(stable),
            'initial':[1,0],'expected_items':t,'hours_per_item':[1,8],
            'expected_hours_per_root':t[0]+8*t[1],
            'roots_per_day':2,'workload_hours_per_day':workload,
            'capacity_hours_per_day':[4,4],
            'global_load_feasible':sum(workload)<8,'specialist_load_feasible':False,
            'series_inverse_max_difference':max(abs(a-b) for a,b in zip(t,numerical))},
        'unreachable_supercritical_block':{'global_spectral_radius':spectral_radius_2(disconnected),
            'root_reachable_expected_items':unreach},
        'diamond_dag':{'path_counts':path_counts,'total_path_visits':sum(path_counts),'distinct_claims':4},
        'checks':'6 conceptual assertions plus inverse/series numerical comparison passed',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    (Path(__file__).resolve().parents[2]/'results'/'compositional-science.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
