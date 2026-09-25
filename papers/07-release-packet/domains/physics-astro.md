# Physics and astronomy: one calibration, many apparently independent checks

**Research question.** Can a small, version-bound record keep numerical agreement
from being mistaken for independent evidence when analyses share a measurement
pipeline?

**Bounded answer.** It can expose the distinction when the dependency is declared;
it cannot discover all hidden dependencies or establish the calibration's adequacy.
This is a synthetic teaching example, not an analysis of gravitational-wave data.

## The situation

The invented Meridian collaboration releases a dimensionless amplitude estimate
from a synthetic transient. Two external groups independently run its public
analysis script and obtain the same estimate, 10.5. A catalog compiler would like
to call the result “confirmed by three groups.” All three groups used the same
calibration file. Repeating the calculation has checked execution, not supplied
three independent calibrations.

Calibration is a substantive measurement issue, not merely a file-integrity
problem. Cahillane et al. describe calibration uncertainty for LIGO's first two
observing runs and its relevance to astrophysical inference. That established
motivation informs this example; none of the numbers below are taken from their
study. [Primary paper, abstract and version record checked 2026-09-25](https://arxiv.org/abs/1708.03023v3).

The first participant need not join a new institution. A graduate student can
check one arithmetic step. A collaboration can expose a public downselect plus a
bounded, witnessed analysis of restricted inputs. Both need to say which evidence
was actually available. The collaboration's hundred internal agents are useful
workers but remain within its single declared control boundary.

## A model with an irreducible shared error

For this toy model let repeated estimates be

$$Y_i=\theta+C+\epsilon_i,\qquad
E[C]=E[\epsilon_i]=0,\quad
\operatorname{Var}(C)=\tau^2,\quad
\operatorname{Var}(\epsilon_i)=\sigma^2.$$

Assume the individual errors are mutually independent and independent of the
shared calibration error. Then

$$\operatorname{Var}(\bar Y)=\tau^2+\frac{\sigma^2}{n}.$$

The derivation follows by expanding the variance: the same random variable $C$
appears once in the average, while independent errors contribute
$n\sigma^2/n^2$. A mistaken independent-error model gives
$(\tau^2+\sigma^2)/n$. With $n=16$, $\tau=0.5$, $\sigma=0.2$, the actual modeled
standard error is $\sqrt{0.2525}\approx0.50249$; the mistaken one is
$\sqrt{0.018125}\approx0.13463$. More reruns cannot beat the $0.5$ shared-error
floor. These are uncertainty calculations under specified random-error assumptions,
not a claim that an actual calibration bias is random or Gaussian.

A second, deterministic model makes the amendment concrete. Let raw amplitude
$x=10.5$ and response gain $g_1=1.00$. The released estimate is $x/g_1=10.5$.
Replacing the gain with $g_2=1.05$ yields $10.0$. Every exact claim downstream of
the old gain needs its *use* reconsidered. The original receipt that the old script
returned 10.5 remains historically correct. A later change does not falsify the
statement “this old script produced this old number.”

Neither simple model captures frequency-dependent complex response, waveform
systematics, inference priors, or selection functions. Its purpose is to show a
dependency boundary that a general-purpose “reviewed” badge conceals.

## Four receipts, with an honest narrow result

The identifiers below are fixture labels. The machine fixture computes a real
SHA-256 digest of its synthetic evidence object; that is content identity only,
not authentication or evidence of physical measurement.

| Action | Concrete record |
|---|---|
| Offer `astro-offer-v1` | Meridian offers target `astro-amplitude@1`, evidence digest from the fixture, scope `numerical_reconstruction`, accessible raw scalar and script; excludes physical calibration validation. Declares dependency `astro-calibration@1`. Requests one reconstruction check costing 1 effort token. |
| Check `astro-check-v1` | External group North records `10.5/1.0=10.5`; result `support` for reconstruction only; limits: shared calibration, no independent measurement, no waveform check. One group identity, regardless of internal team size. |
| Rely `astro-rely-v1` | Named catalog editor permits use as a *reconstructed synthetic example* under policy `teaching-v1`, scope `numerical_reconstruction`, until logical time 20; no physical-detection or population-inference authority is supplied. Publication authorization, if needed, is a separate record. |
| Amend `astro-amend-v2` | Calibration steward identifies gain revision 1.00→1.05, links the earlier exact calibration target and dependent amplitude target, requests reconsideration. Current use becomes pending; a new reconstruction and authorized reliance can support the amended version. |

An external calibration expert could later perform a physically meaningful check
under a different offer. The existing reconstruction record must not silently grow
to cover that work. An “unknown” or inaccessible calibration check is a useful
result, especially when it prevents a downstream user from assuming coverage.

## Failure and repair

The failure workflow asks three teams to rerun the same code, counts their account
names, and reports “three independent confirmations.” It ignores common control,
shared evidence, and common measurement assumptions. It then overwrites the
calibration URL, leaving no clear statement of which result used which version.

The repaired workflow separates three questions: did the script execute; was the
measurement response checked; and who accepts the resulting uncertainty for a
particular use? It keeps a dependency from the amplitude claim to the exact gain
artifact. After amendment, a currentness query marks that use pending. A new target
version plus a new check can restore a narrow use. An offline cached copy retains
its historical content but has unknown freshness once its declared refresh age is
exceeded.

The negative control deliberately omits the calibration dependency. The receipt
engine cannot infer it from prose or the shape of a graph. In the planted ground
truth, two claims depend on calibration and one unrelated figure does not. With
one dependency hidden, the declared graph reaches only one of the two affected
claims: correction recall is $1/2$, despite perfect traversal of declared edges.
Reporting both recall and precision distinguishes incomplete provenance from a
broken traversal implementation.

## Attention and collective scale

Suppose the teaching clinic has 8 effort tokens: reconstruction costs 1,
calibration review 4, independent interpretation 2, and coordination 1. A complete
planned bundle costs all 8; it leaves no reserved amendment capacity. The organizer
must either reserve repair capacity by admitting less work, acquire additional
qualified capacity, or disclose that repairs may wait. Adding 100 internal agents
does not increase the external calibration specialist's 4-token capacity.

These tokens are declared scheduling units, not empirical hours. If one person
performs coordination and calibration, both tasks debit that person's shared
ledger. A single person appearing under two roles cannot be booked twice at full
capacity. A lone author can instead offer only the 1-token reconstruction and
honestly leave calibration uncovered.

## Human clinic and answer key

**Ten-minute entry:** Participants see a short “three teams agree” paragraph and
the scalar table. Ask them to write one sentence beginning “I checked…” and one
beginning “This does not show…”. Introduce the gain amendment after those answers.

**Answer key:** 10.5 is a reproducible old calculation; the revised calculation is
10.0; numerical replication alone does not establish physical calibration; the
unrelated figure needs no automatic scientific rejection. Correctness means
preserving the narrow old statement while changing the current permissible use.

**Forty-five-minute clinic:** An author, checker, catalog editor and calibration
steward take the four roles. First do the exercise with an ordinary letter, then a
plain structured template, then the proposed receipt interface. Counterbalance
order across future participants; do not treat within-session learning as a
protocol effect. The facilitator records time, assistance, unperformed tasks,
incorrect authority upgrades, and which dependent claims were reconsidered.

## Direct implementation task and falsifiable benchmark

Run `fixtures/domain_models.py`, inspect `physics`, and verify both variance
expressions and the exact rational amplitude revision. Then replay the target,
dependency, check and amendment through the toy engine. Compare these variants:

1. full declared graph, unchanged team size;
2. same graph with internal team size 1→100 (no new external authority);
3. a hidden calibration dependency (known recall loss);
4. an unrelated claim (negative control against overbroad amendment);
5. expired or stale reliance (no fabricated current result).

The mechanical benchmark fails if a declared affected use remains current after
the amendment, an unrelated target is automatically declared scientifically
false, or redundant internal labels manufacture independent reviewers. The human
hypothesis fails if receipts do not improve scope discrimination over the plain
template at matched total labor. No human effect size has been measured.

## Claim ledger and boundary

| Claim | Type | Support or remaining test |
|---|---|---|
| Calibration matters for GW inference | P | Cahillane et al.; only source abstract/version inspected here |
| Shared error leaves a variance floor | T | Stated independent-error model and `physics_model` oracle |
| Gain amendment changes 10.5 to 10.0 | T/I | Exact arithmetic fixture and regression |
| Explicit dependencies permit targeted reconsideration | D/I | Proposed records; toy traversal tests in framework |
| These records improve real collaborative science | H | Unrun human comparison and future field work |

All synthetic outputs are reproducible without downloads. This case is a teaching
adapter, not a claim of LIGO, Virgo, KAGRA, or journal compatibility, endorsement,
or successful interoperability. A real deployment still needs authenticated
responsibility, qualified judgment, access controls, and measured repair capacity.
