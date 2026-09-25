"""Synthetic boundary semantics: no signing, identity, networking, or legal engine.

Inputs are trusted fixture facts. A real system must authenticate and authorize
each fact before calling this projection. Time uses integer synthetic epochs.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Reliance:
    release: str
    scientific_disposition: str
    decided_at: int
    expires_at: int


@dataclass(frozen=True)
class Snapshot:
    release: str
    observed_at: int
    unresolved_material_change: str | None
    evidence_available: bool


def reliance_view(receipt: Reliance, snapshot: Snapshot | None,
                  now: int, max_snapshot_age: int) -> dict:
    if receipt.expires_at <= receipt.decided_at or now < receipt.decided_at or max_snapshot_age < 0:
        raise ValueError('invalid temporal policy')
    reasons=[]
    if now >= receipt.expires_at:
        reasons.append('expired')
    if snapshot is None:
        reasons.append('freshness_unknown')
    else:
        if snapshot.release != receipt.release or snapshot.observed_at > now:
            raise ValueError('snapshot binding or future observation invalid')
        if snapshot.observed_at < receipt.decided_at or now-snapshot.observed_at > max_snapshot_age:
            reasons.append('freshness_unknown')
        # Receipt-relative unresolved change, not simply the latest historical
        # amendment. Authorized re-reliance may resolve an earlier amendment.
        if snapshot.unresolved_material_change is not None:
            reasons.append('reconsideration_pending')
        if not snapshot.evidence_available:
            reasons.append('dependency_unavailable')
    return {'historical_disposition':receipt.scientific_disposition,
            'historical_release':receipt.release,
            'as_of':snapshot.observed_at if snapshot else None,
            'currentness':'conditions_observed' if not reasons else 'not_established',
            'reasons':reasons,
            'limit':'Currentness projection only; not scientific truth or cryptographic verification'}


def affected(dependencies: dict[str,set[str]], changed: str) -> set[str]:
    """Reachability in a declared finite graph, deduplicated by claim ID."""
    reached={changed}
    while True:
        new={claim for claim,deps in dependencies.items() if deps & reached}-reached
        if not new:
            return reached-{changed}
        reached.update(new)


def capacity_feasible(allocations: dict[str,dict[str,float]], capacities: dict[str,float]) -> bool:
    """Shared person/epoch accounting, not a complete scheduling optimizer."""
    import math
    for person,lanes in allocations.items():
        if person not in capacities:
            return False
        values=[capacities[person],*lanes.values()]
        if any(isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<0 for v in values):
            raise ValueError('finite nonnegative hours required')
        if sum(lanes.values())>capacities[person]+1e-12:
            return False
    return True
