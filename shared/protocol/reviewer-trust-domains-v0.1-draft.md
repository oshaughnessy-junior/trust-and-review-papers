---
artifact_role: protocol-working-draft
authors: [Codex, junior]
status: proposed-v0.1
date: 2026-08-24
publication_status: private-not-approved
name: MCRP Trust-Domain and Review-Governance Profile
short_name: TDRG
version: 0.1-draft
claim_posture: proposed-not-validated
---

# MCRP Trust-Domain and Review-Governance Profile (TDRG) v0.1 draft

## 1. Purpose and boundary

TDRG specifies how independently governed actors and communities may authorize,
route, publish, evaluate, challenge, sanction, and rely on MCRP reviews without
creating one global reputation or exposing a persistent public reviewer
identity.

TDRG regulates review actors and derived trust views. It does not change an
MCRP Scientific Record Release (SRR), decide that a claim is true, or grant an
algorithm scientific authority.

This document uses **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**
normatively. It is a working draft and has not been validated in a real review
community.

## 2. Core invariants

1. There is no universal actor score or global `trusted=true`.
2. Trust is directed, typed, domain- and capability-scoped, evidence-bearing,
   expiring, and evaluated from declared roots.
3. Every public review case uses a fresh persona that is unlinkable to the
   reviewer's other cases within the declared adversary model.
4. Identity uniqueness, domain eligibility, review publication, reputation
   custody, assignment, policy evaluation, and exceptional identity opening are
   separate authority classes.
5. A review-level vote, actor-level trust delegation, scientific disposition,
   and conduct adjudication are different objects and MUST NOT be silently
   converted into one another.
6. Trust is evaluated in one topic-and-capability layer at a time. Cross-layer
   transfer requires an explicit bridge accepted by the importing domain.
7. Distrust, suspension, or adverse evidence MUST NOT propagate transitively or
   cross a domain bridge by default.
8. A domain may fork its policy and trust overlay without deleting or forking
   the immutable scientific and review objects beneath it.
9. Graph standing is evidence for routing, supervision, or audit. It MUST NOT
   determine whether a scientific claim passes.
10. Scientific disagreement alone MUST NOT justify identity opening, sanction,
    or reputation loss.

## 3. Threat model

Every deployment MUST publish which of these adversaries it addresses:

- one human controlling multiple identities;
- multiple credentialed humans coordinating reviews or votes;
- negligent, unqualified, or malicious reviewers;
- authors or managers retaliating against reviewers;
- a captured domain board, registrar, assignment service, reputation service,
  publisher, evaluator, or identity-opening trustee;
- bribery, financial dependence, supervisory pressure, and undisclosed conflict;
- ballot stuffing, bad-mouthing, reciprocal review rings, whitewashing,
  on/off behavior, and prestige laundering;
- graph manipulation, malicious trust roots, bridge capture, and domain spam;
- metadata, timing, writing-style, and small-anonymity-set deanonymization;
- issuer/verifier, verifier/verifier, or infrastructure collusion;
- credential theft, sharing, revocation failure, replay, and key compromise;
- malicious documents or metadata targeting reviewing agents.

The deployment MUST state unaddressed threats and residual risks. A signature
does not prove unique personhood, competence, independence, honesty, or truth.

## 4. Trust-domain manifest

Every trust domain MUST publish an immutable, signed, versioned manifest with:

- stable `domain_id`, version, predecessor, and effective date;
- normative governance parent, if any;
- topic expression, included and excluded scopes, and ontology identifiers;
- review capabilities and role definitions;
- acceptance rubrics and review-quality outcome vocabulary;
- recognized uniqueness, competency, and conflict issuers;
- trust roots and their controller, funding, hosting, and key-custody metadata;
- trust evaluator, algorithm, parameters, maximum path depth, capacity rules,
  decay, uncertainty, and staleness rules;
- assignment, randomization, workload, independence, and newcomer policies;
- anonymity profile, trusted operators, minimum effective anonymity-set policy,
  timing/metadata controls, and residual deanonymization risks;
- registrar, reputation custodian, publisher, policy evaluator, trustees, and
  control-principal separation;
