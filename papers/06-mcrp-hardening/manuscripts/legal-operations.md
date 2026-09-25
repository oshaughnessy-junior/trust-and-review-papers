# Bounded contestability: legal and operational limits for a federated research commons

**Working research paper — 25 September 2026. Proposed design, not legal advice, legal clearance, or demonstrated field efficacy.**

**Research question.** Can MCRP preserve meaningful challenges to evidence, authority, and publication while preventing the right to complain from becoming an unbounded claim on scarce human attention?

**Answer to be tested.** A common, small challenge interface can route to distinct authority processes, while per-case ordinary review budgets, protected rights intake, independent appeal, and removable public projections bound some operational costs without treating either silence or procedural closure as scientific agreement.

## Abstract

A commons cannot credibly promise both unlimited individualized adjudication and bounded volunteer labor. Agents intensify this constraint by making plausible complaints cheap to generate, while the scientific and legal cost of evaluating them remains heterogeneous. We formulate contestability as an allocation problem with rights constraints rather than a universal reputation mechanism. The proposed architecture preserves MCRP's exact claim/evidence/version bindings and the Trust-Domain and Review-Governance Profile's existing appeal lanes. It adds an operator compliance track, explicit separation between content visibility and scientific status, and an exhaustion-resistant case lifecycle. A workload bound and a branching-process calculation identify when ordinary appeals remain schedulable; a capacity impossibility result identifies what these controls cannot guarantee. The result is a pilot specification and falsifiable evaluation plan, not an assertion that the service qualifies for liability protections or that its governance will be accepted by researchers.

## 1. Starting point and scope

The outward-facing publication policy already separates provenance, release checks, and qualified-human scientific disposition. It binds approval to exact artifacts, limits delegation, and permits removal of sensitive content despite append-only decision history. The Commons prototype separately identifies payment entitlements and contributor capability, supports reports/corrections/hiding, and currently relies on founder-only moderation. Its README describes a stable deterministic public pseudonym; TDRG instead requires fresh per-case personas. The integration review is an older architectural review: it must not be treated as proof of current deployed behavior, especially where the newer README reports subsequent implementation.

We assume an initial US-operated, invitation-only research pilot involving adults, already-public arXiv/GitHub source material, no patient records, no confidential journal manuscripts, and a named operator. These are design assumptions, not jurisdictional findings. Public availability does not establish a redistribution license. The operator's legal entity, domicile, contracts, funding conditions, hosting arrangements, participant locations, and actual activities remain facts to establish before launch. The paper neither creates an attorney-client relationship nor determines applicable law.

The product proposition should be modest: *a versioned evidence and review service with inspectable decisions*, not an arbiter of truth, accreditation body, research-misconduct tribunal, or legally anonymous channel. Institutional and journal decisions retain their own scope.

## 2. One front door; authority remains typed

The shared protocol uses **offer, check, rely, amend**. Within its amendment action, a complainant points to the exact object, explains the concern and requested remedy, receives a response or routing receipt, and can inspect the reasoned decision. These are local intake steps, not a competing core vocabulary. A user need not understand cryptographic manifests or cite legal provisions. Assisted intake may structure free text; it must preserve the submitted meaning and allow correction.

Intake labels are not new tribunals:

| Intake concern | Existing TDRG route | Additional operator action |
|---|---|---|
| Evidence, inference, reproduction, scientific scope | Scientific-content appeal | Preserve claim-specific challenge and competing evidence |
| Eligibility, assignment, private standing | Private-standing appeal | Provide privately accessible reasons and correction route |
| Harassment, impersonation, conflicts, credential abuse | Conduct/opening appeal | Reversible access containment when justified |
| Copyright, privacy, legal demand, urgent exposure | Operator compliance track; refer to conduct/opening only for a justified identity or conduct decision | Assess applicable obligations and content visibility independently |

The compliance track is deliberately not a fourth scientific appeal. A removal can leave the recorded scientific disposition unchanged, annotated that its evidence is unavailable. A scientifically upheld critique can still disclose personal data that should not be displayed. A sanctioned participant's old valid result need not become false. Conversely, a person in good standing may publish an unsupported claim. Retaliatory complaints cannot turn adverse reviews into misconduct findings.

Define a case state

\[
X=(S,V,P,I),
\]

