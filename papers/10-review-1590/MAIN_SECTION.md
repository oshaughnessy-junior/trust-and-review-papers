### A bounded four-action decision procedure

The [sequential reference machine](../../10-review-1590/README.md) now supplies an
explicit implementation profile for one synthetic episode. It admits at most
eight versioned targets and 64 accepted events. State consists of target scope,
declared dependencies, phase, fixed panel/alias draws, next attempt, audit slots,
spent/held work, immutable event records and separately dated reliance decisions.
Every command carries a unique request ID and actor; records add sequence,
version/scope, outcome/evidence and exact resource balances. Rejections leave the
state unchanged. The bounded local guard rules are:

| Action | Guard | Transition |
|---|---|---|
| offer | New identity; declared author; no known stale dependency; audit preflight and sufficient worst-case work reservation | Fix distribution and three attempt slots; create open target. |
| check | Declared verifier; exact open target/scope and planned representatives; explicit result/evidence | Debit the next slot; refusal stays open until exhausted; completed success becomes ready; completed failure becomes failed. |
| rely | Separately declared decision-maker; ready exact target/scope; matching last successful check | Append current reliance; a check never creates it implicitly. |
| amend | Declared author; changed identity and fresh successor | Mark declared transitive affected targets pending, suspend current reliance, preserve historical events; compute an optional repair planning bound. |

Equivalent dispatcher pseudocode is: validate request identity; save state;
validate the action guard; apply its transition and resource debit; append the
event; restore saved state on any rejected command. This is single-process
sequential atomicity, not distributed consensus, durable replay protection or
authentication. Actor strings, evidence references and scientific outcomes remain
trusted fixture assertions. A successor designation neither performs repair nor
renews reliance. Missing dependency edges remain a demonstrated failure premise.

### One trace through all four models

Offer `mean@v1` over three synthetic values, depending on `data@v1`. Uniform group
panels AB,AC,BC give offered category probability p=1/3 for AB; interchangeable
aliases do not change this law. Set panel-level completion a=1 for AB and b=1/4
otherwise, with completion coins fixed independently before observing audit
results. For three IID attempts, s=1/2, E[N]=7/4, completion probability=7/8, and
AB's completed share=2/3. These are probabilities over the stipulated fixture,
not frequencies inferred from its single realization.

Invitation work costs 1/10 and completed checking costs one abstract unit. Audit
cost is one, the fixed three-slot cohort has quota at most one, and ex-ante q=1/3.
Before attempts, reserve 43/10 units for worst-case checking and auditing from one
20-unit account. Expected check work is 21/20; expected audit work is 7/12 under
the stipulated stopping/independence premises. Administrative overhead is not
modeled, and these units are not calibrated human hours. Static audit utilities
c=1/10,R=1,u=0,alpha=1/20,beta=17/20,F=1 yield effort lower bound 1/8 and hard cap
1/3, so this configured q passes the ex-ante feasibility test.

| Event | Retained realization | Cumulative actual work |
|---|---|---:|
| offer | Fix mean@v1 and reserve 43/10 | 0 |
| check 1 | AC refuses | 1/10 |
| check 2 | AC refuses | 1/5 |
| check 3 | AB completes; one audit executes | 23/10 |
| rely | Separate decision cites check 3 | 23/10 |
| amend | data@v1→data@v2 suspends current reliance | 23/10 |

One affected claim starts repair workload Z0=(1,0). Matrices
M1=((1/4,1/4),(0,1/2)) and M2=((1/2,0),(1/4,1/4)) share w=(1,1), r=1/2, giving
conditional expected cumulative weighted repair ≤2. The machine records this
planning bound; it neither reserves nor executes repair from that expectation.
Absent a valid witness, invalidation still occurs and the bound stays unavailable.

This is accounting composition, **not a composed incentive or safety theorem**.
The API reveals audit outcomes: if the first refused slot consumes the only audit,
later conditional q=0 and honest effort need not remain a best response. The
positive trace fixes behavior before reading those outcomes; the implementation
retains the adaptive counterexample rather than claiming concealment. Reward
funding, sanctions, truthful effort and physical audit performance remain external
premises. Additional branches reject expected-budget-only admission, stale reliance,
wrong scope/authority, duplicate requests and insufficient capacity; hidden lineage
and unstable repair switching remain explicitly failing premises. This executable
linkage—not new probability theory or measured efficacy—is the added contribution.

