"""Bounded local JSON interface to the existing synthetic protocol runtime.

Trusted caller/policy only. An agent_id is not authenticated by this interface.
No network, subprocess, arbitrary execution, path dereference or persistence.
"""
import copy
from dataclasses import asdict
import hashlib
import json
import math
from pathlib import Path
import sys

PACKET=Path(__file__).resolve().parents[1]
if str(PACKET) not in sys.path:sys.path.insert(0,str(PACKET))
from toy_agents.protocol import Actor,Target,Protocol,Rejected
from adapters.legacy import canonical,adapt,AdapterError

SCHEMA='mcrp-agent-task/0.1'
POLICY_SCHEMA='mcrp-agent-policy/0.1'
MAX_BYTES=262144
MAX_COMMANDS=64


class InputError(ValueError):pass


def text(value,name):
    if type(value) is not str or not value.strip() or len(value)>4096:raise InputError(name+': nonempty string <=4096 characters required')
    return value


def integer(value,name,zero=False):
    if type(value) is not int or not (0 if zero else 1)<=value<=1000000:raise InputError(name+': bounded integer required')
    return value


def fields(value,required,optional=()):
    if type(value) is not dict or set(value)-set(required)-set(optional) or set(required)-set(value):
        raise InputError('exact required/optional fields violated: '+','.join(sorted(required)))


def labels(value,name,empty=False):
    if type(value) is not list or len(value)>128 or (not empty and not value):raise InputError(name+': bounded list required')
    for x in value:text(x,name)
    if len(set(value))!=len(value):raise InputError(name+': duplicate labels')
    return value


def bounded_tree(value,depth=0,count=None):
    if count is None:count=[0]
    count[0]+=1
    if depth>16 or count[0]>10000:raise InputError('JSON depth/node limit exceeded')
    if type(value) is dict:
        if len(value)>128:raise InputError('JSON object member limit exceeded')
        for key,child in value.items():
            text(key,'JSON key');bounded_tree(child,depth+1,count)
    elif type(value) is list:
        if len(value)>128:raise InputError('JSON array limit exceeded')
        for child in value:bounded_tree(child,depth+1,count)
    elif type(value) is str:
        if len(value)>4096:raise InputError('JSON string limit exceeded')
    elif type(value) is float:
        if not math.isfinite(value):raise InputError('nonfinite number')
    elif value is not None and type(value) not in (bool,int):raise InputError('invalid JSON value')
    elif type(value) is int and len(str(abs(value)))>16:raise InputError('integer token too long')


def parse(raw):
    if not isinstance(raw,bytes) or len(raw)>MAX_BYTES:raise InputError('input byte limit exceeded')
    def pairs(items):
        result={}
        for key,value in items:
            if key in result:raise InputError('duplicate JSON key')
            result[key]=value
        return result
    def number(token):
        if len(token)>17:raise InputError('integer token too long')
        return int(token)
    def floating(token):
        if len(token)>32:raise InputError('float token too long')
        result=float(token)
        if not math.isfinite(result):raise InputError('nonfinite number')
        return result
    def invalid(token):raise InputError('nonfinite JSON constant')
    try:
        value=json.loads(raw.decode('utf-8'),object_pairs_hook=pairs,parse_int=number,parse_float=floating,parse_constant=invalid)
        bounded_tree(value);return value
    except (UnicodeDecodeError,json.JSONDecodeError,RecursionError) as error:raise InputError('invalid or too deeply nested JSON') from error


def digest(value):return 'sha256:'+hashlib.sha256(canonical(value)).hexdigest()


def load_policy(policy):
    bounded_tree(policy)
    fields(policy,('schema','synthetic_fixture','policy_id','principals','agents'))
    if policy['schema']!=POLICY_SCHEMA or policy['synthetic_fixture'] is not True:raise InputError('explicit synthetic policy schema required')
    text(policy['policy_id'],'policy id')
    if type(policy['principals']) is not list or not 1<=len(policy['principals'])<=16:raise InputError('1..16 principals required')
    principals={};actors=[];capacities={};skill_caps={}
    allowed_ops={'offer','check','rely','amend','observe','availability','adapt_legacy'}
    for row in policy['principals']:
        fields(row,('principal_id','control_group','skills','roles','capacity','skill_capacity','operations'))
        pid=text(row['principal_id'],'principal')
        if pid in principals:raise InputError('duplicate principal')
        group=text(row['control_group'],'control group')
        skills=labels(row['skills'],'skills',True);roles=labels(row['roles'],'roles',True)
        if set(roles)-{'scientific','publication'}:raise InputError('unknown role')
        operations=labels(row['operations'],'operations',True)
        if set(operations)-allowed_ops:raise InputError('unknown operation')
        capacities[pid]=integer(row['capacity'],'capacity',True)
        if type(row['skill_capacity']) is not dict or set(row['skill_capacity'])!=set(skills):raise InputError('exact skill capacities required')
        for skill,amount in row['skill_capacity'].items():skill_caps[pid,skill]=integer(amount,'skill capacity',True)
        actors.append(Actor(pid,group,frozenset(skills),frozenset(roles)))
        principals[pid]=row
    if type(policy['agents']) is not list or not 1<=len(policy['agents'])<=32:raise InputError('1..32 agents required')
    agents={}
    for row in policy['agents']:
        fields(row,('agent_id','principal_id'))
        aid=text(row['agent_id'],'agent');pid=text(row['principal_id'],'principal')
        if aid in agents or pid not in principals:raise InputError('duplicate agent or unknown principal')
        agents[aid]=pid
    return Protocol(actors,capacities,skill_caps),principals,agents


