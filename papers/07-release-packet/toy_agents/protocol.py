"""Deterministic bounded-reliance simulator. Trusted fixtures, not a service."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from itertools import combinations
import copy
import random
from typing import Iterable


class Rejected(ValueError):
    """A declared toy policy prevented an action; not a legal/scientific verdict."""


def units(value: int, *, zero: bool = False) -> int:
    if type(value) is not int or value < (0 if zero else 1):
        raise Rejected('effort/time must be an integer in the declared range')
    return value


def scope_set(value):
    if isinstance(value, str):
        raise Rejected('scope must be a collection, not a bare string')
    result = frozenset(value)
    if any(not isinstance(v, str) or not v.strip() for v in result):
        raise Rejected('scope labels must be nonempty strings')
    return result


@dataclass(frozen=True, order=True)
class Target:
    claim_id: str
    version: str
    evidence_digest: str

    def __post_init__(self):
        if not all(isinstance(x, str) and x.strip() for x in asdict(self).values()):
            raise Rejected('target fields must be nonempty strings')


@dataclass(frozen=True)
class Actor:
    actor_id: str
    control_group: str
    skills: frozenset[str]
    roles: frozenset[str] = frozenset()
    internal_size: int = 1

    def __post_init__(self):
        if not all(isinstance(v,str) and v.strip() for v in (self.actor_id,self.control_group)):
            raise Rejected('actor and accountable control group required')
        for field in ('skills','roles'):
            value=getattr(self,field)
            if isinstance(value,str) or any(not isinstance(v,str) or not v.strip() for v in value):
                raise Rejected('roles and skills require collections of nonempty strings')
            object.__setattr__(self,field,frozenset(value))
        units(self.internal_size)


@dataclass(frozen=True)
class Offer:
    record_id: str
    target: Target
    author_id: str
    scope: frozenset[str]
    dependencies: tuple[Target, ...]
    required_groups: int = 1


@dataclass(frozen=True)
class Check:
    record_id: str
    offer_id: str
    reviewer_id: str
    scope: frozenset[str]
    method: str
    outcome: str
    limits: str
    generations: tuple[tuple[Target, int], ...]
    completed_at: int


@dataclass(frozen=True)
class Reliance:
    record_id: str
    offer_id: str
    decision_maker: str
    check_ids: tuple[str, ...]
    purpose: str
    scope: frozenset[str]
    kind: str
    expires: int
    issued_at: int
    required_groups: int
    generations: tuple[tuple[Target, int], ...]


class Ledger:
    """One epoch. Reservation charged once; completion does not refund spent work.

    Both person-total and person-skill constraints hold. Multiple account labels
    sharing a real person must map to that person's *same* capacity key upstream.
    Here actor IDs are capacity keys, so hidden overlapping membership is unmodeled.
    """
    def __init__(self, person_capacity, skill_capacity):
        self.person_capacity = dict(person_capacity)
        self.skill_capacity = dict(skill_capacity)
        for value in [*self.person_capacity.values(), *self.skill_capacity.values()]:
            units(value, zero=True)
        self.reservations: dict[str, tuple[tuple[str, str, int], ...]] = {}
        self.spent: set[str] = set()

    def totals(self):
        p, s = {}, {}
        for entries in self.reservations.values():
            for actor, skill, amount in entries:
                p[actor] = p.get(actor, 0) + amount
                s[actor, skill] = s.get((actor, skill), 0) + amount
        return p, s

    def reserve(self, reservation_id, entries):
        if reservation_id in self.reservations:
            raise Rejected('reservation already exists')
        entries = tuple(entries)
        if not entries:
            raise Rejected('empty reservation')
        p, s = self.totals()
        for actor, skill, amount in entries:
            units(amount)
            p[actor] = p.get(actor, 0) + amount
            s[actor, skill] = s.get((actor, skill), 0) + amount
        if any(v > self.person_capacity.get(k, 0) for k, v in p.items()):
            raise Rejected('person capacity unavailable')
        if any(v > self.skill_capacity.get(k, 0) for k, v in s.items()):
            raise Rejected('skill capacity unavailable')
        self.reservations[reservation_id] = entries

    def consume(self, reservation_id):
        if reservation_id not in self.reservations or reservation_id in self.spent:
            raise Rejected('reservation missing or already consumed')
        self.spent.add(reservation_id)

    def cancel(self, reservation_id):
        if reservation_id in self.spent:
            raise Rejected('spent work cannot be refunded')
        if reservation_id not in self.reservations:
            raise Rejected('unknown reservation')
        del self.reservations[reservation_id]


def sample_panel(actors: Iterable[Actor], skill: str, seats: int, excluded_groups=(), seed=0):
    """Uniform over canonical feasible group sets, then one representative/group.

    Static skill/conflict eligibility only; caller must reserve the complete panel
    jointly. No retries or capacity-conditioned distribution guarantee is made.
    """
    units(seats)
    actors = tuple(actors)
    if len({a.actor_id for a in actors}) != len(actors):
        raise Rejected('duplicate actor identifier')
    groups = {}
    for a in actors:
        if skill in a.skills and a.control_group not in excluded_groups:
            groups.setdefault(a.control_group, []).append(a.actor_id)
    panels = tuple(combinations(sorted(groups), seats))
    if not panels:
        raise Rejected('coverage unavailable')
    rng = random.Random(seed)
    chosen = rng.choice(panels)
    return tuple(rng.choice(sorted(groups[g])) for g in chosen)


class Protocol:
    def __init__(self, actors, person_capacity, skill_capacity):
        actor_list = tuple(actors)
        self.actors = {a.actor_id: a for a in actor_list}
        if len(self.actors) != len(actor_list):
            raise Rejected('duplicate actor identifier')
        self.ledger = Ledger(person_capacity, skill_capacity)
        self.offers: dict[str, Offer] = {}
        self.checks: dict[str, Check] = {}
        self.reliances: dict[str, Reliance] = {}
        self.generations: dict[Target, int] = {}
        self.dependencies: dict[Target, tuple[Target, ...]] = {}
        self.available: dict[Target, bool] = {}
        self.events: list[dict] = []
        self.degraded = False
        self.clock = 0

    def _actor(self, actor_id):
        if actor_id not in self.actors:
            raise Rejected('unknown actor')
        return self.actors[actor_id]

    def _time(self, now):
        units(now, zero=True)
        if now < self.clock:
            raise Rejected('backdated action or historical query unsupported')

    def _id(self, prefix):
        return f'{prefix}-{len(self.events)+1:04d}'

    def _closure(self, target):
        seen, stack = set(), [target]
        while stack:
            t = stack.pop()
            if t not in seen:
                seen.add(t)
                stack.extend(self.dependencies.get(t, ()))
        return seen

    def _snapshot(self, target):
        return tuple(sorted((t, self.generations[t]) for t in self._closure(target)))

    def offer(self, target, author_id, scope, dependencies=(), required_groups=1):
        units(required_groups)
        if self.degraded:
            raise Rejected('degraded: new discretionary offers paused')
        self._actor(author_id)
        scope = scope_set(scope)
        dependencies = tuple(dependencies)
        if not scope:
            raise Rejected('explicit nonempty scope required')
        if target in self.dependencies:
            raise Rejected('exact target already offered')
        if any(t not in self.generations for t in dependencies):
            raise Rejected('dependency must already be offered')
        oid = self._id('offer')
        self.offers[oid] = Offer(oid, target, author_id, scope, dependencies, required_groups)
        self.dependencies[target] = dependencies
        self.generations[target] = 0
        self.available[target] = True
        self.events.append({'action':'offer', 'id':oid, 'target':asdict(target)})
        return oid

    def check(self, offer_id, reviewer_id, scope, method, outcome, limits, units=1, now=0):
        self._time(now)
        o = self.offers[offer_id]
        a = self._actor(reviewer_id)
        scope = scope_set(scope)
        if not scope or not scope <= o.scope or not scope <= a.skills:
            raise Rejected('check scope outside offer or reviewer capability')
        if a.control_group == self.actors[o.author_id].control_group:
            raise Rejected('author-control conflict')
        if outcome not in {'support', 'contradiction', 'unknown'} or not method or not limits:
            raise Rejected('explicit outcome, method and limitations required')
        if any(not self.available[t] for t in self._closure(o.target)):
            raise Rejected('dependency evidence unavailable')
        cid = self._id('check')
        # Effort charged once per checked skill; explicit units per skill.
        self.ledger.reserve(cid, [(reviewer_id, s, units) for s in sorted(scope)])
        self.ledger.consume(cid)
        self.clock = now
        self.checks[cid] = Check(cid, offer_id, reviewer_id, scope, method, outcome,
                                  limits, self._snapshot(o.target), now)
        self.events.append({'action':'check', 'id':cid, 'outcome':outcome, 'now':now})
        return cid

    def check_panel(self, requests):
        """All-or-none in this serial simulator; no concurrent transaction claim.

        Requests are keyword dictionaries accepted by check(). Validation and
        complete resource reservation occur on a detached state before commit.
        """
        trial = copy.deepcopy(self)
        ids = tuple(trial.check(**request) for request in requests)
        if not ids:
            raise Rejected('empty panel')
        self.__dict__.update(trial.__dict__)
        return ids

    def rely(self, offer_id, decision_maker, check_ids, purpose, scope, kind,
             expires, now=0, required_groups=None):
        self._time(now); units(expires)
        if self.degraded:
            raise Rejected('degraded: new discretionary reliance paused')
        o = self.offers[offer_id]
        a = self._actor(decision_maker)
        required_groups = o.required_groups if required_groups is None else required_groups
        units(required_groups)
        if required_groups < o.required_groups:
            raise Rejected('reliance cannot weaken offered coverage contract')
        if kind not in {'scientific', 'publication'} or kind not in a.roles:
            raise Rejected('missing typed decision authority')
        scope, check_ids = scope_set(scope), tuple(check_ids)
        if not purpose or not scope or not scope <= o.scope or expires <= now:
            raise Rejected('bounded purpose, scope and future expiry required')
        if len(set(check_ids)) != len(check_ids):
            raise Rejected('duplicate check IDs cannot multiply evidence')
        if any(not self.available[t] for t in self._closure(o.target)):
            raise Rejected('dependency evidence unavailable')
        records = [self.checks[c] for c in check_ids]
        if any(c.offer_id == offer_id and c.outcome == 'contradiction' and
               c.generations == self._snapshot(o.target) and c.scope & scope
               for c in self.checks.values()):
            raise Rejected('current contradictory check requires explicit amendment/recheck')
        if any(c.offer_id != offer_id or c.outcome != 'support' or
               c.generations != self._snapshot(o.target) or c.completed_at > now
               for c in records):
            raise Rejected('checks mismatch target, outcome, current generation or time')
        # Every scope item gets required distinct groups, not just the union.
        for s in scope:
            groups = {self.actors[c.reviewer_id].control_group for c in records if s in c.scope}
            if len(groups) < required_groups:
                raise Rejected('insufficient independent scope coverage')
        rid = self._id('rely')
        self.clock = now
        self.reliances[rid] = Reliance(rid, offer_id, decision_maker, check_ids,
            purpose, scope, kind, expires, now, required_groups, self._snapshot(o.target))
        self.events.append({'action':'rely', 'id':rid, 'kind':kind, 'now':now})
        return rid

    def amend(self, target, reason, now=0):
        self._time(now)
        if target not in self.generations or not reason:
            raise Rejected('known exact target and explicit reason required')
        self.clock = now
        self.generations[target] += 1
        affected = sorted(t for t in self.generations if target in self._closure(t))
        self.events.append({'action':'amend', 'target':asdict(target), 'reason':reason,
                            'now':now, 'affected':[asdict(t) for t in affected]})
        return affected

    def set_available(self, target, available):
        if target not in self.available or type(available) is not bool:
            raise Rejected('known target and Boolean availability required')
        self.available[target] = available
        self.events.append({'action':'availability', 'target':asdict(target), 'available':available})

    def currentness(self, reliance_id, now, observed_at, max_age):
        self._time(now); units(max_age, zero=True)
        r = self.reliances[reliance_id]
        if now < r.issued_at:
            raise Rejected('query precedes reliance')
        if observed_at is not None:
            units(observed_at, zero=True)
            if observed_at > now:
                raise Rejected('future observation')
        self.clock = now
        if now >= r.expires:
            return 'expired'
        if observed_at is None or now - observed_at > max_age:
            return 'freshness_unknown'
        target = self.offers[r.offer_id].target
        if any(not self.available[t] for t in self._closure(target)):
            return 'dependency_unavailable'
        if r.generations != self._snapshot(target):
            return 'reconsideration_pending'
        if any(c.offer_id == r.offer_id and c.outcome == 'contradiction' and
               c.generations == r.generations and c.scope & r.scope
               for c in self.checks.values()):
            return 'contradiction_pending'
        return 'current_under_toy_policy'

    def enter_degraded(self, reason):
        if not reason:
            raise Rejected('reason required')
        self.degraded = True
        self.events.append({'action':'degraded', 'reason':reason})


@dataclass(frozen=True)
class PolicyAgent:
    """A scripted actor, never an independent source of scientific truth."""
    actor_id: str
    outcome: str = 'support'

    def act(self, protocol, offer_id, scope, now=0):
        return protocol.check(offer_id, self.actor_id, scope,
            method='scripted fixture policy', outcome=self.outcome,
            limits='No empirical or scientific validation; trusted synthetic inputs.', now=now)
