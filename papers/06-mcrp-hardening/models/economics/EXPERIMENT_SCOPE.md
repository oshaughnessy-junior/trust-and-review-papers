# Synthetic economic sensitivity checks

Run `python3 run.py` (Python standard library only). The script regenerates `allocation.csv`, `queues.csv`, and `results.json`, recording configuration, seeds, Python version, script/data hashes, per-seed outcomes, summaries and descriptive Monte Carlo uncertainty. This is a small numerical exercise of the economic paper's declared models, not a calibrated test of MCRP or human behavior.

## Allocation experiment

Thirty matched seeds generate 80 lots with potential loss from lognormal(0,1) and detection productivity from lognormal(-.2,.5). Budgets are 20 and 80 hours. A designated quarter of lots forms an underserved stratum for sensitivity analysis; membership does not change true competence except in the explicitly different blind-spot scenario. All policies face the same true task values within a seed/scenario/budget.

Compare uniform effort; water filling using observed parameters; water filling with a 20% budget floor uniformly spread across underserved lots; and an unattainable latent-information oracle. The reserve policy solves the concave allocation with lower bounds, rather than accidentally overspending capacity. True avoided loss and regret are evaluated with generating values. A separate residual-loss floor records the blind spots that no effort of this type can remove.

Scenarios are known parameters; independent zero-mean log errors with SD .5, 1, or 2 in both value and productivity; a systematically underestimated underserved stratum; and a blind spot .8 in that stratum which the allocator ignores. Zero-mean log errors are not unbiased level estimates. The SD=2 stress condition was added after the initial narrower sweep as an explicitly exploratory high-misspecification check; all conditions and results are retained. These distributions and utility scales are invented, not estimates.

Selected results (mean paired difference from uniform; 30 seeds):

| Scenario | Hours | Estimated water-filling gain | Monte Carlo SE |
|---|---:|---:|---:|
| Known parameters | 20 | 25.929 synthetic loss units | 1.698 |
| Log-error SD 1 | 20 | 12.146 | 1.394 |
| Log-error SD 2 | 20 | -2.408 | 1.493 |
| Known parameters | 80 | 19.465 | 1.169 |
| Log-error SD 2 | 80 | -22.437 | 2.170 |

The known-parameter gain is expected from the definition of the optimization problem; it does not validate the assumed objective. The high-noise reversal demonstrates that optimizing noisy inputs can be worse than uniform allocation inside this model. Its magnitude is not a prediction for science.

Under systematic understatement at 20 hours, estimated water filling allocates the underserved quarter a mean .321 hours, versus 5 under uniform and 4.216 under the reserve policy. Mean true objective gain versus uniform is 20.254 without the reserve and 20.305 with it. These numbers do not establish that the reserve is costless generally: under known parameters it loses a mean 2.063 objective units relative to the optimum.

The “coverage” diagnostic counts lots receiving at least .25 hour. It is threshold-sensitive: with the 20-hour budget, the reserve gives each underserved lot a floor of .2 hour, which is positive service but below that arbitrary diagnostic threshold. Use exact allocated hours alongside counts; neither means a scientific check was completed. There are no setup costs or real task completion in this experiment.

## Aggregate daily workload experiment

Thirty matched seeds per configuration simulate 365 days and 8 staff-hours/day. Baseline primary utilization ranges over .5/.7/.9; arrival multipliers are 1/2/4; primary effort multipliers are 1/.75/.5. Attempts are Poisson. Primary handling cost is exponential with mean 2 times the effort multiplier. Each case adds an appeal with probability .1, with cost min(8,.5*Pareto(shape=1.5)) hours. The capped appeal cost has expectation 1.25 hours. The primary-load parameter excludes appeals; reported total load includes them.

Compare unbounded admission with a conservative one-day estimated-work reservation policy. The reservation policy subtracts actual current backlog, computes available expected-service slots, and admits the first arriving cases up to that limit. It does not know their actual future handling costs. Rejected cases are counted but are **not queued**. This is a model of bounded ordinary commitments, not a policy for rights-sensitive claims or legal deadlines.

Selected matched-stream means:

| Baseline primary load, arrival multiplier, effort multiplier | Policy | Expected total offered load | Final backlog (hours) | Rejected cases | Completed staff-hours |
|---|---|---:|---:|---:|---:|
| .7, 1, 1 | Unbounded | .74375 | 5.541 | 0 | 2174.295 |
| .7, 1, 1 | One-day reserve | .74375 | .624 | 244.267 | 1651.898 |
| .7, 2, .75 | Unbounded | 1.1375 | 404.294 | 0 | 2912.498 |
| .7, 2, .75 | One-day reserve | 1.1375 | .140 | 772.300 | 2058.298 |

The smaller admitted backlog comes with rejected work and lower resource utilization. It is not evidence of improved social welfare or a successful fairness policy. In particular, this conservative one-day gate rejects many cases even in an underloaded system. An implementable design would choose a larger bounded commitment horizon or a transparent waiting mechanism appropriate to its obligations, then evaluate the tradeoff rather than reward a small displayed queue.

These are aggregate fluid-workload recursions, not individual waiting-time estimates. The model omits specialized capabilities, incoming triage/duplicate costs, legal protected lanes, priority, abstention, strategic reattempts, common-cause absences, and time-varying capacity. Rejected users can resubmit in reality; that feedback is not simulated. Backlog decrease does not establish timely legally required handling. Mass-balance assertions confirm admitted workload equals completed work plus final backlog for every run.

## Interpretation and review limits

The full files contain 1,440 allocation rows and 1,620 workload rows. Summaries use across-seed standard errors and normal-approximate descriptive intervals; they are not simultaneous coverage guarantees, empirical population uncertainty, or preregistered hypothesis tests. No outcome establishes adoption, fairness, scientific quality, legal safety, or mechanism-wide incentive compatibility. Independent review and human release approval are unrecorded.
