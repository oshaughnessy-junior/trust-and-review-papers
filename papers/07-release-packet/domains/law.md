# Law: a disputed interpretation is not settled by counting reviewers

**Research question.** Can the same small interface support legal scholarship and
operator process without turning a scientific review network into a court?

**Bounded answer.** Only if evidence checks, legal interpretations, institutional
authority, content access, and deadline obligations remain different objects.
The examples below are invented educational cases, not advice for a live dispute
or a representation that MCRP satisfies any jurisdiction's requirements.

## The situation

The invented Alder research commons hosts a scholarly memorandum arguing that a
fictional institutional policy permits a particular reuse. One reviewer finds its
citations accurate. Another accepts the citations but rejects the interpretation.
The institution's authorized officer must decide whether its own staff may rely
on the memorandum. Separately, the commons receives a rights complaint concerning
an attached diagram. That complaint may require a different decision maker,
restricted evidence, and a deadline that no scholarly vote can suspend.

The memorandum, policy and diagram are synthetic fixtures. There is no client,
legal representation, identifiable complainant, or actual contested content.
The protocol is useful here if it makes disagreements and authority legible,
not if it declares the highest-reputation interpretation “the law.”

## Why the interfaces need separate authority

An evidence check can say that a cited passage exists and is accurately described.
A substantive reviewer can offer an interpretation with reasons and limits. An
authorized institution may adopt a position for its own conduct. A court may have
authority that neither reviewer possesses. Those actions should not be represented
as interchangeable positive votes.

