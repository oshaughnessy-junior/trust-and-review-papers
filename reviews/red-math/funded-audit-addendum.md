# Independent review: delivered audits, participation and funded resources

## Judgment

The funded-audit addition closes a useful and narrow simulation loop. It reserves audit and reward budgets, draws a fixed concealed quota, commits actions, performs selected inspections and transfers stipulated collectible losses. It no longer merely inserts an unsupported audit probability into agent utilities. **Qualified assent continues after the two numerical defects below were repaired and independently rechecked.** This remains a one-shot game with fixed identities, trusted concealment, automatic auditor effort and artificial token utility. It is not a deployed sanction system or a whole-network equilibrium.

## Findings and repair verification

**RM-5: epsilon authorized positive work against no hours.** The original ledger accepted a 1e-12 audit debit against a zero reservation. With positive review/audit costs of 1e-13 and zero actual reviewer/auditor capacity, the entire default program still executed. The per-person tolerance was bounded rather than the earlier unlimited per-hold accumulation, but it contradicted the pathwise funded-hour claim. The repaired ledger uses exact decimal-rational capacity, reservation and debit arithmetic. It rejects the zero-capacity examples and correctly accepts three .1-hour debits against .3 hours. Original code and outputs remain preserved.

**RM-6: floating ties changed the declared strategy.** At q=1/8, alpha=.1, beta=.3, loss=2, reward=.6, effort=.05 and outside option zero, honest and shallow utility both equal 21/40. The declared tie rule selects honest work; original float arithmetic chose shallow work for all eight actors. Conversely, reward=.4, effort=.1, outside=.3, alpha=0 and q=1 should select refusal at equality; floating arithmetic chose honest work. Exact decimal-rational utility comparison now implements the stated refusal/honest/shallow order, with exact utility fields in output. Both original failures are executable from the archived source and both repairs were independently confirmed.

`funded-original-model.txt` preserves the original. `funded_review.py` runs that archived source as a local fixture and checks the repaired implementation, writing `funded-review-results.json`. The preserved vulnerabilities are not current release implementations.

## Independent finite-path oracle

The adversarial oracle independently computes rational utilities and the preferred action for each quota subset. It then enumerates every positive-probability sanction outcome, injects that controlled selection/detection path into the actual runtime, and checks its actions, event debits, collateral transfers and realized utilities. This is an independent conditional outcome oracle, not an alternative random-number generator certification. The imported quota sampler was separately checked in the earlier mathematical review.

The oracle covers **3,839 positive-probability paths across nine configurations**: concealed funded audits, partial refusal, early selection disclosure, high-false-positive total refusal, certain false sanctions, both tie boundaries, shared cross-role hours and no inspections. Exact expected results include:

| Configuration | Honest / shallow / refused | Expected inspections | Expected sanctions | Expected utility per ordinary actor |
|---|---:|---:|---:|---:|
| Concealed funded | 8 / 0 / 0 | 4 | 2/25 | 7/25 |
| Four fixed refusals | 4 / 0 / 4 | 2 | 1/25 | 7/25 among participating actors |
| Early disclosure | 4 / 4 / 0 | 4 | 2/25 | 43/100 before selection is revealed |
| High false-positive refusal | 0 / 0 / 8 | 0 | 0 | 1/10 |
| Certain false sanctions, larger reward | 8 / 0 / 0 | 4 | 4 | 2 |
| Honest/shallow exact tie | 8 / 0 / 0 | 1 | 1/10 | 21/40 |
| Honest/refusal exact tie | 0 / 0 / 8 | 0 | 0 | 3/10 |

The early-disclosure expected utility is averaged before disclosure across selected/unselected status; actual commitment uses the revealed 0/1 probability. It must not be substituted into the concealed-information best-response calculation.

Separately, I reproduced all **11 saved full traces and 220 seeded sweep rows**, including status, action/detection counts, token expenditure and the broken-promise regret measure. All **18** current author tests pass. These replications test both structural cases and the actual recorded RNG runs; neither represents human data.

## Conditional marginal and participation

The k/N statement is correct for each fixed actor whose participation decision and private shocks do not depend on the concealed subset. Leaving refused slots unused preserves that actor's marginal. It does not force the realized audit fraction among participants to equal k/N in every run, and the all-refusal denominator is undefined. The manuscript now states these distinctions.

All actions are committed before any outcome is exposed. Early disclosure correctly changes the relevant probability to zero or one and makes the unselected actors choose shallow work. Arbitrary selection-dependent participation, collusion, public seed inference, sequential outcome leakage or replacement of unused slots would require a different conditional calculation. The fixture supplies the information boundary; the output's eventual disclosure is for evaluator inspection, not an implementation of secrecy.

The k=0 edge case needs no binomial coefficient with negative lower index: it has inclusion probability zero directly. The manuscript states this separately after review.

## Resource and authority boundaries

Audit tokens and reward tokens are reserved separately; sanctions do not refinance those promises. Per-actor collateral makes the stipulated loss collectible within the fixture. It does not establish consent, legitimate legal authority, real wealth, capital costs or a recommended bond requirement. Requiring collateral can exclude low-resource contributors; the model's unavailable result is a disclosed boundary, not an institutional recommendation.

The dedicated mode's eight decision accounts share one reviewer capacity key. They are eight modeled task/contract choices, not eight independently resourced people. Cross-role mode similarly maps tasks to two actual resource pools. Different account labels must not be read as independent scientific judgment. The conservative shared-role reservation covers the worst quota subset before sampling, preventing capacity-conditioned rejection from silently changing the lottery. This consumes opportunity to use otherwise spare hours; it is not an optimal allocation claim.

Review and audit hours are distinct from utility effort and token units. The utility function stipulates unit marginal utility for reward and loss tokens. It is not calibrated wealth utility. Refusals here consume no human hours; the coupled queue has a different refusal-cost model. Those assumptions cannot be silently combined into one empirical estimate.

Auditors execute automatically with given detection probabilities. No model of auditor refusal, strategic effort, institutional budget diversion, sanction appeal or false-positive reversal is supplied. The new program closes audit delivery within its declared one-shot fixture. It does not repair the old coupled model retrospectively or make its assumed q empirically credible.

## Collective disposition

The new experiment supports a stronger but still bounded claim: some promised audit incentives can be connected to actual simulated resource reservation and execution, while leakage, false positives, weak capacity and collateral shortages produce visible failure. It does not make the entire collection one coherent institution. Keep the old perceived-audit model, this delivered-audit model and their incompatible assumptions explicit in the synthesis. My continued research-seed assent includes this repaired addition and its negative controls.
