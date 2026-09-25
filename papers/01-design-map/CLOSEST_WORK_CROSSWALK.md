# Paper 01 closest-work and standards crosswalk — v0.2

Audit dates: 2026-08-25–2026-08-26
Scope: a bounded scholarship-gate audit covering computational-publication,
continuous-analysis, workflow/capture, provenance, archival, review-event exchange,
and correction/supersession components omitted from the prior manuscript narrative.
Posture: primary papers, normative specifications, and official documentation only;
no claim of exhaustiveness, effectiveness, or novelty.

## Method and decision rule

The comparison dimensions were fixed before evaluating the added systems:
addressable unit; environment and execution capture; data and dependency lineage;
claim-to-evidence mapping; review/sign-off semantics; resource and access semantics;
archival identity; freshness/later-failure semantics; and the strongest conclusion
the source actually authorizes. A blank in a source is recorded as “not specified
in checked source,” not as proof that no implementation or later version supports
the feature.

Searches run on 2026-08-25 used title/DOI queries for “executable paper,” “Binder
2.0,” “continuous analysis,” “Whole Tale,” “Galaxy reproducible,” “ReproZip,” and
“Software Heritage archive reference,” plus official documentation searches for
Binder, Renku, RO-Crate, Workflow Run RO-Crate, and Zenodo versioning. Inclusion
required a primary paper, normative specification, or official project document
with a stable locator and a feature-level statement relevant to the dimensions.
On 2026-08-26, the search added “peer review terminology standard,” “review event
notification protocol,” “DocMaps review version,” “Crossref peer review metadata,”
“Crossmark correction update,” “journal article version standard,” “retraction
metadata standard,” “JATS related article correction,” and “DataCite Reviews
Obsoletes.” One-hop backward and forward linkage review started from the included
end-to-end and review-event sources, as documented below. Inclusion required a
primary paper, normative specification, or official project document with a stable
locator and a feature-level statement relevant to the dimensions. The audit is
targeted rather than systematic; absence from the table is not evidence of absence,
and broad novelty remains blocked.

## Feature-level crosswalk

