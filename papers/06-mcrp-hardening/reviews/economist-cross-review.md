# Economics cross-review of games draft

Reviewed `work/games/paper.md`, 2026-09-25. This is an agent cross-review, not human scientific sign-off. No source literature beyond the draft's stated scope was needed to verify these algebraic points.

## Verified conditional derivations

- Equation (1) follows by direct subtraction. It is properly labeled a one-step deviation condition rather than a network equilibrium theorem.
- Equation (2) correctly solves the absorbing two-state honest-policy recursion. The false-positive cost affects continuation value and is not silently held constant as F increases.
- Synthetic deterrence examples are arithmetically consistent: the original threshold is approximately 3.034; beta=.02 gives approximately .160; delta=.10 gives approximately .021.
- Equation (3) is the interior mixed inspection equilibrium under perfect detection, S>g and B>a. The stated failures outside that region are appropriately limited.
- The additive coalition expression is valid for the specified comparison, including correlated adverse events when only their additive expected losses matter.
- Common-mode unanimous-error probability and equicorrelated mean-error variance are correct under their respective assumptions; their scopes are correctly separated.

## Required clarification: whitewashing changes the honest value too

The whitewashing subsection instructs replacing W by W_eff in (1). If alpha>0, making reentry available also changes the honest policy's continuation value V, because honest reviewers can receive an adverse outcome and then reenter. Reusing V from the absorbing formula (2) while replacing only W is generally inconsistent. State that V and W_eff must solve the modified Bellman system together, with V_new explicitly specified as an exogenous entry value or determined endogenously. The qualitative zero-cost/full-privilege conclusion remains valid when V_new=V, but intermediate numerical deterrence calculations must recompute both values.

## Required scope clarification: compatibility with canonical governance

The current draft still describes a contribution ledger and newcomer track record without explicitly preserving TDRG fresh public case personas. State that durable reviewer history belongs to protected domain-account custody; public credit attaches to review objects/case personas, or selectively disclosed credentials under an explicit different profile. The parent has selected shared core verbs offer/check/rely/amend; the draft's offer/review/repair can be local substeps, not a competing canonical protocol.

## Nonblocking improvements

1. Equation (4)'s label “necessary condition against that joint deviation” is clear in context; call it an exact no-profitable-deviation inequality for the specified additive comparison to avoid seeming weaker than the derivation.
2. For the finite suspension illustration, emphasize that its deterministic loss formula is an illustration, not the exact Bellman gap when false-positive restrictions can recur after reinstatement. The subsequent instruction to use actual state-specific values already points in this direction.
3. Exploration denominator w_i requires nonnegative weights and a positive sum when epsilon<1; add those assumptions or define the all-zero fallback as uniform.
4. The correlated-error variance requires an admissible covariance matrix (equicorrelation eta in [-1/(k-1),1] for k>1). If interpreting positive common-mode dependence only, state eta∈[0,1].

## Conclusion

The core mathematics is defensible under its explicit assumptions. Whitewashing's continuation-value feedback is the one substantive algebra/model-consistency issue found; the remaining required change is alignment with the repository's privacy and protocol interfaces. No claim of field efficacy is warranted, and the paper already mostly respects that limit.
