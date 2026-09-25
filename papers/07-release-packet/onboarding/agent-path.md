# Implement one boundary: the agent and developer path

Begin with the executable fixtures and their expected outcomes. A toy agent is
a deterministic policy acting in a simulated environment; it is not an enrolled
reviewer, authenticated service or independently responsible organization.

## What an adapter must preserve

The small external vocabulary is offer, check, rely, amend. Existing internal
workflows can remain complex. An adapter must preserve the intended use, exact
claim/evidence version, declared dependencies, check scope and result, responsible
actor, decision authority, resource assumptions, and unresolved changes.

An adapter may carry an existing DOI, repository commit, notebook, review letter
or institutional decision as a reference. It must not infer consent, signatures,
reviewer independence or scientific acceptance from a URL. Missing metadata stays
missing. Map unsupported fields to explicit unknowns and report information loss.

Try the [runnable legacy-review adapter](legacy-adapter.md) for a concrete bridge
from an existing review record to the toy runtime, including its loss report and
separate trusted-fixture enrichment.

## First implementation exercise

1. Run the supplied toy-agent scenarios and preserve the configuration, seed,
   outputs and test results.
2. Add one actor whose internal team has 100 members. Keep its accountable control
   group unchanged. Show that internal expansion alone grants no extra panel weight
   under the group-first baseline.
3. Change one evidence version after a check. Attempt the old reliance decision.
   Demonstrate the currentness/target mismatch and the new work required.
4. Reduce a scarce skill's capacity while leaving total capacity high. Show the
   unavailable or delayed outcome. Do not replace it with an unqualified checker.
5. Add one real workflow adapter using only shareable example data. Produce a
   round-trip report identifying preserved fields, missing fields and any lossy
   translations. Do not claim standards conformance from field names alone.

Consult [the toy-agent framework](../models/agent-framework.md) and its package
README for executable commands and the actual API. The prose here is a behavioral
contract; it does not introduce a second incompatible wire format.

## Two independent axes of success

| Record behavior | Scientific adequacy |
|---|---|
| Exact version survives round trip | The evidence addresses the intended claim |
| Typed check cannot become an authority grant | The person deciding is competent and authorized |
| Amendment reaches declared dependents | Relevant dependencies were actually declared |
| Resource reservation is not double spent | Capacity estimates represent real available people |
| Unknown/stale remains visible | The recipient notices and responds appropriately |

The first column can be substantially tested in a toy system. The second needs
external evidence and accountable judgment. Passing one does not establish the
other.

## Contribution package

Supply a minimal scenario, one command, expected and actual outputs, source and
environment versions, explicit assumptions, a negative control, and a short
claim ledger. Include the failed case before a proposed repair. Report all offered
tasks and unfinished work, not merely successful completions. Use synthetic
identities and local files; no network credentials are required for this prototype.

An implementation may extend the record with domain fields, but it should still
render the six-question human card. If a person cannot tell what a record means
without reading the implementation, the adapter has failed the onboarding goal.

## Toward a real service

Authentication, adversarial identity and common-control discovery, concurrency,
durable transactions, privacy, external notification, legal operations, and actual
appointment of decision makers are outside the toy runtime. Preserve these as
named unimplemented boundaries. A new profile should state its own tests and
compatibility choices instead of silently inheriting production guarantees from
this research demonstration.

For the separate future human comparison and immediate synthetic conformance
exercise, read the [pre-results evaluation plan](evaluation-plan.md). Passing
agent fixtures cannot substitute for its human outcomes.