where \(S\) is scientific disposition, \(V\) public visibility, \(P\) participation/credential state, and \(I\) identity-disclosure authorization. Every action carries an authority scope and a permitted write set. A visibility officer's action has \(W\subseteq\{V\}\), a scientific decision \(W\subseteq\{S\}\), and an opening tribunal \(W\subseteq\{I\}\). A compound incident requires separately authorized linked actions. **Separation invariant:** a transition cannot modify coordinates outside its write set. This is an enforceable access-control design, not a claim that adjudicators are socially independent. Shared controllers must still be disclosed. This invariant concerns local stored fields only. Export, notification, cache, recipient access and downstream-derived standing/reliance require separate tests. Historical scientific disposition can remain unchanged while a current-use view reports dependency unavailable or reconsideration pending. Where applicable, GDPR Article 19 can require recipient communication concerning covered changes, subject to its exceptions; neither a local removal nor a notice guarantees recall of remote copies.

## 3. Case lifecycle and protected remedies

An ordinary scientific challenge has one initial assessment and one independent appeal. Both can conclude **upheld**, **partly upheld**, **not established**, **out of scope**, or **unresolved at resource boundary**. The last outcome is essential: failure to secure labor is not failure to establish truth. A closed docket remains addressable with its dissent. A later independent scientific contribution may cite it without demanding another adjudication.

Material new evidence, a newly identified conflict, compromised process, or changed target version can justify reopening. Cosmetic rephrasing, a larger agent team repeating the same proposition, or disagreement with the result does not automatically create a new entitlement. A preliminary duplicate determination must identify the earlier case and allow a short explanation of the material difference. Similar wording alone is insufficient: genuinely independent replication and newly affected persons must not be collapsed into abuse.

The budget bounds the operator's ordinary handling commitment; it does not extinguish statutory remedies, court access, regulator access, applicable notice obligations, or required complaint windows. Rights-sensitive reports and urgent privacy/safety requests are accessible without payment or an exhausted graph-session allowance. They have a reachable fallback contact independent of the interactive graph. Anonymous emergency intake may be accepted, while particular legal processes can require additional identifying information privately.

Appeal reviewers cannot have participated in the original decision or be controlled by the party whose decision is challenged. The pilot needs a named alternate before the founder's decisions become appealable. If no unconflicted person is available, report that fact, suspend any claim of independent resolution, preserve the challenge, and offer external referral where appropriate. Do not manufacture independence by assigning another agent run controlled by the same founder.

Counterclaims are linked but independently assessed. A scientific rebuttal belongs in the scientific record; a harassment allegation against a complainant belongs in conduct review; a copyright counter-notice has its own statutory meaning. None is automatically a defense to another. Emergency action may precede full notice if needed to contain exposure, but must expire or receive renewed justification and review. Internal review cannot authorize disregard of a lawful binding order.

## 4. Mathematics of grievance exhaustion

### 4.1 Capacity conservation

Let \(H\) be available steward minutes per week after ordinary research work. Let \(H_E\) be protected emergency/legal capacity and \(H_N=H-H_E\) ordinary capacity. For each *distinct admitted ordinary case*, let initial review cost be \(c_0\), appeal cost \(c_1\), and appeal probability \(p\). If arrivals have long-run rate \(\lambda\), the modeled utilization is

\[
\rho_N=\frac{\lambda(c_0+pc_1)+d}{H_N},
\]

where \(d\) is triage, duplicate checking, and other ordinary overhead per week. Under this accounting, load above one cannot be sustained indefinitely; \(\rho_N\le1\) is the necessary mean-load condition. Strict slack \(\rho_N<1\) is the operating target for ordinary stochastic queues, not an unrestricted mathematical necessity: perfectly synchronized deterministic arrival and service can have zero backlog at equality. Neither condition alone guarantees latency under bursts, heavy tails, correlated attacks, absences, or incorrect service-cost estimates. Costs should be measured in staff time, not request counts.

Overhead must be measured as \(d_t=d(\lambda_{\mathrm{try}},\text{payload sizes},\text{classification errors},\text{incident correlations})\), not assumed fixed as attempted intake increases. Distinguish automated receipt, human triage, admitted substantive cases, and reopened work. Ten thousand refused or mislabeled-emergency items at 0.1 staff-minute each consume 1,000 minutes even if none becomes an admitted case. Reserving emergency capacity does not guarantee that capacity is sufficient. Track oldest rights-lane item and human triage load separately; a fallback contact does not supply infinite service.