| Component | Primary unit and captured mechanics | Scientific-review semantics in checked source | Lifecycle/resource observations | Closest MCRP role and remaining boundary |
|---|---|---|---|---|
| JOSS | Research-software repository, release, documentation, tests, and contribution/research relevance review. | Software review with an editorial decision; not a review of every scientific claim produced with the software. | Durable paper/repository linkage; resources and later scientific reruns are not its stated unit. | Reusable review of a transitive software dependency; MCRP still needs claim scope and accepted-boundary semantics. |
| ReScience | Independent computational replication report with code and result artifacts. | Review object is the replication and its implementation, stronger in independence than replaying the original implementation. | Sustainable code practice is explicit; general freshness and resource-vector semantics are not specified in the checked paper. | Independent-evidence-path mode; MCRP must state which original claims and shared dependencies the replication covers. |
| CODECHECK | Independent execution of computations underlying an article, with a certificate and report. | Makes an execution check inspectable; the paper explicitly distinguishes execution from broader reproducibility and validity. | Records an exact check, limitations, and environment information; expensive/restricted modes require additional policy. | Full or bounded execution report linked to exact claims; does not supply domain reliance governance. |
| ACM artifact badges | Artifact availability, functionality, and result-reproduction outcomes are separate badge categories. | Badge vocabulary limits the warranted conclusion rather than equating artifact review with truth. | Persistent identifiers are encouraged for availability; a badge is not a complete staleness event model. | Precedent for typed dispositions; MCRP adds per-claim scope, resources, boundaries, and later failures. |
| Jupyter + Binder | Notebook combines narrative, code, and outputs; Binder builds a temporary interactive environment from repository configuration. | Supports reader-controlled execution and modification; checked sources do not define scientific sign-off. | Dependency pinning is required for rebuild durability, and repository-size/service constraints are explicit. | R0 presentation/execution surface; must be paired with upstream identity, tests, claims, and non-service archival capture. |
| Continuous analysis | Version-control changes trigger a containerized rerun; results and run state are synchronized with code/data changes. | Produces an automated audit trail and executable environment, not an independent domain-validity judgment. | Strong freshness mechanism while CI, base images, data, and services remain available; cost/access policy is deployment-specific. | Scheduled re-execution and failure-event input; MCRP adds claim dispositions and accountable human review. |
| Whole Tale | “Tale” joins data, code, environment, narrative, workflow/process, and publication linkage in an executable research object. | Supports verification and reproduction as infrastructure; checked design paper does not define claim-specific scientific approval. | Explicitly addresses long-tail and data/compute-intensive work and uses persistent-identifier services. | Closest end-to-end packaging/environment component; MCRP contribution must be limited to review, claim, resource-mode, trust-boundary, and correction profiles that are not already present. |
| Galaxy | Domain workflow/history platform records tools, parameters, datasets, and reusable workflows; Conda/containers support tool environments and remote compute. | Enables transparent replay and sharing, but platform history is not itself an independent scientific review. | Directly treats large collections and backend scaling; deployment/operator support and reference-data services are material dependencies. | HPC/domain execution substrate; MCRP must surface platform, operator, reference-data, and transitive-tool boundaries. |
| ReproZip | System-call tracing captures files, libraries, environment information, and configuration into a portable experiment package. | Facilitates reviewer replay and modification; checked source does not map outputs to paper claims or authorize validity. | Captures otherwise implicit dependencies, subject to observed-execution coverage and platform assumptions. | Dependency-capture implementation option; needs declared capture scope, missed-dependency tests, claim mapping, and archival release. |
| PROV-O + CWLProv + RO-Crate/Workflow Run RO-Crate | Entity–activity–agent provenance, workflow prospective/retrospective provenance, packaged research objects, and run profiles with increasing granularity. | Representation standards do not determine whether a scientific assumption or calibration is acceptable. | Can carry identifiers, licenses, software, equipment, inputs/outputs, and run metadata; retention and execution policy remain external. | Preferred transport semantics; MCRP should profile rather than replace them and document every lossy extension. |
| Software Heritage + Zenodo | Software source/history can receive intrinsic granular identifiers; deposits/releases receive version-specific and concept-level DOIs. | Establishes retrieval/reference identity, not executability, review, or correctness. | Separates immutable versions from evolving concepts; preserved source still depends on environments, services, data, and hardware. | Archival identity layer; MCRP adds attested run identity, freshness windows, failed-rerun events, and supersession. |

## Review-event and correction/supersession crosswalk

