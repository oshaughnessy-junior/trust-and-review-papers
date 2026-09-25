# MCRP hardening: make reliance precise, participation small, and repair affordable

**Integrated research position, 25 September 2026. Private working draft.**
Prepared through specialist AI drafting and adversarial review. Human authorship,
scientific review, legal applicability, and release approval are not established.

## The proposition

A useful research commons should let a reader answer a small question: **What may
I rely on here, for which use, and what would make me reconsider?** MCRP already
offers part of the answer by binding claims, evidence, checks, and decisions to an
exact release. Its next step should make those records cheap to contribute,
portable between communities, and explicit about the labor needed to keep them
current.

Our recommended participant interface is **offer → check → rely → amend**. These
are actions, not four exclusive stages. A person can challenge before review,
several checks can run concurrently, and different institutions can make different
reliance decisions about the same evidence. A solo author, large collaboration,
single agent, and agent team can expose the same boundary record. Internal
complexity remains their choice; it does not manufacture independent external
authority.

The small interface is the central design proposal. A universal reputation score,
a compulsory market in review, and sophisticated graph routing are not prerequisites.
Start with qualified, conflict-aware random assignment, workload limits, and
reserved newcomer opportunity where feasible independent supervision exists. Charge onboarding and supervision to the same resource ledger; a reserve cannot guarantee completed service when the required expertise is absent. Make additional routing machinery earn its cost against
that baseline. The protocol should still be useful if its entire reputation layer
is removed.

## What the specialists changed

The economist treats attention as a scarce input rather than free labor attached
to publication. The game theorist asks who pays for detecting nonperformance and
why any promised audit is credible. The lawyer separates scientific disagreement,
participation decisions, content visibility, and lawful handling of rights. The
scientist treats review as a composition of fallible checks and follows the
correction workload through dependent claims. Their constraints reinforce one
another, but they do not collapse into a single trust score.

### 1. Funding independence is broader than verdict independence

The Commons prototype's separation of payment from qualification and verdict is
a necessary design boundary. It is insufficient. If sponsors can generate many
more submissions into a neutral queue, they can consume most attention without
ever purchasing a favorable verdict. Sponsors can also become indispensable to
the operator's survival.

Keep disposition independent of payment under frozen evidence, eligibility and
policy. Separately measure queue share, shared reviewer capacity, principal-level
concentration, and funding dependence. A sponsored pool is additive only to the
extent that it adds capacity instead of drawing the same experts away from the
common pool. There is no purely cryptographic repair for a service that cannot
afford to offend its only funder.

The economics model derives an optimal continuous effort allocation under known
defect risk and productivity. Those inputs are hypothetical, not quantities
learned from a trust graph. Numerical stress tests deliberately perturb them. With
large estimation noise, the apparent optimum can lose to uniform allocation.
This supports a conservative allocation baseline and explicit exploration, not
the deployment of an omniscient optimizer.

### 2. Bound final allocation, not just intermediate graph scores

For personalized restart routing, the imported-mass bound

$$p(X)\le\frac{\alpha\epsilon}{1-\alpha+\alpha\epsilon}$$

holds only when every post-filter honest row sends at most $\epsilon$ transition
probability to the external region and restart mass is local. A tiny raw edge can
normalize to probability one. Independently checking each candidate's max-flow
can reuse the same frontier budget many times. A score-to-assignment softmax can
give nearly all attention to many low-score accounts even when their total graph
mass is tiny.

The resulting requirement is end-to-end: construct feasible complete panels,
apply disclosed control-group and frontier constraints jointly, reserve shared
capacity atomically, and inspect the resulting assignment distribution. Choose over canonical accountable-group panels before representatives: one-seat-per-group constraints alone do not prevent duplicate labels from biasing selection. State whether a bound applies to offered or completed panels; refusals, selective completion and retries can destroy a proposal-level probability bound. If the
required independent expertise does not exist, return **coverage unavailable**.
Do not silently relax the contract. Common-control information itself remains
uncertain; this is a constrained scheduling design, not a solved identity problem.

