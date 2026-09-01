# Independent sanitized HPC downselect review — IR001

Review target: exact commit
`a75d671f730ade7a0c42bf1d2cdd0aee2ae23000` in a fresh detached, no-hardlinks
clone on the same host.

Disposition: **HOLD_PENDING_VERIFIER_CORRECTIONS**.

The reviewer confirmed that the exact packet begins from four registered synthetic
partitions, regenerates per-partition summaries and the aggregate posterior, has a
complete and matching 21-entry index at that commit, and passes its baseline nine
tests and clean replay. The claim exclusions correctly withhold production
representativeness, full execution, restricted attestation, independent replication,
and scientific validity.

Two material robustness defects blocked clearance:

1. standalone replay could accept coherently recorded failed invariants; and
2. repository validation could accept an omitted packet-index entry.

The review also required the bounded-recomputation definition to stop implying
unperformed scaling or representativeness checks, exact-looking rounded values to
be qualified, and unsupported realistic/zero-cost resource language to be removed.
The full structured record in `independent-review-2026-08-31.json` preserves five
adversarial probes and eight decomposed independence dimensions. Fresh checkout and
executor context were only limited forms of separation; implementation, inputs,
libraries, institution, scientific judgment, and method were not independent.

This report is review evidence, not scientific approval. Corrections require a new
exact-commit replay before the robustness gate can clear.
