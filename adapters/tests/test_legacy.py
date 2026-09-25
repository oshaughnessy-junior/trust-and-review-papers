import copy
import hashlib
import json
from pathlib import Path
import unittest
from adapters.legacy import adapt,roundtrip,execute_fixture,AdapterError
from toy_agents.protocol import Rejected

ROOT=Path(__file__).resolve().parents[1]

class LegacyTests(unittest.TestCase):
    def setUp(self):
        self.source=json.loads((ROOT/'fixtures/review-issue.json').read_text())
        self.enrich=json.loads((ROOT/'fixtures/trusted-enrichment.json').read_text())
    def test_roundtrip_preserves_unknown_extension_and_values(self):
        original=copy.deepcopy(self.source);envelope=adapt(self.source)
        self.source['author']['display_name']='mutated caller value'
        self.assertEqual(roundtrip(envelope),original)
        self.assertIn('extension:editorial_note',roundtrip(envelope))
    def test_absent_empty_null_distinguished(self):
        statuses=[]
        for present,value in [(False,None),(True,None),(True,[]),(True,{'x':'y'})]:
            s=copy.deepcopy(self.source)
            if present:s['dependencies']=value
            statuses.append(adapt(s)['mapped']['dependencies']['status'])
        self.assertEqual(statuses,['absent','null','explicit_empty','value'])
    def test_names_urls_teams_recommendation_never_grant_authority(self):
        s=copy.deepcopy(self.source);s['author']['display_name']='Independent Authorized Scientific Editor';s['review']['recommendation']='approve';s['author']['team_members']*=20
        e=adapt(s)
        self.assertEqual(e['protocol_assertions'],{'authorization':'unknown','independence':'unknown','dependency_completeness':'unknown'})
        with self.assertRaises(AdapterError):execute_fixture(e)
    def test_projection_tampering_rejected(self):
        e=adapt(self.source);e['mapped']['check_scope']['value']=['clinical-use']
        with self.assertRaises(AdapterError):roundtrip(e)
    def test_boolean_integer_projection_bypass_rejected(self):
        self.source['claim']['immutable_refs']=1
        e=adapt(self.source)
        with self.assertRaises(AdapterError):execute_fixture(e,self.enrich)
        e['mapped']['immutable_refs']['value']=True
        with self.assertRaises(AdapterError):roundtrip(e)
        with self.assertRaises(AdapterError):execute_fixture(e,self.enrich)
    def test_nested_numeric_token_types_are_distinct(self):
        # Strict canonical-token policy: 1 and 1.0 are distinct metadata values.
        self.source['review']['limits']={'nested':[1,{'x':False}]}
        e=adapt(self.source)
        e['mapped']['check_limits']['value']['nested'][0]=1.0
        with self.assertRaises(AdapterError):roundtrip(e)
        e=adapt(self.source)
        e['mapped']['check_limits']['value']['nested'][1]['x']=0
        with self.assertRaises(AdapterError):roundtrip(e)
    def test_envelope_nonfinite_injection_rejected(self):
        e=adapt(self.source);e['extra']=float('nan')
        with self.assertRaises(AdapterError):roundtrip(e)
    def test_source_tampering_rejected(self):
        e=adapt(self.source);e['source']['review']['result']='unknown'
        with self.assertRaises(AdapterError):roundtrip(e)
    def test_successful_cycle_retains_loss_and_enrichment(self):
        e=adapt(self.source);r=execute_fixture(e,self.enrich)
        self.assertEqual(r['adapter_envelope']['loss_report'],e['loss_report'])
        self.assertEqual(r['trusted_fixture_enrichment'],self.enrich)
        self.assertEqual(r['before_amendment'],'current_under_toy_policy')
        self.assertEqual(r['after_amendment'],'reconsideration_pending')
    def test_contradiction_cannot_be_overridden_by_accept(self):
        self.source['review']['result']='contradiction'
        e=adapt(self.source)
        self.assertTrue(any('tension' in x['effect'] for x in e['loss_report']['items']))
        with self.assertRaises(Rejected):execute_fixture(e,self.enrich)
    def test_missing_result_is_not_accept(self):
        del self.source['review']['result']
        with self.assertRaises(AdapterError):execute_fixture(adapt(self.source),self.enrich)
    def test_nonempty_dependency_not_silently_dropped(self):
        self.source['dependencies']=[{'id':'calibration','version_ref':'missing'}]
        with self.assertRaises(AdapterError):execute_fixture(adapt(self.source),self.enrich)
    def test_source_authority_or_control_not_overwritten(self):
        for field,value in [('control_groups',{'author':'same','reviewer':'same'}),('authorizations',{'scientific':'denied'})]:
            s=copy.deepcopy(self.source);s[field]=value
            with self.subTest(field=field),self.assertRaises(AdapterError):execute_fixture(adapt(s),self.enrich)
    def test_scope_cannot_be_widened_by_enrichment(self):
        self.enrich['scope'].append('clinical-use')
        with self.assertRaises(AdapterError):execute_fixture(adapt(self.source),self.enrich)
    def test_control_conflict_and_missing_typed_authority_rejected(self):
        for field,value in [('reviewer_group',self.enrich['author_group']),('decision_roles',['publication'])]:
            e=copy.deepcopy(self.enrich);e[field]=value
            with self.subTest(field=field),self.assertRaises(Rejected):execute_fixture(adapt(self.source),e)
    def test_mutable_url_is_not_exact_version(self):
        self.source['claim']['version_ref']='https://example.invalid/main'
        with self.assertRaises(AdapterError):execute_fixture(adapt(self.source),self.enrich)
    def test_fabricated_evidence_digest_only_format_not_verification(self):
        # The adapter deliberately does not claim to validate artifact bytes.
        self.source['claim']['evidence_ref']='sha256:'+'a'*64
        result=execute_fixture(adapt(self.source),self.enrich)
        self.assertEqual(result['adapter_envelope']['source']['claim']['evidence_ref'],'sha256:'+'a'*64)
    def test_fixture_evidence_hash_matches_actual_synthetic_file(self):
        self.assertEqual(self.source['claim']['evidence_ref'],'sha256:'+hashlib.sha256((ROOT/'fixtures/evidence.txt').read_bytes()).hexdigest())
    def test_nonjson_or_nonfinite_input_rejected(self):
        for x in [{'x':float('nan')},{'x':{1,2}},{1:'nonstring-key'}]:
            with self.assertRaises(AdapterError):adapt(x)

if __name__=='__main__':unittest.main()
