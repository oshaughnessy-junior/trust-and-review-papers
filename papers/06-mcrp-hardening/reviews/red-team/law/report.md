# Adversarial review: bounded contestability and operational law

25 September 2026. Dedicated law/operations adversary. This is a same-model, same-operator adversarial analysis, not counsel, independent external validation, or an applicability determination. No expert source file was modified.

## Verdict

**Retain the paper, narrow the readiness claim, and repair six operational seams before a contested human pilot.** The elementary capacity results survive the tests. The manuscript explicitly rejects blanket immunity, absolute anonymity, infinite service, and substitution of its ordinary appeal budget for law. I found no basis for claiming those cautions are absent. The strongest defects are incomplete handoffs between the proposed legal architecture and an executable operations policy. These matter because a small interface can hide difficult decisions; it cannot eliminate them.

The shared protocol is a plausible interface hypothesis. It does not yet constitute a tested dispute service. Nothing here establishes that MCRP is subject to a particular statute or currently violates one.

## Reviewed targets and method

- `work/law/paper.md`, `sources.md`, `research-packet.md`, `threat-matrix.md`, and `capacity_model.py`.
- `work/trust-and-review-papers/papers/06-mcrp-hardening/SYNTHESIS.md` and `protocol/minimal-profile.md`.
- Ran the author's arithmetic script and the new `fixtures.py`; outputs are preserved beside this report. All assertions passed under Python 3.9.6. These are synthetic witnesses, not deployment tests.
- Checked critical operational legal propositions against current official indexed statutory text: US House §512 and §1507; EUR-Lex GDPR and DSA. Some findings concern missing operational requirements, not errors in the cited statutory summaries. No comprehensive case-law or jurisdictional survey was performed.

Severity denotes consequence **if the gap is carried into a live implementation**: High means a necessary pilot gate; Medium means a consequential specification correction. It is not an assertion of an existing production vulnerability.

## LAW-01 — High: a private counter-notice is not confidential from the complainant

**Target:** `paper.md:50,108,112,120`; `threat-matrix.md`, “Spurious copyright notice”; `minimal-profile.md:51–53`.

**Reproduction/source:** A pseudonymous critic submits a statutory counter-notice after a hostile author requests removal. The paper calls the handling private, forbids publishing identifying fields, and correctly mentions identifying statements. It does not explicitly say that the counter-notice copy is provided to the original notifier. The conditional §512(g)(2)(B) process includes forwarding the counter-notice; §512(g)(3)(D) specifies identity/contact and jurisdiction information. A service can follow all the paper's public-log restrictions while disclosing those details to the hostile notifier. This is not public posting, and it need not await a TDRG opening tribunal. [US House, 17 USC §512](https://uscode.house.gov/view.xhtml?req=%28title%3A17+section%3A512+edition%3Aprelim%29).

**Consequence:** A scientifically legitimate critic may reasonably misunderstand “private” as operator-only confidentiality. Notice-and-counter-notice becomes a targeted identity-pressure channel. Threshold identity-opening governance does not cover all legitimate disclosure pathways.

**Minimum repair:** At the counter-notice entry point, distinguish public disclosure, operator access, required recipient transmission, and compelled disclosure. Before collection, explain intended recipients and required fields in plain language. Route uncertain cases to a qualified human; do not silently submit or forward a user's ordinary scientific rebuttal as a legal counter-notice. Add a fixture where the same target has a confidential conduct case, public scientific amendment, and separately authorized statutory response. Check recipient-specific exports.

**Residual risk:** Even an accurate explanation may chill a vulnerable reviewer. A safer interface cannot promise confidentiality incompatible with the selected process. Actual eligibility and lawful alternatives require case-specific judgment.

**Claim verdict:** L10 is accurate but operationally incomplete. L15 correctly remains a hypothesis. The stated 10–14-business-day framework is not refuted. A restoration workflow also needs to handle qualifying Copyright Claims Board proceedings under §1507(d), not only court filings; “relevant proceedings” already leaves room for this. [US House, 17 USC §1507](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title17-section1507).

## LAW-02 — High: scalar backlog and oldest-item age cannot schedule distinct legal obligations

**Target:** `paper.md:60–68,86,90–104,146`; `capacity_model.py:backlog`; synthesis, “The limiting resource may be correction” and operating-envelope legal row.

**Reproduction:** `fixtures.py` gives two jobs released together: ordinary work costs 50 minutes with deadline 100; a rights task costs 10 with deadline 15. Both orders consume 60 minutes and leave scalar backlog zero. Ordinary-first completes the rights task at 60 and misses its deadline; rights-first completes it at 10. Repeating this with 100 minutes of capacity per epoch produces zero end-of-epoch backlog at 60% load while a bad scheduler repeatedly fails the short deadline. These deadlines are synthetic, not legal periods.

**Consequence:** The accounting theorem is correct, but it cannot support a timely-rights-handling claim. “Oldest rights item” is also insufficient when younger items have earlier deadlines, a different qualifying handler, or faster containment needs. Publication pausing cannot retroactively repair a missed deadline.

