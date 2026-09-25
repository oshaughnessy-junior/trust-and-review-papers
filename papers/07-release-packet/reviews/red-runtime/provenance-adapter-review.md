# Third-wave review: evidence lineage, adapter types and publication sequences

**Internal AI adversarial review, 25 September 2026.** This supplements the first
runtime and integration reports. It is not an independent institutional audit.
The final candidate's bytes were not frozen when this report was written.

## New findings

**RR-13 — P2, saved evidence was not bound to model validation.** The initial
validation manifest named Python sources, CSV tables and test logs, but omitted
JSON traces/oracles and figures. Editing a saved result after a passing run and
rebuilding could create a self-consistent export with an unrelated `passed=true`
record. Export integrity alone says what bytes were packaged, not which bytes
were the recorded results. Source hashes were also captured only after commands,
allowing a concurrent edit to appear as tested source.

The author added a before/after source-and-fixture inventory, an evidence inventory
covering generated JSON and figures, and export verification of validation,
source-copy and figure-lineage references. A further omission of the adapter's
actual evidence text fixture was identified and corrected. Five independent
regressions verify that a post-validation JSON or SVG edit followed by a rebuild
fails verification, that mid-run source or fixture mutation marks validation
failed, and that the evidence text is an input. These use a miniature packet and
stub commands: they test binding machinery, not scientific correctness. Final
full-model reproduction and final candidate verification remain separate gates.

**RR-14 — P2, JSON Boolean/integer confusion upgraded a legacy assertion.** Set
raw `claim.immutable_refs` to integer `1`: the adapter correctly refused execution.
Change only its projected value to Boolean `true`: the original `roundtrip`
accepted the envelope because Python nested equality equates `True` and `1`.
Execution then accepted the literal Boolean flag. The source hash and raw source
still recorded the integer. This violated the adapter's deterministic projection
boundary without forging any source hash or institutional credentials.

The author replaced ordinary equality with canonical JSON-byte equality.
`test_adapter_boundary.py` independently verifies rejection of the same mutation.
The original observed sequence is recorded in `adapter-baseline.json`. The repair
preserves the intended distinction among Boolean, integer and floating tokens;
it does not authenticate the legacy source or verify a referenced artifact's
bytes. A well-shaped fabricated digest remains an explicitly documented negative
control, not a security feature supplied by this repair.

## Publication sequences that survived challenge

Four additional tests exercise combinations beyond field-by-field mutation:

- A `missing` observation made before delivery remains the **last dated observation**
  until a new observation occurs. Delivery alone does not upgrade it.
- A matching observation after decision expiry does not revive publication
  authority; currentness remains `decision_unavailable`.
- An observation for wrong evidence metadata reports binding mismatch without
  poisoning a prior correctly bound receipt for the actual candidate.
- An initially tampered stored delivery cannot be silently overwritten by an
  idempotent repeat. Recovery through a new release ID requires a new decision,
  a new observation and an explicit amendment edge.

These sequences pass. The model is deliberately narrow: it is not a remote
transport repair implementation or continuous monitoring system. Outstanding
work reservations also have no wall-clock lease or automatic stale-reservation
reaper. They live in an explicit synthetic epoch until settled or cancelled.
A claim of deadline-aware availability or recovery would require a new model.

## Composition and reproducibility limits

The legacy adapter actually calls the adjacent toy protocol under separate,
explicit synthetic enrichment. It does **not** make the coupled or ecology
simulators implementations of that runtime. Its one-target fixture starts a new
protocol instance per run; repeating the demo is not a persistent shared-capacity
service. An external appointment, consent, identity assertion or actual review
method is never supplied by passing a metadata roundtrip test.

Core reproduction uses Python's standard library. The new export regressions use
a deterministic renderer stub, avoiding an accidental Pandoc dependency in the
core suite. Actual HTML rendering requires optional Pandoc; scientific figure
regeneration requires optional Matplotlib and is distinct from rerunning model
arithmetic. Byte inventories bind saved outputs but do not establish that their
interpretation is correct, or defend against a hostile trusted process.

## Status

At this review checkpoint, **23 runtime red regression methods pass**: thirteen
from earlier rounds, four publication sequences, one adapter type-confusion
regression and five evidence-binding regressions. The checked-in log is
`third-wave-test-log.txt`. This count is included in, not additional to, the full
packet's aggregate count. No exact final-export certificate is issued here.

I continue to support release of the repaired package as an explicitly synthetic,
inspectable research seed, conditional on the final ZIP and rendered candidate
passing the agreed integrity, lineage and clean-extraction reproduction checks.
