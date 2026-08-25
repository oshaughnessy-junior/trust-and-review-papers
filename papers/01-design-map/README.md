# Paper 01 — Design map and consolidation

## Maturity

**Private LaTeX first draft; structurally complete, not submission-ready.**

`main.tex` is a coherent critical-design-synthesis manuscript rather than an
expanded outline. Its contribution posture is deliberately bounded to
unification, clarification, operational consolidation, explicit interfaces,
and falsifiable protocol choices. The compiled document is 18 pages including
approximately three pages of references (roughly 15 substantive manuscript
pages).

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

The worked cases are design walkthroughs, **not implementation results**.

## Source and claim artifacts

- `references.bib`: paper-local bibliography containing only cited sources;
- `CLOSEST_WORK_CROSSWALK.md`: dated feature-level primary-source crosswalk
  covering the first bounded part of G1;
- `bibliography-audit-input-2026-08-25.json` and
  `bibliography-audit-2026-08-25.md`: structured metadata input and audit
  receipt for the six added peer-reviewed sources;
- `writing-packet.json`: audience, evidence inputs, constraints, exclusions,
  and human questions;
- `claim-ledger.json`: 13 consequential claims with identity/support posture;
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

## First unmet gates

1. **G1 scholarship:** extend the dated source-locator crosswalk from executable
   publication, continuous analysis, workflow/capture, provenance, and archival
   identity into review-event exchange/correction standards and backward/forward
   citation chaining; record inclusion/exclusion decisions and rerun metadata
   audits. The 2026-08-25 v0.1 crosswalk is a bounded advance, not gate closure.
2. **G2/G3 evidence:** instantiate immutable R0 and public/sanitized HPC case
   packets with runs, negative tests, resource measurements, and bounded
   sign-offs.
3. **G4 independent review:** obtain separate scholarly-communication,
   computational-science, and governance/privacy close reads.
4. **G5 human release:** resolve authorship responsibility, AI disclosure,
   privacy/security review, venue, license, fees, and explicit release approval.
