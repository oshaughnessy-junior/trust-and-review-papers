---
artifact_role: architecture-white-paper
authors: [Codex, junior]
status: working-draft
date: 2026-08-24
publication_status: private-not-approved
scope: reviewer trust, anonymity, topic domains, nested governance, and corpus-scale MCRP
claim_posture: proposed-not-validated
---

# Scaling MCRP from records to a peer-review corpus

## Executive decision

MCRP already specifies how to preserve claims, evidence, executions, review
reports, attestations, challenges, and later corrections. That solves the
record problem. It does not solve the actor problem:

- who is eligible to review which claim;
- whose review another community is willing to rely on;
- how bad, careless, captured, or malicious actors lose influence;
- how a reviewer remains anonymous on each case without becoming an
  unaccountable permanent pseudonym;
- how one scientific community separates from another without corrupting the
  shared record;
- how interdisciplinary work composes several kinds of expertise.

The proposed answer is a new MCRP **Trust-Domain and Review-Governance (TDRG)**
layer. It has one shared event substrate and many local, typed, forkable trust
views. It deliberately has no universal reviewer reputation.

The core rule is:

> Trust is a directed willingness by one actor or community to rely on another
> for a named capability in a named domain, under a versioned policy, until an
> expiry. It is not an intrinsic property of a person.

## 1. The architecture

The corpus has five separable planes:

```text
Scientific record plane
  immutable SRRs, claims, evidence, executions, review reports, challenges

Actor-credential plane
  unique-human enrollment, domain membership, competencies, conflicts, roles

Private accountability plane
  civil identity <-> domain account <-> per-review persona mappings

Trust-domain plane
  charters, roots, scoped delegations, bridges, forks, appeals, sanctions

Derived-view plane
  frozen, policy-specific reviewer routing and claim-coverage views
```

The scientific record remains portable even when trust domains disagree or
fork. The accountability mapping remains private even when review reports are
public. Derived views can be recomputed; they never rewrite the history beneath
them.

### No global `trusted=true`

A meaningful reviewer-routing statement has this shape:

> Under domain charter D, trust roots T, role R, topic scope S, event snapshot E,
> policy P, and time t, actor X is eligible for supervised/full review with the
> following evidence, exclusions, uncertainty, and conflict status.

Different roots can reach different results from the same history. That is a
feature. A global score would hide the dependence on roots, topic, role, and
policy and would let one captured consensus poison every consumer.

## 2. Reviews are anonymous per case, not under one public persona

Each human has three identities:

1. A civil or institutional identity, known only to a uniqueness registrar.
2. A random domain account, known to an independent eligibility/reputation
   service but not publicly connected to the civil identity.
3. A fresh review persona for each paper, release, round, and role.

The review persona is stable within its case so authors can receive replies and
revisions can be attributed to the same review. It is not reused on another
paper. The public therefore cannot build a prestige profile or retaliatory map
across a reviewer's cases.

This creates a non-negotiable tradeoff: somebody or some cryptographic protocol
must privately connect review outcomes to the durable domain account. TDRG v0.1
uses separated services and threshold-controlled mappings because they are
auditable with contemporary tools. Anonymous credentials, scoped nullifiers,
and hidden reputation proofs are an advanced profile.

The anonymity claim is bounded. Authors, public readers, ordinary reviewers,
line management, and the review publisher should not be able to identify the
reviewer or link separate reviews. The registrar and reputation service can
collude to make that link, and content, timing, or a tiny expert pool can reveal
identity. Those threats must be stated and tested.

### One review and one vote without a public identity

Each assignment derives an immutable scope from:

```text
domain version
+ SRR/release digest
+ review round
+ requested role
+ policy version
```

The reviewer receives one capability for that scope and generates a fresh
signing key. A one-use handle or scoped nullifier prevents a second review under
the same credential without linking reviews across scopes. Review-quality polls
use separate one-use credentials; voting eligibility does not imply review
authorship.

Votes attach to review objects, not public reviewer profiles. They answer typed
questions—coverage, evidence anchoring, actionability, professional conduct—not
“do you like this reviewer?” or “did this reviewer agree with the paper?”

## 3. Local graph trust

The trust graph is directed and multilayered. A positive edge means:

> A is willing to rely on B for capability C in topic/domain D, within limits L,
> until expiry T, based on evidence E.

Examples of capabilities include:

- calibration review;
- statistical-model review;
- numerical reconstruction;
- software/provenance review;
- uncertainty assessment;
- review-of-review adjudication;
- privacy-trustee or domain-governance service.

The edge is not “B is a good scientist.” It is not transferable to another
topic, role, or risk level.

