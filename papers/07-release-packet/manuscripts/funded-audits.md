# From promised inspection to delivered inspection: a closed-loop funded-audit toy

**Research prototype, 25 September 2026.** Synthetic actors, fixed identities,
artificial utility and token units, and a declared person-hour ledger. No real
assets, sanctions or audit authority are created. This experiment closes one
specific modeling gap: the earlier coupled simulator gave actors a perceived
audit probability without executing or funding those audits. Here an audit plan
reserves resources, draws its fixed quota, accepts committed actor decisions,
executes inspections and records detection and collateral transfers.

## What is fixed before behavior

The fixture has eight planned task decision units, called actors in the output.
They are not eight independently controlled human reviewers: the resource mapping
can assign several such decisions to one execution person. Utilities are separable
across these fixed units, with task-specific escrow and a pre-reserved program; no
portfolio, identity or organizational independence theorem follows.
Each can honestly perform a bounded task,
submit a shallow completion assertion, or refuse. The identities, role mapping,
qualification and possible actions are fixed. There is no entry, identity reset,
coalition formation, learned qualification or population equilibrium.

The organizer proposes a quota $k$ among $N=8$ offers. Before issuing invitations,
it verifies audit-token funding, reward-token funding, enough stipulated actor
collateral, distinct declared reviewer/auditor controls and a whole-program hour
reservation. If any conforming preflight fails, the result is **unavailable before
offering**: planned population remains eight, offered count is zero, and no audit
promise is made. It does not keep drawing random subsets until one fits capacity.

If preflight passes, the program uniformly selects exactly $k$ offered indices
using the existing hard-quota sampler from `models/math/protocol_math.py`.
The chosen set is hidden from actors in the main condition. **All actors commit
their actions before any completion or audit result appears in the event trace.**
An actor who refuses leaves a selected slot unused. The organizer does not replace
that actor with another candidate or change the denominator silently.

The Python output eventually reveals the selected slots so the experiment is
inspectable. That output is an evaluator trace, not the actor's information set
when making its decision. The code is not a cryptographic concealment mechanism.

## Three resource accounts, not one ambiguous cost

**Audit funding:** inspections cost one artificial token each. The main budget
holds four tokens for at most four inspections. **Reward funding:** each completed
task receives $.6$ reward tokens, backed by a separate $4.8$-token reserve for all
eight possible completions. Unused funding remains unspent. Penalties are never
recycled to justify an audit or reward promise.

**Actor collateral:** every offered actor is stipulated to have two loss tokens
already available in escrow. A sanction removes two tokens from that balance into
a separate quarantine account. The trace records opening/closing escrow, actual
sanctions and rewards. This makes the toy loss collectible within the fixture;
it does not show that real participants have wealth, consent to deposits or face
legitimate sanctions. The utility model assigns unit marginal utility to reward and loss tokens and
ignores the opportunity cost of locking collateral and nonlinear wealth effects.
Those are significant omitted participation costs, not solved implementation work.

**Human hours:** a review consumes one booked hour, and an executed audit consumes
half an hour. This ledger is separate from tokens and utility effort. Honest and
shallow submissions both occupy one review slot; the model does not infer a
productivity gain from lower private effort cost. Refusals consume no review or
audit hours here. Real refusal/triage labor is omitted and would require a positive
resource debit; the coupled queue model separately accounts for refusal costs.

In dedicated roles, one reviewer reserves eight hours and another auditor reserves
two. In the shared-role condition, P0 reviews four actors and audits P1's work;
P1 reviews the other four and audits P0's work. No person audits their own check.
Each reserves

$$H_p=4h_R+\min(k,4)h_A.$$

At $h_R=1,h_A=.5,k=4$, this is six hours per person. This conservative reservation
covers every possible quota subset, including all four audited works being
assigned to the same opposite reviewer. The program reserves twelve hours even
though all eight reviews plus four audits use only ten; the extra slack protects
the unconditioned lottery. It is real opportunity cost and is reported as reserved
versus used time. With only five hours each, the program returns unavailable. Some
specific draws would fit five hours, but conditioning on those draws would change
the assignment mechanism and requires a different analysis.

