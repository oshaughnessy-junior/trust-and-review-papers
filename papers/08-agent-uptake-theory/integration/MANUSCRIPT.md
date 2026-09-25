# When better detection is worth its cost

This note connects the adoption and correlated-review models without equating agreement with value. All probabilities and costs below are stipulated toy parameters; none estimates MCRP effectiveness.

Let an incoming claim be invalid with prevalence $p$. Under review policy $j$, let $q_j$ be the probability of clearing an invalid claim and $a_j$ the probability of flagging a valid claim. Let $L$ be the loss from clearing an invalid claim, $A$ the cost of a false alarm, $s$ a direct saving in record assembly or reuse, and $c$ the additional review cost. Comparing policy 1 with policy 0 gives expected net benefit

$$b=s+pL(q_0-q_1)-(1-p)A(a_1-a_0)-c.$$

This follows by subtracting expected losses $pLq_j+(1-p)Aa_j$ and including direct savings and cost. The two error rates condition on different populations. Neither reviewer count nor controller separation determines them. Unmodeled consequences, including abstention and downstream reuse, need their own outcomes and costs.

In the adoption lane, this $b=h_i-c_i$ supplies a per-period standalone benefit, with setup cost amortized separately as $k/H$ and entry intercept $b-k/H$. The recurring review cost $c$ is already included and must not be subtracted twice. Network terms must then represent additional benefits rather than counting the same reuse saving twice. Fixed horizons, risk neutrality, stationary prevalence and losses, and binary validity are assumptions of this bridge, not scientific facts.

## A counterexample to more checks always helping

Take $q_0=.28$ and $q_1=.1+.9(.2)^5$, a shared-error floor with five residual checks. Independently stipulate valid-case false alarms $a_0=.02$ and $a_1=1-.98^5$. Set $L=100$, $A=5$, $c=.2$, and $s=0$. With prevalence $.001$, benefit is approximately $-.56204$; with prevalence $.05$, it is $+.33718$. Thus the same improvement in invalid-case detection can help or hurt depending on prevalence and false-alarm cost. Residual independence on invalid cases does not justify valid-case independence; the example explicitly stipulates both separately.

The posterior invalidity of a cleared claim is

$$P(\mathrm{invalid}\mid\mathrm{clear})=\frac{pq}{pq+(1-p)(1-a)},$$

when the denominator is nonzero. A conditional false-clear probability $q$ cannot be reported as this posterior. Zero clear probability leaves the posterior undefined.

## A small robust decision rule

Suppose the five probabilities $(p,q_0,q_1,a_0,a_1)$ lie in specified closed intervals, with nonnegative fixed costs. Benefit is affine in each probability while holding the others fixed. On this rectangular uncertainty set its extrema occur at corners: successively move each coordinate to an endpoint that does not increase (or decrease) the function. Enumerating $2^5=32$ corners therefore computes exact minimum and maximum. A strictly positive minimum favors policy 1 for recurring standalone value **under these assumptions and bounds**; a negative maximum favors policy 0 on that comparison. Neither alone determines entry: setup cost $k/H$ and additional network benefits must enter the tested margin first. For example, standalone benefit 1 with setup cost 2 and horizon 1 does not justify entry without network benefit. An interval straddling zero does not determine even the standalone choice. A rectangular bound can be conservative when parameters are coupled. Unjustified bounds provide no reliability guarantee.

`model.py` performs rational arithmetic and `test_integration.py` tests the loss identity, opposite decisions, posterior dependence on prevalence, and corner bounds against an interior grid. `results.json` retains exact rational strings alongside display decimals. These checks test implementation against stipulated algebra, not intervention efficacy.

## First empirical target

Measure assembly/reuse savings and review time separately from error outcomes on a blinded, bounded task set. Compare like claim scopes and capture complete in-scope attempts, including abstentions, repairs and failures. Estimate both false clears and false alarms, report uncertainty and task prevalence, and disclose shared tools and methods. This would make the utility question testable without promising a universal reliability badge. No such study has been conducted here.
