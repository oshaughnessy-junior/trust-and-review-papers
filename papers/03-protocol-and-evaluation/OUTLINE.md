# Paper 03 outline — TDRG protocol and reference evaluation

## Working title

**Plural Trust Without a Global Reviewer Score: A Conformance Profile and Adversarial Evaluation for Machine-Verifiable Scientific Review**

Status: outline-ready; no implementation or empirical results are claimed.

Protocol dependency: `../../shared/protocol/reviewer-trust-domains-v0.1-draft.md`

Evaluation dependency: `../../shared/research/reviewer-trust-domain-experiments.md`

Expected tooling dependency: the private `trust-and-review-tooling` repository, with immutable releases of schemas, fixtures, evaluator code, test reports, and run manifests.

## Research question and designed answer

**Question.** Can a concrete, interoperable review-governance profile separate a shared scientific record from community-relative reviewer routing while making its privacy, capture-resistance, and operational limits falsifiable?

**Designed answer.** TDRG v0.1 defines such a separation and a reproducible test contract; any stronger claim that it improves review quality, anonymity, or capture resistance is conditional on the preregistered comparative and adversarial results.

## Claim boundary

The paper may claim that the protocol **defines** objects, invariants, authority separation, and conformance tests. It may claim that a named implementation **implements** a tested behavior only after a versioned run supports it. It may claim comparative benefit only after frozen A0–A4 experiments support the relevant estimand.

The paper must not claim that it invents decentralized peer review, graph-based reviewer selection, topic reputation, anonymous reputation, immutable review records, fair assignment, or provenance standards. It must not equate conformance with scientific validity, reviewer competence, real-world anonymity, or improved governance.

## Contribution table

| Contribution class | Proposed contribution | Required evidence | Current posture |
|---|---|---|---|
| Prior art (P) | Bounded synthesis of repository peer review, local/global trust, attack-resistant graph metrics, fair assignment, anonymous accountability, and scholarly exchange standards | Primary-source citations plus the dated closest-work matrix | Draft audit exists; source verification remains a gate |
| Synthesis/taxonomy (D) | Separation of shared claim/evidence events from root-, domain-, topic-, capability-, policy-, and time-relative trust views | TDRG definitions and crosswalk to prior constructs | Proposed design |
| Protocol choice (D) | Fresh case personas; separated authorities; typed review, reliance, and conduct events; importer-approved bridges; nontransitive adverse information; forkable policy overlays | Normative v0.1 text, schemas, examples, and review | Draft protocol exists; schemas pending |
| Formal result (T) | None required for this paper; any theorem belongs in Paper 02 and must be imported by immutable reference | Model, proof, and independent checking | Out of scope unless later supplied |
| Implementation result (I) | Reference tooling validates objects, replays policies deterministically, and exercises declared failure cases | Tagged code release, CI report, fixtures, environment and run manifest | Not yet admissible |
| Comparative empirical result (E) | A0–A4 behavior under frozen synthetic populations and attacks | Preregistered design, seeds, datasets, reports, uncertainty and adverse results | Not yet admissible |
| Field or human-subject result (E) | None | Paper 04 ethics-approved study | Explicitly out of scope |

## Proposed manuscript architecture

### 1. Abstract

Use four moves only: the governance problem; the protocol separation; the reference-evaluation contract; the bounded result. Until results exist, describe tests as planned and the protocol as a draft. The final sentence must distinguish machine-checkable conformance from scientific or social validity.

### 2. Introduction

1. Start from the machine-verifiable scientific record: claim/evidence objects can be preserved even when communities disagree about who should review or be relied upon.
2. State the scaling failure: one global reputation score creates an unnecessary common failure domain and erases topic, capability, policy, time, and relying-party context.
3. State the privacy/governance tension: review must be case-anonymous under a declared adversary model while duplicate participation, private appeals, and narrowly authorized conduct processes remain possible.
4. State the contribution as protocol composition and falsifiable evaluation, not invention of the component mechanisms.
5. Preview the limits: trust routing is not scientific disposition; synthetic tests are not a field trial; anonymity is conditional on operators and metadata controls.

### 3. Related work and novelty boundary

Organize by function, not by project chronology:

