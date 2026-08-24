---
artifact_role: preregistered-evaluation-design
status: proposed
date: 2026-08-24
publication_status: private-not-approved
claim_posture: no-benefit-claim
---

# Evaluating reviewer trust domains

This plan tests whether the proposed Trust-Domain and Review-Governance (TDRG)
profile behaves better than simpler alternatives under declared attacks. It
does not test whether a cryptographic mechanism makes reviewers honest or
whether graph rank establishes scientific validity.

## 1. Questions

1. Does root-relative, topic-scoped routing limit the effect of malicious or
   poorly calibrated actors better than a global recursive reputation?
2. Do frontier-capacity and control-diversity constraints add protection beyond
   personalized graph rank?
3. Can fresh review personas preserve case-level anonymity while still
   enforcing one-person/one-assignment limits and private appeals?
4. Do explicit bridges prevent cross-topic authority laundering?
5. Can a fork localize governance capture while preserving the common review
   and scientific record?
6. What does each safeguard cost in qualified-reviewer coverage, newcomer wait,
   operational trust, privacy, and compute?

## 2. Frozen comparison arms

Use the same synthetic actors, cases, ground truth, assignments, review
contents, and event order in every arm.

| Arm | Routing and standing | Required interpretation |
|---|---|---|
| A0 | eligibility credential plus uniform random routing; no reputation | minimal non-graph baseline |
| A1 | raw review-feedback average or vote count | deliberately weak popularity baseline |
| A2 | one global EigenTrust/PageRank-like recursive score | global mean-field baseline |
| A3 | topic-scoped personalized restart walk from declared roots | local graph baseline |
| A4 | topic-scoped personalized walk after max-flow/frontier caps, then control-diversity and workload constraints | proposed TDRG baseline |

Within every arm, assignment SHOULD use the same established fair/randomized
assignment method after the arm determines eligibility. Otherwise improvements
from assignment randomization could be misattributed to the trust model.

The exact implementations, seeds, parameters, graph snapshots, and evaluator
digests MUST be frozen before outcomes are inspected. Results MUST include
sensitivity analyses, not only the best parameter setting.

## 3. Populations and scenarios

Construct at least three topic layers with partially overlapping expertise, one
multidisciplinary case, two governance parents, and one fork. Include:

- calibrated senior reviewers, calibrated newcomers, and narrow specialists;
- sincere but systematically mistaken reviewers;
- qualified dissenters whose findings are confirmed late;
- Sybil accounts controlled by one human;
- multiple real humans in a review/voting ring;
- shared employer, supervisor, funder, and infrastructure clusters;
- an honest and a captured trust root;
- a malicious or self-interested registrar, assignment service, reputation
  custodian, publisher, and manager, one at a time and in declared coalitions;
- restricted-data and expensive-compute reviews whose outcomes arrive late;
- sparse domains in which aggressive defenses can exclude nearly everyone.

Run at least these attacks:

1. ballot stuffing and reciprocal helpfulness voting;
2. Sybil edge injection at varying attack-frontier capacity;
3. real-person collusion that passes uniqueness checks;
4. bad-mouthing of a competent minority reviewer;
5. prestige laundering through a high-status root;
6. cross-topic trust transfer with and without an accepted bridge;
7. whitewashing, on/off behavior, and credential expiry;
8. assignment manipulation by management;
9. false conflict or conduct allegations intended to expose identity;
10. deanonymization using timing, rare attributes, graph structure, and prose;
11. bridge capture, parent overreach, policy rollback, and evaluator compromise;
12. a domain fork followed by selective recognition and later reconciliation.

Scientific fixtures MUST include planted material defects, harmless deviations,
false alarms, unresolved disputes, and later reversals. Review-quality labels
MUST be assigned from the evidence and rubric, not from agreement with the
editorial decision or simulated majority.

## 4. Primary measures

- **capture radius:** fraction of honest actors/cases whose routing or private
  standing changes materially after the attack;
- **false eligibility / false exclusion:** malicious actors admitted and
  qualified actors excluded, by topic and newcomer status;
- **material-defect yield:** confirmed material defects found per reviewer-hour;
- **minority survival:** probability a qualified dissenting review remains
  discoverable, routable, and unsanctioned until adjudication;
- **cross-topic leakage:** imported authority without an accepted, unexpired
  bridge;
- **control concentration:** assignments and effective influence after
  employer, supervisor, funding, and infrastructure clustering;
- **newcomer access:** wait time, supervision load, progression, and erroneous
  adverse classification;
- **appeal quality:** false allegation, reversal, correction latency, and
  identity-opening rates;
- **privacy loss:** persona linkage precision/recall and effective anonymity set
  under each declared adversary;
- **operational cost:** human/agent review intelligence, governance time,
  credential operations, storage, communication, and evaluator compute;
- **policy replay:** identical view from identical frozen inputs and explicit,
  explainable difference under a changed policy;
- **fork localization:** proportion of shared records preserved and malicious
  influence crossing the fork boundary.

Report distributions and subgroup results. Averages alone may hide capture of a
small specialty or retaliation against a minority view.

## 5. Falsifiable hypotheses

- H1: A3 and A4 reduce capture radius relative to A2 when malicious influence
  enters through a bounded frontier.
- H2: A4 reduces capture from dense review rings relative to A3, at a measurable
  cost to coverage in sparse domains.
- H3: topic scoping plus explicit bridges reduces cross-topic false eligibility
  relative to A2 without materially reducing legitimate multidisciplinary
  coverage.
- H4: delayed typed outcomes preserve qualified dissent better than raw votes.
- H5: forked overlays localize a captured root or policy while preserving all
  public scientific and review objects.
- H6: brokered per-case personas meet duplicate-prevention and private-appeal
  requirements, but anonymity fails when timing or attribute pools are too
  small; the system correctly downgrades its claim to `confidential`.

## 6. Stop and no-go conditions

Do not promote TDRG into core MCRP conformance if any of these remain true after
mitigation:

- the proposed arm has equal or greater capture radius than the global arm in
  the primary threat regimes;
- newcomer or minority false exclusion exceeds the predeclared bound;
- an ordinary operator can link personas across cases or directly recover civil
  identity contrary to the manifest;
- a raw vote, graph anomaly, or scientific disagreement can automatically
  sanction an actor or open identity;
- imported authority crosses a topic/domain boundary without importer consent;
- policy replay is not deterministic from the frozen inputs;
- a fork cannot preserve and independently interpret the shared record;
- operational demands make the claimed safeguards fictitious in the intended
  deployment.

## 7. Real-community pilot

After synthetic testing, run a sanitized, consented pilot with at least two
independently governed domains. Predeclare cases, compensation, access classes,
opening rules, stopping rules, incident response, and participant exit. Use a
parallel conventional-review arm where ethically possible. Collect qualitative
evidence about management pressure, reviewer burden, explanation quality, and
whether actors understood the difference between review feedback, private
standing, scientific disposition, and conduct findings.

No real pilot should begin until privacy/security review and an accountable
operator for appeals exist. No participant's civil identity or private trust
history belongs in the public evaluation dataset.
