# Verification — Paper 02 formal dynamics

Date: 2026-08-24

Scope: `papers/02-formal-dynamics/` only
Status: passed for a private, pre-results theory/model first draft

## Deliverable checks

- `main.tex`: present; 5,947 source words; 16 compiled pages.
- `references.bib`: present; 12 cited primary or canonical works.
- `writing-packet.json`: present and valid.
- `logical-claims-audit.json`: present and valid.
- `claim-ledger.json`: present and valid, with unsupported consequential claims blocked.
- `README.md`: compile instructions, maturity, claim posture, and first unmet gates recorded.
- No theorem is described as proved.
- No simulation, pilot, field result, phase diagram, or comparative policy result is described as completed.
- Candidate propositions, open hypotheses, planned experiments, actual-results status, and no-go rules are explicitly separated.
- Evidence-gate blocks guard the central scientific claim, novelty, anonymity, baseline fidelity, feedback result, bridge proposition, fission, actor controls, resource calibration, simulation, all result language, and field interpretation.

## Semantic artifact validation

Commands:

```bash
python3 "$OPENCLAW_WORKSPACE/skills/scientific-writing/scripts/validate_writing_artifact.py" writing-packet.json logical-claims-audit.json
python3 "$OPENCLAW_WORKSPACE/skills/cite-and-verify/scripts/validate_claim_ledger.py" claim-ledger.json
```

Results:

```text
VALID: writing-packet.json
VALID: logical-claims-audit.json
VALID: 10 claims
```

## Bibliography identity audit

Command:

```bash
python3 "$OPENCLAW_WORKSPACE/skills/audit-bibliography/scripts/validate_refs.py" references.bib --profile astronomy
```

Result: 11 references resolved automatically as `OK`; no fabricated, authoritatively mismatched, unresolved, or lookup-failed identifier was reported. The validator marked `stelmakh2021peerreview4all` as `CHECK` because its title search found the 2018 preprint while the bibliography cites the canonical 2021 JMLR version. The JMLR primary record was inspected directly and confirms Ivan Stelmakh, Nihar B. Shah, and Aarti Singh, volume 22, article 163, pages 1–66, 2021. The flag is publication/preprint year drift, not an identity conflict.

The two P4 page-range warnings (`1--122` for the Physics Reports review and `1--66` for the JMLR article) were checked against their canonical records and retained as real page ranges.

## LaTeX compilation

Command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
python3 "$OPENCLAW_WORKSPACE/skills/read-compile-latex/scripts/summarize_errors.py" build/main.log
```

Results:

- `latexmk`: exit 0; target up to date.
- PDF: `build/main.pdf`, 16 US-letter pages.
- Critical LaTeX errors: none.
- Summarized warnings: none.
- Undefined citations or references: none.
- Overfull boxes: none after wrapping the coverage-contract equation.
- Remaining underfull boxes are limited to narrow table/bibliography line breaking and do not clip or overlap content.

## Rendered-page inspection

Commands:

```bash
pdftoppm -png -r 110 build/main.pdf build/rendered/page
montage build/rendered/page-*.png -thumbnail 360x -tile 4x4 -geometry +8+8 build/rendered/contact-sheet.png
```

All 16 pages were inspected in the contact sheet. Pages 3, 6, 8, and 12–16 were also inspected at original rendered resolution because they contain dense related-work prose, comparison tables, equations, the longtable continuation, evidence-gate page breaks, notation, and references. No clipping, overlap, broken citation, malformed equation, unreadable table, or orphaned heading was observed. Evidence-gate color and the draft-status box render legibly.

## Content audit

A search for result-like phrases found only prohibitions such as “not a demonstrated improvement” and “must not be called superior.” The Results section contains artifact requirements and figure specifications only, not mock outcomes.

The manuscript explicitly covers:

- root-relative multicolor trust and prohibited implicit color averaging;
- importer-approved, versioned, expiring, capacity-limited bridges;
- nested domains, dependency closure, capture surfaces, fission, and contamination radius;
- malicious, sincere-miscalibrated, qualified-dissenting, Sybil, unique-human-coalition, and institutional-controller actor classes;
- fresh case personas and observer-specific anonymity observability;
- A0–A4 comparison arms under a common downstream assignment stage;
- epistemic, inclusion, governance, concentration, privacy, and multiaxis-resource observables;
- portable, high-resource, witnessed/bounded, digest/provenance, and record-only review paths;
- no-go regimes and explicit negative-result posture.

## Digests

```text
3fbb3ca9f64e330af7cb40ce974f8dacc4ad79db6e57c587e19dca7ca0c66331  main.tex
7f333f1dd1ac34e78e89d700f881fc5cf5c2dfeac483346a5b9ef1f083430ced  references.bib
63ca7cd7166fb5dffad63bdcb900a101613f8121bdcc1e235e092b940c41d5e4  writing-packet.json
362d0cdae3e1f383035e49ffebf59d019a263427c578541b3c6a032f5d55eea0  logical-claims-audit.json
5ffd13795357080858da8aa484d38a6ed660352a8c368706352eb2a5ff22dd75  claim-ledger.json
278f69f776cb1b229378b02a015163cd3743711c3ab41baa7da872c85d63e4d1  build/main.pdf
```

The PDF digest is a generated verification artifact; generated build products remain ignored and uncommitted.

## First unmet evidence gates

1. Check Candidate Proposition 1 against the exact bridge transition and normalization semantics, including cyclic bridge composition and counterexample search.
2. Define machine-readable dependency closure and replay tests for Candidate Proposition 2.
3. Establish the state space and analyze the feedback model, or replace it with a better tractable family.
4. Implement faithful A0–A4 baselines and preregister synthetic adversarial/resource experiments.
5. Obtain independent mathematical, security/privacy, scientific, and human governance review before any public claim or submission.
