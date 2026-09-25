#!/usr/bin/env python3
"""Deterministic checks of explicitly synthetic mathematical examples."""
import hashlib
import json
import math
import platform
from pathlib import Path


def continuation_gap(r, r0, alpha, fine, delta):
    return (r - r0 - alpha * fine) / (1 - delta + delta * alpha)


def stationary_two_state(continuation, leakage):
    return continuation * leakage / (1 - continuation + continuation * leakage)


def softmax_adverse_share(total_adverse, adverse_count, beta):
    # One trusted candidate, equal workloads and costs, v_i = p_i.
    log_ratio = math.log(adverse_count) + beta * (total_adverse / adverse_count - (1 - total_adverse))
    return 1 / (1 + math.exp(-log_ratio))


def max_flow(capacities, source, sink):
    """Edmonds-Karp, integral capacities only; tiny independent fixture graphs."""
    residual = {}
    for (u, v), capacity in capacities.items():
        residual.setdefault(u, {})[v] = capacity
        residual.setdefault(v, {}).setdefault(u, 0)
    total = 0
    while True:
        parent = {source: None}
        queue = [source]
        for u in queue:
            for v, capacity in residual[u].items():
                if capacity > 0 and v not in parent:
                    parent[v] = u
                    queue.append(v)
            if sink in parent:
                break
        if sink not in parent:
            return total
        bottleneck = math.inf
        v = sink
        while parent[v] is not None:
            u = parent[v]
            bottleneck = min(bottleneck, residual[u][v])
            v = u
        v = sink
        while parent[v] is not None:
            u = parent[v]
            residual[u][v] -= bottleneck
            residual[v][u] += bottleneck
            v = u
        total += bottleneck


def main():
    results = {}
    gap = continuation_gap(1, 0, .01, 0, .95)
    assert math.isclose(gap, 1 / .0595)
    results['effort_benchmark'] = {'gap': gap, 'deterrence_bound': (.20 - .01) * .95 * gap}
    assert results['effort_benchmark']['deterrence_bound'] > 2
    results['low_detection_bound'] = (.02 - .01) * .95 * gap
    assert results['low_detection_bound'] < 2
    # Check Bellman equations with both honest false positives and immediate loss.
    r, r0, alpha, fine, delta = 2, .2, .03, .4, .8
    W = r0 / (1 - delta)
    V = W + continuation_gap(r, r0, alpha, fine, delta)
    assert math.isclose(V, r-alpha*fine+delta*((1-alpha)*V+alpha*W))
    results['bellman_with_false_positives'] = {'V': V, 'W': W, 'residual': V-(r-alpha*fine+delta*((1-alpha)*V+alpha*W))}
    a, raw = .85, 1e-6
    results['raw_capacity_normalization'] = {'raw_capacity': raw, 'actual_leakage': raw/raw, 'actual_stationary_adverse': stationary_two_state(a, 1), 'invalid_raw_bound': stationary_two_state(a, raw)}
    assert math.isclose(results['raw_capacity_normalization']['actual_stationary_adverse'], .85)
    # Verify tight stationary equation independently over a small parameter grid.
    for a in (.1, .5, .85, .99):
        for leakage in (0, .0001, .01, .2, 1):
            x = stationary_two_state(a, leakage)
            assert math.isclose(x, a*(leakage*(1-x)+x), abs_tol=1e-12)
    m = 1000
    share = softmax_adverse_share(.01, m, 1)
    assert share > .997
    results['softmax_multiplicity'] = {'stationary_adverse_total': .01, 'adverse_candidates': m, 'beta': 1, 'actual_assignment_adverse': share}
    results['softmax_count_sweep'] = [{'adverse_candidates': m, 'share': softmax_adverse_share(.01, m, 1)} for m in (1, 10, 100, 1000)]
    # One frontier edge supports every per-target eligibility flow separately.
    n = 7
    caps = {('root', 'broker'): 1}
    caps.update({('broker', f'candidate{i}'): 1 for i in range(n)})
    independent = [max_flow(caps, 'root', f'candidate{i}') for i in range(n)]
    joint = dict(caps)
    joint.update({(f'candidate{i}', 'sink'): 1 for i in range(n)})
    simultaneous = max_flow(joint, 'root', 'sink')
    assert independent == [1] * n
    assert simultaneous == 1
    results['frontier_reuse'] = {'independent_candidate_maxflows': independent, 'sum_of_independent_results': sum(independent), 'simultaneous_maxflow': simultaneous}
    # Eligibility filtering can condition all honest routing mass away.
    honest_p, adverse_p = .99, .01
    conditioned = adverse_p / (0 * honest_p + adverse_p)
    assert conditioned == 1
    results['eligibility_conditioning'] = {'unconditional_adverse': adverse_p, 'conditional_adverse': conditioned, 'cap_policy_response': 'infeasible if adverse cap < 1; do not silently renormalize'}
    results['common_mode'] = .10 + (1-.10)*.10**3
    assert math.isclose(results['common_mode'], .1009)
    script = Path(__file__)
    report = {'status': 'all deterministic assertions passed', 'interpretation': 'Synthetic mathematical fixtures only; no real scientific, human or deployment outcomes.', 'python': platform.python_version(), 'script_sha256': hashlib.sha256(script.read_bytes()).hexdigest(), 'randomness': 'none', 'results': results}
    out = (script.resolve().parents[2]/'results'/'game-theory.json')
    out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
