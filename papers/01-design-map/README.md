# Paper 01 — Design map and consolidation

## Maturity

**Private LaTeX first draft; structurally complete, not submission-ready.**

`main.tex` is a coherent critical-design-synthesis manuscript rather than an
expanded outline. Its contribution posture is deliberately bounded to
unification, clarification, operational consolidation, explicit interfaces,
and falsifiable protocol choices. The current page count is recorded by the latest
verification receipt rather than treated as stable manuscript content.

The manuscript includes:

- the rerenderability → repeatability → reproducibility → independent
  replication → scientific-validity ladder;
- claim/evidence, provenance/identity, resources, and governance as separate
  dimensions;
- an R0 portable floor and an HPC/GPU/restricted-data case with explicit
  downselect modes;
- compute, storage, access, platform, wall-clock, human expertise, agent
  capability, operator/support, monetary/allocative cost, and freshness;
- plural root/topic/capability/policy/time-relative trust views with no global
  reviewer score;
- transitive trust boundaries, threat cases, anti-patterns, limitations,
  falsifiers, downgrade rules, and first unmet gates.

Case A now includes a bounded public R0 implementation observation, separate-agent
clean-checkout replay, and non-independent human GW scientific acceptance for the
registered candidate conclusion. Case B now includes a synthetic partitioned-
inference downselect with registered inputs, regenerated digests, nine checks,
six explicitly non-equivalent assessment modes, and a ten-axis distinction between
local and illustrative full-scale resources. It is not representative production
evidence. Neither case is evidence of independent scientific replication, broader
scientific validity, or review-system effectiveness.

## Source and claim artifacts

- `references.bib`: paper-local bibliography containing only cited sources;
- `CLOSEST_WORK_CROSSWALK.md`: dated feature-level primary-source crosswalk v0.2
  covering executable/capture/provenance/archival components plus review-event,
  correction, versioning, bounded linkage review, and inclusion/exclusion decisions;
- `bibliography-audit-input-2026-08-25.json` and
  `bibliography-audit-2026-08-25.md`: structured metadata input and audit
  receipt for the six added peer-reviewed sources;
- `bibliography-audit-input-2026-08-26.json` and
  `bibliography-audit-2026-08-26.md`: clean registrar audit for six DOI-bearing
  standards/primary sources plus manual authoritative-page checks for four web
  specifications;
- `writing-packet.json`: audience, evidence inputs, constraints, exclusions,
  and human questions;
- `claim-ledger.json`: 19 consequential claims with identity/support posture;
- `logical-claims-audit.json`: rhetorical and logical-strength audit.

The local bibliography identity command could not reach external metadata
services because shell DNS was unavailable. It returned 20 `[LOOKUP FAILED]`
records and no adverse identity finding; lookup failure was not treated as
evidence against a citation. Shared-program identity auditing had already
resolved 14 of 17 shared entries, with official ACM and RO-Crate pages handled
as authoritative web/specification records. Additional identifiers introduced
here were checked against primary or authoritative records during this pass.
Semantic support remains distinct from source identity and is recorded in
`claim-ledger.json`.

The 2026-08-25 network-enabled audit of the six new peer-reviewed sources
resolved five cleanly. The Jupyter DOI resolved to the correct work but its
registrar response omitted the named authors; the bibliography retains the
author list verified on the open-access primary paper's title page, and the
adjudication is recorded in `bibliography-audit-2026-08-25.md`.

## Compile

From this directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

Generated build products are ignored. The verified local artifact was
`build/main.pdf`.

## Verification record — 2026-08-24

Commands and results:

```text
map_document.py main.tex
  PASS — 14 sections, 12 subsections, and 4 paragraph anchors mapped.

validate_writing_artifact.py writing-packet.json logical-claims-audit.json
  PASS — both artifacts valid.

validate_claim_ledger.py claim-ledger.json
  PASS — 12 claims valid.

latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
  PASS — 18-page PDF, all targets up to date.

summarize_errors.py build/main.log
  PASS — no critical errors and no summarized warnings.

log scan for Overfull, undefined citations/references, LaTeX Error,
Emergency stop, and Fatal error
  PASS — no matches.

pdftoppm -png -r 110 build/main.pdf ...
  PASS — all 18 pages rendered.
```

Visual inspection covered the 18-page contact sheet and full-resolution pages
10–13, including both evidence-gate blocks, the assessment-mode table, the
two-page threat table, and the anti-pattern list. No clipping, overflow,
broken references, unreadable table content, or malformed page breaks were
observed. Ragged-right table columns were introduced after the first render to
remove excessive interword spacing in narrow columns, then recompiled and
reinspected.

## Verification update — 2026-08-26

The v0.2 standards slice passed document mapping, scientific-writing artifact
validation, claim-ledger validation (14 claims), JSON parsing, repository
validation, bibliography identity audit (6/6 DOI records clean plus four
authoritative web records manually checked), and `latexmk`. The compiled PDF is
21 letter-size pages. The LaTeX summarizer reported no critical errors or warnings;
the explicit scan found no overfull boxes, unresolved citations/references, or
fatal errors. Render inspection covered manuscript pages 6–8 and bibliography
pages 18–21; the added section and new references are readable with no clipping or
malformed page break. `git diff --check` passed.

## Verification update — 2026-08-30

The sanitized HPC downselect passed nine unit and adversarial checks plus clean
replay. Its 21-entry packet index, four source identities, exact ten-axis resource
declaration, and exact six-mode status vector passed repository validation.
Scientific-writing validation passed for 19 ledger claims and 16 logical claims.
The manuscript compiled to a 22-page letter-size PDF with no critical LaTeX errors,
summarized warnings, overfull boxes, unresolved citations, or unresolved references.
Rendered inspection of pages 11–14 covered the case transition, full assessment-
mode table, remaining-evidence gate, and threat-table transition with no clipping or
malformed page break. No external source was added, so bibliography identity and
support artifacts were unchanged and no new bibliography audit was required.

## First unmet gates

1. **G2 evidence complete at the bounded case level:** the GW150914-v2 public R0 release candidate now has registered
   source digests, a locked portable environment, a recorded run, eight positive
   and adversarial checks, a ten-axis resource declaration, claim-scoped evidence,
   trust boundaries, an append-only freshness policy, and a bounded separate-agent
   clean-checkout replay with explicit independence dimensions, plus a
   source-bounded six-decision scientific-review dossier, reusable blank form, and
   human acceptance for exact commit `2495989`, recorded by Codex on behalf of
   R. O'Shaughnessy. The sign-off is not independent and supplies no release
   authorization. Stronger organizational or implementation independence remains
   a distinct possible evidence path.
   Archival identity and repository licensing also remain human-gated.
2. **G3 evidence partially advanced:** the synthetic HPC downselect now has exact
   source identities, executable digest generation and aggregate inference, nine
   positive/adversarial checks, all ten resource axes, all six assessment modes,
   explicit trust boundaries, freshness rules, and bounded machine evidence.
   Independent inspection, representative public or sanitized production mapping,
   measured full-scale resources, and any genuine restricted attestation or
   domain sign-off remain open.
3. **G4 independent review:** obtain separate scholarly-communication,
   computational-science, and governance/privacy close reads.
4. **G5 human release:** resolve AI disclosure, privacy/security review, venue,
   license, fees, and explicit release approval; the requested manuscript byline is
   now recorded.
