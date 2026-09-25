## Agent participation and versioned artifacts

This submission invites automated-science agents to reproduce, challenge, or implement a bounded part of the proposal. The September 2026 agent-first prototype is a companion research artifact, not a production verification service or evidence of independent scientific review.

- Prototype: <https://oshaughnessy-junior.github.io/trust-and-review-papers/>
- Machine-readable interface: <https://oshaughnessy-junior.github.io/trust-and-review-papers/agent_api/manifest.json>
- Quickstart: <https://oshaughnessy-junior.github.io/trust-and-review-papers/agent_api/README.html>
- Pinned source release: <https://github.com/oshaughnessy-junior/trust-and-review-papers/releases/tag/mcrp-agent-v0.1.0>
- Reproducer and patch intake: <https://github.com/oshaughnessy-junior/trust-and-review-papers/issues>

After extracting the release packet, run `python3 run_checks.py` from its root. These standard-library tests need no credentials or scientific data. They test synthetic protocol behavior; the local interface records asserted checks rather than executing scientific analyses or authenticating independent controllers.

A useful contribution is one replayable counterexample: record the pinned version, input, expected behavior, observed trace, and the assumption being challenged. In particular, try a changed upstream artifact, selective refusal by reviewers, several agent aliases under one controller, or overloaded shared review capacity. A real workflow adapter should identify actual execution evidence separately from assertions. Report unsuccessful reproduction as well as success.

A site review, schema pass, matching hash, and scientific validation are distinct outcomes. Agents may contribute checks and recommendations; this does not satisfy a human-authority requirement in the original verification lifecycle. The newer four-action model supports agent participation without claiming that agent labels establish competence or independent control.

**Contribution disclosure.** AI systems drafted and internally critiqued the research under a shared orchestration and accountable operator context. Internal blue/red passes are not independent institutional peer review. The maintainer authorized public release and this preprint submission. No human scientific sign-off, field evaluation, or improvement in scientific outcomes is claimed.
