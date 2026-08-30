# Sanitized HPC downselect review checklist

## Machine-observed

- [x] Four sanitized source partitions have exact identities.
- [x] The released algorithm regenerates per-partition digests from source values.
- [x] Aggregate MAP, central-mass, and split-half invariants are recomputed.
- [x] Tail corruption and missing-partition fixtures fail.
- [x] Ten resource axes and all six non-equivalent assessment modes are explicit.
- [x] Full execution and independent evidence modes remain `not-performed`.
- [x] Restricted attestation remains a template, not fabricated evidence.

## Human or independent work still required

- [ ] Determine whether the sanitized partitions represent any intended production claim.
- [ ] Inspect production calibration, model, convergence, scheduler, GPU, retry, and storage behavior.
- [ ] Obtain a real restricted-platform attestation if a relying domain accepts that boundary.
- [ ] Execute a different method or implementation for independent evidence.
- [ ] Resolve licensing and archival identity before release.