- challenge, appeal, conduct, sanction, opening, and reinstatement processes;
- governance voting or decision rules, compensation rules, and conflicts;
- parent, child, recognition, bridge, and fork-lineage links;
- health measures, review cadence, fission/fork triggers, and exit/export rules;
- policy, schema, evaluator, and test-fixture digests;
- signature and zero or more independent registration receipts.

A mutable web page is not a domain manifest. A new material policy creates a new
version. Retrospective application MUST be explicitly authorized by a
pre-existing incident rule and recorded as a new event.

### 4.1 Interoperability and reuse

TDRG is a governance and conformance profile, not a replacement scholarly
metadata universe. A conforming implementation:

- MUST map review roles, stages, anonymity, interaction, and outcomes to
  ANSI/NISO Z39.106-2023 terms where equivalents exist;
- SHOULD exchange repository/review-service requests and notifications through
  COAR Notify and its ActivityStreams/Linked Data Notifications model where
  applicable;
- SHOULD publish editorial and review-event projections compatible with
  DocMaps;
- SHOULD register public reviews, decision letters, and author responses using
  Crossref peer-review metadata when DOI registration is appropriate;
- MUST preserve MCRP claim, evidence, execution, challenge, and attestation
  identifiers rather than duplicating those objects inside a trust score;
- MUST document every extension, loss boundary, and access-controlled field;
- MUST provide round-trip fixtures showing that identity scope, claim scope,
  signatures, challenges, supersession, and policy meaning are not changed by
  export and reimport.

An implementation MAY use a different exchange substrate, but it MUST publish a
crosswalk and justify why the established representation was insufficient.

### 4.2 Domain structure

A domain MUST have at most one normative governance parent. It MAY recognize
many competency imports and peer domains. This prevents ambiguous constitutional
inheritance while permitting multidisciplinary membership.

A parent's recognition means only what the recognition object states. It MUST
NOT imply that:

- parent standing transfers to a child;
- child standing transfers to a parent;
- the parent controls a child's scientific judgments;
- a member is competent across all descendant topics;
- a sanction or distrust edge propagates between domains.

## 5. Actor identifiers and authority separation

### 5.1 Three identifier scopes

Each reviewer MUST be represented by three distinct identifiers:

1. **Identity record:** civil/institutional identity held by a uniqueness
   registrar.
2. **Domain account:** random domain-specific identifier held by the eligibility
   and reputation custodian.
3. **Review persona:** fresh public signing key and identifier for one exact
   review case.

A review case is the tuple:

`(domain version, SRR digest, review request, round, role, policy version)`.

The review persona MAY remain stable for replies and revisions inside that case.
It MUST NOT be reused in another case. Public artifacts MUST NOT contain the
domain account or civil identity unless the reviewer knowingly signs a separate
identity-disclosure event.

### 5.2 Separation of duties

No routine principal SHOULD control more than one of these combinations:

- identity registrar plus review publisher;
- identity registrar plus reputation custodian;
- reputation custodian plus assignment authority;
- assignment authority plus conduct adjudicator;
- policy authority plus sole policy evaluator;
- line management plus identity-opening threshold;
- review publisher plus sufficient identity-opening shares.

If operational constraints require a combination, the manifest MUST identify
it, explain the privacy/governance loss, provide independent audit, and forbid a
stronger anonymity or independence claim.

No ordinary operator MUST possess a plaintext table mapping public review
personas directly to civil identities.

## 6. Enrollment, eligibility, and uniqueness

The uniqueness registrar MUST:

- verify one enrollment per human under a disclosed identity-assurance policy;
- issue or authorize a random domain account without publishing the identity
  link;
- record recovery, duplicate resolution, suspension, and exit procedures;
- disclose which civil, institutional, ORCID, employment, or other assertions
  it relies on;
- keep identity evidence outside the public review corpus;
- publish aggregate enrollment and revocation accounting consistent with its
  privacy model.

Identity uniqueness is not competence. A domain-eligibility credential MUST
separately bind:

