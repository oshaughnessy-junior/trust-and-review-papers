# Synthetic domain fixtures

Run from the repository root:

```sh
python3 papers/07-release-packet/domains/fixtures/domain_models.py
python3 papers/07-release-packet/domains/fixtures/replay_receipts.py
python3 -m unittest discover -s papers/07-release-packet/domains/fixtures -p 'test_*.py'
```

Both scripts print JSON and write nothing. All inputs are invented and committed
in `scenarios.json`. Rational arithmetic is exact; displayed square roots use
Python floating point. There is no random sampling or estimated parameter.

| Case | Mathematical behavior | Engine behavior |
|---|---|---|
| Physics | Shared-error variance 101/400 versus mistaken 29/1600; calibration revision 10.5→10 | Declared calibration amendment makes old use pending; fresh exact calculation supports new version |
| Biology | Two different treatment/batch explanations both have RSS 4; crossed toy contrast 1 | Arithmetic is supported while the separate additive-model coefficient is unknown; broader model scope rejected; crossed version checked separately |
| Economics | Trial mixture 8/5 versus target mixture 2/5; adverse completion share 100/109; separate final selection changes 1/10 to 1 | Trial and target calculations retain distinct versioned evidence; transport assumptions remain unchecked |
| Law | Same total work, FIFO misses one deadline and selected deadline order misses none; one infeasible job remains | Citation accuracy supports a teaching publication only; unsupported legal authority kind rejected |

`replay_receipts.py` calls the actual neighboring toy engine. It does not merely
print prewritten receipts. Its adapters perform narrow deterministic calculations,
then submit those outcomes to the engine. The engine trusts roles, control groups,
outcomes and clock inputs. It neither rediscovers the science nor authenticates
the inputs. It does not model counter-notices, privileged material or legal
calendars. The law schedule is an independent mathematical illustration.

The known negative control omits a real planted dependency. Its result remains
`current_under_toy_policy` even after the undeclared premise changes. This is an
intentional demonstrated limit, not a passing real-world currentness guarantee.
Two affected planted cases yield one pending record, hence recall 1/2. This
denominator consists of two separate synthetic replays, not two actual papers.

For the interaction counterexample, contrasts 1 and 3 produce an average of 2,
`crossed_exact_additivity=false` and a null `crossed_additive_effect`. The receipt
adapter then supports arithmetic only. Tests preserve the conditional-exogeneity
and causal-countermodel distinctions; a full-rank observed design is not causal
identification.

The checked-in `oracle-results.json` and `replay-results.json` are convenience
outputs. Regenerate with the scripts and compare parsed JSON. `run-manifest.json`
records source/output hashes and the Python version used for the accompanying
test run. These outputs establish only deterministic fixture behavior.

## Scope of validation

Tests use independently specified numeric expectations, limiting cases, missing
support, dropped-job rejection, content-identity behavior, actual engine amendment
cycles, and prohibited scope/authority upgrades. They do not establish scientific
efficacy, fairness under unknown common control, or safe operation with real users.

Future extensions should add partial confounding and sampling noise, heterogeneous
transport uncertainty, cross-skill scheduling, and hidden-common-cause sampling.
Those are proposals, not capabilities supplied by this four-case package.
