# Pre-results evaluation plan: does the smaller interface actually help?

**Draft design, 25 September 2026. No human study has been conducted, approved,
registered or recruited through this packet.** This is a decision-ready outline
for a future evaluation, plus executable artificial design calculations. It does
not claim that the four-action interface is superior or that a small pilot can
establish equivalence. Applicable institutional review, consent, data handling,
recruitment arrangements and responsibility must be resolved before any study.
This document creates none of those permissions.

## The question and the deliberately strong baseline

Does an **offer/check/rely/amend card** help people respond adequately to material
changes without spending more collective attention than an ordinary structured
referee template? The protocol should earn its additional concepts. A positive
result for a machine parser is not an answer about the human interface.

The baseline is a competent structured template, not an unhelpful blank page.
Both formats receive identical source material, exact version labels, check
results, scope limitations, amendment notices and relevant evidence. The template
uses familiar headings such as “item reviewed,” “methods and evidence,” “findings
and limitations,” and “follow-up.” The card arranges the same information under
offer, check, rely and amend. Equalize reading length and visual prominence as far
as practical; retain both rendered artifacts and document any remaining mismatch.
If the card alone receives an automatic alert or extra evidence, the comparison
would test a bundle of information advantages rather than the interface.

This evaluation tests a **frozen minimal interface**, without reputation scores,
market payments, graph routing or mandatory adoption of a new publication venue.
Participants can keep their ordinary paper and referee letter. The intervention
is the portable boundary record and its presentation.

## Primary task and estimand

Each randomized boundary receives two short fictional cases. One asks whether a
numerical conclusion may still be used after a calibration amendment. The other
asks what can be concluded after access to supporting evidence changes. A neutral
orientation teaches the task mechanics without exposing the alternative format.
Then the boundary reads its assigned format, makes a scoped reliance decision,
receives a scripted material change, and records its response. No task asks for
real medical, legal or scientific advice.

**Case N: changed numerical input.** The original object records $x=10$, offset
$c=8$, and the limited numerical claim $x-c>0$. The amendment changes $c$ to 12
for that exact version's intended use. An adequate response identifies the changed
input and affected claim, declines to continue the old positive conclusion, and
requests or supplies a new scoped calculation. Correct arithmetic alone is not
enough if the participant presents an old receipt as authorization for the new
result. This example is arithmetic; it represents no real experiment.

Include an unaffected-use positive control in this same case: the supplied raw
scalar remains 10, so the separate statement “the supplied raw scalar is positive”
still follows from the unchanged public input. The answer should distinguish
that narrow statement from the amended offset-adjusted claim. A script that
declares every old statement false or unsupported must not pass merely because
it sounds cautious. A participant need only explain the distinction; choosing
not to take a real action or declining the exercise remains permissible.

**Case E: evidence unavailable.** A synthetic evidence attachment becomes
inaccessible while the original dated check remains authentic. An adequate
response preserves the historical record, states that present evidence access is
unresolved, and avoids asserting either that the original claim has become false
or that its present reliability has been re-established. The task states what the
participant can access; no private data or real rights dispute is involved.

Freeze a scoring key with acceptable paraphrases and examples of borderline
answers before allocation. Two assessors unaware of assignment score redacted
responses independently; record disagreements and adjudication time. Because
wording can reveal the arm, record assessor guesses and acknowledge incomplete
blinding. Domain experts should check task clarity before the trial without
contributing trial outcomes to the power assumptions.

Let $Y_i(z)=1$ if randomized boundary $i$ under format $z$ gives an adequate
response to **both** material changes within the observation window, with no
critical authority upgrade. Otherwise $Y_i(z)=0$, subject to the missing-data
rules below. The primary finite-sample estimand is

$$\Delta_Y=\frac1N\sum_{i=1}^N\{Y_i(\mathrm{card})-Y_i(\mathrm{template})\}.$$

