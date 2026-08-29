# Paper 01 outline — A design map for plural, machine-verifiable scientific review

Status: working outline; private; not approved for submission  
Provisional article type: design map / critical synthesis with worked cases  
Primary contribution posture: unification, clarification, and operational consolidation

## Research question and bounded answer

**Research question.** What information and governance structures are required for a machine-verifiable scientific record to support reproducibility review by independent actors who differ in expertise, resources, incentives, and trust relationships?

**Answer the paper is designed to support.** Existing reproducibility, provenance, archival, peer-review, graph-trust, anonymous-credential, and polycentric-governance mechanisms can be composed into a coherent two-layer architecture: a shared claim/evidence record and plural, scoped trust-domain views; the design map makes the composition and its unresolved tradeoffs explicit, but does not establish scientific correctness or the empirical superiority of any trust mechanism.

## Candidate title and abstract spine

**Working title:** *From Executable Artifacts to Plural Review: A Design Map for the Machine-Verifiable Scientific Record*

**Abstract spine:**

1. Computational-publication systems often make papers, code, data, or environments addressable, but scientific assessment also depends on claim-specific evidence, transitive tools, reviewer competence, resource feasibility, and institutional trust.
2. The relevant mechanisms are fragmented across scholarly communication, reproducibility, workflow provenance, research-object standards, archival infrastructure, graph trust, privacy-preserving credentials, and polycentric governance.
3. We provide a critical design map that distinguishes epistemic states, resource profiles, record objects, review actions, and governance decisions.
4. We synthesize a two-layer architecture: an immutable or version-addressed claim/evidence record plus local, topic/capability/time/policy-specific trust views over independent review actors.
5. Two worked cases—portable laptop execution and an HPC/restricted-data workflow—show how full reruns and evidence downselects can satisfy different review obligations without being mislabeled as equivalent.
6. We identify explicit trust boundaries, interoperability obligations, falsifiers, and an evaluation agenda; automation checks records and consistency but does not prove scientific validity.

## Contribution table

| Contribution class | What this paper may claim | What it must not claim | Required support |
|---|---|---|---|
| Established prior art | Reproducibility services, workflow provenance, research objects, review metadata, graph trust, anonymous accountability, and polycentric governance each cover important parts of the problem. | That these mechanisms are new, absent, or ineffective merely because they are not integrated here. | Dated primary-source table plus source-specific scope notes. |
| Synthesis/taxonomy | A common vocabulary separates epistemic achievement, record completeness, resource burden, and governance reliance. | That a taxonomy alone demonstrates better review outcomes. | Definitions reconciled with primary standards and representative systems; worked classifications. |
| Design map | A shared claim/evidence record can be separated from plural trust overlays through typed, versioned interfaces. | That this is the only valid architecture or a proof of correctness. | Explicit objects, interfaces, invariants, trust boundaries, and counter-designs. |
| Protocol choice | Claim-to-evidence mappings, review coverage contracts, multiaxis resource profiles, local typed trust views, and forkable governance are proposed defaults. | That defaults are empirical facts or universal mandates. | Rationale, alternatives, failure modes, and conditions for revision. |
| Worked cases | The map can represent both a lightweight full execution and an expensive/restricted workflow with downselected evidence. | That a synthetic or sanitized case establishes field effectiveness. | Complete, inspectable case records and a checklist application. |
| Evaluation agenda | Specific comparisons and adversarial tests can discriminate useful consolidation from relabeling. | That future tests have already succeeded. | Preregisterable outcomes, baselines, falsifiers, and stop rules. |

## Central distinctions

These distinctions are definitions or design commitments, not empirical findings.

### Epistemic achievement ladder

1. **Rerenderability:** regenerate a presentation artifact from preserved derived values; useful, but compatible with fabricated, stale, or scientifically invalid upstream work.
2. **Computational repeatability:** rerun the same implementation with materially equivalent inputs and environment and obtain results within declared tolerances.
3. **Computational reproducibility:** an independent actor reconstructs the reported computational result from identified data, code, configuration, dependencies, and workflow, with discrepancies explained.
4. **Independent replication:** a materially independent implementation, dataset, method, or experiment tests the same scientific claim.
5. **Scientific validity:** the claim survives appropriate domain scrutiny of assumptions, calibration, measurement, inference, uncertainty, alternatives, and external knowledge.

