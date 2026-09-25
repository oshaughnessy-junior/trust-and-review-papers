"""Public-API probe: per-hold tolerances must not mint unreserved capacity."""
import importlib.util
import json
from pathlib import Path
import sys


def ledger_class():
    path=Path(__file__).resolve().parents[2]/'models/coupled/simulator.py'
    spec=importlib.util.spec_from_file_location('red_coupled_simulator',path)
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
    return m.Ledger


def probe():
    ledger=ledger_class()({'A':0})
    tokens=[ledger.reserve({'A':0}) for _ in range(3)]
    results=[]
    for token in tokens:
        try:
            ledger.settle(token,{'A':1e-12},'probe')
            results.append('accepted')
        except ValueError as e:results.append(str(e))
    return {'settlements':results,'ledger':ledger.report()}

if __name__=='__main__':print(json.dumps(probe(),indent=2))
