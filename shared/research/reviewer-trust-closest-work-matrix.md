---
artifact_role: bounded-closest-work-and-novelty-gate
status: working-draft
date: 2026-08-24
publication_status: private-not-approved
---

# Reviewer trust-domain closest-work matrix

## Gate result

- **NO-GO:** do not claim that TDRG invents decentralized peer review,
  repository-mediated review, reviewer selection from scholarly graphs,
  topic-specific reviewer reputation, anonymous-but-accountable reputation,
  immutable review records, token incentives, or reviewer-reputation networks.
- **CONDITIONAL:** a contribution may remain in the consolidation of a shared
  claim/evidence scientific record with plural root-relative trust views,
  per-case unlinkable personas, strict event-type separation, importer-approved
  competency bridges, and fork/fission containment—if the protocol is
  interoperable and the comparative evaluation supports those choices.

This matrix is a bounded audit, not proof of novelty or an exhaustive systematic
review.

## Closest systems

| Work | What it already establishes | Preemption risk | Residual difference to test, not assume |
|---|---|---|---|
| Rodriguez, Bollen, and Van de Sompel, [“The convergence of digital libraries and the peer-review process” (2006)](https://doi.org/10.1177/0165551506062327) | Repository-centric deconstructed peer review, OAI-PMH review metadata, social-network reviewer selection, and weighting of reviewer evaluations. | **High** for “review outside journals,” portable review metadata, and graph-based reviewer routing. | TDRG binds routing to claim/evidence releases, explicit policy snapshots, local typed reliance, private personas, challenges, bridges, and forks. |
| Rodriguez and Bollen, [“An Algorithm to Determine Peer-Reviewers” (2006/2008)](https://arxiv.org/abs/cs/0605112) | Coauthorship-network and relative-rank selection of domain-relevant reviewers, with some conflict detection. | **High** for automated reviewer discovery from scholarly networks. | TDRG does not infer competence from coauthorship alone and separates routing from scientific authority, control independence, and private outcome history. |
| [PeerReview4All](https://www.jmlr.org/papers/v22/20-190.html) and [randomized reviewer assignment](https://proceedings.neurips.cc/paper/2020/hash/93fb39474c51b8a82a68413e2a5ae17a-Abstract.html) | Mature work on fair, accurate, and randomized assignment, including defenses against collusion, torpedo reviewing, and assignment-based deanonymization. | **High** for fair/randomized routing and assignment-integrity claims. | TDRG should consume these assignment methods after scoped eligibility; its contribution cannot be “randomly assign qualified reviewers.” |
| Naessens, Demuynck, and De Decker, [“A Fair Anonymous Submission and Review System” (2006)](https://doi.org/10.1007/11909033_5) | Reputation-based anonymous reviewing using anonymous credentials, topic/subtopic reputation, aging information, conflicts, and accountability/deanonymization. | **Very high** for anonymous-yet-accountable topic reputation. | TDRG's possible difference is operational governance: one fresh case persona, separated authorities, narrow opening causes, private appeals, plural root-relative graph views, and scientific-record integration. A security comparison is mandatory. |
| Tenorio-Fornés et al., [“Decentralizing science” (2021)](https://doi.org/10.1016/j.ipm.2021.102724) and its earlier prototype work | Interoperable decentralized open peer-review architecture using blockchain/IPFS, reviewer reputation, transparent governance, two prototypes, interviews/survey, and cost analysis. | **Very high** for decentralized open review, reputation networks, interoperability, and governance. | TDRG rejects a universal reputation, keeps review records portable beneath forked policies, and adds claim/evidence semantics, local trust roots, typed bridges, privacy/accountability separation, and explicit no-go tests. |
| Sun, Zhou, and Guo, [“Decentralized knowledge assessment” (2025)](https://doi.org/10.1016/j.xinn.2025.100945) | Verified scholar identities, timestamped actions, decentralized storage/computation, dual token/reputation incentives, simulations using KDD/ICLR data, and blockchain implementation. | **Very high** for scalable decentralized assessment, incentives, identity, reputation, and simulation. | TDRG permits anonymous per-case review, treats review agreement/popularity as non-ground-truth, tests malicious roots/management and minority survival, and makes community-relative forks first-class. |
| Decentralized Peer Review in Open Science, [mechanism proposal (2024)](https://arxiv.org/abs/2404.18148) | Community governance, reviewer remuneration, anonymized public reports, reviewer reputation, and digital certificates. | **High** for the broad governance/reputation proposal. | TDRG must show why claim-level records, scoped reliance semantics, bridges/forks, and accountable anonymity add enforceable behavior rather than more architecture prose. |
| Traxia, [agent-native publishing architecture (2026)](https://arxiv.org/abs/2606.08256) | Signed agent identities, provenance, contribution records, knowledge graph, multi-tier review, contradiction detection, reputation/staking, and partial prototype. | **High** for agent-native identity, review, provenance, and reputation claims. | TDRG may differ through standards-grounded scientific claim/evidence contracts, no-global-score policy, per-review human anonymity, domain fission, and comparative validation. |
| EigenTrust, [Kamvar et al. (2003)](https://nlp.stanford.edu/pubs/eigentrust.pdf) | Global recursive reputation with pre-trusted peers and simulation under malicious collectives. | **High** for global reputation algorithms; also the required baseline. | TDRG hypothesizes that scientific review needs local typed views, visible roots, capacity bounds, and assignment exploration. This must be demonstrated, not asserted. |
| Levien and Aiken, [attack-resistant max-flow trust (1998)](https://www.usenix.org/conference/7th-usenix-security-symposium/attack-resistant-trust-metrics-public-key-certification) | Root-relative capacity constraints that bound hostile identities under declared graph assumptions. | **High** for frontier-capacity defense. | TDRG merely profiles the technique for scientific routing and combines it with control-diversity and topic constraints; the algorithm itself is prior art. |
| Massa and Avesani, [local versus global trust (2005)](https://aaai.org/Papers/AAAI/2005/AAAI05-020.pdf) | Local trust can outperform global trust for controversial actors in a recommender setting. | **High** for the conceptual case for observer-relative trust. | Scientific-review validity, domain bridges, anonymous accountability, and institutional fracture require separate evidence. |
| AnonRep, [anonymous reputation system](https://dedis.cs.yale.edu/dissent/papers/anonrep-abs/) | Anonymous participation with reputation without ordinary long-term public tracking. | **High** for “anonymous reputation” as a general claim. | TDRG must specify scientific-review scopes, operator collusion, one-case personas, appeals/opening, and integration with claims/evidence. |

## Existing exchange standards

| Standard/infrastructure | Existing coverage | TDRG obligation |
|---|---|---|
| [COAR Notify](https://coar-repositories.org/tools-and-resources/notify/) | Decentralized linking of repositories and peer-review services through Linked Data Notifications and ActivityStreams. | Profile its requests/notifications instead of creating a new review transport. |
| [DocMaps](https://docmaps.knowledgefutures.org/) | Extensible machine-readable editorial and review-event assertions. | Map public review, response, challenge, and supersession projections. |
| [Crossref peer-review metadata](https://www.production.crossref.org/news/2018-06-05-introducing-metadata-for-peer-review/) | Registration of reviews, decision letters, author responses, stage, and review type. | Reuse for DOI-linked public artifacts; preserve case-persona and MCRP scope through extensions. |
| [ANSI/NISO Z39.106-2023](https://www.niso.org/publications/z39106-2023-peerreview) | Standard terminology for peer-review practices. | Use canonical terms and document any TDRG-specific vocabulary. |

## Consolidation claim that may survive

Subject to implementation and evaluation, the defensible claim is:

> We synthesize a trust-domain profile for a claim-level, machine-verifiable
> scientific record. It separates scientific evidence from actor routing;
> review-object feedback from future reliance and conduct adjudication; and a
> common event history from local, topic/capability/policy/time-specific trust
> views. It adds per-case accountable personas, explicit attenuated bridges,
> and fork/fission semantics, then compares these choices against flat and
> global-reputation baselines under capture, collusion, privacy, newcomer, and
> minority-view harms.

This is a protocol-composition and evaluation claim. The words **first**,
**decentralized reputation**, **anonymous review**, **graph reviewer
selection**, and **immutable peer review** are not defensible novelty claims.

## Required differential experiments

1. Reimplement or faithfully approximate the closest global, local, and
   decentralized baselines rather than comparing only against no reputation.
2. Demonstrate whether explicit topic/capability layers and bridges reduce
   authority leakage relative to topic credentials or similarity alone.
3. Demonstrate whether fresh personas plus private accountability achieve a
   useful privacy boundary beyond a durable anonymous reputation credential.
4. Test captured roots and platform/management incentives, not only anonymous
   Sybils.
5. Test whether forked policy overlays localize capture while preserving shared
   scientific and review objects.
6. Measure false exclusion, newcomer delay, qualified dissent survival, and
   operator intelligence cost alongside attacker exclusion.

If those tests do not show a material difference, TDRG should be presented as an
interoperability profile and governance vocabulary, not a new peer-review
mechanism.
