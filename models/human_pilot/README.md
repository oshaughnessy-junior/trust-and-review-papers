# Pre-results human-interface design tools

These files prepare an evaluation; they do not conduct or authorize a study.
Read [evaluation-plan.md](../../onboarding/evaluation-plan.md).

```sh
python3 -m unittest discover -s papers/07-release-packet/models/human_pilot -p 'test_*.py' -v
python3 papers/07-release-packet/models/human_pilot/run_design.py
```

Python 3.9+ standard library only. Eight tests and 15 exact finite-design power
rows. All IDs and potential outcomes are artificial. The fixed published seed
is for reproduction, not a concealed allocation method for real participants.

`balanced_assignment` assigns two of four boundary units per preformed block.
`sharp_null_test` computes an exact two-sided Fisher randomization p-value under
the sharp no-effect null, not a generally exact test of zero average effect.
`design_power` enumerates every permitted assignment for a supplied fixed binary
potential-outcome table with at most six blocks. `missing_effect_bounds` reports
worst-case missing-outcome bounds on the realized randomized-arm rate contrast.
It does not bound the finite-population causal average effect: assignment
uncertainty and unobserved counterfactual outcomes remain. With unchanged potential
outcomes `(0,0,1,1)` in each block, assigning both successes to the card can yield
complete-data contrast bounds `[1,1]` while the true average causal effect is zero.
The regression preserves this distinction. These bounds are not confidence intervals.

The toy power family has baseline adequacy .5, no harms, and selected baseline
failures improved by the card. It is optimistic and not fitted. At the largest
tested effect (.5), exact power is 0 for N=8, about .325 for N=16 and .729 for
N=24. No tested design reaches .8; the coarse-grid threshold field is null.
Do not interpret this as a recommended study size or actual minimum detectable
effect for a real population.

Primary source verified 2026-09-25: Jason Wu and Peng Ding, *Randomization Tests
for Weak Null Hypotheses in Randomized Experiments*, author preprint v5 (2020),
https://arxiv.org/abs/1809.07419 . Title, authors, abstract and journal reference
were opened. Used only to substantiate the sharp-null/weak-null distinction;
local enumeration derivations and source code are self-contained.
