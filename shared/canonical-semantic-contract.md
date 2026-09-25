# Canonical cross-paper semantic contract (private v0.1)

This note is normative for terminology across the private TrustAndReview drafts. It is a drafting contract, not a public standard or validated scientific result.

## Layer boundary

- **MCRP core** governs the machine-verifiable claim/evidence record: claims, evidence, data and software identity, provenance, executions, resource profiles, review events, and scientific dispositions.
- **TDRG** is an optional, separately versioned actor-routing and reliance profile. It remains outside MCRP core conformance until privacy, accountability, interoperability, replay, and empirical promotion gates pass.
- Paper 01 owns the cross-literature design map, interface obligations, epistemic distinctions, and worked design walkthroughs.
- Paper 02 imports the MCRP record as an exogenous input and owns formal observability, dynamics, candidate propositions, A0--A4 comparisons, and future proofs/counterexamples/simulations.
- Paper 03 owns the proposed normative TDRG exchange/profile objects and conformance/evaluation contract.
- Paper 04 owns the ethics-gated independent-actor pilot protocol.

## Canonical reliance view

Use the conceptual signature

```text
V(S, d, z, c, r, q, P, E_{<=tau}, t_eval)
```

where `S` is the relying root set, `d` the trust domain, `z` the topic, `c` the capability, `r` the role, `q` the case/reliance question, `P` the versioned policy/evaluator, `E_{<=tau}` the frozen event cut, and `t_eval` the evaluation clock with `tau <= t_eval`. Separating event cut and evaluation time permits historical replay under explicitly chosen current or historical freshness/expiry rules.

The output is a **reliance view** or **routing feature**, never a scientific verdict, intrinsic actor property, or global trust score.

## Canonical glossary

- **Trust domain:** versioned governance container with declared roots, policies, authorities, and imports.
- **Positive delegation:** scoped input edge; not evidence that its subject is correct.
- **Reliance view:** root-relative computed output under the canonical signature.
- **Routing feature:** non-dispositive numeric or categorical input to assignment/human judgment.
- **Scientific disposition:** claim-level human/review outcome, typed separately from actor reliance.
- **R0 portable-lightweight:** technical resource profile requiring contemporary portable tools, lightweight compute, and no specialty scheduler; not a reproducibility grade.
- **Deterministic replay:** reproducing an evaluator output from a frozen record and policy; not independent scientific reproduction.

## Resource vector and modes

The canonical resource vector is:

```text
(compute, storage, access, platform, wall-time, human-intelligence,
 agent-intelligence, operational-support, financial-cost, freshness)
```

Human and agent resources are reported separately and are not assumed fungible. Technical shorthand `R0`--`R3` is subordinate to the vector.

Canonical assessment modes are:

1. full execution;
2. bounded recomputation;
3. digest audit;
4. restricted-platform witnessed attestation;
5. frozen-output inspection;
6. independent evidence path.

Every non-full mode declares covered and excluded claims. Witnessed execution and bounded recomputation remain distinct because custody and inferential scope differ.

## Bridges and forks

- A bridge is importer-approved and scoped to domains, topics, capabilities, roles, event types, time, and policy.
- Bridges may map credential, capability, review-event, and evidence vocabularies. They may reference MCRP claim IDs but cannot rewrite or promote claims.
- Scientific dispositions, sanctions, and negative standing do not transfer through an ordinary positive-delegation bridge. Transfer requires a separately authorized typed-event mapping and is off by default.
- A fork preserves access to the common public record while changing governance boundary conditions. Private state does not copy by default.
- **Dependency separation/localization** is a replay property. **Capture containment** remains an empirical estimand and must not be stated as established.

## Anonymity boundary

Use **case-scoped public unlinkability against a named observer**, not generic anonymity. Durable private accountability requires an explicitly declared linkage custodian or cryptographic state. Small pools, timing, stylometry, rare expertise, and colluding services remain leakage channels. No current implementation establishes this property.
