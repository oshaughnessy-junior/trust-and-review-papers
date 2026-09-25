# Start an agent on one bounded task

This is the initial agent entry point for the MCRP research seed. It accepts a
local JSON task and returns machine-readable accepted records or refusals. No
human onboarding session, account or network service is needed. Python3.9+ and
the standard library are sufficient.

From the repository root:

```sh
python3 papers/07-release-packet/agent_api/cli.py \
  --policy papers/07-release-packet/agent_api/examples/policy.json \
  --request papers/07-release-packet/agent_api/examples/physics_astro.json
```

Read [manifest.json](manifest.json) for machine discovery, the
[request schema](request.schema.json) for structure, and the four complete JSON
fixtures under `examples/`. Relative paths in the manifest are relative to this
directory unless labeled as repository-root commands. The CLI never fetches the
schema URL or any URL in an evidence record.

Each example should return `completed_with_refusals`: **12 submitted commands,
11 accepted, one intentional stale-check refusal**, two exact offers, two checks
and two scoped reliance records. The material correction supplies genuinely
changed claim/evidence content and a new version. The new version's reliance is
current under the fixture while the old reliance remains reconsideration-pending.
A new support assertion does not silently repair old scientific content.

The four examples cover calibration arithmetic for physics/astronomy, an assay
mean for biology, a completion denominator for economics/social science, and a
fictional event ordering for law. These are small calculations, not domain
validation, biological efficacy, causal estimates or legal advice. The check
method and result are **caller assertions**; this CLI does not execute a scientific
analysis or establish that the assertion is true.

## The small interface

A task contains `schema`, `synthetic_fixture: true`, `task_id` and `commands`.
Each command has an immutable local `id`, an `action`, asserted `agent_id`, integer
simulation `now`, and `input`. The four main actions are offer, check, rely and
amend. Observe queries a receipt's local currentness. Availability records a local
evidence-access condition. Adapt_legacy exposes the existing adapter's explicitly
non-authorizing projection and loss report.

| Action | Input | Result |
|---|---|---|
| `offer` | Claim ID/text, inline evidence object, scope, dependency offer aliases, required groups | Exact target and offer record |
| `check` | Offer alias, scope, method/outcome/limits, units | Bounded check assertion or refusal |
| `rely` | Offer and check aliases, purpose, scope, kind, expiry | Separately typed fixture reliance or refusal |
| `amend` | Offer alias and reason | Old target generation changes; declared dependents become affected |
| `observe` | Reliance alias, observation time or null, maximum age | Local currentness state |
| `availability` | Offer alias, Boolean availability, reason | Declared local evidence-access condition |
| `adapt_legacy` | Inline legacy source object | Loss report; creates no offer, check or authority |

Command aliases are local to one batch, unique and type checked. Only successful
offer/check/rely commands create referenceable records. A failed future-dated
command cannot advance the clock, consume check capacity or create an alias.
Successful commands commit one at a time; earlier successful commands are retained
when a later command is refused. This is a serial in-memory transaction boundary,
not concurrent storage or durable delivery.

## Agent identity, principal and control are different

The separate trusted policy file maps agent IDs to principals, and principals to
control groups, skills, roles, operations and declared check budgets. The example
`review-agent` and `review-team-child` share one principal. Both debit the same
principal's check-effort budget, and they do not become two independent control
groups. Two different principals may also share a control group and therefore not
supply independent scope coverage.

The policy is selected by the trusted local caller. **This is not a multi-tenant
server**: a request's agent ID is an assertion, not an authenticated credential.
A caller that supplies the decision agent's ID is choosing that synthetic role.
Do not expose this command as a public authorization service. The role named
`scientific` does not appoint a scientist, and `publication` does not grant real
publication permission. A new policy file is a new set of assumptions, not
independent evidence that the actor deserves those roles.

A principal is the fixture's capacity/authority key, not automatically a real
person or institution. Actual overlapping people across distinct principals,
hidden common control and inaccurate qualification declarations remain unmodeled.
Internal agent-team expansion alone supplies no new principal or control group.

## Version and scope semantics

`target.version` is a SHA-256 digest of the canonical offer profile: claim ID/text,
evidence object, sorted scope labels, resolved dependency targets and required
group count. `target.evidence_digest` separately hashes the evidence object. JSON
Boolean, integer and floating-number values remain distinct in the canonical
representation. This is the repository adapter's deterministic JSON convention,
not a claim of standards-level canonical JSON or cryptographic signatures.

Consequently, corrected evidence gets a new target version. Correcting a dependency
or check contract can also get a new profile version **without falsifying a change
in evidence bytes**. Re-offering the identical profile in one batch is refused.
Changing profile metadata does not resolve an earlier reliance record automatically;
old and new targets remain distinct. Hashes bind supplied bytes and metadata, not
scientific truth or completeness of the declared dependency graph.

Existing check scope cannot be broadened into a new use, duplicate checks cannot
multiply coverage, and a reliance cannot lower its offer's coverage floor. A new
offer's floor is still an author-selected fixture contract, not a proof that the
floor is scientifically sufficient. The offering principal alone may amend or
change availability for its target under this narrow profile.

## Refusals, limits and provenance

With valid CLI arguments, stdout is one JSON object. Exit0 means the batch was
processed, including any ordinary per-command refusals. Exit2 means a local input
or envelope was invalid. `--help` and command-line usage errors follow ordinary
argument-parser conventions. Requests may come from a named local file or stdin
with `--request -`. No state is persisted between runs.

Inputs are limited to 256KiB each, depth16, 10,000 JSON nodes, 64 commands,
16 principals, 32 agent aliases, 128 array items and 4,096-character strings.
Duplicate JSON keys, nonfinite numbers, oversized numeric tokens, unknown schema
fields and Boolean values used as integer time/effort are rejected. No panel
combination enumeration, arbitrary code, subprocess, remote evidence lookup,
credential use or network operation is exposed.

The ledger charges **declared check effort per checked scope** using the existing
runtime. Offer, reliance, amendment, observation, adaptation and administrative
labor are not charged. A bounded command count is not a measured compute or human
cost guarantee. The separate coupled models study broader participation costs.
Currentness uses the supplied simulation clock and local state; a fresh timestamp
is not a live evidence observation or delivery receipt.

Each result includes request and trusted-policy digests, accepted/refused command
counts, a complete bounded runtime-state summary and a state digest. These make
replays comparable; they are not signatures or transferable external approvals.
The result's `boundaries` object stays machine-readable so an agent can retain
these limitations with any derived artifact.

## First useful contribution

Run the four supplied cases. Then modify one example to break one claimed
property: give two aliases one small capacity, attempt to reuse a stale check,
change a scope, hide a dependency, or replace a decision role with a reviewer.
Keep the original request, mutation, actual response and a short explanation.
A useful contribution is a reproducible counterexample or an adapter that preserves
these boundaries, not a new “trust score” without a test.

```sh
python3 -m unittest discover -s papers/07-release-packet/agent_api/tests -p 'test_*.py' -v
python3 papers/07-release-packet/agent_api/build_examples.py
```

Seventeen author tests cover these boundaries; independent launch review lives in
`../reviews/agent-launch-red/`. The example result manifest records imported runtime
and adapter source hashes as well as local source hashes. Submit a proposed patch
or issue through the repository's ordinary owner-reviewed contribution process.
This CLI never posts an issue, opens a PR, enrolls anyone or publishes anything.