The paper will emphasize that the ladder is not a single scalar badge. A release can be strong on preservation and repeatability while remaining weak on independent replication or scientific validity.

### Four orthogonal record dimensions

| Dimension | Question answered | Examples of captured objects |
|---|---|---|
| Claim/evidence | What exact assertion is supported by what evidence and reasoning? | claim IDs, tables/figures, likelihoods, diagnostics, derivations, reviewer findings |
| Provenance/identity | Which versioned inputs, transformations, environments, tools, and actors produced the evidence? | raw/intermediate/derived digests, workflow runs, commits, containers, calibrations, service responses |
| Resources | What would another actor need to inspect or reproduce the result? | compute, accelerator, storage, wall time, scheduler, access, human expertise, agent assistance, support labor |
| Governance/reliance | Who reviewed which scope, under which policy, and whose judgment does a relying domain accept? | review requests, scoped credentials, reports, challenges, local trust roots, bridges, forks, sign-offs |

### Multiaxis resource profile

Avoid a one-dimensional “reproducibility level.” Each evidence path declares a vector:

```text
R = (compute, storage, data-access, platform, wall-clock,
     human-expertise, agent-capability, operator/support, monetary cost, freshness)
```

The profile supports multiple **assessment modes** for one claim:

- full independent execution;
- reviewer-controlled downselect over raw or reduced inputs;
- verification of digest-generation algorithms plus sampled recomputation;
- attested execution on a restricted platform;
- inspection of frozen outputs, invariants, logs, and provenance when rerun is infeasible;
- independent replication through a different evidence path.

Modes must state what they do and do not establish. A cheaper mode is not silently promoted to full reproduction.

## Manuscript structure

### 1. Introduction: preserving records is not yet scaling review

**Purpose:** establish the problem and the bounded thesis.

- Open with a concrete contrast: rebuilding a figure from saved data versus validating the measurements, transformations, calibrations, inference, and transitive tools that make the figure evidence.
- Explain why agentic execution increases both opportunity and risk: agents can inspect larger evidence graphs, but can also reproduce cosmetic outputs, inherit tool errors, and manufacture persuasive audit trails.
- Identify the actor problem left after record preservation: eligibility, competence, independence, anonymity, accountability, institutional capture, cross-domain reliance, and dissent.
- State the two-layer thesis and the no-global-score design posture.
- List contributions using bounded verbs: synthesize, distinguish, operationalize, map, and derive an evaluation agenda.
- State non-contributions up front: no proof that peer review yields truth; no new universal trust metric; no novel cryptographic primitive; no claim that machine checks replace scientific judgment.

### 2. Method: critical design synthesis and primary-source gap audit

**Purpose:** make the design map reviewable rather than an impressionistic essay.

#### 2.1 Corpus construction

- Define literature families before search: computational reproducibility; executable papers/continuous analysis; workflow and provenance standards; research objects and persistent identifiers; software/data archival and licensing; peer-review metadata and assignment; local/global graph trust and Sybil resistance; anonymous credentials/accountable anonymity; multilayer networks; polycentric governance; agentic reproducibility assessment.
- Record databases, exact queries, dates, inclusion/exclusion rules, backward/forward citation search, and deduplication.
- Prefer normative standards, system papers, original algorithm papers, and primary empirical studies over reviews for consequential claims.
- Freeze a source ledger and report the final-search date. Mark 2025–2026 preprints as non-peer-reviewed where applicable.

#### 2.2 Feature-level comparison

- Compare systems at the object/interface level, not by name or marketing category.
- Required columns: claim granularity; raw/intermediate/derived identity; environment/workflow capture; compute/resource declaration; transitive dependencies; validation/invariants; human sign-off; anonymity/accountability; local versus global trust; topic/capability scoping; archival versioning; freshness/correction; restricted/HPC support; interoperability.
- Invite contradiction: for each claimed gap, search for a system that already supplies the feature or composition.

#### 2.3 Design derivation

- Trace each proposed requirement to (a) a documented failure mode, (b) an existing standard or mechanism, or (c) an explicit design judgment.
- Maintain the claim ledger in `CLAIMS.md`.
- Separate standards profiling from invention: reuse PROV-O, RO-Crate/Workflow Run RO-Crate, persistent identifiers, COAR Notify, DocMaps, Crossref peer-review metadata, and NISO terminology where they fit.

