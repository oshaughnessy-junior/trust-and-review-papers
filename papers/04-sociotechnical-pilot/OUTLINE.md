# Paper 04 outline — preregistered sociotechnical pilot

## Working title

**Plural Review Governance in Practice: A Preregistered, Safety-Gated Pilot of Independent Trust Domains**

Status: preregistration-outline-ready only. No recruitment, intervention, human-subject data collection, or field-effect claim is authorized by this document.

Dependencies: a stable Paper 01 vocabulary; a tested Paper 03 protocol/tooling release; an independent ethics/IRB determination; security/privacy review; participating-domain agreements; and a public or access-controlled preregistration approved by the human investigators.

## Research question and designed answer

**Question.** When independently governed scientific communities use a shared claim/evidence record with local trust overlays, what changes in review effectiveness, capture localization, minority/newcomer treatment, participant burden, privacy, and institutional power compared with their ordinary review process?

**Designed answer.** It is not yet known; the pilot is designed to estimate plural process and harm outcomes, identify boundary conditions, and determine whether a larger confirmatory study is ethical and operationally credible—not to certify TDRG as superior.

## Non-negotiable human-subject gate

Before any interaction designed to generate generalizable knowledge—including interviews, surveys, tabletop exercises with recorded responses, shadow reviews, logs linked to participants, or collection of operational trust decisions—the investigators must obtain and record:

1. a written determination from the responsible IRB/ethics authority (approval, exemption, or not-human-subjects determination as applicable);
2. a final protocol, recruitment material, consent/waiver basis, compensation plan, and participant exit process;
3. a privacy/security assessment covering identity mapping, metadata, prose stylometry, small pools, colluding operators, and breach response;
4. an accountable operator and independent appeal/incident path that line management cannot unilaterally control;
5. a data-management and retention plan, access tiers, disclosure review, and repository/compute jurisdictions;
6. a preregistration with hypotheses, primary outcomes, analysis, sample-size/precision rationale, exclusions, missingness, stopping rules, and deviations policy;
7. evidence that each participating domain is operationally independent to the degree claimed and can withdraw or fork without losing its scientific record;
8. explicit human authorization for authorship, AI assistance, dissemination, venue, licensing, and release.

If any gate is absent, work is limited to non-participant protocol development and synthetic fixtures.

## Contribution table

| Contribution class | Proposed contribution | Evidence needed | Current posture |
|---|---|---|---|
| Prior art (P) | Situate plural review governance within peer-review, organizational power, anonymous accountability, participatory governance, and metascience evidence | Primary-source, ethics, and domain-specific literature audit | Incomplete; must be expanded before G1 |
| Synthesis/design (D) | Operationalize a field pilot that keeps effectiveness, plural legitimacy, capture, anonymity, labor, and adverse effects separate | Approved protocol and preregistration | Proposed design |
| Protocol/implementation (I) | Deploy the exact tested TDRG/tooling version and conventional comparator without changing ordinary scientific disposition during the safety stage | Immutable release, deployment manifest, dry run, operator sign-off | Not yet admissible |
| Human-subject evidence (E) | Estimate predeclared outcomes and document heterogeneous experience across independent domains | Ethics-approved recruitment, locked data, analysis, uncertainty, qualitative audit, deviations | Not yet admissible |
| Theory (T) | None required; Paper 02 results may motivate strata or mechanisms but cannot substitute for field evidence | Immutable external result | Out of scope unless supplied |

## Study purpose and scope

The initial pilot tests feasibility, safety, measurement, and mechanism plausibility. It does not test whether individual reviewers are “good people,” rank participants globally, or adjudicate scientific truth. It must not make employment, promotion, authorship, funding, publication, or disciplinary decisions. During the initial safety stage, TDRG outputs are supplemental/shadow outputs and must not determine the official scientific disposition.

## Units and independence

Potential units are scientific review cases, review assignments, reviewers, domain governance episodes, and participating domains. The preregistration must identify the estimand and unit for every outcome and account for nesting and repeated observations.

“Independent domains” requires more than two labels or institutions. For every domain, record and analyze common control through:

- governance and appointment authority;
- line management and supervision;
- funding and compensation;
- identity, credential, assignment, hosting, and opening operators;
- data/compute infrastructure;
- policy authorship and evaluator custody;
- overlapping personnel and conflicts.

At least two domains must have distinct governance roots and a credible, exercisable exit/fork path. Any shared controller is disclosed and included in the control graph. Independence is a measured property and sensitivity variable, not a binary prestige label.

## Candidate staged design

The final design remains subject to ethics and participating-domain approval.

### Stage 0 — non-participant readiness

- Freeze the intervention, comparator, data flow, opening workflow, test cases, and threat model.
- Run synthetic and sanitized fixtures, incident drills, failure injection, and operator tabletop tests that collect no research data from human participants unless separately approved.
- Demonstrate that a participant can withdraw, appeal private standing, export permissible records, and receive an explanation.
- Stop if the tested Paper 03 release or privacy/incident controls are unavailable.

### Stage 1 — consented shadow pilot

- Use real or realistic review cases only under approved access and consent/waiver terms.
- Run TDRG routing/evaluation in parallel with the domain’s ordinary review process; do not let experimental standing or personas determine the official disposition.
- Where ethically and operationally possible, randomize case, assignment, or sequence to comparator versus shadow-TDRG exposure, stratified by domain, topic, case risk, and reviewer experience.
- If randomization is infeasible, preregister a matched, interrupted-time, stepped-wedge, or other design and its identification assumptions; do not imply causal effects beyond those assumptions.
- Use an independent adjudication process for planted/sanitized defects and evidence-path findings. Editorial agreement and majority vote are not ground truth.

### Stage 2 — bounded operational pilot (separate gate)

Proceed only after Stage 1 safety review, IRB amendment/confirmation, domain consent, and preregistered escalation criteria. Give TDRG a narrowly bounded operational role with rollback and ordinary-review fallback. No reputation output may be used for employment, discipline, or public ranking.

## Research questions and open hypotheses

1. **Review process:** Does the intervention change adjudicated material-defect/evidence-gap yield per reviewer-hour, explanation quality, latency, abandonment, or downstream correction?
2. **Plural governance:** Do domains reach different but inspectable routing/standing decisions from the same event record, and can they understand why?
3. **Capture localization:** Does a governance fault or management pressure in one domain remain localized rather than altering another domain’s view?
4. **Minority survival:** Are qualified dissenting reviews preserved, discoverable, and protected from automatic standing loss until evidence resolves the dispute?
5. **Newcomer access:** How do wait time, supervision load, participation, false exclusion, and progression differ by experience and specialty sparsity?
6. **Privacy and accountability:** Under the declared adversary model, what persona linkage, reidentification, duplicate-prevention, appeal, and opening outcomes occur?
7. **Institutional power:** How do line management, funding, compensation, workload, and operator control affect voluntariness, candor, routing, challenge, and exit?
8. **Usability and legitimacy:** Can participants distinguish review feedback, private standing, scientific disposition, and conduct findings, and do they regard explanations and appeals as procedurally acceptable?
9. **Resource burden:** What human expertise, agent intelligence, governance time, compute, storage, security, and support are required for each function?
10. **Adverse effects:** Does the intervention create retaliation, chilling, exclusion, surveillance, gaming, false confidence, burden shifting, or privacy/security harm?

All are hypotheses or descriptive questions until approved data and analysis exist. Heterogeneous or conflicting outcomes are expected and must not be collapsed into one “trust” or “success” score.

## Outcomes and measurement

The final preregistration must choose a small set of co-primary outcomes and declare the rest secondary/exploratory. No composite may hide a safety failure.

