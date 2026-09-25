# MCRP bounded reliance profile: offer, check, rely, amend

Proposed v0.1, 2026-09-25. Human-facing profile of MCRP/TDRG; not a new universal
trust standard, adopted policy, deployed service, or replacement for legal duties.

## The one-minute protocol

1. **Offer:** Point to one exact claim and release. Say what you want checked,
   what evidence is available, and what effort you can support.
2. **Check:** Record what you actually did, what you found, what you did not
   check, and what might make your check dependent on someone else's.
3. **Rely:** A responsible person or institution states what use it accepts,
   on which evidence and conditions, with an explicit scope and expiry.
4. **Amend:** Point to new evidence or a change. Correct, narrow, dispute, or
   withdraw the affected reliance; keep the earlier record identifiable.

Every screen answers: **what is this about, who is responsible, what is supported,
and what remains unknown?** Versioning, signatures, retries, and policy expansion
belong in the software. Advanced controls appear when their risks arise; the
software must not silently supply consent, reviewer judgment, or omitted facts.

## Stable semantics beneath the small interface

- Exact version: use the claim, acceptance contract, evidence-set digest, and
  release digest already defined by MCRP. A mutable URL alone is insufficient.
- Typed evidence: support, bound, context, and contradiction remain distinct.
- Typed authority: integrity, check result, scientific disposition, publication
  authorization, and observation of delivery remain distinct records.
- Accountable boundary: one external principal may contain any internal team;
  its agents do not independently multiply allocation, authority, or anonymity.
- Explicit uncertainty: unknown, inaccessible, unchecked, and disputed are valid
  outcomes, never implicit passes.
- Bounded reliance: every decision states purpose, policy, scope, validity and
  correction path; science is not reduced to a binary platform verdict.
- Removable projection: content identity does not imply perpetual public access.
  Sensitive content can be removed while a minimal permitted notice remains.

These are seven implementation invariants, not seven extra user forms. A default
template can fill structural fields from the release, but the human sees and
confirms every scientific or responsibility assertion attributed to them.

## Minimal receipt shapes (illustrative, not a cryptographic implementation)

| Receipt | Required semantic content |
|---|---|
| Offer | Stable ID; exact target tuple; requested scope; accessible evidence; excluded scope; responsible principal; resource/deadline envelope |
| Check | Offer ID; observed exact target; check method and evidence; findings/limits; role/control/conflict disclosure; authenticated origin; completion time |
| Reliance | Exact target and check IDs; authorized decision maker; kind of authority; allowed use; policy; conditions; expiry; correction endpoint |
| Amendment | Earlier record IDs; material change/evidence; requested remedy; authority if deciding; updated scope/state; links to new versions |

Public representations omit private account mappings, sensitive evidence and
fine-grained identifying metadata. The production identity and signature profile
must be separately implemented and reviewed. Labels on JSON are not authentication.

## A simple default allocation policy

Use credential/capability eligibility, conflicts and available resources to form a
candidate set. Start with randomized assignment within that set, workload caps,
and a reserved newcomer/supervised-review budget where qualified independent supervision is feasible. Charge setup and supervision to the shared person/skill ledger; this is an opportunity reserve, not a guarantee of completed service. Treat this simple baseline as
the default until a more complex local-trust router improves a preregistered
outcome under matched constraints. Do not require personalized PageRank, graph
max-flow, or a reputation score to use the four actions.

Where joint allocation uses trust routing, preserve frontier/control budgets in
the final assignment optimization. Do not independently reuse a frontier budget
for every candidate or normalize tiny raw capacities into large probabilities.
No feasible independent panel means **coverage unavailable**, not a quiet waiver
of the declared scientific contract. Alternatives are to narrow the claim,
obtain genuinely distinct expertise, or explicitly accept a different review
scope through the appropriate human authority.

Sponsors may buy compute or support review labor under disclosed arrangements.
They may not purchase scientific dispositions, credentials, challenge outcomes,
or hidden priority. Queue shares and sponsor concentration require separate
monitoring even if the verdict function never reads a payment field.

## Disputes without a universal tribunal

`Amend` includes challenges and requests for correction. Retain TDRG's existing
scientific-content, private-standing, and conduct/opening appeal lanes. A separate
operator compliance track handles rights/legal exposure. All share a small intake
front door, but each remedy is limited to its authority. Closing ordinary process
does not mean scientific agreement, and hiding content does not change its truth.

