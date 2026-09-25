import random
import copy
import unittest
from toy_agents.protocol import Actor, Target, Ledger, Protocol, PolicyAgent, Rejected, sample_panel
from toy_agents.scenarios import fixture, release_cycle, hidden_dependency

class ResourceTests(unittest.TestCase):
    def test_atomic_reservation_no_double_spend(self):
        l=Ledger({'a':4,'b':1},{('a','x'):4,('a','y'):4,('b','x'):1})
        with self.assertRaises(Rejected): l.reserve('panel',[('a','x',2),('b','x',2)])
        self.assertEqual(l.totals(),({},{}))
        l.reserve('check',[('a','x',3)])
        with self.assertRaises(Rejected): l.reserve('appeal',[('a','y',2)])
        l.consume('check')
        with self.assertRaises(Rejected): l.cancel('check')
        with self.assertRaises(Rejected): l.consume('check')

    def test_invalid_effort(self):
        for value in [True,-1,1.5,float('nan'),float('inf')]:
            with self.subTest(value=value),self.assertRaises(Rejected): Ledger({'a':value},{('a','x'):1})

    def test_reservations_independent_sum_oracle(self):
        rng=random.Random(83)
        l=Ledger({'a':7,'b':5},{('a','x'):4,('a','y'):6,('b','x'):5})
        accepted=[]
        for i in range(100):
            entries=[rng.choice([('a','x',1),('a','y',2),('b','x',2)]) for _ in range(rng.randrange(1,4))]
            candidate=accepted+entries
            expected=all(sum(n for a,s,n in candidate if a==actor)<=cap for actor,cap in [('a',7),('b',5)]) and all(sum(n for a,s,n in candidate if (a,s)==key)<=cap for key,cap in [(('a','x'),4),(('a','y'),6),(('b','x'),5)])
            try: l.reserve(str(i),entries); actual=True
            except Rejected: actual=False
            self.assertEqual(actual,expected)
            if actual: accepted.extend(entries)

