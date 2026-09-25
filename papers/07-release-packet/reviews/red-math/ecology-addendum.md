# Ecology addendum and full-packet collective position

The mathematics reviewer inspected the new `local-rules.md`, ecology implementation and all recorded results, alongside the previously reviewed mathematics, coupled simulator, blog and human/agent onboarding. This addendum records the final substantive review of the research model before repair verification.

## What was independently confirmed

`ecology_review.py` reran all **216** scenarios and compared all CSV metrics. It checked **351** aggregate metric summaries and paired differences, reproducing every reported mean, minimum and maximum. All policies shared the same offered-input fingerprints and number of common-blindness periods within each seed/regime. Every trajectory conserved actor-period integer labor and every bounded-policy score stayed in [0,1]. Seed ranges and paired means are appropriately described as descriptive sensitivity, without inferential confidence claims.

The softmax attention ceiling is correct for K>=1, epsilon in [0,1] and beta>=0. State these parameter ranges beside the result; they are already enforced by the routing implementation. The ceiling applies to a selected group at a particular lottery with its active set, not to final population coverage. It is not a completed-panel or downstream reliance bound.

The separate symmetric mean-field multiplier is correct. An independent central difference in a zero-sum direction gave 0.9283333333304222 versus the analytic 0.9283333333333333 at K=6, epsilon=.15, beta=2, mu=.1. The simulator is not that map: credit comes from audits and correction, and heterogeneous capacity and queues change feedback. The manuscript prominently preserves this distinction. The local threshold supplies a diagnostic, not a proof of global self-organization or cooperation.

The shared-blindness negative control was independently reproduced with three fully diligent but jointly blind groups: six completed checks, zero accuracy, zero recognized repair debt. This is a useful demonstration that throughput and quiet correction queues can conceal common error.

## New incentive boundary: correction credit can reward avoidable defects

A second negative control uses three otherwise identical groups with 100 capacity tokens each, no audits, no common blindness and perfectly diligent checking. Keep the offer process/configuration fixed, and compare all clean offers with all defective offers. After 30 periods, clean work produces no correction credit and total score about **0.04239** (decay of initial credit). Defective work produces 22 completed corrections and total score about **1.34493**. Repair gives credit to both handler and original author.

This does not demonstrate that actual participants would deliberately produce defects. It does show that the recognition mechanism contains a potential incentive to create work whose repair earns credit, while clean unaudited work earns none. A false alarm can also create a correction task; the model does not adjudicate whether correction credit was deserved. Because offer defect rates, diligence and participation are exogenous, the present ecology cannot establish incentive compatibility of this rule.

Keep the result as an explicit unresolved mechanism question. The strongest next experiment allows a toy author to choose costly prevention versus strategically created defects, then compares recognition and resource outcomes. Separate useful disclosure/correction credit from avoidable-defect production without punishing honest error reporting. A large punitive rule table is not yet warranted by this synthetic case; the uniform baseline remains the default comparison.

## Collective exchange

The domain/legal reviewer independently noticed author credit after false-alarm correction and agrees this is a disclosed research boundary, not a reason to block a protocol-seeding publication. Both reviewers agree that the packet makes no explicit claim that bounded attention, group invariance, audit incentives and repair bounds compose into a general cooperative equilibrium. The collective report should say that plainly: each positive result has its own assumptions, and passing the adjacent runtime checks does not supply identity, competence, funding or legal authority.

The runtime reviewer found an accumulating ledger-tolerance defect and public-export concerns; those require their own repair/recheck. The mathematics reviewer found the audit endpoint inconsistency RM-3, with the original preserved for regression. These concrete software defects are different from the remaining hypotheses about human incentives and adoption.

**Qualified collective assent:** support a curated public research seed once the concrete defects and final artifact checks are closed. The blog gives a reasonable invitation; human onboarding can begin with one synthetic claim and a colleague, while agents can immediately run the models. No need to construct an entire appeals institution before people discuss a research protocol. Public attribution, licensing scope, exact destination/artifact and responsible intake remain concrete publication choices. This assent does not authorize or certify a live dispute/review service.
