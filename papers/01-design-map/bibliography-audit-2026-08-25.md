# Bibliography audit receipt — 2026-08-25

Scope: the six peer-reviewed sources added during the Paper 01 closest-work
crosswalk advance. The audit was run with the structured input in
`bibliography-audit-input-2026-08-25.json` against Crossref and Semantic
Scholar using the local read-only bibliography auditor.

## Machine result

- 5 references: `OK` by DOI metadata.
- 0 fabricated identifiers.
- 0 unresolved lookups after network-enabled rerun.
- 1 `CHECK`: DOI `10.3233/978-1-61499-649-1-87` resolved to the correct
  Jupyter paper, but the registrar record did not expose the named authors in
  the structured audit response.

## Human/source adjudication of the one check

The DOI was not changed. The open-access primary paper title page identifies
Thomas Kluyver, Benjamin Ragan-Kelley, Fernando Pérez, Brian Granger, Matthias
Bussonnier, Jonathan Frederic, Kyle Kelley, Jessica Hamrick, Jason Grout,
Sylvain Corlay, Paul Ivanov, Damián Avila, Safia Abdalla, Carol Willing, and
the Jupyter Development Team. It also prints DOI
`10.3233/978-1-61499-649-1-87`. The paper-local BibTeX therefore retains the
verified named-author list; the audit finding is classified as incomplete
registrar metadata, not an invented author or wrong identifier.

Primary locator used for adjudication:
<https://orca.cardiff.ac.uk/id/eprint/108581/1/9781614996491.pdf>, title page
of the Jupyter chapter (printed p. 87; PDF p. 98), accessed 2026-08-25.

## Commands and exit interpretation

```text
python3 audit_refs.py bibliography-audit-input-2026-08-25.json --sleep 0
  sandbox pass: 6 LOOKUP FAILED because DNS was unavailable; not findings
  network-enabled rerun: 5 OK, 1 CHECK, 0 fabricated, 0 lookup failed
```

The nonzero auditor status reflects the one P2 registrar-author discrepancy.
It is not treated as a clean machine pass; it is closed only for this draft by
the primary-source title-page check above. Semantic support remains separately
recorded in `claim-ledger.json` and `CLOSEST_WORK_CROSSWALK.md`.
