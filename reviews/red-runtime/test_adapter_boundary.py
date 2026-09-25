"""Type confusion must not promote raw metadata into a stronger assertion."""
import copy
import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from adapters.legacy import adapt,roundtrip,execute_fixture,AdapterError

class AdapterRedTests(unittest.TestCase):
    def test_integer_immutable_flag_cannot_be_upgraded_in_projection(self):
        source=json.loads((ROOT/'adapters/fixtures/review-issue.json').read_text())
        enrichment=json.loads((ROOT/'adapters/fixtures/trusted-enrichment.json').read_text())
        source['claim']['immutable_refs']=1
        env=adapt(source)
        with self.assertRaises(AdapterError):execute_fixture(env,enrichment)
        env['mapped']['immutable_refs']['value']=True
        with self.assertRaises(AdapterError):roundtrip(env)
        with self.assertRaises(AdapterError):execute_fixture(env,enrichment)

if __name__=='__main__':unittest.main()
