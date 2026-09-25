"""Check lineage guards using harmless mini-packets and a stub renderer/runner.

These test integrity plumbing; they do not claim scientific validation of fixtures.
"""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import shutil
import tempfile
from types import SimpleNamespace
import unittest
from export_probes import module,PACKET


def source_tree(root):
    for rel,body in {
        'toy_agents/results/demo.json':'{"scenarios":{"release_cycle":{}}}',
        'toy_agents/protocol.py':'# harmless source fixture\n',
        'surfaces/portal.html.in':'<p>Fixture __TRACE_JSON__</p>',
        'surfaces/site.css':'body {color:black}',
        'domains/fixtures/scenarios.json':'{}',
        'reviews/red-math/original_completion.json':'{"counts":{}}',
        'domains/fixtures/oracle-results.json':'{}',
        'domains/fixtures/replay-results.json':'{}',
        'adapters/fixtures/evidence.txt':'public evidence fixture',
        'adapters/fixtures/input.json':'{}',
        'models/results/value.json':'{"value":1}',
        'results/figures/chart.svg':'<svg xmlns="http://www.w3.org/2000/svg"></svg>',
    }.items():
        p=root/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body)
    for rel in ('publication/blog-introduction.md','domains/README.md','reviews/COLLECTIVE.md','publication/release-assessment.md'):
        p=root/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('# Fixture\nPublic text.\n')


class EvidenceBindingTests(unittest.TestCase):
    def altered_artifact(self,name):
        builder=module(PACKET/'surfaces/build.py','evidence_builder')
        verifier=module(PACKET/'surfaces/verify_export.py','evidence_verifier')
        builder.subprocess=SimpleNamespace(run=lambda *a,**k:SimpleNamespace(stdout='<p>Fixture</p>',stderr=''))
        with tempfile.TemporaryDirectory(prefix='mcrp-evidence-red-') as tmp:
            root=Path(tmp)/'source';source_tree(root);builder.ROOT=root
            original=hashlib.sha256((root/name).read_bytes()).hexdigest()
            (root/'results/validation.json').write_text(json.dumps({'passed':True,'source_sha256':{},'table_sha256':{},'check_groups':[],
                'evidence_sha256':{name:original},'inputs_changed_during_run':[]}))
            clean=Path(tmp)/'before';builder.build(clean)
            self.assertTrue(verifier.verify(clean)['passed'])
            (root/name).write_text((root/name).read_text()+'\n ')
            changed=Path(tmp)/'after';builder.build(changed)
            result=verifier.verify(changed)
            self.assertFalse(result['passed'])
            self.assertIn('validation evidence hash mismatch: '+name,result['errors'])

    def test_changed_result_json_rebuild_does_not_inherit_pass(self):
        self.altered_artifact('models/results/value.json')

    def test_changed_figure_rebuild_does_not_inherit_pass(self):
        self.altered_artifact('results/figures/chart.svg')

    def mutation_during_runner(self,name):
        with tempfile.TemporaryDirectory(prefix='mcrp-input-red-') as tmp:
            root=Path(tmp);source_tree(root)
            shutil.copyfile(PACKET/'run_checks.py',root/'run_checks.py')
            runner=module(root/'run_checks.py','fixture_runner')
            calls=[]
            def fake_run(*args,**kwargs):
                if not calls:(root/name).write_text((root/name).read_text()+'\n')
                calls.append(args)
                return SimpleNamespace(stdout='{}',stderr='',returncode=0)
            runner.subprocess=SimpleNamespace(run=fake_run)
            with contextlib.redirect_stdout(io.StringIO()):result=runner.main()
            manifest=json.loads((root/'results/validation.json').read_text())
            self.assertEqual(result,1)
            self.assertFalse(manifest['passed'])
            self.assertIn(name,manifest['inputs_changed_during_run'])

    def test_source_changed_during_commands_fails_validation(self):
        self.mutation_during_runner('toy_agents/protocol.py')

    def test_fixture_changed_during_commands_fails_validation(self):
        self.mutation_during_runner('adapters/fixtures/input.json')

    def test_historical_probe_fixture_changed_during_commands_fails_validation(self):
        self.mutation_during_runner('reviews/red-math/original_completion.json')

    def test_evidence_text_is_in_frozen_input_inventory(self):
        runner=module(PACKET/'run_checks.py','inventory_runner')
        with tempfile.TemporaryDirectory(prefix='mcrp-input-red-') as tmp:
            root=Path(tmp);source_tree(root)
            self.assertIn('adapters/fixtures/evidence.txt',runner.source_input_inventory(root))

if __name__=='__main__':unittest.main()
