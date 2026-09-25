"""Finite exact membership check against utilities, independent of interval derivation."""
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'07-release-packet/models/math'))
from protocol_math import hard_audit_interval

def main():
    cases = points = 0
    for c,R,F,alpha,beta,a,B in itertools.product(
        [Q(0),Q(1,2)], [Q(0),Q(1)], [Q(0),Q(1)],
        [Q(0),Q(1,2),Q(1)], [Q(0),Q(1,2),Q(1)],
        [Q(0),Q(1)], [Q(0),Q(3,2),Q(3)]):
        n=3;u=Q(0)
        result=hard_audit_interval(c,R,F,alpha,beta,u,n,a,B)
        cases+=1
        lo=None if result['minimum_audit_exact'] is None else Q(result['minimum_audit_exact'])
        hi=Q(result['maximum_audit_exact'])
        for q in [Q(i,12) for i in range(13)]:
            direct=(R-c-q*alpha*F >= R-q*beta*F and R-c-q*alpha*F >= u
                    and q*n <= (n if a==0 else min(n,B//a)))
            interval=result['feasible'] and lo<=q<=hi
            assert direct==interval,(c,R,F,alpha,beta,a,B,q,result)
            points+=1
    report={'method':'Direct rational utility inequalities and identical-cost count cap versus returned exact interval; no sampling',
            'parameter_cases':cases,'q_grid_points_checked':points,'passed':True,
            'limits':'finite grid, same author-directed team, no empirical validation'}
    (HERE/'root-oracle-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
if __name__=='__main__': main()
