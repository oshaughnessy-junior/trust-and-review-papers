# Public RIFT production-system mapping v0.1

Status: **documentary mapping only; no RIFT execution or production validation**  
Recorded: 2026-09-02

This note tests whether the sanitized fixture can be compared to a named public
computational workflow without inflating a small synthetic rerun into production
evidence. RIFT is the representative public system because its published purpose
and documentation expose the scientific and operational layers that the fixture
deliberately omits.

## Source-bounded RIFT structure

The original RIFT paper introduces an iterative parameter-inference algorithm and
validates reported results against LALInference; it also motivates costly waveform
models (arXiv:1805.10457). The public project documentation separates an initial
intrinsic grid, parallel ILE marginalized-likelihood evaluations, CIP likelihood
fitting and posterior sampling, iterative feedback, and convergence testing. Its
pipeline guide additionally records PSD/grid and configuration inputs, HTCondor
submit files and a DAG, per-iteration logs, likelihood consolidation, posterior
products, and recommended CUDA/CuPy support. A separate primary paper reports GPU
acceleration of parts of RIFT (DOI 10.1103/PhysRevD.99.084026).

Authoritative project pages checked on 2026-09-02:

- <https://rift-documentation.readthedocs.io/en/latest/overview.html>
- <https://rift-documentation.readthedocs.io/en/latest/using-pipeline.html>

These `latest` pages are mutable dependencies. Their relevant claims must be
rechecked at the case freshness date; this packet does not treat them as an
immutable release.

## Narrow correspondences

| Public RIFT layer | Fixture element | What the correspondence does **not** show |
|---|---|---|
| event/configuration, PSD, and initial grid | fixed five-point grid and exact synthetic partition identities | no strain, PSD, calibration, event setup, waveform, or RIFT initialization |
| HTCondor DAG, submit files, iteration directories, and logs | one local Make target and direct Python command | no DAG construction, scheduler execution, retries, recovery, or log-lineage audit |
| parallel ILE marginalized-likelihood evaluations | four synthetic likelihood arrays | arrays are not ILE products; no Monte Carlo marginalization or waveform-data comparison |
| consolidated likelihood files and provenance | regenerated argmax/log-sum-exp digests bound to source hashes | digest is an audit toy, not a RIFT composite product or production algorithm |
| CIP fitting, posterior sampling, and iterative feedback | sum likelihoods and normalize a fixed-grid posterior | no fit, sample generation, adaptive grid, feedback, or iteration |
| convergence and output diagnostics | MAP, central-mass, split-half, identity, and negative tests | local invariants are not RIFT convergence tests or output-format validation |
| optional/strongly recommended GPU execution | separate declared full-scale and observed-local resource fields | no GPU execution, equivalence, throughput, or measured RIFT resource envelope |

The correspondence is therefore useful as a **gap map**. It identifies the
scientific products, transitive tools, operational records, and expert judgments a
credible RIFT review would have to cover. It does not establish that the fixture is
a reduced RIFT run or that its four partitions are representative.

## Protocol disposition

No assessment-mode status changes. Bounded recomputation, digest audit, and
frozen-output inspection remain performed only on the four sanitized synthetic
partitions. Full independent execution and an independent evidence path remain
`not-performed`; restricted-platform attestation remains `template-only`.

The values 8192 partitions, 16 GPUs, 1800 GPU-hours, 6 TB scratch, and 30 TB
retained storage remain an illustrative stress shape chosen for the protocol
fixture. They are not measured, literature-derived, or claimed as RIFT
requirements.

## Next evidence gate

The mapping must not be promoted until a public RIFT example is executed under a
separately recorded custody path, or a qualified reviewer supplies domain
inspection and measured resource/lineage evidence. Any restricted-platform
attestation remains a different, explicitly governed assessment mode.