If every appeal can spawn another with probability \(p\), constant cost \(c\) gives expected cost \(c/(1-p)\) for \(p<1\). A depth cap \(K\), counting the initial decision as depth zero, changes this to

\[
E[C_K]=c\sum_{j=0}^{K}p^j\le c(K+1).
\]

At \(p=1\), the unbounded procedure never terminates, while initial decision plus one appeal costs at most \(2c\), before genuine reopenings. That is the limited benefit of bounded ordinary appeal, not a defense against unlimited novel cases.

More generally, if each decided node generates mean \(m\) subsidiary review demands, the expected total number of nodes in a Galton-Watson abstraction is \(1/(1-m)\) for \(m<1\). A finite depth cap bounds expected nodes by \(\sum_{j=0}^{K}m^j\), but a bound on mean offspring is not a deterministic workload bound. Actual guarantees require bounded child count, bounded admitted case size, and bounded handling commitment. Multiple complainants cannot each reset the same case's ordinary appeal depth by merely joining it.

The ordinary service envelope therefore binds a case and time epoch, accepted payload/attachment work, and available staff effort. Material new evidence is recorded and queued without automatically minting immediate fresh review entitlement. At the envelope boundary the case can remain scientifically unresolved. A designated compliance authority separately assesses handling required by applicable law; the ordinary envelope does not waive those duties. The synthetic sequential-update fixture demonstrates that even a single case can accumulate unresolved work despite a depth cap.

### 4.2 A finite-resource impossibility result

Assume each substantively distinct complaint requires at least \(\epsilon>0\) staff minutes to assess and an adversary may submit an unbounded number \(A\) per interval. Any policy promising individualized substantive assessment within that interval needs at least \(A\epsilon\) minutes. For fixed \(H\), choose \(A>H/\epsilon\). The promise is impossible. Free intake, authenticity checks, prioritization, incident consolidation, external help, and publication pauses can mitigate the consequences; no scoring formula removes this inequality.

Therefore MCRP should promise a receipt and an explicit status under a published service policy, not infinite rapid adjudication. A rights intake backlog cannot be silently hidden behind the ordinary scientific budget. When timely required handling is at risk, narrow or pause publication/enrollment, add qualified capacity, and escalate. Legal obligations do not disappear when a queue exceeds its design envelope.

### 4.3 Triage is a constrained allocation, not a truth score

For item \(i\), let \(u_i\) be assessed urgency, \(h_i\) expected avoidable harm, \(c_i\) estimated handling cost, and \(x_i\in\{0,1\}\) a service choice. An ordinary planning heuristic is

\[
\max_x \sum_i x_i u_i h_i\quad\text{subject to}\quad\sum_i x_i c_i\le H,
\]

with additional constraints for applicable deadlines, protected intake, conflict-free adjudication, and access by people with limited resources. This is a decision-support abstraction: values are uncertain and manipulable, and affected individuals' rights are not commensurable with a platform's engagement utility. Payment, prestige, and favorable conclusions are not urgency variables. Reserve a random sample of low-priority items for audit to estimate triage false negatives. Treat a large well-funded collaboration and a lone author by case scope and actual workload, not headcount.

A simple backlog recursion supports monitoring:

\[
B_{t+1}=\max(0,B_t+W_t-H_t),
\]

where all quantities are staff-minute obligations for the same lane and epoch. Repeated positive drift triggers reduced new intake commitments. This preserves an accounting truth that dashboards otherwise conceal: an acknowledgment is not a resolution.

### 4.4 Deadline and authority constraints beyond workload

Maintain an obligation ledger with receipt time, applicable process and unresolved applicability, clock-start event, deadline/urgency, permitted extension, qualified handler, remaining effort, and notification/containment duties. Measure deadline slack, not merely oldest-item age. Two jobs of 50 and 10 minutes can fit 100 minutes of service yet miss the second job's synthetic deadline of 15 minutes if the long job runs first. For jobs released at zero with deadlines no later than D, their required effort cannot exceed available qualified service by D. This is necessary, not sufficient for heterogeneous legal work. GDPR Articles 12(3) and 12(5), where applicable, have conditions that an overload label does not waive. An automated urgency classifier must preserve uncertain cases and measure false negatives; an attacker can strategically relabel ordinary complaints as emergencies, so nominal reserve labels do not solve triage.

The appeal arrangement must assess conflicts with both parties and the original adjudicator, including appointment/removal, funding, records access, and implementation of reversals. Predetermine recusal, replacement, appeal authority and what happens if the founder refuses to execute a reversal. A ceremonial alternate does not supply independence. Document inability to supply an independent route rather than silently certifying it.