- repository-mediated and decentralized peer review;
- reviewer discovery, fair assignment, and assignment privacy;
- global, local, and attack-resistant trust metrics;
- topic-scoped and anonymous reputation;
- verifiable credentials, transparency logs, and accountable opening;
- NISO peer-review terminology, COAR Notify, DocMaps, and Crossref peer-review metadata;
- research objects, provenance, and claim/evidence records inherited from MCRP.

End with a feature-level closest-work table. Explicitly identify which components are reused, profiled, or constrained. Avoid “first,” “novel decentralized,” and “trustless.”

### 4. Requirements and threat model

Derive the protocol requirements from the v0.1 threat model:

- malicious, negligent, poorly calibrated, coerced, or conflicted reviewers;
- Sybils and real-person collusion;
- captured roots, boards, managers, registrars, publishers, evaluators, or opening trustees;
- review rings, bad-mouthing, whitewashing, on/off behavior, prestige laundering, and cross-topic leakage;
- metadata-, prose-, graph-, timing-, and small-pool deanonymization;
- stale credentials, rollback, partitions, compromised services, and malicious agent inputs.

For every threat, state the protected property, trusted operators, collusion assumptions, residual risk, and testability. A signature is not evidence of personhood, competence, independence, honesty, or truth.

### 5. Protocol profile

Present the minimum semantic objects and invariants, with the normative draft as the authoritative source:

1. immutable versioned domain manifest;
2. distinct identity record, domain account, and fresh review-case persona;
3. separated identity, eligibility, assignment, publication, reputation, policy, adjudication, and opening authorities;
4. typed evaluation, reliance, adverse-event, appeal, and scientific-disposition objects;
5. root-relative trust-view snapshot over one topic/capability layer and frozen inputs;
6. importer-approved, attenuated cross-domain bridge;
7. fork/fission lineage over a shared immutable scientific and review record;
8. transparency/privacy log and bounded opening procedure;
9. explicit conformance statement and promotion gate.

Each subsection must include an anti-claim: what the object does **not** prove.

### 6. Reference implementation contract

The tooling release must expose, at minimum:

```text
schemas/          normative object schemas and versioning rules
fixtures/         valid, invalid, adversarial, stale, and restricted examples
src/              deterministic policy evaluator and reporting code
tests/            unit, property, integration, attack, and round-trip tests
reports/          machine-readable and human-readable result bundles
environment/      locked environment and platform declarations
RUN.md            exact commands, seeds, resource envelope, and expected outputs
ATTESTATION.*     release digest, CI identity, signatures/receipts if used
```

Every report must bind the protocol version, schema digests, code revision, environment digest, configuration, seed stream, synthetic population/event snapshots, clock, hardware/compute class, and test result. Restricted inputs must be represented by disclosed commitments and access-class metadata rather than copied into a public artifact.

### 7. Conformance and adversarial test matrix

The tooling team should preserve these stable IDs. Splitting a row is allowed; silently changing its meaning is not.

#### Current v0.1 implementation slice versus roadmap

The first v0.1 artifact is intentionally a bounded slice of this matrix. Subject to an immutable verification report, it may support only:

- partial TM-01 schema/manual validation;
- TM-02 deterministic policy replay;
- the topic-mismatch and exact bridge-deny/bridge-allow cases within TM-06;
- the event-type separation cases within TM-04;
- revocation, expiry, and declared time-decay cases within TM-15, but not rollback/partition recovery;
- root-relative output binding within TM-07, but not the comparative frontier/collusion claim;
- malformed and malicious input rejection within TM-17, but not a general agent-security claim.

The current slice does **not** implement or validate negative-edge propagation defenses, A0–A4 collusion/capture comparisons, persona unlinkability or anonymity, appeals/opening, fork/reconciliation behavior, standards round trips, or stale-evaluator rollback. Those remain roadmap items. The paper must report coverage at the subtest level and must not use a partial row to imply that the whole row passed.

