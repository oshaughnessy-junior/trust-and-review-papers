import unittest,copy
from fractions import Fraction as F
from machine import Machine,repair_bound
M=(((F(1,4),F(1,4)),(F(0),F(1,2))),((F(1,2),F(0)),(F(1,4),F(1,4))))
class MachineTests(unittest.TestCase):
    def offer(self,m,**kw):
        args=dict(actor='author',target='claim@1',scope='toy mean',dependencies=('data@1',),seed=4);args.update(kw)
        return m.apply('offer','offer',**args)
    def check(self,m,outcome='passed',request='check',**kw):
        args=dict(actor='verifier',target='claim@1',scope='toy mean',representatives=m.planned_representatives('claim@1'),outcome=outcome,evidence='fixture:e');args.update(kw)
        return m.apply(request,'check',**args)
    def test_four_actions_and_history(self):
        m=Machine();self.offer(m);e=self.check(m)
        m.apply('rely','rely',actor='decision-maker',target='claim@1',scope='toy mean',check_seq=e['seq'])
        before=copy.deepcopy(m.events)
        a=m.apply('amend','amend',actor='author',changed='data@1',successor='data@2',matrices=M,weights=(F(1),F(1)))
        self.assertEqual(a['repair_plan']['bound'],2);self.assertEqual(a['repair_reserved'],0)
        self.assertFalse(m.reliances[0]['current']);self.assertEqual(m.events[:len(before)],before)
        self.assertEqual(m.offers['claim@1']['phase'],'pending-amendment')
    def test_rejections_atomic(self):
        m=Machine();self.offer(m)
        for changes in ({'actor':'author'},{'scope':'wrong'},{'representatives':('A:0','A:0')},{'evidence':''}):
            before=copy.deepcopy(m.__dict__)
            with self.assertRaises(ValueError):self.check(m,**changes)
            self.assertEqual(m.__dict__,before)
        with self.assertRaises(ValueError):m.apply('offer','offer',actor='author',target='x',scope='x',dependencies=())
    def test_admission_reserves_shared_work_and_rejects_hard_budget(self):
        m=Machine(capacity=F(4));before=copy.deepcopy(m.__dict__)
        with self.assertRaises(ValueError):self.offer(m)
        self.assertEqual(m.__dict__,before)
        with self.assertRaises(ValueError):self.offer(Machine(),audit_q=F(1,2),audit_budget=F(3,2))
    def test_refusals_have_cost_and_stop_at_limit(self):
        m=Machine();self.offer(m)
        for i in range(3):self.check(m,'refused','check'+str(i))
        self.assertEqual(m.spent,F(13,10));self.assertEqual(m.held,0)
        self.assertEqual(m.offers['claim@1']['phase'],'exhausted')
    def test_audit_unique_and_cap(self):
        for seed in range(40):
            m=Machine();self.offer(m,seed=seed)
            for i in range(3):self.check(m,'refused','check'+str(i))
            self.assertEqual(sum(e.get('audit_executed',False) for e in m.events),1)
            self.assertEqual(m.offers['claim@1']['audit_spent'],1)
    def test_clone_invariance_does_not_change_later_draws(self):
        for seed in range(20):
            a=Machine();b=Machine(counts={'A':100,'B':1,'C':1});self.offer(a,seed=seed);self.offer(b,seed=seed)
            self.assertEqual(a.offers['claim@1']['panels'],b.offers['claim@1']['panels'])
            self.assertEqual(a.offers['claim@1']['audits'],b.offers['claim@1']['audits'])
    def test_rely_requires_exact_success_and_separate_actor(self):
        for kwargs in ({'actor':'author'},{'scope':'other'},{'target':'claim@2'},{'check_seq':99}):
            m=Machine();self.offer(m);e=self.check(m)
            args=dict(actor='decision-maker',scope='toy mean',target='claim@1',check_seq=e['seq']);args.update(kwargs)
            with self.assertRaises(ValueError):m.apply('rely','rely',**args)
        m=Machine();self.offer(m);e=self.check(m,'failed')
        with self.assertRaises(ValueError):m.apply('rely','rely',actor='decision-maker',scope='toy mean',target='claim@1',check_seq=e['seq'])
    def test_stale_dependency_cannot_be_reoffered(self):
        m=Machine();self.offer(m);self.check(m)
        m.apply('amend','amend',actor='author',changed='data@1',successor='data@2',matrices=M,weights=(F(1),F(1)))
        with self.assertRaises(ValueError):m.apply('offer2','offer',actor='author',target='claim@2',scope='toy mean',dependencies=('data@1',))
    def test_unstable_and_invalid_envelopes_do_not_prevent_invalidation(self):
        for family in ((((F(0),F(2)),(F(0),F(0))),((F(0),F(0)),(F(2),F(0)))),()):
            m=Machine();self.offer(m)
            a=m.apply('amend','amend',actor='author',changed='data@1',successor='data@2',matrices=family,weights=(F(1),F(1)))
            self.assertFalse(a['repair_plan']['certified']);self.assertEqual(m.offers['claim@1']['phase'],'pending-amendment')
    def test_successor_collisions_are_atomic(self):
        m=Machine();self.offer(m)
        before=copy.deepcopy(m.__dict__)
        with self.assertRaises(ValueError):m.apply('amend','amend',actor='author',changed='data@1',successor='claim@1',matrices=M,weights=(1,1))
        self.assertEqual(m.__dict__,before)
    def test_transitive_amendment_blocks_downstream_reliance(self):
        m=Machine();self.offer(m);self.check(m)
        m.apply('offer2','offer',actor='author',target='claim@2',scope='downstream',dependencies=('claim@1',))
        e=m.apply('check2','check',actor='verifier',target='claim@2',scope='downstream',representatives=m.planned_representatives('claim@2'),outcome='passed',evidence='fixture:downstream')
        m.apply('rely2','rely',actor='decision-maker',target='claim@2',scope='downstream',check_seq=e['seq'])
        a=m.apply('amend','amend',actor='author',changed='data@1',successor='data@2',matrices=M,weights=(1,1))
        self.assertEqual(a['affected'],('claim@1','claim@2'));self.assertFalse(m.reliances[0]['current'])
        with self.assertRaises(ValueError):m.apply('stale','rely',actor='decision-maker',target='claim@2',scope='downstream',check_seq=e['seq'])
    def test_integer_repair_inputs_remain_exact(self):
        result=repair_bound((((0,1),(0,0)),),(3,1),(1,0))
        self.assertEqual(result['r'],F(1,3));self.assertEqual(result['bound'],F(9,2))
        self.assertIsInstance(result['bound'],F)
    def test_audit_disclosure_breaks_sequential_incentive_premise(self):
        for seed in range(30):
            m=Machine();self.offer(m,seed=seed)
            if m.offers['claim@1']['audits']=={0}:
                first=self.check(m,'refused')
                self.assertTrue(first['audit_executed'])
                self.assertNotIn(1,m.offers['claim@1']['audits'])
                self.assertGreater(F(1,10),F(0)*F(4,5))
                break
        else:self.fail('Expected explicit disclosed-quota counterexample')
    def test_hidden_dependency_remains_undetected(self):
        m=Machine();self.offer(m,dependencies=());self.check(m)
        a=m.apply('amend','amend',actor='author',changed='data@1',successor='data@2',matrices=M,weights=(F(1),F(1)))
        self.assertEqual(a['affected'],());self.assertEqual(m.offers['claim@1']['phase'],'ready')

if __name__=='__main__':unittest.main()