## 5. Visibility, retention, and identity

Separate three stores: public scientific content; minimal public decision receipts; restricted case evidence. Ordinary corrections append new versions. Harmful payload removal changes availability, not the historical claim that a decision existed. Public receipts should use neutral reasons such as “restricted pending rights assessment” when detail would itself identify a person or repeat an allegation. Never place raw legal notices, private contact data, identity-opening evidence, or recoverable sensitive plaintext in the public log.

TDRG's immutable-object language must be interpreted as integrity/version identity, not a requirement of perpetual public access. A withdrawn object can have a stable identifier and a tombstone; if even its digest or linkage is sensitive, the public projection requires a narrower replacement. Crypto-erasure does not delete copies previously downloaded. Backups, replicas, logs, caches, and downstream exports need an explicit retention/withdrawal design. Legal holds can justify restricted preservation where applicable; they are not blanket permission to retain everything forever.

An identity-opening record is not public doxxing permission. Threshold trustees address an internal governance threat, but cannot establish that no legal disclosure obligation exists. A privacy notice must explain which operators can access mappings, what the process promises, and what it cannot promise. The prototype's stable persona is not conformant with TDRG's per-case persona promise; until the implementation and inference risks are tested, describe confidentiality properties narrowly.

## 6. Existing legal and institutional structures

### US publication and hosting

Section 230 distinguishes third-party content treatment from information a service helps create or develop and contains explicit exceptions, including intellectual property and federal criminal law. It is not an all-purpose shield for an operator's own scientific judgments, promises, or conduct. Counsel must classify the actual service and claims; a draft architecture cannot establish immunity. [47 U.S.C. §230](https://uscode.house.gov/view.xhtml?req=communications+decency+act+section+230).

