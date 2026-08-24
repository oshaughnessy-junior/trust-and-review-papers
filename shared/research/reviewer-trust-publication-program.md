---
artifact_role: publication-and-research-program
authors: [Codex, junior]
status: working-draft
date: 2026-08-24
publication_status: private-not-approved
claim_posture: synthesis-and-proposed-design-not-validated
---

# Publication program: trust domains for a machine-verifiable scientific record

## Decision

This work merits an umbrella white paper and, if the stated evaluations are
performed, a connected series of research articles. Its defensible contribution
is not invention of every component. It is the consolidation of fragmented
mechanisms into a scientific-review architecture with explicit semantics,
boundaries, failure modes, and testable design choices.

The umbrella claim is:

> A machine-verifiable scientific record cannot scale through provenance alone.
> It also needs a plural governance layer that binds anonymous review actions to
> privately accountable actors, routes reliance through topic-local trust, and
> permits communities to bridge or fork without rewriting the scientific record.

This is a systems and institutional-design thesis. It should not be sold as a
new centrality algorithm, a proof that peer review works, or a cryptographic
solution to scientific judgment.

## 1. Theory of the consolidated object

The prior literatures usually model different pieces:

- provenance systems model how evidence and computations relate;
- peer-review studies measure reviewer agreement, bias, and reliability;
- graph-trust systems estimate reliance or resist some classes of attack;
- anonymous-credential systems separate eligibility from identity disclosure;
- transparency logs preserve append-only, auditable events;
- polycentric-governance theory explains overlapping, autonomous institutions;
- archival standards preserve addressable research objects over time.

MCRP's unifying object is not a paper and not a reviewer score. It is a typed,
time-indexed relation among a scientific claim, its evidence, a review action,
the actor authority behind that action, and a relying community's policy.

Let:

```text
E_tau = the frozen scientific, review, credential, conflict, and governance events at time tau
D     = a versioned trust domain
R     = the relying actor or declared trust roots
K     = one topic × capability × role layer
P     = a versioned policy and evaluator
Q     = a review request or reliance question
```

Then a trust view is:

```text
V(R, D, K, Q, tau) = F(E_tau, R, D, K, Q, P)
```

`V` is a reproducible, expiring answer to a scoped reliance question. It is not
an intrinsic latent quality of a person. Changing roots, topic, policy, event
cut, or risk class can legitimately change the answer.

This formulation supplies three clarifications absent from a global score:

1. **Epistemic separation:** evidence supports claims; actor trust only helps
   route or weight human attention. Neither substitutes for the other.
2. **Perspective:** reliance is observer- or community-relative, so disagreement
   can remain explicit instead of being collapsed into one rank.
3. **Governance provenance:** roots, bridge decisions, conflicts, parameters,
   and policy versions are part of the result and can be challenged or forked.

## 2. Dynamics and the mean-field failure mode

Reviewer reputation is a feedback system:

```text
standing -> visibility/assignment -> opportunity to review -> feedback/outcomes
         -> new standing -> further visibility/assignment
```

A global recursively computed score couples every topic and community through
this loop. Under strong social influence or preferential assignment, small
differences in initial prestige, root choice, or early votes can become
self-reinforcing concentration. The issue is not that PageRank-like or
EigenTrust-like methods are mathematically invalid; it is that their global
fixed point answers the wrong governance question and can obscure who supplied
the boundary conditions.

TDRG proposes four interventions whose effects must be measured:

- **spectral separation:** evaluate one topic/capability layer at a time;
- **localized boundary conditions:** compute from declared roots rather than a
  universal prior;
- **frontier capacity:** cap influence that enters through a small trusted cut;
- **assignment exploration:** sample qualified reviewers, protect newcomer
  routes, and prevent rank from monopolizing future evidence production.

Explicit bridges create controlled coupling between layers. A fork changes
governance boundary conditions while preserving the common event history. This
turns institutional fracture from a database catastrophe into a versioned,
testable property of the system.

This is currently a qualitative theory. A formal article should analyze simple
stochastic endorsement/assignment dynamics and identify regimes for
concentration, capture radius, cross-topic leakage, minority survival, and
fork-localization. It should connect, not merely allude, to existing network
models of endorsement hierarchy, social influence, Sybil resistance, and local
trust.

## 3. What is prior art and what is proposed