**Minimum repair:** Add an obligation ledger containing receipt time, applicable process and applicability status, event that starts the clock, deadline or urgency, permitted extension, assigned qualified handler, service effort remaining, and notification/containment obligations. Track deadline slack and capacity by skill. Test infeasible demand within windows, not just average utilization. For jobs released at zero with deadlines at most D, the necessary single-resource condition is `sum(required effort) <= available service by D`; it is not a sufficiency theorem for the heterogeneous legal workflow.

**Primary check:** If GDPR applies, Article 12(3) imposes a response period and conditional extension with notice; Article 12(5) addresses manifestly unfounded/excessive requests with a controller burden. Those conditions are not an automatic emergency-flood exemption. [GDPR, Article 12](https://eur-lex.europa.eu/eli/reg/2016/679).

**Residual risk:** Unknown facts, disputed applicability, variable service time and legal interpretation prevent a scheduler from determining legal compliance on its own. Preserve “needs human determination” and infeasible states.

**Claim verdict:** L02–L04 survive. No arithmetic bug found. The paper already disclaims latency guarantees; the gap is between that disclaimer and the proposed monitoring/stop policy, which needs the richer ledger before activation.

## LAW-03 — High: “stop live intake” can disable the very protected route the design preserves

**Target:** `paper.md:148` versus `paper.md:50,86`; `threat-matrix.md`, pilot gates 4 and 9; `minimal-profile.md:85–90`.

**Reproduction:** An incident operator implements the instruction “Stop live intake if required handling becomes unavailable” as disabling all incoming forms and mail processing. Ordinary offer intake and existing-content rights reporting share the front door. Existing harm and time-sensitive requests continue after publication stops, but users can no longer submit them or prove receipt. The paper elsewhere says publication/enrollment should pause; the broader stop wording conflicts with that limit.

**Consequence:** A fail-closed publishing policy can become a fail-closed complaints policy. The two functions need opposite failure behavior: stop creating commitments while preserving reachable reporting and evidence of receipt.

**Minimum repair:** Replace the ambiguous stop condition with separate controls: suspend new publication/enrollment and discretionary promises; preserve legally appropriate reporting, fallback contact, receipt timestamps and explicit unresolved status; escalate qualified capacity and containment. Define a degraded mode for the shared front door. Do not promise unlimited payload storage or immediate human assessment.

**Residual risk:** Keeping intake reachable does not ensure it can be processed. Operators need a prearranged escalation and wind-down plan for already-hosted material and existing obligations.

**Claim verdict:** L05 is a sound design invariant; this stop instruction can contradict it. This is a concrete wording and operating-policy repair, not a demand for perpetual unlimited service.

## LAW-04 — Medium: state-coordinate separation is weaker than information-flow and downstream authority separation

**Target:** `paper.md:34–42,108–112`; research-packet L01/L06/L16; `minimal-profile.md:27–36,51–53`.

**Reproduction:** The fixture changes only V from public to hidden and passes the permitted write-set test. A previously generated export still contains a synthetic reviewer contact. Separately, a downstream adopter can exclude every hidden claim from reviewer eligibility without changing local P. The local invariant holds while information remains disclosed or remote participation consequences arise. The paper recognizes caches and UI risks but does not make these separate invariants or receipt semantics.

**Consequence:** A proof about four stored coordinates can be read as a stronger guarantee of institutional independence or privacy. Visibility actions necessarily change what evidence can be checked; they can also become a practical sanction even if S is preserved. “Truth unchanged” does not mean evidentiary support remains inspectable or usable.

**Minimum repair:** State explicitly that the invariant is local authorization over stored fields. Add separate tests for exports, notifications, caches, access roles, and derivations from visibility to standing or reliance. Mark evidence unavailable and affected reliance pending where warranted, without changing historical scientific judgment. Maintain a recipient ledger where appropriate; when GDPR applies, Article 19 can require recipient communication about covered rectification/erasure/restriction, subject to its exceptions. [GDPR, Article 19](https://eur-lex.europa.eu/legal-content/EN-SV/TXT/?uri=CELEX%3A32016R0679).

**Residual risk:** Remote recipients may retain copies or infer identity; federation cannot enforce local noninterference everywhere. The design already honestly rejects perfect deletion. Do not convert recipient-notification duties into a promise of recalled copies.

**Claim verdict:** L01 is valid as scoped access control; any inference to privacy, independent judgment, or downstream consequence isolation is unsupported. L06 survives as a semantic distinction.

## LAW-05 — Medium: a named alternate is necessary but does not establish operational independence

**Target:** `paper.md:52,142`; `threat-matrix.md`, founder self-review; synthesis, “Bounded disputes need real exceptions and real capacity.”

**Reproduction:** A founder appoints an unrelated reviewer who never participated in the original case. The founder can remove the reviewer, withhold case evidence or payment, and decline to implement reversal. Formal distinct identity and no prior participation coexist with effective veto power. Alternatively, the only alternate is a close collaborator of the complainant rather than the respondent. The text's “not controlled” requirement rejects some of this in principle but lacks a decision test or enforceable arrangement.

**Consequence:** Independence becomes an unverified label. A sponsor or founder can capture outcomes through appointments, resources, records or execution instead of directly selecting a verdict.

**Minimum repair:** Define case-specific independence across both parties, original adjudicator, appointment/removal, relevant funding and institutional conflicts. Predetermine appeal authority, access to the necessary record, recusal/replacement, effect of reversal, and publication of unresolved implementation disputes. Small pilots can use a modest written arrangement with a genuinely separate person; they need not invent a court. Expose “no independent route available” rather than assigning a ceremonial alternate.

**Residual risk:** Small expert communities contain unavoidable dependencies; conflicts are not fully observable. Independence should remain a documented assessment with limitations, not a binary fact inferred from different accounts.

**Claim verdict:** L08 survives. The operational instantiation remains unproved. The expert already rejects another founder-controlled agent as an independent appeal, correctly.

## LAW-06 — Medium: protected intake needs an adversarial route-selection model

**Target:** `paper.md:50,68,86,90–96`; `threat-matrix.md`, grievance flooding and wealthy process; minimal profile's common front door.

**Reproduction:** An attacker receives little expected benefit from an ordinary queue but expects faster containment if the same allegation is marked imminent privacy harm. If labeling has near-zero cost and increases the probability/duration of removal, urgent labeling is a profitable deviation even when the attacker never wins on the merits. The fixture sends 1,300 labels at 0.1 triage minute each against 120 reserved minutes: 10 minutes remain before any substantive case is admitted. The author's larger ordinary-triage flood already anticipates part of this; this is a distinct emergency-budget and strategic-routing witness.

**Consequence:** Either false emergency labels censor good work and monopolize the reserve, or blanket suppression of repeated labels harms valid requests from vulnerable people. A genuinely sophisticated attacker can submit distinct plausible rights claims; no classifier or quota eliminates the capacity impossibility.

**Minimum repair:** Specify an evidence-sensitive provisional containment rule, maximum duration/review trigger, separated scientific status, safe report channel, and audited triage of low-priority claims. Measure false containment duration and false-negative harm as well as completion/backlog. Keep emergency classification independent of payment and prestige. Add attacker choice of label to the game-theory model; ordinary appeal caps alone cannot deter this deviation. Conditional DSA Article 23 safeguards are not permission to suspend anyone who loses scientific disputes; the paper correctly says so. [DSA, Article 23](https://eur-lex.europa.eu/legal-content/en-fr/TXT/?uri=CELEX%3A32022R2065).

**Residual risk:** Some disruption is unavoidable if genuine urgent reports remain reachable. The repair is a bounded, measurable tradeoff, not complete Sybil resistance or an automatic legal-abuse classifier.

**Claim verdict:** The exhaustion impossibility result strengthens this objection rather than solving it. Claims of bounded operational cost must be restricted to admitted work under the stated envelope, not the protected route as a whole.

## Claims that resisted attack

1. The geometric depth calculation is correct under its stated constant-cost and continuation assumptions. The expert expressly separates novel cases and reopening; charging those back to the geometric bound would be an unfair criticism.
2. The necessary mean-load condition is carefully distinguished from strict-slack operating advice and tail latency. The equality fixture correctly permits deterministic zero backlog.
3. Legal availability and scientific merit are different questions. The separate operator compliance route is better specified than a generic platform “appeal” used for everything.
4. The legal summaries generally state applicability and exceptions rather than announcing safe harbor or global compliance. DSA size/scope conditionality, GDPR research limits, and venue-policy versus law are explicitly recognized.
5. Stable public personas, exact-version identity, and privacy are not conflated in the expert report. The design expressly concedes that downloaded copies cannot be recalled and that public availability does not prove a redistribution license.
6. Organizational/legal authority is not inferred from affiliation alone. Operator entity, domicile, participant locations, contracts and license authority remain missing launch facts rather than silently assumed facts.

## Collective red-team agenda

- Ask the game theorist to model emergency-label and false-takedown strategy, including asymmetric harm from an hour of invisibility.
- Ask the economist to count legal triage, independent appeal, incident response and repair against the same qualified humans; reserve labels must not double-spend capacity.
- Ask the scientist to test whether the four verbs reveal routing, independent authority and evidence-unavailability limits at the moment of use. A compact interface can conceal failure if its defaults are optimistic.
- Ask the combined team who can execute a reversal against the founder or indispensable funder. That is an implementation and governance question, not a theorem supplied by a trust graph.

Do not claim the paper's mathematics proves institutional viability. It proves useful limited constraints and supplies falsifiers. The next credible result is a synthetic end-to-end incident and appeal run with timestamps, recipient-specific exports, explicit capacity infeasibility and a real documented authority chain.
