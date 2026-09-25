# MCRP as a bridge between evidence, decisions, and repair

Research positioning draft, 2026-09-25. The comparison below was checked against
primary specifications and community documentation; retrieval scope appears in
[the source ledger](positioning-sources.md). This is a proposed integration design,
not a standards-conformance report, adoption announcement, or priority claim.

**Question:** When does an additional protocol help people use existing research
artifacts without losing the boundaries of the checks and decisions behind them?

**Answer proposed for testing:** A small, portable reliance profile may help when
one artifact supports several uses with different authority, evidence, freshness,
and repair requirements. Where an existing workflow already conveys those facts
adequately, the right result is a faithful adapter—or no additional layer.

## The strongest positive proposition

An astronomer can correctly reproduce a catalog calculation without checking its
calibration. A biologist can reproduce a contrast that does not identify a causal
effect. An economist can verify a trial calculation that does not transfer to a
new population. A legal scholar can verify citations without acquiring authority
to decide an institution's conduct. Each has contributed something useful. The
problem arises when the contribution crosses an organizational boundary and its
limits disappear.

MCRP proposes to carry those limits with the object: this exact claim, these
performed checks, this intended use, this responsible decision maker, and these
conditions for reconsideration. It also asks who has capacity to perform the
promised follow-up. **Offer → check → rely → amend** is the human entry into that
profile; it is not a claim that science follows four sequential states.

The seed is most compelling as a way to connect existing records. A successful
deployment could preserve a laboratory's internal system, a collaboration's
editorial process, and an individual's preferred writing tools. The external
record would make a particular use inspectable without requiring agreement on a
universal score or one institutional theory of evidence.

## What already exists—and should be reused

