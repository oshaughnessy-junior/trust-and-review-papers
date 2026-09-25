# Toy agents: an executable offer/check/rely/amend boundary

These are **scripted policies over synthetic fixtures**, not LLMs, independent
reviewers, authenticated services or scientific fact checkers. The point is to
make the proposed boundary falsifiable: a counterexample should be easy to write.
A team of one or a thousand internals exposes the same accountable actor record.

From `papers/07-release-packet`:

```sh
python3 -m unittest discover -s toy_agents/tests -v
python3 -m toy_agents.run --seed 17 --output toy_agents/results/demo.json
```

Python 3.9+ and standard library only. No network, credentials, external dataset,
GPU, package installation or model inference. Nineteen test methods cover the current runtime, including adversarial repairs. The checked-in result records Python version, seed,
configuration and source hashes. Re-running on another Python version can change
random samples; the deterministic arithmetic claims do not depend on the sample.

## A small reusable API

```python
from toy_agents import Actor, Target, Protocol, PolicyAgent

actors = [
    Actor('author', 'collaboration', frozenset(), internal_size=100),
    Actor('checker', 'other-lab', frozenset({'numerics'})),
    Actor('editor', 'journal', frozenset(), frozenset({'scientific'})),
]
p = Protocol(actors,
             person_capacity={'checker': 4},
             skill_capacity={('checker', 'numerics'): 4})
o = p.offer(Target('figure-2', 'v1', 'fixture:table-1'),
            'author', {'numerics'})
c = PolicyAgent('checker').act(p, o, {'numerics'})
r = p.rely(o, 'editor', [c], purpose='reproduce plotted values',
           scope={'numerics'}, kind='scientific', expires=10)
assert p.currentness(r, now=1, observed_at=1, max_age=1) == 'current_under_toy_policy'
p.amend(p.offers[o].target, 'table corrected', now=2)
assert p.currentness(r, now=2, observed_at=2, max_age=1) == 'reconsideration_pending'
```

`fixture:` identifiers above are deliberate placeholders. The simulator binds to
exact tuples but **does not calculate or authenticate artifact content digests**.
The actor registry's roles, skills and control groups are trusted input assertions.
Calling a decision `scientific` does not turn a toy agent into a scientist.

The API accepts scope as a collection of explicit skill labels. A check charges
`units` for **each** skill in its scope. Effort units are integer tokens chosen by
the fixture author, not measured hours. One epoch spans the entire Protocol object.
Every reservation is bounded simultaneously by total person capacity and the
person-skill capacity; completed work remains charged. `Ledger.cancel` releases
only unspent reservations. A new epoch requires a new ledger, with carried
obligations explicitly accounted upstream.

`check_panel(requests)` is an all-or-none serial operation: it validates a detached
copy before committing checks and reservations. This is not a database transaction
or concurrency implementation. `sample_panel` chooses control groups first, then
representatives. It models static skill/conflict eligibility. It does **not**
condition its group distribution on capacity, completion or retries. If the sampled
panel cannot be jointly reserved, callers must report unavailable rather than
silently resample and inherit the original distribution claim.

Checks are support/contradiction/unknown. Unknown is not support. Current contradictory
checks overlapping the requested scope block a new reliance even if the caller omits
those check IDs. This deliberately conservative fixture rule does not implement a
scientific adjudication system. An amendment followed by new checks can support a
new reliance; the historical record remains about its old generation.

A scientific reliance requires the toy `scientific` role; publication authorization
requires the separate `publication` role. Every scope item needs the requested
number of distinct reviewer groups. Author-controlled review is rejected. These
are minimal **declared** control constraints, not a full conflict-of-interest
policy. There is no actor registry enrollment, group discovery or appeal tribunal.

## Scenarios and what they actually demonstrate

| Scenario | Comparison / challenge | Bounded result |
|---|---|---|
| `release_cycle` | Exact check, wrong authority, source amendment, recheck, degraded intake | Old check cannot renew changed dependencies; new authorized checks can renew; historical receipt preserved |
| `capacity_failure` | One expert shared across review and appeal vs separate lane accounting | 3 + 2 tokens cannot fit capacity 4, despite each lane independently fitting |
| `selection_attack` | Representative-pair lottery vs canonical-group lottery | 100 declared clones change naive group A selection to 200/201; canonical static group probability stays 2/3 |
| `completion_bias` | Offered vs completed populations | Scripted risky completion 1 vs safe .01 can yield about .917 risky completions from .1 risky offers |
| `hidden_dependency` | Declared graph vs fixture author's known missing edge | The simulator reports current while an omitted dependency changed; this is an expected exposed failure |

The completion experiment records offered, eligible, invited, accepted, completed,
refused, unresolved, relied and retries separately. Here acceptance immediately
completes by definition; refused requests are unresolved. There are no retries or
issued reliance decisions. Its one token per invitation also charges refused work.
Zero retries and reliance are properties of this scenario, not service-wide
guarantees.

## Currentness and deliberate nonclaims

The engine checks receipt-relative dependency generations, evidence availability,
expiry and caller-supplied observation age. Its result is an ordered single-status
projection; `expired` takes precedence over stale evidence or pending amendment.
This does not erase other causes, which remain inspectable in state. The caller
supplies the observation timestamp: there is **no live freshness witness**. The
latest known state is consulted conservatively even if the observation timestamp
is older. The engine is not a historical database query at `observed_at`. Timed actions must be
nondecreasing; historical queries before the latest timed event are rejected.

An amendment follows only already-declared dependencies. No missing-edge detector,
scientific truth oracle, signed identity, real capacity measurement, overlapping
person/team membership resolver, confidentiality boundary, deadline scheduler,
rights adjudicator, legal compliance or delivery observation is implemented.
Actor IDs are the capacity keys: two IDs for the same person would double-count
capacity unless consolidated upstream. Internal team size does not multiply
reviewer independence, but the simulator does not discover common team membership.

The state is ordinary mutable Python data in a trusted process. Calling methods
cannot secure the process against hostile code that edits dictionaries directly.
A prototype client can explore the records immediately; public operational claims
would require different infrastructure, governance and evidence.

Use the counterexamples to improve or reject a mechanism. Do not rename a green
synthetic assertion as scientific validation.
