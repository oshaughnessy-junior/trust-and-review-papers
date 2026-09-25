# A completion bound that survives adapted retry policies

Red mathematical review contribution; conditional theorem, not measured human behavior.

Let a request's attempt index be j=1,...,L. The pre-attempt history H_j includes all earlier offers, refusals, costs and any algorithm state. Let I_j indicate that this attempt is reached. The decision to stop or continue must be measurable before drawing the current offered category. On each reached history h, define

- p_h = Pr(current offered category is R | h, I_j=1),
- a_h = Pr(completion | R,h,I_j=1),
- b_h = Pr(completion | not R,h,I_j=1).

Assume p_h <= epsilon < 1, a_h <= u <= 1, and b_h >= ell > 0 on every reached history. Stop at the first completion; an adapted policy may instead stop unresolved before an attempt. No independence or stationary p_h,a_h,b_h is assumed.

**Proposition.** If there is positive total completion probability, then

$$\Pr(R\mid \text{terminal completion})\le
\frac{\epsilon u}{\epsilon u+(1-\epsilon)\ell}.$$

**Proof.** Conditional on reaching h, risky terminal-completion probability is x_h=p_h a_h, and other terminal-completion probability is y_h=(1-p_h)b_h. Set K=epsilon u/((1-epsilon)ell). By the assumptions x_h <= K y_h. Multiply by the probability mass of reaching h and sum across all histories and attempts. First-completion events are disjoint, so total risky and other terminal masses X,Y satisfy X<=K Y. Hence X/(X+Y)<=K/(1+K). For u=0, X=0 directly. The argument uses expectation/integration in place of finite sums for non-discrete history. A countably infinite horizon follows by monotone convergence when terminal completion has positive probability. This does not establish finite expected attempts, cost or resolution time. QED.

The policy must not inspect and discard the current draw without counting it as an invitation/attempt. Such cherry-picking changes the effective p_h or completion kernel. The theorem also does not cover selecting a favorable subset of already completed panels for reliance: that is another selection stage.

**Executable independent evidence.** `probes.py` enumerates category-specific refusal paths for 20 history-dependent policies to depth eight, including adapted unresolved stops. With epsilon=1/5,u=4/5,ell=3/10, all shares satisfy 2/5. A tightness case is the constant policy at the extrema, which gives 2/5 at every finite positive attempt limit. The existing implementation already verifies static tightness; this contribution specifically tests adapted histories.

**Necessary boundary.** Keeping p_h=.1 at every attempt but setting a_h=1,b_h=0 gives risky share one among completed requests, despite the offer cap. Eight attempts yield completion probability 1-.9^8=.56953279, entirely risky. The positive safe-completion floor cannot be replaced by an observed pooled average from a different population or time interval. Refusal remains legitimate; the theorem creates no entitlement to compel it.

**Third selection stage.** If p=.1 and a=b=1, completed risk remains .1. If the decision maker relies only on R completions, the relied-upon share is one. Publish both completion and reliance denominators and model any reliance filter separately. A bound on completion composition does not regulate an actor's independent decision to rely.

**What does not generalize.** The geometric formulas for expected attempts, unresolved probability and expected costs in the manuscript rely on stationary IID attempts. The proof above generalizes only the completion-share envelope. Estimate or bound costs separately under the adapted policy, and account for invitation, partial work, reservation and refusal costs at their actual stages.
