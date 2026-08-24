# Claim register: Paper 02 formal dynamics

Status: pre-evidence claim discipline  
Rule: proposed mechanisms and candidate lemmas are not results until the cited analysis, code, and verification artifacts exist

## Claim matrix

| ID | Candidate claim | Current status | Required evidence | Main prior-art / preemption risk | Falsifier or downgrade condition | Allowed wording now |
|---|---|---|---|---|---|---|
| C01 | Reviewer reliance is better represented as root-, topic-, capability-, role-, policy-, and time-relative than as one intrinsic global score. | Design thesis | Formal semantics; motivating counterexamples; comparison with local/global trust literature; stakeholder/pilot evidence later | Personalized PageRank, local trust, topic-sensitive rank, multilayer networks already establish most components | Local views add no decision-relevant information or create unacceptable fragmentation/cost | “We formalize and evaluate a scoped reliance view.” |
| C02 | Global score → assignment → feedback dynamics can amplify early prestige, social agreement, or captured-root effects. | Plausible; not shown for TDRG setting | Stability/concentration analysis; finite-size simulations; sensitivity to roots and initial conditions | Endorsement hierarchy, preferential attachment, PageRank feedback, and Matthew-effect literature | Effect disappears under realistic assignment and delayed-outcome models, or is no worse than local arms | “We test when global recursive routing produces concentration and root sensitivity.” |
| C03 | Topic/capability-local evaluation reduces cross-topic authority leakage relative to a collapsed global graph. | Partly true by construction; utility untested | Explicit definition of leakage; faithful global/local baselines; interdisciplinary coverage and false-exclusion results | Topic-sensitive ranking and multilayer inference are established | Legitimate coverage collapses, implicit proxies recreate coupling, or global baseline performs equally under matched constraints | “Explicit layer separation prevents unapproved graph transitions by construction; we evaluate its practical trade-offs.” |
| C04 | Importer-approved capacity-limited bridges bound the stationary influence imported from an external domain. | Candidate lemma | Checked proof under declared transition/restart assumptions; cyclic/multibridge counterexamples; simulation | Max-flow trust and Markov-chain perturbation bounds are established | Normalization, cycles, internal collusion, or hidden control defeats the bound | “Under stated assumptions, importer-controlled transition mass implies an upper bound on imported routing mass.” |
| C05 | Capacity gating plus local routing contains bounded-frontier attacks better than local routing alone. | Hypothesis | A3 versus A4 adversarial experiments across sparse/dense layers, Sybils, and real-human coalitions | Levien–Aiken and Sybil-defense literature | Equal/worse capture radius or unacceptable qualified-actor exclusion | “We compare a prior-art capacity gate composed with local routing against local routing alone.” |
| C06 | Forkable policy overlays can localize root or governance capture while preserving a common scientific/review record. | Structural design claim; behavioral value untested | Dependency proposition; deterministic policy replay; fork simulations; record-preservation and coverage metrics | Polycentric governance, forks, append-only logs, and decentralized systems | Private/captured events alter the other view without an accepted dependency, or necessary shared services remain a single capture point | “We formalize fork-local views and test containment and coverage costs.” |
| C07 | Fresh per-case personas are incompatible with public person-level longitudinal reputation unless auxiliary linkage information is introduced. | Strong conceptual/privacy claim | Observation model and non-identifiability argument; privacy literature comparison | Anonymous reputation and credential systems already analyze related trade-offs | A public protocol derives durable reputation while preserving the stated unlinkability against the same adversary without auxiliary linkage | “Public unlinkability removes the identifier required for public longitudinal aggregation; any such aggregation must introduce a linkage boundary or stronger private computation.” |
| C08 | Votes on reviews cannot be treated as ground truth for reviewer competence or scientific correctness. | Supported boundary claim | Peer-review agreement and review-rating literature; measurement model; delayed defect fixtures | Established peer-review reliability/bias literature | None for the absolute boundary; a validated task-specific proxy could support a narrower inference | “Review feedback is a typed noisy observation, not a correctness label.” |
| C09 | Malicious, uninformed, dissenting, Sybil, colluding, and institutionally controlling actors require distinct models and controls. | Taxonomic/design claim | Threat model; simulations with separable actor types; failure analysis | Security, peer-review bias, and institutional-governance literatures cover components | Model cannot distinguish the types observationally or proposed controls respond identically | “We separate threat classes that graph-only evaluations often conflate.” |
| C10 | Localization has a capture-resistance versus coverage/inclusion/privacy trade-off, especially in sparse specialties. | Hypothesis | Phase diagrams; subgroup metrics; anonymity-set and newcomer analyses | General security-usability and community-fragmentation trade-offs | No measurable trade-off over realistic regimes, or an alternative dominates | “We quantify the trade-off rather than assuming localization is beneficial.” |
| C11 | Human and agent intelligence are first-class review resources alongside compute, storage, time, access, orchestration, and support. | Framework contribution | Resource schema; calibrated cost model; sensitivity analysis; real workflow case later | Human-in-the-loop, computational reproducibility, and cost-accounting literatures | Resource axes cannot be measured reproducibly or add no explanatory value | “We model review feasibility using a multiaxis resource vector.” |
| C12 | Declared downselect/digested review modes can preserve assessability of some claims when full reproduction is infeasible, but must carry reduced scope and residual uncertainty. | Protocol-linked thesis | Formal mode semantics; representative HPC/restricted-data workflows; defect-detection comparison | Reproducibility tiers, audit/witness, and executable-paper prior art | Downselect provenance is unverifiable or reviewers systematically overgeneralize its conclusions | “We distinguish full reproduction from declared lower-resource evidence paths and evaluate what each can support.” |
| C13 | The composite A4 policy improves defect-oriented routing without unacceptable exclusion, privacy, or operational cost. | **Unsupported primary empirical claim** | Preregistered experiments and later consented pilot | Fair assignment, graph trust, and decentralized review systems are strong baselines | Any no-go threshold is crossed or simpler arms match performance | Do not assert. Say only “A4 is the proposed arm under evaluation.” |
| C14 | The framework generalizes beyond scientific peer review. | Speculative | Cross-domain formal result and external validation | Broad trust/reputation literature likely preempts generic claims | Result depends on peer-review-specific outcome or governance assumptions | Do not claim unless a clean general theorem/result emerges. |

