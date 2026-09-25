"""Independent trace reconstruction and finite-path oracle for release wave 2."""
from collections import Counter,defaultdict
from fractions import Fraction as F
from pathlib import Path
import csv, hashlib, json, math, statistics, sys
ROOT=Path(__file__).resolve().parent
PACKET=ROOT.parent.parent
sys.path.insert(0,str(PACKET/'models/coupled'))
from simulator import Config,run,one_request_oracle
sys.path.insert(0,str(PACKET/'models/math'))
from protocol_math import hard_audit_interval,blinded_audit_sample
import random

def tree(retry):
    panels=[('A','B'),('A','C'),('B','C')]
    probs={'A':F(1),'B':F(1,4),'C':F(1)}
    stack=[(F(1),0,None)];done=F(0);risk=F(0);attempts=F(0)
    while stack:
        mass,t,fixed=stack.pop()
        if t==3:continue
        choices=[(fixed,F(1))] if fixed is not None and retry=='fixed_panel' else [(p,F(1,3)) for p in panels]
        attempts+=mass
        for panel,selection in choices:
            # Explicit individual Bernoulli response outcomes, not mixed success formula.
            for x in (False,True):
                for y in (False,True):
                    response=(probs[panel[0]] if x else 1-probs[panel[0]])*(probs[panel[1]] if y else 1-probs[panel[1]])
                    path=mass*selection*response
                    if x and y:done+=path;risk+=path*int('A' in panel)
                    else:stack.append((path,t+1,panel))
    return {'completion':done,'unresolved':1-done,'expected_attempts':attempts,'risky_completed_share':risk/done}

def reconstruct_trace(data):
    c=data['counts'];events=data['events'];responses=defaultdict(list);used=Counter()
    for event in events:
        if event['event']=='actor_response':
            responses[event['request'],event['attempt']].append(event)
            used[event['true_person']]+=event['hours']
    assert len(responses)==c['reserved_panels']
    assert sum(len(x) for x in responses.values())==c['invited_actors']
    completed=[group for group in responses.values() if all(e['reported_complete'] for e in group)]
    assert len(completed)==c['completed_requests']
    assert sum(all(e['action']=='honest' for e in g) for g in completed)==c.get('full_effort_completed_panels',0)
    assert sum(len({e['true_person'] for e in g})==2 for g in completed)==c.get('true_independent_completed_panels',0)
    actual_repairs=sum(e['event']=='repair_check' for e in events)
    assert actual_repairs==c['repaired_reliances']
    used['A']+=.5*actual_repairs;used['C']+=.5*actual_repairs
    used['steward']=(c['offered_requests']-c.get('intake_capacity_rejections',0))*.05+(c['selection_attempts']-c.get('triage_capacity_rejections',0))*.02+c['reserved_panels']*.1+c['relied_requests']*.1+actual_repairs*.1
    for row in data['ledger']:
        assert abs(used[row['person']]-row['used'])<1e-10
        assert abs(sum(row['lanes'].values())-row['used'])<1e-10
        assert abs(row['held'])<1e-10
    assert abs(sum(used.values())-data['total_hours'])<1e-10
    # Hidden true chain reaches all requests, declared chain reaches 0..3 only.
    noticed=[r for r in data['receipts'] if r['request']<4]
    assert len(noticed)==c['noticed_affected_reliances']
    assert all(r['currentness']=='unresolved_material_change' for r in noticed)
    assert all(r['currentness']=='as_recorded' for r in data['receipts'] if r['request']>=4)
    return {'counts_reconstructed':True,'all_person_debits_reconstructed':True,'no_automatic_repair_renewal':True,'completed':len(completed),'hours':sum(used.values())}

def main():
    output={'interpretation':'Independent adversarial reconstruction; synthetic traces only'}
    finite={}
    for retry in ('fixed_panel','reroll'):
        got=tree(retry);ref=one_request_oracle(Config(retry=retry),{'A':F(1),'B':F(1,4),'C':F(1)})
        assert got==ref
        finite[retry]={k:str(v) for k,v in got.items()}
    output['independent_path_oracle']=finite
    traces={}
    for name in ('group_first_scarce','group_first_plentiful','naive_scarce','hidden_control','selective_reliance'):
        saved=json.loads((PACKET/'models/coupled/results'/f'{name}.json').read_text())
        fresh=run(Config(**saved['config']),saved['seed'],trace=True)
        assert json.loads(json.dumps(fresh))==saved
        traces[name]=reconstruct_trace(saved)
    output['traces']=traces
    # Reconstruct all 7,400 runs, all reported means, and pooled shares.
    summary=json.loads((PACKET/'models/coupled/results/summary.json').read_text())
    metrics=('completed_requests','unresolved_requests','relied_requests','reservation_failures','retry_attempts','refuse_actors','repaired_reliances','pending_repairs','unnoticed_affected_reliances','full_effort_completed_panels','true_independent_completed_panels','total_hours')
    checked=0
    csv_rows={(int(row["scenario"]),row["metric"]):row for row in csv.DictReader((PACKET/"models/coupled/results/policy-sweep.csv").open())}
    interval_checks=0
    for entry in summary['scenario_results']:
        cfg=Config(**{k:entry[k] for k in Config.__dataclass_fields__})
        samples=[run(cfg,70000+j) for j in range(100)]
        for key in metrics:
            vals=[s['total_hours'] if key=='total_hours' else s['counts'].get(key,0) for s in samples]
            mean=statistics.mean(vals)
            assert abs(mean-entry[key])<1e-12
            # Independent variance identity; 100 replicate units, not 1,200 requests.
            se=math.sqrt(sum((v-mean)**2 for v in vals)/(len(vals)*(len(vals)-1)))
            row=csv_rows[entry['scenario'],key]
            assert abs(float(row['normal95_low'])-(mean-1.96*se))<1e-12
            assert abs(float(row['normal95_high'])-(mean+1.96*se))<1e-12
            interval_checks+=1
        for stage in ('initial','selected','reserved','completed','relied'):
            n=sum(s['counts'].get(stage+'_panels',0) for s in samples)
            k=sum(s['counts'].get('A_'+stage+'_panels',0) for s in samples)
            assert n==entry[stage+'_panels_total']
            assert (k/n if n else None)==entry['A_'+stage+'_share']
        checked+=len(samples)
    output['sweep_reproduced_runs']=checked
    output['independent_replicate_interval_checks']=interval_checks
    # Preserve the second-wave discovered endpoint defect independently of repaired code.
    archived={};exec(compile((ROOT/'original_hard_audit.txt').read_text(),'archived_hard_audit','exec'),archived)
    interval=archived['hard_audit_interval'](0,1,0,0,0,0,6,1,5)
    try:archived['blinded_audit_sample'](6,interval['maximum_audit'],1,5,random.Random(1))
    except ValueError as error:output['preserved_RM3']={'returned_feasible':interval['feasible'],'returned_maximum':interval['maximum_audit'],'sample_error':str(error)}
    else:raise AssertionError('archived RM3 endpoint failure missing')
    output['reviewed_source_sha256']={str(p.relative_to(PACKET)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [PACKET/'models/coupled/simulator.py',PACKET/'models/math/protocol_math.py']}
    (ROOT/'second-wave-results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))
if __name__=='__main__':main()
