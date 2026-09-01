# Sanitized HPC downselect review checklist

## Machine-observed

- [x] Four sanitized source partitions have exact identities.
- [x] The released algorithm regenerates per-partition digests from source values.
- [x] Aggregate MAP, central-mass, and split-half invariants are recomputed.
- [x] Tail corruption and missing-partition fixtures fail.
- [x] Ten resource axes and all six non-equivalent assessment modes are explicit.
- [x] Full execution and independent evidence modes remain `not-performed`.
- [x] Restricted attestation remains a template, not fabricated evidence.
- [x] IR001 fresh-context review is preserved with a hold rather than overwritten.
- [x] Standalone replay rejects coherently recorded failed invariants.
- [x] Packet-index validation requires complete and unique non-self coverage.
- [x] Bounded recomputation names checks and excludes scaling, convergence, and representativeness.
- [x] Rounded values and illustrative/unmeasured resource language are explicit.

## Human or independent work still required

- [ ] Determine whether the sanitized partitions represent any intended production claim.
- [ ] Inspect production calibration, model, convergence, scheduler, GPU, retry, and storage behavior.
- [ ] Obtain a real restricted-platform attestation if a relying domain accepts that boundary.
- [ ] Execute a different method or implementation for independent evidence.
- [ ] Resolve licensing and archival identity before release.
- [x] Reinspect corrections at exact commit `5f26da1e5995ff5a0b11fff664dbc82dbc430aa1`; IR001 robustness hold cleared only for the sanitized packet.