| Component | Native unit and relation/event support | What the checked source does not establish | MCRP mapping decision |
|---|---|---|---|
| ANSI/NISO Z39.106-2023 | Controlled terminology for peer-review practices and their communication. | It is not a transport, event log, scientific disposition schema, or reviewer-reliance model. | Reuse terminology when describing review policy and process; retain MCRP claim scope, resources, mode, boundaries, and disposition separately. |
| COAR Notify 1.0.1 + Event Notifications | Linked Data Notifications transport with ActivityStreams payloads for requesting, accepting, rejecting, tentatively responding to, and announcing reviews or relationships. | Delivery of a message does not authenticate reviewer competence, prove report quality, or define a claim-level scientific verdict. | Use as an exchange envelope where applicable; require immutable event identity, review target, signer/role, and MCRP payload/profile reference. |
| DocMaps release 7 | Immutable assertions describing single- or multi-event editorial/review processes, links among documents, and process providers. | DocMaps is not a document representation, current-state service, notification protocol, or scientific-validity judgment; portable authenticity is not supplied by the base framework. | Reuse process-event assertions and links; add attestation, claim/evidence scope, assessment mode, resources, disposition, and later-event semantics. |
| Crossref peer-review metadata | DOI registration for reports, decision letters, author responses, post-publication reviews, anonymous roles, stages, types, rounds, recommendations, and required `isReviewOf` relation. | Registration identifies and relates a review object but does not establish competence, independence, evidentiary coverage, or local reliance. | Register public review objects when policy permits; keep observer-relative private accountability and detailed scope outside public metadata when required. |
| Crossmark + Crossref update relations | Publisher-maintained current-status display and typed update links, with editorially significant updates normally registered separately and linked to the unchanged original. | It is publisher-centric and does not classify every reproducibility failure as a formal correction, retraction, or withdrawal. | Map only semantically equivalent publisher updates; record failed-rerun/challenge events independently until an authorized editorial disposition exists. |
| NISO JAV (RP-8-2008) + JATS 1.4 | Named article versions (including Version of Record and Corrected Version of Record); JATS serializes free-form or controlled version values and typed correction/retraction links. | JATS documents limited consensus on version terminology; neither mechanism supplies claim/evidence review semantics. The JAV revision is still in progress. | Retain native version labels and directed links; bind every MCRP event to an immutable release, and do not treat a draft JAV revision as normative. |
| NISO CREC (RP-45-2024) | Recommended metadata creation, transfer, and display for retractions, removals, and expressions of concern affecting original works and notices. | It addresses communication after an authorized editorial status decision, not the full pre-decision challenge or reproducibility-review process. | Use for equivalent terminal/editorial statuses; preserve pre-decision failures, affected claims, evidence, and appeal state as MCRP events. |
| DataCite Metadata Schema 4.7 | Typed PID relations including `IsReviewedBy`/`Reviews`, version relations, and `Obsoletes`/`IsObsoletedBy`. | Typed links do not carry report payload, review policy, disposition reasoning, claim coverage, or trust context. | Reuse relations for discovery and identity; attach the richer signed event by reference and flag the projection as lossy. |

## Primary-source locator ledger

