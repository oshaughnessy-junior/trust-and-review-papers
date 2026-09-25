"""Adversarial mathematical fixtures; no human or deployment evidence."""
import hashlib
import json
import math
from pathlib import Path

r, alpha, beta, delta, entry, g = 1, .01, .20, .95, 10, 1.4
baseline = r/(1-delta+delta*alpha)
modified = (r+delta*alpha*entry)/(1-delta+delta*alpha)
stale_bound = (beta-alpha)*delta*(baseline-entry)
correct_bound = (beta-alpha)*delta*(modified-entry)
assert stale_bound < g < correct_bound
assert abs(modified-(r+delta*((1-alpha)*modified+alpha*entry))) < 1e-12
assert abs(baseline-(r+delta*((1-alpha)*baseline+alpha*entry))) > .09
# A probabilistic panel cap before acceptance does not survive completion selection.
initial_bad, good_completion, bad_completion = .1, .01, 1
completed_bad = initial_bad*bad_completion/((1-initial_bad)*good_completion+initial_bad*bad_completion)
assert completed_bad > .91
# A per-panel distinct-group constraint is not group-level distribution invariance.
# Three groups A, B, C and 2 seats: initially AB, AC, BC; replicate A m times.
m=100
before=2/3
after=2*m/(2*m+1)
assert after > .99
# Explicit stochastic retry example also illustrates why deterministic support caps survive.
feasible_panels = [('local', 'import1'), ('local', 'import2')]
assert all(sum(x.startswith('import') for x in p) <= 1 for p in feasible_panels)
# Inspecting two deviations: passing D1's incentive test says nothing about D2.
L=delta*baseline
assert 2 <= (.20-alpha)*L
assert 2 > (.011-alpha)*L
report={
 'status':'all adversarial assertions passed',
 'scope':'synthetic equations and combinatorics only; no implementation of panel sampler claimed',
 'reset':{'baseline_V':baseline,'correct_V':modified,'stale_bound':stale_bound,'correct_bound':correct_bound,'gain':g},
 'completion_conditioning':{'proposal_bad_share':initial_bad,'completed_bad_share':completed_bad},
 'panel_multiplicity':{'group_A_seat_probability_before':before,'group_A_seat_probability_after_100_labels':after},
 'deviation_coverage':{'checked_deviation_bound':(.20-alpha)*L,'unmonitored_deviation_bound':(.011-alpha)*L},
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
Path(__file__).with_name('fixtures.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