- domain and version;
- allowed role/capability and supervision state;
- competency basis and issuer;
- issuance and expiry;
- conflict-check requirement;
- rate and assignment limits;
- appeal and revocation method.

A domain MUST provide a newcomer path that does not require a public prestige
score. Supervised reviews, training fixtures, independent competency evidence,
or bounded probation MAY be used. Newcomers MUST NOT be silently treated as
malicious because their graph history is sparse.

## 7. Anonymous review transaction

### 7.1 Review authorization

For each case, the assignment service MUST create a signed scope containing:

- immutable review request and target SRR/claim digests;
- domain, role, round, policy, and deadline;
- required competency and conflict predicates;
- permitted number of submissions and revisions;
- privacy and evidence-access class;
- assignment method and selection receipt.

The reviewer MUST create a fresh review-persona key. The eligibility service
MUST issue a one-use capability or anonymous proof bound to the case and persona
key. The publisher MUST verify authorization, scope, expiry, persona signature,
and unused handle/nullifier before accepting the review.

The capability MUST reveal only the attributes needed by the request. Exact
private standing, history, identity, rare qualifications, and unneeded
affiliations MUST NOT be disclosed.

### 7.2 Duplicate prevention

A deployment MUST prevent one domain account from submitting more reviews or
votes than the case permits. It MAY use:

- a random one-use handle tracked privately by the issuer;
- a blindly issued one-use token;
- a scoped nullifier derived from the assignment or poll scope;
- another independently reviewed mechanism with equivalent properties.

A nullifier MUST use the narrowest scope requiring duplicate detection. A
global or domain-wide nullifier is prohibited because it creates a durable
tracking identifier.

Duplicate prevention does not prove unique personhood; it inherits the
registrar's assurance and credential-sharing limitations.

### 7.3 Publication and metadata

The review publisher MUST:

- remove transport metadata not required by the protocol;
- use batching or delayed publication where timing would identify a reviewer;
- avoid publishing exact rare attributes or a fine-grained private trust band;
- state the effective anonymity set and how it was estimated;
- publish `confidential` rather than `anonymous` when the claimed adversary or
  anonymity-set requirement is not met;
- preserve the review, revisions, challenge links, and persona signature.

Text, specialist facts, and writing style can reveal identity. A deployment MUST
NOT claim absolute anonymity or coercion resistance.

## 8. Review evaluation and votes

### 8.1 Typed evaluation

Every review-evaluation request MUST state who is eligible to evaluate and which
questions are being asked. Initial types are:

- `scope-covered`;
- `evidence-path-identified`;
- `method-executed-as-declared`;
- `limitation-made-explicit`;
- `actionable`;
- `professional-conduct`;
- `defect-confirmed`;
- `defect-falsified`;
- `defect-unresolved`;
- `material-defect-missed`;
- `outside-assigned-scope`;
- `conflict-or-conduct-event-adjudicated`.

The following MUST NOT directly update actor standing:

- agreement with the manuscript;
- agreement with a majority or editor;
- favorable/unfavorable recommendation alone;
- author satisfaction;
- citation count, academic rank, employer prestige, or public popularity.

### 8.2 Anonymous review voting

An anonymous poll MUST use a credential separate from review authorship and MUST
bind each vote to one immutable poll scope. The tally MUST reject duplicate
handles/nullifiers and publish its inclusion, exclusion, and invalid-ballot
rules.

Raw vote counts MUST NOT revoke standing, open identity, decide misconduct, or
serve as a scientific disposition. A vote MAY trigger an audit or contribute to
a delayed typed outcome under the domain policy.

### 8.3 Delayed outcomes

Where possible, standing updates SHOULD wait for rebuttal, reproduction,
adjudication, correction, or later evidence. Every update MUST retain:

- review and claim targets;
- triggering event and evidence;
- policy version;
- updater authority;
- prior and new private state;
- uncertainty and expiry;
- appeal status.

A reversed or partly upheld outcome MUST create a corrective event. History MUST
NOT be silently rewritten.

## 9. Trust delegations and adverse events

### 9.1 Positive delegation

A trust delegation MUST state:

