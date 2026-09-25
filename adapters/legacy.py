"""Synthetic legacy metadata adapter. No API connector or format conformance."""
from __future__ import annotations
import copy
import hashlib
import json
import re
from typing import Any

class AdapterError(ValueError):
    pass

FIELDS={
    'claim_id':('claim','id'),
    'version_ref':('claim','version_ref'),
    'evidence_ref':('claim','evidence_ref'),
    'immutable_refs':('claim','immutable_refs'),
    'check_scope':('review','scope'),
    'check_result':('review','result'),
    'check_method':('review','method'),
    'check_limits':('review','limits'),
    'review_recommendation':('review','recommendation'),
    'authorizations':('authorizations',),
    'control_groups':('control_groups',),
    'dependencies':('dependencies',),
}

def canonical(value: Any) -> bytes:
    def validate(v):
        if v is None or type(v) in (str,bool,int):return
        if type(v) is float:
            if not __import__('math').isfinite(v):raise AdapterError('nonfinite JSON number')
            return
        if type(v) is list:
            for x in v:validate(x)
            return
        if type(v) is dict:
            if any(type(k) is not str for k in v):raise AdapterError('JSON object keys must be strings')
            for x in v.values():validate(x)
            return
        raise AdapterError('expected a JSON value tree')
    validate(value)
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')


def slot(source, path):
    node=source
    for index,key in enumerate(path):
        if not isinstance(node,dict):
            return {'status':'blocked_by_nonobject','at':'.'.join(path[:index]),'value':copy.deepcopy(node)}
        if key not in node:return {'status':'absent'}
        node=node[key]
    if node is None:return {'status':'null','value':None}
    if node=='' or node==[] or node=={}:return {'status':'explicit_empty','value':copy.deepcopy(node)}
    return {'status':'value','value':copy.deepcopy(node)}


def adapt(source):
    if type(source) is not dict:raise AdapterError('legacy input must be a JSON object')
    raw=canonical(source)
    mapped={name:slot(source,path) for name,path in FIELDS.items()}
    issues=[]
    for name in ('authorizations','control_groups','dependencies'):
        issues.append({'field':name,'source_status':mapped[name]['status'],
                       'effect':'not interpreted as verified protocol assertions; explicit enrichment required'})
    result=mapped['check_result'].get('value')
    recommendation=mapped['review_recommendation'].get('value')
    if result not in ('support','contradiction','unknown'):
        issues.append({'field':'check_result','effect':'unsupported or missing result; never inferred from recommendation'})
    if recommendation in ('accept','approve') and result in ('contradiction','unknown'):
        issues.append({'field':'review_recommendation','effect':'recommendation/result tension retained; recommendation cannot override result'})
    if mapped['check_limits']['status']=='explicit_empty':
        issues.append({'field':'check_limits','effect':'explicitly empty is not a positive assertion of no limitations'})
    mapped_paths={'.'.join(path) for path in FIELDS.values()}
    def leaves(value,path=()):
        if isinstance(value,dict) and value:
            for key,child in value.items():
                yield from leaves(child,path+(key,))
        else:
            yield '.'.join(path)
    for path in leaves(source):
        if not any(path==known or path.startswith(known+'.') for known in mapped_paths):
            issues.append({'field':path,'effect':'preserved only in raw legacy payload; no protocol authority inferred'})
    return {'adapter':'mcrp-synthetic-legacy/0.1','source_sha256':hashlib.sha256(raw).hexdigest(),
            'source':copy.deepcopy(source),'mapped':mapped,
            'loss_report':{'roundtrip':'lossless JSON-value roundtrip; original bytes/whitespace/key order not certified',
                           'semantic_projection':'partial and deliberately non-authorizing','items':issues},
            'protocol_assertions':{'authorization':'unknown','independence':'unknown','dependency_completeness':'unknown'}}


def roundtrip(envelope):
    expected=adapt(envelope['source'])
    # Python equality conflates True/1 and 1/1.0. Canonical JSON preserves
    # those token-type distinctions; compare serialized values, not dict ==.
    if canonical(envelope)!=canonical(expected):raise AdapterError('envelope does not match deterministic source projection')
    return copy.deepcopy(envelope['source'])


def _value(envelope,name):
    field=envelope['mapped'][name]
    if field['status']!='value':raise AdapterError(name+': explicit nonempty value required')
    return field['value']


