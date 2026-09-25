# Compact main-text additions for review 1588

## After Proposition 1: a constrained construction

Proposition 1 already permits any fixed nonempty feasible family; the following
new synthetic fixture exercises conflicts, skill coverage and capacity. A two-task
panel requires distinct groups to supply calibration and inference, one unit each.

| Group | Declared skills | Available units | Fixed weight |
|---|---|---:|---:|
| A | calibration | 1 | 1 |
| B | inference | 1 | 1 |
| C | calibration, inference | 1 | 2 |
| D | inference | 1 | 1 |
| E | calibration | 0 | 1 |

Forbidden pairs are A–B and C–D. Enumerate pairs, reject conflicts and insufficient
capacity, and require an injective matching of groups to the two skill tasks.
Exactly AC, AD and BC remain. Choosing Q proportional to fixed group-weight
products gives Q(AC)=2/5, Q(AD)=1/5, Q(BC)=2/5. Uniform Q would also be valid.
Neither choice is claimed optimal. A normalized within-panel representative kernel
preserves this Q when A has 1, 10 or 100 interchangeable labels; explicit finite
enumeration confirms it. Uniform representative-first sampling instead gives A
inclusion 2/3 with one label and 20/21 with ten. Its uniform baseline differs from
the deliberately weighted Q, and should not be conflated with it.

This construction assumes the group/control map, skills, one-unit capacity and
conflicts are supplied correctly and unchanged by cloning. Genuine new capacity
or skill changes feasibility and is outside that transformation. An empty feasible
family leaves the request unassigned rather than silently relaxing coverage or
conflicts. The example constructs one panel; it does not authenticate controllers,
reserve resources concurrently, or solve general review scheduling.

## After the IID retry example: sensitivity to completion and cost

For 0<p<1 and a,b>0, completed risk share z obeys

$$\frac{z}{1-z}=\frac{p}{1-p}\frac ab,\qquad z>p\iff a>b.$$

Hence the completion-rate ratio, rather than either parameter alone, determines
the odds distortion. At p=1/10:

| a | b | Exact completed share |
|---:|---:|---:|
| 1/10 | 1 | 1/91 |
| 1/10 | 1/10 | 1/10 |
| 1/10 | 1/100 | 10/19 |
| 1 | 1/100 | 100/109 |

Under the IID retry model, cost sensitivity is exactly
partial E[C_L]/partial c_i=E[N_L] and
partial E[C_L]/partial c_c=P(completion). At L=10 with the original p=.1,a=1,b=.01,
changing (c_i,c_c) from (.2,2) to (.02,2), (.2,20), or (2,2) changes expected
cost from 2.625583 to 1.494949, 14.949489, or 13.931919 model units. This does not
alter completed share under IID assumptions; adaptive behavior requires another
model. These are stipulated parameter sensitivities, not observed labor.

## After the reconciled audit propositions: a sensitivity boundary

Use c=.2,R=1,u=.1,F=2,alpha=.02,beta=.8,N=100, audit cost a_a=.1 and B=2 as the
synthetic baseline. Its hard-cap interval is [5/39,1/5]. One-at-a-time changes give:

| Changed parameter | Hard-cap interval | Feasible? |
|---|---|---|
| alpha=.3 | [1/5,1/5] | Weak-indifference point only |
| beta=.4 | [5/19,1/5] | No |
| c=.4 | [10/39,1/5] | No |
| F=4 | [5/78,1/5] | Yes |
| a_a=.2 | [5/39,1/10] | No |
| B=4 | [5/39,2/5] | Yes |

For alpha>0,F>0,beta>alpha, compatibility of effort and participation requires

$$c\alpha\le(R-c-u)(\beta-\alpha).$$

F cancels: increasing sanctions cannot repair this particular conflict. For
R=.4,c=.2,u=.1,alpha=.3,beta=.8, right minus left is -.01, so F=1,2,8 all fail
even before funding is considered. A nonempty interval only makes honesty a weak
best response; it neither selects that behavior at ties nor funds real rewards.

A simultaneous stipulated box c∈[.1,.2], alpha∈[.01,.04], beta∈[.7,.9], F∈[2,3],
with other baseline quantities fixed, has common hard-feasible interval
[5/33,1/5]. The effort lower bound increases with c and alpha and decreases with
beta and F; the participation upper bound decreases with c, alpha and F here,
where R-c-u>0. These monotonicities justify the endpoint calculation throughout
the continuous box; sixteen corners and an interior grid are additional code
checks. The box is assumed, not a fitted confidence region.

The supplementary sensitivity package retains 15 completion cases, 27 retry-cost
cases, 23 audit variations, sanction conflicts and the constrained panel fixture.
Eleven named tests check direct utilities, finite retry paths, skill matchings
and representative pushforwards using exact rational arithmetic. It does not
supply measured human/agent preferences, independence, enforcement or field efficacy.
