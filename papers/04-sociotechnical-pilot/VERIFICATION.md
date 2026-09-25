# Paper 04 verification record

Date: 2026-08-24 (America/New_York)

Scope: private Stage-0 LaTeX protocol and semantic writing artifacts only. This
record does not verify ethics approval, study feasibility, intervention fidelity,
participant safety, privacy, anonymity, fairness, domain independence, or field
efficacy.

## Structural and semantic validation

- `map_document.py main.tex` found 16 top-level sections plus 8 subsections and the
  three appendices; the argument runs from rationale through staged methods,
  outcomes, privacy, analysis, stopping, reproducibility, promotion, and limits.
- `validate_writing_artifact.py writing-packet.json logical-claims-audit.json`
  returned `VALID` for both artifacts.
- `validate_claim_ledger.py claim-ledger.json` returned `VALID: 16 claims`.
- Four high-consequence claims remain explicitly blocked: real-community efficacy,
  anonymity, safety/enforceability, and operational domain independence.

## Bibliography identity audit

Command:

```bash
python3 "$OPENCLAW_WORKSPACE/skills/audit-bibliography/scripts/validate_refs.py" \
  references.bib --style off
```

Final network-enabled result: 13 references; 8 `OK`; zero fabricated identifiers,
P1/P2 findings, unresolved works, or lookup failures. Five P3 advisories remain:

- Crossref returns abbreviated title strings for the real DOI records for
  Bratteteig and Wagner, the NIST Privacy Framework, and Brennan et al.; the full
  titles and DOI identities were checked on Springer, NIST, and ACM-facing records.
- The no-DOI official Belmont and Menlo documents produce title-search year drift;
  their identities were checked on HHS and DHS/government-hosted source pages.

These advisories are metadata-tool limitations, not support verification. Claim
support and scope are recorded separately in `claim-ledger.json`.

## LaTeX compilation

Command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

Result: success, 14 letter-sized pages. `summarize_errors.py build/main.log`
reported no critical errors and no LaTeX/package warnings. The log contains only
underfull-box typography notices in narrow table cells; there are no overfull boxes,
undefined citations, or undefined references.

Final verification digests after cross-paper integration of the canonical MCRP/TDRG
boundary and event-cut/evaluation-clock language:

- `main.tex`: `00d7aec3ae0ba1526cfa74f6085d51d98ce766d9d240249520bc303146b3e5a5`
- `build/main.pdf`: `32bc968a2a81b0657a309389a102bd24b767a9987d84a7d827c8e532a9fb3e06`

## Rendered-PDF inspection

`pdftoppm -png -r 120 build/main.pdf build/render/page` produced 14 page images.
All pages were inspected as a contact sheet, with pages 1, 7, 12, and 14 inspected
at page resolution. Checks covered:

- page-1 private-draft banner and explicit no-results/no-deployment language;
- outcome-table continuation and column containment;
- gate-status table wrapping and pre-enrollment checklist;
- bibliography completion and long-URL wrapping;
- clipping, overprinting, missing glyphs, broken citations, excessive blank pages,
  and margin overflow.

No visual blocker was found. The gate table's first column was widened after the
first inspection to remove severe heading hyphenation; the manuscript was then
recompiled and page 12 re-inspected.

## Human gates still open

- G1 systematic literature gap audit and domain-specific scholarship;
- G2 independent statistics, qualitative-methods, ethics, privacy/security, and
  scientific-domain review;
- written IRB/ethics determination and final approved protocol;
- participating-domain selection, agreements, and control-graph audit;
- frozen intervention, deployment manifest, instruments, estimands, precision,
  sample size, privacy thresholds, and stop bounds;
- independent appeal, incident, adjudication, and safety operators;
- human authorship, AI-assistance disclosure, venue, licensing, submission, and
  release authorization.

No recruitment, participant work, external contact, commit, push, publication, or
submission occurred in this work unit.
