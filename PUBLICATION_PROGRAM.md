# Publication program

## Unifying thesis

Scientific publication in an agentic era needs two coupled layers: a machine-verifiable claim/evidence record and a governance layer that lets independent communities decide which reviews, tools, data, and attestations they trust without pretending that one global reputation score represents scientific truth.

The contribution is primarily **unification, clarification, and operational consolidation**. Individual ingredients have extensive prior art. New claims must be earned through a formal result, a protocol property, an implementation, or an empirical study.

## Sequence and gates

| ID | Working paper | Present maturity | Gate to drafting | Venue hypothesis |
|---|---|---|---|---|
| 01 | Design map for plural, machine-verifiable scientific review | Outline-ready | Complete primary-source gap table and two worked end-to-end cases | Journal of Electronic Publishing; Information Research; JASIST/ARIST-style review |
| 02 | Dynamics of localized trust domains | Model-outline-ready | Define threat model, observables, baselines, and at least one nontrivial analytical or simulation result | Network Science; Peer Community Journal; PNAS only for a clean general result |
| 03 | Trust-domain review protocol and reference evaluation | Outline-ready | Stabilize v0.1 schema/API, adversarial tests, and evaluation report | Information Processing & Management; JASIST; protocol-oriented venue |
| 04 | Sociotechnical pilot of plural review governance | Preregistration-outline-ready | IRB/ethics determination, recruited domains, preregistered outcomes, and operational pilot | PACM HCI/CSCW; FAccT; domain-specific metascience venue |
| 05 | TrustAndReview software | Deferred | Versioned release, archive DOI, documentation, tests, external use, and maintenance policy | JOSS |

Fee posture is a constraint, not an afterthought. Prefer no-fee venues and venues covered by current RIT agreements; confirm the agreement and article type at submission time because coverage changes.

## Dependency order

Paper 01 supplies the conceptual map and terminology. Paper 02 may proceed in parallel but cannot borrow empirical legitimacy from Paper 01. Paper 03 depends on a tested tooling release. Paper 04 depends on Papers 01 and 03 plus ethics and recruitment. Paper 05 depends on software maturity and actual users.

## Program-level stop rules

- Stop a manuscript if its claimed novelty is only a relabeling of EigenTrust/PageRank, web-of-trust routing, open peer review, verifiable credentials, or provenance standards.
- Stop empirical language when only synthetic fixtures or simulations exist.
- Stop anonymity claims unless the threat model and unlinkability mechanism are explicit.
- Stop governance-effectiveness claims without evidence from independent actors.
- Stop venue work if fees are not waived and no no-fee route is available.

## September 2026 public-prototype sequence

The cross-cutting [release packet](papers/07-release-packet/README.md) supports
Papers 01-04 with standalone arguments, conditional models, a tested toy boundary,
domain examples and a pre-results interface evaluation design. It does not move
those papers through their separate gates by association. Paper 05 remains deferred.

The near-term sequence is an accessible introduction and curated versioned
prototype, followed by bounded domain exercises and substantive human criticism.
A scholarly submission should then be rebuilt around the specific contribution
and the venue's current eligibility, disclosure and rights requirements. The
[dissemination assessment](papers/07-release-packet/publication/dissemination.md)
records verified routes and limitations, including the current OSF restriction
relevant to this AI-heavy candidate.
