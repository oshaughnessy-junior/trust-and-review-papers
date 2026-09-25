# Response to aiXiv review 1588

This packet revises **Small contracts, measurable limits** after the Official Agent
review of aixiv.260925.000007 version1.0. The canonical manuscript is
[math-foundations.md](../07-release-packet/manuscripts/math-foundations.md).
All development and internal adversarial review were conducted within the same
author-directed AI team. The new evidence is synthetic, not an independent field study.

The [response](response-to-review-1588.md) distinguishes assumptions already stated
in the original from new worked examples and clearer theorem statements.
[Formal review](formal-audit.md), [independent internal probes](formal-red-evidence.md),
and [primary-source comparison](related-work-source-audit.md) retain the review trail.

Run from the repository root:

```sh
python3 -m unittest discover -s papers/07-release-packet/models/math -p 'test_*.py' -v
python3 -m unittest discover -s papers/09-review-1588/formal -p 'test_*.py' -v
python3 -m unittest discover -s papers/07-release-packet/models/math/review1588-sensitivity -p 'test_*.py' -v
python3 papers/09-review-1588/formal_red_probe.py
python3 papers/09-review-1588/root_oracle_check.py
```

Build the PDF with Pandoc and a Python environment containing `typst`:

```sh
python3 scripts/build_math_submission.py --output /tmp/review-mathematical-models-v1.1.pdf
```

Prose in this directory is offered under CC BY 4.0; code and synthetic fixtures
under MIT, using [the existing MIT text](../07-release-packet/LICENSES/MIT.txt)
and [CC BY 4.0 terms](https://creativecommons.org/licenses/by/4.0/).
These scoped grants do not alter other licenses or imply scientific endorsement.
The original mcrp-agent-v0.1.0 release remains frozen.

The new `scripts/build_math_submission.py` renderer is also offered under MIT.
The prepared revised PDF is `review-mathematical-models-v1.1.pdf` in this directory;
its aiXiv upload status is recorded separately from the public source release.
