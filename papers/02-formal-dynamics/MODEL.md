# Model specification: localized trust dynamics for scientific review

Status: candidate formalization; assumptions and results are not yet validated  
Purpose: make the Paper 02 claims precise enough for mathematical analysis and reproducible simulation

**2026-09-25 research extension:** the [hardening dossier](../06-mcrp-hardening/README.md)
checks the conditional influence lemma, exhibits raw-capacity/normalization and
assignment counterexamples, derives a simplified feedback threshold, and adds
resource, incentive and multitype repair models. It does not implement or validate
the full A4 composite below. In particular, a raw max-flow capacity bound does not
automatically establish the normalized transition premise, and a graph-mass bound
does not automatically survive final panel assignment or completion selection.

## 1. Objects and scopes

Let:

- `i, j ∈ A` denote durable private domain accounts, not public reviewer personas;
- `q ∈ Q` denote review requests tied to a claim/evidence release;
- `d ∈ D` denote a versioned governance domain;
- `z ∈ Z` denote a scientific topic;
- `c ∈ C` denote a review capability, such as calibration, inference, numerical reconstruction, provenance, or uncertainty review;
- `r ∈ R` denote a review role;
- `ℓ = (d,z,c,r)` denote one trust layer;
- `τ` denote an event cut and evaluation time;
- `P` denote a versioned policy; and
- `S_ℓ` denote declared trust roots for layer `ℓ`.

The append-only event history `E_{≤τ}` contains signed, typed events: credentials, scoped positive delegations, assignments, review reports, report evaluations, later defect outcomes, conflicts, bridge decisions, sanctions with due process, policy changes, and forks. It does not contain an omniscient reviewer-quality label.

A trust view is

```text
V(S_ℓ, ℓ, q, τ; P) = F(E_{≤τ}, S_ℓ, ℓ, q, P).
```

It returns:

```text
(admissible actors, routing features, exclusions, uncertainty,
 resource feasibility, provenance/explanation, expiry).
```

It must not be interpreted as an intrinsic or universal person score.

## 2. Identity and observation model

Each review case creates a fresh public persona `π_{i,q}`. It is linkable within the case and ordinarily unlinkable to `π_{i,q'}` for `q ≠ q'`. A private accountability service can associate `π_{i,q}` with domain account `i`; a separate registrar can associate `i` with civil identity. The public graph therefore does not contain longitudinal person nodes.

Define observer classes:

- `O_pub`: authors, readers, and ordinary reviewers; see case personas and public events;
- `O_route`: assignment/policy service; sees eligible private handles and policy inputs but not civil identity;
- `O_rep`: reputation custodian; sees domain accounts and private longitudinal outcomes but not civil identity;
- `O_reg`: uniqueness registrar; sees civil identity ↔ domain account but not review text;
- `O_coalition`: a declared coalition of services;
- `O_open`: threshold-authorized identity-opening process.

Any anonymity result must name the observer. A model that joins all persona nodes by construction has assumed away the central privacy problem.

**Non-identifiability statement.** From `O_pub` events alone, person-level longitudinal standing is not identifiable when fresh personas are information-theoretically or cryptographically unlinkable. A public evaluator can score review objects or case personas, but cannot consistently estimate a durable actor parameter without auxiliary linkage information. Timing, prose, rare expertise, or resource signatures are auxiliary information and must be modeled as leakage, not legitimate identifiers.

## 3. Typed positive-delegation graph

For each layer `ℓ`, define a directed graph

```text
G_ℓ(τ) = (A_ℓ, W_ℓ(τ)),    W^ℓ_ij ≥ 0.
```

An edge is a scoped willingness by `i` to rely on `j` for layer `ℓ`, with evidence, limits, and expiry. Expired, conflicted, suspended, or policy-ineligible edges are removed before evaluation.

Negative judgments are not algebraic negative edges. They are source-local route blocks, recusals, challenges, or adjudicated sanctions with scope and appeal. This prevents an “enemy of my enemy” rule and automatic contamination of unrelated neighbors.

Let `T_ℓ` be the row-stochastic transition matrix derived from admissible positive edges. Let `s_ℓ` be a normalized restart distribution supported on declared roots. A basic local routing feature is personalized stationary mass

```text
p_ℓ = (1-α)s_ℓ + α T_ℓᵀ p_ℓ,       0 < α < 1.
```

This is prior-art personalized PageRank used as one routing signal. It is not a scientific disposition and is not, by itself, eligibility.

