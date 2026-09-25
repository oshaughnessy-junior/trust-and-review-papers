# Targeted bibliography audit — 2026-09-02

Scope: the two DOI-bearing primary RIFT sources introduced for the documentary
production-system mapping. The two public project-documentation pages were checked
manually because they have no DOI and are mutable `latest` pages.

## Structured identity audit

Command:

```text
python3 audit_refs.py bibliography-audit-input-2026-09-02.json --sleep 0
```

Result:

```text
[OK]         1 (datacite:doi)
[OK]         2 (crossref:doi)

2 ok, 0 fabricated, 0 to check, 0 not found, 0 lookup failed, 2 references
No findings across 2 references.
```

DataCite resolved the RIFT preprint DOI and Crossref resolved the GPU paper DOI
to the cited titles, authorship, years, and venues. The GPU input intentionally
marks its author list as truncated.

## Feature-level support check

- arXiv:1805.10457 identifies RIFT as iterative gravitational-wave parameter
  inference, reports comparison to LALInference, and identifies costly waveform
  models as a motivating use.
- DOI 10.1103/PhysRevD.99.084026 reports GPU translation of parts of RIFT and
  reduced cost and latency.
- The public Overview page separates initial grid, ILE, CIP, iterative feedback,
  and convergence testing.
- The public pipeline page documents HTCondor submit files and a DAG, ILE/CIP
  jobs, iteration logs, consolidated likelihood files, posterior products,
  PSD/grid inputs, and recommended CUDA/CuPy support.

None of these sources supports the fixture's illustrative partition, GPU-hour, or
storage values, and none makes the four synthetic partitions representative. The
mapping and manuscript preserve those exclusions.