### Baseline evaluator

The proposed baseline is deliberately hybrid:

1. Filter to one domain/topic/capability layer and remove expired, conflicted,
   suspended, or policy-ineligible edges.
2. Use a root-relative flow/capacity rule to bound how much influence can cross
   a weakly trusted frontier.
3. Within the admissible set, use a short personalized restart walk as one
   routing signal.
4. Apply institution/control diversity, workload, coverage, newcomer, and
   randomization constraints outside the graph score.
5. Return an eligibility band, reasons, paths, uncertainty, and missing
   evidence—not a public scalar leaderboard.

This combines useful ideas from attack-resistant max-flow trust and
personalized PageRank. It has no claim of optimality. Every parameter and root
set is a governance choice that must be versioned and tested.

### Bad actions are localized

TDRG does not propagate negative trust algebraically. An adverse event can:

- challenge or supersede one review;
- block a route from one source or domain;
- require supervision or an audit;
- suspend a role within one domain;
- remove a delegation edge;
- trigger a due-process proceeding.

It cannot automatically lower every neighbor, create trust through “enemy of my
enemy,” or revoke standing in unrelated domains. A manager or majority cannot
delete the original review or an actor's competing interpretation.

The system separates three feedback types:

- **report evaluation:** a vote or assessment of a particular review object;
- **trust delegation:** willingness to rely on an actor for a future scoped role;
- **conduct adjudication:** an evidence-bearing institutional decision with
  appeal rights.

Conflating these is how a popularity vote becomes a purge mechanism.

## 4. Topic colors and nested domains

TDRG uses a multicolored graph for storage but single-color evaluation by
default. Each edge is keyed by domain, topic, capability, and predicate. A trust
computation cannot silently average colors.

A complex SRR carries a review coverage contract such as:

```text
AND
  one compact-binary-inference scientific review
  one detector-calibration/data-quality review
  one statistical-uncertainty review
  one workflow/provenance review
  one reviewer-controlled execution or declared downselect
  independence constraints across named control relationships
```

The result is a coverage matrix, not the mean reputation of a panel.

### Domain nesting

Domains form a versioned graph with:

- one normative governance parent;
- zero or more competency imports;
- child domains;
- peer-recognition bridges;
- fork lineage.

The normative parent supplies protocol formats, identity/privacy guarantees,
minimum due process, and perhaps general scientific conduct rules. It does not
transfer scientific authority. A gravitational-wave parent cannot make its
members competent in calibration, waveform systematics, or Bayesian inference
by inheritance.

A cross-domain bridge must state:

- source and target domain/version;
- source and target capability;
- accepted evidence;
- maximum imported eligibility (normally supervised/onboarding);
- attenuation or limits;
- expiry;
- target-domain approver;
- review and revocation terms.

No distrust or sanction crosses a bridge automatically.

### Domain fission and forks

There is no evidence-based universal maximum domain size. Instead, each domain
publishes health thresholds for:

- active qualified reviewers per topic and role;
- effective independence after control/institution/collaboration clustering;
- assignment concentration;
- review latency and backlog;
- topic entropy and rubric calibration;
- bridge concentration;
- challenge, appeal, and reversal rates;
- newcomer time-to-unsupervised eligibility;
- effective anonymity-set size;
- missed and confirmed defect rates where measurable.

A child or fork is indicated when one rubric no longer calibrates the work, a
small bridge set controls cross-topic decisions, or members cannot agree on
roots or policy but can still share evidence. Forks preserve the common MCRP
record and publish distinct trust overlays. They do not inherit private mappings
or distrust, and they do not need to agree which fork is “the real community.”

## 5. Management and institutional capture

The protocol assumes organizations and managers can be conflicted actors. No
single controller should operate the registrar, reputation service, assignment
service, review publisher, trust-view evaluator, and identity-opening process.

Minimum separation:

| Function | May know | Must not control alone |
|---|---|---|
| Registrar | civil identity and domain account | review text, routing rank, opening decision |
| Reputation service | domain account and private history | civil identity, public review corpus administration |
| Assignment service | eligible candidate handles and conflicts | identity map, reputation updates, adjudication |
| Review publisher | case persona and capability proof | domain-account link, opening keys |
| Policy evaluator | declared event snapshot | source records or policy authority |
| Opening trustees | threshold key shares | routine management, scientific disposition |

Policy, roots, parameters, eligibility changes, sanctions, and opening
authorizations are append-only signed events. Changes are prospective unless an
explicit incident policy says otherwise. Every actor has an export and appeal
path. A community can fork its policy while retaining the evidence corpus.