This is the average effect on the enrolled randomized boundaries, each weighted
once. It is not an estimate over all scientists, all readers or all members of a
large collaboration. A task-level score, each individual critical failure,
recognition of the unaffected-use control, time to notice change and appropriate
refusal are secondary measures. Merely clicking
an amendment notice does not count as adequate response.

## Total attention is a co-primary decision quantity

Record person-minutes, including participants, team consultation, facilitator
help, technical support, assessor review, adjudication and follow-up required by
unresolved work. Separate study-only measurement labor from labor an operational
interface would routinely require; report both. Do not count two simultaneously
working people as one minute of labor. Keep elapsed latency as another measure.

For boundary $i$, let $L_i$ be attributable total person-minutes up to a common
predeclared horizon, including follow-up during that horizon. Report
$\Delta_L=N^{-1}\sum_i\{L_i(\mathrm{card})-L_i(\mathrm{template})\}$, arm totals,
per-role totals, tails and the number still unresolved at the horizon. This is a
restricted-horizon estimand, not a claim that late work costs zero. Track later
work descriptively when authorized. Allocate shared facilitation overhead by a
frozen rule, such as equal time per randomized boundary, and also show the full
unallocated overhead total. Recruitment and orientation costs remain visible.

The potential-outcome notation $L_i(z)$ also assumes that another boundary's
assignment does not change this boundary's available help or measured work.
Shared facilitators can violate that assumption through fatigue or competing
support requests even without cross-arm coaching. Prespecify support availability,
session order and overhead allocation; record congestion and deviations. If
material spillovers cannot be prevented, redesign the randomization unit or
define an assignment-level service-regime estimand before recruitment. An equal
division of overhead is an accounting convention, not proof of no interference.

Do not use time **only among successful completers** as the primary cost result.
A format that makes people abandon a task can look artificially fast. A “minutes
per adequate response” ratio may be a descriptive secondary statistic, with both
numerator and denominator shown; it cannot replace the two separate outcomes.
No weighted utility score should conceal an authority mistake behind a small time
saving.

## Enrollment boundary, strata and assignment

Use two initial strata:

1. People new to the framework, acting for themselves.
2. A declared representative or small fixed team acting for an existing large
   collaboration or organizational workflow.

The experimental unit is the **accountable participation boundary**, not the
number of internal agents or collaboration members it represents. List its actual
study participants before allocation. Multiple representatives of one collaborating
organization belong to the same randomized boundary if they could share the
intervention. Do not multiply the effective sample size by calling them independent
people. Report team size and all participating person-minutes; equal boundary
weighting is a deliberate estimand choice and may differ from person weighting.

Form four-boundary blocks within each stratum using pre-treatment familiarity
and, where feasible, relevant domain background. Assign exactly two boundaries
per block to each format with a concealed allocation process independent of
recruitment. Freeze eligibility and block formation before revealing assignments.
The code's published toy seed is illustrative, not allocation concealment for a
real study. Do not choose a seed until the assignments look convenient.

The **primary comparison is parallel first use**, not crossover. People cannot
unlearn a card's scope/authority concepts before reading the template. A later
optional crossover can collect preferences and transfer-learning observations,
but cannot be pooled into the first-use causal estimate. If crossover is studied
later, randomize order and model period, case, learning and carryover explicitly.
A “washout” interval is not evidence that conceptual learning has disappeared.

Within each arm, counterbalance the two fictional cases' order independently of
format assignment and preserve that schedule. If learning from the first case
changes the second, the primary bundled two-case task still has its randomized
interpretation; exploratory case-specific effects require order labels. Domain
skins for physics/astro, biology, economics/social science and law can be tested
in later replications. A tiny study cannot support separate efficacy claims for
all four domains. If domain-specific primary estimates are desired, redesign the
blocking, estimands and sample planning before enrollment.

Prevent cross-arm coaching during the primary task. Log shared facilitators,
institutional membership, troubleshooting and any visible contamination. If
boundaries cannot be kept from sharing the intervention, randomize the interacting
cluster and analyze at that level. Independence is a design constraint, not a
standard-error option selected after observing the results.

