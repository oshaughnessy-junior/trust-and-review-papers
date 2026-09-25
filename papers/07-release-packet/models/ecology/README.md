# Local-rule attention ecology

A deliberately small **hypothetical** multi-period agent model. Agents are scripted
resource/skill/quality profiles, not LLMs or sampled humans. It studies whether
bounded credit and exploration are enough to prevent attention concentration and
repair overload. The answer is conditional and often negative.

From `papers/07-release-packet`:

```sh
python3 -m unittest discover -s models/ecology/tests -v
python3 -m models.ecology.run
python3 -m models.ecology.correction_game
```

Python 3.10+ standard library only. Nine perturbation regimes × three policies ×
eight paired seeds × 80 periods produce 216 rows in `results/sweep.csv`. Every
policy receives the same exogenous offers, defect states and common blind periods
for a given seed/regime; policy-dependent choices and observations diverge.
`summary.json` records source/test hashes, Python version, sweep hash, means and
seed ranges, and paired differences against uniform group routing. These ranges
are descriptive simulation variation, not confidence intervals. Full default
bounded-policy history is retained in `example-trajectory.json`.

## Only a few local rules

1. Each group emits synthetic jobs according to fixed arrival/volume, skill and
   defect parameters. One large team has more volume and capacity, but remains one
   accountable group. The first group also starts with a visibility advantage.
2. Route an oldest queued offer within a selected active group. **Prestige** uses
   cumulative completed attention plus pending-volume multiplication. **Bounded**
   uses decaying capped verified-check/correction credit, with an exploration
   mixture. **Uniform** chooses among active groups uniformly.
3. Select an independent qualified reviewer proportional to available capacity.
   Intake costs two tokens, check ten, independent audit five. Review quality is
   a stipulated diligence parameter; blind periods create common-mode errors.
4. Flagged defects or audit-discovered misses create correction jobs. Corrections
   consume twenty tokens (scaled in stress tests), oldest first, from the same
   independent qualified experts before new checks. Completed corrections and
   favorable audits supply capped credit.

Budgets reset each period; queue and correction debts persist. The simulator
records every offered job, completed job, unresolved offer and correction debt,
all stage labor, refused-capacity attempts and audits unavailable for lack of
capacity. Invitation/refusal counts are **attempts**, so a queued offer may count
again next period. An inability to find even two intake tokens is counted as a
capacity refusal without a paid invitation. Routing CPU cost and author labor
are excluded, not claimed free in a real institution.

The capacity/skill map is heterogeneous. Low-resource actors can perform one
check but cannot individually absorb a twenty-token repair. Tasks are indivisible
within a period; no fractional progress or pooled repair team is modeled. Therefore
aggregate spare capacity does not imply feasible specialized repair. Reviewer and
auditor control groups differ from the author, and an auditor differs from the
reviewer; actual independence is a trusted fixture assertion.

## What the metrics mean

- `correct_checks_per_offer`: correct toy judgments divided by **all offers**,
  including work not reached. It is not scientific value.
- `accuracy_among_completed`: conditional judgment accuracy; can be high while
  coverage and defect discovery are poor.
- `defect_detection_fraction`: defects found by a check or independent audit
  divided by all actual synthetic offered defects, including unresolved work.
- `attention_hhi`: sum of squared shares of completed author attention. Unequal
  offered volume makes this a descriptive concentration measure, not a fairness
  verdict. Compare per-group completion coverage too.
- `minimum_group_coverage`: the lowest completion/offered ratio, not minimum
  attention share. Reducing concentration can worsen this metric.
- `repair_backlog`: known pending correction jobs. It excludes undiscovered defects;
  a quiet correction queue can be a blindness signal rather than success.
- `labor`: intake + checks + audits + repairs over all agents, constrained by the
  same per-period individual capacities. No token is spent twice.

## Deliberate limitations and negative controls

Audit truth is a fixture oracle, conditional on access and capacity; it is not a
real scientific verification mechanism. A biased-verification regime gives large
team offers much greater audit access. Blind checks always return support, so
high common-mode blindness can produce low observed repair debt while missing
most defects. A unit test sets all claims defective, full blindness and no audits:
completed accuracy is zero while the repair backlog is also zero.

The model has no endogenous participation, strategic effort, lying about control,
staged repair credit, institutional enforcement or equilibrium. “Cooperation” here
means accomplished check/repair tasks under scripted willingness; it is not an
emergent motive. For strategic honest/shallow/refuse comparisons use the separate
`models/coupled` study. Recognition and dominance are hypotheses represented by
allocation feedback, not asserted explanations of human scientific conduct.

There is no claim that bounded routing beats uniform routing. The overload and
expensive-repair regimes expose tradeoffs and failures. Run-level differences are
exploratory, not optimized or preregistered. All policies and all regimes are kept.
See `../../manuscripts/local-rules.md` for exact equations and bounded conclusions.

## Correction-credit incentive bridge

The separate `correction_game.py` compares clean work with deliberately manufactured
and then repaired work using the same bounded score/attention update. Three credit
policies, six parameter cases and eight additional tests preserve a unilateral and
coalition counterexample, a no-allocation-credit baseline, cost internalization,
credible intent-detection assumptions and scarce independent repair capacity.
`results/correction-game.json` records exact payoffs and source/test hashes. This is
a two-action one-step game, not an equilibrium claim about the ecology or humans.
The ordinary ecology's original no-audit credit vulnerability remains unchanged.
The full tests command now runs eighteen methods.
