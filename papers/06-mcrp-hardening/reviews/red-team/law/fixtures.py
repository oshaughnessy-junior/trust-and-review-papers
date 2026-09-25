#!/usr/bin/env python3
"""Adversarial conceptual witnesses, not attacks on a deployed MCRP service."""
import importlib.util
import json
from pathlib import Path

source = Path(__file__).resolve().parents[3] / 'models' / 'legal' / 'capacity_model.py'
spec = importlib.util.spec_from_file_location('capacity_model', source)
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)


def completion(order):
    # Both jobs available at time zero; minute units. Deadlines are synthetic.
    jobs = {'ordinary': (50, 100), 'rights': (10, 15)}
    now = 0
    results = {}
    for name in order:
        cost, deadline = jobs[name]
        now += cost
        results[name] = dict(completed=now, deadline=deadline, late=now > deadline)
    return results


def main():
    assert model.backlog([60], [60]) == [0]
    first_ordinary = completion(['ordinary', 'rights'])
    first_rights = completion(['rights', 'ordinary'])
    assert first_ordinary['rights']['late']
    assert not first_rights['rights']['late']
    # A low-rate system clears each epoch and still misses every short deadline.
    assert model.backlog([60]*4, [100]*4) == [0]*4

    # Internal authorization survives while an already-public sensitive export persists.
    before = dict(S='supported', V='public', P='active', I='closed')
    after = dict(before, V='hidden')
    changed = {key for key in before if before[key] != after[key]}
    assert changed <= {'V'}
    export = {'reviewer_contact': 'synthetic-person@example.invalid'}
    assert export['reviewer_contact']

    # A triage burst alone can exhaust protected capacity, with zero substantive admissions.
    attempts, cost, reserved = 1300, .1, 120
    assert model.backlog([attempts*cost], [reserved]) == [10.0]

    rejected = 0
    for bad in [True, -1, float('inf'), float('nan'), '2']:
        try:
            model.backlog([bad], [10])
        except ValueError:
            rejected += 1
    assert rejected == 5

    results = {
        'status': 'conceptual specification witnesses; not deployed defects',
        'deadline_blindness': {
            'identical_scalar_backlog': model.backlog([60], [60]),
            'ordinary_first': first_ordinary,
            'rights_first': first_rights,
            'repeated_low_load_end_epoch_backlog': model.backlog([60]*4, [100]*4),
        },
        'emergency_triage_flood': {
            'attempts': attempts, 'triage_minutes_per_attempt': cost,
            'reserved_minutes': reserved, 'substantive_admissions': 0,
            'pending_minutes': model.backlog([attempts*cost], [reserved]),
        },
        'write_set_is_not_information_flow': {
            'permitted_coordinate_change': sorted(changed),
            'sensitive_export_still_exists': bool(export),
        },
        'invalid_numeric_inputs_rejected': rejected,
    }
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
