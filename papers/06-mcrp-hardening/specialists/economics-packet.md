# Science packet: The scarce resource is a warranted judgment

Status: private working draft; no publication authorization or human sign-off. Prepared 2026-09-25.

## Question and answer

**Question:** How can a versioned, locally governed review commons allocate scarce qualified attention without converting wealth, popularity, or internal team size into scientific authority?

**Answer supported:** Bounded tasks, explicit resource and uncertainty budgets, payment-independent authority, and capacity-aware allocation expose important failure modes; conditional allocation and incentive models identify design constraints, while effectiveness and fairness remain untested.

## Contribution table

| Category | Content | Scope |
|---|---|---|
| Established prior art | Concave allocation/KKT; queue workload and Little's law; effort incentives; peer prediction; polycentric governance | No novelty claimed |
| Inherited repository design | Version-bound claim/contract/evidence/release decisions; plural scoped trust; private accountability and fresh case personas; resource vector; explicit bridges; A0–A4 comparisons | TDRG and formal model already contain these |
| Synthesis | Treat attention, appeals, repair, and recognition as distinct scarce goods; separate eligibility, allocation, and scientific disposition | Analytical framing |
| Design choice | Shared offer/check/rely/amend interface; bounded lot and bundle; exploration allocation; independent common/campaign accounting; fixed fee and bounded process audit | Proposed, not validated |
| Formal result | Water-filling solution; irreducible detection floor; effort/participation inequalities; coverage infeasibility; parameterized workload and sponsor-runway identities | Elementary conditional derivations; not new general theorems |
| Counterexample | Sponsor attention capture despite payment-independent verdicts; fragmentation; complementarity defeating coordinate-greedy allocation; agreement equilibrium | Explicit small constructions |
| Implementation result | One deterministic arithmetic check of the worked example | No allocator or service implementation asserted in manuscript |
| Human/field evidence | None generated | Primary external experiment cited narrowly; no transfer claim |

## Claim ledger

| ID | Type | Consequential statement | Evidence | Boundary |
|---|---|---|---|---|
| EC01 | D | Review lot binds object, boundary, effort, deliverable, remainder | Sections 1–2 | Interface proposal |
| EC02 | T | Separable exponential benefit yields water filling | Section 3 KKT proof | Known fixed parameters; divisible hours; independent additive benefits |
| EC03 | T | Detection floor is pLb | Section 3 limit | Same review method; modeled error class |
| EC04 | D/H | Exploration can protect opportunity and learn neglected value | Section 3; E1/H3 | No fairness/efficiency guarantee |
| EC05 | T | Complementary capability model defeats coordinate-greedy initialization | Section 4 product model | Deliberate counterexample |
| EC06 | T | Fewer independent eligible control groups than required implies infeasibility | Section 4.1 cardinality proof | Independence classification assumed correct |
| EC07 | P/T | Stable queues relate load, time, occupancy; rho<1 workload condition | Section 5; Little primary paper | rho≤1 is necessary non-overload; strict slack neither universally necessary nor universally sufficient |
| EC08 | T | Automation changes load by factor kr | Section 5 substitution | Unchanged human capacity and included cost boundary |
| EC09 | T | Effort iff q(d0-d1)F≥c in stated utility model | Section 6 difference in payoffs | Risk neutrality; fixed conditional loss F≤Fmax; exogenous credible auditing; bounded process only |
| EC10 | T | Constant matching reports can be an equilibrium | Section 6 two-reviewer example | Naive agreement payment only |
| EC11 | P | Multi-task mechanisms give conditional information/effort incentives | Dasgupta–Ghosh; Shnayder et al. | Abstract-level bibliographic verification; do not import unexamined theorem details |
| EC12 | P | Turnaround responds to incentives in one journal experiment | Chetty et al. working-paper record | Does not identify MCRP validity effects |
| EC13 | P | Replication incentives can create overturn bias | Galiani et al. working-paper record | Does not establish all challenges are biased |
| EC14 | T | Sponsor submissions halve unsponsored expected lottery slots in example | Section 7 hypergeometric expectation 20×100/200 | Equal eligibility; fixed common capacity |
| EC15 | T | Sponsor withdrawal runway B/g under fixed remaining finances | Section 7 budget identity | No adjustment, insurance, or replacement revenue |
| EC16 | T | Per-claim guaranteed hours reward splitting | Section 8 k-fold representation example | Rule lacks deduplication/bundle constraints |
| EC17 | H | Bounded review lowers cost without losing coverage | H1 pilot | Unmeasured |
| EC18 | H | Scoped status reduces unwarranted inferences | H2 pilot | Unmeasured |
| EC19 | D | No public durable reviewer score or default persona linkage | TDRG inherited design; section 1.1 | Privacy claims require implementation-specific threat model |
| EC20 | H | Funded campaigns add rather than displace capacity | H4 pilot | Revenue is not additionality evidence |