## 4. Frontier-capacity gate

Before computing or using `p_ℓ`, the proposed A4 arm applies a root-relative capacity gate. Edge capacities `u^ℓ_ij` encode the maximum reliance the source is willing to delegate through that route. An actor is admissible only if it receives sufficient root-relative flow under the frozen policy, possibly with independent-path or control-cluster requirements.

The exact max-flow construction is a profile choice drawn from attack-resistant trust prior art. Paper 02 must not claim the algorithm as novel. The new question is whether applying an explicit frontier budget before reviewer routing limits capture without excessive exclusion in sparse scientific domains.

### Candidate stationary-influence bound

Partition one layer into importer-trusted nodes `H` and an external/adverse region `X`. Assume:

1. restart mass has no support in `X`;
2. from any distribution supported in `H`, at most `ε` transition mass crosses from `H` into `X` after capacity gating; and

3. once in `X`, an adversary may retain all transition mass.

If `x = Σ_{i∈X} p_i`, then

```text
x ≤ α[ε(1-x) + x]
```

and therefore

```text
x ≤ αε / (1 - α + αε).
```

This is a worst-case candidate lemma, not yet a paper result. It must be checked for the actual normalization, dangling-node treatment, multiple roots, bridge composition, and time-varying graph. It bounds stationary routing influence, not actor count, correctness, or collusion by real humans already inside `H`.

## 5. Multicolor layers and explicit bridges

The storage graph is multilayered; inference is single-layer by default. No operation may silently sum or average `W_ℓ` over topics or capabilities.

A bridge from source layer `m` to importing layer `ℓ` is

```text
B_{ℓ←m} = (approver, mapping, evidence predicate, attenuation γ,
           capacity b, maximum eligibility band, expiry, revocation rule).
```

Only the importer can authorize the bridge. Imported candidates normally enter a supervised or onboarding band; bridge import does not transfer scientific dispositions or sanctions.

The bridged transition operator may be represented as a block matrix whose off-diagonal mass is bounded by importer policy. Absent an unexpired `B_{ℓ←m}`, the corresponding block is exactly zero. The stationary-influence bound above can be applied to importer-controlled aggregate bridge mass `ε`, with care for cycles among multiple domains. A chain of bridges should compose using the strictest capacity/eligibility rule and multiplicative or explicitly specified attenuation, never an implicit transitive closure.

An interdisciplinary review request is a coverage contract, for example:

```text
AND(calibration, inference, uncertainty, provenance,
    execution-or-approved-downselect, control-diversity).
```

Satisfaction is a vector or Boolean contract over declared layers. It is not the average of panel reputation.

## 6. Nested domains and fission

Domains have one normative parent and zero or more competency imports. Normative inheritance may supply common event formats, identity/privacy rules, minimum due process, and archival requirements. It does not create a scientific-trust edge.

A domain view has state

```text
Ω_d(τ) = (E_shared≤τ, E_private,d≤τ, S_d, P_d, Bridges_d, Resources_d).
```

A fork at `τ_f` creates `d_a` and `d_b` that reference the same immutable public history through `τ_f` but may choose different roots, policies, bridges, and later events. Private mappings and private trust edges do not copy automatically.

### Structural containment proposition

If `F_d` is deterministic from `Ω_d`, and domain `d_a` neither imports an event class from `d_b` nor accepts a bridge/path controlled by `d_b`, then changes confined to `E_private,b`, `S_b`, or `P_b` cannot change `V_a`. This is dependency separation, not a behavioral theorem: public misinformation, shared infrastructure compromise, off-protocol pressure, or an accepted bridge can still cross the boundary.

### Contamination radius

For a perturbation or attack event set `ΔE`, define a case-level decision distance `δ_q` between the unperturbed and attacked views, such as assignment-set symmetric difference, total-variation distance in assignment probabilities, or eligibility-band change. Then

```text
CR(ΔE; η) = (1/|Q_eval|) Σ_q 1[δ_q(V, V^Δ) ≥ η].
```

Report `CR` by layer, domain, institution/control cluster, newcomer status, and risk class. A low global average can hide complete capture of a small specialty.

Fork localization can be measured by the fraction of shared scientific/review objects preserved, the post-fork contamination radius across the boundary, and the legitimate coverage lost.

## 7. Actor types and latent variables

Simulation may assign latent variables, but evaluation must distinguish them from observables.

