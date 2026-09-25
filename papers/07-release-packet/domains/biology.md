# Biology: a perfect rerun of a nonidentifying experiment

**Research question.** Can a review receipt distinguish a reproducible assay
calculation from an experiment that identifies a biological effect?

**Bounded answer.** Yes as a declared scope distinction, with a small mathematical
counterexample; whether people make better decisions with the interface is untested.
Everything in this case is synthetic. There are no patient records, organisms,
laboratory instructions, clinical decisions, or actual interventions.

## The situation

The invented Birch lab reports that a benign laboratory condition changes an
abstract assay reading by two units. All controls were measured in batch A; all
treated samples were measured in batch B. Its script is public and reproducible.
Three agent teams recalculate the difference and agree. A downstream researcher
wants to rely on the two-unit number to choose which hypothesis to investigate.

The useful first question is not whether the script ran. It is whether treatment
and batch can be separated in the observed design. Reproducible computation is
valuable but can faithfully reproduce a confounded comparison.

This packet draws on established practice rather than inventing reproducibility.
Baggerly and Coombes published forensic analyses with source, intermediate outputs,
and a frozen supplement plus separate corrections. Their supplement is a concrete
prior model for inspectable artifacts; it is not evidence about our invented assay.
[Primary authors' supplement, checked 2026-09-25](https://bioinformatics.mdanderson.org/Supplements/ReproRsch-All/index.html).

## A rank-deficiency result, not a confidence score

Let a synthetic measurement satisfy

$$Y_i=\mu+\beta T_i+\gamma B_i+\epsilon_i,$$

where $T_i\in\{0,1\}$ is treatment, $B_i\in\{0,1\}$ is batch, and the errors
satisfy the conditional-mean assumption $E[\epsilon_i\mid T_i,B_i]=0$ under
the stipulated model. Unconditional mean zero alone is insufficient: for a balanced
binary $T=B$, the error $\epsilon=T-1/2$ averages to zero but has conditional
means $-1/2$ and $1/2$. If $T_i=B_i$ for every observation,
then

$$E[Y_i\mid T_i]=\mu+(\beta+\gamma)T_i.$$

The treatment and batch columns of the design matrix are identical. Only their
sum is identified: $(\beta,\gamma)=(2,0)$ and $(0,2)$ give exactly the same fitted
means. Collecting more samples with the same design reduces some sampling error
but never separates these two explanations. Adding a “batch correction” command
does not create the missing information. This is a linear-model identification
result, not a statement that all real assay problems are linear.

The first fixture has four rows:

| Treatment | Batch | Assay |
|---:|---:|---:|
| 0 | 0 | 9 |
| 0 | 0 | 11 |
| 1 | 1 | 11 |
| 1 | 1 | 13 |

The group means differ by 2, but both parameter explanations above have the same
residual sum of squares, 4. A large significance statistic for the combined
contrast would not identify $\beta$.

A separate synthetic factorial design crosses each treatment with each batch:

| Treatment | Batch | Assay |
|---:|---:|---:|
| 0 | 0 | 10 |
| 1 | 0 | 11 |
| 0 | 1 | 12 |
| 1 | 1 | 13 |

The within-batch treatment differences are both 1. The columns are now linearly
independent and the stipulated additive model identifies $\beta=1$, $\gamma=2$.
The output names this an exact additive-model coefficient, not a causal effect.
For example, the same observed rows arise from $Y=10+2B+U$ with observed $T=U$;
intervening on $T$ while leaving $U$ unchanged has zero effect. Crossed observed
columns alone do not supply randomization, conditional exchangeability, consistency,
or absence of interference.

If the last assay value were 15 instead of 13, the within-batch contrasts would
be 1 and 3. Their equally weighted average is 2, but no single treatment coefficient
fits this noiseless additive model exactly. The oracle reports that average
separately, sets `crossed_exact_additivity` false, and leaves
`crossed_additive_effect` null. An interaction is retained as a finding; it is not
silently renamed additive identification.

This noiseless four-row example has no power analysis or biological validation.
Its purpose is to make the missing comparison visible. Real designs need domain
expertise, replication, noise models, and appropriate ethical review.

## Four receipts and a refusal that helps

| Action | Concrete record |
|---|---|
| Offer `bio-offer-v1` | Birch lab offers `bio-assay-contrast@1`, a synthetic row table and script, scopes `arithmetic` and `additive_model_identification`; asks whether the reported contrast is computed correctly and identifies the treatment coefficient within the declared additive model. Declares batch map as a dependency. |
| Check `bio-arithmetic-v1` | External quantitative reviewer finds mean difference 2 and records `support` for `arithmetic`; excludes treatment identification and real assay validation. |
| Check `bio-design-v1` | Independent design reviewer records `unknown` for the separate additive-model treatment coefficient: treatment equals batch; two parameter explanations fit identically. This is not evidence that the true treatment effect is zero. |
| Rely `bio-rely-v1` | An authorized scientific role accepts the object as a classroom example of a reproducible group contrast, scope `arithmetic`, logical expiry 20. A requested reliance on `additive_model_identification` is rejected by the toy policy because it lacks supporting coverage. |
| Amend `bio-amend-v2` | A corrected offer adds the crossed synthetic design at version 2, explicitly as new data rather than an overwrite. New checks support the additive-model contrast only; the old nonidentification remains in history. |

A single author can supply the table and its limitations. A large collaboration
can supply independently governed measurement and analysis checks, but internal
subteams must disclose common control and shared material. Renaming one lab's
analysis agents does not create independent biological replication.

## Failure and repaired workflow

The failure path treats a reproducible script, many technical replicates, and many
agent reviewers as mutually reinforcing “validation.” Its narrow numerical check
is silently widened into a biological claim. The repaired path asks for the batch
map before broadening reliance. It records an unresolved separate model-coefficient scope, retaining the additional
causal boundary, instead of
rejecting the useful arithmetic work or rewarding a confident invented answer.

The batch map itself may be wrong or incomplete. A false `batch=A` label will pass
a syntactic schema check. An omitted common reagent lot can make apparently
independent assays dependent. The protocol cannot make those facts true. A field
study must independently sample underlying records to assess declaration quality;
using the same declarations as both input and ground truth would be circular.

An amendment to a sample map should reach results that actually use it, not every
paper from the lab. Reuse of a shared check saves effort only when the exact input,
method, and applicability remain valid. A new batch or outcome can invalidate that
reuse without invalidating the old computation.

## Scarce review and the cost of a better question

Give the clinic 6 effort tokens. Arithmetic requires 1, a batch-design check 2,
and an independent interpretation check 2; coordination requires 1. A second
arithmetic rerun consumes attention without resolving the identification defect.
Under these stipulated costs, assigning the design check before a redundant rerun
exposes more of the planted problem. This is a fixture result, not a general
optimizer: real defect risk and review productivity are unknown.

If the only design reviewer belongs to the author lab, the declared independent
coverage is unavailable. The organizer can accept the narrow arithmetic result,
seek another reviewer, or explicitly change the review contract through the proper
authority. It must not mark the causal question covered merely because the queue
is full. Onboarding a novice costs supervisor time and must share that supervisor's
capacity ledger with checking and correction work.

## Human entry and answer key

**Ten-minute entry:** Give participants the first table and ask what the two-unit
difference establishes. Let them draft an ordinary review sentence. Then reveal
that treatment equals batch and ask which words must change.

**Completed four-sentence card:** “I offer the four-row group contrast. I checked
that the means differ by two and that treatment and batch are identical columns.
I would rely on this for an arithmetic example, not a separate treatment effect.
I would reconsider after receiving a design that separates those columns, while
still asking what supports a causal interpretation.”

**Answer key:** “The observed mean difference is two” survives. “Treatment causes
a two-unit difference” does not follow under the declared model. Neither “the
treatment has no effect” nor “batch correction proves the effect” is justified.
The second design identifies a one-unit additive contrast in the noiseless model;
it does not by itself establish causation or biological transport. If the last
cell changes to 15, report contrasts 1 and 3, average 2, and failed exact additivity;
do not report a unique exact additive treatment coefficient.

**Forty-five-minute clinic:** Assign author, quantitative checker, design checker,
and relying researcher. Introduce one hidden sample-map error after the first
reliance. Ask the group to name affected claims and preserve useful unaffected
checks. The facilitator records scope overstatement, time spent on redundant
reruns, and whether uncertainty was honestly retained. Participants may decline a
role or leave a field unknown; fluent completion is not the goal.

## Agent implementation and discriminating tests

The domain oracle calculates both residual sums of squares and the crossed
within-batch contrast using exact rational arithmetic. The domain receipt replay
must produce a supporting arithmetic check, an unknown identification check, a
permitted arithmetic reliance, and a rejected broad reliance. It should then
allow a fresh, appropriately scoped check of version 2.

Benchmark against three policies: arithmetic-only checks; a plain structured
design checklist; and receipt-guided checking with equal total effort. Include a
negative control with treatment crossed across batches, a perfect-confounding
case, partial overlap, and deliberately incorrect metadata. Report sensitivity to
planted nonidentification and false alarms separately; do not reward the receipt
system merely for rejecting everything. Our deterministic oracle covers the two
displayed designs, not the full proposed benchmark.

The decisive human hypothesis is that participants more accurately distinguish
arithmetic, identification, and replication without unacceptable overhead. It is
falsified if the structured checklist does as well with less labor. No patients or
wet-lab work are needed for this initial interface comparison.

## Claim ledger and closest work

| Claim | Type | Support or boundary |
|---|---|---|
| Frozen computational artifacts and correction pages predate MCRP | P | Baggerly–Coombes primary supplement |
| Perfect treatment–batch collinearity prevents separate identification in the additive model | T | Identical design columns; exact fixture |
| Crossed toy design separates the two stipulated effects | T/I | Within-batch differences and tests |
| Scopes can preserve a useful narrow check while withholding a broader use | D/I | Receipt design and toy replay |
| This produces better real replication decisions | H | Unrun human and field comparisons |

The contribution is a teaching workflow around existing statistical reasoning.
It is not a replacement for repositories, laboratory quality systems, ethics
committees, registries, or clinical evidence standards. An implementation must
retain protected-data boundaries; our public fixtures contain only invented rows.
