# MCRP: a public-prototype release candidate

Release candidate prepared 25 September 2026. **Not yet published or licensed.**
This packet advances the [prior protocol and hardening work](publication/background.md)
with executable toy agents, domain teaching cases, a second blue/red review cycle,
and a concrete route for public participation. It is a protocol-seeding research
prototype, not an operating review institution or a claim of field efficacy.

## Start with a question

- **What is the idea?** Read [the introductory post](publication/blog-introduction.md).
- **Can we release it?** Read [the release assessment](publication/release-assessment.md).
- **Can I try it without programming?** Follow [the human path](onboarding/human-path.md).
- **Can my agent implement it?** Follow [the implementer path](onboarding/agent-path.md).
- **Where does my discipline fit?** Choose [physics and astronomy](domains/physics-astro.md),
  [biology](domains/biology.md), [economics and social science](domains/economics-social-science.md),
  or [law](domains/law.md).
- **Where can this conversation happen?** See [dissemination](publication/dissemination.md).
- **How does it fit existing work?** Read [positioning and adoption](publication/positioning-and-adoption.md).
- **How would the site launch work?** See [the prepared integration plan](publication/site-integration.md).

The four participant actions remain **offer, check, rely, amend**. They are a
small vocabulary for scoped records and consequences, not four mandatory workflow
stages. Internal team size does not create additional independent authority.

## Evidence and contribution

The proposed contribution is a compact coordination boundary and a set of
falsifiable modeling environments. Prior reproducibility, provenance, research
object, versioning, peer-review and governance methods remain prior work. Code
results demonstrate behavior of the specified toy models. They do not establish
that humans will cooperate, save time, reach correct judgments, or adopt MCRP.

AI agents drafted the material, wrote and ran code, and challenged one another.
All share the same orchestration and accountable operator context. Human
scientific review, independent institutional review, licensing, authorship and
public deployment are separate decisions. See the release assessment for the
exact public candidate boundary.

## Build and release boundaries

The repository is the working source; the public export will contain an explicit
allowlist of this packet and necessary self-contained references. Making the
entire private repository public is not part of this candidate. No credentials,
private correspondence, clinical records, participant identities, or Git history
are needed to run the examples. Domain cases are synthetic.

The publication documents are prepared copy. Outreach drafts are unsent. A
named human or organization must accept responsibility for any public release;
the agent byline discloses contributions and does not confer legal authorship,
institutional sponsorship or scientific authority.

## Reproduce from this packet

From the directory containing this README, including after extracting the download:

```sh
python3 run_checks.py
```

The core suite uses Python 3.9 or later and the standard library, with no network
access or credentials. It regenerates synthetic tables, traces and a validation
manifest. Repository-prefixed commands elsewhere are for the full working checkout;
this command is the portable entry point. Rendering reading pages additionally
requires Pandoc; regenerating optional figures requires Matplotlib. Saved pages
and figures can be read without either. See [reproduction](publication/reproduction.md).

See the [contribution and claim map](CLAIMS.md) for consequential claims, evidence,
review boundaries and what remains hypothetical.

## Research map

Read [the synthesis](manuscripts/synthesis.md) for the argument and the explicit
assumption matrix. Then choose [conditional proofs](manuscripts/math-foundations.md),
[coupled strategic toy agents](manuscripts/coupled-agents.md),
[funded audit delivery](manuscripts/funded-audits.md),
[attention and correction incentives](manuscripts/local-rules.md), or
[the executable boundary](models/agent-framework.md). The
[collective adversarial assessment](reviews/COLLECTIVE.md) preserves findings and
remaining limits. Figures and machine-readable results are included in the packet.
