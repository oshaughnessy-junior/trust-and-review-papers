"""Independent adversarial tests for the local JSON entry point.

Uses the author's policy as an explicitly trusted synthetic fixture; no claims
of authenticating the supplied agent ID or of externally independent control.
"""
import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

PACKET = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PACKET / 'agent_api'))
from interface import InputError, execute, parse


def policy():
    return json.loads((PACKET / 'agent_api/examples/policy.json').read_text())


def command(cid, action, agent, now, data):
    return dict(id=cid, action=action, agent_id=agent, now=now, input=data)


def offer(cid='offer', **extra):
    data=dict(claim_id=cid, claim='The supplied integers sum to three',
              evidence={'a': 1, 'b': 2}, scope=['calibration-arithmetic'],
              dependencies=[], required_groups=1)
    data.update(extra)
    return command(cid, 'offer', 'author-agent', 0, data)


def check(cid='check', agent='review-agent', now=1, target='offer', **extra):
    data=dict(offer=target, scope=['calibration-arithmetic'], method='Declared arithmetic',
              outcome='support', limits='Synthetic asserted check only', units=1)
    data.update(extra)
    return command(cid, 'check', agent, now, data)


def rely(cid='rely', now=2, target='offer', checks=None, **extra):
    data=dict(offer=target, checks=checks or ['check'], purpose='Arithmetic lesson',
              scope=['calibration-arithmetic'], kind='scientific', expires=20)
    data.update(extra)
    return command(cid, 'rely', 'decision-agent', now, data)


def envelope(commands):
    return dict(schema='mcrp-agent-task/0.1', synthetic_fixture=True,
                task_id='independent-adversary', commands=commands)


