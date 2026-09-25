# Independent adversarial review: agent entry point

Review date: 2026-09-25. Scope: the local `agent_api` JSON/CLI surface, its four
teaching fixtures, machine-readable boundaries, and agent/public onboarding.
This review does not certify a deployed service or the final exported bytes.

**Qualified assent to public release as a local synthetic research entry point.**
The interface gives an agent a concrete first action without a human workshop.
It preserves useful refusal and version boundaries within its stated fixture.
It does not establish authentication, real decision authority, factual adequacy,
reviewer independence, or persistent resource conservation.

## Independent evidence

Run from the repository root:

```sh
python3 -m unittest discover -s papers/07-release-packet/reviews/agent-launch-red -p 'test_*.py' -v
```

All **23 independent tests pass** against the reviewed interface. These tests were
written separately from the author's suite. Three helper scope tokens were updated
from `calibration` to the author's more accurate `calibration-arithmetic` label;
no assertions were removed or weakened. Before that fixture-name alignment, three
checks failed because their requested skill no longer existed in the policy.

Separately invoking the actual CLI on physics/astronomy, biology,
economics/social science, and law produced exit0 and empty stderr for each:
12 submitted commands, 11 accepted, one intentional refusal, two offers, two
checks and two reliances. The independent tests inspect the changed exact targets,
new current reliance, and old reconsideration-pending reliance, not just counts.

The probes cover shared-principal capacity, same-control-group coverage,
unauthorized amendment, role injection, exact-version reuse, dependency/profile
identity, expiry, unavailable evidence, failed-command atomicity, duplicate keys
and IDs, strict numeric types, input limits, digest injection, non-authorizing
legacy projection, and deterministic stateless replay.

## Material defects found and repaired

1. **Amendment teaching fixtures originally renewed unchanged content.** A reason
   said the evidence changed, but the example rechecked the old offer and made it
   current again. For physics, changing an offset from 8 to 12 reverses the stated
   difference; a fresh support assertion does not repair that old positive claim.
   All four fixtures now offer changed claim/evidence content and rely on its new
   exact version. The old reliance remains pending. The CLI still cannot determine
   whether a supplied support assertion is scientifically true; the README now
   states this explicitly.
2. **Version identity originally omitted dependencies and the review contract.**
   Discovering a dependency while keeping the evidence unchanged could not create
   a distinct profile without inventing an evidence change. The profile digest
   now binds claim, evidence, scope, resolved dependency targets, and required
   group count. Independent tests hold evidence constant, vary dependencies or
   coverage, and require distinct versions with the same evidence digest. Old
   checks cannot satisfy a new exact profile.
3. **Cost and identity language needed narrower interpretation.** The entry docs
   now say that the ledger charges declared check effort per scope only. Other
   actions and administrative labor are uncharged. Agent IDs are local caller
   assertions, and the decision role is selected from a trusted synthetic policy,
   not authenticated or appointed by this tool.

## Important successful attacks against stronger claims

These are deliberately preserved limits, not hidden assurances:

- A caller can use the configured decision agent's name and receive its synthetic
  role. One passing test explicitly demonstrates this. This command must not be
  exposed as a multi-tenant authorization endpoint without new controls.
- Replaying an entire request starts a fresh state and budget. Identical results
  demonstrate deterministic replay, not durable deduplication or conservation
  across invocations.
- Aliases of one principal share capacity and do not add independent coverage.
  Different declared principals can conceal the same real people or controller;
  neither this interface nor a policy digest discovers that fact.
- A supplied method/outcome can misdescribe the world. Domain fixtures illustrate
  arithmetic and record transitions. They do not execute scientific validation,
  establish a causal effect, or decide a real legal deadline or entitlement.
- A fresh simulation timestamp is not a live observation. Correct dependency
  propagation only reaches declared dependencies. A hash proves neither their
  completeness nor the truth of the evidence.

The README and machine-readable boundaries disclose these limits close to the
entry point. Public agent-only uptake is appropriate as a reproducible contribution
loop. It should not be described as autonomous scientific governance or an enrolled
review service. A static seed needs no new legal institution merely to run synthetic
fixtures and receive ordinary owner-reviewed repository contributions.

## Onboarding and composition

The manifest, quickstart, example fixtures, and explicit refusal supply a tractable
first action. The older onboarding exercise concerning a 100-member actor and
panel weights belongs to the separate model framework: the JSON entry point has
no panel API. The author was asked to distinguish it and use two aliases sharing
one principal for the immediate CLI exercise.

The structural JSON Schema is a guide, not a substitute for executing the bounded
parser and stateful checks. In particular, generic schema integer validation does
not express every lexical numeric restriction enforced by the CLI. An external
implementation should preserve the runtime tests rather than infer conformance
from accepting the schema alone.

Passing this suite is evidence about this boundary, not composition of all papers'
conditional models into a common operational system. Final source/evidence lineage,
archive verification, site deployment, and public endpoint checks remain with the
release integrator. No additional institution-building gate is recommended for
this clearly labeled local research seed.