#### 2.4 Limitations of the method

- This is a critical design synthesis, not initially a registered systematic review or meta-analysis.
- English-language and database coverage may omit practice embedded in collaborations, internal review boards, observatories, regulated science, or non-public infrastructure.
- A diagram showing compatible interfaces does not establish deployability, security, adoption, or better scientific decisions.

### 3. Landscape: what the existing components establish

**Purpose:** present prior art as foundations and constraints, not foils.

#### 3.1 Executable and independently checked computational work

- JOSS: repository-centered software review and open-source quality expectations.
- ReScience C: independent reimplementation and replication/reproduction reports.
- CODECHECK: independent execution during scholarly review and certificate/report artifacts.
- Executable-paper and continuous-analysis systems: automated regeneration and environment capture.
- Distinguish each system's unit of review and strongest warranted epistemic claim.

#### 3.2 Provenance, research objects, and archival identity

- W3C PROV-O; CWLProv; RO-Crate and Workflow Run RO-Crate.
- Software/data releases, version-specific and concept identifiers, content digests, archival deposit, licensing, and access metadata.
- Identify what these standards encode and what remains a domain judgment.

#### 3.3 Claim-level knowledge representation

- Evidence graphs, micropublications, nanopublications, and related claim/evidence models.
- Test whether the proposed claim manifest is a profile/composition of existing models rather than a new ontology.

#### 3.4 Review exchange and reviewer assignment

- COAR Notify, DocMaps, Crossref peer-review metadata, and ANSI/NISO peer-review terminology.
- Repository-mediated peer review and graph-based reviewer selection.
- Fair/randomized assignment methods and their adversarial threat models.

#### 3.5 Trust and adversarial participation

- EigenTrust/global recursive reputation; personalized/local trust; max-flow/capacity defenses; signed networks; multilayer networks.
- Anonymous reputation, anonymous credentials, blind tokens, scoped nullifiers, and the unavoidable linkage boundary.
- Explicitly preempt novelty claims for global/local trust, graph routing, anonymity plus accountability, or topic-specific reputation.

#### 3.6 Polycentric and forkable governance

- Nested and polycentric governance as an institutional lens.
- Separate shared event/data interoperability from local policy authority.
- Treat forks as containment and exit, not adjudication of scientific truth.

#### 3.7 Agentic assessment

- Assess emerging agents that reproduce, inspect, or review scientific workflows.
- Separate demonstrations of task completion from evidence of scientific-review reliability.
- Require disclosure of model/tool versions, prompts/policies, external services, human interventions, uncertainty, and failure cases.

### 4. The consolidated design map

**Purpose:** define the minimum coherent architecture without presenting it as the only possible one.

#### 4.1 Layer A: shared claim/evidence record

Minimum objects:

- immutable release and mutable project identities;
- individually addressable claims with scope and uncertainty;
- evidence links and transformation paths;
- raw, intermediate, and derived data identities;
- source, environment, workflow, configuration, randomness, hardware/compute, and external-service records;
- validation tests, scientific invariants, negative/adversarial tests, and human sign-off;
- transitive-tool/data/calibration trust boundaries;
- licenses, access restrictions, retention, archival location, and attestations;
- freshness policy, scheduled checks, supersession, correction, and failed-reproduction events.

#### 4.2 Layer B: plural review governance

Minimum objects:

- review requests scoped by claim, capability, role, and evidence path;
- fresh per-case public personas with private accountability and stated unlinkability limits;
- review reports, responses, challenges, appeals, and dispositions as distinct event types;
- local trust views computed from declared roots, topic, capability, policy, event cut, and time;
- institution/control diversity and conflicts separated from graph score;
- importer-approved, attenuated, expiring cross-domain bridges;
- domain forks that retain the common record while changing roots or policy;
- no universal `trusted=true` and no public scalar leaderboard.

#### 4.3 Interface between the layers

A review action references exact claim IDs, evidence IDs, release digests, requested competence, assessment mode, resource declaration, and policy version. A trust view may route attention or document reliance; it cannot change evidence or make a scientific claim true.

#### 4.4 Minimal invariants

