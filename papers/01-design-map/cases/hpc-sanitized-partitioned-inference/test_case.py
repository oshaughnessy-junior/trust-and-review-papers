#!/usr/bin/env python3
import copy
import hashlib
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import run_case


class SanitizedHPCDownselectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claim = run_case.read_json(run_case.ROOT / "claim-manifest.json")
        cls.sources = run_case.read_json(run_case.ROOT / "source-manifest.json")
        cls.partitions = run_case.load_partitions(cls.sources, cls.claim["configuration"])

    def test_registered_source_identities(self):
        self.assertEqual(len(self.partitions), 4)

    def test_digest_algorithm_is_recomputed(self):
        digests = run_case.partition_digests(self.partitions, self.sources)
        self.assertEqual([item["argmax_theta"] for item in digests], [2, 2, 2, 2])

    def test_registered_aggregate_invariants(self):
        result = run_case.evaluate(self.partitions, self.claim["configuration"])
        self.assertTrue(result["passed"])

    def test_adversarial_tail_corruption_fails(self):
        mutated = copy.deepcopy(self.partitions)
        mutated[0]["log_likelihood"][4] = 50.0
        result = run_case.evaluate(mutated, self.claim["configuration"])
        self.assertFalse(result["passed"])
        self.assertFalse(result["invariants"]["map_theta_matches_registered"])

    def test_missing_partition_is_rejected(self):
        mutated = copy.deepcopy(self.sources)
        mutated["sources"].pop()
        with self.assertRaisesRegex(run_case.CaseError, "partition count"):
            run_case.load_partitions(mutated, self.claim["configuration"])

    def test_six_assessment_modes_remain_non_equivalent(self):
        modes = run_case.read_json(run_case.ROOT / "assessment-modes.json")["modes"]
        self.assertEqual(len(modes), 6)
        self.assertEqual(sum(item["status"].startswith("performed") for item in modes), 3)
        self.assertEqual(next(item for item in modes if item["id"] == "full-independent-execution")["status"], "not-performed")

    def test_ten_resource_axes_are_exact(self):
        resources = run_case.read_json(run_case.ROOT / "resource-declaration.json")["axes"]
        self.assertEqual(set(resources), {"compute","storage","access","platform","wall_clock","human_expertise","agent_capability","operator_support","monetary_allocative_cost","freshness"})

    def test_attestation_is_template_not_evidence(self):
        attestation = run_case.read_json(run_case.ROOT / "restricted-attestation-template.json")
        self.assertEqual(attestation["status"], "TEMPLATE_ONLY_NOT_AN_ATTESTATION")

    def test_committed_evidence_clean_replay(self):
        run_case.verify()

    def test_coherent_failed_artifacts_are_rejected_by_standalone_replay(self):
        with tempfile.TemporaryDirectory() as directory:
            copied = Path(directory) / "case"
            shutil.copytree(run_case.ROOT, copied, ignore=shutil.ignore_patterns("__pycache__"))
            source_path = copied / "data/sampled-partitions/partition-000.json"
            source = json.loads(source_path.read_text())
            source["log_likelihood"][4] = 50.0
            source_path.write_text(json.dumps(source, separators=(",", ":")) + "\n")
            digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
            manifest_path = copied / "source-manifest.json"
            manifest = json.loads(manifest_path.read_text())
            manifest["sources"][0]["sha256"] = digest
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
            recorded = subprocess.run(
                ["python3", "run_case.py", "--record"], cwd=copied,
                text=True, capture_output=True, check=False,
            )
            replayed = subprocess.run(
                ["python3", "run_case.py", "--verify"], cwd=copied,
                text=True, capture_output=True, check=False,
            )
            self.assertNotEqual(recorded.returncode, 0)
            self.assertNotEqual(replayed.returncode, 0)
            self.assertIn("registered sanitized invariant failed during replay", replayed.stderr)

    def test_packet_index_is_complete_and_unique(self):
        index = run_case.read_json(run_case.ROOT / "packet-index.json")
        paths = [entry["path"] for entry in index["entries"]]
        actual = {
            str(path.relative_to(run_case.ROOT))
            for path in run_case.ROOT.rglob("*")
            if path.is_file()
            and path.name != "packet-index.json"
            and "__pycache__" not in path.parts
        }
        self.assertEqual(len(paths), len(set(paths)))
        self.assertEqual(set(paths), actual)


if __name__ == "__main__":
    unittest.main()
