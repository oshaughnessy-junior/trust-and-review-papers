# Independent integration review

Adoption-theory agent, 26 September 2026. Internal cross-review, not external peer
review. Reviewed MANUSCRIPT.md, model.py, results.json, and test_integration.py.
Seven author tests pass. Additional independent probes pass at 243 points in a
heterogeneous probability box and 27 posterior boundary cases.

## Findings

**I-1 — interpretation correction required before using the robust rule as an
adoption recommendation.** The corner result itself is correct: the expected
benefit is multi-affine over the five probabilities and its extrema occur at box
corners. However, the sentence “A strictly positive minimum warrants adoption”
reads as a complete entry decision even though b excludes integration cost k/H
and network effects. Counterexample: b=1, setup cost k=2, H=1, zero network value;
all probability intervals can be points, so min b=1>0, but entry margin is -1.
Likewise a negative maximum standalone benefit need not warrant rejecting entry
if demonstrated network value exceeds the shortfall. Replace with: “A positive
minimum favors policy 1 over policy 0 on the modeled recurring standalone balance;
a negative maximum favors policy 0 on that balance. Entry and network decisions
still require their separately modeled costs and benefits.” Alternatively include
k/H and an explicitly bounded network term in the quantity whose sign is tested.

**I-2 — map the bridge to h-c, not h.** The bridge b already subtracts recurring
review cost c. In the adoption note its counterpart is h_i-c_i, and the entry
intercept is b-k/H. State this mapping explicitly to prevent subtracting the
recurring cost a second time when the two models are combined. Existing prose
mentions separate setup amortization but calls b a benefit; an equation would
remove the ambiguity.

**No algebraic blocker found.** The direct loss difference is correct, conditional
valid-case and invalid-case errors remain separate, the posterior uses the
appropriate clearance likelihoods, and zero-clearance probability correctly
returns undefined. The false-alarm independence assumption is explicitly separate
from the invalid-case common-cause model. Exact rational result strings support
reproduction; decimal examples match.

**Scope retained.** The rectangular interval is a stipulated uncertainty set, not
a calibrated confidence region. The example is risk-neutral, binary validity,
fixed losses, and no abstention; notes explicitly admit omitted consequences.
There is no empirical claim from the toy benefit changing sign with prevalence.

## Operational gate self-audit for the aiXiv design revision

The companion proposed §6 rule uses nested S1 ⊆ S2 ⊆ S3 and cannot award a higher
level when a lower mandatory gate fails. Qualified human disposition, independent
authority, exact identity, and version-specific archive identity remain mandatory
S1 gates. Thus agent-only records remain level 0/pending despite useful machine
checks; this is consistent with the existing lifecycle, and should be stated in
release-facing summaries. Full-release aggregation requires full claim scope,
preventing a high-level slice result from masquerading as full-claim assurance.
Unknown, disputed, and stale conditions must remain distinct from a completed
negative scientific result. Nonapplicability is allowed only under predeclared
policy rules and cannot exempt mandatory gates.

No additional logical contradiction found. This is a proposed policy: a follow-up
implementation must encode the exact predicate inventory and applicability rules,
rather than claiming the existing synthetic runner already enforces them.
