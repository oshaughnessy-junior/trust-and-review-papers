"""Independent exact adversarial probes. Run from any working directory."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import math
ROOT=Path(__file__).resolve().parent


def adaptive_tree(policy, depth):
    """Enumerate category-specific refusal histories; no formula under review reused."""
    outcomes={'risky':F(0),'other':F(0),'unresolved':F(0),'attempts':F(0)}
    frontier=[('',F(1))]
    while frontier:
        history,mass=frontier.pop()
        if len(history)==depth or policy(history) is None:
            outcomes['unresolved']+=mass
            continue
        p,a,b=policy(history)
        outcomes['attempts']+=mass
        outcomes['risky']+=mass*p*a
        outcomes['other']+=mass*(1-p)*b
        frontier += [(history+'R',mass*p*(1-a)),(history+'O',mass*(1-p)*(1-b))]
    assert outcomes['risky']+outcomes['other']+outcomes['unresolved']==1
    completed=outcomes['risky']+outcomes['other']
    outcomes['risky_share']=outcomes['risky']/completed if completed else None
    return outcomes


def main():
    # Expected audit budget is not a hard capacity. Exact Binomial tail.
    N,q,cost,budget=100,F(1,5),F(1,10),F(2)
    kmax=int(budget/cost)
    tail=sum(F(math.comb(N,k))*q**k*(1-q)**(N-k) for k in range(kmax+1,N+1))
    assert F(2,5)<tail<F(1,2)
    # Nonintegral audit capacity exposes strict gap even with optimal hard-cap design.
    hard_N,hard_cost,hard_budget=3,F(1),F(3,2)
    hard_q=F(hard_budget//hard_cost,hard_N)
    expected_q=hard_budget/(hard_N*hard_cost)
    assert hard_q==F(1,3) and expected_q==F(1,2)
    # Equal marginal fixed-size sample, independent of observed actions.
    samples=list(combinations(range(5),2))
    marginals=[F(sum(i in s for s in samples),len(samples)) for i in range(5)]
    assert all(x==F(2,5) for x in marginals)

    eps,u,ell=F(1,5),F(4,5),F(3,10)
    bound=eps*u/(eps*u+(1-eps)*ell)
    checked=[]
    for variant in range(20):
        def policy(h):
            if h.endswith('ROR') and variant%2:
                return None  # an adapted stop before the next offered category
            v=(sum(map(ord,h))+variant)%3
            return ([eps,F(1,10),F(0)][v], [u,F(1,2),u][v], [ell,F(1,2),F(1)][v])
        result=adaptive_tree(policy,8)
        assert result['risky_share'] is None or result['risky_share']<=bound
        checked.append(result)
    # Refuse every safe panel. Same cap at every offer, but no safe completion floor.
    manipulated=adaptive_tree(lambda h:(F(1,10),F(1),F(0)),8)
    assert manipulated['risky_share']==1
    # Final discretionary reliance is a third selection mechanism, even if all checks complete.
    complete=adaptive_tree(lambda h:(F(1,10),F(1),F(1)),1)
    assert complete['risky_share']==F(1,10)
    relied_share=complete['risky']/(complete['risky']+F(0)*complete['other'])
    assert relied_share==1

    # Correlated latent repair regime: marginal first-generation mean is misleading.
    latent=[F(1)]+[F(1,4)*2**t for t in range(1,11)]
    assert latent[1]==F(1,2) and latent[10]==256
    # Once one descendant is observed, high regime is known: conditional multiplier=2.
    # Thus this violates the manuscript conditional premise, not the theorem.

    old=json.loads((ROOT/'original_completion.json').read_text())['counts']
    assert old['unresolved']==0 and old['offered']-old['completed']>0
    result={
      'interpretation':'Exact toy counterexamples and theorem-boundary probes, no empirical validation',
      'audit':{'iid_expected_cost':float(N*q*cost),'budget':float(budget),'iid_probability_cost_exceeds_budget':float(tail),'hard_cap_noninteger_example':{'N':hard_N,'budget':str(hard_budget),'cost':str(hard_cost),'max_equal_marginal':str(hard_q),'expected_budget_only_marginal':str(expected_q)},'fixed_size_marginals':[str(x) for x in marginals]},
      'adaptive_completion':{'policies_checked':len(checked),'maximum_depth':8,'conditional_bound':str(bound),'max_observed_share':str(max(x['risky_share'] for x in checked if x['risky_share'] is not None)),'floor_violation_share':str(manipulated['risky_share']),'floor_violation_completion':str(1-manipulated['unresolved']),'offered_cap':'.1','completed_share_before_reliance_filter':str(complete['risky_share']),'relied_share_after_category_filter':str(relied_share)},
      'conditional_repair':{'initial_first_moment_ratio':str(latent[1]),'generation_10_expected_work':str(latent[10]),'conditional_survivor_ratio':2,'violates_conditional_envelope':True},
      'preserved_original_accounting':{'offered':old['offered'],'completed':old['completed'],'reported_unresolved':old['unresolved'],'required_unresolved_if_no_other_terminal_outcome':old['offered']-old['completed']},
      'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'probe-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
