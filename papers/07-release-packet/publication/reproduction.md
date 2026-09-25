# Read, reproduce and change the candidate

The portable starting directory contains `README.md`, `run_checks.py`, `models/`,
`toy_agents/` and `domains/`. In the working repository that directory is
`papers/07-release-packet`. In the download it is `mcrp-prototype`.

## Read without installing anything

Open `index.html` from the extracted download in a browser. All reading pages,
figures, styles, controls and saved traces are local; there are no analytics,
remote fonts or network calls. Interactive controls evaluate the three stated
formulas. They do not execute the Python simulation. Saved results are also
provided as JSON and CSV beside their source code.

The download includes research fixtures with deliberately vulnerable baseline
code, clearly labeled in `reviews/red-runtime`. They reconstruct the original
packaging counterexamples using public sentinel strings. Use `surfaces/build.py`
and `surfaces/verify_export.py` for the repaired packaging tools.

## Reproduce the experiments

Use Python 3.9 or later. From the portable starting directory:

```sh
python3 run_checks.py
```

No third-party Python package, network, credentials, model inference or external
data is needed for this command. It runs the model suites and independent
adversarial regressions, then regenerates synthetic outputs. The terminal reports
each check group and the final total. `results/validation.json` records success,
test counts, Python version, source/input hashes, saved-result hashes and the full
log inventory. Inputs are captured before and after execution; a changed source
or fixture makes the run fail. These checks bind evidence to a run, not the
scientific truth of its content.

This is a research run, not a production readiness assessment. Successful negative
controls mean the specified failure is exposed, not that it has been eliminated.
Random-number implementation differences across Python versions may change sampled
trajectories; deterministic finite arithmetic and invariant tests are separate.

Run on a working copy: regenerated timings, logs and environment records will
change some files. An export's original manifest describes the original snapshot;
it is not expected to certify your modified reproduction directory afterward.
Preserve the original download if you want to compare results or verify integrity.

## Choose a smaller entry point

| Question | Command from the portable directory |
|---|---|
| Can an existing review record enter the toy runtime honestly? | `python3 -m adapters.demo` |
| How much could a tiny human-interface study establish? | `python3 models/human_pilot/run_design.py` |
| What happens to a scoped decision after amendment? | `python3 -m toy_agents.run` |
| What does publication approval bind in the separate toy cycle? | `python3 models/release_cycle.py --output results/release-cycle.json` |
| What are the exact panel, repair and audit bounds? | `python3 models/math/run_experiments.py` |
| What changes across allocation, completion and reliance? | `python3 models/coupled/run_experiments.py` |
| Does recognition feedback beat uniform routing? | `python3 -m models.ecology.run` |
| Do promised inspections actually get funded and delivered? | `python3 models/funded_audits/run_experiments.py` |
| Can correction credit reward manufactured work? | `python3 -m models.ecology.correction_game` |
| What does the biology or legal example actually calculate? | `python3 domains/fixtures/domain_models.py` |
| Can domain examples issue and amend real toy receipts? | `python3 domains/fixtures/replay_receipts.py` |

Change one parameter or one premise, preserve the old result, and explain what
changed. A failed invariant is useful evidence. A new parameter result is not a
new theorem. Include the full offered-work and unfinished-work denominators.

## Optional figure and reading-page generation

The core tests are standard-library-only. Scientific figure regeneration
additionally uses Matplotlib (the saved figure manifest records the version):

```sh
python3 surfaces/make_figures.py
```

When a different environment changes those saved result bytes, regenerate figures
before building a new export so their input hashes agree. Merely reproducing the
core models does not require Matplotlib.

Figures read the retained coupled/ecology results. Their manifest binds source,
input tables and output bytes. The ecology whiskers are seed ranges, not confidence
intervals. The selection figure shows pooled stage shares rather than independent
observations from people.

Reading-page generation additionally requires Pandoc available on `PATH`:

```sh
python3 surfaces/build.py ../mcrp-public-candidate
python3 surfaces/verify_export.py ../mcrp-public-candidate
```

The output must be outside the source packet. The builder stages a fresh candidate,
rejects symlinks and unexpected pre-existing output, then replaces only a recognized
unchanged prior export. It does not publish, deploy or change repository visibility.
The verifier checks exact file and ZIP membership, hashes, local links/fragments,
validation-evidence references and four declared disclosure patterns. It cannot
establish that every private fact or rights issue has been discovered.

The file-map digest and ZIP digest identify a candidate. Neither is a signature,
license, approval or statement that source claims are true. A release decision
must identify the responsible maintainer, adopted rights terms and destination
for those exact bytes.

The optional eight-page synthesis brief uses ReportLab, Pillow and pypdf:

```sh
python3 surfaces/build_brief.py
```

It writes `results/mcrp-release-brief.pdf` and a manifest binding its builder and
figure input. Its PDF metadata is fixed for reproduction; metadata dates are not
release timestamps. The saved PDF can be read without these packages.