## Refusal, unresolved work and missing outcomes

Publish the full flow: approached, eligible, consented, randomized, started,
completed initial decision, received amendment, completed response, unresolved,
withdrew and analyzable. Pre-randomization refusal affects recruitment and
generalizability; it is not an observed randomized failure. An observed
post-randomization choice not to complete the task can count as no adequate task
response under the treatment-policy outcome if the consent/data plan permits that
record. That is a task measurement, not a judgment about the person or a penalty.
An appropriate refusal within a substantive answer may itself satisfy the rubric.

Withdrawal that prevents retained outcome use, lost logs or unavailable follow-up
is **missing**, not silently assigned success or failure. Report arm-specific
missingness and worst-case sensitivity bounds for the realized arm-rate contrast.
If $s_z$ successes are observed
among $o_z$ of $n_z$ randomized units, the possible adequacy rate lies between
$s_z/n_z$ and $(s_z+n_z-o_z)/n_z$. Subtract the adverse arm endpoints to bound the
realized arm difference. These bound that complete-data contrast under every
binary completion of the missing outcomes. They are not identification bounds or
confidence intervals for the finite-sample causal effect $\Delta_Y$: unobserved
counterfactuals and random assignment uncertainty remain even when no records are
missing. For example, assignment may place every always-successful boundary in
one arm and every always-unsuccessful boundary in the other; the realized
contrast is one while every individual causal effect is zero. The missingness
calculation does not repair differential missingness or supply causal uncertainty.
Do not impute labor as zero for missing
records; report observed labor and what remains unmeasured.

## Exact small-design calculations: why “a few people” cannot prove much

The accompanying code generates balanced four-unit-block assignments and computes
an exact two-sided Fisher randomization test of the **sharp null that the format
changes no boundary's outcome**. For observed block success count $K_b$, the
number of treated successes has hypergeometric assignment weights

$$\Pr(S_b=s)=\frac{\binom{K_b}{s}\binom{4-K_b}{2-s}}{\binom42}.$$