For a real-world analogy, the Federal Rules of Evidence govern admission or
exclusion of evidence in covered federal proceedings, subject to the rules’
applicability and exceptions; an MCRP check cannot perform
that institutional function. The rules and their applicability remain with the
legal system. [Official U.S. Courts overview, checked 2026-09-25](https://www.uscourts.gov/forms-rules/current-rules-practice-procedure/federal-rules-evidence).

Another concrete boundary is conditional U.S. copyright procedure. Section
512(g)(2) describes counter-notice forwarding and a 10–14 business-day replacement
window, subject to its conditions and the specified notice of a filed action.
Section 512(g)(3) requires identifying information in a counter-notice. Therefore
an operator-private submission is not necessarily confidential from the notifier.
Applicability and other obligations require separate assessment; this toy does
not calculate statutory deadlines or claim safe-harbor eligibility.
[U.S. Copyright Office statutory text, §512(g), checked 2026-09-25](https://www.copyright.gov/title17/92chap5.html#512).

Those examples motivate a typed design, not a universal legal workflow. Other
jurisdictions, institutional contracts, procedural orders, accessibility needs,
retention duties, and protected reporting can impose different obligations.

## A small authority model

Let $A(p,k,o)$ mean that principal $p$ has authority of kind $k$ over object $o$.
Let $C(r,s)$ mean receipt $r$ supplies a check of scope $s$. A proposed relying
action has a policy predicate

$$\operatorname{Allow}(p,k,o,s)=A(p,k,o)\land
\operatorname{Coverage}(o,s)\land\operatorname{Current}(o,s).$$

This is a declared application rule, not a theory of law. In particular,

$$\sum_r \mathbf 1\{C(r,\text{citation accuracy})\}>0
\quad\not\Rightarrow\quad A(p,\text{legal decision},o).$$

Increasing the number of correct citation checks does not logically grant a
reviewer institutional power. The missing authority premise cannot be supplied
by a reputation score. An implementation must establish actual authorization
outside this fixture; a JSON `role` string is merely a trusted assertion here.

The current toy engine models only `scientific` and `publication` reliance kinds.
It deliberately refuses `legal_operational` requests. The legal example uses the
engine only to check a citation ledger and permit publication of a *synthetic
teaching artifact*. The institution's operational decision remains a separately
illustrated record, outside the engine. This refusal is useful backward
compatibility: a partial adapter must not invent support for an authority type.

## Four actions with a preserved disagreement

| Action | Concrete record |
|---|---|
| Offer `law-offer-v1` | A scholar offers `law-memo@1`, exact synthetic policy text, argument and citation ledger. Requests `citation_accuracy`; explicitly excludes a binding legal determination. |
| Check `law-citations-v1` | An external reader verifies the fictional quotations. Another reader records a competing interpretation in a separate narrative check; neither acquires power to decide the institution's conduct. |
| Rely `law-publication-v1` | A named publication editor authorizes use of the checked synthetic citation ledger in the teaching exercise, with expiry at logical time 20. It does not adopt the memo's conclusion as law. |
| Rely, separate institutional record | The fictional officer, under a stated fictional appointment and scope, chooses a provisional institutional position with conditions, an expiry, and a route to reconsideration. This is a narrative authority example; the toy API does not implement it. |
| Amend `law-amend-v2` | A policy revision changes a premise. The prior memo's use becomes pending. A rights notice concerning the diagram is linked but enters the operator compliance track, not the scientific-disagreement tally. |

Publication of an accurate quotation ledger can coexist with unresolved substantive
disagreement. Restricting diagram access can coexist with a historically unchanged
scholarly disposition. None of those records should be overwritten with one global
green/red status.

## Deadline mathematics: aggregate capacity can lie

Use a deliberately simple, deterministic service model: one handler performs one
unit of work per logical tick; tasks are nonpreemptive; every task in the first
example is available at tick 0. These ticks are not days or statutory time.

| Job | Effort | Deadline | Purpose |
|---|---:|---:|---|
| A | 3 | 4 | Discretionary scholarly clarification |
| B | 1 | 1 | Synthetic protected-intake acknowledgment |

Total effort is 4 and total capacity over four ticks is 4. FIFO in order A→B
finishes B at tick 4 and misses its deadline. The order B→A finishes B at 1 and
A at 4, meeting both. Thus a scalar utilization test is insufficient even in this
small model. This is an example, not an optimality theorem for arbitrary releases,
multiple handlers, precedence constraints or emergencies.

An infeasibility negative control uses C with effort 2 due at tick 1 and D with
effort 2 due at tick 4. Aggregate utilization still equals 1, but C cannot finish
on time at unit service rate. Reordering does not repair absent capacity. The
appropriate result is a recorded infeasible obligation and escalation through
the authorized institution, not a fabricated “handled” status.

For multiple skills, a necessary capacity condition is

$$\sum_{j:\,\text{skill}(j)=s} w_j\le H_s,$$

along with per-person limits. It is not sufficient for deadlines, independence or
lawful access. A promised alternate needs appointment, access, resources and the
power to implement reversal. Another agent controlled by the same founder does
not provide independent institutional review.

## Failure and repair

The failure workflow sends a rights notice into a bounded scientific-appeal queue,
charges it against a reputation quota, or claims that a popular memorandum settles
the complaint. Another failure exposes counter-notice identity fields in a public
receipt while promising blanket confidentiality. A third processes easy optional
work while a protected deadline expires.

The repaired design has a shared intake front door but separate remedy tracks:
scientific content, private standing, conduct/opening, and operator compliance.
An intake classifier may suggest a track, but uncertain applicability goes to an
authorized handler and must not erase the clock-start information. Public receipts
contain minimal permitted status; restricted records hold sensitive evidence and
recipient-specific disclosure rules. Removal and retention require their own
authority; immutable hashes do not require perpetual public content.

When resources fail, pause new discretionary commitments while preserving the
appropriate existing reporting channel and timestamps. A research prototype with
no live users need not pretend to run such a service. Before admitting real
disputes, the operator must establish the actual responsibilities it is promising.

## Human onboarding: a tabletop, not client intake

**Ten-minute exercise:** Give participants the two-job table and the memo's accurate
citation check. Ask who can authorize publication, who can authorize institutional
reliance, and which order meets both synthetic deadlines.

**Answer key:** Citation accuracy establishes neither authority nor a binding
interpretation; B→A meets the first schedule, neither order solves C; a rights
notice and scholarly rebuttal may concern the same artifact but need different
remedies. A legal operational reliance type unsupported by the adapter must be
refused rather than relabeled `scientific`.

**Forty-five-minute clinic:** Assign scholar, opponent, publication editor and
operator. Keep all notices fictional. Introduce a founder conflict, a sensitive
field, a policy amendment and an unavailable alternate. Record which assertions
must remain unresolved, who sees each field, and whether the group escalates
without inventing authority. Do not solicit real legal problems or confidential
documents as onboarding material.

## Implementer task and falsifiable benchmark

Run the schedule oracle and replay the citation check through the toy engine.
Attempt `kind="legal_operational"`; the expected result is rejection. Verify that
a later policy amendment marks the relevant teaching use pending while preserving
the old record. Test rights intake separately from scientific rating: no queue
score should convert a notice into a scientific result.

A future tabletop comparison should measure mistaken authority upgrades, missed
synthetic deadlines, inappropriate disclosure, correct routing, inaccessible
appeals, total labor and unresolved cases. Include a plain case-management checklist
as the strongest practical baseline. “More receipts produced” is not success. The
proposed interface loses if it creates more overhead without improving these
outcomes. No legal process or human study has been validated here.

## Claim ledger and closest-work boundary

| Claim | Type | Support or remaining test |
|---|---|---|
| Evidence admissibility is an institutional function | P | Official U.S. Courts overview; no applicability opinion |
| §512(g) includes timing and recipient disclosure provisions | P | Official Copyright Office text; conditional summary only |
| Total work within aggregate capacity need not meet deadlines | T/I | Two exact schedule fixtures and tests |
| Typed authority must not be inferred from citation agreement | D | Explicit design predicate; no claim to grant authority |
| MCRP improves dispute operations | H | Unrun tabletop and institution-specific assessment |

Existing docket, case-management, scholarly commentary and correction practices
already separate many of these objects. MCRP's proposed contribution is a portable
record of the particular use and its limits. Its public research release should
invite criticism from those communities without advertising a live legal service.
