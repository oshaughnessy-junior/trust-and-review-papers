# Second-wave integration review: models, exported evidence and release boundaries

**Internal AI red team; same operator; not external security certification.**
This supplements `report.md` with the coupled model and public-export boundary.

## Evidence and release implications

The coupled simulator's fourteen tests were independently executed and passed.
It joins allocation, retries, person capacity, reported completion, selection for
reliance, hidden declared dependencies and repair under a single synthetic budget.
Its strongest positive semantic choices are that reported completion does not
establish honest effort and completing repair does not silently renew reliance.
The manuscript explicitly says these receipts are **not conformance** with the
adjacent stronger target/authority runtime. Keeping that distinction prevents
an illustrated sequence from becoming an invented end-to-end implementation.

The supposedly static packaging boundary had substantive independent defects.
The export inventory was computed from every file present in the destination,
after deleting only paths named by a prior manifest. An untracked leftover was
therefore promoted into the approved-looking inventory and download ZIP. Source
file symlinks were followed, copying content outside the intended packet. The
verifier checked only listed files and ignored ZIP content entirely.

`export_probes.py` demonstrates the original behavior without touching private
material: a temporary miniature packet, public sentinel strings, and a temporary
source symlink to another public sentinel. The original builder and verifier are
archived as `baseline_export_builder.py` and `baseline_export_verifier.py`.
**Those are intentionally vulnerable research fixtures, not release tools.**

| ID | Severity | Original API result | Required boundary |
|---|---|---|---|
| RR-8 | P1 for release packaging | Existing `untracked.txt` is inventoried and zipped despite being outside the source suffix allowlist. | Reject unknown destination entries; build into a clean staging tree; inventory explicit generated/copied paths only. |
| RR-9 | P1 for release packaging | Source `linked.json` dereferences an outside-source file and exports its content. | Reject source and destination symlinks; do not treat a suffix check as confinement. |
| RR-10 | P2 integrity assurance | A ZIP with extra `../PUBLIC-EXTRA.txt` passes `verify_export`; an extra output file also passes. | Require exact exported-file membership and exact safe ZIP membership/content, including duplicate-name rejection. |
| RR-11 | P2 reproducibility | The validation runner names `.txt` logs and their hashes, while the initial export extension allowlist excludes `.txt`. | Export the intended logs and validate every manifest source/table/log reference after packaging. |

RR-10 also covered ZIP metadata: changing a member to a UNIX symlink while
preserving its name and bytes initially passed the repaired verifier. Symlink
member metadata is now rejected. RR-12 concerns the coupled ledger: three
zero-hour holds on zero capacity could each settle a positive $10^{-12}$ hours
because of a per-hold tolerance. Arbitrarily many outstanding holds amplified
that allowance. Settlement now strictly requires actual work not exceed the
individual reservation. The default sweep results were unaffected. The remaining
reservation comparison tolerance is a numerical convention, not exact real-number
arithmetic.

These are relevant even for a research prototype: a clean mathematical model
cannot justify copying unrelated local material into its release, and a correct
source manifest cannot vouch for a different download archive. The findings do
not imply actual secret leakage; only deliberately public sentinels were used.
The narrow disclosure-pattern scanner is correctly described as incomplete.

## Other limits retained

The coupled model knows the true-person mapping for capacity even when control
labels are hidden. That is a simulation oracle, not successful identity recovery.
It does not run or fund audits, enforce institutional authority, schedule real
legal deadlines, measure human utility or authenticate receipts. Its claims make
those exclusions explicit. The initial group lottery, capacity-conditioned panel,
completed population and relied-on population still require distinct denominators.

Executable instructions must identify their working directory. The root
`run_checks.py` is the canonical command from an extracted packet; paths beginning
`papers/07-release-packet/` are repository-checkout commands. Reproducibility is
best checked from the actual ZIP, not inferred from a successful repository run.
A correct export hash is an integrity statement, not adoption of a license,
authorship responsibility or permission to publish.

## Verification status

Original results are recorded in `export-baseline.json` and
`coupled-ledger-baseline.json`; repaired outputs are in `export-repaired.json`
and `coupled-ledger-repaired.json`. All thirteen runtime red regression methods
pass: seven original semantic boundaries, five export boundaries and one coupled
ledger boundary. The test run also passed with `PATH=/nonexistent`, confirming
that this suite does not accidentally require a Pandoc executable. Packaging
unit probes replace only their miniature fixture's renderer with a deterministic
stub; they do not claim to verify Pandoc or visual layout. Actual rendered export
verification is separate.

RR-8, RR-9, RR-10 and RR-12 are repaired and independently regression-tested.
RR-11's exporter and validation-reference checks are implemented; its final
artifact evidence remains conditional on the completed export and extracted-ZIP
run. The main builder now stages generation before replacing a previous candidate.
The collective must not confuse these integrity checks with approval, signing,
legal clearance or a comprehensive secret scanner.

The mathematical lane independently checks coupled distributions, event
accounting and statistical summaries; this lane focuses on API meaning,
packaging and evidence binding. Provisional integration verdict: public release
as a candid, synthetic research seed is appropriate after the final exact export
passes integrity and reproduction checks. No evidence supports treating the
three model engines as one operational service.