1. Every consequential review conclusion points to a claim/evidence scope.
2. Derived views never rewrite signed source events.
3. Trust is typed, directed, expiring, and root-relative.
4. Negative events do not propagate into unrelated domains by default.
5. A cheaper assessment mode cannot be reported as a stronger epistemic achievement.
6. Transitive dependencies and restricted components are explicit trust boundaries, not omitted nodes.
7. Machine checks report conformance and discrepancies; designated humans make scientific and governance decisions.
8. Later failures append a new status/correction event and do not erase the previously reviewed release.

### 5. Worked case A: portable Level-0 computational analysis

**Instantiated scenario:** a contemporary laptop-scale analysis of the public
GWOSC GW150914-v2 H1/L1 strain products, using portable locked tools, no specialty
scheduler, about 2 MB of registered input, and a deterministic workflow. The
release candidate checks exact source identity and event-time quality metadata,
recomputes a bounded lag-correlation invariant, and exercises digest/version and
adversarial-shift failures. Separate-agent replay and bounded human GW acceptance
are recorded; independent scientific replication remains absent.

**Walkthrough:**

1. Freeze three scientific claims and their figure/table evidence.
2. Identify raw, intermediate, and derived artifacts by digest and archive release.
3. Capture code commit, environment lock, configuration, seed, commands, expected resource envelope, and tolerances.
4. Execute positive tests, scientific invariants, and at least one negative test that should fail under a corrupted input or invalid configuration.
5. Assign independent scientific and provenance review scopes.
6. Record reviewer-controlled execution, discrepancies, responses, and human sign-off.
7. Schedule a freshness run and append a failure/supersession event if dependency drift later breaks execution.

**What the case can establish now:** bounded computational repeatability of the
registered path, satisfaction of one necessary lag invariant, machine conformance
of the record, and implementation of the ten-axis/lifecycle representation.

**What it cannot establish:** the original search, calibration validity,
astrophysical origin, independent replication, general scientific validity,
security of identity services, or scalability to HPC.

### 6. Worked case B: HPC/GPU/restricted-data workflow with downselects

**Scenario:** a RIFT-like scientific inference workflow needing a specialty scheduler, GPUs, substantial compute/storage, domain calibrations, and possibly restricted or too-large raw inputs. The published case must use public or sanitized material and disclose that it is representative rather than an internal collaboration audit.

**Walkthrough:**

1. Decompose claim evidence into acquisition/calibration, preprocessing, expensive inference, reduced posterior or likelihood products, diagnostics, and final claims.
2. Declare the full resource vector, including scheduler, accelerator class, software stack, storage tiers, wall time, monetary/allocative cost, operator support, domain expertise, and agent assistance.
3. Provide several explicitly labeled assessment modes:
   - full rerun for a suitably resourced independent site;
   - reviewer-controlled reduced-scale rerun with convergence/scaling checks;
   - sampled regeneration of digested products from accessible partitions;
   - inspection and tests of the digest-generation algorithm;
   - trusted attestation plus audit logs for restricted data or platforms;
   - independent alternative-method check on a bounded claim.
4. Map transitive tools, waveform/calibration/data products, external services, and scheduler/container runtime as reviewed or accepted external trust boundaries.
5. Use a coverage contract spanning domain science, statistics, provenance/software, compute operations, and restricted-data governance; do not average those competencies.
6. Record exactly which claims remain unverified when cost, access, retention, or confidentiality blocks full execution.

**What the case can establish:** the architecture can represent heterogeneous evidence paths and honest partial assessment without treating them as equivalent.

**What it cannot establish:** that downselected evidence detects every material error, that attestations are honest, or that the resource package is sustainable across institutions.

### 7. Adversarial and negative analysis

Apply the design map to failure scenarios:

- a Makefile regenerates figures from saved values while upstream computation is absent;
- a preserved container calls a mutable external model or service;
- raw data are restricted and the attesting institution is conflicted;
- two tools share the same erroneous calibration library;
- a reviewer has graph prestige in the wrong topic;
- one manager controls assignment, private identity linkage, and sanctions;
- public review personas are linkable through timing, stylometry, or a tiny expert pool;
- a global score suppresses a qualified minority or newcomers;
- a fork retains evidence but not private identity maps or inherited distrust;
- a scheduled rerun fails after environment or hardware drift.

