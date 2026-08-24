---
artifact_role: bounded-research-synthesis
authors: [Codex, junior]
status: working-draft
date: 2026-08-24
question: How can MCRP scale from trustworthy records to a corpus reviewed by independent, unequal, sometimes adversarial actors?
claim_posture: source-facts-separated-from-design-inference
publication_status: private-not-approved
---

# Reviewer trust, anonymity, and domain governance

## Research judgment

MCRP should not adopt a global reviewer score, a raw vote, or one consensus
graph. The defensible design is:

> one interoperable event history; one typed, privacy-protected multilayer
> graph; many local trust views computed from declared roots for a particular
> topic, review capability, policy, and time.

Graph trust can help route work, bound the influence of weakly connected
coalitions, and make trust dependence explicit. It cannot establish scientific
truth, unique human identity, independence, or misconduct. Those claims bottom
out in identity issuers, domain institutions, evidence, and accountable human
processes.

Per-review unlinkability also creates a hard systems constraint. If observers
cannot link two reviews to the same person, they cannot compute a public
longitudinal reputation for that person. A practical first deployment must use
an independent private linkage service, or relax unlinkability, or implement
substantially more complex zero-knowledge/MPC state. MCRP should state that
tradeoff rather than promise “anonymous reputation” without a trust boundary.

## 1. Why a universal score is unsafe

### Global recursive reputation is useful prior art, not the target