class AgentInterfaceRed(unittest.TestCase):
    def run_commands(self, commands, fixture=None):
        return execute(fixture or policy(), envelope(commands))

    def test_one_principal_aliases_cannot_supply_two_groups(self):
        r=self.run_commands([offer(required_groups=2), check(),
            check('child', agent='review-team-child'), rely(checks=['check','child'])])
        self.assertEqual(r['receipts'][-1]['status'], 'refused')
        self.assertEqual(r['counts']['reliances'], 0)

    def test_aliases_share_capacity_and_failure_is_atomic(self):
        p=policy(); p['principals'][1]['capacity']=1
        commands=[offer(),check()]
        baseline=self.run_commands(commands,p)
        r=self.run_commands(commands+[check('child',agent='review-team-child',now=99)],p)
        self.assertEqual(r['receipts'][-1]['status'],'refused')
        self.assertEqual(r['state'],baseline['state'])

    def test_different_principals_same_control_do_not_supply_independence(self):
        p=policy();p['principals'][2]['control_group']='reviewer-control'
        r=self.run_commands([offer(required_groups=2),check(),
            check('other',agent='second-review-agent'),rely(checks=['check','other'])],p)
        self.assertEqual(r['receipts'][-1]['status'],'refused')

    def test_request_cannot_inject_role_or_publication_kind(self):
        bad=rely();bad['input']['roles']=['publication']
        r=self.run_commands([offer(),check(),bad])
        self.assertEqual(r['receipts'][-1]['status'],'refused')
        r=self.run_commands([offer(),check(),rely(kind='publication')])
        self.assertEqual(r['receipts'][-1]['status'],'refused')

    def test_author_control_check_and_foreign_amendment_refused(self):
        p=policy();p['principals'][1]['control_group']='author-control'
        r=self.run_commands([offer(),check()],p)
        self.assertEqual(r['receipts'][-1]['status'],'refused')
        p=policy();p['principals'][1]['operations'].append('amend')
        r=self.run_commands([offer(),command('foreign','amend','review-agent',1,
                            {'offer':'offer','reason':'not mine'})],p)
        self.assertEqual(r['receipts'][-1]['status'],'refused')

    def test_failed_future_command_does_not_poison_clock_or_alias(self):
        bad=check('bad',now=999,units=True)
        r=self.run_commands([offer(),bad,check()])
        baseline=self.run_commands([offer(),check()])
        self.assertEqual(r['state'],baseline['state'])
        self.assertNotIn('bad',r['state']['aliases'])

    def test_old_checks_cannot_cover_a_new_exact_content_version(self):
        second=offer('new',claim_id='offer',evidence={'a':2,'b':3})
        second['now']=2
        r=self.run_commands([offer(),check(),second,rely(target='new')])
        self.assertEqual(r['receipts'][-1]['status'],'refused')
        targets=[v['target'] for v in r['state']['offers'].values()]
        self.assertNotEqual(targets[0]['version'],targets[1]['version'])
        self.assertNotEqual(targets[0]['evidence_digest'],targets[1]['evidence_digest'])

    def test_amendment_blocks_old_check_and_preserves_old_reliance(self):
        amend=command('amend','amend','author-agent',3,{'offer':'offer','reason':'Changed premise'})
        observe=command('obs','observe','decision-agent',3,{'reliance':'rely','observed_at':3,'max_age':0})
        r=self.run_commands([offer(),check(),rely(),amend,rely('bad',now=3),observe])
        self.assertEqual(r['receipts'][-2]['status'],'refused')
        self.assertEqual(r['receipts'][-1]['currentness'],'reconsideration_pending')
        self.assertEqual(r['counts']['reliances'],1)

    def test_expiry_and_unavailable_evidence_are_not_refreshed_by_observation(self):
        obs=command('obs','observe','decision-agent',20,{'reliance':'rely','observed_at':20,'max_age':0})
        r=self.run_commands([offer(),check(),rely(),obs])
        self.assertEqual(r['receipts'][-1]['currentness'],'expired')
        unavailable=command('off','availability','author-agent',3,{'offer':'offer','available':False,'reason':'Fixture inaccessible'})
        r=self.run_commands([offer(),check(),rely(),unavailable,check('bad',now=3)])
        self.assertEqual(r['receipts'][-1]['status'],'refused')

    def test_bool_integer_and_null_coverage_are_not_interchangeable(self):
        for value in (True,1.0,None,'1'):
            with self.subTest(value=value):
                r=self.run_commands([offer(),check(units=value)])
                self.assertEqual(r['receipts'][-1]['status'],'refused')
        r=self.run_commands([offer(),check(),rely(required_groups=None)])
        self.assertEqual(r['receipts'][-1]['status'],'refused')

    def test_duplicate_command_ids_and_json_keys_rejected(self):
        with self.assertRaises(InputError):self.run_commands([offer(),offer()])
        for raw in (b'{"a":1,"a":2}',b'{"outer":{"a":1,"a":2}}'):
            with self.assertRaises(InputError):parse(raw)

    def test_nonfinite_depth_node_and_byte_limits(self):
        for raw in (b'{"x":NaN}',b'{"x":1e999}',b'['*40+b'0'+b']'*40,
                    b' '*262145,b'['+b'0,'*128+b'0]'):
            with self.subTest(raw=raw[:24]):
                with self.assertRaises(InputError):parse(raw)

    def test_envelope_unknown_fields_and_false_synthetic_flag_rejected(self):
        for key,value in (('roles',['publication']),('synthetic_fixture',1)):
            e=envelope([offer()]);e[key]=value
            with self.assertRaises(InputError):execute(policy(),e)

    def test_stateless_replay_is_deterministic_not_cross_batch_deduplication(self):
        e=envelope([offer(),check(),rely()])
        self.assertEqual(execute(policy(),e),execute(policy(),e))
        # Repeat executions start fresh; this is explicitly not durable replay protection.

    def test_asserted_known_agent_id_is_not_authentication(self):
        r=self.run_commands([offer(),check(),rely()])
        self.assertEqual(r['receipts'][-1]['status'],'accepted_under_synthetic_policy')
        self.assertIn('not authenticated',r['boundaries']['identity'])

    def test_cli_invalid_input_is_structured_json(self):
        result=subprocess.run([sys.executable,str(PACKET/'agent_api/cli.py'),
            '--policy',str(PACKET/'agent_api/examples/policy.json'),'--request','-'],
            input=b'{"duplicate":1,"duplicate":2}',capture_output=True,timeout=5)
        self.assertEqual(result.returncode,2)
        self.assertEqual(json.loads(result.stdout)['status'],'invalid_input')
        self.assertEqual(result.stderr,b'')

    def test_evidence_true_one_and_one_point_zero_have_distinct_versions(self):
        versions=[]
        for value in (True,1,1.0):
            r=self.run_commands([offer(evidence={'value':value})])
            versions.append(r['receipts'][0]['record']['target']['version'])
        self.assertEqual(len(set(versions)),3)

    def test_expected_digest_cannot_be_injected_as_unchecked_override(self):
        bad=offer();bad['input']['evidence_digest']='sha256:'+'0'*64
        r=self.run_commands([bad])
        self.assertEqual(r['receipts'][0]['status'],'refused')
        self.assertEqual(r['state']['offers'],{})

    def test_unknown_and_contradictory_checks_cannot_be_upgraded(self):
        for outcome in ('unknown','contradiction'):
            r=self.run_commands([offer(),check(outcome=outcome),rely()])
            self.assertEqual(r['receipts'][-1]['status'],'refused')

    def test_legacy_metadata_adapter_is_not_an_authority_grant(self):
        adapt=command('legacy','adapt_legacy','author-agent',0,{
            'source':{'review':{'recommendation':'approve'},
                      'authorizations':['publication'], 'control_groups':['external']}})
        r=self.run_commands([adapt,rely(target='legacy')])
        self.assertEqual(r['receipts'][0]['kind'],'non_authorizing_legacy_projection')
        self.assertEqual(r['receipts'][-1]['status'],'refused')
        self.assertEqual(r['counts']['offers'],0)

    def test_domain_examples_keep_original_pending_and_bind_changed_content(self):
        for name in ('physics_astro','biology','economics_social','law'):
            path=PACKET/'agent_api/examples'/f'{name}.json'
            if not path.exists():
                # Filenames are fixture names, not dynamically supplied paths.
                self.fail(f'Missing expected fixture {name}')
            r=execute(policy(),json.loads(path.read_text()))
            by_id={item['command_id']:item for item in r['receipts']}
            self.assertEqual(by_id['observe-original']['currentness'],'reconsideration_pending')
            self.assertEqual(by_id['observe-renewed']['currentness'],'current_under_toy_policy')
            self.assertNotEqual(by_id['offer']['record']['target']['version'],
                                by_id['offer-updated']['record']['target']['version'])

    def test_new_dependency_changes_profile_without_fabricating_new_evidence(self):
        dep=offer('dependency',evidence={'reference':7})
        corrected=offer('corrected',claim_id='offer',dependencies=['dependency'])
        corrected['now']=2
        r=self.run_commands([dep,offer(),check(),corrected,rely(target='corrected')])
        by_id={item['command_id']:item for item in r['receipts']}
        self.assertEqual(by_id['corrected']['status'],'accepted_under_synthetic_policy')
        old=by_id['offer']['record']['target'];new=by_id['corrected']['record']['target']
        self.assertEqual(old['evidence_digest'],new['evidence_digest'])
        self.assertNotEqual(old['version'],new['version'])
        self.assertEqual(r['receipts'][-1]['status'],'refused')

    def test_changed_coverage_contract_has_distinct_profile_identity(self):
        old=self.run_commands([offer()])['receipts'][0]['record']['target']
        new=self.run_commands([offer(required_groups=2)])['receipts'][0]['record']['target']
        self.assertEqual(old['evidence_digest'],new['evidence_digest'])
        self.assertNotEqual(old['version'],new['version'])


if __name__=='__main__':unittest.main()
