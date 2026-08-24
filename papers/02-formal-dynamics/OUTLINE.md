# Paper 02 outline: Formal dynamics of localized trust domains

Status: theory package for internal development; not submission-ready  
Primary contribution type: formal consolidation, comparative analysis, and falsifiable design evaluation  
Default venue class: network science / computational social science  

## Working title

**Trust Without a Global Score: Localized, Typed, and Forkable Reviewer Networks**

Alternative, if the analysis supports a sharper claim:

**Containing Reputation Capture in Multidomain Peer-Review Networks**

## One-sentence thesis

When reviewer standing affects future assignments, a single recursively computed reputation couples otherwise distinct scientific communities and can amplify prestige, mistakes, or capture; root-relative topic-and-capability views with importer-bounded bridges and forkable policies can localize that influence, but only under explicit assumptions and at measurable costs to coverage, newcomer access, privacy, and reviewer intelligence.

## Contribution boundary

This paper does **not** claim to invent graph reputation, personalized trust, multilayer networks, Sybil resistance, fair reviewer assignment, anonymous reputation, polycentric governance, or decentralized peer review. Those are prior work.

The candidate contribution is narrower:

1. formalize reviewer reliance as a root-, topic-, capability-, policy-, and time-relative view rather than an actor property;
2. join endogenous reviewer-assignment dynamics to typed trust layers, explicit importing bridges, nested governance, and domain fission;
3. define contamination, authority leakage, qualified-minority survival, and fork localization in a common model;
4. compare global reputation, local personalized trust, and capacity-bounded local trust under malicious, uninformed, captured, and resource-constrained regimes; and
5. identify when localization helps, when it merely fragments the reviewer pool, and when no graph method is identifiable from available outcomes.

The defensible verbs are **synthesize**, **formalize**, **separate**, **bound**, **compare**, and **evaluate**. Avoid **first**, **solves trust**, **proves reviewer quality**, or **guarantees correctness**.

## Research questions

- **RQ1 — Feedback:** Under what assignment/endorsement feedback regimes does a global reviewer score concentrate opportunities or become sensitive to roots and early stochastic events?
- **RQ2 — Localization:** When do topic-and-capability-local views reduce capture radius and cross-topic authority leakage relative to a global recursive score?
- **RQ3 — Bridges:** What importer-side capacity, attenuation, and expiry rules bound influence imported from another trust domain while retaining useful interdisciplinary coverage?
- **RQ4 — Fission:** When can a domain fork localize a captured root or policy while preserving shared scientific and review records?
- **RQ5 — Heterogeneous actors:** How do malicious actors, sincere but poorly calibrated actors, qualified dissenters, Sybils, real-human coalitions, and institutional controllers differ in their observable effects and appropriate defenses?
- **RQ6 — Anonymity:** Which quantities remain computable when public reviews use fresh, unlinkable case personas and durable standing is available only to separated private services?
- **RQ7 — Resources:** How do compute, storage, access, time, support, and human/agent intelligence constraints change reviewer eligibility, evidence quality, and the apparent performance of a trust policy?
- **RQ8 — Limits:** Which latent properties cannot be identified from review votes, editorial outcomes, or graph structure without delayed defect evidence and independent audits?

## Paper structure

### 1. The scaling problem is actor governance, not record storage

- Begin with a claim-level machine-verifiable scientific record whose provenance is already preserved.
- Show why a corpus also needs reviewer routing, accountability, disagreement, and exit.
- Motivate the dangerous loop: standing → assignments → observed review outcomes → standing.
- State that graph position routes scarce attention; it does not establish scientific validity.

### 2. Prior work and the remaining gap

Organize by mechanism, not chronology:

