# Targeted bibliography audit — 2026-08-27

Scope: the one new primary dataset citation introduced with the Paper 01 public
R0 implementation observation. This is a targeted identity check, not a renewed
audit of the full bibliography.

## Structured audit result

Command:

```text
python3 audit_refs.py bibliography-audit-input-2026-08-27.json
```

Result:

```text
[OK]         1 (datacite:doi)

1 ok, 0 fabricated, 0 to check, 0 not found, 0 lookup failed, 1 references
No findings across 1 references.
```

DataCite resolved DOI `10.7935/K5MW2F23` to *Data release for event GW150914*,
LIGO Scientific Collaboration, Gravitational Wave Open Science Center, 2016.

## Feature-level source check

The official GWOSC GW150914-v2 event page was checked on 2026-08-27. It identifies
the v2 release and states that the 4-kHz files correct a phase error in the previous
release. The local source manifest records the exact H1/L1 URLs, byte counts,
SHA-256 digests, access date, CC BY 4.0 data license, and the accepted upstream
calibration/data-curation boundary.

This source supports dataset identity and the scientific materiality of selecting
v2. It does not support the local filter/correlation result; that observation is
supported by the attached run and evidence artifacts under claim P01-C015.