Bound ordinary handling using disclosed initial review and independent appeal
budgets, with reopening for material new evidence or process defects. Do not use
those budgets to eliminate applicable rights, legal duties, emergency reporting,
or reasonable access to the correct institution. Preserve dissent. Duplicate
complaints may share handling only after checking whether evidence, affected
persons, or requested remedies materially differ.

## Two worked paths

### Individual author, narrow and inexpensive check

An author offers a preprint-version claim and a script/table/figure bundle. The
contract requests numerical reconstruction, not evaluation of the underlying
measurement calibration. A reviewer records that the figure matches the table
and that calibration is outside scope. A journal editor can rely on the rendering
check for production quality. A scientist cannot infer calibrated evidence from
that reliance. If the table changes, the prior check remains about the earlier
table; a new check is needed for the new tuple.

### Large collaboration with an agent team

A collaboration offers a claim supported by a controlled high-resource run and
a public downselect. Its internal agents audit provenance and prepare the bundle.
An external specialist checks the downselect-generation method and witnesses a
bounded rerun, recording inaccessible raw inputs. Another independent specialist
examines the inference logic. The qualified scientific panel records a scoped
disposition conditional on the stated access boundary. The publishing identity
separately receives exact-artifact editorial authorization. A public observer
checks delivery. None of the internal agents counts as an extra external panel
member. A later calibration change opens targeted reconsideration, deduplicates
shared repair work, and exposes pending reliance until a new disposition exists.

## Backward-compatible entry and honest exits

| Existing practice | Entry into this profile | What must not be inferred |
|---|---|---|
| DOI/arXiv preprint version | Offer target plus immutable artifact identifiers | DOI existence is not review |
| Conventional review letter | Check with author-confirmed scope/limits | Text import is not consent to public release |
| Editor's decision | Scoped reliance by a named authorized role | No new scientific authority from the adapter |
| GitHub release/tests | Artifact and executable check evidence | CI success is not scientific judgment |
| COAR Notify announcement | Notification referring to a receipt | Transport acknowledgment is not acceptance |
| Correction/retraction | Amendment linking affected versions | Withdrawal need not erase all lawful history |

This is a proposed mapping. No independent implementation round trip has been
performed. Preserve unsupported fields as unknown; preserve extension namespaces;
do not discard scopes or privacy restrictions to obtain a convenient export.

## What would falsify the profile's value?

Compare against a conventional letter and a structured claim/evidence template
on the same tasks. If people mistake checks for authority, correction ownership
is unclear, or administrative labor rises without better detection/scope accuracy,
simplify or reject this profile. If complex routing does no better than constrained
random assignment, omit it. If the repair workload exceeds measured capacity,
restrict intake or narrow the service promise; never silently mark unresolved
claims current.

## Current reliance is a view, not an immortal receipt

Keep the historical scientific disposition unchanged when projecting current use.
A currentness view names its observation/checkpoint time, unresolved material
change relative to that receipt, evidence availability, expiry, and relying policy's maximum snapshot age.
An offline, expired or stale view reports **freshness unknown**, **expired**,
**dependency unavailable**, or **reconsideration pending**, as applicable.
Authenticated old bytes do not establish current evidence availability. A remote
PDF or cached reader cannot be forced to refresh. High-consequence use must follow
its declared currentness policy or decline reliance when freshness cannot be checked.
The synthetic `models/boundary.py` illustrates these distinctions with trusted
fixture inputs; it implements no signatures or live update service.

## Sampling and resource boundaries

Choose over canonical accountable-group panels before choosing representatives,
or demonstrate an invariant distribution under redundant labels. One-seat-per-group
constraints alone do not prevent an actor from increasing its selection chance by
exporting many equivalent labels. Define whether each probability bound applies to
offers or completed reviews; completion and retries can change distributions.
Record refusals/rerolls, keep support restrictions, and return unavailable rather
than silently weakening a promise at the completion boundary.

Use one person/skill/epoch budget across checks, audits, repairs, intake and appeals.
For time-sensitive obligations also record clock start, deadline, handler, remaining
work and unresolved applicability. Average load is not a deadline guarantee.
An appeal requires both available skill-hours and a genuinely independent authority
with access to the record and a way to implement reversal.
