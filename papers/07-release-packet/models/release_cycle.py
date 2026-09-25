"""A trusted-input publication boundary model, not a deployment/security service.

Every identity/role comes from the fixture operator. No signature, sandbox,
network, institutional independence, or legal authority is implemented. The
purpose is to distinguish decisions about bytes from observations of delivery.
"""
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, FrozenSet, Optional, Tuple


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      allow_nan=False).encode("utf-8")


@dataclass(frozen=True)
class Candidate:
    release_id: str
    source_revision: str
    content: bytes
    evidence_digest: str
    policy_version: str
    content_class: str
    destination: str

    @property
    def binding(self) -> str:
        return digest(canonical({
            "release_id": self.release_id,
            "source_revision": self.source_revision,
            "artifact_digest": digest(self.content),
            "evidence_digest": self.evidence_digest,
            "policy_version": self.policy_version,
            "content_class": self.content_class,
            "destination": self.destination,
        }))


@dataclass(frozen=True)
class Delegation:
    delegation_id: str
    publisher: str
    content_classes: FrozenSet[str]
    destination: str
    policy_version: str
    valid_from: int
    expires: int

    @property
    def binding(self) -> str:
        return digest(canonical({**asdict(self),
                                 "content_classes": sorted(self.content_classes)}))


@dataclass(frozen=True)
class Decision:
    candidate_binding: str
    delegation_binding: str
    verifier: str
    checked_at: int
    expires: int
    required_checks: Tuple[str, ...]


class BoundaryError(ValueError):
    pass


class PublicationModel:
    """Single-process deterministic state with explicit observation semantics."""

    def __init__(self, author: str, publisher: str, verifiers: FrozenSet[str],
                 observers: FrozenSet[str], policy_version: str,
                 required_checks: FrozenSet[str]):
        if author == publisher or author in verifiers or publisher in verifiers:
            raise BoundaryError("fixture role separation violated")
        if not verifiers or not observers or publisher in observers:
            raise BoundaryError("a non-publisher observer is required")
        self.author = author
        self.publisher = publisher
        self.verifiers = frozenset(verifiers)
        self.observers = frozenset(observers)
        self.policy_version = policy_version
        self.required_checks = frozenset(required_checks)
        self.revoked = set()
        self.decisions: Dict[str, Decision] = {}
        self.deliveries: Dict[str, bytes] = {}
        self.attempts: Dict[str, str] = {}
        self.events = []
        self.clock = 0
        self.superseded = {}
        self.successor_bindings = {}

    def _time(self, now: int):
        if type(now) is not int or now < self.clock:
            raise BoundaryError("time must be a monotone integer")

    def _authorize(self, candidate: Candidate, delegation: Delegation, now: int):
        expected = self.successor_bindings.get(candidate.release_id)
        if expected is not None and expected != candidate.binding:
            raise BoundaryError("amendment successor binding mismatch")
        if delegation.delegation_id in self.revoked:
            raise BoundaryError("delegation revoked")
        if not delegation.valid_from <= now < delegation.expires:
            raise BoundaryError("delegation outside validity interval")
        if delegation.publisher != self.publisher:
            raise BoundaryError("publisher mismatch")
        if candidate.destination != delegation.destination:
            raise BoundaryError("destination outside delegation")
        if candidate.content_class not in delegation.content_classes:
            raise BoundaryError("content class outside delegation")
        if candidate.policy_version != self.policy_version or delegation.policy_version != self.policy_version:
            raise BoundaryError("policy version mismatch")

    def verify(self, candidate: Candidate, delegation: Delegation,
               verifier: str, checks: Dict[str, bool], now: int,
               expires: int) -> Decision:
        self._time(now)
        self._authorize(candidate, delegation, now)
        if verifier not in self.verifiers:
            raise BoundaryError("unlisted verifier")
        if any(checks.get(name) is not True for name in self.required_checks):
            raise BoundaryError("required check absent or not passed")
        if type(expires) is not int or not now < expires <= delegation.expires:
            raise BoundaryError("decision expiry outside delegation")
        d = Decision(candidate.binding, delegation.binding, verifier, now,
                     expires, tuple(sorted(self.required_checks)))
        self.clock = now
        self.decisions[candidate.binding] = d
        self.events.append({"type": "verified", "binding": candidate.binding,
                            "verifier": verifier, "at": now})
        return d

    def publish(self, candidate: Candidate, delegation: Delegation,
                publisher: str, now: int, transport: str = "ok") -> str:
        self._time(now)
        self._authorize(candidate, delegation, now)
        if publisher != self.publisher:
            raise BoundaryError("caller is not the publisher")
        d = self.decisions.get(candidate.binding)
        if d is None or d.delegation_binding != delegation.binding:
            raise BoundaryError("no decision for exact candidate and delegation")
        if not d.checked_at <= now < d.expires:
            raise BoundaryError("decision expired")
        old = self.attempts.get(candidate.release_id)
        if old is not None and old != candidate.binding:
            raise BoundaryError("release identifier cannot be rebound")
        if transport not in ("ok", "fail", "tamper"):
            raise BoundaryError("unknown fixture transport")
        self.clock = now
        self.attempts[candidate.release_id] = candidate.binding
        if transport == "fail":
            self.events.append({"type": "delivery_failed", "at": now,
                                "release_id": candidate.release_id})
            return "delivery_failed"
        if candidate.release_id in self.deliveries:
            return "already_delivered"
        self.deliveries[candidate.release_id] = (candidate.content if transport == "ok"
                                                else candidate.content + b"tampered")
        self.events.append({"type": "delivered_unobserved", "at": now,
                            "release_id": candidate.release_id})
        return "delivered_unobserved"

    def observe(self, candidate: Candidate, observer: str, now: int) -> dict:
        self._time(now)
        if observer not in self.observers:
            raise BoundaryError("unlisted observer")
        self.clock = now
        actual = self.deliveries.get(candidate.release_id)
        actual_binding = self.attempts.get(candidate.release_id)
        status = ("missing" if actual is None else
                  "binding_mismatch" if actual_binding != candidate.binding else
                  "matches" if digest(actual) == digest(candidate.content) else "mismatch")
        # The observer reports bytes, not current delegation or scientific validity.
        receipt = {"type": "observation", "release_id": candidate.release_id,
                   "expected_binding": candidate.binding, "actual_binding": actual_binding, "status": status,
                   "expected_digest": digest(candidate.content),
                   "actual_digest": None if actual is None else digest(actual),
                   "observer": observer, "at": now}
        self.events.append(receipt)
        return dict(receipt)

    def revoke(self, delegation_id: str, now: int):
        # Revocation authority is the trusted fixture operator, outside the model.
        self._time(now)
        if not isinstance(delegation_id, str) or not delegation_id:
            raise BoundaryError("delegation identifier required")
        self.clock = now
        self.revoked.add(delegation_id)
        self.events.append({"type": "delegation_revoked", "id": delegation_id, "at": now})

    def amend(self, old: Candidate, new: Candidate, now: int):
        self._time(now)
        if old.release_id not in self.deliveries:
            raise BoundaryError("no old delivery to amend")
        if old.release_id == new.release_id:
            raise BoundaryError("amendment needs a distinct release identifier")
        if self.attempts[old.release_id] != old.binding:
            raise BoundaryError("old target mismatch")
        if old.release_id in self.superseded:
            raise BoundaryError("old release already superseded")
        if new.release_id in self.attempts:
            raise BoundaryError("amendment successor must be a new release identifier")
        expected = self.successor_bindings.get(new.release_id)
        if expected is not None and expected != new.binding:
            raise BoundaryError("amendment successor binding mismatch")
        self.clock = now
        self.successor_bindings[new.release_id] = new.binding
        self.superseded[old.release_id] = new.release_id
        self.events.append({"type": "amendment", "old": old.release_id,
                            "new": new.release_id, "new_binding": new.binding, "at": now})

    def currentness(self, candidate: Candidate, delegation: Delegation, now: int):
        self._time(now)
        self.clock = now
        attempted = self.attempts.get(candidate.release_id)
        if attempted is not None and attempted != candidate.binding:
            return "release_binding_mismatch"
        if candidate.release_id in self.superseded:
            return "superseded"
        if delegation.delegation_id in self.revoked:
            return "authorization_revoked"
        try:
            self._authorize(candidate, delegation, now)
        except BoundaryError:
            return "authorization_unavailable"
        d = self.decisions.get(candidate.binding)
        if d is None or d.delegation_binding != delegation.binding or now >= d.expires:
            return "decision_unavailable"
        observations = [e for e in self.events if e["type"] == "observation"
                        and e["expected_binding"] == candidate.binding]
        if not observations:
            return "unobserved"
        # Even a matching historical observation is dated, not continuous monitoring.
        return "last_observation_" + observations[-1]["status"]


