"""Write deterministic synthetic task fixtures and their locally executed results."""
import hashlib
import json
from pathlib import Path
import platform
from interface import execute

ROOT=Path(__file__).resolve().parent
DOMAINS={
 'physics_astro':('calibration-arithmetic','Synthetic signal x-offset is positive at x=10, offset=8.',{'x':10,'offset':8,'difference':2},'Offset changed to12: old positive-use conclusion needs reconsideration.'),
 'biology':('assay-arithmetic','Synthetic assay mean is5 for observations4 and6; no biological efficacy claim.',{'observations':[4,6],'mean':5,'scope':'arithmetic only'},'An input is corrected from6 to10: recompute the mean; no health inference.'),
 'economics_social':('selection-accounting','Synthetic sample has2 completions among4 offers; no population causal claim.',{'offered':4,'completed':2,'share':'0.5'},'One previously omitted offer is disclosed: denominator changes.'),
 'law':('timeline-accounting','Synthetic record lists a response before a fictional internal deadline; no legal advice.',{'response_tick':3,'fictional_deadline_tick':4,'jurisdiction':'none'},'The fictional receipt timestamp is corrected to5: old ordering must be reconsidered.')}


def principal(pid,group,skills,roles,operations,capacity=12):
 return {'principal_id':pid,'control_group':group,'skills':skills,'roles':roles,'capacity':capacity,
         'skill_capacity':{s:capacity for s in skills},'operations':operations}


def policy():
 skills=[v[0] for v in DOMAINS.values()]
 return {'schema':'mcrp-agent-policy/0.1','synthetic_fixture':True,'policy_id':'four-domain-local-fixture-v1',
         'principals':[principal('author-principal','author-control',[],[],['offer','amend','availability','adapt_legacy']),
                       principal('reviewer-principal','reviewer-control',skills,[],['check']),
                       principal('second-reviewer-principal','second-reviewer-control',skills,[],['check']),
                       principal('decision-principal','decision-control',[],['scientific'],['rely','observe'])],
         'agents':[{'agent_id':a,'principal_id':p} for a,p in [('author-agent','author-principal'),('review-agent','reviewer-principal'),
                    ('review-team-child','reviewer-principal'),('second-review-agent','second-reviewer-principal'),('decision-agent','decision-principal')]]}


def command(cid,action,agent,now,data):return {'id':cid,'action':action,'agent_id':agent,'now':now,'input':data}


def request(domain):
 skill,claim,evidence,reason=DOMAINS[domain]
 corrected={
  'physics_astro':('Synthetic signal x-offset is negative at x=10, offset=12.',{'x':10,'offset':12,'difference':-2}),
  'biology':('Synthetic assay mean is7 for observations4 and10; no biological efficacy claim.',{'observations':[4,10],'mean':7,'scope':'arithmetic only'}),
  'economics_social':('Synthetic sample has2 completions among5 offers; no population causal claim.',{'offered':5,'completed':2,'share':'0.4'}),
  'law':('Synthetic record lists a response after a fictional internal deadline; no legal advice.',{'response_tick':5,'fictional_deadline_tick':4,'jurisdiction':'none'})}
 new_claim,new_evidence=corrected[domain]
 offer={'claim_id':'toy-'+domain,'claim':claim,'evidence':evidence,'scope':[skill],'dependencies':[],'required_groups':1}
 check={'offer':'offer','scope':[skill],'method':'Caller asserts a manual synthetic fixture check; not executed by this interface','outcome':'support',
        'limits':'Only the disclosed toy calculation; no empirical or institutional validation','units':1}
 rely={'offer':'offer','checks':['check'],'purpose':'synthetic local demonstration only','scope':[skill],'kind':'scientific','expires':20}
 commands=[command('offer','offer','author-agent',0,offer),command('check','check','review-agent',1,check),
           command('rely','rely','decision-agent',2,rely),command('observe-before','observe','decision-agent',2,{'reliance':'rely','observed_at':2,'max_age':0}),
           command('amend','amend','author-agent',3,{'offer':'offer','reason':reason}),
           command('observe-after','observe','decision-agent',3,{'reliance':'rely','observed_at':3,'max_age':0}),
           command('stale-check-refusal','rely','decision-agent',3,rely),
           command('offer-updated','offer','author-agent',4,{**offer,'claim':new_claim,'evidence':new_evidence}),
           command('recheck','check','review-team-child',5,{**check,'offer':'offer-updated'}),
           command('renew','rely','decision-agent',6,{**rely,'offer':'offer-updated','checks':['recheck']}),
           command('observe-renewed','observe','decision-agent',6,{'reliance':'renew','observed_at':6,'max_age':0}),
           command('observe-original','observe','decision-agent',6,{'reliance':'rely','observed_at':6,'max_age':0})]
 return {'schema':'mcrp-agent-task/0.1','synthetic_fixture':True,'task_id':domain+'-bounded-cycle','commands':commands}


def main():
 (ROOT/'examples').mkdir(exist_ok=True);(ROOT/'results').mkdir(exist_ok=True)
 p=policy();(ROOT/'examples/policy.json').write_text(json.dumps(p,indent=2)+'\n')
 manifest=[]
 for domain in DOMAINS:
  req=request(domain);result=execute(p,req)
  (ROOT/'examples'/(domain+'.json')).write_text(json.dumps(req,indent=2)+'\n')
  (ROOT/'results'/(domain+'.json')).write_text(json.dumps(result,indent=2)+'\n')
  manifest.append({'domain':domain,'request':'examples/'+domain+'.json','result':'results/'+domain+'.json',
                   'expected_refused_commands':['stale-check-refusal'],
                   'expected_observations':['current_under_toy_policy','reconsideration_pending','current_under_toy_policy','reconsideration_pending'],
                   'request_digest':result['request_digest'],'state_digest':result['state_digest']})
 (ROOT/'results/manifest.json').write_text(json.dumps({'schema':'mcrp-agent-examples/0.1','python':platform.python_version(),
  'examples':manifest,'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.glob('*.py'))},
  'imported_sha256':{str(p.relative_to(ROOT.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                    (ROOT.parent/'toy_agents/protocol.py',ROOT.parent/'adapters/legacy.py')}},indent=2)+'\n')
 print(json.dumps({'domains':len(DOMAINS),'expected_stale_refusals':len(DOMAINS)}))

if __name__=='__main__':main()
