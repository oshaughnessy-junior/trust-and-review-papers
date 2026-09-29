# Review 1590: internal adversarial audit

## Disposition

No remaining blocker in the bounded sequential machine after the two findings below were addressed. This review is performed by a separate internal agent, not an independent institution or external scientific replication. The final integrated Section 5, reference README and reviewer response were checked against the current implementation: no substantive inconsistency remains. A minor timestamp wording correction was requested: the model records sequences, not dates.

## Findings and resolutions

1. Fixed audit quotas do not provide sequential incentive compatibility merely because their ex-ante marginals satisfy Proposition 4. With one audit in three slots, a revealed audit on a refused first attempt makes the later conditional audit probability zero. The positive effort condition then fails. The machine retains this explicit counterexample and limits its incentive statement to an ex-ante fixed-action annotation. The positive fixture precomputes completion outcomes before receiving audit results. This stipulation is not strategic commitment enforced by the API, cryptographic concealment, or an equilibrium proof.
2. The initial repair helper validated integer inputs but computed ratios before converting them, yielding floating output. All inputs now normalize to exact Fraction values. The independent example with matrix ((0,1),(0,0)), weights (3,1), and initial (1,0) now returns r=1/3 and bound=9/2 exactly.

## Independent checks

The final 14 author tests pass, including added transitive-staleness and successor-collision checks. A separately written enumeration checked 864 outcome sequences: eight seeds, four audit probabilities (1/8, 1/3, 1/2, 1), and all 27 length-three refused/passed/failed sequences. Across 1,248 accepted transitions it verified exact cumulative debit against the event ledger, nonnegative reservation, shared capacity, realized per-offer audit cap, unchanged state after duplicate request rejection, and release of the hold at termination. These checks are finite regression evidence, not a proof for arbitrary programs or adversaries.

The reserve includes worst-case attempt administration, completion work and the maximum audit count; actual work is debited once per accepted event. Rejected replay IDs and malformed transitions roll back within a single sequential object. These properties do not establish durable multi-process idempotency, transactional isolation, or race resistance. Actor names, declarations, evidence strings, group identities, random seeds and stored dependency edges remain trusted toy inputs. Undeclared edges remain undetected. The repair bound is an expectation annotation conditional on a supplied offspring envelope, not reserved repair capacity, a deadline, or a pathwise maximum.

## Reviewer table adjudication

The submitted local v1.1 PDF has ten nonempty pages. Its page-four completion table has three separate columns a, b, and Exact completed share, not an a/b column. Recomputing p=1/10 gives exactly 1/91, 1/10, 10/19 and 100/109 for its four rows. The concern is best addressed by clearer headers or an additional ratio column; no arithmetic correction or concession of an erroneous original fraction is warranted.
