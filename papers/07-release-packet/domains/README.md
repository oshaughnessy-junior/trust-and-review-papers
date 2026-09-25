# Four ways to enter MCRP

These are synthetic teaching cases for a public research prototype, dated
2026-09-25. They make no claims about actual people, experiments, lawsuits, or
institutional endorsement. All numerical data and organizations are invented.
The proposed common interface is **offer → check → rely → amend**. Different
communities retain their own standards of evidence and decision authority.

| Audience | Start with a question | Worked case | Small first contribution |
|---|---|---|---|
| Physics and astronomy | Which conclusions share this calibration? | [Shared calibration](physics-astro.md) | Reconstruct one number and name the untested measurement assumption |
| Biology | Did the experiment identify the effect? | [Batch, assay, replication](biology.md) | Map sample, batch and treatment before rerunning the statistics |
| Economics and social science | What population and estimand does this estimate concern? | [Identification and transport](economics-social-science.md) | Compare one preregistered estimand with one reported estimand |
| Law | Who can decide what, by when, with what remedy? | [Contested interpretation and deadlines](law.md) | Separate an evidence check from an institution's decision |

## Human entry

Choose one case, read its opening situation, and fill four sentences before seeing
JSON: “I offer…”, “I checked…”, “I would rely on this for…”, “I would reconsider
if…”. A facilitator then introduces the planted failure. The exercise succeeds
when the participant narrows an unsupported use or names missing evidence; it does
not require an affirmative verdict. Each case contains an answer key and a longer
clinic. Onboarding time and supervision count as real labor.

An established collaboration can import its existing release and review letter.
A lone researcher can contribute a one-claim numerical check. Neither must
reorganize its internal workflow. Public disclosure, authorship, and a relying
institution's authority remain explicit human decisions.

## Implementer entry

The independent, standard-library domain oracle is executable immediately:

```sh
python3 papers/07-release-packet/domains/fixtures/domain_models.py
python3 papers/07-release-packet/domains/fixtures/replay_receipts.py
python3 -m unittest discover -s papers/07-release-packet/domains/fixtures -p 'test_*.py'
```

`scenarios.json` contains semantic scenario fixtures, not wire-protocol conformance
vectors. Its declared schema separates immutable target content, human-readable
receipt narratives, expected domain calculations, and failure-injection goals.
The toy-agent framework in `../toy_agents/` provides a separate receipt engine;
using both does not turn either into a production scientific or legal service.
Fixture identifiers and control groups are trusted inputs. No identity discovery,
signature verification, confidential-data handling, or real decision is executed.

Every adapter must preserve `scope`, `limits`, exact target identity, and authority
kind. An adapter that can represent only `scientific` and `publication` reliance
must refuse a legal operational-decision type; it must not relabel that decision as
scientific to get through the API. Domain-specific semantic checks sit beside the
receipt engine rather than silently changing its contract.

## Evidence and contribution boundary

| Type | Contribution here | Evidence |
|---|---|---|
| P: established practice | Calibration uncertainty; reproducibility artifacts; trial registration; legal authority and procedural duties | Primary-source links in each case, checked 2026-09-25 |
| D: protocol design | Small receipts and two entry paths | Explicitly proposed templates |
| T: mathematical illustration | Shared-error floor, nonidentifiability, completion selection, capacity/deadline counterexample | Derivations and executable deterministic oracles |
| I: implementation | Four numerical cases and regression tests | Local command output; no field evidence |
| H: human efficacy | Better scope comprehension at tolerable labor | Unrun comparative study described in each case |

These cases do not claim new statistical theorems. Their contribution is to make
well-understood failure modes actionable at the point of reliance. Existing
artifacts can already carry much of this information. The closest comparator is a
plain structured claim/evidence/limitation template, not unstructured chaos.

No real participants were recruited. Drafting used AI agents; final human authorship
and release approval are governed by the release packet, not supplied by these
examples. Primary sources contextualize the cases; they do not endorse MCRP.