def fixture():
    m = PublicationModel("author", "publisher", frozenset({"verifier"}),
                         frozenset({"observer"}), "p1",
                         frozenset({"scope", "disclosure", "rights_inventory", "artifact_tests"}))
    c = Candidate("release-1", "synthetic-source-1", b"synthetic public artifact",
                  digest(b"synthetic evidence"), "p1", "research_prototype", "staging://public")
    d = Delegation("delegation-1", "publisher", frozenset({"research_prototype"}),
                   "staging://public", "p1", 0, 20)
    return m, c, d


def run_demo():
    from dataclasses import replace
    m, c, d = fixture()
    m.verify(c, d, "verifier", {k: True for k in m.required_checks}, 1, 15)
    before = m.currentness(c, d, 2)
    failed = m.publish(c, d, "publisher", 3, "fail")
    missing = m.observe(c, "observer", 4)
    delivered = m.publish(c, d, "publisher", 5)
    duplicate = m.publish(c, d, "publisher", 6)
    observed = m.observe(c, "observer", 7)
    new = replace(c, release_id="release-2", source_revision="synthetic-source-2",
                  content=b"corrected synthetic public artifact")
    m.amend(c, new, 8)
    old_status = m.currentness(c, d, 9)
    try:
        m.publish(new, d, "publisher", 10)
    except BoundaryError as e:
        new_blocked = str(e)
    m.verify(new, d, "verifier", {k: True for k in m.required_checks}, 11, 19)
    m.publish(new, d, "publisher", 12)
    m.observe(new, "observer", 13)
    m.revoke(d.delegation_id, 14)
    return {"schema": "mcrp.toy-release-cycle.v1", "synthetic": True,
            "authentication": "trusted fixture identities; no signatures",
            "before_delivery": before, "failed_attempt": failed,
            "missing_observation": missing["status"], "delivery": delivered,
            "duplicate_attempt": duplicate, "observation": observed["status"],
            "old_after_amendment": old_status, "new_without_approval": new_blocked,
            "new_after_revocation": m.currentness(new, d, 15), "events": m.events}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    out = json.dumps(run_demo(), indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(out)
    else:
        print(out, end="")
