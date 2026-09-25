# Targeted bibliography audit — 2026-08-29

Scope: the three primary GW papers used to prepare the Paper 01 R0 qualified-human
scientific-review dossier. This is a targeted identity and feature-level support
check, not a renewed audit of the full bibliography or a human scientific review.

## Structured audit result

Command:

```text
python3 audit_refs.py bibliography-audit-input-2026-08-29.json --sleep 0
```

Result:

```text
[OK]         1 (crossref:doi)
[OK]         2 (crossref:doi)
[OK]         3 (crossref:doi)

3 ok, 0 fabricated, 0 to check, 0 not found, 0 lookup failed, 3 references
No findings across 3 references.
```

Crossref resolved the discovery paper DOI
`10.1103/PhysRevLett.116.061102`, the GW150914 detector-characterization paper
DOI `10.1088/0264-9381/33/13/134001`, and the LVC data-guide DOI
`10.1088/1361-6382/ab685e` to the cited titles, lead author, year, and venue. The
input marks the thousand-author collaboration lists as intentionally truncated.

## Feature-level source check

- The discovery paper, Figure 1 caption and pp. 061102-2--4, supports the
  35--350 Hz visualization context, approximately 0.2-second signal duration,
  measured 6.9 ms delay, 10 ms H1--L1 light-travel scale, and orientation-driven
  inversion. It does not validate the packet's exact local statistic.
- The LVC data guide, Sections 4 and 10.2, shows a different whitened, tapered,
  eighth-order zero-phase filtering recipe, labels the narrow passband as
  visualization-only, and shows correlation sensitivity to time window and
  bandpass. This supports leaving the local fourth-order, unwhitened path and
  exact 820-sample window for human judgment.
- The detector-characterization paper, Sections 5.2 and 6, supports the
  search-specific role of quality vetoes and documents checks beyond public
  event-time flags. It prevents the dossier from treating bit-mask success as a
  fresh calibration or detector-validation audit.

The undated official GWOSC technical-details and O1 release pages were manually
checked on 2026-08-29 for bit definitions, one-second granularity, cumulative
categories within an analysis family, and family-specific injection exclusions.
They have no separate DOI and are cited as authoritative web documentation with
access dates. The source-to-decision mapping is recorded in
`cases/r0-gw150914-strain-lag/scientific-review-dossier.json`.
