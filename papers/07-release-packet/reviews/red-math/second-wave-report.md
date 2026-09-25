# Second mathematical red pass: coupled behavior and audit repair

This review follows the first blue repairs and the new coupled simulator. It reads the actual code, manuscript, five traces, aggregate outputs, introductory blog and both onboarding paths. This is a second internal adversarial pass, not independent institutional peer review.

## Verdict at this checkpoint

**Qualified assent to a public research seed, conditional on the new RM-3 interface repair and the runtime reviewer's ledger repair.** The coupled experiment meaningfully advances the first packet: capacity reservation, strategic toy responses, retries, reliance selection and repair now share one person-hour ledger. Its unfavorable results remain visible. The blog and onboarding preserve the distinction between a useful record and a scientifically adequate check. No service-readiness or human-efficacy endorsement follows.

## Original findings verified

**RM-1 corrected in the model and prose.** The expected-budget inequality is now labeled expected expenditure. The separate hard-cap design selects bounded-size subsets of a fixed invitation population with equal marginal audit probabilities. Concealment, actual delivery, constant cost and independent authority remain explicit assumptions. Mixture of floor(Nq) and ceil(Nq) has correct marginal q and respects the count cap when its parameters are represented consistently. The new function's arithmetic interface has a defect described next; the mathematical design itself is sound.

**RM-2 corrected in executable behavior.** The same seeded completion scenario now reports 8,956 unresolved requests and satisfies offered=completed+unresolved. This review executed the repaired function rather than relying on an author's reported test result. The original defect and output remain archived.

**Adaptive completion theorem accepted.** The incorporated extension correctly requires history-conditional bounds, and does not transfer IID expected-cost formulas to adaptive retry. The explicit reliance-selection caveat is retained. The proof's stopping decision is taken before observing the next draw; discarding inconvenient draws must be counted as selection/refusal, not hidden.

## RM-3: returned hard-audit endpoint cannot be sampled

At N=6, a=1, B=5 and zero effort/loss, `hard_audit_interval` returns feasible=true and maximum_audit=0.8333333333333334. Passing that exact returned float to `blinded_audit_sample` raises `ValueError: marginal exceeds hard audit count cap` because converting its decimal representation to Fraction and multiplying by six gives a value slightly greater than five.

This is an interface inconsistency, not evidence that the hard-cap theorem fails. The function changes numerical interpretations between output and input. Preserve the count cap; do not permit a sixth audit by widening a comparison tolerance. Preferred repair: expose exact rational interval endpoints and let the sampler consume rational parameters directly, retaining floating values as display conveniences. Compute feasibility under consistent decimal/rational input semantics. Simply rounding an upper endpoint down is conservative, but can spuriously eliminate a boundary-only incentive-feasible interval.

The original implementation is preserved in `original_hard_audit.txt`; `second_wave.py` executes that snapshot so the failure remains reproducible after repair. A new regression should pass the interval's own exact endpoint directly to the sampler at nonterminating fractions such as 5/6 and verify zero budget violations.

## Coupled simulation validation

`second_wave.py` independently checked:

- All 7,400 recorded replicate runs and their scenario means and pooled stage shares.
- All **888** pointwise normal intervals, recalculating replicate variance through an independent sum-of-squared-deviations identity. The replication unit is the whole shared-budget run, not individual requests.
- All five full event traces, comparing regenerated events with saved outputs, then reconstructing actor work, steward intake/triage/invitation/reliance/repair debits, completed panels, full-effort panels and true-control independence counts.
- Per-person lane totals, zero terminal holds, true-versus-declared dependency reach, and the absence of automatic renewal after a repair check.
- An independent finite tree of individual completion outcomes. Fixed-panel retry gives completion 23/32, attempts 15/8 and completed A-share 101/138. Reroll gives 7/8, 7/4 and 5/6. These agree with the manuscript and the author oracle.
- All 14 coupled tests and 19 mathematical tests at this checkpoint passed.

The five reconstructed actual-work totals were 7.59 (group-first scarce), 27.51 (group-first plentiful), 5.05 (naive scarce), 26.48 (hidden control), and 27.41 (selective reliance), up to ordinary floating representation. Validation results and reviewed source hashes are stored in `second-wave-results.json`.

## Remaining interpretation boundaries

**Believed audits are not delivered audits.** The coupled agents use an exogenous q in hypothetical utilities; the coupled code supplies no audits or reward funding. This is stated prominently in code, README and manuscript. Coupling the new hard-cap audit assignment to those decisions is a valuable next experiment, but absence of that coupling is not concealed. Do not call the present result an enforced honest equilibrium.

**Skills are fixture predicates.** A and C are designated calibration/inference repair specialists, with actual-person capacity shared across lanes. The experiment does not fit heterogeneous skill proficiency, parallel scheduling, service deadlines or competence discovery. The manuscript says so. Its valid accounting identities are useful despite those omissions.

**Multiplicity invariance is unusually strong only within this fixture.** Group-first runs preserve the random path under clone-count changes because their group lottery, true-person mapping and behavior do not consume representative-dependent randomness. Complete-trace equality is correct here. Adding real expertise, changing a qualification threshold or allowing a new capacity pool changes the model rather than refuting the stated fixed-boundary result.

**More completions need not optimize the intended objective.** The synthetic A category has a different acceptance/effort pattern. Naive concentration can improve reported completion under plentiful resources while worsening representative opportunity. The model has not selected a normative social-welfare objective. The manuscript avoids presenting one aggregate score as universal success.

**Repair checks remain checks.** Known affected reliance stays unresolved after repair. Unknown graph edges preserve a falsely quiet local view relative to the omniscient simulation oracle. This is an appropriate negative control, not a discovery mechanism.

**Floating ledger invariants require careful closure.** The runtime reviewer independently found that allowing actual settlement to exceed each reservation by a tolerance can accumulate excess through multiple zero-demand holds. That finding is theirs; their preserved probe and repair verification should govern disposition. Default coarse-hour traces reproduced correctly in this mathematical review. Passing those traces does not excuse an incorrect public API invariant.

## Collective recommendation

The release is compelling when framed as a small falsifiable boundary with tangible examples: label multiplication, reservation scarcity, legitimate refusal, selective reliance, hidden dependencies and repair without automatic renewal. Its blue/red record now demonstrates substantive correction rather than merely attaching caveats. Complete RM-3 and the independent runtime/export fixes, rerun the release checks, and bind the final collective assent to that exact candidate. A live institution still requires people, authority, budgets and measured behavior outside this packet.