class ProtocolTests(unittest.TestCase):
    def setUp(self):
        self.p=fixture(); self.t=Target('claim','v1','fixture:a'); self.o=self.p.offer(self.t,'author',{'numerics'})
    def check(self,who='reviewer-a',outcome='support'):
        return self.p.check(self.o,who,{'numerics'},'fixture arithmetic',outcome,'synthetic only')
    def rely(self,checks,**kwargs):
        return self.p.rely(self.o,'scientist',checks,'fixture use',{'numerics'},'scientific',10,**kwargs)
    def test_typed_authority(self):
        c=self.check()
        for who in ['reviewer-a','editor']:
            with self.assertRaises(Rejected): self.p.rely(self.o,who,[c],'use',{'numerics'},'scientific',10)
        r=self.p.rely(self.o,'editor',[c],'publish fixture',{'numerics'},'publication',10)
        self.assertEqual(self.p.reliances[r].kind,'publication')
    def test_team_size_and_duplicate_receipts_not_independence(self):
        with self.assertRaises(Rejected): self.check('author')
        c=self.check()
        with self.assertRaises(Rejected): self.rely([c,c])
        with self.assertRaises(Rejected): self.rely([c],required_groups=2)
    def test_every_scope_covered_independently(self):
        p=Protocol([Actor('author','a',frozenset()),Actor('x','x',frozenset({'x'})),Actor('y','y',frozenset({'y'})),Actor('d','d',frozenset(),frozenset({'scientific'}))],{'x':2,'y':2},{('x','x'):2,('y','y'):2})
        o=p.offer(self.t,'author',{'x','y'}); c=[PolicyAgent(a).act(p,o,{a}) for a in ['x','y']]
        with self.assertRaises(Rejected): p.rely(o,'d',c,'use',{'x','y'},'scientific',10,required_groups=2)
    def test_unknown_and_contradiction_omission(self):
        c=self.check(outcome='unknown')
        with self.assertRaises(Rejected): self.rely([c])
        c=self.check(); self.check('reviewer-b','contradiction')
        with self.assertRaises(Rejected): self.rely([c])
    def test_exact_version(self):
        c=self.check(); o=self.p.offer(Target('claim','v2','fixture:b'),'author',{'numerics'})
        with self.assertRaises(Rejected): self.p.rely(o,'scientist',[c],'use',{'numerics'},'scientific',10)
    def test_currentness_renewal_and_evidence(self):
        c=self.check(); r=self.rely([c])
        for now,observed,expected in [(1,None,'freshness_unknown'),(3,1,'freshness_unknown'),(10,10,'expired')]: self.assertEqual(copy.deepcopy(self.p).currentness(r,now,observed,1),expected)
        with self.assertRaises(Rejected): self.p.currentness(r,1,2,1)
        self.p.amend(self.t,'changed assumption',1)
        self.assertEqual(self.p.currentness(r,1,1,1),'reconsideration_pending')
        with self.assertRaises(Rejected): self.rely([c],now=1)
        c2=PolicyAgent('reviewer-a').act(self.p,self.o,{'numerics'},now=2); r2=self.rely([c2],now=2)
        self.assertEqual(self.p.currentness(r2,2,2,1),'current_under_toy_policy')
        self.assertEqual(self.p.currentness(r,2,2,1),'reconsideration_pending')
        self.p.set_available(self.t,False)
        self.assertEqual(self.p.currentness(r2,2,2,1),'dependency_unavailable')
    def test_later_contradiction_invalidates_existing_reliance(self):
        c=self.check(); r=self.rely([c])
        self.p.check(self.o,'reviewer-b',{'numerics'},'counterexample','contradiction','synthetic',now=1)
        self.assertEqual(self.p.currentness(r,1,1,1),'contradiction_pending')

    def test_coverage_contract_cannot_be_weakened(self):
        p=fixture(); o=p.offer(self.t,'author',{'numerics'},required_groups=2)
        c=PolicyAgent('reviewer-a').act(p,o,{'numerics'})
        with self.assertRaises(Rejected):
            p.rely(o,'scientist',[c],'use',{'numerics'},'scientific',10,required_groups=1)
        c2=PolicyAgent('reviewer-b').act(p,o,{'numerics'})
        r=p.rely(o,'scientist',[c,c2],'use',{'numerics'},'scientific',10)
        self.assertEqual(p.reliances[r].required_groups,2)

    def test_query_time_cannot_roll_back(self):
        c=self.check(); r=self.rely([c])
        self.assertEqual(self.p.currentness(r,10,10,1),'expired')
        with self.assertRaises(Rejected): self.p.currentness(r,1,1,1)

    def test_atomic_complete_panel(self):
        p=fixture(capacity=1); o=p.offer(self.t,'author',{'numerics'})
        req=dict(offer_id=o,reviewer_id='reviewer-a',scope={'numerics'},method='toy',outcome='support',limits='toy'); before=list(p.events)
        with self.assertRaises(Rejected): p.check_panel([req,req])
        self.assertEqual(p.events,before); self.assertEqual(p.ledger.totals(),({},{}))
    def test_dependency_closure_independent_forward_oracle(self):
        rng=random.Random(177); targets=[self.t]; edges=[]
        for i in range(1,16):
            t=Target(f'claim{i}','v1',f'fixture:{i}'); deps=[j for j in range(i) if rng.random()<.2]
            self.p.offer(t,'author',{'numerics'},[targets[j] for j in deps]); edges.extend((j,i) for j in deps); targets.append(t)
        for source in range(len(targets)):
            affected={source}
            for _ in targets: affected|={b for a,b in edges if a in affected}
            self.assertEqual(set(self.p.amend(targets[source],'fixture')),{targets[i] for i in affected})
    def test_backdated_action_rejected_without_mutation(self):
        self.check(); self.p.amend(self.t,'change',now=3)
        before=list(self.p.events)
        with self.assertRaises(Rejected): self.check()
        self.assertEqual(self.p.events,before)

    def test_degraded_correction_retained(self):
        self.p.enter_degraded('capacity')
        with self.assertRaises(Rejected): self.p.offer(Target('new','v1','fixture:z'),'author',{'numerics'})
        self.assertEqual(self.p.amend(self.t,'existing correction'),[self.t])
    def test_cycle_and_hidden_dependency_negative_control(self):
        r=release_cycle(); self.assertEqual(r['after'],'reconsideration_pending'); self.assertEqual(r['renewal'],'current_under_toy_policy'); self.assertTrue(hidden_dependency()['failure_exposed'])

class SelectionTests(unittest.TestCase):
    def test_seedwise_group_distribution_invariance(self):
        base=[Actor(g,g,frozenset({'x'})) for g in 'ABC']; clones=base+[Actor(f'A{i}','A',frozenset({'x'})) for i in range(50)]; groups={a.actor_id:a.control_group for a in clones}
        for seed in range(200): self.assertEqual({groups[a] for a in sample_panel(base,'x',2,seed=seed)},{groups[a] for a in sample_panel(clones,'x',2,seed=seed)})
    def test_coverage_unavailable(self):
        actors=[Actor(str(i),'same',frozenset({'x'})) for i in range(20)]
        with self.assertRaises(Rejected): sample_panel(actors,'x',2)
        with self.assertRaises(Rejected): sample_panel(actors,'x',1,{'same'})

if __name__=='__main__': unittest.main()