| ID | Property under test | Minimum fixture or comparison | Passing observation | Supports |
|---|---|---|---|---|
| TM-01 | Object/schema conformance | Valid and minimally mutated invalid instances of every object | Valid instances accepted; each invalid mutation rejected with a stable reason | I: parser/schema behavior |
| TM-02 | Deterministic policy replay | Same frozen events, roots, clock, policy, evaluator, and parameters repeated across clean runs | Byte-identical canonical view or documented semantically identical digest | I: replayability |
| TM-03 | Policy sensitivity | Change exactly one declared policy input | Explainable output delta attributable only to that change | I: explicit policy dependence |
| TM-04 | Event-type separation | Votes, review evaluations, scientific dispositions, allegations, and conduct findings on one case | No forbidden conversion or automatic standing/sanction update | I: separation invariant |
| TM-05 | Negative-edge containment | Bad-mouthing and enemy-of-enemy graphs | Adverse events do not propagate or create inferred positive trust | I: nontransitivity |
| TM-06 | Topic/capability isolation | Same actor across multiple layers with absent, expired, and valid bridges | No unapproved transfer; accepted transfer obeys attenuation and supervision | I/E: leakage rate |
| TM-07 | Root relativity and frontier bounds | Honest and captured roots; Sybil edges at varying frontier capacity | Views bind roots; influence respects declared capacity rule | I/E: capture radius |
| TM-08 | Control diversity | Path-disjoint actors sharing employer, supervisor, funding, or infrastructure | Common control is reported and constrained separately from graph diversity | I/E: concentration |
| TM-09 | Fair routing and newcomer access | Sparse newcomers, specialists, workload, and comparable eligibility | Sampling follows declared workload/newcomer policy; top rank is not deterministically selected | I/E: waiting time and exclusion |
| TM-10 | Per-case persona and replay defense | Same domain account across two cases plus duplicate review/vote attempts | Distinct public personas; permitted within-case continuity; duplicate submissions rejected | I: case scoping |
| TM-11 | Anonymity-claim downgrade | Timing, rare attribute, graph, prose, and small-pool attacks | Linkage measured; output says `confidential` when declared threshold is missed | I/E: privacy loss |
| TM-12 | Authority collusion boundary | Registrar/publisher, registrar/custodian, assignment/custodian, manager/trustee coalitions | Capabilities and privacy losses match the manifest; overclaims fail conformance | I: threat declaration |
| TM-13 | Appeals and opening | Qualified dissent, false allegation, reversal, and unauthorized management request | Scientific appeal stays identity-free; corrections append; unauthorized opening rejected | I/E: reversal/opening rates |
| TM-14 | Fork and bridge governance | Captured parent/root, child fork, export, selective recognition, later reconciliation | Shared records retain identifiers; policy views diverge explicitly; private state is not copied without consent | I/E: localization |
| TM-15 | Staleness and rollback | Expired credentials, delayed revocation, partitions, old evaluator, clock changes | Stale/unknown/restricted remain distinct; rollback is detected or declared | I: freshness handling |
| TM-16 | Standards projections | COAR Notify, DocMaps, Crossref, and NISO fixtures including restricted extensions | Round trip preserves identity scope, claim scope, signatures, challenges, supersession, and policy meaning | I: interoperability |
| TM-17 | Agent-input safety | Prompt injection and malicious document/metadata fixtures | Data cannot alter policy or execution authority; incident is retained | I: declared input boundary |
| TM-18 | Comparative arms A0–A4 | Identical synthetic actors, cases, events, attacks, seeds, and assignment method | Complete result bundle with uncertainty, subgroup results, costs, and adverse outcomes | E: comparative hypotheses |

Passing any implemented subtest establishes only the recorded behavior for that exact fixture and release. Completion of TM-01–TM-17 would establish only tested implementation behavior under the recorded fixtures. TM-18 can support only synthetic comparative claims. Neither establishes real-community benefit.

### 8. Comparative evaluation

Freeze all arms before outcome inspection:

- **A0:** eligibility plus uniform random routing, no reputation;
- **A1:** raw feedback average or vote count, deliberately weak popularity baseline;
- **A2:** global EigenTrust/PageRank-like recursive score;
- **A3:** topic-scoped personalized restart walk;
- **A4:** A3 after frontier capacity bounds, followed by control-diversity, workload, and newcomer constraints.

