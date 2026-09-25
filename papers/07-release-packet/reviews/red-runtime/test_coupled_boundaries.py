import unittest
from coupled_runtime_probe import ledger_class

class CoupledBoundaryTests(unittest.TestCase):
    def test_zero_capacity_cannot_be_minted_by_multiple_zero_holds(self):
        ledger=ledger_class()({'A':0})
        holds=[ledger.reserve({'A':0}) for _ in range(10)]
        for hold in holds:
            with self.assertRaises(ValueError):ledger.settle(hold,{'A':1e-12},'probe')
        self.assertEqual(ledger.used['A'],0)
        self.assertEqual(len(ledger.holds),10)

if __name__=='__main__':unittest.main()