| ID | Source | Stable identifier | Feature-level locator used |
|---|---|---|---|
| S01 | Smith et al., *JOSS: design and first-year review* (2018) | DOI `10.7717/peerj-cs.147` | design principles and review process sections |
| S02 | Rougier et al., *Sustainable computational science: the ReScience initiative* (2017) | DOI `10.7717/peerj-cs.142` | initiative, replication, and review descriptions |
| S03 | Nüst and Eglen, *CODECHECK* (2021) | DOI `10.12688/f1000research.51738.2` | abstract; workflow, certificate, and limitation sections |
| S04 | ACM, *Artifact Review and Badging v1.1* | <https://www.acm.org/publications/policies/artifact-review-and-badging-current> | official badge definitions; accessed 2026-08-25 |
| S05 | Kluyver et al., *Jupyter Notebooks—a publishing format* (2016) | DOI `10.3233/978-1-61499-649-1-87` | pp. 87–89, especially notebook, Binder, environment, data-size, and publishing discussion |
| S06 | Binder, *Ensure reproducibility for your Binder repository* | <https://mybinder.readthedocs.io/en/latest/tutorials/reproducibility.html> | dependency pinning and Dockerfile caveat; accessed 2026-08-25 |
| S07 | Beaulieu-Jones and Greene, *Continuous analysis* (2017) | DOI `10.1038/nbt.3780` | methods/workflow and discussion; supplementary source-code record |
| S08 | Brinckman et al., *Capturing the Whole Tale* (2019) | DOI `10.1016/j.future.2017.12.029` | abstract; architecture; related work pp. 863–865; summary pp. 865–866 |
| S09 | Afgan et al., *Galaxy … 2018 update* (2018) | DOI `10.1093/nar/gky379` | abstract; scalability, dependency resolution, containers, histories/workflows, and community infrastructure |
| S10 | Chirigati et al., *ReproZip* (2016) | DOI `10.1145/2882903.2899401` | abstract and §§1–2, especially captured dependencies and cross-platform unpacking |
| S11 | W3C, *PROV-O* (2013) | <https://www.w3.org/TR/prov-o/> | normative entity/activity/agent and relation definitions |
| S12 | Khan et al., *CWLProv* (2019) | DOI `10.1093/gigascience/giz095` | workflow provenance model and implementation mapping |
| S13 | *RO-Crate Metadata Specification 1.2* | DOI `10.5281/zenodo.13751027` | data entities, contextual entities, licensing, software, equipment, and provenance |
| S14 | Leo et al., *Recording provenance of workflow runs with RO-Crate* (2024) | DOI `10.1371/journal.pone.0309210` | process-, workflow-, and provenance-run profile scopes |
| S15 | Di Cosmo, *Archiving and Referencing Source Code with Software Heritage* (2020) | DOI `10.1007/978-3-030-52200-1_36` | §§1–4: archival/reference distinction and intrinsic granular identifiers |
| S16 | Zenodo, *Manage versions* | <https://help.zenodo.org/docs/deposit/manage-versions/> | version DOI versus concept DOI; accessed 2026-08-25 |
| S17 | ANSI/NISO, *Standard Terminology for Peer Review* (2023) | DOI `10.3789/ansi.niso.z39.106-2023` | official scope and terminology purpose |
| S18 | COAR, *COAR Notify Protocol 1.0.1* | <https://coar-notify.net/specification/1.0.1/> | transport model, required notification fields, and review workflow patterns; accessed 2026-08-26 |
| S19 | Hochstenbach et al., *Event Notifications in Value-Adding Networks* (2022) | DOI `10.1007/978-3-031-16802-4_11` | notification model and interoperability architecture |
| S20 | DocMaps Technical Committee, *Framework Overview*, release 7 (2021) | <https://docmaps.knowledgefutures.org/pub/sgkf1pqa/release/7> | immutable process assertions, provider/consumer roles, explicit non-goals; accessed 2026-08-26 |
| S21 | Crossref, *Peer Review Metadata* | <https://www.crossref.org/documentation/schema-library/markup-guide-record-types/peer-reviews/> | object types, stage/round/role fields, recommendation, and `isReviewOf`; accessed 2026-08-26 |
| S22 | Crossref, *Crossmark* and *Registering Updates* | <https://www.crossref.org/documentation/crossmark/>; <https://www.crossref.org/documentation/register-maintain-records/maintaining-your-metadata/registering-updates/> | current-status service, update types, immutable original, separate linked notice; accessed 2026-08-26 |
| S23 | ANSI/NISO, *Journal Article Versions* (2008) | DOI `10.3789/niso-rp-8-2008` | version labels and corrected/enhanced Version of Record definitions |
| S24 | ANSI/NISO, *Communication of Retractions, Removals, and Expressions of Concern* (2024) | DOI `10.3789/niso-rp-45-2024` | metadata transfer/display scope for original works and editorial notices |
| S25 | NCBI/NISO, *JATS Journal Publishing Tag Set 1.4* (2024) | <https://jats.nlm.nih.gov/publishing/1.4/> | `article-version` plus correction/retraction `related-article-type` values; accessed 2026-08-26 |
| S26 | DataCite Metadata Working Group, *Metadata Schema 4.7* (2026) | DOI `10.14454/qdd3-ps68` | relation-type registry for review, version, and obsolescence links |

## Bounded backward/forward linkage review

This is one-hop linkage review, not a citation-network census. “Backward” means a
normative dependency or cited precursor named by a seed; “forward” means a later
official mapping, implementation note, or current service document linked from or
explicitly implementing the seed. The purpose is to catch adjacent components and
scope changes, not to estimate impact.

