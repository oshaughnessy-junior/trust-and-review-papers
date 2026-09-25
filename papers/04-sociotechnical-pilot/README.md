# Paper 04 — Sociotechnical pilot

Working title: **Plural Review Governance in Practice: A Preregistered,
Safety-Gated Pilot of Independent Trust Domains**

Status: private Stage-0 preregistration/protocol first draft. The 14-page LaTeX
manuscript is structurally complete enough for independent ethics, privacy,
security, statistics, qualitative-methods, peer-review, and participating-domain
critique. It is not an approved study protocol, Registered Report, recruitment
instrument, field deployment, or result.

No participant activity, intervention, submission, posting, or release is
authorized. No prose may imply that TDRG is useful, safe, fair, anonymous,
independent, capture-resistant, or effective.

## Contents

- `main.tex` — compile-ready Stage-0 manuscript;
- `references.bib` — paper-local cited sources only;
- `writing-packet.json` — purpose, evidence inputs, constraints, retrieval record,
  missing sources, and excluded claims;
- `logical-claims-audit.json` — rhetorical and logical audit of consequential
  claims;
- `claim-ledger.json` — source-identity/support gate plus four explicitly blocked
  positive field-claim classes;
- `OUTLINE.md` and `CLAIMS.md` — upstream design and full program ledger;
- `VERIFICATION.md` — exact validation, compilation, bibliography, and rendered-PDF
  review record.

## Compile

From this directory:

```bash
mkdir -p build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
python3 "$OPENCLAW_WORKSPACE/skills/read-compile-latex/scripts/summarize_errors.py" build/main.log
mkdir -p build/render
pdftoppm -png -r 120 build/main.pdf build/render/page
```

Generated files under `build/` are ignored.

## Validate semantic artifacts

```bash
python3 "$OPENCLAW_WORKSPACE/skills/scientific-writing/scripts/validate_writing_artifact.py" \
  writing-packet.json logical-claims-audit.json
python3 "$OPENCLAW_WORKSPACE/skills/cite-and-verify/scripts/validate_claim_ledger.py" \
  claim-ledger.json
python3 "$OPENCLAW_WORKSPACE/skills/audit-bibliography/scripts/validate_refs.py" \
  references.bib --style off
```

The bibliography audit requires network access to authoritative metadata services.
The final run found no fabricated identifiers, P1/P2 findings, unresolved works, or
lookup failures. It retained five P3 advisories caused by abbreviated Crossref
metadata for three real DOI records and title-search drift for the official Belmont
and Menlo reports; their identities were checked against publisher or government
sources and are recorded in `claim-ledger.json` and `VERIFICATION.md`.

## Maturity and first unmet gate

The first unmet scholarship gate is a systematic G1 gap audit covering workplace
coercion and retaliation, organizational power, peer-review harms, participatory
governance, qualitative methods, and the eventual scientific domains. G2 then
requires independent methods, statistics, qualitative, ethics, privacy/security,
and domain review before any design parameter is frozen.

The manuscript deliberately leaves participating domains, allocation unit,
co-primary outcomes, sample size or precision target, instruments, privacy
thresholds, and numerical stop bounds unset. Those are human governance and methods
decisions, not blanks an authoring agent may fill.