def json_record(value):
    if hasattr(value,'__dataclass_fields__'):return json_record(asdict(value))
    if type(value) is dict:return {str(k):json_record(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [json_record(x) for x in value]
    if isinstance(value,(set,frozenset)):return [json_record(x) for x in sorted(value)]
    return value


def ledger_view(p):
    used,skills=p.ledger.totals()
    return [{'principal_id':key,'capacity_units':cap,'charged_units':used.get(key,0),
             'skills':{skill:{'capacity':amount,'charged':skills.get((who,skill),0)}
                       for (who,skill),amount in sorted(p.ledger.skill_capacity.items()) if who==key}}
            for key,cap in sorted(p.ledger.person_capacity.items())]


def apply(p,aliases,principal,command):
    action=command['action'];data=command['input'];now=integer(command['now'],'now',True)
    p._time(now)
    def ref(name,kind):
        key=text(name,'reference')
        if key not in aliases or aliases[key]['kind']!=kind:raise InputError('unknown or wrong-kind reference: '+key)
        return aliases[key]['record_id']
    if action=='offer':
        fields(data,('claim_id','claim','evidence','scope','dependencies','required_groups'))
        claim_id=text(data['claim_id'],'claim id');claim=text(data['claim'],'claim')
        if type(data['evidence']) is not dict:raise InputError('evidence must be an inline JSON object')
        scope=labels(data['scope'],'scope');deps=labels(data['dependencies'],'dependencies',True)
        required=integer(data['required_groups'],'required groups')
        if required>16:raise InputError('group count exceeds bounded fixture')
        dependencies=tuple(p.offers[ref(x,'offer')].target for x in deps)
        profile={'claim_id':claim_id,'claim':claim,'evidence':data['evidence'],'scope':sorted(scope),
                 'dependencies':[json_record(t) for t in sorted(dependencies)],'required_groups':required}
        target=Target(claim_id,digest(profile),digest(data['evidence']))
        rid=p.offer(target,principal,scope,dependencies,required)
        result={'record':json_record(p.offers[rid]),'claim':claim,'evidence':data['evidence'],
                'version_basis':'canonical claim/evidence/scope/resolved-dependencies/required-groups offer profile'}
        kind='offer'
    elif action=='check':
        fields(data,('offer','scope','method','outcome','limits','units'))
        rid=p.check(ref(data['offer'],'offer'),principal,labels(data['scope'],'scope'),text(data['method'],'method'),
                    text(data['outcome'],'outcome'),text(data['limits'],'limits'),integer(data['units'],'units'),now)
        result={'record':json_record(p.checks[rid])};kind='check'
    elif action=='rely':
        fields(data,('offer','checks','purpose','scope','kind','expires'),('required_groups',))
        checks=labels(data['checks'],'checks')
        required=data.get('required_groups')
        if required is not None:integer(required,'required groups')
        elif 'required_groups' in data:raise InputError('explicit null required_groups unsupported')
        rid=p.rely(ref(data['offer'],'offer'),principal,[ref(x,'check') for x in checks],text(data['purpose'],'purpose'),
                   labels(data['scope'],'scope'),text(data['kind'],'kind'),integer(data['expires'],'expires'),now,required)
        result={'record':json_record(p.reliances[rid])};kind='reliance'
    elif action=='amend':
        fields(data,('offer','reason'))
        offer=p.offers[ref(data['offer'],'offer')]
        if offer.author_id!=principal:raise InputError('only offering principal may amend this fixture target')
        affected=p.amend(offer.target,text(data['reason'],'reason'),now)
        rid=None;result={'target':json_record(offer.target),'affected':json_record(affected)};kind='amendment'
    elif action=='availability':
        fields(data,('offer','available','reason'))
        text(data['reason'],'reason')
        if type(data['available']) is not bool:raise InputError('availability requires Boolean')
        offer=p.offers[ref(data['offer'],'offer')]
        if offer.author_id!=principal:raise InputError('only offering principal may change this fixture evidence availability')
        p.set_available(offer.target,data['available'])
        rid=None;result={'target':json_record(offer.target),'available':data['available'],'reason':data['reason']};kind='availability'
    elif action=='observe':
        fields(data,('reliance','observed_at','max_age'))
        observed=data['observed_at']
        if observed is not None:integer(observed,'observed_at',True)
        reliance_id=ref(data['reliance'],'reliance')
        state=p.currentness(reliance_id,now,observed,integer(data['max_age'],'max_age',True))
        rid=None;result={'reliance':reliance_id,'currentness':state,'now':now,'observed_at':observed,
                          'observation_basis':'caller-supplied synthetic clock, not live evidence observation'};kind='observation'
    elif action=='adapt_legacy':
        fields(data,('source',))
        rid=None;result={'projection':adapt(data['source'])};kind='non_authorizing_legacy_projection'
    else:raise InputError('unsupported action')
    p.clock=now
    if rid is not None:aliases[command['id']]={'kind':kind,'record_id':rid}
    return {'kind':kind,'record_id':rid,**result}


def execute(policy,envelope):
    bounded_tree(envelope)
    fields(envelope,('schema','synthetic_fixture','task_id','commands'))
    if envelope['schema']!=SCHEMA or envelope['synthetic_fixture'] is not True:raise InputError('explicit synthetic task schema required')
    text(envelope['task_id'],'task id')
    commands=envelope['commands']
    if type(commands) is not list or not 1<=len(commands)<=MAX_COMMANDS:raise InputError('1..64 commands required')
    seen=set()
    for command in commands:
        fields(command,('id','action','agent_id','now','input'))
        for key in ('id','action','agent_id'):text(command[key],key)
        if command['id'] in seen:raise InputError('duplicate command id')
        seen.add(command['id'])
        if type(command['input']) is not dict:raise InputError('command input must be object')
    p,principals,agents=load_policy(policy);aliases={};receipts=[]
    for command in commands:
        base={'command_id':command['id'],'action':command['action'],'asserted_agent_id':command['agent_id']}
        try:
            if command['agent_id'] not in agents:raise InputError('unknown asserted agent')
            pid=agents[command['agent_id']]
            base.update(principal_id=pid,declared_control_group=principals[pid]['control_group'])
            if command['action'] not in principals[pid]['operations']:raise InputError('operation not delegated by fixture policy')
            trial=copy.deepcopy(p);trial_aliases=copy.deepcopy(aliases)
            result=apply(trial,trial_aliases,pid,command)
            p,aliases=trial,trial_aliases
            receipts.append({**base,'status':'accepted_under_synthetic_policy',**result})
        except (InputError,Rejected,AdapterError) as error:
            receipts.append({**base,'status':'refused','code':'BOUNDED_POLICY_REFUSAL','reason':str(error)})
    refused=sum(r['status']=='refused' for r in receipts)
    state={'clock':p.clock,'aliases':aliases,'events':p.events,'ledger':ledger_view(p),
           'offers':{key:json_record(value) for key,value in p.offers.items()},
           'checks':{key:json_record(value) for key,value in p.checks.items()},
           'reliances':{key:json_record(value) for key,value in p.reliances.items()},
           'target_state':[{'target':json_record(t),'generation':p.generations[t],'available':p.available[t]} for t in sorted(p.generations)]}
    return {'schema':'mcrp-agent-result/0.1','task_id':envelope['task_id'],
            'mode':'local synthetic conformance only','policy_id':policy['policy_id'],'policy_digest':digest(policy),
            'request_digest':digest(envelope),'state_digest':digest(state),
            'status':'completed_with_refusals' if refused else 'completed',
            'counts':{'submitted_commands':len(commands),'accepted_commands':len(commands)-refused,'refused_commands':refused,
                      'offers':len(p.offers),'checks':len(p.checks),'reliances':len(p.reliances)},
            'receipts':receipts,'state':state,
            'boundaries':{'identity':'asserted agent ID resolved through trusted local policy; not authenticated',
                          'authority':'fixture role declarations only; no human, scientific or publication approval',
                          'capacity':'all aliases of one principal share its declared unit budget; overlapping real principals unmodeled',
                          'execution':'check methods/results are assertions; no arbitrary code or scientific validation executed',
                          'currentness':'simulation state and supplied times only; no remote notification or live observation'}}