- global recursive trust and pre-trusted roots: EigenTrust;
- observer-relative/local trust: personalized PageRank, Massa–Avesani;
- attack-frontier bounds: Levien–Aiken and later Sybil defenses;
- hierarchy and feedback dynamics: endorsement/visibility models including Kawakatsu et al.;
- multilayer and multiplex networks: Boccaletti et al. and successors;
- fair, randomized, and collusion-aware reviewer assignment: PeerReview4All and related work;
- anonymous/accountable reputation: Naessens et al., AnonRep, anonymous credentials;
- decentralized peer-review systems: Rodriguez et al., DecSci, decentralized knowledge assessment;
- nested/polycentric governance: Ostrom and later institutional work.

End this section with a closest-work matrix. The gap is not an absent component; it is the absence of a common model connecting typed reliance, assignment feedback, importer-approved bridges, fork containment, anonymity, and resource costs for scientific review.

### 3. Formal object: a scoped reliance view

Define the immutable event history, actors/domain accounts, fresh case personas, scientific topics, review capabilities, roles, domains, roots, policies, and evaluation time. Define

```text
V(R, D, K, Q, τ; P) = F(E≤τ, R, D, K, Q, P)
```

as an expiring, reproducible answer to a reliance question. `V` returns an admissible set, routing signals, exclusions, uncertainty, resource requirements, and an explanation—not a public universal leaderboard.

### 4. Five comparison families

- **A0:** verified eligibility plus random assignment; no longitudinal reputation.
- **A1:** raw review-object votes or average ratings.
- **A2:** one global EigenTrust/PageRank-like recursive score.
- **A3:** layer-local personalized restart walk from declared roots.
- **A4:** layer-local walk after frontier-capacity gating, followed by control-diversity, workload, exploration, and resource-feasibility constraints.

Use the same cases, events, assignment opportunities, seeds, and latent actor types across arms. Apply a common fair/randomized assignment method after each arm determines admissibility.

### 5. Endogenous standing and assignment dynamics

- Introduce a minimal stochastic reinforcement model in which standing affects visibility and future assignments.
- Separate latent task competence from observed review feedback, confirmed defect outcomes, and social approval.
- Derive the stability or concentration threshold of a tractable mean-field specialization.
- Show sensitivity to early events, conformity, assignment exploitation, and root quality.
- Add exploration/newcomer quotas and compare their distributional cost.

### 6. Multicolor trust and importer-approved bridges

- Store a multilayer graph; evaluate one declared topic × capability × role layer at a time.
- Prohibit implicit averaging of colors.
- Model an importing bridge as a directed, versioned, expiring operator with attenuation and capacity chosen by the importer.
- Prove a simple upper bound on imported stationary influence when the importer controls transition mass across the boundary.
- Treat interdisciplinary review as a coverage contract across layers, not the mean score of a panel.

### 7. Nested domains, capture, and fission

- Distinguish normative parentage from competency import.
- Define root capture, policy capture, bridge capture, and management-controlled assignment.
- Define contamination radius as the set or mass of unaffected-domain decisions that materially change after an adverse event set.
- Model a fork as shared immutable events plus independent roots, policies, bridges, and private actor mappings.
- Establish the structural containment result: without an importer-approved path, a fork's private trust events cannot alter another fork's view.
- Measure what is lost: reviewer coverage, cross-domain reach, calibration, and privacy-set size.

### 8. Accountable anonymity changes the observable graph

- Public case personas are fresh and unlinkable across reviews.
- Durable domain accounts and longitudinal evidence exist only inside separated private services.
- Model ordinary observers, service coalitions, and threshold identity-opening authorities separately.
- Show that public persona graphs alone cannot identify person-level longitudinal reputation.
- Report anonymity-set degradation from rare specialty, timing, prose, and resource signatures.

### 9. Resource-constrained review

Represent each reproduction/review path by a resource vector rather than a one-dimensional level:

```text
(compute, storage, wall time, access, orchestration, support, human intelligence, agent intelligence)
```

- Level 0 corresponds to documented, portable, lightweight execution without specialty schedulers.
- Higher-cost paths may require Condor/HPC, GPUs, restricted data, large storage, scarce experts, or substantial agent supervision.
- A downselect or digested product is a declared review mode with its own claims, algorithms, provenance, and residual uncertainty—not a silent substitute for full reproduction.
- Compare policies under fixed resource budgets and report defects found per reviewer-hour as well as false inclusion/exclusion.

