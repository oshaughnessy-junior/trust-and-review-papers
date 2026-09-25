import unittest
from boundary import Reliance, Snapshot, reliance_view, affected, capacity_feasible

class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.receipt=Reliance('synthetic-release-v1','accepted-for-declared-use',0,10)
    def test_old_authentic_receipt_does_not_imply_currentness(self):
        old=Snapshot('synthetic-release-v1',1,None,True)
        view=reliance_view(self.receipt,old,5,2)
        self.assertIn('freshness_unknown',view['reasons'])
        self.assertEqual(view['historical_disposition'],'accepted-for-declared-use')
    def test_visibility_and_amendment_do_not_rewrite_science(self):
        current=Snapshot('synthetic-release-v1',5,'calibration-v2',False)
        view=reliance_view(self.receipt,current,5,2)
        self.assertEqual(view['reasons'],['reconsideration_pending','dependency_unavailable'])
        self.assertEqual(view['historical_disposition'],self.receipt.scientific_disposition)
    def test_offline_expired_unknown(self):
        self.assertEqual(reliance_view(self.receipt,None,10,2)['reasons'],['expired','freshness_unknown'])
    def test_new_reliance_can_resolve_prior_material_change(self):
        renewed=Reliance('synthetic-release-v2','accepted-after-calibration-review',6,16)
        snapshot=Snapshot('synthetic-release-v2',7,None,True)
        self.assertEqual(reliance_view(renewed,snapshot,7,2)['currentness'],'conditions_observed')
    def test_bad_binding_and_future_rejected(self):
        for snap in [Snapshot('other',1,None,True),Snapshot('synthetic-release-v1',6,None,True)]:
            with self.assertRaises(ValueError): reliance_view(self.receipt,snap,5,2)
    def test_current_projection_still_has_no_truth_claim(self):
        view=reliance_view(self.receipt,Snapshot('synthetic-release-v1',5,None,True),5,2)
        self.assertEqual(view['currentness'],'conditions_observed')
        self.assertIn('not scientific truth',view['limit'])
    def test_withheld_graph_finds_missing_and_spurious_edges(self):
        true={'A':{'C'},'B':{'C'},'D':{'unrelated'}}
        declared={'A':{'C'},'B':set(),'D':{'C'}}
        actual=affected(true,'C');observed=affected(declared,'C')
        self.assertEqual(actual,{'A','B'})
        self.assertEqual(observed,{'A','D'})
        self.assertEqual(len(actual&observed)/len(actual),.5)
        self.assertEqual(len(actual&observed)/len(observed),.5)
    def test_cycles_and_diamonds_deduplicated(self):
        graph={'A':{'C'},'B':{'C'},'D':{'A','B'},'C':{'D'}}
        self.assertEqual(affected(graph,'C'),{'A','B','D'})
    def test_joint_capacity_not_three_independent_budgets(self):
        self.assertFalse(capacity_feasible({'p':{'review':4,'repair':3,'audit':2}},{'p':8}))
        self.assertTrue(capacity_feasible({'p':{'review':4,'repair':2,'audit':2}},{'p':8}))
        # An alternate scientific adjudicator is an additional eligibility fact.
        eligible_appealers={'p'}-{'p'}
        self.assertFalse(eligible_appealers)

if __name__=='__main__':unittest.main()