| Component | Status | MCRP/TDRG contribution |
|---|---|---|
| recursive graph reputation | established prior work | rejects universal use; makes roots, topic, role, time, and uncertainty explicit |
| personalized/local trust | established prior work | adopts it as a reviewer-routing primitive, not a scientific vote |
| max-flow/capacity Sybil resistance | established prior work | applies a bounded frontier before local discovery and declares its identity assumptions |
| pairwise identifiers, blind tokens, scoped nullifiers, anonymous credentials | established standards/research | composes them into fresh case personas with review, vote, appeal, and opening semantics |
| multilayer networks | established theory | uses typed layers and importer-approved bridges for scientific competencies |
| polycentric/nested governance | established theory | specifies versioned parents, children, bridges, forks, and non-inheritance rules |
| append-only logs and signed attestations | established engineering | separates registration, endorsement, scientific disposition, and trust views |
| claim/evidence provenance | core MCRP work, built on standards | keeps scientific truth conditions separate from actor routing |
| consolidated end-to-end protocol | proposed contribution | defines interoperable objects, invariants, authorities, lifecycle, failure handling, and conformance |
| comparative adversarial evaluation | proposed contribution | tests global/local/capacity arms under collusion, capture, privacy, and newcomer harms |

The novelty language should therefore use **synthesize**, **formalize**,
**operationalize**, **separate**, **compose**, and **evaluate**. Avoid
**first**, **solves**, **trustworthy reviewer**, and **proof of correctness**
without evidence.

The detailed no-go claims and closest end-to-end systems are recorded in
[`../research/reviewer-trust-closest-work-matrix.md`](../research/reviewer-trust-closest-work-matrix.md).

## 4. Connected article sequence

### Article I — Why reviewer trust must be local

**Type:** theory/position paper with formal model and simulations.

**Question:** Why does a global reviewer-reputation fixed point create the wrong
couplings for heterogeneous science, and when do local typed domains and
capacity-limited bridges reduce capture?

**Minimum result:** derive or simulate endorsement/assignment dynamics for a
global graph, topic-local personalized graph, and capacity-bounded local graph;
report concentration, capture radius, cross-topic leakage, newcomer inclusion,
and qualified-minority survival. Include sensitivity to malicious roots and
real-human collusion, not only Sybils.

**Natural audience:** science-of-science, network science, computational social
science, and sociotechnical governance.

### Article II — TDRG: an accountable anonymous review protocol

**Type:** protocol/systems design paper with threat model and reference objects.

**Question:** How can independently governed communities share scientific and
review records while keeping per-case reviewers publicly unlinkable, privately
accountable, and locally routable?

**Minimum result:** specify roles, identity scopes, event schemas, local trust
views, bridges, forks, votes, appeals, opening, privacy claims, conformance, and
interoperability fixtures. Provide a security/privacy analysis and at least two
independent implementations of the exchange objects. Do not require novel
cryptography.

**Natural audience:** scholarly communication, information systems, security
and privacy, research integrity, and responsible computing.

### Article III — Does the consolidation work under attack?

**Type:** preregistered empirical evaluation.

**Question:** Compared with no reputation, raw votes, and a global recursive
score, does TDRG improve defect-oriented reviewer routing without unacceptable
privacy, exclusion, concentration, or governance cost?

**Minimum result:** execute the frozen arms and attacks in
[`../evaluation/reviewer-trust-domain-experiments.md`](../evaluation/reviewer-trust-domain-experiments.md),
publish negative results, and retain the no-go thresholds. A later consented
multi-domain pilot should follow synthetic tests.

**Natural audience:** research integrity, quantitative science studies, open
science, and empirical software/systems research.

### Optional Article IV — Domain case study

**Type:** domain deployment/case study.

Use a sanitized computational-science workflow with lightweight reproduction,
HPC witness/downselect, restricted evidence, transitive-tool review, and later
freshness failure. Study reviewer burden, domain bridges, management pressure,
and whether the vocabulary improves decisions. This article is warranted only
after real use produces evidence not already contained in Articles I–III.

## 5. Publication path

The immediate artifact should be an arXiv-hosted white paper only after the
repository's authorship, privacy, security, citation, licensing, and editorial
gates are passed. A plausible primary category is `cs.CY` (Computers and
Society), cross-listed to `cs.SI` (Social and Information Networks); a protocol
paper with substantial privacy analysis may additionally fit `cs.CR`. Category
choice should follow the actual manuscript, not marketing.

The default venue must impose no author fee when no publication funds are
available. Prefer diamond open access; treat a guaranteed no-funds waiver or a
zero-fee subscription route plus arXiv deposit as secondary. Do not budget on a
discretionary waiver.

