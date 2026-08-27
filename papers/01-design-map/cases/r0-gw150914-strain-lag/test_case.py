#!/usr/bin/env python3
"""Conformance and adversarial tests for the GW150914 R0 strain-lag case."""

from __future__ import annotations

import copy
import json
import unittest

import run_case


class R0StrainLagTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source_manifest = json.loads(run_case.SOURCE_MANIFEST.read_text(encoding="utf-8"))
        cls.claim_manifest = json.loads(run_case.CLAIM_MANIFEST.read_text(encoding="utf-8"))
        cls.records = run_case.verify_source_registry(cls.source_manifest)
        cls.detectors = {record["detector"]: run_case.load_detector(record) for record in cls.records}
        cls.configuration = cls.claim_manifest["workflow_configuration"]

    def test_registered_input_digests(self) -> None:
        for record in self.records:
            self.assertEqual(run_case.sha256(run_case.RAW_DIR / record["filename"]), record["sha256"])

    def test_v2_identity_is_required(self) -> None:
        mutated = copy.deepcopy(self.source_manifest)
        mutated["event_version"] = "GW150914-v1"
        with self.assertRaisesRegex(run_case.CaseError, "non-v2"):
            run_case.verify_source_registry(mutated)

    def test_digest_mutation_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.source_manifest)
        mutated["sources"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(run_case.CaseError, "digest mismatch"):
            run_case.verify_source_registry(mutated)

    def test_quality_and_injection_policy(self) -> None:
        for detector in ("H1", "L1"):
            record = self.detectors[detector]
            for name in ("DATA", "CBC_CAT1", "CBC_CAT2", "BURST_CAT1", "BURST_CAT2"):
                self.assertTrue(record["event_dq_bits"][name])
            self.assertTrue(record["event_injection_bits"]["NO_CBC_HW_INJ"])
            self.assertTrue(record["event_injection_bits"]["NO_BURST_HW_INJ"])

    def test_observed_lag_satisfies_bound(self) -> None:
        result, _ = run_case.evaluate(self.detectors, self.configuration)
        self.assertTrue(result["invariants"]["absolute_lag_within_h1_l1_physical_bound"])
        self.assertLessEqual(result["absolute_lag_seconds"], 0.010)
        self.assertGreaterEqual(result["absolute_correlation"], 0.30)

    def test_25ms_shift_fails_physical_bound(self) -> None:
        result, _ = run_case.evaluate(self.detectors, self.configuration, negative_shift_seconds=0.025)
        self.assertFalse(result["invariants"]["absolute_lag_within_h1_l1_physical_bound"])

    def test_committed_evidence_clean_replay(self) -> None:
        run_case.verify_committed()

    def test_human_scientific_signoff_remains_pending(self) -> None:
        signoff = json.loads((run_case.ROOT / "review-signoff.json").read_text(encoding="utf-8"))
        self.assertEqual(signoff["human_scientific_review"]["status"], "pending")
        self.assertFalse(signoff["machine_checks"]["scientific_validity_proven"])


if __name__ == "__main__":
    unittest.main()