## Prior-art boundary

The paper must explicitly credit as established:

- recursive/global reputation and pre-trusted roots (e.g. EigenTrust);
- personalized and observer-relative trust;
- topic-sensitive ranking and multilayer network representations;
- root-relative max-flow/capacity defenses and their assumptions;
- fair, randomized, and collusion-aware reviewer assignment;
- anonymous credentials and anonymous-but-accountable reputation;
- repository-mediated and decentralized peer review;
- polycentric and nested governance;
- append-only records, attestations, and provenance standards.

The residual contribution is the **scientific-review-specific consolidation and evaluation** of these pieces around claim-level evidence, endogenous assignment, typed competencies, importer control, fork containment, private per-case anonymity, and multiaxis resources.

## Candidate formal results

### R1 — Imported stationary-mass bound

If restart mass is wholly importer-local, importer policy caps honest-to-external transition mass by `ε`, and an external region may retain all mass, then the candidate upper bound is

```text
p(external) ≤ αε / (1 - α + αε).
```

Before use, verify edge cases, dangling nodes, cyclic bridges, multiple imports, and correspondence between flow capacity and transition mass. This is likely a useful lemma, not by itself a sufficient paper contribution.

### R2 — Feedback stability or concentration threshold

Derive a threshold in a tractable assignment/standing model showing when symmetric or competence-ordered allocation becomes unstable as exploitation and social-feedback strength increase, and how exploration changes the threshold. The result must be distinguished from known reinforcement/preferential-allocation results by a reviewer-routing implication or new typed-domain comparison.

### R3 — Fork dependency separation

Show that a deterministic local view cannot change under events that are not in its declared dependency closure. This is a protocol dependency proposition. Its empirical value depends on whether real deployments avoid shared-service capture and covert coupling.

### R4 — Trade-off or impossibility result

Seek a result showing that, under sparse expertise and unlinkable personas, stronger locality/capacity constraints necessarily trade capture resistance against coverage, newcomer delay, or anonymity-set size. A clean result here could be more important than claiming A4 wins.

## Primary estimands

- capture radius after root, bridge, manager, or coalition perturbation;
- cross-topic authority leakage;
- false eligibility and false exclusion by topic and actor type;
- qualified-minority survival until evidence-bearing adjudication;
- assignment concentration after control/institution clustering;
- newcomer waiting time and supervision burden;
- material defects found per human-hour, agent-hour, compute unit, and support hour;
- persona linkage precision/recall and effective anonymity set by observer;
- fork record preservation and cross-fork influence;
- deterministic policy replay from frozen events.

## No-go thresholds

Downgrade the work to a vocabulary/interoperability paper, or report a negative result, if:

- the proposed composite has equal or greater capture radius than the global arm in declared target regimes;
- newcomer or qualified-minority exclusion exceeds a preregistered bound;
- authority crosses a topic/domain boundary without importer approval;
- policy replay is nondeterministic from frozen inputs;
- claimed anonymity requires an undeclared linkage service or fails for ordinary observers;
- evaluations rely on agreement, acceptance, or a hidden omniscient quality oracle;
- resource costs make the safeguards fictitious for the claimed deployment class;
- a fork cannot preserve the shared public record or depends on a captured common operator.

## Evidence discipline

- Every result claim must link to a fixed experiment manifest, code revision, environment, data/graph digest, parameters, seeds, and verification artifact.
- Analytical claims require a checked proof or a clearly labeled conjecture plus counterexample search.
- Simulation claims are conditional on the generative model.
- Human-data claims require consent, privacy review, and an explicit missingness/selection analysis.
- Negative and subgroup results must be reported; global averages are insufficient.
- Neither graph score nor review vote may be described as proof of scientific validity.

## Venue-dependent claim posture

- **Network Science / Peer Community Journal:** emphasize the formal model, phase diagram, sensitivity, and network/governance trade-offs.
- **Physical Review E:** only if there is a substantial analytic/statistical-physics result with finite-size and robustness analysis.
- **PNAS:** only as an exceptional short hook if a clean, general result survives outside the application—for example a broadly applicable containment or phase-transition theorem. Do not target PNAS for the framework narrative alone.