Different person labels are stipulated different controls in this toy world.
They are not evidence of independent real reviewers or protection against
collusion. A self-audit configuration is rejected before offers whenever $k>0$.

## Conditional finite best response

Risk-neutral private utilities are

$$U_H=R-c-q\alpha F,\quad U_S=R-q\beta F,\quad U_R=u.$$

Here $R=.6$, effort disutility $c=.3$, outside utility $u=.1$, enforceable toy loss
$F=2$, false-sanction chance $\alpha=.02$ and shallow-work detection chance
$\beta=.8$. An audit occurs with the actor's information-conditional probability
$q$ if the actor participates. Ties favor refusal, then honest work, then shallow
work. The predicted action is just the maximum of these three numbers.

**Finite proposition.** Given the stipulated one-shot risk-neutral preferences,
credible delivered audit probability and collateral-backed loss, honest work is a
weak best response precisely when

$$c\le q(\beta-\alpha)F,\qquad R-c-q\alpha F\ge u.$$

*Proof.* Subtract $U_S$ and $U_R$ respectively from $U_H$. These inequalities are
necessary and sufficient among the three fixed actions. They neither predict
strict participation at ties nor rule out an unmodeled deviation. $\square$

The implementation makes actual completion, audit, false-positive/detection draws,
reward payments and loss transfers. Realized utility varies with the detection
draw; the best-response calculation concerns expected utility at commitment.
No actor learns and adapts within the same round. It is not a repeated-game result
or an equilibrium of a review institution.

## What the quota really guarantees

**Selection proposition.** A uniform $k$-subset of a fixed $N$-actor population
includes any actor with probability

$$q=\binom{N-1}{k-1}/\binom Nk=k/N,$$

for $1\le k\le N$; $k=0$ gives inclusion probability zero directly. It uses at most $k$ audit slots on every run. If each executed audit costs exactly
$a$ tokens, actual audit cost is at most $ka$, whether or not selected actors refuse.
The whole-program hour reservation bounds actual person-hour use pathwise.

For a fixed actor who participates without learning selection, suppose its action
and private decision shocks are independent of the concealed subset. Then

$$\Pr(\mathrm{audited}\mid\mathrm{participates})=k/N.$$

This statement is conditional on that information structure and independence.
Refusals leave unused slots and do not invalidate a participating actor's marginal.
The **realized** audited fraction among completers need not equal $k/N$ in each
run. If all participants refuse, that fraction is undefined, not zero evidence
about the intended marginal. Nor is executed-audits divided by all offers a claim
that refused actors were audited.

The exact test enumerates all $\binom84=70$ quota subsets. Each actor appears in
35. If a fixed four actors participate and the other four refuse, the expected
number of executed audits is two; realized audits can range from zero to four.
A separate test verifies that refused selected slots remain unused in the actual
event trace. No claim of a conditional marginal survives arbitrary entry,
selection-dependent refusal, leaked quota information or adaptive replacement.

## Failure cases are the experiment

Eleven conditions run over twenty displayed seeds each (220 small runs). Detection
counts are descriptive seeded outcomes; the structural results below follow from
the disclosed utilities, exact quota and resource accounting.

| Condition | Advertised / delivered quota | Actions in each fixed-utility run | Interpretation |
|---|---:|---|---|
| No audit | 0 / 0 | 8 shallow | Unmonitored private effort has no advantage here |
| Concealed, funded | 4 / 4 | 8 honest | Delivered conditional probability matches the decision premise |
| Partial refusal | 4 / 4 | 4 honest, 4 refuse | Selected refused slots stay unused; no quiet reassignment |
| Broken promise | 4 / 1 | 8 honest under advertised belief | Actual expected incentives differ from the belief used to choose |
| Corrected probability | 1 / 1 | 8 shallow | Accurate low capacity does not magically preserve effort |
| Selection disclosed early | 4 / 4 | 4 honest, 4 shallow | Unaudited actors know their actual probability is zero |
| False sanctions rise to .3 | 4 / 4 | 8 refuse | Strong inspection can eliminate participation |
| Shared cross-audit roles | 4 / 4 | 8 honest | Both roles debit the same two people without self-audits |
| Shared capacity too small | no offer | unavailable | Does not condition the quota draw on available capacity |
| Self-audit only | no offer | unavailable | Another task by the same person is not independent audit capacity |
| Collateral insufficient | no offer | unavailable | The model does not invent enforceable loss |

