"""Independent red regressions for repaired API boundaries; stdlib only."""
import copy
from dataclasses import replace
import unittest
from probes import toy_reliance, release_approved, BoundaryError, Rejected, PolicyAgent, fixture, Target


class AdversarialRuntimeTests(unittest.TestCase):
    def test_later_contradiction_cannot_leave_direct_reliance_current(self):
        p,t,o,c,r=toy_reliance()
        PolicyAgent('reviewer-b','contradiction').act(p,o,{'numerics'},now=2)
        self.assertNotEqual(p.currentness(r,3,3,1),'current_under_toy_policy')

    def test_expired_currentness_query_cannot_be_rolled_back(self):
        p,t,o,c,r=toy_reliance()
        self.assertEqual(p.currentness(r,10,10,1),'expired')
        with self.assertRaises(Rejected):p.currentness(r,2,2,1)

    def test_publication_invalid_calls_leave_runtime_state_unchanged(self):
        # Direct deepcopy only for observation; all changes use public APIs.
        callbacks=[lambda m,c,d:m.publish(c,d,'bad',100000),
          lambda m,c,d:m.verify(c,d,'bad',{k:True for k in m.required_checks},2,15),
          lambda m,c,d:m.verify(c,d,'verifier',{},2,15),
          lambda m,c,d:m.publish(c,d,'publisher',2,'unknown'),
          lambda m,c,d:m.observe(c,'bad',2),
          lambda m,c,d:m.amend(c,replace(c,release_id='other'),2)]
        for call in callbacks:
            with self.subTest(call=call):
                m,c,d=release_approved(); before=copy.deepcopy(m.__dict__)
                with self.assertRaises(BoundaryError):call(m,c,d)
                self.assertEqual(m.__dict__,before)

    def test_observer_checks_metadata_even_with_identical_content(self):
        for changes in [dict(source_revision='wrong'),dict(evidence_digest='wrong'),
                        dict(policy_version='wrong'),dict(content_class='wrong'),
                        dict(destination='wrong')]:
            with self.subTest(changes=changes):
                m,c,d=release_approved();m.publish(c,d,'publisher',2)
                other=replace(c,**changes)
                self.assertEqual(m.observe(other,'observer',3)['status'],'binding_mismatch')
                self.assertEqual(m.currentness(other,d,4),'release_binding_mismatch')

    def test_amendment_must_preserve_intended_successor_binding(self):
        m,a,d=release_approved();m.publish(a,d,'publisher',2)
        b=replace(a,release_id='new',content=b'new')
        m.amend(a,b,3)
        wrong=replace(b,evidence_digest='different')
        with self.assertRaises(BoundaryError):m.verify(wrong,d,'verifier',{k:True for k in m.required_checks},4,15)
        m.verify(b,d,'verifier',{k:True for k in m.required_checks},4,15)
        self.assertEqual(m.publish(b,d,'publisher',5),'delivered_unobserved')
        with self.assertRaises(BoundaryError):m.amend(b,a,6)
        with self.assertRaises(BoundaryError):m.amend(a,replace(b,release_id='third'),6)

    def test_declared_offer_floor_cannot_be_weakened(self):
        p=fixture();o=p.offer(Target('strict','v','fixture:e'),'author',{'numerics'},required_groups=2)
        c=PolicyAgent('reviewer-a').act(p,o,{'numerics'})
        with self.assertRaises(Rejected):p.rely(o,'scientist',[c],'use',{'numerics'},'scientific',10,required_groups=1)
        c2=PolicyAgent('reviewer-b').act(p,o,{'numerics'})
        r=p.rely(o,'scientist',[c,c2],'use',{'numerics'},'scientific',10)
        self.assertEqual(p.reliances[r].required_groups,2)

    def test_already_delivered_correction_can_be_observed_after_revocation(self):
        m,c,d=release_approved();m.publish(c,d,'publisher',2)
        m.revoke(d.delegation_id,3)
        self.assertEqual(m.observe(c,'observer',4)['status'],'matches')
        self.assertEqual(m.currentness(c,d,5),'authorization_revoked')

if __name__=='__main__':unittest.main()
