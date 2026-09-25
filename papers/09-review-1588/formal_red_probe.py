"""Independent exact oracle; no manuscript or fixture mutation."""
from pathlib import Path
import sys
from itertools import product
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).resolve().parent/'formal'))
from audit_contract import interval
count=0
for n,a,B,c,alpha,beta,loss in product((1,3,5),(F(0),F(2,3)),(F(0),F(1),F(3,2)),(F(0),F(1,3)),(F(0),F(1,2)),(F(0),F(1,2),F(1)),(F(0),F(2))):
    for kind in ('expected','hard'):
        result=interval(c,1,loss,alpha,beta,F(1,4),n,a,B,kind)
        for q in (F(0),F(1,7),F(1,3),F(1,2),F(1)):
            honest=1-c-q*alpha*loss; shirk=1-q*beta*loss
            count_cap=max(k for k in range(n+1) if a*k<=B)
            budget=(n*a*q<=B) if kind=='expected' else (n*q<=count_cap)
            direct=honest>=shirk and honest>=F(1,4) and budget
            encoded=result is not None and result[0]<=q<=result[1]
            if direct != encoded: raise AssertionError((n,a,B,c,alpha,beta,loss,kind,q))
            count+=1
print({'exact_comparisons':count,'mismatches':0,'independent_cap_enumeration':True})