In the broken-promise negative control, the organizer deliberately violates the
conforming rule with a visibly named configuration flag. It advertises $q=.5$
while delivering only $q=.125$. At the advertised probability honest utility is
$.28$ and shallow utility is $-.2$, so actors choose honestly. Under actual delivery,
honest expected utility is $.295$ while shallow is $.4$. The expected utility
shortfall relative to the correct best response is $.105$ per actor, $.84$ across
the population. That is not a welfare judgment about honesty; it measures the
modeling error created by an unfunded promise. The ordinary implementation rejects
a mismatch unless the explicitly labeled negative-control flag is enabled.

Early disclosure produces a different failure without exceeding a budget. All
four selected actors choose honestly, and the four unselected actors choose
shallow work. The unconditional quota remains one half while inspection among
the shallow actors is zero. Applying a common $q=.5$ incentive calculation after
telling actors their selections would be wrong. Audit records alone can make this
population look unusually clean if unaudited shallow work is ignored.

With false-sanction probability $.3$, $q=.5$ gives honest utility zero and shallow
utility $-.2$, below outside utility $.1$. All eight refuse. The selected slots
remain visible but unused. No completion denominator is invented, no loss is
collected and no audit money is spent. This is a participation failure, not an
efficient zero-cost audit program.

## Validation, meaning and next boundary

Eighteen tests cover exact selection marginals, mixed-refusal slots, all-actions-
committed-before-audit ordering, actual delivery, collateral conservation,
shared-role hours, capacity rejection, self-audit rejection, truthful versus broken
probabilities, disclosed selection and false-positive exclusion. A rational-
arithmetic utility oracle independently checks each dyadic quota from zero to one.
The deliberately small supported populations keep quota probabilities exact in
the reused sampler's floating interface. Source and imported-helper hashes are
recorded with every rebuilt sweep.

```sh
python3 -m unittest discover -s papers/07-release-packet/models/funded_audits -p 'test_*.py' -v
python3 papers/07-release-packet/models/funded_audits/run_experiments.py
```

Python 3.9+ standard library only. Each condition has a full event/actor/ledger
trace, and the CSV includes all 220 runs. No credentials, network calls, payment
providers or real submissions are involved. The proof is self-contained; its
one-shot incentive and quota premises advance `math-foundations.md` and directly
address the adversarial finding that expected cost was previously confused with
a hard resource reservation.

This closes a narrow simulation loop, not the institution. The actors believe the
stated plan; concealment and reserved balances are stipulated by the program;
auditors always execute their scheduled task and have fixed detection behavior.
Real auditor effort, adverse selection, false reports, appeal reversal, dependence
between auditors, collateral costs and legitimate authority remain unmodeled.
A useful next experiment would let an auditor refuse or strategically shirk and
measure which promises become unavailable. It should preserve the same offered,
participating, completed, selected, executed and sanctioned denominators instead
of labeling an undelivered audit as accomplished.

Red review found that the first floating-hour ledger allowed positive work within a $10^{-12}$ tolerance above zero capacity. The repaired ledger uses exact decimal-rational reservation/debit arithmetic with no overspending tolerance. Regression tests reject positive tiny work against zero capacity and verify that .1 plus .2 exactly fills .3. The original source is preserved in `models/funded_audits/results/model-before-exact-ledger.txt`.

The red review also exposed binary-floating tie reversals between honest/shallow and honest/refusal utilities. Preferences now use exact decimal-rational arithmetic internally; output includes the exact advertised utilities. Regression tests preserve the specified refusal-first, then honest, then shallow tie rule. Token rewards and losses enter utility at a stipulated one-to-one marginal conversion, not an inferred welfare measure.
