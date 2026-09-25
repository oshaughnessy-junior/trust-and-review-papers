"""Usage: python3 -m toy_agents.run --output toy_agents/results/demo.json"""
import argparse
import hashlib
import json
import platform
from pathlib import Path
from .scenarios import run_demo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,default=17)
    parser.add_argument('--output',type=Path,default=Path('toy_agents/results/demo.json'))
    args=parser.parse_args()
    root=Path(__file__).parent
    result={'schema':'mcrp-toy-agents/0.1', 'evidence_class':'I: synthetic implementation experiment',
            'seed':args.seed, 'python':platform.python_version(),
            'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*.py'))},
            'configuration':{'selection_draws':3000,'clone_count':100,'completion_offers':10000},
            'scenarios':run_demo(args.seed)}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(f'Wrote {args.output}; synthetic fixtures, no efficacy claim.')

if __name__=='__main__':
    main()