| Existing work | Directly documented capability | Proposed MCRP role, if useful |
|---|---|---|
| [COAR Notify 1.0.1](https://coar-notify.net/specification/1.0.1/) | Standardized scholarly notifications, including requests, acknowledgments, announcements, and offer withdrawal | Refer to scoped receipt resources through existing notification patterns; avoid inventing another transport |
| [W3C PROV-O](https://www.w3.org/TR/prov-o/) | Entities, activities, responsible agents, qualified relations, delegation, derivation and revision | Reuse provenance terms; define application-specific reliance constraints rather than claim provenance is missing |
| [RO-Crate 1.3 introduction](https://www.researchobject.org/ro-crate/specification/1.3/introduction.html) | JSON-LD research packages describing data, contextual entities, production and reuse | Carry evidence and receipt files in a familiar research package |
| [RO-Crate provenance](https://www.researchobject.org/ro-crate/specification/1.3/provenance.html) | Creation/update actions, responsible humans, workflow state changes and retained old/new files | Preserve existing history; add a purpose-specific currentness view only where needed |
| [PCI documentation](https://peercommunityin.org/faq/) | Review, editorial decisions, public recommendations and archived process records | Import the actual institution's decision and limits rather than mint a competing approval |
| [PCI Registered Reports account](https://peercommunityin.org/?p=6218) | Pre-study and post-study review, versioned plans and visible amendments | Link a downstream use to the relevant accepted plan or result version; preserve the original conditions |
| [CRediT](https://credit.niso.org/) and [ORCID](https://info.orcid.org/what-is-orcid/) | Structured contribution roles; persistent researcher identifiers and linked records | Keep attribution and identification distinct from appointment, independence, or authority |

This overlap changes the research claim. “We separate review from publication,”
“we preserve versions,” and “we disclose who did the work” are not sufficient
novelty claims. RO-Crate even describes authorized workflow changes, and PCI RR
already documents a condition-bearing review process. The proposed increment is a
particular **cross-system use profile and executable failure suite**, not ownership
of those ideas. A complete prior-art survey may identify still closer profiles.

An ORCID iD should be an identity reference, not a credential inferred from having
an account; ORCID explicitly permits broad registration and records the source of
connections. A CRediT contribution describes work, not appointment to a review
panel. These are MCRP design inferences about correct use of those systems, not
criticisms that either system failed its stated purpose. [ORCID Trust](https://info.orcid.org/orcid-trust/),
[CRediT role taxonomy](https://credit.niso.org/).

## Semantic crosswalk: preserve meaning before translating names

The following mappings are design proposals. An adapter must keep the originating
institution's identifiers, scope, chronology, and authority; it must not infer
consent or a scientific judgment from a successful import.

Preserve the original access and disclosure conditions too. A record someone may
read is not necessarily theirs to republish. PCI's FAQ, for example, distinguishes
published recommended-review records from rejected reports that are not public.
Use synthetic or permission-cleared material in an open adapter test. If a
receiving public format cannot preserve a restriction, report that incompatibility
or refuse the export rather than copying private content into public metadata.
[PCI review visibility](https://peercommunityin.org/faq/).

| MCRP action | Existing representation to reuse | Additional profile information to preserve |
|---|---|---|
| **Offer** | A versioned evidence package; a PROV entity for the offer record and activity for preparing it; where applicable COAR's `Offer` + `ReviewAction` request pattern | Exact claim and evidence identity, requested check scope, exclusions, resource envelope; sending system is not automatically the author |
| **Check** | PROV activity uses the evidence and generates a report; reviewer association can carry role; COAR review announcement points to that report | What was actually checked, outcome, uncertainty, unavailable evidence, common dependencies and control disclosures; execution success does not imply scientific coverage |
| **Rely** | A distinct decision artifact with its provenance; existing editorial recommendation preserved; COAR endorsement announcement only if the artifact genuinely is that kind of endorsement | Named use, scope, decision authority kind, conditions, time boundary, and correction endpoint; a review receipt alone supplies none of these by implication |
| **Amend** | Revision relationship and new artifact; RO-Crate old/new file history; an appropriate notification of the relevant new resource | Affected uses, material-change reason, unresolved work and responsibility; an old historical check may remain accurate while a present use becomes pending |

For the offer mapping, COAR's [Request Review](https://coar-notify.net/specification/1.0.1/request-review/)
already distinguishes the resource landing page from the content item and uses
`Offer` with `ReviewAction`. For the check mapping, [Announce Review](https://coar-notify.net/specification/1.0.1/announce-review/)
places the review in `object` and the reviewed resource in `context`. An adapter
must not reverse those identities or treat the notification as the report itself.

[Announce Endorsement](https://coar-notify.net/specification/1.0.1/announce-endorsement/)
likewise announces an endorsement resource. It is a candidate carrier for an
appropriate decision, not a universal encoding of every local reliance. A legal
operational decision is not automatically a scholarly endorsement. [Undo Offer](https://coar-notify.net/specification/1.0.1/undo-offer/)
withdraws a previous offer; it must not be used as if it retracts a published result
or resolves every downstream reliance. Where no existing pattern fits, keep the
typed amendment resource and mark the transport mapping unsupported.

PROV terms can express rich responsibility and revision relationships; they are
not an instruction to erase old evidence when current use changes. In particular,
do not equate a disputed scientific use with destruction of the underlying PROV
entity. Nor does a delegated software activity prove independent governance. These
are application semantics the adapter must preserve, using PROV's extension points
where needed. [PROV-O qualified and expanded terms](https://www.w3.org/TR/prov-o/).

An RO-Crate profile is a plausible packaging route: the specification explicitly
supports domain-specific conventions and extension vocabularies. A future MCRP
profile should declare exactly which fields it requires, with examples and
validation rules. That does not make the current plain JSON fixtures conforming
RO-Crates; no such adapter or independent round trip has been demonstrated.
[RO-Crate profiles](https://www.researchobject.org/ro-crate/specification/1.3/profiles.html).

## What would make the integration worth its cost?

The question is not whether these facts *can* be represented in an existing
extensible vocabulary. Usually they can. The question is whether a shared minimal
profile preserves consequential distinctions when information moves between
people and systems—and whether doing so costs less than the mistakes it avoids.

Let a local decision record have semantic projection

$$\Pi(r)=(\text{target},\text{checks},\text{scope},\text{authority},
\text{purpose},\text{conditions},\text{validity},\text{repair}).$$

For an encoder $E$ and decoder $D$, the desired round-trip property is
$\Pi(D(E(r)))=\Pi(r)$ on supported cases. This is a proposed test oracle, not a
proved property of the current package. Unsupported fields must produce explicit
loss information or rejection; they must not disappear into a generic positive
badge. A receiving system may lack the original institution's authority even
when the record is translated perfectly.

A concrete integration test would send two uses of the same calibrated result:
one permits numerical reconstruction, the other requires independent calibration.
Then change only the calibration artifact. Measure which use becomes pending,
which historical check survives, and which specialist work is reserved. Run the
same test with a plain structured attachment. The new profile earns adoption only
if it preserves more relevant meaning at acceptable total labor.

Capacity is part of the proposed decision contract, not a solved standards gap.
For each person and skill, review, supervision, amendment, and appeal commitments
must draw on the same available resources. Existing systems can represent tasks
and costs; MCRP's research opportunity is to test whether binding those commitments
to particular uses prevents silent oversubscription. The dossier's elementary
models expose overload and shared-error cases, but supply no field evidence that
this profile improves them.

## Three cases where existing methods are enough

1. **A computational artifact needs packaging and rerun provenance.** If the user
   only needs inputs, software versions, outputs, and responsible contributors,
   an existing research package plus execution record can answer the question.
   Adding a reliance ceremony would impose labor without a new decision boundary.
   RO-Crate already describes software and file-production history. [Provenance
   guidance](https://www.researchobject.org/ro-crate/specification/1.3/provenance.html).
2. **A reader wants the review history and accepted plan of a registered report.**
   If the existing process already supplies the relevant version, conditions,
   reviews and deviations, point to those records. A duplicate MCRP acceptance
   would create a reconciliation problem. A wrapper becomes useful only for a
   genuinely different downstream use. [PCI RR workflow account](https://peercommunityin.org/?p=6218).
3. **A journal and repository only need to announce that a review exists.** Use
   the existing COAR announcement and link to the actual review. No extra trust
   score or MCRP state machine is required. The narrower transport problem is
   already specified. [Announce Review](https://coar-notify.net/specification/1.0.1/announce-review/).

These are acceptance criteria for the research agenda. A protocol seed that can
recommend its own omission is easier to integrate than one that demands every
existing workflow be renamed.

## Domain entry: one useful bridge per audience

| Audience | Paper focus worth reading first | Human entry and implementer entry | First adoption claim to test |
|---|---|---|---|
| Physics/astro | [Shared calibration case](../domains/physics-astro.md), then [repair mathematics](../manuscripts/math-foundations.md) and [coupled allocation](../manuscripts/coupled-agents.md) | Human: annotate one reconstruction check with its calibration exclusion. Agent: retain the existing release bundle and expose the exact calibration dependency and two differently scoped uses. | A calibration amendment reaches the uses that actually depend on it without invalidating a still-correct old computation. |
| Biology | [Batch and identification case](../domains/biology.md), then the scope/correction analysis | Human: distinguish an arithmetic check from the declared model and a causal claim. Agent: package the batch map and exact design, retain the unknown outcome, and replay the interaction counterexample. | Participants distinguish supported and unsupported interpretations better than with a plain checklist given the same information and comparable declared support; report actual total labor and appropriate retained uses separately. |
| Economics/social science | [Estimands and selection case](../domains/economics-social-science.md), then attention allocation and games | Human: attach a population and intended use to one estimate. Agent: keep trial and target estimands separate and preserve invitation/completion/reliance denominators. | Transport assumptions and final-selection concentration remain visible after export and reuse. |
| Law | [Authority and deadline case](../domains/law.md), then legal operations | Human: distinguish accurate citations, competing interpretations and the power to decide. Agent: preserve institution and jurisdiction scope; refuse an unsupported legal authority type rather than relabel it scientific. | Translation never upgrades scholarly agreement into legal power or hides an unresolved deadline behind a positive badge. |

These are proposed invitations to collaborate, not assertions that those groups
have adopted MCRP. No venue eligibility or available review capacity follows from
the comparison. A community can retain its existing authority and attach one
experimental receipt to a synthetic case before considering real data or decisions.

## A staged adoption experiment

**First, attach rather than migrate.** Start with one shareable or synthetic artifact and a
four-sentence human card. Link the original record; do not replace its identifiers,
decision letter, or correction page. Permit a contributor to add only a scoped
check. This stage needs no shared reputation economy.

**Second, test a read-only adapter.** Select one packaging/provenance combination
and document semantic loss field by field. Include unknown scope, incompatible
authority, withdrawn evidence, conflicting checks, and different institutional
uses of one target. Pass/fail concerns preservation of meaning, not whether the
JSON parses. Keep the original record available to its permitted audience
alongside any projection; do not broaden its readership merely to make an adapter
demonstration public.

**Third, try a two-system synthetic exchange.** Have separately developed adapters
exchange an offer, check, decision and amendment. Duplicate or delayed
notifications must not mint duplicate authority. A transport acknowledgment must
not be displayed as acceptance of the scientific claim. No independent exchange
has been completed in this release packet.

**Fourth, ask humans whether the extra structure helped.** Compare the bridge with
a plain structured paragraph and the community's current workflow. Count author,
reviewer, facilitator, operator and correction labor; record refusals as well as
completed work. If the simpler method preserves the same distinctions more cheaply,
retain its vocabulary and drop unnecessary machinery.

## Contribution and claim ledger

| Claim | Status | Evidence or next test |
|---|---|---|
| Existing systems already supply notifications, provenance, versioned review and contribution records | P | Linked primary documentation; bounded feature inspection in source ledger |
| A particular use should retain scope, authority, conditions and repair responsibility across systems | D | Proposed MCRP profile, not a universal institutional rule |
| The semantic projection is a useful round-trip oracle | D/H | Define fixtures; obtain an independent adapter; test loss and ambiguity |
| Toy models expose failures hidden by an undifferentiated positive badge | I/T within the models | Domain fixtures and preserved counterexamples; no human efficacy inference |
| The bridge improves real scientific or legal practice | H | Unrun comparative studies and community-specific governance work |

The public research invitation can therefore be concrete: **bring a synthetic
record or one you are entitled to share; help us preserve one consequential
distinction when it travels.**
That is a smaller demand than joining a new review institution, and a sharper
experiment than asking whether a new universal trust protocol sounds attractive.