- issuer and subject domain accounts or privacy-preserving commitments;
- domain, topic, capability, role, and maximum risk or authority;
- stance `rely` or `insufficient-evidence`;
- strength/capacity and confidence;
- evidence basis;
- relevant conflicts and control relationships;
- issue and expiry times;
- withdrawal and challenge rules;
- issuer signature or anonymous authorized proof.

Delegation means willingness to route or rely under the stated limits. It does
not mean the subject's future review is correct. It MUST NOT transfer scientific
voting weight.

### 9.2 Negative information

Negative actor events MUST use a typed stance such as:

- `do-not-route-from-this-root`;
- `recusal-required`;
- `audit-required`;
- `role-suspension-proposed`;
- `credential-suspended`;
- `conduct-finding`;
- `insufficient-evidence`.

They MUST identify scope, grounds, evidence-access class, authority, expiry,
challenge, and appeal. `Unknown` or no path MUST remain distinct from adverse
evidence.

The evaluator MUST NOT:

- propagate negative trust through neighbors;
- infer positive trust from two negative edges;
- apply an event to another topic, role, or domain without explicit policy;
- convert an allegation into a finding;
- expose the target's identity merely to make a negative edge public.

## 10. Baseline local trust evaluator

### 10.1 Inputs

Every evaluation MUST bind:

- relying actor/community or root set and weights;
- domain/version, topic, capability, role, and claim risk;
- frozen event, credential, conflict, revocation, and clock snapshots;
- exact evaluator artifact and version;
- maximum path depth, restart, decay, capacity, independence, and uncertainty
  parameters;
- treatment of unknown, restricted, challenged, and stale evidence.

### 10.2 Required stages

The baseline evaluator MUST perform stages in this order:

1. **Layer filter:** retain only exact or explicitly bridged topic-capability
   edges.
2. **Validity filter:** remove expired, revoked, unauthorized, or inapplicable
   edges; mark restricted and unknown evidence separately.
3. **Conflict filter:** apply case-specific recusals and controlling-principal
   rules.
4. **Frontier bound:** apply a root-relative capacity/max-flow or equivalent
   attack-bound rule that limits influence entering through each weak frontier.
5. **Local discovery:** compute a short personalized restart walk or declared
   local metric within the admissible graph.
6. **Diversity constraints:** evaluate institution, supervisor, collaboration,
   funding, infrastructure, and common-control concentration independently of
   graph-path diversity.
7. **Routing:** sample from a qualified set under workload and newcomer rules;
   top rank MUST NOT receive every assignment.
8. **Explanation:** emit eligibility band, reasons, contributing paths,
   capacity bottlenecks, exclusions, uncertainty, and missing evidence.

An implementation MAY use another algorithm only if it publishes the algorithm,
assumptions, attack model, versioned parameters, fixtures, and comparative
evidence. No evaluator may emit an authoritative universal actor score.

### 10.3 Output

A trust-view snapshot MUST contain:

- subject or private candidate-set commitment;
- roots, domain, topic, capability, role, and policy;
- frozen input manifests and digests;
- evaluator and parameter digests;
- eligibility band (`supervised`, `eligible`, `experienced`, `audit-required`,
  `ineligible`, or `unknown`);
- score components if used internally, with uncertainty and non-comparability;
- paths, capacities, bridges, and conflict/diversity findings;
- uncovered or restricted evidence;
- observation and expiry times;
- signature and optional trust-node receipts.

Public routing proofs SHOULD disclose the minimum eligibility predicate, not the
private actor history or exact internal score.

## 11. Cross-domain bridges and multidisciplinary coverage

A bridge MUST state:

- source and target domain/version;
- mapped topic, capability, and evidence vocabulary;
- maximum imported band and supervision requirement;
- attenuation, path-depth cost, or capacity ceiling;
- accepted credential/outcome evidence;
- target-domain approver and conflicts;
- issue, expiry, review, suspension, and revocation rules;
- signature and policy receipts.

The target domain owns the bridge. Source-domain standing MUST NOT cross without
target acceptance. The default imported band SHOULD be no greater than
`supervised` until target-domain evidence exists.

