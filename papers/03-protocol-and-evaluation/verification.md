# Paper 03 verification record

Date: 2026-08-24

Scope: `papers/03-protocol-and-evaluation/` only
Posture: private first draft; no release or publication approval

## Prototype evidence

Inspected repository: private sibling repository `trust-and-review-tooling`

Revision: `9da0cd433147d925bac4ae1e1f94186cc4166e7b`
Working tree at inspection: `main...origin/main`, clean

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Result: `Ran 11 tests in 0.001s` and `OK`.

Exact passing tests:

1. `test_bridge_is_importer_approved_and_topic_specific`
2. `test_duplicate_event_ids_are_rejected`
3. `test_expected_local_view_and_audit_reasons`
4. `test_future_revocation_does_not_apply`
5. `test_malformed_and_negative_weight_are_rejected`
6. `test_output_is_deterministic_under_event_reordering`
7. `test_view_is_root_relative`
8. `test_view_is_topic_colored`
9. `test_hpc_profile_preserves_axes_and_labels_burden`
10. `test_nonfull_mode_must_declare_excluded_claims`
11. `test_portable_profile_is_level_zero`

The manuscript maps these at subtest level. It does not promote partial coverage
to a full TM row.

## Semantic artifacts

Commands:

```bash
python3 ../../../../skills/scientific-writing/scripts/validate_writing_artifact.py \
  writing-packet.json logical-claims-audit.json
python3 ../../../../skills/cite-and-verify/scripts/validate_claim_ledger.py \
  claim-ledger.json
```

Results:

- `VALID: writing-packet.json`
- `VALID: logical-claims-audit.json`
- `VALID: 13 claims`

## Citation identity and support

- Citation MVF: 7 DOI identities queried; 6 verified in Crossref, 1 Crossref
  not-found because the RO-Crate DOI is registered in DataCite.
- General bibliography audit: 16 entries; 11 clean resolutions, 0 fabricated
  identifiers, 0 authoritative mismatches, 2 metadata checks, and 3 official web
  sources manually verified.
- RO-Crate DOI `10.5281/zenodo.13751027` resolved through DataCite and the official
  RO-Crate 1.2 specification page.
- Claim support, locators, caveats, and blocked claims are recorded separately in
  `claim-ledger.json`.

## LaTeX and rendered PDF

Compile command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

Final mechanical checks:

- compile exit: success;
- PDF: 16 US-letter pages;
- LaTeX error summarizer: no critical errors, no warnings;
- log search: no overfull boxes, undefined citations, undefined references,
  LaTeX errors, emergency stops, or fatal errors;
- all 16 pages rendered at 120 dpi with `pdftoppm`;
- contact-sheet inspection completed, followed by original-resolution inspection
  of the threat table, implementation table, TM matrix, and A0--A4 table;
- no clipping, detached post-bibliography floats, broken citations, or illegible
  table text observed in the final render.

Underfull-box diagnostics remain in narrow table cells and bibliography URLs; they
are cosmetic and do not overflow the page.

## Explicitly unverified

- signatures or attestations;
- identity uniqueness and credential security;
- Sybil/collusion/capture resistance;
- persona anonymity or unlinkability;
- appeals, opening, fork, or reconciliation behavior;
- TM-16 standards round trips;
- TM-17 malicious-document or prompt-injection safety;
- A0--A4 implementation or outcomes;
- field efficacy, reviewer competence, or scientific validity;
- archival release, finalized licensing, or independent rerun.