## 6. How reviews change standing

Standing should not update instantly from applause or disagreement. Use a
delayed typed outcome record:

- defect confirmed, falsified, partly upheld, or unresolved;
- assigned evidence path actually inspected;
- required execution completed and reproducible;
- material limitation correctly identified;
- critical planted or later-discovered defect missed;
- report outside assigned scope;
- undisclosed conflict or fabricated evidence adjudicated;
- correction, withdrawal, or appeal outcome.

Outcome evidence updates a private topic-and-capability history. A domain policy
may convert that history into coarse states such as `supervised`, `eligible`,
`experienced`, `audit-required`, or `suspended`. Public proofs should disclose
only what a case needs, because exact history and rare attributes can
deanonymize a reviewer.

Agents can score coverage, detect missing links, compare executions, and propose
outcomes. They cannot decide scientific adequacy, misconduct, reviewer
competence, or identity opening without the required human authority.

## 7. A realistic rollout

### Stage A — brokered accountable anonymity

- independent registrar and domain-account service;
- per-case signing keys and ordinary signed one-use capabilities;
- sealed or threshold-encrypted mappings;
- private typed reviewer histories;
- transparent domain charters and policy snapshots;
- local graph routing with flow caps and random selection;
- review-level feedback and three-lane appeals;
- no public actor score.

This is deployable without custom cryptography, though its separation of duties
must be audited.

### Stage B — blind voting and scoped nullifiers

- blindly issued one-use vote tokens;
- anonymous group-membership proofs;
- per-assignment or per-poll nullifiers;
- independently audited tally and replay prevention;
- batched issuance/publication to reduce correlation.

### Stage C — privacy-preserving credentials

- selective proof of domain membership and eligibility band;
- threshold issuers and openers;
- private reputation updates or verifiable threshold proofs;
- multi-implementation interoperability and cryptographic audit.

Stage C remains research until it is implemented and independently examined.

## 8. What this framework does not solve

- It does not make review conclusions correct.
- It does not make identity issuers honest or institutions independent.
- It does not prevent real humans from colluding.
- It does not guarantee anonymity against stylometry, timing, or small pools.
- It does not establish that local trust improves peer review.
- It does not give a graph algorithm authority to punish people.
- It does not eliminate politics; it makes policy roots, control, and exit more
  visible.

The point is narrower and important: bad actions can be attached to exact review
objects, challenged, and contained within explicit trust relationships. A
captured or incompetent domain need not define global truth. Communities can
separate without losing the scientific record they disagree about.

## 9. Immediate decision

Adopt the companion [TDRG v0.1 protocol draft](../protocol/reviewer-trust-domains-v0.1-draft.md)
as the concrete actor-regulation layer to evaluate. Do not merge it into core
MCRP conformance yet. Run the preregistered comparison in
[the evaluation agenda](../evaluation/reviewer-trust-domain-experiments.md)
against flat voting, global recursive reputation, local personalized trust, and
capped-flow eligibility. Promotion requires evidence about capture radius,
minority survival, reviewer inclusion, privacy leakage, and defect detection.

The architecture's stake in the ground is:

> MCRP scales by preserving a common verifiable record beneath plural, local,
> topic-scoped, anonymous-but-accountable, and forkable trust domains—not by
> manufacturing a universal scientific reputation.

## 10. Scholarly contribution and publication structure

The contribution is a consolidation, not a claim that its ingredients are new.
MCRP joins scientific provenance, peer-review evidence, graph trust, anonymous
accountability, transparency logs, and polycentric governance into one model
whose boundaries and interactions can be inspected. The central theoretical
object is a scoped trust view:

```text
V(relying roots, domain, topic × capability × role, request, event time)
```

This replaces the underspecified idea that a reviewer possesses one reputation.
It also exposes a feedback dynamic: standing affects assignment, assignment
creates opportunities to produce reviews, and review outcomes affect later
standing. Global recursive scores couple every topic and community through this
loop; TDRG's local layers, frontier capacities, bridge limits, and assignment
exploration are proposed interventions, not yet proven remedies.

A connected publication program is preferable to forcing the full argument into
one manuscript:

1. a theory/position article on global versus local reviewer-trust dynamics;
2. a protocol/systems article specifying accountable anonymity, typed trust
   domains, bridges, forks, and conformance;
3. a comparative evaluation article executing the adversarial experiments and
   no-go criteria;
4. optionally, a later sanitized domain case study.

The detailed contribution boundary, formal framing, article outlines, evidence
gates, and venue fit are recorded in
[`reviewer-trust-publication-program.md`](reviewer-trust-publication-program.md).