The reference tooling has a different, simpler algorithm: maximum decayed path
product. It must not inherit PageRank theorems merely because it emits trust-related
numbers. Its hardening work concerns its actual input and traversal semantics.

### 3. Simplicity can generate both cooperation and capture

The scientist's feedback model has a symmetric allocation whose local eigenvalue
is $(1-\zeta)\beta\chi/K-1$. When opportunity strongly reinforces future opportunity,
small differences can grow into concentration. Exploration helps, but reducing
the use of attention as a proxy for competence attacks the feedback itself.
This is a conditional mathematical model, not a measured behavioral law or a
globally calibrated threshold for a platform.

The game model gives a similarly conditional effort constraint:

$$g\le(\beta_d-\alpha_f)[F+\delta(V-W)],$$

where $g$ is a deviation gain, $\beta_d-\alpha_f$ the monitoring discrimination,
$F$ a modeled enforceable loss, and $V-W$ the continuation-value difference.
Low discrimination, low future value, cheap resets, or coordinated deviations can
destroy the condition. A reputation promise cannot fund or implement its own
auditing. Common-mode failures also make more reviewers a poor substitute for
different evidence and genuinely distinct controls.

The design should make bounded useful checks and honest corrections recognizable.
Whether that recruits prestige incentives better than it recruits performative
criticism is an empirical question. Trust and dominance are useful hypotheses,
not an exhaustive theory of scientists' motivations.

### 4. The limiting resource may be correction, not publication

Adding more dependency links can make repair more precise and more expensive.
A homogeneous branching model has expected work $1/(1-R)$ for $R<1$. A multitype
model instead uses $t=z_0(I-M)^{-1}$ when the relevant spectral radius is below one.
The latter exposes a hidden failure: an average offspring rate of $.71$ can mask
a specialty with growth factor above $1.2$.

Even stable propagation may demand more calibration or legal expertise than exists.
One fixture requires about 7.62 hours/day in total against 8 available, yet requires
5.08 hours/day of a specialty with only 4 available. Review, repair, appeals and
intake may compete for the same people; their capacity promises cannot each spend
the same hour. Track commitments across these uses, with protected obligations
and explicit priorities. An untested stationary branching approximation is not
an admission controller for changing, adversarial workflows.

Deduplicating notices is not equivalent to discharging scientific obligations.
Track distinct affected claim versions and reusable checks. Expose pending reliance
when repair is delayed. A quiet dashboard must not conceal a stale scientific use. Current reliance views must show observation time, unresolved material changes relative to that receipt, evidence availability, and expiry; an authentic cached receipt may still have unknown currentness. Renewed authorized reliance can resolve a previous amendment without erasing its history.

### 5. Bounded disputes need real exceptions and real capacity

Preserve TDRG's scientific-content, private-standing, and conduct/opening appeal
lanes. Add a separate operator compliance track; it does not become a scientific
court. The same concern may require several linked decisions with different
authority. Hiding exposed personal information does not make the science false.
Keeping a historical disposition does not mean its evidence remains accessible.

An ordinary case can have a bounded initial review and independent appeal, an
explicit unresolved-at-resource-boundary outcome, and reopening for material new
evidence. Count triage of refused and duplicate requests: an attacker does not
need to win admission to consume labor. A named alternate must handle founder
conflicts; another agent controlled by the founder is not independent governance.
A named alternate also needs protected access, appointment/removal safeguards, and a defined way to execute reversal. Rights-handling needs deadline-aware obligations and recipient-specific disclosure, not scalar backlog alone. When capacity fails, pause new publication and discretionary promises while preserving appropriate reporting and timestamps for existing obligations. Protected rights intake cannot be sold or exhausted by a graph-navigation quota,
and ordinary budgets cannot cancel applicable legal duties.

