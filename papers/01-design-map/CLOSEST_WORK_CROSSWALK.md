# Paper 01 closest-work and standards crosswalk — v0.1

Audit date: 2026-08-25  
Scope: one bounded scholarship-gate advance covering computational-publication,
continuous-analysis, workflow/capture, provenance, and archival components omitted
from the prior manuscript narrative.  
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
The search was targeted rather than systematic; database coverage, citation
chaining, review-exchange metadata, and additional platforms remain open.

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

## Consequence for the contribution claim

The checked literature preempts broad novelty claims about executable papers,
environment reconstruction, continuous reruns, workflow histories, dependency
capture, workflow-run provenance, research-object packaging, and immutable source
identity. Paper 01 may presently claim only a proposed consolidation and profile:
claim-scoped evidence and review dispositions; the ten-axis resource declaration;
six non-equivalent assessment modes; transitive scientific trust boundaries;
human sign-off; and append-only freshness, failure, and correction events. Even that
bounded contribution remains subject to the incomplete closest-work audit and the
existing blocked claim dispositions.

## Next unmet part of G1

Expand the dated audit to review-event exchange and correction/supersession
standards (including COAR Notify, DocMaps, Crossref/NISO relations where relevant),
then perform backward/forward citation chaining for end-to-end systems and record
explicit inclusion/exclusion decisions. Only after that work may G1 be considered
complete.
