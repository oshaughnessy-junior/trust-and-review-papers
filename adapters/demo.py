"""Run from packet root: python3 -m adapters.demo"""
from pathlib import Path
import hashlib
import json
import platform
from .legacy import adapt,roundtrip,execute_fixture,AdapterError

def main():
    root=Path(__file__).parent
    source=json.loads((root/'fixtures/review-issue.json').read_text())
    enrichment=json.loads((root/'fixtures/trusted-enrichment.json').read_text())
    envelope=adapt(source)
    unaugmented={}
    try:execute_fixture(envelope)
    except AdapterError as error:unaugmented={'status':'refused','reason':str(error)}
    if unaugmented.get('status')!='refused':raise AssertionError('legacy input unexpectedly authorized')
    demo=execute_fixture(envelope,enrichment)
    assert roundtrip(envelope)==source
    assert demo['before_amendment']=='current_under_toy_policy'
    assert demo['after_amendment']=='reconsideration_pending'
    output={'schema':'synthetic-legacy-demo/0.1','python':platform.python_version(),
            'roundtrip_equal':True,'unaugmented_attempt':unaugmented,'augmented_demo':demo,
            'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.suffix in ('.py','.json','.txt') and 'results' not in p.parts}}
    output['runtime_sha256']=hashlib.sha256((root.parent/'toy_agents/protocol.py').read_bytes()).hexdigest()
    (root/'results/demo.json').write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    print('Synthetic adapter: roundtrip preserved; raw reliance refused; enriched cycle pending after amendment.')

if __name__=='__main__':main()
