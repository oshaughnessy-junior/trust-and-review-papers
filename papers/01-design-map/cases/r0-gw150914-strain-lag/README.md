# Public R0 worked case: GW150914 v2 intersite strain lag

This release candidate is a laptop-scale, scheduler-free worked example of the
Paper 01 record model. It begins with two exact, versioned public GWOSC HDF5 strain
files—not saved figure values—then checks identity and data-quality metadata,
applies a declared filter, computes an H1/L1 event-window correlation, evaluates a
necessary physical lag invariant, runs adversarial fixtures, and emits claim-scoped
evidence, lineage, environment, and all ten resource axes.

GWOSC states that this v2 release corrects a phase error in the previous 4 kHz
files. The case therefore treats version and content identity as scientifically
material. It is an immutable-source-bound **release candidate**, not an archived
release: no DOI has been minted and repository licensing remains human-gated.

## Run

Requirements: Pixi and a contemporary macOS arm64 or Linux x86-64 laptop. The lock
file pins Python, NumPy, SciPy, and h5py for both platforms. The approximately 2 MB
scientific inputs are bundled, so analysis needs no data service, account,
scheduler, or accelerator. A cold environment still needs network access or a
pre-populated package cache/mirror because locked dependencies are not vendored.

```bash
make verify
```

To create a new append-only recorded run:

```bash
make run
make verify
```

## Record topology

- `claim-manifest.json`: the one claim, frozen configuration, evidence links,
  strongest conclusion, exclusions, and `archive_status: UNMINTED`.
- `source-manifest.json`: GWOSC v2 DOI/URLs/license, sizes, SHA-256 digests, phase-
  correction note, and accepted upstream boundary.
- `data/raw/`: exact H1/L1 public strain inputs. These are calibrated external
  products, not raw interferometer telemetry.
- `run_case.py`: identity checks, HDF5 ingestion, quality/injection policy,
  filtering, correlation, invariant, negative fixtures, provenance, and resources.
- `test_case.py`: digest/version mutation, quality, scientific invariant,
  adversarial lag, clean-replay, and sign-off-boundary tests.
- `artifacts/intermediate/`: selected metadata and preprocessing configuration.
- `artifacts/derived/`: regenerated lag-correlation digested product.
- `artifacts/evidence/`: claim result and adversarial observations.
- `artifacts/provenance/`: run/environment identities and ten-axis declaration.
- `trust-boundaries.json`: reviewed-here scope, accepted external components, and
  independence limits.
- `lifecycle-events.json`: append-only release/freshness state and later-failure
  disposition requirements.
- `review-checklist.md`: separate machine, human-science, independent-custody, and
  archival controls.
- `packet-index.json`: SHA-256 inventory of the release-candidate packet (excluding
  the index itself).
- `review-signoff.json`: machine and agent scopes; human scientific sign-off is
  explicitly pending rather than fabricated.
- `independent-replay-report.json`: fresh-context detached-checkout execution,
  adversarial audit, discrepancies, and decomposed independence limits.

## Scientific scope

The registered workflow uses a fourth-order 35–350 Hz Butterworth bandpass applied
forward and backward, an 820-sample window (0.2001953125 s at 4096 Hz) centered at
GPS 1126259462.4, and normalized cross-correlation over ±40 ms. The claim requires
an absolute recovered lag no
larger than 10 ms and absolute correlation of at least 0.30. The physical bound is
necessary, not sufficient, for a common astrophysical signal.

Clean replay requires identical registered claim evidence and negative-test
decisions. Individual samples in the full derived correlation curve are compared
with declared absolute tolerances of 1 ps in lag and `1e-10` in normalized
correlation, accommodating platform-level floating-point variation without
weakening the 10 ms and 0.30 scientific decision thresholds.

The main adversarial fixture zero-pads a +25 ms L1 window shift; it must move the
best correlation outside the physical bound. Source-registry tests also reject a
v1 label or altered digest before analysis. The exact algorithms that create the
digested metrics are included and exercised during clean replay.

This packet does **not** reproduce the original search, detection significance,
calibration, parameter estimation, or astrophysical interpretation. It does not
establish independent replication or scientific validity. GWOSC calibration,
quality flags, event curation, and HDF5 construction; Pixi/conda-forge; CPython;
NumPy; SciPy; h5py/HDF5; the OS; and CPU math libraries are declared transitive
trust boundaries rather than silently treated as reviewed here.

## Freshness and later failure

The initial source retrieval is dated 2026-08-27. The resource record requests a
clean replay by 2026-11-27. Any source drift, dependency failure, numerical
discrepancy, or invariant failure must append a `stale` or `reproduction-failed`
event and a superseding run; this passing record must not be overwritten.

The first Linux CI replay did exactly that: exact string equality for the full
correlation curve failed despite matching claim and negative-test records. The
failure and remediation are retained in `lifecycle-events.json`. Declared
scientifically negligible floating-point tolerances replaced undeclared bytewise
numeric equality; subsequent Linux and macOS checks passed without changing the
claim thresholds or pending human-review disposition.