For each, report whether the architecture prevents, detects, localizes, merely records, or does not address the failure.

### 8. Evaluation and falsification agenda

#### 8.1 Design-map evaluation

- **Coverage test:** can independent annotators map representative systems and both cases without inventing new fields?
- **Interoperability test:** can core objects project into established provenance, research-object, and review-event standards with documented loss?
- **Decision test:** do declared assessment modes and coverage contracts change what a reviewer can honestly sign?
- **Complexity test:** measure author/reviewer/operator burden, not only machine runtime.
- **Adversarial test:** evaluate missing/stale provenance, captured roots, topic leakage, collusion, privacy leakage, newcomer exclusion, and restricted-access claims.

#### 8.2 Baselines/counter-designs

- paper-to-repository link plus Makefile;
- reproducible container without claim mapping;
- global recursive reviewer reputation;
- raw review voting;
- one centralized review board;
- shared event history with no cross-domain trust overlay;
- local typed trust plus explicit bridges/forks (proposed profile).

#### 8.3 Falsifiers and downgrade rules

Downgrade the contribution to a vocabulary or interoperability profile if:

- primary-source review finds an existing end-to-end system with materially the same object model and governance semantics;
- worked cases require exceptions that erase the claimed separation between evidence and actor reliance;
- independent annotators cannot apply the distinctions reliably;
- standards mapping reveals avoidable reinvention or incompatible semantics;
- resource/downselect modes obscure rather than clarify what was actually assessed;
- plural trust overlays cannot be evaluated without reconstructing a de facto global authority;
- the added record burden is disproportionate to decisions enabled.

No result in this paper may establish improved peer-review quality without a separate empirical study.

### 9. Discussion

- Why “fully runnable” is a valuable floor for lightweight work but not a universal admission rule for valuable science.
- Why resource burden and epistemic strength are separate axes.
- Why human and agent intelligence are resources with identity, capability, cost, provenance, and accountability—not free ambient infrastructure.
- Why review bottoms out in explicitly accepted external tools, data, calibrations, institutions, and human judgment.
- Why local trust contains disagreement but does not resolve it.
- How the design relates to MCRP v0.1 without making TDRG core conformance prematurely.
- Governance hazards: prestige loops, management capture, retaliation, exclusion, privacy failure, responsibility diffusion, and fragmentation.

### 10. Limitations and scope conditions

- The synthesis may miss private or discipline-specific review practices.
- No universal maximum trust-domain size is justified.
- No graph method proves competence, independence, uniqueness, good faith, or scientific truth.
- Per-case anonymity is conditional on service separation, pool size, traffic patterns, content, and opening policy.
- Restricted and expensive workflows may remain only partially assessable.
- Archival identity does not guarantee future executability.
- Resource declarations may be inaccurate without independent measurement.
- Agent-assisted assessment inherits model, tool, prompt, service, and operator dependencies.
- Forking can localize capture but may also fragment authority, increase burden, or enable avoidance of accountability.
- The two worked cases demonstrate coverage, not population-level effectiveness.

### 11. Conclusion

Reiterate only the bounded result: a machine-verifiable scientific record needs both exact evidence/provenance objects and explicit, plural governance over reviewer reliance. The design map turns hidden assumptions into reviewable interfaces and hypotheses; its value depends on primary-source verification, interoperable implementation, adversarial testing, and independent scientific review.

## Figures and tables

1. **Figure 1:** epistemic achievement ladder crossed with record, resource, and governance dimensions (avoid depicting a single total order).
2. **Figure 2:** two-layer architecture—shared event/evidence substrate below plural local trust-domain views.
3. **Figure 3:** full-rerun and downselect evidence paths for the HPC case, each terminating in a bounded sign-off.
4. **Table 1:** contribution table separating prior art, synthesis, design, implementation, and evidence.
5. **Table 2:** closest-work feature matrix with source date and gap status.
6. **Table 3:** multiaxis resource profile and supported assessment modes for both cases.
7. **Table 4:** threat/failure scenario mapped to prevent/detect/localize/record/not-addressed.
8. **Box 1:** anti-patterns: cosmetic Makefile; paper-to-repository equivalence; universal badge; hidden external service; transitive-tool blindness; global reviewer score; anonymous prestige identity; machine validity certification.