[EigenTrust](https://nlp.stanford.edu/pubs/eigentrust.pdf) turns local
satisfactory/unsatisfactory transactions into one global eigenvector. It uses
pre-trusted peers to break malicious collectives and performed well in its
file-sharing simulations. Those are useful ideas, but scientific review differs
in three decisive ways:

1. Review is not one homogeneous transaction. Calibration, statistical
   inference, numerical implementation, provenance, and interpretation are
   distinct capabilities.
2. Pre-trusted peers are a governance choice. A malicious or captured root can
   corrupt the result, and EigenTrust leaves root selection out of scope.
3. A recursive public score can become self-reinforcing when it controls future
   assignments, attention, and the opportunity to earn more score.

The last risk has formal precedent. Kawakatsu et al. found a transition from
egalitarian to hierarchical outcomes in networked endorsement dynamics, with
some PageRank-like regimes exhibiting strong initial-condition dependence and
extreme concentration ([PNAS 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8072324/)).
This does not prove an MCRP implementation would behave the same way. It does
show that feedback between rank and future endorsement can manufacture durable
hierarchy.

A second PNAS result is directly relevant to management incentives. Chiba-Okabe
and Plotkin model an institution that broadcasts reputation signals and show
that its revenue incentives can favor degraded or inflated signals—the
institution itself has moral hazard ([PNAS 2026](https://pubmed.ncbi.nlm.nih.gov/42066047/)).
An MCRP ranking service therefore cannot be presumed neutral merely because its
algorithm is transparent.

### Votes measure reactions, not correctness

Peer review itself is noisy. A meta-analysis reported low inter-reviewer
reliability, while noting that complementary specialists may legitimately
disagree ([Bornmann, Mutz, and Daniel 2010](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0014331)).
At one medical journal, agreement on rejection across 5,881 reviews was only
`kappa = 0.11` ([Kravitz et al. 2010](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010072)).

Review-of-review ratings are not neutral ground truth either. A NeurIPS study
found inconsistency and miscalibration in such ratings, including authors
rating favorable reviews more positively ([Goldberg et al. 2025](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0320444)).
Review votes may be valuable feedback, but they must be typed by rater role and
question. “I agree,” “this was useful,” “this checked the assigned evidence,”
and “a later audit confirmed the defect” are different events.

Status can bias review independently of review quality. Controlled studies
found effects from famous authors and institutions
([Tomkins, Zhang, and Heavlin 2017](https://pubmed.ncbi.nlm.nih.gov/29138317/))
and large rejection differences when the same manuscript carried a Nobel
laureate, anonymous, or little-known author identity
([Huber et al. 2022](https://pubmed.ncbi.nlm.nih.gov/36194633/)). A public
reviewer leaderboard would create another prestige signal capable of entering
the same feedback loop.

## 2. What graph trust can contribute

### Local and personalized views

Personalized PageRank changes the restart distribution, so rank is relative to
a chosen source or trust-root set rather than universal. Topic-sensitive
PageRank shows how separate topic-biased vectors avoid treating highly linked
entities as authoritative for every query
([Haveliwala 2002](https://ilpubs.stanford.edu/573/1/2002-6.pdf)).

Massa and Avesani provide a closer result for the desired social semantics.
They found a meaningful population of controversial actors—trusted by some and
distrusted by others—and reported better predictions from local rather than
global trust metrics for those actors
([AAAI 2005](https://aaai.org/Papers/AAAI/2005/AAAI05-020.pdf)). The lesson for
MCRP is not that their recommender metric should be copied. It is that
controversy should remain view-dependent rather than be forced into one verdict.

### Capacity limits at the trust frontier

Levien and Aiken formulate attack-resistant trust as a graph-flow problem and
derive a max-flow metric that bounds attacks under explicit assumptions
([USENIX Security 1998](https://www.usenix.org/conference/7th-usenix-security-symposium/attack-resistant-trust-metrics-public-key-certification)).
Levien's later group-trust analysis argues that broad classes of scalar metrics
are weak while group metrics can bound how many hostile identities pass a trust
frontier ([thesis](https://www.levien.com/thesis/compact.pdf)).

This supports a two-stage MCRP view:

1. an attack-resistant capacity or independent-path gate decides whether an
   actor is locally admissible for a domain role;
2. a short personalized restart walk helps route among admissible candidates;
3. conflict, coverage, workload, independence, and random audit rules are
   applied separately.

Graph paths do not prove independence. Two paths may share an employer,
supervisor, funding source, collaboration, or management controller. Path
diversity must therefore be supplemented with disclosed control and conflict
attributes.

### The limits of Sybil defenses

The classic Sybil result shows that, absent a logically centralized identity
authority or strong resource assumptions, a distributed system cannot generally
establish that identifiers correspond to unique actors
([Douceur 2002](https://www.microsoft.com/en-us/research/publication/the-sybil-attack/)).

Social-graph systems such as SybilGuard, SybilLimit, and SybilRank depend on
assumptions about sparse attack edges and the mixing of the honest region.
SybilRank was successfully used to prioritize accounts for human inspection,
not to prove guilt
([Cao et al. 2012](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/cao)).
Comparative work shows that community structure and integrated attackers can
violate the assumptions behind these methods
([Alvisi et al. 2013](https://www.cs.utexas.edu/~lorenzo/papers/Alvisi13SoK.pdf)).

MCRP consequently needs a scarce underlying actor credential even if review
personas are publicly anonymous. Graph structure can prioritize audits and
bound local influence; it cannot supply personhood. Coordinated real humans,
captured managers, and review cartels are also not Sybils and require separate
controls.

### Negative edges should localize, not infect

Guha et al. demonstrate that trust and distrust signals can be propagated in a
large signed graph ([WWW 2004](https://snap.stanford.edu/class/cs224w-readings/guha04trust.pdf)).
That predictive result does not justify turning “the enemy of my enemy” into
scientific authority. Signed-network edges can encode structural balance,
status, conflict, or retaliation rather than a single epistemic meaning
([Leskovec, Huttenlocher, and Kleinberg 2010](https://arxiv.org/abs/1003.2424)).

MCRP should propagate only positive, scoped delegation. A negative actor edge
should act as a source-local route block, recusal, quarantine request, or
evidence-bearing challenge. It must name its grounds, scope, expiry, and appeal
path. It must never automatically create positive trust elsewhere or globally
poison the target's neighbors.

## 3. Topic color and domain structure

Trust is multi-relational. Multilayer-network theory exists precisely because
collapsing different relationship types changes the system being analyzed
([Boccaletti et al. 2014](https://doi.org/10.1016/j.physrep.2014.07.001)).
Topic-sensitive expert-finding and trust work likewise treats expertise as
query- or topic-dependent rather than universal.

The right compromise is:

- **Storage:** keep one typed multilayer graph so review objects, attestations,
  challenges, competencies, domains, and bridges remain interoperable.
- **Inference:** evaluate one topic-and-capability layer at a time, or a
  predeclared conjunction of layers.
- **Governance:** let coherent leaf domains define rubrics, roots, conflicts,
  appeals, and reviewer eligibility.
- **Publication:** require a coverage vector across relevant leaf domains rather
  than averaging them.

A gravitational-wave result might need independent coverage from detector
calibration/data quality, compact-binary inference, statistical methodology,
workflow provenance, and HPC execution domains. No parent domain or single
reviewer inherits authority over all five.

### No established maximum domain size

The literature does not establish a universal maximum size for a scientific
trust domain. Evidence that smaller, older, closed online groups may be more
trusted is suggestive, not a scientific-review scaling law
([Ma et al. 2019](https://s.tech.cornell.edu/assets/papers/grouptrust.pdf)).
MCRP should avoid a “Dunbar number” requirement.

Instead, domains should monitor reviewer-pool coverage, effective independence,
assignment concentration, queue latency, appeal reversals, topic entropy,
calibration drift, anonymity-set size, bridge concentration, and confirmed or
missed defects. Fission is justified when a common rubric no longer calibrates
the work or a small broker set controls cross-topic decisions—not when a fixed
member count is reached.

### Nested and forkable governance

Ostrom's polycentric governance describes multiple autonomous decision centers
operating under shared general rules
([American Economic Review 2010](https://www.aeaweb.org/articles?id=10.1257/aer.100.3.641)).
That is a better institutional analogy than one global review authority, though
polycentric systems can also fragment responsibility or reproduce power.

For MCRP, a domain graph should have one normative governance parent and zero
or more explicit competency imports. The parent may supply identity, privacy,
minimum conduct, data formats, and appeal guarantees. It must not confer
scientific standing downward or overwrite child judgments. Cross-domain trust
requires a signed, attenuated, expiring bridge accepted by the importing domain.

Domain forks should share immutable scientific and review records while
adopting different roots and policies. Private trust edges and reviewer mappings
do not copy automatically; distrust never inherits by default. A fork is not a
claim that either side is scientifically correct. It is a containment and exit
mechanism.

## 4. Per-review anonymity with private accountability

### The unavoidable linkage boundary

The public requirement is stronger than a stable pseudonym: each review needs a
fresh persona, so two reviews by one person cannot ordinarily be linked. The
system still needs to enforce eligibility, one review or vote per scope, private
history, sanctions, and appeals.

Use three identities:

1. **Civil or institutional identity**, held by a uniqueness registrar.
2. **Domain account**, a random domain-specific identifier held by a separate
   eligibility/reputation service.
3. **Review persona**, a fresh key stable only within one review case.

No routine operator should possess both the civil-identity map and the review
corpus. Review votes attach to the review object. The reputation service may
associate the result privately with the domain account; the public cannot
connect the review to another case.

### Practical and advanced mechanisms

For v0.1, ordinary signatures, one-use capabilities, role separation, and a
threshold-encrypted identity map are the most inspectable deployable choice.
Anonymous voting can use blindly issued one-use tokens; the Privacy Pass
architecture and protocols specify unlinkable issuance/redemption and document
collusion and correlation risks
([RFC 9576](https://www.rfc-editor.org/rfc/rfc9576.html),
[RFC 9578](https://www.rfc-editor.org/rfc/rfc9578.html)).

A stronger profile can use a scoped nullifier:

`nullifier = PRF(member_secret, assignment_or_poll_scope)`

It detects duplicate use inside one scope without producing a global tracking
identifier. [Semaphore](https://docs.semaphore.pse.dev/) is a working reference
for anonymous membership proofs and duplicate-signal prevention.

BBS credentials support selective disclosure and unlinkable derived proofs,
but as of August 2026 the W3C cryptosuite is still a Candidate Recommendation
Draft ([W3C BBS](https://www.w3.org/TR/vc-di-bbs/)). Coconut demonstrates
threshold issuance and unlinkable selective disclosure
([NDSS 2019](https://www.ndss-symposium.org/ndss-paper/coconut-threshold-issuance-selective-disclosure-credentials-with-applications-to-distributed-ledgers/)).
These are credible pilot paths, not minimum dependencies.

Group signatures directly model anonymous group membership with optional
opening, but operational libraries, membership changes, revocation, and opener
governance are nontrivial. MCRP should not invent bespoke cryptography.

### Accountable opening and residual risk

Opening must never be permitted for unfavorable conclusions, ordinary low
ratings, author pressure, management curiosity, or scientific disagreement.
It may be considered only for enumerated conduct allegations such as identity
fraud, bribery, fabricated evidence, severe undisclosed conflict, misuse of
confidential material, or credible threats, under threshold authorization,
recusal, minimum disclosure, notice, and appeal.

Cryptography does not prevent stylometric, timing, topical, or small-pool
deanonymization. “Anonymous” must name its adversaries, trusted operators,
anonymity-set policy, and residual leakage.

## 5. Review-quality evidence

Review evaluation should use typed questions and delayed outcomes:

- Did the report cite the exact claim and evidence inspected?
- Did it execute the assigned checks and state exclusions?
- Was a reported defect later confirmed, falsified, or left unresolved?
- Did it identify a scope limitation later reflected in the release?
- Did it miss a planted or later-discovered material defect?
- Was it actionable and professionally expressed?
- Was a conflict, fabrication, or procedural violation adjudicated?

Agreement with the paper, author satisfaction, majority alignment, prestige,
and citation count must not directly determine reviewer standing. A qualified
dissent can be the most valuable review in the corpus.

## 6. Recommended MCRP adoption

Adopt a Trust-Domain and Review-Governance (TDRG) profile with these invariants:

1. no global reviewer score;
2. directed, typed, scoped, expiring trust;
3. fresh public persona for every review case;
4. private accountability with separated duties and due process;
5. topic-local personalized routing plus capacity and diversity constraints;
6. report-level votes distinct from actor trust delegations;
7. delayed, evidence-bearing review outcomes rather than agreement scoring;
8. explicit domain charters, parents, imports, bridges, forks, and exit rights;
9. no transitive inheritance of distrust;
10. no graph result or vote may become a scientific disposition.

The first evaluation must compare a flat/no-reputation baseline, global
EigenTrust-like ranking, topic-local personalized propagation, and capped-flow
eligibility. It must test Sybils, real-human review rings, management capture,
malicious negative voting, prestige feedback, sparse new domains, and legitimate
scientific schisms. Measures should include defect detection, false accusation,
minority-view survival, capture radius, privacy leakage, assignment diversity,
and newcomer inclusion—not only agreement or acceptance accuracy.

### Existing review infrastructures to profile, not replace

TDRG must reuse the scholarly-review exchange layer that already exists:

- [COAR Notify](https://coar-repositories.org/tools-and-resources/notify/)
  provides decentralized repository/review-service interoperability using W3C
  Linked Data Notifications and ActivityStreams;
- [DocMaps](https://docmaps.knowledgefutures.org/) represents editorial and
  review events as extensible machine-readable assertions;
- [Crossref peer-review metadata](https://www.production.crossref.org/news/2018-06-05-introducing-metadata-for-peer-review/)
  already registers reviews, decision letters, author responses, stages, and
  review types;
- [ANSI/NISO Z39.106-2023](https://www.niso.org/publications/z39106-2023-peerreview)
  standardizes peer-review terminology.

TDRG should define a profile/crosswalk for its case personas, review objects,
evaluations, challenges, and governance events. It should not invent competing
transport, identifier, or basic review-event concepts where these standards
carry the needed semantics.

## 7. Evidence gaps

This research supports an architecture and evaluation agenda, not the claim that
the architecture works. Missing evidence includes:

- empirical review-outcome ground truth suitable for reputation updates;
- independent implementations of the privacy and trust-view protocols;
- resistance to institutional collusion and captured roots;
- usability and safety of per-review personas and private appeals;
- real-domain calibration and split triggers;
- measurements of retaliation and metadata deanonymization;
- evidence that local graph routing improves review without excluding newcomers
  or suppressing legitimate dissent.

Until those exist, TDRG should be described as a proposed actor-regulation layer
for MCRP, not a solution to peer review.

The companion
[`reviewer-trust-closest-work-matrix.md`](reviewer-trust-closest-work-matrix.md)
records systems that already combine repository review, graph-based reviewer
selection, topic reputation, anonymous accountability, decentralized
governance, incentives, and immutable records. Those systems close broad
novelty claims and define the required comparative baselines.