def execute_fixture(envelope, enrichment=None):
    """Explicitly enriched trusted toy cycle; refuses unaugmented legacy input.

    Enrichment is separate synthetic authority, not discovered metadata. Its
    complete JSON is retained with the result. It must be supplied consciously.
    """
    roundtrip(envelope)
    if enrichment is None:raise AdapterError('legacy metadata supplies no trusted authority, control or dependency assertions')
    required={'synthetic_fixture','fixture_responsibility','author_group','reviewer_group','decision_group',
              'reviewer_skills','decision_roles','dependencies','purpose','scope','expires','capacity','limitations'}
    if type(enrichment) is not dict or set(enrichment)!=required or enrichment.get('synthetic_fixture') is not True:
        raise AdapterError('exact separately explicit synthetic enrichment fields required')
    canonical(enrichment)
    for name in ('fixture_responsibility','author_group','reviewer_group','decision_group','purpose','limitations'):
        if type(enrichment[name]) is not str or not enrichment[name].strip():raise AdapterError(name+': nonempty assertion required')
    if enrichment['dependencies']!=[]:
        raise AdapterError('this one-target adapter demo accepts only explicitly asserted empty dependency list')
    # Do not overwrite a source's disclosed prerequisite list with an empty graph.
    dep=envelope['mapped']['dependencies']
    if dep['status']=='value' or dep['status']=='blocked_by_nonobject':
        raise AdapterError('nonempty/malformed legacy dependencies unsupported; preserve and resolve them outside this demo')
    for name in ('authorizations','control_groups'):
        if envelope['mapped'][name]['status'] in ('value','blocked_by_nonobject'):
            raise AdapterError(name+': nonempty legacy assertions require reconciliation outside this narrow demo')
    if dep['status']=='explicit_empty' and dep.get('value')!=[]:
        raise AdapterError('legacy dependencies must be a list when explicitly empty')
    for name in ('reviewer_skills','decision_roles','scope'):
        if type(enrichment[name]) is not list or not enrichment[name] or any(type(x) is not str or not x.strip() for x in enrichment[name]):
            raise AdapterError(name+': nonempty explicit string list required')
    for name in ('expires','capacity'):
        if type(enrichment[name]) is not int or enrichment[name]<1:raise AdapterError(name+': positive integer required')
    if enrichment['expires']<=1:raise AdapterError('expiry must follow the demonstration amendment at time one')
    claim=_value(envelope,'claim_id'); version=_value(envelope,'version_ref'); evidence=_value(envelope,'evidence_ref')
    if type(claim) is not str or not claim.strip() or not isinstance(version,str) or re.fullmatch(r'git:[0-9a-f]{40}',version) is None or not isinstance(evidence,str) or re.fullmatch(r'sha256:[0-9a-f]{64}',evidence) is None or _value(envelope,'immutable_refs') is not True:
        raise AdapterError('declared exact claim, git object and SHA-256 references required; no URL-only target')
    scope=_value(envelope,'check_scope'); outcome=_value(envelope,'check_result'); method=_value(envelope,'check_method')
    if type(scope) is not list or not scope or any(type(x) is not str or not x.strip() for x in scope):raise AdapterError('explicit scope list required')
    if set(enrichment['scope'])!=set(scope):raise AdapterError('fixture must preserve original check scope exactly')
    if outcome not in ('support','contradiction','unknown') or type(method) is not str or not method.strip():raise AdapterError('explicit method and supported check result required')
    from toy_agents.protocol import Actor,Target,Protocol
    actors=[Actor('legacy-author',enrichment['author_group'],frozenset()),
            Actor('legacy-reviewer',enrichment['reviewer_group'],frozenset(enrichment['reviewer_skills'])),
            Actor('fixture-decision',enrichment['decision_group'],frozenset(),frozenset(enrichment['decision_roles']))]
    p=Protocol(actors,{'legacy-reviewer':enrichment['capacity']},
               {('legacy-reviewer',s):enrichment['capacity'] for s in enrichment['reviewer_skills']})
    target=Target(claim,version,evidence)
    offer=p.offer(target,'legacy-author',scope,dependencies=())
    # Keep legacy limitations alongside explicit fixture limitations; empty source
    # limitations never become an assertion that the actual check had no limits.
    limits=json.dumps({'legacy':envelope['mapped']['check_limits'],'fixture':enrichment['limitations']},sort_keys=True)
    check=p.check(offer,'legacy-reviewer',scope,method,outcome,limits,now=0)
    reliance=p.rely(offer,'fixture-decision',[check],enrichment['purpose'],scope,'scientific',enrichment['expires'],now=0)
    before=p.currentness(reliance,now=0,observed_at=0,max_age=0)
    p.amend(target,'Synthetic later material evidence change',now=1)
    after=p.currentness(reliance,now=1,observed_at=1,max_age=0)
    return {'adapter_envelope':copy.deepcopy(envelope),'trusted_fixture_enrichment':copy.deepcopy(enrichment),
            'offer':offer,'check':check,'reliance':reliance,'before_amendment':before,
            'after_amendment':after,'events':p.events,
            'limitations':'Synthetic declared metadata only; no origin authentication, consent, live connector or dependency discovery.'}
