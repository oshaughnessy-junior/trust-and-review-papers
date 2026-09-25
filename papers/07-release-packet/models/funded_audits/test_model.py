from dataclasses import replace
from fractions import Fraction
from itertools import combinations
import unittest
from model import Config,ResourceLedger,run,plan,utilities,best_response,exact_selection_marginals


class FundedTests(unittest.TestCase):
    def test_exact_quota_marginals(self):
        self.assertEqual(exact_selection_marginals(8,4),[Fraction(1,2)]*8)
        self.assertEqual(exact_selection_marginals(8,1),[Fraction(1,8)]*8)

    def test_concealed_funding_delivers_selected_audits(self):
        for seed in range(30):
            r=run(seed=seed);c=r['counts']
            self.assertEqual(c['honest'],8);self.assertEqual(c['audited'],4)
            self.assertEqual(r['tokens']['audit_spent'],4)
            self.assertEqual(r['aggregate_expected_utility_regret_under_actual_information'],0)
            self.assertEqual(sum(a['audited'] for a in r['actors']),4)
            self.assertTrue(all(a['closing_escrow']>=0 for a in r['actors']))

    def test_all_actions_commit_before_audit_disclosure(self):
        r=run(seed=10)
        self.assertEqual([e['event'] for e in r['events'][:8]],['decision_commit']*8)
        self.assertFalse(any(e['event']=='decision_commit' for e in r['events'][8:]))
        self.assertTrue(all(e['decision_q']==.5 and not e['selection_disclosed'] for e in r['events'][:8]))

    def test_refusal_does_not_redistribute_slots(self):
        r=run(seed=17,outside_options=[10]*8)
        self.assertEqual(r['counts']['refused'],8)
        self.assertEqual(r['counts']['selected_audit_slots'],4)
        self.assertEqual(r['counts']['unused_refused_audit_slots'],4)
        self.assertEqual(r['counts']['audited'],0)
        self.assertEqual(r['tokens']['audit_spent'],0)

    def test_partial_refusal_preserves_marginal_without_reallocation(self):
        subsets=list(combinations(range(8),4));participants=set(range(4,8))
        expected=Fraction(sum(len(set(s)&participants) for s in subsets),len(subsets))
        self.assertEqual(expected,2)
        for seed in range(20):
            r=run(seed=seed,outside_options=[1]*4+[.1]*4)
            self.assertEqual(r['counts']['refused'],4)
            self.assertEqual(r['counts']['completed'],4)
            self.assertEqual(r['counts']['audited']+r['counts']['unused_refused_audit_slots'],4)
            self.assertFalse(any(a['audited'] for a in r['actors'] if a['action']=='refuse'))

    def test_broken_promise_changes_best_response(self):
        broken=run(Config(delivered_quota=1,allow_broken_promise=True))
        repaired=run(Config(promised_quota=1,delivered_quota=1))
        self.assertEqual(broken['counts']['honest'],8)
        self.assertEqual(repaired['counts']['shallow'],8)
        self.assertGreater(broken['aggregate_expected_utility_regret_under_actual_information'],0)
        self.assertEqual(repaired['aggregate_expected_utility_regret_under_actual_information'],0)
        self.assertEqual(run(Config(delivered_quota=1))['status'],'unavailable_before_offering')

    def test_disclosure_changes_information_and_action(self):
        r=run(Config(disclose_selection=True))
        self.assertEqual(r['counts']['honest'],4);self.assertEqual(r['counts']['shallow'],4)
        self.assertTrue(all(a['action']=='shallow' for a in r['actors'] if not a['audit_slot_selected']))

    def test_false_positives_can_induce_refusal(self):
        r=run(Config(false_positive=.3))
        self.assertEqual(r['counts']['refused'],8)
        self.assertEqual(r['counts']['audited'],0)

    def test_shared_roles_reserve_worst_case_and_never_self_audit(self):
        cfg=Config(role_mode='shared_cross')
        for seed in range(20):
            r=run(cfg,seed)
            self.assertTrue(all(a['review_person']!=a['audit_person'] for a in r['actors']))
            for row in r['person_ledger']:
                self.assertEqual(row['reserved_hours'],6)
                self.assertLessEqual(row['spent_hours'],6)
                self.assertEqual(row['lanes']['review'],4)
        bad=run(Config(role_mode='shared_cross',shared_person_capacity=5))
        self.assertEqual(bad['status'],'unavailable_before_offering')
        self.assertEqual(bad['counts']['offered'],0)
        self.assertIn('capacity',bad['reason'])

    def test_independent_capacity_funding_and_collateral_gates(self):
        for cfg in (Config(role_mode='self_audit'),Config(audit_token_budget=3),
                    Config(reward_token_budget=4),Config(actor_escrow=1),Config(audit_capacity=1)):
            self.assertEqual(run(cfg)['status'],'unavailable_before_offering')

    def test_atomic_failure_and_overdraw(self):
        ledger=ResourceLedger({'A':1,'B':0})
        self.assertFalse(ledger.reserve_program({'A':1,'B':1}))
        self.assertEqual(ledger.reserved,{'A':0.,'B':0.})
        self.assertTrue(ledger.reserve_program({'A':1}))
        ledger.spend('A',1,'review')
        with self.assertRaises(ValueError):ledger.spend('A',.1,'audit')

    def test_utility_exact_finite_best_response_condition(self):
        cfg=Config();c=Fraction(3,10);R=Fraction(3,5);F=2;alpha=Fraction(1,50);beta=Fraction(4,5);outside=Fraction(1,10)
        for k in range(9):
            q=Fraction(k,8)
            u={'honest':R-c-q*alpha*F,'shallow':R-q*beta*F,'refuse':outside}
            exact=max(('refuse','honest','shallow'),key=lambda a:u[a])
            self.assertEqual(best_response(utilities(cfg,.3,.1,float(q))),exact)

    def test_actual_penalty_transfer_conserves_collateral(self):
        cfg=Config(reward=3,reward_token_budget=24,false_positive=1,detection=1)
        result=run(cfg,4,efforts=[0]*8)
        self.assertEqual(result['counts']['honest'],8)
        self.assertEqual(result['counts']['false_sanctions'],4)
        self.assertEqual(result['tokens']['penalties_quarantined'],8)
        self.assertEqual(result['tokens']['escrow_closing_total']+result['tokens']['penalties_quarantined'],result['tokens']['escrow_opening_total'])
        self.assertEqual(result['tokens']['reward_spent'],24)
        self.assertFalse(result['tokens']['penalties_recycled_into_budget'])

    def test_no_epsilon_capacity_can_fund_positive_work(self):
        ledger=ResourceLedger({'A':0})
        self.assertTrue(ledger.reserve_program({'A':0}))
        with self.assertRaises(ValueError):ledger.spend('A',1e-12,'audit')
        self.assertEqual(ledger.used['A'],0)
        config=Config(review_hours=1e-13,audit_hours=1e-13,review_capacity=0,audit_capacity=0)
        self.assertEqual(run(config)['status'],'unavailable_before_offering')

    def test_decimal_debits_exactly_fill_without_tolerance(self):
        ledger=ResourceLedger({'A':.3})
        self.assertTrue(ledger.reserve_program({'A':.3}))
        ledger.spend('A',.1,'review');ledger.spend('A',.2,'audit')
        self.assertEqual(ledger.used['A'],Fraction(3,10))
        with self.assertRaises(ValueError):ledger.spend('A',1e-30,'audit')

    def test_exact_honest_shallow_tie_uses_stated_preference(self):
        cfg=Config(promised_quota=1,delivered_quota=1,false_positive=.1,detection=.3)
        values=utilities(cfg,.05,0,.125)
        self.assertEqual(values['honest'],Fraction(21,40))
        self.assertEqual(values['honest'],values['shallow'])
        result=run(cfg,1,efforts=[.05]*8,outside_options=[0]*8)
        self.assertEqual(result['counts']['honest'],8)

    def test_exact_honest_refusal_tie_prefers_refusal(self):
        cfg=Config(promised_quota=8,delivered_quota=8,reward=.4,reward_token_budget=3.2,
                   audit_token_budget=8,audit_capacity=4,false_positive=0,detection=1)
        values=utilities(cfg,.1,.3,1)
        self.assertEqual(values['honest'],Fraction(3,10))
        self.assertEqual(values['honest'],values['refuse'])
        self.assertEqual(run(cfg,1,efforts=[.1]*8,outside_options=[.3]*8)['counts']['refused'],8)

    def test_invalid_configuration(self):
        for kwargs in ({'offered_population':True},{'promised_quota':9},{'audit_token_cost':0},{'false_positive':2}):
            with self.assertRaises(ValueError):Config(**kwargs)
        with self.assertRaises(ValueError):run(efforts=[.3])


if __name__=='__main__':unittest.main()
