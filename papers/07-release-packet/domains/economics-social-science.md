# Economics and social science: the denominator is part of the claim

**Research question.** Can a portable reliance record preserve the distinction
between a registered analysis, an identified sample effect, a transported policy
claim, and the population of reviews that actually finishes?

**Bounded answer.** A declared record can keep these objects separate. Two elementary
models show why the separation matters; they do not show that a real institution
will honor it. The study, people, outcomes, and effort prices here are synthetic.

## The situation

The invented Harbor team evaluates an informational intervention in two types of
site. Its versioned plan specifies an average effect for the trial sample. The
team obtains a positive estimate and shares code that reproduces its table. A
municipal analyst wants to use that estimate for a different mix of sites. A
funder also wants an apparently neutral review queue to prioritize its own studies.

These are distinct questions. Registration can document what was planned;
reproduction can document what code calculates; identification concerns how the
design supports the estimand; transport concerns a new setting. The review queue
itself has a selection problem if some reviewers disproportionately decline or
finish particular work.

The AEA RCT Registry's official guidelines distinguish registration review from
research-quality or ethics review and support versioned study entries. Its stated
eligibility is social-science RCTs, not clinical trials. Use the registry as a
source identifier and chronology, not as a quality badge. [Guidelines, checked
2026-09-25](https://docs.socialscienceregistry.org/registration_guidelines).

Deaton and Cartwright's primary paper emphasizes that moving trial findings to
other groups requires justification. That motivates our explicit transport
assumptions; our numerical example is independently constructed. [Primary paper
record, search-retrieved abstract checked 2026-09-25](https://www.nber.org/papers/w22595).

## Model 1: a sample effect is not automatically a target effect

Let $S\in\{A,B\}$ label site type and let $\tau_s$ be its average treatment
effect. Under random assignment within the toy trial, an appropriate estimator
can estimate the sample mixture

$$\tau_{\mathrm{trial}}=w_A\tau_A+w_B\tau_B.$$

Suppose $\tau_A=2$, $\tau_B=0$, and trial weights are $(0.8,0.2)$. The trial
effect is $1.6$. A target population with weights $(0.2,0.8)$ has effect $0.4$
*if* the within-type effects transfer unchanged and both target types have trial
support. The fourfold difference comes entirely from composition. It is not a
bias correction that MCRP can infer from a citation.

The elementary transport formula

$$\tau_{\mathrm{target}}=\sum_s v_s\tau_s$$

requires target weights, adequate support, stable definitions of treatment and
outcome, and justified within-type transport. Interference, unmeasured effect
modifiers, endogenous participation, implementation changes and general-equilibrium
effects can break that model. A missing type C cannot be repaired by renormalizing
only A and B without changing the target estimand. Report unsupported transport
as unknown or partial, not as zero effect for C.

The fixture uses stipulated exact effects, so no confidence interval is claimed.
A real analysis would propagate sampling uncertainty and weight uncertainty, and
separate confirmatory and exploratory analyses.

## Model 2: completed reviews are a selected population

Let an invitation target an adversarial control group with probability $q$, with
completion probabilities $c_a$ for adversarial and $c_h$ for other invitees. Then

$$P(a\mid\mathrm{complete})=
\frac{q c_a}{q c_a+(1-q)c_h}.$$

At $q=0.1$, $c_a=1$, $c_h=0.01$, the completed share is $100/109\approx0.91743$.
An invitation-level “10% maximum” would badly misdescribe completed reviews. This
is a conditional-probability identity, not an estimated attack rate.

The repair is not simply to reroll until someone completes. Rerolls spend time,
can amplify selection, and may exhaust the only independent experts. Record
offered, eligible, invited, accepted, completed and relied-upon denominators, plus
refusals and retries. A fair invitation distribution and a fair completion
distribution are different design objectives. Neither establishes correct reviews.

Reliance can select once more, independently of allocation. Suppose 10 adverse and
90 other reviews have completed: the adverse completion share is 0.1. If an editor
relies only on the adverse 10, the adverse share among relied-upon reviews is 1.
That is a separate finite-count fixture, not a continuation of the earlier 100/109
example. Recording every stage exposes the selection; it does not constrain the
editor’s legitimate discretion or prove decision quality. Any promised influence
bound must specify whether it concerns invitations, completions, or actual reliance.
Representation, expertise and decision quality are different objectives.

## Four receipts, without upgrading the estimand

| Action | Concrete record |
|---|---|
| Offer `econ-offer-v1` | Harbor offers target `econ-trial-ate@1`, synthetic strata table, code and plan version; scopes `arithmetic` and `estimand_alignment`. Target population and transport are excluded. Requested check budget: 2 effort tokens. |
| Check `econ-check-v1` | An external analyst verifies $0.8(2)+0.2(0)=1.6$ and confirms that the *synthetic* plan's named estimand is the trial mixture; records inaccessible/nonexistent real assignment records and no empirical causal validation. |
| Rely `econ-rely-v1` | A named scientific decision maker accepts 1.6 as the worked model's trial-mixture calculation, not as an actual intervention estimate or citywide recommendation. Scope stays bounded; expiry is logical time 20. |
| Amend `econ-amend-v2` | The municipal analyst supplies target weights $(0.2,0.8)$ and requests a separate target claim. Version 2 computes 0.4 under stated transport assumptions. It links the original stratum estimates but does not overwrite the trial estimand. |

In a real application, a substantive identification check would need more than
matching a plan and script. Timestamped plans can still be underspecified or
amended; protocol records should show both chronology and deviations. An exploratory
analysis may be valuable if labeled as such. The framework should not incentivize
retroactive relabeling as preregistered.

## Scarcity, sponsorship and individual versus team participation

Suppose 20 studies compete for 40 effort tokens. A sponsor submits 15 studies,
each requesting 2 tokens; unsponsored authors submit 5. Uniform allocation per
study gives 75% of attention to the sponsor even if the verdict function never
reads a payment field. This does not prove wrongdoing, but it shows why “no paid
verdict” is incomplete as an attention-fairness claim.

Track sponsor/control-group shares separately from judgments. Compare uniform
qualified assignment, disclosed principal-level caps, and a newcomer opportunity
reserve under matched expertise and total capacity. Caps can themselves deny
useful work; publish exclusions and delays. An allegedly additive sponsored pool
is not additive if it draws the same scarce reviewers away from the common pool.

A solo researcher can contribute a 1-token estimand check. A large team can
prepare a replication bundle and conduct internal checks, but its agents do not
become many independent outside reviewers. An economist may model different
within-team production functions while retaining one external accountable
principal. The protocol needs the boundary, not a theory of every team's internals.

## Failure and repaired workflow

The failure path labels a registered, reproducible estimate “policy-ready,” reports
only completed favorable reviews, and cites an invitation cap as protection from
capture. The repaired path retains the original estimand, offers transport as a
new scoped claim, records unsupported population cells, and reports completion
selection separately from allocation. A declined or incomplete check is visible
work, not erased from the denominator.

An amendment can change an analysis plan, an estimate, or an intended use. These
are different events. A changed city population does not necessarily invalidate
the old trial calculation; it can invalidate its relevance to the city. Exact
receipt identity permits both statements to coexist without a global trust score.

## Human exercise and answer key

**Ten-minute entry:** Ask participants to compute the two weighted averages and
write the population attached to each. Then give them the completion probabilities
and ask whether a 10% invitation share ensures a 10% completed-review share.

**Answer key:** Trial mixture 1.6; target mixture 0.4 conditional on transport;
completed adverse share about 91.74%. In the separate final-selection example,
a 10% completed share becomes a 100% relied-upon share. An unrepresented target
type remains unknown.
A perfectly performed arithmetic check does not establish causal identification.

**Forty-five-minute clinic:** Participants play author, checker, municipal analyst,
and resource steward. The author presents a plan deviation; the analyst changes
the target population; the steward introduces asymmetric refusal. Each role must
preserve the useful narrow result and state which new work is needed. Count the
steward's administrative labor, not just the reviewing economists' labor.

## Agent task and falsifiable evaluation

The domain oracle computes the two mixture effects and conditional completion
share with exact rational arithmetic. The implementer should maintain distinct
targets for the trial calculation and transport calculation, with transport
assumptions as explicit dependencies. A new target mix must not silently mutate
the old result. The toy receipt engine checks scopes and declared dependencies;
it does not estimate treatment effects or validate randomization.

Proposed evaluation crosses three interfaces (letter, structured template,
receipts) with hidden versus explicit population changes. A separate routing
experiment varies completion probabilities, sponsor submission share, and
principal labeling. Outcomes include estimand errors, unsupported transport,
completion concentration, denied work, and total labor. Arithmetic accuracy alone
is an inadequate endpoint. No study has been preregistered or run by this packet.

## Claim ledger and closest-work boundary

| Claim | Type | Support or remaining test |
|---|---|---|
| Registry presence is not research-quality approval | P | AEA's own registration guidelines |
| Trial-to-target transfer requires justification | P | Deaton–Cartwright primary paper abstract |
| Mixture changes yield 1.6 versus 0.4 in this model | T/I | Explicit effects and exact fixture |
| Completion can reverse an invitation-level impression | T/I | Conditional-probability identity and fixture |
| Typed receipts improve policy interpretation and incentives | H | Future comparative study; no behavioral evidence |

The addition to existing registry, replication and evidence-synthesis practice is
a proposed portable boundary around a particular use. It is not a new causal
identification theorem, public procurement rule, or mechanism-design equilibrium.