Convolution gives the exact allocation distribution. With $B$ blocks the observed
mean difference is $(2S-\sum_bK_b)/(2B)$. The code sums probabilities at least as
extreme in absolute value as the observed statistic. It uses exact integer and
Fraction arithmetic, with an independent labeled-assignment enumeration test.
This test is not an exact test that **only the average effect** is zero under
arbitrary heterogeneous effects. The distinction is substantive; the primary
research literature addresses additional conditions and studentization for weak
nulls. [Wu and Ding, author preprint](https://arxiv.org/abs/1809.07419)

The mock power analysis specifies every potential outcome rather than inventing
an empirical baseline. In each block, two boundaries always respond adequately
and two do not under the template. The card improves a chosen subset of baseline
failures, with no harmed boundaries. This is an optimistic artificial family;
real interfaces may harm some users or interact with domain and team structure.
For 8, 16 and 24 units, the script enumerates all 36, 1,296 and 46,656 permissible
allocations respectively. It tests five effects from zero through .50.

| Units | Effect .125 | Effect .25 | Effect .375 | Effect .50 |
|---:|---:|---:|---:|---:|
| 8 | .000 | .000 | .000 | .000 |
| 16 | .017 | .056 | .141 | .325 |
| 24 | .027 | .100 | .286 | .729 |

Entries are exact rejection probabilities for that particular finite potential-
outcome table at two-sided $\alpha=.05$. Eight units have only 36 allocations;
a complementary two-sided extreme pair has probability at least $2/36>.05$.
That is a discrete resolution limit, not a coding failure. None of these tested
sizes reaches 80% power even at the largest tested effect in this family. The
output's coarse-grid minimum-detectable-effect field is therefore null. It is
not a recommendation to enroll 24, proof that 25 would suffice, or a general
power curve. Blocking arrangements, baseline rates, harms and clustering can
change it. Very small effect increases need not monotonically increase this
particular discrete rejection probability.

A small feasibility exercise can identify confusing language, test logging and
estimate burdens for future planning. It should not be sold as an efficacy or
noninferiority trial. Before a confirmatory comparison, select a meaningful
adequacy margin and labor tradeoff with prospective users, account for the actual
randomization unit and missingness, and plan uncertainty on the desired estimand.
Do not turn the artificial sensitivity table into measured prior knowledge.
The code gives exact sharp-null p-values and missingness bounds; it deliberately
does **not** report an unjustified exact confidence interval for average effects.

## Pre-results progression and simplicity rules

Before seeing outcomes, a future study owner should freeze the tasks, versions,
scoring rubric, observation horizon, analysis, recruitment limits and progression
criteria in a dated plan. This draft is not a preregistration. If the interface
changes during a teaching session, it is a new intervention; do not quietly pool
its later outcomes with the frozen version.

Use the initial small exercise for decisions about the next iteration:

- **Stop and repair the interface** if it systematically invites a critical
  authority upgrade, hides unresolved changes, or requires unplanned facilitator
  instruction to interpret its core record. Inspect individual failures in both
  arms; no significance threshold is needed to correct a clear design defect.
- **Simplify toward the template** if the card adds labor or concepts without a
  visible task benefit in the feasibility exercise. This is a conservative design
  choice, not a statistical declaration of equivalence or noninferiority.
- **Continue to a planned larger comparison** only if logging, recruitment,
  accessibility, treatment fidelity and total labor are feasible, and prospective
  users judge the proposed effect worth the additional study. A promising tiny
  p-value or a visually favorable average is not the progression criterion.

Any numerical burden tolerance or acceptable adequacy loss must be chosen before
outcome review and justified by stakeholders; none is inferred from toy data.
Refusal and unresolved work must stay in the presentation whichever decision is
made. The simplest successful record should remain usable without the rest of
the machinery.

## Teaching clinic is a different activity

The existing facilitator guide is an onboarding clinic: demonstrations, questions,
peer help and revised examples are welcome. Its goal is understanding and design
feedback. It does not produce blinded comparative evidence, and its attendees
must not be described as trial participants or independent endorsers. Keep clinic
notes, recruitment records and frozen evaluation datasets distinct. Do not
reuse workshop artifacts as outcome data without an appropriate separate plan.
No invitation, contact or solicitation is sent by this release packet.

## Agent-only conformance exercise: immediate and separate

Agents can start now on synthetic fixtures without enrolling humans. Fix a
runtime version, seed, policy and exact target fixture. Give the implementation
six conditions: wrong release target, unqualified checker, unchanged historical
receipt after amendment, unavailable evidence, double-booked reviewer and an
attempted downgrade of required independent groups. Record accept/reject/unresolved
behavior, exact reason, state transition and resource debits. Include at least
one valid offer/check/rely/amend/renewal sequence to distinguish rejecting
incorrect authority from rejecting everything.

Use the existing runtime and release-cycle tests for these semantics; the coupled
and ecology models test behavioral consequences under their own assumptions.
A model that prints a scoped receipt is not automatically a runtime-conformant
agent. An adapter needs explicit field mapping and adversarial tests. Compare
implementations on identical fixtures and report uncovered cases. An agent test
pass establishes only the tested behavior under the supplied authority and
identity inputs. It does not count as a human adequacy outcome, independent peer
review, or permission to process real protected material.

## Files and verification

```sh
python3 -m unittest discover -s papers/07-release-packet/models/human_pilot -p 'test_*.py' -v
python3 papers/07-release-packet/models/human_pilot/run_design.py
```

Python 3.9+ standard library only. Eight tests verify allocation balance,
independent enumeration, sharp-null size on selected finite tables, complementary
assignments, potential-effect arithmetic, missingness bounds, their distinction
from causal effects, and invalid inputs.
The results directory contains a labeled artificial allocation, 15 exact power
rows, source/table hashes and a mock statistic. No names, contact details, human
responses or purported ethics approvals are generated.
