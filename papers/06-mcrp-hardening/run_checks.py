#!/usr/bin/env python3
"""Run the bounded research checks and record source/data identity."""
from __future__ import annotations
import hashlib
import json
import platform
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parent


def main():
    logs=ROOT/'results'/'check-logs';logs.mkdir(parents=True,exist_ok=True)
    commands=[
        ('science-boundary-tests',['-m','unittest','discover','-s','models','-p','test_*.py','-v']),
        ('economics-tests',['-m','unittest','discover','-s','models/economics','-p','test_*.py','-v']),
        ('legal-tests',['-m','unittest','discover','-s','models/legal','-p','test_*.py','-v']),
        ('science-sweeps',['models/run_experiments.py']),
        ('economic-sweeps',['models/economics/run.py']),
        ('game-fixtures',['models/game_theory/model_checks.py']),
        ('compositional-science',['models/science/model_checks.py']),
        ('legal-capacity',['models/legal/capacity_model.py']),
        ('adversarial-science',['reviews/red-team/science/fixtures.py']),
        ('adversarial-games',['reviews/red-team/games/fixtures.py']),
        ('adversarial-law',['reviews/red-team/law/fixtures.py']),
        ('original-economics-defects',['reviews/red-team/economics/checks.py']),
    ]
    outcomes=[]
    for name,args in commands:
        p=subprocess.run([sys.executable,*args],cwd=ROOT,text=True,capture_output=True)
        data=p.stdout+p.stderr
        (logs/f'{name}.txt').write_text(data)
        outcomes.append({'name':name,'command':['python3',*args],'returncode':p.returncode,
                         'log':f'results/check-logs/{name}.txt','sha256':hashlib.sha256(data.encode()).hexdigest()})
        print(f'{name}: {"PASS" if p.returncode==0 else "FAIL"}',flush=True)
        if name=='legal-capacity' and p.returncode==0:
            (ROOT/'results/legal-capacity.json').write_text(p.stdout)
    report={'schema':'mcrp-hardening.validation.v1','environment':{'python':platform.python_version()},
            'status':'passed' if all(x['returncode']==0 for x in outcomes) else 'failed',
            'unit_test_methods':25,
            'scope':'Synthetic model checks; original-economics-defects reproduces rejected original solver behavior, not a passing implementation',
            'checks':outcomes,
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in sorted(ROOT.rglob('*.py'))},
            'table_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in sorted((ROOT/'results').rglob('*.csv'))}}
    (ROOT/'results/validation.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    return 0 if report['status']=='passed' else 1


if __name__=='__main__':raise SystemExit(main())