Use identical actors, scientific cases, planted defects, harmless deviations, false alarms, unresolved disputes, event order, and downstream adjudications across arms. Hold the fair/randomized assignment procedure constant after eligibility so assignment quality is not misattributed to the trust model.

Primary measures are capture radius, false eligibility/exclusion, material-defect yield per reviewer-hour, minority survival, cross-topic leakage, control concentration, newcomer access, appeal quality, privacy loss, operational cost (including human and agent intelligence), deterministic replay, and fork localization. Report distributions and topic/newcomer/minority subgroups, not averages alone.

Before running the confirmatory suite, freeze:

- the data-generating process and ground-truth construction;
- scenario and seed counts justified by precision or power analysis;
- primary contrasts and multiplicity control;
- acceptable bounds for newcomer/minority exclusion and privacy failure;
- treatment of failed runs, missing outcomes, and unresolved cases;
- sensitivity grid and which analyses are confirmatory versus exploratory;
- stop/no-go conditions from the evaluation design.

### 9. Results

This section must remain an explicit placeholder until an immutable report exists. Use one subsection per claim rather than one per attractive plot. Report failed tests, null results, subgroup harms, resource costs, and sensitivity to roots/parameters. A result from a synthetic fixture must be called synthetic.

### 10. Discussion

Separate:

1. conformance achieved by the implementation;
2. comparative behavior in synthetic regimes;
3. unresolved security/privacy properties;
4. field questions reserved for Paper 04;
5. operational tradeoffs, including compute, storage, governance labor, and human/agent intelligence;
6. conditions under which TDRG should be reduced to an interoperability vocabulary rather than promoted as a governance mechanism.

### 11. Limitations and trust boundaries

At minimum: synthetic ground truth; model-dependent attacks; untested collusion; small anonymity pools; prose stylometry; credential sharing; compromised issuers; uncertain competency; dependence on external assignment and cryptographic mechanisms; stale software/standards; restricted evidence; evaluator implementation errors; and the inability of graph standing or conformance tests to establish scientific correctness.

### 12. Reproducibility and release statement

Apply MCRP to this paper itself. Map each claim to source, schema, fixture, run, or open hypothesis. Archive tagged paper and tooling releases with immutable identifiers where permitted. Record software/data licenses and access restrictions. Include freshness dates for standards and dependencies, scheduled rerun policy, and a visible supersession/adverse-status event if later re-execution fails.

## Falsifiable hypotheses

- H1: A3/A4 reduce capture radius relative to A2 when malicious influence enters through a bounded frontier.
- H2: A4 reduces capture from dense review rings relative to A3, with a measurable coverage cost in sparse domains.
- H3: explicit topic/capability scoping and importer-approved bridges reduce cross-topic false eligibility relative to A2 without unacceptable multidisciplinary exclusion.
- H4: delayed typed outcomes preserve qualified dissent better than raw votes.
- H5: forked overlays localize a captured policy/root while preserving common scientific and review objects.
- H6: brokered per-case personas enforce duplicate limits and private appeals, but correctly downgrade anonymity claims under timing, attribute, graph, prose, or small-pool attacks.

These remain hypotheses until the frozen evaluation report exists.

## Review gates

- **G0 Argument:** claim ledger and outline reviewed for non sequiturs and overclaiming.
- **G1 Scholarship:** every high-risk novelty comparison checked against primary sources and current standards.
- **G2 Methods:** schemas stable; A0–A4 faithful; test matrix and stop rules frozen before confirmatory outcomes.
- **G3 Artifact:** tagged protocol/tooling, locked environment, immutable fixtures/reports, rerun command, and release attestation.
- **G4 Independent review:** external-to-drafting reviewers challenge threat model, privacy/security, implementation, statistics, and domain assumptions.
- **G5 Human release:** authors approve authorship/AI record, licensing, access controls, venue/fees, and submission.

## Drafting stop conditions

Stop or narrow the manuscript if the implementation cannot replay views from frozen inputs; if topic leakage, event-type conversion, unauthorized opening, or record-destructive forks remain possible; if A4 does not materially differ from simpler baselines; if harms to newcomers/minority views exceed frozen bounds; or if the closest-work audit shows the claimed contribution is only relabeling.
