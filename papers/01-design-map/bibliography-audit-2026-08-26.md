# Paper 01 bibliography and source audit — 2026-08-26

Scope: the ten new bibliography records supporting the v0.2 review-event and
correction/supersession crosswalk. Identity verification is distinct from semantic
support; claim-level support is recorded in `claim-ledger.json` as P01-C014.

## Registrar audit

Command:

```text
python3 audit_refs.py bibliography-audit-input-2026-08-26.json
```

Result:

```text
[OK] 1 (crossref:doi) — ANSI/NISO Z39.106-2023
[OK] 2 (crossref:doi) — Event Notifications in Value-Adding Networks
[OK] 3 (crossref:doi) — NISO RP-8-2008 JAV
[OK] 4 (crossref:doi) — NISO RP-45-2024 CREC
[OK] 5 (crossref:doi) — ANSI/NISO Z39.96-2024 JATS 1.4
[OK] 6 (datacite:doi) — DataCite Metadata Schema Documentation 4.7

6 ok, 0 fabricated, 0 to check, 0 not found, 0 lookup failed.
```

The first pass flagged the valid JAV DOI because the shortened local title did not
match the registrar's full title. The bibliography and audit input were corrected
to the registrar title; the DOI was not changed. The clean result above is from the
second pass.

## Authoritative web/specification records

The remaining four records were manually checked against their authoritative
owners on 2026-08-26:

| Record | Authoritative locator | Checked identity/scope |
|---|---|---|
| COAR Notify 1.0.1 | <https://coar-notify.net/specification/1.0.1/> | current version heading; Linked Data Notifications transport; ActivityStreams payloads; review workflow patterns |
| DocMaps Framework Overview, release 7 | <https://docmaps.knowledgefutures.org/pub/sgkf1pqa/release/7> | release identity; immutable process assertions; provider/consumer model; stated non-goals |
| Crossref peer-review metadata | <https://www.crossref.org/documentation/schema-library/markup-guide-record-types/peer-reviews/> | supported review objects, roles, stages, rounds, recommendations, and required `isReviewOf` relation |
| Crossmark | <https://www.crossref.org/documentation/crossmark/> | publisher-maintained status/update function; checked with the linked update-registration and versioning guidance |

Additional feature-level checks used the official JATS 1.4 pages for
`related-article-type` and `article-version`, the DataCite 4.7 relation-type list,
the NISO CREC landing page and recommended practice, and the official NISO JAV
revision page. The draft JAV revision was excluded from normative mapping.

## Adjudication

No identity defect remains in the added records. The sources authorize the narrow
interoperability statement in P01-C014: complementary terminology, transport,
process, registration, status, serialization, and identifier relations exist.
They do not authorize a claim of exhaustive coverage, system effectiveness,
reviewer competence, scientific validity, or novelty. Those stronger propositions
remain outside the claim or blocked.