| Seed | Backward link checked | Forward/current link checked | Decision |
|---|---|---|---|
| COAR Notify | W3C Linked Data Notifications and ActivityStreams 2.0; Event Notifications paper/specification. | COAR workflow catalogue and current protocol 1.0.1. | Include Event Notifications as architectural lineage; treat W3C standards as transport substrate, not separate scientific-review semantics. |
| DocMaps release 7 | Publishing Status Ontology, Publishing Workflow Ontology, FaBiO, and community terminology precedents named by the framework. | Official JATS4R comparison and 2024 DocMaps authenticity/implementation note. | Include DocMaps at process-assertion scope; record its transport/current-state non-goals and portable-authenticity gap rather than inferring attestation. |
| Crossref peer-review/Crossmark | NISO terminology, JATS, DOI relations, and publisher update practice named in official documentation. | Current peer-review markup, update registration, versioning, and relationship guidance. | Include DOI review-object registration and publisher-status roles; do not map reproduction failure to a correction without editorial authority. |
| NISO JAV | Earlier publisher/version taxonomies summarized in the recommendation. | JATS 1.4 `article-version`, Crossref versioning guidance, and the official in-progress JAV revision page. | Include RP-8-2008 as current published recommendation; exclude the unfinished revision from normative claims. |
| Whole Tale / Galaxy / ReproZip | Related-work sections identify notebooks, containers, workflow systems, and environment capture as distinct precursors. | Later profiles and service documentation were sampled for packaging, scaling, and preservation boundaries. | Keep the v0.1 component-level rows; no source located in this bounded chain collapses execution infrastructure into claim-level scientific approval. |
| PROV-O / RO-Crate / Workflow Run RO-Crate | PROV entity/activity/agent model and workflow provenance profiles. | Workflow-run profiles and current RO-Crate 1.2 specification. | Reuse provenance transport; review disposition and reliance remain explicit profile extensions. |

## Inclusion and exclusion decisions

| Candidate | Decision | Reason |
|---|---|---|
| NISO Z39.106, COAR Notify, Event Notifications, DocMaps, Crossref peer-review metadata | Include | Together cover terminology, exchange, process assertions, and registered review objects; each has an authoritative or primary locator and a distinct scope. |
| Crossmark, NISO JAV, NISO CREC, JATS 1.4, DataCite 4.7 | Include | Cover status, version, correction/retraction communication, serialization, and typed PID relations without supplying MCRP's full scientific-review meaning. |
| W3C Linked Data Notifications and ActivityStreams 2.0 | Exclude as standalone rows | They are normative COAR transport dependencies, already represented through the COAR row; neither defines scholarly scientific dispositions. |
| PROV-O, RO-Crate, Workflow Run RO-Crate | Keep in prior row; do not duplicate | They represent provenance and research objects, not peer-review-specific state, and were already audited in v0.1. |
| JATS4R recommendations | Exclude from core matrix | Useful implementation guidance and a DocMaps mapping check, but not an independent review policy or correction authority. |
| Draft NISO JAV revision | Exclude from normative mapping | The official project page reports revision work in progress; only published RP-8-2008 is treated as normative here. |
| ORCID peer-review recognition | Exclude from this slice | Reviewer credit/identity is adjacent but does not define the review-event payload, correction state, or scientific disposition under study. |
| Generic notification, blockchain, or reputation platforms without a scholarly-review primary source | Exclude | Outside the predeclared feature-level scope; inclusion would broaden the search without resolving the targeted interoperability question. |

## Consequence for the contribution claim

The checked literature preempts broad novelty claims about executable papers,
environment reconstruction, continuous reruns, workflow histories, dependency
capture, workflow-run provenance, research-object packaging, and immutable source
identity. Paper 01 may presently claim only a proposed consolidation and profile:
claim-scoped evidence and review dispositions; the ten-axis resource declaration;
six non-equivalent assessment modes; transitive scientific trust boundaries;
human sign-off; and append-only freshness, failure, and correction events. Even that
bounded contribution remains subject to the incomplete closest-work audit and the
existing blocked claim dispositions. The review-event audit specifically supports
an interoperability claim: existing standards cover complementary parts of the
lifecycle, while projection of the full MCRP event is sometimes lossy. It does not
support “first,” effectiveness, or completeness claims.

## Gate status and next unmet evidence

The targeted G1 crosswalk is complete at v0.2: the predeclared component families,
review-event and correction standards, bounded one-hop linkage review, and explicit
inclusion/exclusion decisions are recorded. This is not an exhaustive novelty
review, so the broad novelty claim remains blocked and a wider independent search
remains a release gate. The next first unmet Paper 01 evidence gate is an immutable,
public R0 worked-case packet with a recorded run, negative test, ten-axis resource
measurement, claim-scoped disposition, and bounded sign-off. The sanitized
HPC/restricted-data case follows rather than being inferred from the R0 result.
