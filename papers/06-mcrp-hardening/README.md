# MCRP hardening and modeling dossier

Private research draft, 25 September 2026. This dossier develops the existing
publication program; it is not a new adopted protocol or a sixth promised journal
paper. Authorship, independent human review, legal applicability, and public
release remain unapproved.

## Read in this order

1. [Integrated position](SYNTHESIS.md): the proposed small protocol and the joint
   constraints on its operation.
2. [Minimal profile](protocol/minimal-profile.md): offer, check, rely, amend;
   worked individual and collaboration paths; explicit unknowns and currentness.
3. Specialist working manuscripts:
   - [Economics](manuscripts/economics.md): attention, allocation, incentives and funding.
   - [Game theory](manuscripts/game-theory.md): effort, audit credibility, coalitions and resets.
   - [Law and operations](manuscripts/legal-operations.md): bounded contestability and rights.
   - [Scientific dynamics](manuscripts/scientific-dynamics.md): influence, feedback and repair.
   - [Compositional science](manuscripts/compositional-science.md): multitype correction work.
   - [Frontier critique](manuscripts/frontier-critique.md): failures between graph and assignment.
4. [Collective red-team report](reviews/COLLECTIVE.md) and
   [author responses](reviews/ADJUDICATION.md). Individual reports and original
   objections are retained under `reviews/red-team/`.

The claim/source packets are in `specialists/`. All numerical results are
synthetic or analytical; no human study or real-world trust outcome was measured.
Separate specialist and adversarial agents share this orchestration and operator.
They do not constitute external peer review or a diversity-of-models experiment.

## Reproduce

From the repository root, with Python 3.9 or newer and no third-party runtime
packages:

```sh
python3 papers/06-mcrp-hardening/run_checks.py
```

The runner executes meaningful equation, counterexample, currentness, capacity,
allocation and adversarial tests, then regenerates synthetic tables. It records
source/data hashes and environment in `results/validation.json`. It does not run
the hosted Commons application or certify its security. The separately hardened
`trust-and-review-tooling` branch has its own tests and audit report.

Optional reading copies use ReportLab and Pandoc:

```sh
python3 papers/06-mcrp-hardening/rendering/build_reading_copy.py /path/to/output-directory
```

This produces a four-page PDF brief, a standalone MathML HTML dossier, and a
standalone collective-review reading copy. The source Markdown remains canonical.

## Scope of evidence

- Analytical results are conditional derivations, mostly applications of
  established probability, optimization, queueing and repeated-game methods.
- Simulations diagnose those chosen models and include negative outcomes. They
  are not calibrated to a research population and are exploratory, not preregistered.
- The small reference boundary projection uses trusted facts and synthetic clocks;
  it provides no signature, identity, live freshness or legal decision service.
- The existing local-trust evaluator uses maximum decayed path products, not the
  stationary restart walk in the mathematical paper.
- A4 trust routing, cryptographic privacy, external interoperability, completed-panel
  fairness, uptake and institutional independence remain unestablished.

Source lineage is recorded in `SOURCE_LINEAGE.json`. No live deployment or public
website change is part of this dossier.