| Outcome family | Candidate measures | Required disaggregation or caveat |
|---|---|---|
| Scientific-review process | Adjudicated material defects/evidence gaps found; false alarms; unresolved findings; later reversals; reviewer-hours | By domain, topic, case risk, reviewer experience; adjudication uncertainty retained |
| Timeliness and completion | Assignment latency, review latency, abandonment, revision cycles, backlog | Separate intervention learning cost from steady-state estimates |
| Routing and capture | Assignment concentration, capture radius, root/bridge dependence, policy overrides, attempted unauthorized changes | Cluster common management/funding/infrastructure; do not treat graph paths as independence |
| Minority and newcomer | Dissent survival, adverse updates before resolution, wait time, supervision load, false exclusion, exit | Small specialties and protected/vulnerable groups require disclosure control; avoid stigmatizing labels |
| Privacy/accountability | Effective anonymity set, linkage precision/recall, suspected/confirmed reidentification, duplicate attempts, appeal/opening frequency and correctness | Condition every claim on adversary and operator assumptions; suppress identifying cells |
| Understanding and legitimacy | Comprehension tasks; explanation usefulness; perceived procedural fairness; willingness to challenge/exit | Self-report is not proof of safety or correctness; analyze power/role differences |
| Labor and resources | Human and agent hours by role; compensation; governance/security/support time; compute, storage, service dependencies | Report who bears cost and who receives benefit; include unpaid/hidden labor |
| Adverse effects | Retaliation, pressure, chilling, exclusion, harassment, confidentiality breach, false allegations, misuse of standing, automation overreliance | Safety events reported individually under protected access; no averaging away severe events |

## Institutional dynamics and anti-coercion controls

- Recruitment and consent must occur outside direct supervisory chains wherever possible.
- Declining, withdrawing, challenging, or receiving an adverse private outcome must not affect employment, funding, authorship, publication, access to ordinary review, or standing outside the pilot.
- Managers cannot request persona linkage, identity opening, assignment overrides, or private histories outside the approved process.
- Compensation must not be contingent on favorable reviews, agreement, or continued participation and must be analyzed as a possible dependency.
- Investigators must disclose whether they control the protocol, tooling, domain, participant employment, publication venue, or incident process.
- Participants need a nonmanager channel for questions, withdrawal, complaints, and adverse-event reporting.
- Governance meetings and qualitative interviews must account for status, seniority, disciplinary, and employment power; apparent consensus is not treated as independent agreement.
- The paper must preserve minority interpretations and domain-specific outcomes, including a domain’s reasoned rejection of TDRG.

## Anonymity and privacy threat model

The preregistration must name adversaries separately: authors, other reviewers, domain members, line managers, investigators, platform operators, credential issuers, publishers, data analysts, trustees, outsiders, and coalitions among them. For each, specify accessible data, timing, auxiliary knowledge, attack objective, mitigations, and residual risk.

Minimum attacks and controls:

- timing and assignment correlation → batching, delays, and access separation;
- rare expertise/attribute disclosure → coarse proofs and minimum effective pool;
- prose stylometry and specialist facts → explicit residual-risk consent and controlled release;
- graph/relationship inference → private histories and disclosure-limited explanations;
- operator collusion → separation of duties, threshold opening, access logs, and independent audit;
- small cells in reports → suppression, aggregation, or access-controlled results;
- linkage across cases → fresh persona keys and absence of global nullifiers;
- legal/safety demands → predeclared process, minimum disclosure, notice where allowed, and correction rights.

The system must call a review `confidential`, not `anonymous`, when its declared anonymity threshold is not met. No participant identity or private trust history belongs in the public research dataset.

## Adverse-event and stopping framework

Pause the affected function immediately and notify the accountable safety/ethics process when any of the following occurs:

- unauthorized identity linkage, opening, or access to private history;
- credible retaliation, coercion, harassment, employment/funding threat, or publication penalty;
- material confidentiality or restricted-data breach;
- an experimental output affects official disposition outside the approved scope;
- a raw vote, graph anomaly, scientific disagreement, or allegation automatically sanctions a participant;
- managers or investigators bypass assignment, appeal, or opening controls;
- severe burden, distress, exclusion, or uncompensated labor exceeds the preregistered bound;
- an ordinary operator can defeat the declared anonymity or policy boundary;
- the incident/appeal operator is unavailable or conflicted;
- protocol/tooling drift invalidates consent, threat assumptions, or preregistration.

The safety plan must define who can pause, who is notified, protection against retaliation, investigation without unnecessary opening, remediation, participant communication, IRB reporting, restart authority, and whether the event is reportable in aggregate. Safety stopping is not a failed scientific result and must not be suppressed.

## Analysis plan requirements