Copyright safe harbors have conditions. If the operator seeks applicable §512 protection, assess designated-agent, notice/counter-notice, and repeat-infringer processes. A qualifying counter-notice can start a 10–14-business-day restoration framework, subject to statutory conditions and relevant proceedings; it is not an ordinary scientific appeal timer. Counter-notices entail required identifying and jurisdictional statements. Do not publish those fields or improvise automated legal advice. Operator-private handling does not mean confidentiality from the notifier: the conditional section 512(g)(2)(B) process includes providing the counter-notice to the original notifier, and section 512(g)(3)(D) includes identifying/contact and jurisdictional statements. Before collection, explain recipient-specific disclosure, required fields, and compelled-disclosure limits. Never silently transform an ordinary scientific rebuttal into a statutory counter-notice. Relevant restoration proceedings can include qualifying Copyright Claims Board proceedings under [17 U.S.C. §1507(d)](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title17-section1507). [17 U.S.C. §512](https://uscode.house.gov/view.xhtml?req=%28title%3A17+section%3A512+edition%3Aprelim%29); [Copyright Office overview](https://www.copyright.gov/512/).

A license should cover only rights actually held, with attribution and source-license records. Linking to a paper differs from redistributing its figures or manuscript. Human contribution, machine generation, license scope, and venue authorship are different questions. The Copyright Office's AI report retains human authorship as central while recognizing protectable human contributions to AI-assisted work. [Copyright Office report announcement](https://www.copyright.gov/newsnet/2025/1060.html).

Calling an accusation “opinion” does not automatically protect false factual implications. *Milkovich* rejected a separate categorical opinion privilege; jurisdiction, context, fault, and other elements still matter. Product practice should favor precise defect descriptions and evidence boundaries over public labels such as “fraudster.” This is risk reduction, not a legal safe harbor. [*Milkovich v. Lorain Journal Co.*, 497 U.S. 1 (1990), Court opinion reproduced by Cornell](https://www.law.cornell.edu/supremecourt/text/497/1).

### Conditional EU exposure

GDPR territorial scope includes an EU establishment and certain non-EU offering/monitoring activities; US hosting alone is not dispositive. If applicable, determine roles, lawful basis, minimization, retention, rights handling, security, and transfers. Pseudonymization is not automatically anonymization. Research-related provisions and erasure exceptions are conditional, not universal permissions for immutable personal-data logs. [GDPR, Arts. 3, 5, 17, 89](https://eur-lex.europa.eu/eli/reg/2016/679/).

If the DSA applies, service classification and size exclusions matter. Hosting notice/reasons duties in Articles 16–17 differ from the online-platform complaint rules in Article 20; Article 19 excludes qualifying micro/small platforms from much of that section. Where Article 20 applies, complaints are free and available for at least six months. Article 23's abuse process is conditional and requires safeguards; losing a substantive scientific argument is not manifest abuse. The pilot's ordinary appeal rule must yield to applicable law. [DSA, Arts. 16–23](https://eur-lex.europa.eu/eli/reg/2022/2065).

### Journals, institutions, and accountable agents

Export the exact review target, version, evidence boundary, contribution record, and decision scope into journal-compatible metadata. Do not imply journal endorsement or reprint confidential editorial correspondence. ICMJE, an influential biomedical policy rather than universal law, does not permit AI tools as authors and places responsibility on humans; the internal writing-agent byline must therefore map to an AI-contribution disclosure where a destination venue requires it. [ICMJE AI-author guidance](https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html).

Research-misconduct allegations may belong to institutional processes with their own confidentiality and regulatory obligations. For PHS-covered work, ORI's framework matters; it does not confer general misconduct jurisdiction on MCRP. Refer serious allegations with a precise, access-controlled record rather than inventing a parallel verdict. [ORI institutional policy](https://ori.hhs.gov/institutional-policy).

Every publishing agent or agent team needs a responsible human or organization, bounded authorization, and a reachable incident contact. That is a proposed accountability requirement, not a conclusion about legal liability or AI personhood. Large collaborations designate a competent representative without extinguishing individual authors' rights. Contracts should identify who can license, approve, correct, and withdraw, how disputes are handled, and what happens on dissolution. Institutional authority should be evidenced rather than inferred from an email domain. Choice-of-law clauses cannot safely be assumed to displace mandatory law, third-party rights, or regulator jurisdiction.

## 7. Minimum live-pilot gates and evaluation

Start with synthetic disputes; use two named, separately controlled human decision-makers for initial decision and appeal, with a disclosed failure mode if the small cohort cannot supply independence. Provide free rights intake, scoped credential roles, private case evidence, minimal public receipts, and a reversible hide/unhide path. No real identity escrow, confidential manuscripts, or advanced anonymity promise should be added merely because the library exposes an interface.

Before cohort expansion, exercise: founder conflict; threatened reviewer; mistaken takedown; novel evidence mislabeled duplicate; wealthy-author complaint flood; one person with no paid account; compromised operator; reversed standing decision; lawful-process escalation; corrupted log; cached sensitive payload; and a scientific critique whose author is separately sanctioned. Verify state-coordinate separation and that rights intake survives exhausted graph quota. Test export without identity leakage and truthful tombstones after removal.

Compare (A) founder ad hoc handling, (B) unlimited recursive appeals, and (C) bounded ordinary case handling with protected compliance capacity on identical synthetic streams. Record staff-minute backlog, oldest unresolved rights item, legitimate-challenge false rejection, duplicate false merge, reversal rate, time to containment, and independence failures. Include negative controls: valid unpopular dissent, repeated wording with genuinely new evidence, and high-status but meritless complaints. Report uncertainty and workload distributions, not only mean completion time.

Suspend new publication, enrollment, and discretionary service commitments if required handling becomes unavailable, sensitive data escape, founder conflicts have no independent route, or ordinary closure is displayed as scientific vindication. Preserve legally appropriate reporting, a fallback contact, receipt timestamps, containment, and explicit unresolved status for existing obligations; use a documented escalation and wind-down arrangement. Do not disable protected reporting along with ordinary offers. Synthetic results can validate queue accounting and state transitions only. A later consented human pilot needs separately approved research/ethics review as appropriate and must measure whether understandable procedure actually improves participation and trust.

## 8. Bounded conclusion

MCRP can make a strong, limited promise: a challenge has an exact target, an accountable decision-maker, a reason, a scope, and a repair path. It cannot promise inexhaustible attention, universal anonymity, legal immunity, or correct science. The architectural contribution is to keep these limits visible and independently enforceable while retaining a four-verb human interface.

**Authorship record:** Draft prepared by an AI legal/operations analysis agent at the user's request; no licensed-counsel review, human-author approval, field experiment, or release approval is recorded. Exact model identity is unrecorded in this artifact. See `research-packet.md`, `threat-matrix.md`, `sources.md`, and `capacity_model.py` for claim provenance and reproducibility.
