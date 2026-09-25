"""Adversarial public-API probes; no internal dictionaries are modified.

This is a diagnostic, not a suite that mistakes retained defects for correctness.
Results expose baseline behavior, and can change after author repairs.
"""
import json
import sys
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'models'))
from toy_agents.protocol import Target, Rejected, Actor, Protocol, PolicyAgent
from toy_agents.scenarios import fixture
from release_cycle import fixture as release_fixture, BoundaryError


def toy_reliance():
    p = fixture()
    t = Target('claim', 'v1', 'fixture:source')
    o = p.offer(t, 'author', {'numerics'})
    c = PolicyAgent('reviewer-a').act(p, o, {'numerics'}, now=1)
    r = p.rely(o, 'scientist', [c], 'fixture use', {'numerics'}, 'scientific', 10, now=1)
    return p, t, o, c, r


def contradiction_after_reliance():
    p,t,o,c,r = toy_reliance()
    PolicyAgent('reviewer-b', 'contradiction').act(p,o,{'numerics'},now=2)
    old = p.currentness(r, now=3, observed_at=3, max_age=1)
    try:
        p.rely(o,'scientist',[c],'fixture use',{'numerics'},'scientific',10,now=3)
        new = 'accepted'
    except Rejected as e:
        new = str(e)
    return {'old_reliance': old, 'identical_new_reliance': new}


def currentness_clock():
    p,t,o,c,r = toy_reliance()
    late = p.currentness(r, now=10, observed_at=10, max_age=1)
    try:
        early = p.currentness(r, now=2, observed_at=2, max_age=1)
    except Rejected as e:
        early = str(e)
    return {'query_at_10':late,'subsequent_query_at_2':early}


def release_approved():
    m,c,d = release_fixture()
    m.verify(c,d,'verifier',{k: True for k in m.required_checks},1,15)
    return m,c,d


def observation_metadata_rebinding():
    m,c,d = release_approved()
    m.publish(c,d,'publisher',2)
    other = replace(c, source_revision='never-published-revision', evidence_digest='never-published-evidence')
    m.verify(other,d,'verifier',{k: True for k in m.required_checks},3,15)
    receipt = m.observe(other,'observer',4)
    state = m.currentness(other,d,5)
    try:
        published = m.publish(other,d,'publisher',6)
    except BoundaryError as e:
        published = str(e)
    return {'other_candidate_observation':receipt,'currentness':state,'publish':published,
            'bindings_differ':c.binding != other.binding}


def failed_future_action_advances_clock():
    m,c,d = release_approved()
    try:
        m.publish(c,d,'not-publisher',1_000_000)
    except BoundaryError as e:
        first = str(e)
    try:
        second = m.publish(c,d,'publisher',2)
    except BoundaryError as e:
        second = str(e)
    return {'invalid_future_attempt':first,'subsequent_valid_attempt':second,'clock':m.clock}


def author_contract_weakening():
    # Revised probe after contract API was added: the floor belongs to offer,
    # not a previous caller's one-off stronger reliance request.
    actors = [Actor('a','A',frozenset(),frozenset({'scientific'})),
              Actor('r','R',frozenset({'x'}))]
    p=Protocol(actors,{'r':2},{('r','x'):2})
    o=p.offer(Target('c','v','e'),'a',{'x'},required_groups=2)
    c=PolicyAgent('r').act(p,o,{'x'})
    results={}
    for requested in (2,1):
        try:
            r=p.rely(o,'a',[c],'use',{'x'},'scientific',10,required_groups=requested)
            results[str(requested)]='accepted'
        except Rejected as e:
            results[str(requested)]=str(e)
    return {'offer_floor':2,'reliance_requests':results,
            'scope_limit':'author chooses offer floor; external approval of its adequacy is not modeled'}


def hidden_person_aliases():
    p=Protocol([Actor('a','A',frozenset()),Actor('r1','R',frozenset({'x'})),Actor('r2','R',frozenset({'x'}))],
               {'r1':1,'r2':1},{('r1','x'):1,('r2','x'):1})
    o=p.offer(Target('c','v','e'),'a',{'x'})
    for who in ('r1','r2'): PolicyAgent(who).act(p,o,{'x'})
    return {'charged_actor_totals':p.ledger.totals()[0],
            'if_both_labels_are_one_person_total_work':2,'declared_upstream_person_capacity':1,
            'classification':'known excluded capacity-key premise violation; not fixed by control-group labels'}



def amendment_chain_and_target_binding():
    m,a,d = release_approved()
    m.publish(a,d,'publisher',2)
    b=replace(a,release_id='release-2',content=b'corrected')
    m.amend(a,b,3)
    m.verify(b,d,'verifier',{k: True for k in m.required_checks},4,15)
    m.publish(b,d,'publisher',5)
    try:
        m.amend(b,a,6)
        cycle='accepted'
    except BoundaryError as e:
        cycle=str(e)
    c=replace(a,release_id='release-3',content=b'intended correction')
    try:
        m.amend(a,c,7)
        overwrite='accepted'
    except BoundaryError as e:
        overwrite=str(e)
    m2,a,d = release_approved()
    m2.publish(a,d,'publisher',2)
    m2.amend(a,c,3)
    other=replace(c,source_revision='other-revision',content=b'other correction')
    try:
        m2.verify(other,d,'verifier',{k: True for k in m2.required_checks},4,15)
        rebound=m2.publish(other,d,'publisher',5)
    except BoundaryError as e:
        rebound=str(e)
    return {'cycle':cycle,'successor_overwrite':overwrite,'other_bound_replacement':rebound,
            'intended_binding':c.binding,'published_alternative_binding':other.binding}

def main():
    results={f.__name__:f() for f in [contradiction_after_reliance,currentness_clock,
        observation_metadata_rebinding,failed_future_action_advances_clock,
        author_contract_weakening,hidden_person_aliases,amendment_chain_and_target_binding]}
    print(json.dumps(results,indent=2,sort_keys=True))

if __name__=='__main__':main()
