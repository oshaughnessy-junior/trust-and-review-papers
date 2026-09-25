# Coupled allocation, toy behavior, capacity and repair

Read [coupled-agents.md](../../manuscripts/coupled-agents.md) for the model, exact
special cases and conditional interpretation.

```sh
python3 -m unittest discover -s papers/07-release-packet/models/coupled -p 'test_*.py' -v
python3 papers/07-release-packet/models/coupled/run_experiments.py
```

Standard library only. 14 tests; 74 scenarios x 100 replicate seeds; 88,800
synthetic requests; 888 metric rows with replicate-mean nominal intervals. Five
full event traces show scarce capacity, plentiful capacity, naive multiplicity,
hidden control and selective reliance. No claim of real efficacy or protocol
conformance is made.

The shared person ledger covers intake, triage, invitation/check work, scoped
reliance and repair. It accounts for holds and actual debits atomically. Skills
and actual-person mappings are fixed toy facts; the operator does not thereby
learn real identity. Repair checks do not automatically renew reliance. Missing
dependencies remain invisible to the local reliance view and visible to the
simulation evaluator's separate oracle.

Behavior injection: `run(Config(...), seed=1, trace=True, behavior=fn)` accepts a
function `(person, request_index, prior_used_hours, rng)` returning
`(action, reported_completed, actual_hours, utility_dict)`. It must honor
`actual_hours <= 1` per invitation and use `honest`, `shallow` or `refuse` actions.
The default model gives actors a perceived audit probability; it does not deliver
or fund audits. Use the separate math model for audit budget experiments.

Returned simulation receipts are plain records, not signed protocol messages.
The adjacent runtime has stronger target and authority semantics. Connecting the
behavior model to that runtime requires an explicit adapter and new validation.
