# Scientific argument packet

Status: draft prepared with AI assistance; no human scientific sign-off, authorship approval, external peer review, or release approval recorded.

## Research question and intended answer

**Question:** Under which explicit behavioral and institutional assumptions can a small, version-bound review protocol sustain careful contribution without converting popularity or resource abundance into scientific authority?

**Answer:** Scoped commitments can support effort when reliable discrimination, credible auditing, continuing value, and bounded identity/coalition influence satisfy the derived incentive constraints; these conditions can fail even when integrity and local graph checks pass.

## Contribution table

| Category | Contribution | Evidence/status |
|---|---|---|
| Established prior art | Repeated-game incentives; Sybil problem; peer-prediction alternatives and failure equilibria; prestige mechanisms | Primary-source references in paper; bounded descriptions |
| Existing repository design | Plural local roots, layered delegation, frontier capacity, bridges, forks, private domain accounts, due-process outcomes | Paper 02 MODEL and TDRG v0.1 draft; no novelty claimed |
| Synthesis | Connect effort, inspection, identity reset, coalition payoffs, and common-mode errors to a version-bound review contract | Argument, not empirical efficacy |
| Protocol choice | Four shared actions; principal representation invariance; scoped correction history; post-selection influence checks | Proposed extension; not adopted |
| Formal result | Imperfect-monitoring effort inequality and absorbing-state value; inspection equilibrium; specified coalition comparison | Equations and explicit derivations in paper |
| Formal result | Tight stationary mass bound under normalized leakage; raw-capacity, shared-flow, and softmax counterexamples | Frontier supplement plus deterministic fixtures |
| Implementation result | Standard-library executable numerical and invariant checks | Run artifact created with `python3 model_checks.py`; only mathematical fixture validation |
| Human/field evidence | None | Efficacy, usability, entry fairness, privacy and capture resistance unresolved |

## Consequential claim ledger

| ID | Label | Claim | Support and boundary |
|---|---|---|---|
| G1 | D | Offer/check/rely/amend can serve as a minimal participant interface | Design hypothesis; usability experiment required |
| G2 | T | g ≤ (beta-alpha)[F+delta(V-W)] deters the specified one-step deviation | Direct payoff subtraction; not whole-game equilibrium |
| G3 | T | Formula (2) gives continuation gap in an absorbing two-state model | Bellman algebra; checks include alpha>0 and F>0 |
| G4 | T | Finite terminal interaction can remove reputation incentive | Counterexample; excludes intrinsic and external consequences |
| G5 | T | Inspector mixed equilibrium q=g/S, x=a/B | Indifference conditions; interior assumptions stated |
| G6 | T | Coalition comparison requires joint deviation gain and incremental expected losses | Additive transferable utility assumption; not coalition-proof theorem |
| G7 | P/T | Identity multiplication undermines redundancy; cheap reset reduces continuation loss | Douceur plus original reset calculation |
| G8 | T | Agreement-only payment supports costless all-pass equilibrium | Explicit two-reviewer counterexample |
| G9 | T | Shared failure creates rho floor in unanimous-error model | Mixture law; synthetic parameters |
| G10 | H | Useful repair/status can improve cooperation | Prestige literature motivates, does not validate this platform |
| G11 | H | Paid discovery can indirectly influence eventual authority | Proposed causal evaluation, not observed result |
| F1 | T | Normalized cross-boundary leakage yields stationary bound | Inequality and tight two-state construction |
| F2 | T | Raw tiny capacity can normalize to unit transition | Two-node counterexample |
| F3 | T | Independent per-target flow tests can reuse one frontier budget | Root–broker–candidate cut argument |
| F4 | T | Small total stationary mass can coexist with near-unit assignment share | Softmax multiplicity and case-conditioning examples |
| F5 | D | Final distribution should enforce cluster caps or fail with uncovered capability | Implementable proposal; real cluster identity remains uncertain |
| P1 | I | Fixture script calculations agree with stated formulas | Deterministic run report; no user or network measurement |

## Closest-work matrix

Primary source records checked 2026-09-25. This is a targeted comparison, not a completed systematic literature review; G1 scholarship remains provisional until a broader nearest-work review, including trust-flow algorithms, is completed by the integrating manuscript.

| Work | Shared feature | Different scope / what is not imported |
|---|---|---|
| Fudenberg & Maskin 1986, Econometrica; author MIT bibliography | Repeated interaction can sustain multiple incentive patterns | Bibliography verified; PDF retrieval failed; no exact folk-theorem conditions imported or novelty claimed |
| Douceur 2002, The Sybil Attack, Microsoft author record | Independence cannot be inferred from distinct identities | This paper adds case-scoped reviewer/control consequences, not a new Sybil defense |
| Shnayder et al. 2016, Informed Truthfulness in Multi-Task Peer Prediction, arXiv:1603.03151 | Eliciting useful information without direct truth labels | Their multi-task assumptions/guarantees are not established for MCRP |
| Gao, Wright & Leyton-Brown 2016, Incentivizing Evaluation via Limited Access to Ground Truth, arXiv:1606.07042 | Effort costs, low-cost coordination, spot checking | Their task model is not proof that scientific adjudication supplies unbiased ground truth |
| Henrich, Chudek & Boyd 2015, The Big Man Mechanism, Phil. Trans. R. Soc. B, PMC4633849 | Prestige and cooperation as modeled mechanisms | No reduction of scientific refereeing to dominance, no validated platform status design |
| Existing MCRP Paper 02 MODEL and TDRG draft | Root-local trust, private accountability, capacity and final assignment | Present work supplies strategic games and counterexamples connecting currently separated stages |

## Methods, negative controls and stopping

The paper proposes budget-matched unstructured/scoped/scoped-plus-audit arms and seeded flaws. Negative controls include an impeccable-looking record with a planted scientific gap, additional reviewers sharing one planted failure, disagreement on a genuinely unresolved question, and a legitimate sparse specialty behind a single broker. Adversarial cases are enumerated in the frontier supplement and paper section 9. Report errors and confidence intervals at the responsible-principal/task level; do not treat correlated internal agents as independent observations. Pilot exposure, effect sizes and stopping thresholds must be fixed before collecting confirmatory data; they are not fabricated here.

## Reproducibility and release limits

The fixture script uses only Python's standard library, no external data or randomness. It records runtime version, configuration, results, and SHA-256 of the script in `model-checks.json`. Compute is a local negligible single-process deterministic calculation. Repository commit and final integrated artifact hashes must be recorded by the integrator; scratch paths are not public provenance. References are public; no private identity or review corpus was copied. Independent review, human authorship approval, and venue requirements remain pending. This packet is not a deployment authorization.
