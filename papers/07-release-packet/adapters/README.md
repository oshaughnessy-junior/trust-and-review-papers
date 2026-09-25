# A legacy review wrapper that refuses to invent authority

This executable example wraps **synthetic repository-issue/review-letter metadata**.
It is neither a GitHub connector nor a parser for arbitrary referee prose. It
claims no W3C PROV, RO-Crate, COAR Notify, Crossref, journal or repository-schema
conformance. It needs no account, network connection, credentials or dependencies.

From the extracted packet root (Python 3.9+ standard library):

```sh
python3 -m unittest discover -s adapters/tests -v
python3 -m adapters.demo
```

Nineteen tests pass after the adversarial adapter revision. The demo writes
`adapters/results/demo.json`, including source/fixture/test/runtime hashes, the
loss report, unchanged legacy payload, explicit enrichment, and actual toy-protocol
events. No message is sent and no real review is imported.

## What is preserved, and what is not inferred

`adapt(source)` retains a deep copy of the entire JSON-value tree, fingerprints its
canonical JSON representation, and maps a small known set of fields. `roundtrip`
checks that the envelope still matches that deterministic projection, then returns
the original JSON values. Envelope comparison uses canonical JSON bytes, not Python value equality: Boolean
`true`, integer `1`, and floating token `1.0` are distinct. Nonfinite numbers are
rejected. The guarantee covers values, **not original byte layout,
whitespace, signing bytes or ordering fidelity**. It is a one-format self-roundtrip,
not an independent implementation interoperability test.

Each mapped field has a status: `absent`, `null`, `explicit_empty`, `value`, or
`blocked_by_nonobject`. A missing dependency field, `null`, and `[]` therefore remain
different. Empty review limitations do not mean that a check had no limitations.
Unknown extension fields are preserved in the raw payload and named in the semantic
loss report; they are not silently upgraded to executable protocol assertions.

The exact claim ID, declared git object reference and declared SHA-256 evidence
reference are retained. The adapter rejects a mutable URL as its only version
reference. It validates **reference syntax and the source's explicit immutability
assertion**, not the existence of a git object, source authenticity or binding to
artifact bytes. The synthetic evidence file's digest is separately checked by a
test. A deliberate negative test shows that a well-shaped fabricated digest still
passes the adapter: that missing verification is an explicit trust boundary.

The adapter preserves check scope, declared result, method, limits and recommendation
separately. A recommendation to “accept” never supplies a missing result or overrides
contradiction. Author names, reviewer names, URLs and team members never establish
independence, skill, consent, authority or dependency completeness. Mapped legacy
authorization/control fields remain unverified data even when present.

## Two executable paths

1. **Unaugmented input:** `execute_fixture(envelope)` refuses scoped reliance because
   no trusted authority, control or dependency assertions exist. A pretty JSON wrapper
   has not made those facts true.
2. **Separately enriched synthetic demonstration:** a different fixture file explicitly
   asserts invented control groups, reviewer capabilities, decision roles, an empty
   dependency graph, purpose, exact scope, expiry, capacity and limitations. The
   adapter retains that file separately from legacy facts. It passes the declaration
   into the actual `toy_agents.Protocol` offer/check/rely/amend methods. After a
   synthetic material amendment, the old reliance reports `reconsideration_pending`.

The enriched run **does not rerun the referee's scientific method**. It records the
legacy check declaration under explicit fixture assumptions and charges synthetic
capacity. Neither the adapter nor the fixture turns a historical letter into consent,
authentication, a real editor's decision or permission to publish private material.

This narrow demo handles one target and an explicitly empty enriched dependency
graph. Nonempty legacy dependencies or nonempty authorization/control assertions
are refused for reconciliation outside the demo; they cannot be overwritten with
more convenient fixture assertions. Unknown/null dependency metadata can be enriched
only by a separately visible explicit fixture assumption. Scope widening, contradictory
checks, shared author-reviewer control and missing scientific decision roles are
rejected. The runtime's counterexamples and limitations still apply.

The public test fixture contains invented identities and `example.invalid` URLs.
Do not adapt private review letters into a public bundle without appropriate authority
and consent. This example makes no claim to implement those permissions.

See `../onboarding/legacy-adapter.md` for the corresponding six-question human card.