An SRR requiring multiple domains MUST declare a logical coverage expression
over claim IDs, domains, capabilities, reviewer-controlled executions, and
independence constraints. Coverage MUST be conjunctive where all dimensions are
material. It MUST NOT be replaced by an average reviewer score or majority vote.

## 12. Domain health, fission, and forks

No universal maximum membership is defined. Each domain MUST publish and review
a health vector including:

- active qualified reviewers per topic/capability;
- effective independent reviewer count after control clustering;
- assignment and trust-root concentration;
- backlog, latency, abandonment, and workload;
- topic entropy and rubric-calibration drift;
- confirmed, falsified, unresolved, missed-defect, and appeal-reversal rates;
- conflicts detected before and after assignment;
- newcomer waiting time and progression;
- bridge concentration and broker dependence;
- effective anonymity set and deanonymization incidents;
- duplicate-identity, reciprocal-voting, and coordinated-behavior indicators;
- stale edges, credential churn, and reviewer attrition.

Threshold breaches MUST trigger a recorded review, not an automatic split or
sanction. A child domain or fork SHOULD be considered when one rubric no longer
calibrates the scope, expertise clusters require different roots, or governance
capture cannot be corrected internally.

A fork MUST:

1. publish a new manifest and explicit lineage;
2. retain shared identifiers for public SRRs, reviews, and events;
3. define new roots and policy without rewriting the predecessor;
4. obtain holder consent before importing private credentials or trust edges;
5. not inherit distrust, sanctions, or identity mappings by default;
6. preserve challenges and competing scientific assessments;
7. provide export and later recognition/bridge mechanisms;
8. disclose shared controllers or infrastructure with the predecessor.

## 13. Challenges, appeals, sanctions, and identity opening

### 13.1 Three appeal lanes

1. **Scientific-content appeal:** reassesses reasoning/evidence without opening
   identity and may supersede a review outcome.
2. **Private-standing appeal:** lets an authenticated reviewer inspect and
   challenge the events and policy that changed their private state without
   public identity disclosure.
3. **Conduct/opening appeal:** handles enumerated abuse under a separate tribunal
   and threshold trustees.

### 13.2 Permitted opening causes

Identity opening MUST NOT be requested for scientific disagreement, an
unfavorable recommendation, an ordinary low rating, author pressure, management
curiosity, or the convenience of adjudicators.

A domain MAY permit opening for a documented allegation of:

- duplicate-identity fraud;
- bribery or severe undisclosed financial/supervisory conflict;
- fabricated evidence or forged execution;
- theft or misuse of confidential material;
- coordinated credential abuse;
- credible threat, harassment, or legal/safety obligation.

Opening requires:

- immutable allegation target and evidence;
- finding that non-identifying remedies are inadequate;
- recusal and conflict checks;
- threshold authorization by independently controlled trustees;
- signed authorization and participation record;
- disclosure to the minimum adjudicating body;
- reviewer notice unless a narrowly bounded safety rule delays it;
- appeal and correction rights;
- identity-free public docket and periodic aggregate statistics.

The opening process MUST NOT publish the reviewer's identity automatically.

## 14. Transparency and privacy log

The deployment SHOULD maintain signed append-only records for:

- domain and policy versions;
- issuer, evaluator, and trustee keys;
- aggregate enrollment, capability issuance, redemption, and revocation counts;
- accepted review handles/nullifiers and review revisions;
- feedback polls and tally artifacts;
- private-standing update commitments without domain-account identifiers;
- challenges, adjudications, appeals, key rotation, and opening authorizations;
- signed checkpoints and independent consistency witnesses.

Exact issuance timing, rare attributes, small counts, and relationship graphs
can deanonymize participants. Public projections MUST use epochs, delayed
aggregation, access control, or privacy-preserving commitments where necessary.
Log inclusion proves registration, not endorsement or correctness.

## 15. Management and governance safeguards

- Domain roots, policy authorities, issuers, evaluators, trustees, funders,
  operators, and controlling principals MUST be disclosed to members.
- Policy and root changes MUST have notice, prospective effect, appeal, and
  export/fork paths.
