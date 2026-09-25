# Formal audit cross-review by the evidence lane

The 11 named tests in `formal/test_audit_contract.py` pass. A separate probe
compared 4,320 exact evaluations of `interval` against independently calculated
utilities and budget feasibility. The probe enumerated affordable integer audit
counts directly, rather than calling the implementation's cap function.

The additional grid used populations 1, 3 and 5; audit costs 0 and 2/3; budgets
0, 1 and 3/2; effort costs 0 and 1/3; false-positive rates 0 and 1/2; detection
rates 0, 1/2 and 1; enforceable losses 0 and 2; fixed reward1 and outsideutility1/4;
both budget contracts; and q in {0,1/7,1/3,1/2,1}. Every interval membership
agreed with direct honest-versus-shirk/abstain comparison and the independently
computed expenditure/count condition.

No mathematical blocker was found. Nonpositive discrimination, zero effort,
zero audit cost and constant participation cases behaved as specified. These are
exact finite checks supplementing algebra, not measured behavior. Concealment,
audit delivery, fixed population and actual identical costs remain external
premises. The all-invitation hard cap does not establish budget feasibility for
unmodeled rewards, appeals or heterogeneous audit costs.

This is a second inspection within the same author-directed team; no independent
institutional or scientific approval is implied. The 4,320 probe comparisons are
not 4,320 extra unit tests or participant observations.
