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
input access, operator support, and domain sign-off. These are a realistic resource
shape, not measured production claims.

Only three modes are performed here: bounded recomputation of four sanitized
partitions, digest audit over those partitions, and inspection of the resulting
frozen evidence. Full independent execution and an independent evidence path are
`not-performed`. Restricted-platform attestation is `template-only`. The six modes
remain non-equivalent in `assessment-modes.json`.

## Strongest conclusion

The packet supports sampled lineage and digest-generation behavior plus bounded
aggregate invariants for the exact accessible downselect. It does not support
full-scale equivalence, partition representativeness, production convergence,
scheduler/GPU/storage behavior, attestor honesty, independent replication, or
scientific validity.