- Management MUST NOT silently alter assignment rank, standing, review
  visibility, opening policy, or evidence windows.
- Random audits MUST sample high-standing, low-standing, controversial, and
  newcomer reviews; audit allocation MUST NOT be purely rank-proportional.
- Reciprocal reviewing and voting, synchronized behavior, common employment,
  supervision, funding, and infrastructure MAY trigger independence review but
  MUST NOT become automatic misconduct findings.
- Compensation and material dependence MUST be available to the conflict policy
  under privacy-appropriate disclosure.
- Minority reviews, unresolved challenges, and losing appeals remain
  addressable and inspectable.

## 16. Conformance statement

A deployment claiming TDRG support MUST report:

```text
TDRG v0.1-draft
domain manifest: [digest and version]
actor profile: [brokered | blind-token | scoped-nullifier | private-credential]
anonymity adversaries: [list]
trusted operators and collusion assumptions: [list]
trust evaluator: [artifact digest and policy]
domain/topic/capability layer: [IDs]
view roots and frozen snapshot: [IDs/digests]
assignment and diversity policy: [ID]
opening threshold and appeal policy: [ID]
health observation window: [dates]
capabilities tested: [list]
unverified properties and residual risks: [list]
```

Conformance means that the declared objects and controls were present and the
listed tests passed. It does not establish reviewer quality, anonymity against
undeclared adversaries, capture resistance, scientific correctness, or benefit
over conventional peer review.

## 17. Minimum test suite

Before deployment, exercise at least:

- two enrollments by one attempted duplicate actor;
- one-use review and vote replay;
- cross-case persona-linkability analysis;
- timing, attribute, graph, and small-pool deanonymization;
- issuer/publisher, registrar/reputation, and trustee collusion assumptions;
- review ring, reciprocal voting, bad-mouthing, whitewashing, and on/off actors;
- malicious and compromised trust roots;
- shared-management paths misidentified as independent;
- cross-topic reputation leakage;
- negative-edge poisoning and enemy-of-enemy inference;
- sparse newcomer and sparse legitimate specialty;
- planted defect, qualified dissent, false allegation, and reversed appeal;
- delayed revocation, partitions, stale credentials, and evaluator rollback;
- domain bridge compromise, parent overreach, fork/export, and later
  recognition;
- malicious document and prompt-injection handling for agents;
- management request for unauthorized identity opening;
- COAR Notify, DocMaps, Crossref, and NISO terminology round trips for the
  implemented projections, including extensions and restricted fields.

Results MUST be retained, including adverse outcomes. Synthetic tests establish
only tested protocol behavior, not real-world reviewer benefit.

## 18. Anti-patterns

- one global reviewer score;
- a permanent public “anonymous” reviewer pseudonym;
- raw vote count used as trust, truth, or sanction;
- agreement rate used as review quality;
- graph centrality used as scientific competence;
- prestige, citations, institution, or seniority as sole reviewer authority;
- public exact reputation histories that defeat anonymity;
- one manager controlling identity, assignment, reputation, and opening;
- a global nullifier or other cross-case tracking identifier;
- negative trust propagated through the graph;
- parent-domain standing or sanctions inherited automatically;
- cross-topic averaging of trust;
- path-disjointness treated as institutional independence;
- graph anomaly treated as misconduct;
- identity opening for disagreement or convenience;
- a fork that deletes, relabels, or captures the shared record;
- cryptography presented as proof of competence, honesty, or scientific truth.

## 19. Promotion gate

TDRG MUST remain outside core MCRP conformance until:

- at least two independent implementations exchange the required objects;
- the brokered privacy boundary and opening workflow receive security/privacy
  review;
- local and global trust baselines are compared under declared attacks;
- one public or sanitized multi-domain review is completed;
- newcomer, minority-view, management-capture, and anonymity harms are measured;
- policy replay reproduces the same view from the same frozen inputs;
- stop conditions in the evaluation plan are not crossed.

The first implementation SHOULD use brokered accountable anonymity with
ordinary signatures. Advanced zero-knowledge profiles MAY be piloted, but core
MCRP MUST NOT depend on custom or immature cryptography.
