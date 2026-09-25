import unittest
from dataclasses import replace

from release_cycle import BoundaryError, fixture, run_demo


class ReleaseBoundaryTests(unittest.TestCase):
    def approved(self):
        m, c, d = fixture()
        m.verify(c, d, "verifier", {k: True for k in m.required_checks}, 1, 15)
        return m, c, d

    def test_bound_component_mutations_need_new_decision(self):
        # Independent enumerated contract: each of the seven bound components.
        changes = [dict(release_id="other"), dict(source_revision="other"),
                   dict(content=b"other"), dict(evidence_digest="other"),
                   dict(policy_version="other"), dict(content_class="other"),
                   dict(destination="staging://other")]
        for change in changes:
            with self.subTest(change=change):
                m, c, d = self.approved()
                with self.assertRaises(BoundaryError):
                    m.publish(replace(c, **change), d, "publisher", 2)
                self.assertEqual(m.deliveries, {})

    def test_delegation_expansion_does_not_inherit_decision(self):
        m, c, d = self.approved()
        with self.assertRaises(BoundaryError):
            m.publish(c, replace(d, expires=30), "publisher", 2)
        self.assertEqual(m.deliveries, {})

    def test_checks_require_literal_success_and_full_coverage(self):
        for value in (None, False, "passed", 1):
            m, c, d = fixture()
            checks = {k: True for k in m.required_checks}
            checks["artifact_tests"] = value
            with self.assertRaises(BoundaryError):
                m.verify(c, d, "verifier", checks, 1, 15)
        m, c, d = fixture()
        with self.assertRaises(BoundaryError):
            m.verify(c, d, "verifier", {}, 1, 15)

    def test_author_cannot_approve_and_verifier_cannot_publish(self):
        m, c, d = fixture()
        with self.assertRaises(BoundaryError):
            m.verify(c, d, "author", {k: True for k in m.required_checks}, 1, 15)
        m, c, d = self.approved()
        with self.assertRaises(BoundaryError):
            m.publish(c, d, "verifier", 2)

    def test_revocation_and_expiry_checked_immediately_before_publish(self):
        m, c, d = self.approved()
        m.revoke(d.delegation_id, 2)
        with self.assertRaises(BoundaryError):
            m.publish(c, d, "publisher", 3)
        m, c, d = self.approved()
        with self.assertRaises(BoundaryError):
            m.publish(c, d, "publisher", 15)
        m, c, d = self.approved()
        with self.assertRaises(BoundaryError):
            m.publish(c, d, "publisher", 20)

    def test_clock_cannot_roll_back_to_restore_authority(self):
        m, c, d = self.approved()
        self.assertEqual(m.currentness(c, d, 16), "decision_unavailable")
        with self.assertRaises(BoundaryError):
            m.publish(c, d, "publisher", 2)

    def test_transport_success_is_not_observation_and_tamper_is_visible(self):
        m, c, d = self.approved()
        self.assertEqual(m.publish(c, d, "publisher", 2, "tamper"), "delivered_unobserved")
        self.assertEqual(m.currentness(c, d, 3), "unobserved")
        self.assertEqual(m.observe(c, "observer", 4)["status"], "mismatch")
        self.assertEqual(m.currentness(c, d, 5), "last_observation_mismatch")

    def test_retry_idempotence_and_amendment_trace(self):
        r = run_demo()
        self.assertEqual(r["failed_attempt"], "delivery_failed")
        self.assertEqual(r["missing_observation"], "missing")
        self.assertEqual(r["duplicate_attempt"], "already_delivered")
        deliveries = [e for e in r["events"] if e["type"] == "delivered_unobserved"]
        self.assertEqual([e["release_id"] for e in deliveries], ["release-1", "release-2"])
        self.assertEqual(r["old_after_amendment"], "superseded")
        self.assertEqual(r["new_after_revocation"], "authorization_revoked")

    def test_observation_is_historical_even_after_approval_expires(self):
        m, c, d = self.approved()
        m.publish(c, d, "publisher", 2)
        receipt = m.observe(c, "observer", 3)
        self.assertEqual(receipt["status"], "matches")
        self.assertEqual(m.currentness(c, d, 15), "decision_unavailable")
        self.assertEqual(receipt["status"], "matches")


if __name__ == "__main__":
    unittest.main()