For actor `i` and layer `ℓ`, let:

- `θ_iℓ` be latent task competence/calibration;
- `h_i` be intent/type: calibrated, uninformed/miscalibrated, malicious, colluding, or strategic;
- `g_iℓ` be task-specific availability;
- `κ_iq` be conflict/control status;
- `ρ_iq` be resource feasibility;
- `y_iq` be a review action or finding; and
- `o_iq(t)` be delayed evidence about whether a material finding was confirmed, falsified, or unresolved.

Important distinctions:

- A sincere uninformed actor may produce systematically wrong findings without adversarial graph behavior.
- A malicious actor may imitate calibrated behavior until strategically valuable cases.
- A qualified dissenter may disagree with the majority while being correct on a later-confirmed defect.
- A Sybil coalition violates identity assumptions; a coalition of unique humans does not.
- A manager can capture assignment or adjudication without adding any graph nodes.

Review-object votes are noisy observations about usefulness, coverage, or conduct. They are not observations of `θ_iℓ` unless an explicit measurement model justifies that inference.

## 8. Assignment-feedback dynamics

### Individual stochastic model

At round `t`, policy arm `a` produces admissibility `e_iq(t) ∈ {0,1}` and routing feature `v_iq(t)`. Assignment probability is

```text
Pr(i assigned to q at t) ∝ e_iq(t)
  exp[β v_iq(t) - λ workload_i(t) - cost(ρ_iq)]
```

subject to expertise coverage, conflicts, control diversity, resource budget, and a declared exploration floor. `β` controls exploitation of standing. Assignment creates the opportunity to generate future evidence and trust events, so `β` is also a feedback-strength parameter.

Standing updates must separate at least:

```text
report feedback,
later evidence-bearing defect outcomes,
trust delegation,
conduct adjudication.
```

They cannot be collapsed into a single “good/bad review” event without a sensitivity analysis.

### Candidate mean-field specialization

For tractability, divide actors into groups `k` (calibrated incumbents, calibrated newcomers, miscalibrated actors, adversarial coalition, qualified minority). Let `x_k(t)` be the group's share of assignment opportunity or stationary routing mass. Define an exploitation-plus-exploration assignment map

```text
a_k(x) = (1-ζ) exp(βx_k) / Σ_j exp(βx_j) + ζ n_k/Σ_j n_j,
```

where `ζ` is exploration and `n_k` is eligible group size. Let the expected update signal be

```text
u_k(x,t) = (1-χ) d_k(t) + χ social_k(x,t) + attack_k(t),
```

where `d_k` is delayed evidence-bearing performance and `χ` is reliance on contemporaneous social feedback. Define a positive fitness transform and a generic dynamical system:

```text
φ_k(x,t) = exp[ηu_k(x,t)]
ẋ_k = a_k(x) φ_k(x,t) - x_k Σ_j a_j(x)φ_j(x,t) - μ(x_k - x^0_k).
```

The positive transform avoids treating a negative signal as a negative assignment rate, while the centered update preserves total mass when `Σ_k x_k = Σ_k x^0_k = 1`. This is a candidate family, not the final equation; boundary invariance and parameter identifiability still require checking. The analysis should determine when its symmetric or competence-ordered fixed point loses stability as `βχ` grows, how exploration `ζ` changes the threshold, and how separate layers alter coupling. A stochastic reinforced-urn model is the primary alternative if it yields cleaner finite-population results.

### What an analytical result must show

At least one of:

1. a stability/concentration threshold with assumptions and finite-size validation;
2. a bound on sensitivity to root perturbation or bridge capacity;
3. a counterexample proving that localization or capacity gates do not provide the expected containment under realistic overlap/control;
4. a theorem identifying a trade-off between capture resistance and qualified-minority/newcomer coverage.

Reproducing a known preferential-attachment or PageRank transition without a new scientific-review implication is insufficient.

## 9. Resource vector and downselect modes

For every review request `q`, define a required resource vector

```text
r_q = (CPU/GPU, storage, wall time, data access, scheduler/orchestration,
       operational support, human intelligence, agent intelligence).
```

For actor/team `i`, define available capacity `b_i(t)` and capability-specific substitution limits. Human and agent intelligence are not assumed interchangeable. Feasibility is `ρ_iq = feasible(r_q, b_i, access_i, policy)`.

Declared review modes include:

- **L0 portable full path:** documented and runnable with contemporary portable tools on lightweight compute and no specialty scheduler;
- **full high-resource path:** e.g. Condor/HPC, GPUs, large storage, or restricted data;
- **witnessed execution:** independent inspection of a controlled run and its attestations;
- **downselect/digested path:** review of the algorithms and provenance that produced smaller artifacts plus tests on those artifacts;
- **record-only path:** provenance and consistency audit when execution is not feasible.

Every mode changes the set of assessable claims and residual uncertainty. The simulation must not count a cheap downselect as equivalent to full reproduction. Primary cost measures include defect yield per reviewer-hour, agent-hour, GPU-hour, storage-byte-month, and operational-support hour.

## 10. Comparison arms

Use frozen events and tasks across arms:

| Arm | Admissibility/routing | Interpretation |
|---|---|---|
| A0 | credential eligibility + uniform/fair random assignment | minimal baseline |
| A1 | raw report ratings or vote average | popularity baseline |
| A2 | one global recursive score | global mean-field baseline |
| A3 | layer-local personalized restart walk | localized baseline |
| A4 | frontier capacity + local walk + diversity/workload/exploration/resource constraints | proposed composite |

The downstream assignment optimizer must be held constant wherever possible. Otherwise benefits from fair assignment may be incorrectly attributed to trust localization.

## 11. Adversarial and failure regimes

Sweep at least:

- root corruption fraction and root centrality;
- Sybil identities and unique-human colluding coalitions;
- reciprocal positive feedback and coordinated bad-mouthing;
- sincere miscalibration rate and correlated scientific error;
- strategic on/off behavior and whitewashing;
- cross-topic bridge capacity, concentration, and expiry lag;
- institutional/control overlap hidden from the graph;
- manager control over assignment, feedback, or adjudication;
- delayed, censored, or selectively observed defect outcomes;
- sparse layers and rare specialists;
- anonymity leakage from timing, prose, topic rarity, and resource fingerprints;
- stale credentials, dependencies, and reviewer availability;
- forks before and after capture, with selective bridge recognition.

No defense should be evaluated only against Sybils. Unique-human coalitions and captured infrastructure are distinct threat classes.

## 12. Observables and estimands

### Safety and epistemic utility

- false eligibility and false exclusion by layer and actor type;
- confirmed material defects found per resource unit;
- false alarms and unresolved findings;
- qualified-minority survival until adjudication;
- missed-defect rate where planted or later-confirmed labels exist.

### Network and governance

- capture radius `CR`;
- cross-topic/domain leakage without a valid bridge;
- root sensitivity and bridge sensitivity;
- assignment HHI/Gini/entropy and control-cluster concentration;
- effective number of independent reviewers;
- fork localization and record preservation;
- challenge, appeal, reversal, and correction latency.

### Inclusion, privacy, and cost

- newcomer wait and supervised-review burden;
- effective anonymity-set size and persona-linkage precision/recall per observer;
- human intelligence, agent intelligence, compute, storage, wall time, access, and support costs;
- coverage lost under capacity limits and fission.

Report distributions and subgroup results, not only averages.

## 13. Identifiability and causal limits

The following are not identifiable from the trust graph alone:

- unique personhood;
- scientific competence or honesty;
- independence of two graph paths;
- correctness of a review;
- whether disagreement is error, specialization, or qualified dissent;
- whether a missing review reflects low quality, scarce resources, exclusion, or restricted access.

Editorial acceptance, author satisfaction, majority agreement, review helpfulness votes, prestige, and citation counts are not ground truth. Later defect confirmation is also selectively observed and affected by which work receives further attention. Empirical studies therefore need planted defects, randomized audits, explicit missingness models, or bounded claims. Simulation results establish behavior under the simulator assumptions, not real-world effectiveness.

## 14. Minimum result and stop rules

The minimum credible paper needs:

1. a checked analytical result or informative impossibility/counterexample;
2. deterministic implementations of A0–A4 with identical frozen inputs;
3. adversarial sweeps including captured roots, unique-human coalitions, miscalibrated actors, and management manipulation;
4. layer, subgroup, privacy, and multiaxis resource outcomes;
5. negative regimes where A4 harms coverage or does not improve capture;
6. reproducible seeds, environments, graph snapshots, parameters, and result manifests.

Do not claim the composite policy is superior if it fails to reduce capture in its target regimes, if newcomer/minority exclusion exceeds the preregistered bound, if bridge imports bypass importer consent, or if the result depends on an unobservable quality oracle.