Before recruitment, freeze:

- co-primary outcomes, estimands, smallest meaningful differences or precision targets, and sample-size rationale;
- assignment/randomization or identification strategy and analysis populations;
- domain/case/reviewer clustering, repeated observations, and period/learning effects;
- covariates, strata, interactions, subgroup disclosure rules, and multiplicity policy;
- missingness, withdrawal, censored appeals, late defect confirmation, and unresolved-case treatment;
- protocol-deviation categories and intent-to-treat/per-protocol roles where applicable;
- quantitative uncertainty intervals and sensitivity analyses;
- qualitative sampling, interview guide, coding/audit/reflexivity process, negative cases, and integration with quantitative evidence;
- adjudication procedure, blinding where feasible, disagreements, and uncertainty;
- disclosure review and the boundary between public, controlled, and destroyed data.

Do not infer reviewer quality from agreement with editors, authors, majority votes, rank, citations, or institutional prestige. Do not interpret a nonsignificant result as equivalence unless an equivalence/noninferiority design was preregistered.

## Proposed manuscript architecture

1. **Abstract:** state pilot status, ethics approval identifier, design, registered outcomes, bounded results, harms, and non-generalizability.
2. **Introduction:** motivate plural governance and state why protocol conformance alone cannot establish social efficacy.
3. **Prior work:** peer-review interventions, open/anonymous review, organizational power and retaliation, governance/common-pool systems, algorithmic reputation, privacy, and participatory/metascience methods.
4. **Intervention and theory of change:** exact protocol/tool versions, mechanisms, assumptions, alternative explanations, and possible harms.
5. **Ethics and positionality:** approvals, consent, compensation, investigator roles/conflicts, community governance, and participant protections.
6. **Methods:** domains, independence/control graph, cases, participants, design, comparator, outcomes, instruments, adjudication, data flow, and preregistration deviations.
7. **Results:** participant flow; implementation fidelity; every co-primary outcome; domain/subgroup heterogeneity; qualitative negative cases; adverse events; resource burden. No section exists until data lock.
8. **Discussion:** mechanism evidence, plural interpretations, institutional dynamics, limits, harms, transfer conditions, and go/no-go for a larger study.
9. **Data/code availability:** public metadata and synthetic fixtures; controlled or unavailable sensitive data with reasons, governance, access process, and retention.
10. **Authorship/AI/funding/conflicts:** human-approved record consistent with venue policy.

## Reproducibility without participant exposure

Archive the protocol, preregistration, amendments, consent/waiver basis as releasable, instruments, code, synthetic fixtures, schema versions, environment, configuration, randomness, compute, analysis logs, and disclosure decisions. Provide a synthetic or disclosure-safe reproduction path for every analysis. Where raw data cannot be shared, publish variable definitions, transformations, aggregate checks, controlled-access conditions, and a signed attestation of independent rerun where allowed. Reproducibility does not override consent, confidentiality, data-use agreements, law, or institutional obligations.

## Review and progression gates

- **G0 Argument:** outline and ledger support a bounded feasibility/safety paper, not a superiority narrative.
- **G1 Scholarship:** primary literature covers sociotechnical governance, power, privacy, peer-review interventions, and closest systems.
- **G2 Methods:** independent methods/statistics, qualitative, domain, privacy/security, and ethics reviewers challenge the preregistration.
- **G3 Artifact:** exact intervention and analysis releases, deployment manifests, synthetic reproduction package, and protected-data controls are verified.
- **G4 Independent review:** at least one reviewer outside the protocol/tooling authors and outside participating management challenges interpretation and harms.
- **G5 Human release:** investigators, domain authorities where appropriate, privacy/ethics officials, and human authors approve dissemination; participants do not receive a veto over valid aggregate findings unless promised by consent/governance, but disclosure protections remain binding.

## Go/no-go after the pilot

A larger or operational study requires evidence that the pilot can run without unacceptable privacy, retaliation, exclusion, burden, or governance harm; that outcomes are measurable without converting agreement into truth; that independent domains can exit/fork; and that the resource package is credible. Null results, domain disagreement, or a conclusion that the protocol is too costly are valid outcomes.
