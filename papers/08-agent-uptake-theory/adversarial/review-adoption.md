# Adversarial review of the adoption theory lane

25 September 2026. Internal agent review under the same orchestration; not an
independent external scientific review. Read `../adoption/MANUSCRIPT.md` and
`../adoption/model.py` after their initial production.

**Disposition:** No blocking error found in the three conditional propositions.
The lower/upper monotone iterations use the correct initial-state restriction;
withdrawal checks forced actors only when other payoff parameters remain fixed;
the potential argument requires strict unilateral improvement and distinguishes
weak equilibria from the declared tie policy. Synchronous oscillation and congestion
negative controls prevent overreading existence as spontaneous uptake.

**Minor implementation findings:** `potential(state)` does not validate state
length/binary values, while `margins` does. `cheapest_stable_full_seed` validates
nonnegative costs but permits floats/NaN/bools despite exact-rational scope. Reported
toy results use valid inputs, so these findings do not invalidate them. Findings
sent to the owning agent for correction.

**Main integration constraint:** The adoption payoff's standalone value must not be
operationalized as number of passing reviews or agreement among agents. Correlated
failure and selective release can increase those counts while reducing useful
information. Calibrate any empirical benefit against an external fault oracle,
unchanged negative controls, the same information in a baseline workflow, and all
in-scope attempts and resource expenditure. A preregistered local batch supplies
a bounded attempt denominator; it cannot establish global absence of hidden trials.

**Release wording:** “A model of conditions for uptake” is supported. “A model showing
agents will adopt” is unsupported. The note already largely preserves this boundary.
No change to the simple four-action interface is required by these results.
