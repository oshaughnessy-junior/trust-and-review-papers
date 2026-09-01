# Sanitized HPC/large-storage downselect fixture

This case demonstrates how an expensive or restricted partitioned-inference
workflow can expose material assessment modes without pretending that a laptop
fixture is a full reproduction. The four bundled likelihood partitions are
synthetic and contain no private, production, collaboration-internal, or LANL
material.

```bash
make verify
```

The executable path starts from exact partition values, regenerates a digest for
each partition, aggregates the likelihood on a registered parameter grid,
normalizes a posterior, and checks MAP, central-mass, and split-half invariants.
It is not a Makefile that redraws a saved final product. A corrupted high-tail
partition changes the scientific decision and must fail; a missing registered
partition fails identity before aggregation.

## Full-scale declaration versus performed modes

The unexecuted full-scale scenario declares 8192 partitions, HTCondor, 16 GPUs,
about 1800 GPU-hours, 6 TB scratch storage, 30 TB retained products, restricted
input access, operator support, and domain sign-off. These are an illustrative resource
shape, not measured production claims.

Only three modes are performed here: bounded recomputation of four sanitized
partitions, digest audit over those partitions, and inspection of the resulting
frozen evidence. Full independent execution and an independent evidence path are
`not-performed`. Restricted-platform attestation is `template-only`. The six modes
remain non-equivalent in `assessment-modes.json`. This bounded recomputation has
named identity, MAP, central-mass, split-half, and adversarial checks but no scaling,
convergence, or representativeness evidence.

## Strongest conclusion

The packet supports sampled lineage and digest-generation behavior plus bounded
aggregate invariants for the exact accessible downselect. It does not support
full-scale equivalence, partition representativeness, production convergence,
scheduler/GPU/storage behavior, attestor honesty, independent replication, or
scientific validity.

## Independent inspection history

IR001 inspected exact commit `a75d671f730ade7a0c42bf1d2cdd0aee2ae23000`
from a fresh detached same-host clone and returned a hold. It confirmed material
regeneration and honest exclusions but found that standalone replay could accept a
coherently failed record and repository validation could accept an omitted index
entry. The hold, five probes, eight independence dimensions, and required corrections
are preserved in `independent-review-2026-08-31.json`; a superseding exact-commit
reinspection was required before clearance. IR001-R1 then reviewed exact correction
commit `5f26da1e5995ff5a0b11fff664dbc82dbc430aa1` in a new detached clone,
passed 11 checks, and made coherent-failure, index-omission, and duplicate-index
probes fail. It clears the robustness hold only for this sanitized packet; every
production and scientific-independence exclusion remains.
