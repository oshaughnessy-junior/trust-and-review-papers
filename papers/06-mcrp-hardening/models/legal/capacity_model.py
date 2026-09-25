#!/usr/bin/env python3
"""Synthetic accounting fixtures. No legal or human-behavior predictions."""
import json
import platform
from math import isclose, isfinite


def nonnegative(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value) or value < 0:
        raise ValueError('costs, workload and capacity must be finite nonnegative numbers')


def probability(value):
    nonnegative(value)
    if value > 1:
        raise ValueError('probability must be in [0,1]')


def bounded_appeal_cost(cost, continuation, max_depth):
    nonnegative(cost)
    probability(continuation)
    if isinstance(max_depth, bool) or not isinstance(max_depth, int) or max_depth < 0:
        raise ValueError('max_depth must be a nonnegative integer')
    return cost * sum(continuation ** depth for depth in range(max_depth + 1))


def backlog(work, capacity):
    if len(work) != len(capacity):
        raise ValueError('work and capacity must describe the same epochs')
    pending = 0
    series = []
    for arriving, available in zip(work, capacity):
        nonnegative(arriving)
        nonnegative(available)
        pending = max(0, pending + arriving - available)
        series.append(pending)
    return series


def utilization(arrivals, initial_cost, appeal_cost, appeal_probability,
                total_capacity, reserved_capacity, overhead):
    for value in [arrivals, initial_cost, appeal_cost, total_capacity, reserved_capacity, overhead]:
        nonnegative(value)
    probability(appeal_probability)
    normal = total_capacity - reserved_capacity
    if normal <= 0:
        raise ValueError('ordinary capacity must be positive')
    return (arrivals * (initial_cost + appeal_probability * appeal_cost) + overhead) / normal


def main():
    assert bounded_appeal_cost(30, 1, 1) == 60
    assert isclose(bounded_appeal_cost(30, .5, 2), 52.5)
    assert backlog([100, 0, 0], [40, 40, 40]) == [60, 20, 0]
    assert backlog([60] * 4, [40] * 4) == [20, 40, 60, 80]
    # Illustrative minutes/week; not calibrated to an actual steward or pilot.
    config = dict(initial_cost=30, appeal_cost=30, appeal_probability=.5,
                  total_capacity=600, reserved_capacity=120, overhead=30)
    result = {
        'status': 'synthetic arithmetic; no empirical service data',
        'python': platform.python_version(),
        'units': 'staff minutes per week except counts/probabilities',
        'randomness': 'none',
        'configuration': config,
        'ordinary_load_sweep': [
            {'cases_per_week': n, 'utilization': utilization(n, **config)}
            for n in [4, 8, 10, 12, 20]],
        'one_appeal_expected_minutes': bounded_appeal_cost(30, .5, 1),
        'recursive_appeal_expected_minutes_p_095': 30 / (1 - .95),
        'one_appeal_expected_minutes_p_095': bounded_appeal_cost(30, .95, 1),
        'sustained_overload_backlog': backlog([600]*8, [480]*8),
        'burst_backlog': backlog([1400]+[0]*7, [480]*8),
        'deterministic_critical_load': backlog([40]*4, [40]*4),
        'refused_intake_flood': {
            'attempts': 10000, 'minutes_per_attempt': .1,
            'utilization_with_fixed_overhead': utilization(4, **config),
            'utilization_with_attempted_intake': utilization(4, **{**config, 'overhead': 1030})},
        'sequential_new_evidence': {
            'epochs': 8, 'minutes_per_update': 30, 'updates_per_epoch': 3,
            'case_epoch_budget': 60,
            'unresolved_work': backlog([90]*8, [60]*8)},
        'limits': ['No latency distribution', 'No abuse-classifier model',
                   'Reserved capacity is not guaranteed sufficient',
                   'Distinct rights claims can overwhelm any finite capacity']}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