## Primary-source gap-check plan

Before prose drafting reaches G1, complete the following. Each row must record exact search date, primary source, quoted-or-paraphrased feature evidence, and decision impact.

| Gap question | Starting sources | Required check | Stop/downgrade condition |
|---|---|---|---|
| Does an existing publication architecture already join claim-level records to plural local trust policies? | Micropublications; evidence graphs; Traxia; decentralized-science systems | Inspect schemas, implementations, identity/trust semantics, and correction model—not abstracts alone. | Same composition and semantics already implemented and evaluated. |
| Is the proposed claim manifest merely an existing profile? | PROV-O; RO-Crate; Workflow Run RO-Crate; nanopublications; evidence graphs | Field-by-field mapping with documented loss and extensions. | A standard profile covers the need without extension. |
| Are resource tiers/vectors already standardized for computational review? | ACM artifact badges; CODECHECK; executable-paper systems; domain reproducibility checklists | Compare compute, storage, access, expertise/support, and downselect semantics. | Existing standard already supplies equivalent axes and sign-off language. |
| Are local topic/capability trust views and bridges established in reviewer systems? | Local trust; multilayer networks; anonymous-review reputation; reviewer assignment | Compare boundary conditions, topic transfer, time, policy, uncertainty, and public/private outputs. | Residual difference is only terminology. |
| Are accountable one-case personas already deployable in scholarly review? | Fair anonymous review; AnonRep; anonymous credentials; Privacy Pass/scoped-nullifier work | Threat-model comparison including issuer/verifier collusion, opening, appeals, timing, stylometry, and small pools. | Proposed profile weakens prior guarantees without an operational benefit. |
| Do review-event standards already express challenges, supersession, and forks? | COAR Notify; DocMaps; Crossref metadata; NISO terminology | Build lossless/lossy projection table and example events. | New event vocabulary duplicates established terms. |
| What does agentic reproduction evidence actually establish? | ARA; coding-agent replication; agent provenance work | Examine task definitions, benchmark construction, human evaluation, failures, model/service capture, and generalization. | Claims exceed evaluated scope or rely on unavailable artifacts. |
| Is polycentric governance an explanatory analogy or an operational model here? | Original polycentric-governance sources and empirical follow-ons | Identify falsifiable implications, known failure modes, and limits of transfer to scientific review. | Use remains metaphorical and adds no design constraint. |

## Worked-case artifact checklist

Each case packet must include:

- frozen claim manifest and evidence graph;
- raw/intermediate/derived data inventory and digests;
- source, environment, workflow, configuration, randomness, compute/hardware, and external-service records;
- validation, invariants, negative/adversarial tests, and tolerances;
- transitive dependency and accepted-boundary list;
- resource vector plus every supported assessment mode;
- review coverage contract, assignment scopes, reports, responses, and human sign-off;
- archive/version identifiers, licenses, access/retention restrictions, and attestation;
- freshness schedule and a simulated later-failure/correction event;
- explicit table of warranted and unwarranted conclusions.

## Drafting and review gates

- **G0 Argument:** an independent reader can reconstruct the chain from problem to bounded synthesis and distinguish proposed design from evidence.
- **G1 Scholarship:** every closest-work gap has a dated primary-source determination; no novelty rests on review articles or abstracts.
- **G2 Methods:** both cases and adversarial scenarios have preregisterable checks, counter-designs, and falsifiers.
- **G3 Artifact:** the exact design map, mappings, cases, source ledger, and validation outputs are versioned.
- **G4 Independent review:** at least one scholarly-communication reviewer, one computational scientist, and one governance/privacy reviewer challenge the work; their coverage is recorded rather than averaged.
- **G5 Human release:** authors approve claims, authorship/AI disclosure, security and privacy review, licenses, fees, preprint, and submission.

## Venue posture

First assess the diamond-open-access **Journal of Electronic Publishing** and the no-author-fee **Information Research** against the finished manuscript's scope. Treat JASIST/ARIST-style synthesis as a possible non-APC or RIT-supported route only after current terms are verified. Venue and agreement claims are time-sensitive: recheck the exact journal, article type, corresponding-author eligibility, annual caps, repository rights, and license immediately before submission. Do not submit, post a preprint, or incur a charge without G5 approval.