RIT affiliation expands the covered set. As of 2026, [RIT Libraries lists
transformative agreements](https://www.rit.edu/library/ntid-blog/publish-open-access-no-cost-through-rit-libraries)
with ACS, ASME, ACM, Cambridge University Press, Elsevier, the Royal Society of
Chemistry, and Springer Nature. Treat a journal under one of these publishers
as fee-compatible only after its exact title, article type, corresponding-author
rule, annual cap, and agreement term are confirmed at submission. The agreements
are time-limited and do not cover every journal. Diamond venues remain the most
portable first choice.

The audited article-to-venue sequence is:

1. **Design map and consolidation:** target the diamond-open-access
   [Journal of Electronic Publishing](https://doaj.org/toc/1080-2711) first.
   It fits a rigorous closest-work map, threat model, requirements, and protocol
   architecture. Its article license may be less reusable than the protocol, so
   keep normative specifications and schemas separately open-licensed. Strong
   alternatives are [Information Research](https://informationr.net/ir/about.html),
   which charges neither submission nor publication fees, and JASIST/ARIST for
   a systematic information-science synthesis under the ordinary no-APC route.
2. **Formal dynamics:** target
   [Network Science](https://www.cambridge.org/core/journals/network-science/information/author-instructions/fees-and-pricing),
   which is currently compatible with RIT's Cambridge agreement and guarantees
   an unfunded-author waiver, or
   [Peer Community Journal](https://peercommunityjournal.org/page/about/)
   through PCI Network Science. SciPost Physics or the traditional/green route
   at Physical Review E becomes appropriate if the result is a genuine
   statistical-physics model with analytic results, phase diagram, and public
   network validation.
3. **Protocol plus implementation/evaluation:** target Information Processing &
   Management, currently potentially covered by RIT's Elsevier agreement and
   the home of the closest DecSci paper. This requires a working system,
   design-science method, and sharp comparison with DecSci and decentralized
   knowledge assessment. JASIST is the fallback.
4. **Sociotechnical pilot:** ACM CSCW/PACMHCI or FAccT becomes plausible only
   after a real study of privacy, power, due process, management capture, and
   participant experience. RIT's ACM agreement may cover publication, but not
   conference registration or travel.
5. **Software:** [JOSS](https://joss.readthedocs.io/en/latest/submitting.html)
   only after the implementation is feature-complete research software with
   sustained public development, documentation, tests, maintainability, actual
   research use, and meaningful human design contribution. A protocol document
   or new repository skeleton is not eligible.

RIT-covered specialist options to adjudicate after the manuscript exists
include **Research Integrity and Peer Review** (Springer Nature) for a real
protocol/pilot study and **ACM Journal on Responsible Computing** or **ACM
FAccT** for a strong privacy, accountability, and power analysis. Coverage of
the exact Springer journal or ACM article/conference charge must be verified;
conference registration and travel are separate costs.

**PNAS** is a contingent hook, not a program home. A submission would need one
clean, domain-general network-dynamics result—such as a phase transition in
global ranking feedback and a demonstrable localization regime—and must stand
without the MCRP protocol narrative. PNAS publication also normally carries
author charges, so this route is off the default no-fee path unless confirmed
institutional coverage or a waiver exists.

Intellectually relevant but financially de-prioritized venues include
Quantitative Science Studies, Research Integrity and Peer Review, Learned
Publishing, and APC-dependent broad open-science journals. Reconsider them only
if full institutional coverage is confirmed before submission.

Do not choose a journal until Article I's formal depth and Article III's
available evidence are known. The first serious target should be selected after
an external literature/novelty review and a short pre-submission inquiry where
the venue permits one.

## 6. Program-level evidence gate

The series should not claim a successful reviewer-governance system until it
has:

- a complete closest-work matrix with claim-level citations;
- a formal or computational model that makes the global/local distinction
  falsifiable;
- a protocol implementation with deterministic policy replay;
- privacy and collusion analysis for the fresh-persona design;
- adversarial comparisons against simpler baselines;
- evidence about newcomer and minority harms, not only attacker exclusion;
- an independently governed or independently implemented second domain;
- a sanitized pilot or a clear statement that no real-world benefit is yet
  known.

Until then, the correct output is a useful white paper and experimental research
program: a consolidation that makes hidden assumptions visible and creates
objects other researchers can criticize, implement, and test.