### 10. Experiments and adversarial regimes

Use synthetic multilayer networks first, followed only later by consented/sanitized empirical calibration. Predeclare:

- honest calibrated experts, calibrated newcomers, narrow specialists;
- sincere but systematically mistaken actors;
- qualified dissenters whose findings are confirmed late;
- Sybils, coordinated real humans, reciprocal-voting rings, and whitewashing actors;
- malicious or captured roots, managers, registrars, assignment services, and bridge approvers;
- sparse topics, correlated institutional control, expensive/restricted review paths, and stale outcomes;
- forks created before and after capture.

### 11. Results

Required minimum:

1. one analytical result for feedback stability/concentration or a rigorously justified negative result;
2. one analytical influence bound for importer-controlled bridges or a counterexample showing why the proposed bound fails;
3. a reproducible phase diagram across global/local/capacity-bounded arms;
4. capture, leakage, minority, newcomer, anonymity, and resource-cost outcomes with uncertainty;
5. regimes where localization is worse than the simpler baseline.

### 12. Discussion and no-go conclusions

- No model proves honesty, personhood, independence, or scientific validity.
- Root choice and bridge approval are governance boundary conditions.
- Sparse domains may pay unacceptable exclusion and privacy costs.
- Confirmed defects arrive selectively and late; observational evaluation is confounded.
- Forks contain authority, not misinformation in shared public records or social influence outside the protocol.
- A null result still supports a useful interoperability vocabulary; it does not support superiority claims.

## Planned figures

1. **Architecture schematic:** shared event substrate beneath multiple root-relative domain views.
2. **Feedback loop:** standing, assignment, review, delayed evidence, and standing update.
3. **Multicolor bridge diagram:** topic layers, importer-side capacity, and coverage contract.
4. **Phase diagram:** concentration/capture versus feedback strength, exploration, and frontier capacity.
5. **Contamination map:** changed assignments after root, bridge, or management capture.
6. **Trade-off frontier:** capture reduction versus false exclusion, newcomer delay, privacy, and intelligence cost.
7. **Fork experiment:** common record, diverged policies, preserved and crossing influence.

## Planned tables

1. Prior-art boundary and residual contribution.
2. Formal notation and observability.
3. Comparison arms and assumptions.
4. Threat regimes and which safeguard addresses each one.
5. Primary observables, estimands, and failure thresholds.
6. Resource profiles and downselect modes.
7. Claims, evidence status, and allowed language.

## Minimum publishable result

The paper is mature enough for submission only if it has all of the following:

- a tractable formal model with declared assumptions and at least one nontrivial analytical result or counterexample;
- faithful global, local, and capacity-bounded baselines;
- preregistered synthetic attacks including captured roots and real-human coalitions, not merely Sybils;
- explicit subgroup harms and operational/intelligence cost;
- reproducible code, seeds, graph snapshots, environment, and negative results;
- a closest-work audit showing that the contribution is consolidation and comparative theory;
- no superiority claim if the proposed arm does not materially outperform simpler arms in its declared target regimes.

A protocol narrative plus illustrative simulation is not enough.

## Venue strategy

Default targets are **Network Science** or **Peer Community Journal** through an appropriate PCI route. **Physical Review E** is plausible only if the paper produces a genuine statistical-physics contribution such as an analytic transition, phase diagram, and robust empirical or generative validation. A short **PNAS** paper is an exceptional hook only if a clean, general result survives beyond peer review—for example, a theorem or well-supported universality result connecting localized boundary conditions to capture containment in adaptive reputation networks. PNAS is not the default home for the full framework.

## Dependencies and gates

- Literature audit must be updated immediately before submission.
- The protocol paper must freeze semantics for domains, bridges, roots, and forks.
- The tooling repository must implement deterministic policy replay and all comparison arms.
- Any human-data calibration requires ethics/privacy review and consent.
- Venue fee/waiver and RIT agreement eligibility must be checked at submission time.
