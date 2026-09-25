"""Independent ecology reproduction and conditional-math boundary probes."""
from pathlib import Path
import csv,hashlib,json,math,statistics,sys
ROOT=Path(__file__).resolve().parent;PACKET=ROOT.parent.parent
sys.path.insert(0,str(PACKET))
from models.ecology.ecology import Config,Agent,AGENTS,probabilities,simulate

def main():
    eco=PACKET/'models/ecology'
    manifest=json.loads((eco/'results/summary.json').read_text())
    csvrows={(r['regime'],int(r['seed']),r['policy']):r for r in csv.DictReader((eco/'results/sweep.csv').open())}
    results={};replications=0
    for regime,kwargs in manifest['regimes'].items():
        for seed in manifest['seeds']:
            for policy in ('bounded','prestige','uniform'):
                result=simulate(Config(seed=seed,periods=80,**kwargs),policy,trace=True)
                results[regime,seed,policy]=result;replications+=1
                row=csvrows[regime,seed,policy]
                for key in manifest['aggregate'][0]['summaries']:
                    assert abs(float(row[key])-result[key])<1e-12
                assert sum(sum(x['spent']) for x in result['history'])==result['labor']
                assert all(s<=a.capacity for h in result['history'] for s,a in zip(h['spent'],AGENTS))
                if policy=='bounded':assert all(0<=s<=1 for h in result['history'] for s in h['scores'])
            assert len({results[regime,seed,p]['exogenous_offer_sha256'] for p in ('bounded','prestige','uniform')})==1
            assert len({results[regime,seed,p]['counters']['blind_periods'] for p in ('bounded','prestige','uniform')})==1
    pairedchecks=0
    for entry in manifest['aggregate']:
        for metric,summary in entry['summaries'].items():
            vals=[results[entry['regime'],s,entry['policy']][metric] for s in manifest['seeds']]
            assert min(vals)==summary['min'] and max(vals)==summary['max']
            assert abs(statistics.mean(vals)-summary['mean'])<1e-12
            diffs=[results[entry['regime'],s,entry['policy']][metric]-results[entry['regime'],s,'uniform'][metric] for s in manifest['seeds']]
            assert abs(statistics.mean(diffs)-entry['paired_difference_from_uniform'][metric])<1e-12
            pairedchecks+=1
    # Finite difference of the explicitly separate mean-field map in zero-sum direction.
    K,eps,beta,mu=6,.15,2.,.1;h=1e-6
    base=[1/K]*K;direction=[1,-1,0,0,0,0]
    def step(s):return [(1-mu)*x+mu*p for x,p in zip(s,probabilities(s,eps,beta))]
    plus=step([s+h*d for s,d in zip(base,direction)])
    minus=step([s-h*d for s,d in zip(base,direction)])
    measured=(plus[0]-minus[0])/(2*h);expected=1-mu+mu*(1-eps)*beta/K
    assert abs(measured-expected)<1e-9
    # No-audit correction-credit counterexample. Three identical qualified groups.
    def population(defect):return tuple(Agent('g'+str(i),100,('common',),1,defect,1) for i in range(3))
    cfg=Config(seed=19,periods=30,arrival=.2,audit_probability=0,blind_probability=0)
    clean=simulate(cfg,agents=population(0),trace=True)
    defective=simulate(cfg,agents=population(1),trace=True)
    assert clean['counters']['repair_completed']==0
    assert defective['counters']['repair_completed']>0
    assert sum(defective['final_scores'])>sum(clean['final_scores'])
    # Perfect shared blindness: every completed check wrong, recognized debt zero.
    blindpop=population(1)
    blind=simulate(Config(seed=19,periods=10,arrival=.2,audit_probability=0,blind_probability=1),agents=blindpop)
    assert blind['completed']>0 and blind['accuracy_among_completed']==0 and blind['repair_backlog']==0
    report={'interpretation':'Reproduction and hypothetical incentive counterexample, no strategic behavior fitted',
      'reproduced_runs':replications,'summary_and_paired_metric_checks':pairedchecks,'meanfield_finite_difference':{'observed':measured,'predicted':expected},
      'correction_credit_boundary':{'clean_final_scores':clean['final_scores'],'defective_final_scores':defective['final_scores'],'clean_repairs':clean['counters']['repair_completed'],'defective_repairs':defective['counters']['repair_completed'],'meaning':'Defect production can generate correction credit; actors do not choose defect rates in present model, so no strategic equilibrium claim.'},
      'shared_blindness':{'completed':blind['completed'],'accuracy':blind['accuracy_among_completed'],'repair_backlog':blind['repair_backlog']},
      'source_sha256':hashlib.sha256((eco/'ecology.py').read_bytes()).hexdigest()}
    (ROOT/'ecology-review-results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