## Closest-work matrix

Primary-source checks made 2026-09-25. This is a narrow conceptual comparison, not an exhaustive systematic review.

| Work | Shared concern or machinery | What this paper adds or changes | What cannot be claimed |
|---|---|---|---|
| Ostrom, 2009 lecture | Locally governed common resources | Applies resource accounting to scoped scientific review and separate operational queues | No deduction that MCRP will self-organize successfully |
| Little, 1961 | Throughput, waiting, system size | Places moderation, scientific time, and repair into review workload accounting | No general waiting-time forecast from Little's law alone |
| Dasgupta & Ghosh, 2013 | Unobserved effort and information elicitation | Declines automatic agreement scoring; narrows auditable compensation to process tasks | No improvement over their mechanism or proof of universal truthfulness |
| Shnayder et al., 2016 | Multi-task correlated information and uninformative strategies | Explains why heterogeneous scientific boundaries need assumptions beyond a payment formula | No impossibility of all peer-prediction applications |
| Chetty et al., 2014 | Review timing and incentives in a randomized field setting | Proposes separate cost/coverage outcomes in an MCRP pilot | No causal transfer of reported effects |
| Galiani et al., 2017 | Incentives surrounding replication and overturns | Requires false-alarm and unresolved-finding denominators in challenge evaluation | No equation of replication with malicious criticism |
| Repository formal dynamics, revision 18deff4 | Scoped graph eligibility, frontier bounds, local routing, resource vectors | Explicit attention objective, queue load, funding displacement, bundle gaming, impossible coverage | No claim to invent plural trust, scoped personas, or exploration |

## Methods, negative controls, and stops

Paper section 9 gives E1–E4 exact experiment families; section 10 gives H1–H5 pilot estimands. Use common frozen task/event inputs across A0–A4; retain the same allocator when comparing trust mechanisms. Include a sponsor-label permutation negative control: labels alone must not alter eligibility or disposition on identical evidence. Add an all-zero detection-productivity negative control: numerical optimization must not report information benefit. Test duplicate claim representations against bundle accounting. A no-automation arm anchors the load model.

Synthetic seeds reveal algorithm behavior under the declared generator, not uncertainty over the real scientific world. Report between-seed intervals with their interpretation, all sweep cells, and code/config hashes. Stops: observed privacy leakage, inability to handle appeal deadlines, missing authorization, unusable specialist capacity, or unsupported transfer of a result to a stronger review mode. Stop expansion rather than silently weakening the contract.

## Reproducibility and sign-off status

- Baseline source repository revision: `18deff4993fca5a30cc2aff2e4f6e4433c6ff391`.
- Manuscript file: `paper.md`; companion source record: `SOURCE_NOTES.md`.
- Checked deterministic numerical illustration using Python standard-library `math`; no randomness, network, datasets, or numerical optimizer were used for that check.
- Checked values: eta=0.9251678148440968; h=(2.3803652294655615,1.5418546340629224,0.07778013647151594); total=4.0; benefit=11.299328740623613.
- E1–E4 implementation/runs: planned, not represented as completed here.
- G0/G1/G2: author self-check only; closest-work coverage remains bounded.
- G3: deterministic arithmetic checked; full experiment artifact pending.
- G4: independent critique required; parent integration/review does not by itself establish scientific validity.
- G5: human authorship, venue fit, licensing, ethics, and release approval not recorded.
