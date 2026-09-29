# Review 1590: four actions in one bounded execution

This directory is a precise **sequential research fixture**, not a production
protocol implementation, scientific validator, authentication layer, or new theorem.
All author/verifier/decision-maker identities, group membership, evidence references,
check results, utility parameters and repair laws are supplied toy assertions.
No real scientific computation or independent review is performed.

## State and command schema

`Machine` stores at most eight immutable target identities and 64 accepted events.
The fixed group universe is A/B/C with uniform two-group panels. Counts only name
interchangeable aliases; they do not create independent people or capacity.
Exact numeric inputs use integers or `Fraction`. Commands share a nonempty unique
`request` string, one `action` in {offer,check,rely,amend}, and these arguments:

| Action | Required fields and guards | Effect |
|---|---|---|
| offer | actor=`author`; new target; nonempty scope; tuple of unique dependency IDs; integer seed; exact q and audit budget satisfying the declared static inequality and hard cap; sufficient shared work capacity | Create open target; fix three panel draws and normalized alias draws; select a bounded audit subset; reserve worst-case check and audit work. |
| check | actor=`verifier`; exact open target/scope; the planned representative tuple; outcome refused/failed/passed; nonempty evidence reference; boolean asserted audit outcome | Consume the next fixed slot, debit invitation and completed-check work plus any selected audit, record the result, then remain open after refusal or close on completion/exhaustion. |
| rely | actor=`decision-maker`; ready target; exact scope and successful last-check sequence | Append a separate reliance record, initially current. Check success never produces this decision implicitly. |
| amend | actor=`author`; changed ID; fresh, noncolliding successor ID; candidate repair matrices and witness | Compute declared transitive affected closure, mark affected target phases pending and current reliance false, release unused holds; attach a repair planning bound if available. |

Every accepted event contains sequence, request/action, authority and target/scope
or amendment IDs, action-specific payload, and exact spent/held totals afterward.
Checks add panel, aliases, slot, result, evidence, audit execution and work charge.
Amendments add affected targets and certified/uncertified planning output. Prior
event dictionaries are never rewritten. Rejected commands roll back state and
consume no request ID, draw or capacity. The demo separately records rejected
calls; there is no persisted refusal log, database, network, signature or race
control. `request` protects only this in-memory bounded episode, not distributed
or authenticated replay. Internal dictionaries are not a hostile Python-object
security boundary.

Targets use phases open, ready, failed, exhausted, pending-amendment. Only open
accepts checks; only ready permits new reliance. Ready means the supplied check
assertions passed, not scientific validity. An amendment blocks affected ready
states even with unchanged claim text. A successor ID is a proposed new version;
no successor offer, repair, renewed approval or carry-forward is automatic. New
offers cannot depend on known retired or non-ready targets. Missing dependencies
remain unknowable: the retained negative test leaves an undeclared dependent ready.

## Single worked episode and composition boundary

The demo offers `mean@v1`, scope `three synthetic values only`, depending on
`data@v1`. Uniform AB/AC/BC sampling gives p=1/3 for category AB. The toy completion
oracle sets a=1 for AB and b=1/4 otherwise. Independent completion coins are drawn
before any audit result is consumed; panel draws and alias draws use separate
streams so extra aliases cannot perturb the panel law. This stipulates IID and
nonadaptive behavior; the API itself does not force actors to follow that policy.

For at most three attempts: s=1/2, expected attempts=7/4, completion probability=7/8,
and AB share among completions=2/3. Invitation cost is 1/10 and completed-check cost
one in **abstract work units**, giving expected checking work 21/20. Fixed slots
receive a quota lottery with ex-ante q=1/3 and one unit per actual audit; audit
budget is one. Expected audit work in this nonadaptive stopped trace is 7/12.
A worst-case 43/10 work units (three complete checks plus one audit) is reserved
before drawing; finite capacity therefore does not introduce a completion-dependent
admission rule inside this example. Neither utility units nor these abstract work
units are calibrated human hours or actual currency. Intake, evidence inspection,
reliance and administration overhead are unmodeled rather than claimed free.

Static audit utility parameters c=1/10, R=1, u=0, alpha=1/20, beta=17/20, F=1 give
effort lower bound 1/8 and hard cap 1/3. The configured q lies between them.
This is an **ex-ante fixed-action annotation**, not an implemented dynamic incentive
guarantee. Audit selection and outcome reporting use trusted fixture inputs; the
seed is not secret or cryptographic, and the API reveals audits and work charges.
After a first-slot audit is disclosed, later conditional q is zero. A strategic
actor can then prefer shirking even though the offer preflight passed. The test
retains that counterexample. Operational sequential incentive compatibility would
need a separate concealment/commitment or conditional-policy design. Reward funding,
sanction enforcement and truthful scientific effort are not implemented.

The retained realization draws AC,AC,AB, with refused,refused,passed outcomes. The
third slot is audited; actual work is 23/10. Separate reliance cites check sequence
4. Amending data to v2 leaves that historical event intact and makes the live
reliance noncurrent. One affected claim seeds Z0=(1,0). The two matrices
M1=((1/4,1/4),(0,1/2)) and M2=((1/2,0),(1/4,1/4)), with w=(1,1), satisfy Mw≤w/2.
The conditional expected cumulative weighted-work bound is two. **No repair work
is reserved or executed.** Invalid or noncontracting proposed witnesses leave
this bound unavailable but do not stop amendment invalidation. This prevents an
expectation from silently becoming a deadline or capacity guarantee.

All four models therefore annotate or constrain the same trace, but their
favorable results are not combined into a claim of truthful equilibrium or
operational safety. The linkage is an executable accounting and decision procedure.

## Reproduce

From the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s papers/10-review-1590 -p 'test_*.py' -v
PYTHONDONTWRITEBYTECODE=1 python3 papers/10-review-1590/demo.py
```

`results.json` retains exact rational outputs. Tests cover guarded transitions,
rollback, exhausted refusals, aliases, hard caps, missing/stale/wrong-scope authority,
transitive amendments, successor collision, integer exactness, concealed-premise
failure and hidden lineage. Synthetic seeded checks are not measured efficacy.
The existing `papers/08-agent-uptake-theory/integration` cost bridge remains
separate: this trace supplies neither calibrated error rates nor measured adoption
utility, and its expected work cannot be relabeled as adoption benefit.

## Licensing and attribution

Original code and fixtures here are MIT licensed; original prose is CC BY 4.0,
under the same grants and limits as the [packet license](../07-release-packet/LICENSE.md)
and [MIT terms](../07-release-packet/LICENSES/MIT.txt). Attribution: MCRP contributors,
maintained by oshaughnessy-junior, with substantial drafting, implementation and
internal critique by Codex agents under the corresponding human maintainer's
orchestration. Internal agents are not independent institutional reviewers.