Content-addressed identity means that changed bytes get a different identity. It
does not require perpetual public availability. Keep public content, minimal
decision notices, and restricted incident evidence separable. Do not label a
stable public pseudonym unlinkable across cases. The Commons documentation and
the more ambitious TDRG privacy profile describe different maturity levels.

## The operating envelope

The program cannot reduce sound operation to one inequality. Under the models'
premises, several conditions must be considered together:

| Constraint | What must be checked | What it does not establish |
|---|---|---|
| Scope and authority | Exact target, performed checks, qualified decision maker | Scientific truth |
| Expertise coverage | Feasible independent panel or openly reduced contract | Real common control is fully known |
| Attention | Review + repair + audit + intake + appeals fit available skill-hours | Bounded tail latency |
| Incentives | Effort, participation, audit funding and coalition constraints | Universal equilibrium selection |
| Influence | Actual final joint allocation respects intended limits | Correct reviews |
| Repair | Reachable changes, type-specific workload, current observations | Discovery of undeclared dependencies |
| Legal/rights | Applicable duties and removal/appeal paths are supported | Legal clearance from this paper |

Failure of a condition produces a narrower service, an unresolved state, or a
recorded need for human judgment. It must not produce a fabricated green status.

## Adoption without replacing established science

The first participant brings an ordinary versioned paper and referee letter.
The wrapper asks which claim, which check, which evidence, and which limits.
Existing editor, institution, and collaboration decisions retain their scope.
Machine-readable adapters can preserve identifiers and corrections using existing
provenance and notification formats; no external interoperability is claimed yet.

A single researcher can contribute a short numerical check. A collaboration can
expose a witnessed execution and a downselect with inaccessible assumptions clearly
marked. An agent team can prepare and verify records within an accountable human
boundary. The current profile retains qualified-human scientific disposition;
supporting organizational enrollment would require a separate compatible profile.

This is backward compatibility through honest wrappers, not automatic conversion
of old prose into consent, signatures, or retrospective approval. Large mandatory
forms would defeat the adoption premise. Material conditions still have to be
visible at the point where someone decides to rely.

## What to build and test next

First build the smallest complete synthetic release cycle: offer an exact claim,
attach a check, record a separately authorized reliance, deliver a frozen artifact,
observe it, and propagate a material amendment to affected uses. Exercise failure
and recovery, not only the happy path. The current numerical models and tooling
tests are ingredients, not evidence that this cycle is deployed.

Then compare three interfaces on the same tasks and labor budgets: conventional
review, a simple structured template, and the four-action interface. Measure
material defects found, incorrect authority upgrades, uncovered scope, total human
labor including stewards, correction-cone accuracy, subgroup waiting time, and
specialist overload. Separate routing as a later experimental factor. Report
refused work and unresolved cases. Report the full offered, eligible, invited, accepted, completed and relied-upon denominators, including refusals, exclusions, retries, unresolved work and their costs; reducing backlog by excluding participants is
a tradeoff, not a free efficiency gain.

Before a confirmatory human pilot, establish recruitment, consent/ethics,
jurisdiction, access rules, and effect-size-based stopping criteria. Do not call
this research package a preregistered study after observing its exploratory
simulations. The decisive test is whether the simple structured template does as
well at lower cost. If it does, keep the portable record and drop the extra machinery.

## Evidence posture

The contribution is a disciplined synthesis, elementary conditional derivations,
counterexamples, executable synthetic models, and bounded prototype hardening.
It is not a demonstrated new institution. None of the agent reviewers is external
to this orchestration or its operator. The dedicated adversarial reports and
collective red-team assessment preserve objections separately from the authors'
responses. Unresolved objections remain part of the deliverable.

The specialist manuscripts contain primary-source references, derivations,
claim ledgers, and limitations. The source lineage and run manifests distinguish
existing designs, new proposals, theoretical results, and implementation evidence.
No public website, hosted Commons deployment, authorship, license, or scientific
approval is changed by this draft.
