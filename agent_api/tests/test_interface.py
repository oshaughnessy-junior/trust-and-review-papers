import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
from interface import InputError,parse,execute,digest,MAX_BYTES
from build_examples import policy,request,command,DOMAINS


class InterfaceTests(unittest.TestCase):
    def test_four_domains_new_content_and_old_reliance_pending(self):
        for domain in DOMAINS:
            r=execute(policy(),request(domain));receipts={x['command_id']:x for x in r['receipts']}
            self.assertEqual(r['counts']['refused_commands'],1)
            self.assertEqual(receipts['stale-check-refusal']['status'],'refused')
            self.assertEqual(receipts['observe-renewed']['currentness'],'current_under_toy_policy')
            self.assertEqual(receipts['observe-original']['currentness'],'reconsideration_pending')
            self.assertNotEqual(receipts['offer']['record']['target'],receipts['offer-updated']['record']['target'])
            self.assertNotEqual(receipts['offer']['evidence'],receipts['offer-updated']['evidence'])
            self.assertEqual(receipts['recheck']['record']['offer_id'],receipts['offer-updated']['record_id'])

    def test_replay_is_deterministic(self):
        self.assertEqual(execute(policy(),request('biology')),execute(policy(),request('biology')))

    def test_inline_content_binds_version_and_evidence(self):
        a=request('physics_astro');a['commands']=a['commands'][:1]
        b=copy.deepcopy(a);b['commands'][0]['input']['evidence']['x']=11
        ra=execute(policy(),a)['receipts'][0]['record']['target'];rb=execute(policy(),b)['receipts'][0]['record']['target']
        self.assertNotEqual(ra['version'],rb['version']);self.assertNotEqual(ra['evidence_digest'],rb['evidence_digest'])
        self.assertEqual(ra['evidence_digest'],digest(a['commands'][0]['input']['evidence']))

    def test_profile_metadata_change_gets_new_version_without_false_evidence_change(self):
        r=request('biology');r['commands']=r['commands'][:1]
        root=copy.deepcopy(r['commands'][0]);root['id']='dependency';root['input']['claim_id']='dependency-claim'
        revised=copy.deepcopy(r['commands'][0]);revised.update(id='revised-profile',now=1)
        revised['input']['dependencies']=['dependency'];revised['input']['required_groups']=2
        r['commands']=[root,r['commands'][0],revised]
        result=execute(policy(),r)
        self.assertEqual(result['counts']['refused_commands'],0)
        old=result['receipts'][1]['record']['target'];new=result['receipts'][2]['record']['target']
        self.assertNotEqual(old['version'],new['version'])
        self.assertEqual(old['evidence_digest'],new['evidence_digest'])

    def test_boolean_integer_float_distinction(self):
        self.assertNotEqual(digest({'x':True}),digest({'x':1}))
        self.assertNotEqual(digest({'x':1.0}),digest({'x':1}))
        r=request('biology');r['commands'][1]['input']['units']=True
        result=execute(policy(),r)
        self.assertEqual(result['receipts'][1]['status'],'refused')

    def test_unknown_fields_and_duplicate_aliases_fail_closed(self):
        r=request('law');r['extra']='ignored?'
        with self.assertRaises(InputError):execute(policy(),r)
        r=request('law');r['commands'][1]['id']='offer'
        with self.assertRaises(InputError):execute(policy(),r)
        r=request('law');r['commands'][1]['input']['roles']=['scientific']
        self.assertEqual(execute(policy(),r)['receipts'][1]['status'],'refused')

    def test_parser_rejects_duplicate_keys_nonfinite_huge_depth_and_bytes(self):
        for raw in (b'{"a":1,"a":2}',b'{"x":NaN}',b'{"x":1e999}',b'['*1000+b'0'+b']'*1000,b'0'*(MAX_BYTES+1),b'{"x":123456789012345678}'):
            with self.assertRaises(InputError):parse(raw)

    def test_request_cannot_grant_agent_or_principal(self):
        r=request('biology');r['commands'][2]['agent_id']='review-agent'
        result=execute(policy(),r)
        self.assertEqual(result['receipts'][2]['status'],'refused')
        r['commands'][2]['agent_id']='invented-agent'
        self.assertEqual(execute(policy(),r)['receipts'][2]['status'],'refused')

    def test_aliases_share_principal_budget(self):
        p=policy();p['principals'][1]['capacity']=1
        p['principals'][1]['skill_capacity']={k:1 for k in p['principals'][1]['skills']}
        r=request('physics_astro');r['commands']=r['commands'][:2]
        again=copy.deepcopy(r['commands'][1]);again.update(id='child-check',agent_id='review-team-child',now=2)
        r['commands'].append(again)
        result=execute(p,r)
        self.assertEqual(result['receipts'][-1]['status'],'refused')
        spent=next(x for x in result['state']['ledger'] if x['principal_id']=='reviewer-principal')
        self.assertEqual(spent['charged_units'],1)

    def test_aliases_do_not_multiply_independent_coverage(self):
        r=request('biology');r['commands']=r['commands'][:3]
        r['commands'][0]['input']['required_groups']=2
        child=copy.deepcopy(r['commands'][1]);child.update(id='child-check',agent_id='review-team-child')
        r['commands'].insert(2,child)
        r['commands'][-1]['input']['checks']=['check','child-check']
        self.assertEqual(execute(policy(),r)['receipts'][-1]['status'],'refused')
        # A genuinely different declared control group supplies the missing fixture coverage.
        r['commands'][2]['agent_id']='second-review-agent'
        self.assertEqual(execute(policy(),r)['receipts'][-1]['status'],'accepted_under_synthetic_policy')

    def test_future_failed_action_rolls_back_clock_aliases_and_events(self):
        r=request('law');r['commands']=r['commands'][:4]
        baseline=execute(policy(),r)
        bad=copy.deepcopy(r['commands'][2]);bad.update(id='future-bad',now=999)
        r['commands'].insert(3,bad)
        result=execute(policy(),r)
        self.assertEqual(result['receipts'][3]['status'],'refused')
        self.assertEqual(result['state'],baseline['state'])
        self.assertEqual(result['state_digest'],baseline['state_digest'])

    def test_wrong_principal_cannot_amend(self):
        p=policy();p['principals'][3]['operations'].append('amend')
        r=request('law');r['commands']=r['commands'][:5];r['commands'][-1]['agent_id']='decision-agent'
        result=execute(p,r)
        self.assertEqual(result['receipts'][-1]['status'],'refused')
        self.assertEqual(result['state']['target_state'][0]['generation'],0)

    def test_cross_scope_check_and_publication_upgrade_refused(self):
        r=request('biology');r['commands']=r['commands'][:3]
        r['commands'][1]['input']['scope']=['calibration']
        self.assertEqual(execute(policy(),r)['receipts'][1]['status'],'refused')
        r=request('biology');r['commands']=r['commands'][:3];r['commands'][2]['input']['kind']='publication'
        self.assertEqual(execute(policy(),r)['receipts'][2]['status'],'refused')

    def test_unavailable_evidence_and_missing_observation_are_explicit(self):
        r=request('biology');r['commands']=r['commands'][:3]
        r['commands'] += [command('missing','observe','decision-agent',3,{'reliance':'rely','observed_at':None,'max_age':0}),
                          command('hide','availability','author-agent',4,{'offer':'offer','available':False,'reason':'toy access withdrawn'}),
                          command('look','observe','decision-agent',4,{'reliance':'rely','observed_at':4,'max_age':0})]
        result=execute(policy(),r)
        self.assertEqual(result['receipts'][3]['currentness'],'freshness_unknown')
        self.assertEqual(result['receipts'][-1]['currentness'],'dependency_unavailable')

    def test_legacy_projection_does_not_create_authority(self):
        r=request('law');r['commands']=[command('legacy','adapt_legacy','author-agent',0,
            {'source':{'review':{'recommendation':'accept'},'authorizations':['publication'],'control_groups':['trust-me']}})]
        result=execute(policy(),r)
        self.assertEqual(result['counts']['offers'],0);self.assertEqual(result['counts']['reliances'],0)
        self.assertEqual(result['receipts'][0]['projection']['protocol_assertions']['authorization'],'unknown')

    def test_batch_limit_applies_before_state(self):
        r=request('biology');r['commands']=r['commands']*6
        with self.assertRaises(InputError):execute(policy(),r)

    def test_cli_stdout_json_and_meaningful_exit_codes(self):
        cmd=[sys.executable,str(ROOT/'cli.py'),'--policy',str(ROOT/'examples/policy.json'),'--request','-']
        good=subprocess.run(cmd,input=json.dumps(request('biology')),text=True,capture_output=True)
        self.assertEqual(good.returncode,0);self.assertEqual(json.loads(good.stdout)['status'],'completed_with_refusals')
        bad=subprocess.run(cmd,input='{"schema":1,"schema":2}',text=True,capture_output=True)
        self.assertEqual(bad.returncode,2);self.assertEqual(json.loads(bad.stdout)['status'],'invalid_input')
        self.assertNotIn('Traceback',bad.stderr)


if __name__=='__main__':unittest.main()
