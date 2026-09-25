"""Additional state-sequence challenges, beyond initial mutation regressions."""
from dataclasses import replace
import unittest
from probes import release_approved, BoundaryError

class PublicationSequenceTests(unittest.TestCase):
    def test_observed_missing_stays_historical_until_new_observation(self):
        m,c,d=release_approved()
        self.assertEqual(m.observe(c,'observer',2)['status'],'missing')
        m.publish(c,d,'publisher',3)
        self.assertEqual(m.currentness(c,d,4),'last_observation_missing')
        self.assertEqual(m.observe(c,'observer',5)['status'],'matches')
        self.assertEqual(m.currentness(c,d,6),'last_observation_matches')

    def test_expired_authority_cannot_be_revived_by_matching_observation(self):
        m,c,d=release_approved();m.publish(c,d,'publisher',2)
        self.assertEqual(m.observe(c,'observer',16)['status'],'matches')
        self.assertEqual(m.currentness(c,d,16),'decision_unavailable')
        with self.assertRaises(BoundaryError):m.publish(c,d,'publisher',16)

    def test_unpublished_wrong_metadata_does_not_poison_correct_receipt(self):
        m,c,d=release_approved();m.publish(c,d,'publisher',2)
        m.observe(c,'observer',3)
        wrong=replace(c,evidence_digest='other')
        self.assertEqual(m.observe(wrong,'observer',4)['status'],'binding_mismatch')
        self.assertEqual(m.currentness(wrong,d,5),'release_binding_mismatch')
        self.assertEqual(m.currentness(c,d,5),'last_observation_matches')

    def test_tampered_delivery_requires_new_release_and_new_decision(self):
        m,c,d=release_approved();m.publish(c,d,'publisher',2,'tamper')
        self.assertEqual(m.observe(c,'observer',3)['status'],'mismatch')
        self.assertEqual(m.publish(c,d,'publisher',4),'already_delivered')
        self.assertEqual(m.observe(c,'observer',5)['status'],'mismatch')
        new=replace(c,release_id='corrected')
        m.amend(c,new,6)
        with self.assertRaises(BoundaryError):m.publish(new,d,'publisher',7)
        m.verify(new,d,'verifier',{k:True for k in m.required_checks},7,15)
        m.publish(new,d,'publisher',8)
        self.assertEqual(m.observe(new,'observer',9)['status'],'matches')
        self.assertEqual(m.currentness(c,d,9),'superseded')

if __name__=='__main__':unittest.main()
