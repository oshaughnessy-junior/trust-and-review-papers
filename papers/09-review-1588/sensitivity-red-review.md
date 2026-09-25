# Independent internal audit: sensitivity and constrained panels

Read `models/math/review1588-sensitivity/sensitivity.py` and independently checked
its principal claims. Internal author-directed review, not external scientific
replication. The eleven named sensitivity tests pass.

## Independent checks

- Enumerated feasible two-group panels directly for the supplied capacities,
  calibration/inference tasks and conflict pairs. The result is exactly AC, AD,
  BC; BD lacks calibration, AB and CD conflict, and E has zero capacity.
- Computed the fixed product-of-group-weight distribution as 2/5, 1/5, 2/5 on
  AC, AD, BC. The C weight is two. It is a nonuniform law on a constrained family,
  demonstrating that neither uniformity nor all-subsets feasibility is required.
- Independently enumerated actual representative pairs with A multiplicities
  1, 2, 5 and 10, filtered them through the same group-panel constraints, and
  recovered the naive representative-first distribution each time. The fixed
  group-weighted law remains unchanged. These are four finite enumerations,
  not sampled trials.
- Checked 625 distinct interior/corner points in the proposed effort/false-positive/
  detection/sanction box. Every resulting hard interval contains q=4/25. The grid
  supports the implementation but is not by itself a proof over a continuum.

## Necessary interpretation

For the specified box with positive participation surplus, the effort lower bound
c/((beta-alpha)F) increases with c and alpha and decreases with beta and F. The
participation upper bound (R-c-u)/(alpha F) decreases with c, alpha and F. The
budget cap is fixed. Consequently their worst endpoints occur at the relevant
corners: the common hard interval is [5/33,1/5]. State that monotonicity argument
when describing the entire box as robust. Without it, finitely checked corners
would not imply a continuous-box guarantee.

The group-weighted policy and the uniform representative-first policy have
different baseline weighting conventions: C has weight two in the first,
whereas representative counts alone determine the latter. The example must not
attribute their entire difference at unit multiplicities to cloning. The cloning
claim is the invariance or change *within each policy* when A gains labels.

The audit sensitivity routine intentionally covers only a positive-denominator
branch; the independent formal fixture supplies degenerate cases. A parameter
sweep and a box of arbitrary model values are not confidence intervals,
behavioral parameter estimates, or evidence of real-world protocol effectiveness.

**Code disposition:** no mathematical implementation blocker found. The preceding
monotonicity and policy-label qualifications were sent to the author before final
prose integration.

## Final prose review

Read the completed `SUPPLEMENT.md`. It now contains the analytic monotonicity
argument for the full stipulated box and explicitly separates the weighted group
law from the naive representative policy's different one-label baseline. The
completion odds multiplier, listed rational table values, sanction-independent
incompatibility, fractional-budget contrast, and constrained panel construction
match the exact code. All eleven sensitivity tests pass. No remaining mathematical
or numerical blocker was found. The manuscript's integrated Propositions 4a/4b
also preserve fixed positive N, actual identical audit costs, the division-free
degenerate cases, and the information-set/concealment premise.
