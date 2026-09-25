# TrustAndReview papers

Private working repository for a coordinated publication program on machine-verifiable scientific records and scalable, plural peer-review trust.

This repository is a research workspace, not a claim that every planned paper is ready. Each paper has its own maturity gate. Outlines separate established prior work, proposed synthesis, implementation claims, and claims that require new theory or empirical evidence.

## Publication sequence

1. **Design map and consolidation** — unify reproducibility records, accountable review, plural trust, and lifecycle governance; mature enough for a full outline.
2. **Formal dynamics of localized trust domains** — analyze contamination, bridge policies, fission, and nested domains; mature enough for a model-and-experiments outline, not yet for broad claims.
3. **Protocol and reference evaluation** — specify interoperable review events and evaluate a minimal implementation; mature enough for a full outline tied to the tooling repository.
4. **Sociotechnical pilot** — study use by independent actors under adversarial and institutional conditions; mature enough for a preregistration-style outline, not yet a results paper.
5. **Software paper** — deferred until the tooling has a stable release, external use, documentation, tests, and archival citation.

See [PUBLICATION_PROGRAM.md](PUBLICATION_PROGRAM.md) for gates, venue hypotheses, and dependencies.

## September 2026 hardening dossier

[MCRP hardening and modeling](papers/06-mcrp-hardening/README.md) develops the
publication/trust model through economics, game theory, legal operations, and
scientific dynamics. It includes specialist manuscripts, executable synthetic
models, dedicated adversarial reviews, and a collective red-team assessment.
The recommended interface is **offer, check, rely, amend**; complex trust routing
must justify itself against simpler constrained assignment. This is a working
research dossier, not an adopted protocol, field evaluation, or public release.

## Public-prototype release preparation

The [release packet](papers/07-release-packet/README.md) extends the merged dossier
with a blog introduction, self-contained mathematical manuscripts, coupled toy
agents, four domain teaching cases, human and agent onboarding, an executable
legacy-review adapter, and a further collective adversarial pass. Its static
export is prepared for a public protocol seed; publication, attribution and rights
remain separate explicit release decisions. This is a cross-cutting packet for the
existing publication sequence, not evidence that all five papers passed their gates.

## Shared controls

- [SCIENCE_WRITING_PACKET.md](SCIENCE_WRITING_PACKET.md): claim discipline, evidence standards, review gates, and manuscript checks.
- [CLAIM_LEDGER_TEMPLATE.md](CLAIM_LEDGER_TEMPLATE.md): required claim-to-evidence mapping for each paper.
- `shared/research/`: inherited research packets and closest-work comparisons.
- `shared/protocol/`: current protocol source material.

## Provenance and release posture

The seed material is derived from the private `oshaughnessy-junior/mcrp-protocol-paper` worktree at commit `666e897` and earlier reviewed commits recorded there. Copied files retain their original text; new manuscripts must cite primary sources rather than cite the internal packet as authority.

No submission, preprint, public release, or license grant is implied. Authorship, AI-assistance disclosure, venue, and repository licensing require human decisions before release.
