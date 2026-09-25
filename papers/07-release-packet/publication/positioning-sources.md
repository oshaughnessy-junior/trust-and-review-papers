# Positioning source ledger

Primary-source inspection on 2026-09-25. All links below were retrieved through
the web tool. This ledger supports `positioning-and-adoption.md`; it is not a
comprehensive systematic review or standards-conformance audit. No outreach,
submission, registration, account creation or external notification was performed.

## Sources actually read

| ID | Primary page and version | Inspected material | Bounded use |
|---|---|---|---|
| S1 | [COAR Notify specification index](https://coar-notify.net/specification/) | Design principles and current-version link | Established decentralized notification architecture; index identified 1.0.1 as current on inspection date |
| S2 | [COAR Notify 1.0.1](https://coar-notify.net/specification/1.0.1/) | Baseline activity requirements and pattern list | Existing notification families; no claim of implemented endpoint compatibility |
| S3 | [Request Review, 1.0.1](https://coar-notify.net/specification/1.0.1/request-review/) | Required types and resource/content distinction | Candidate offer mapping; exact MCRP tuple is additional profile data |
| S4 | [Announce Review, 1.0.1](https://coar-notify.net/specification/1.0.1/announce-review/) | `object`, `context`, activity types | Review notification is distinct from the review resource and reviewed resource |
| S5 | [Announce Endorsement, 1.0.1](https://coar-notify.net/specification/1.0.1/announce-endorsement/) | Endorsement resource and context | Conditional mapping for a genuine endorsement, not every reliance kind |
| S6 | [Undo Offer, 1.0.1](https://coar-notify.net/specification/1.0.1/undo-offer/) | Withdrawal semantics and original-offer reference | Do not confuse an offer withdrawal with a scientific retraction |
| S7 | [PROV-O, W3C Recommendation 2013-04-30](https://www.w3.org/TR/prov-o/) | Introduction, starting/expanded/qualified terms, responsibility and revision descriptions | Provenance and extensibility already exist; proposed mapping is not proof of semantic equivalence |
| S8 | [RO-Crate 1.3 introduction](https://www.researchobject.org/ro-crate/specification/1.3/introduction.html) | Package model, metadata document and human preview | Existing research-artifact packaging; no MCRP conformance assertion |
| S9 | [RO-Crate 1.3 provenance](https://www.researchobject.org/ro-crate/specification/1.3/provenance.html) | Equipment/software actions and recording changes | Existing human authorization, workflow changes and old/new file history |
| S10 | [RO-Crate 1.3 profiles](https://www.researchobject.org/ro-crate/specification/1.3/profiles.html) | Profile requirements, extension support and conformance declarations | A possible future packaging profile; none implemented here |
| S11 | [PCI FAQ](https://peercommunityin.org/faq/) | Recommender role, recommendation process and archive description | Existing institutionally grounded open review; no acceptance guarantee for this work |
| S12 | [PCI account of version-controlled Registered Reports](https://peercommunityin.org/?p=6218) | Pre/post-study review, amendments and version-specific examples | Prior workflow already connects versions, decisions and changes; historical explanatory account, not verified current submission instructions |
| S13 | [CRediT resource hub](https://credit.niso.org/) | Fourteen-role taxonomy and standard status | Reuse contributor-role vocabulary; no automatic panel authority inferred |
| S14 | [CRediT Validation role](https://credit.niso.org/contributor-roles/validation/) | Role description | Contribution vocabulary can describe checking work; it does not itself establish a particular external review's sufficiency |
| S15 | [About ORCID](https://info.orcid.org/what-is-orcid/) | Identifier, record and API description | Persistent identity reference, not a substitute for domain appointment |
| S16 | [ORCID Trust](https://info.orcid.org/orcid-trust/) | Individual control, broad eligibility and source transparency | Identity/contribution context should not be promoted into unstated qualification or common-control guarantees |

COAR's vocabulary index was also read to verify the published action names.
The main source claims are paraphrased; no long source passages or payloads were
copied. Proposed semantic mappings and adoption tests are our design inferences,
not instructions endorsed by the standards bodies or communities.

## Retrieval and inference boundaries

The direct PCI Registered Reports about page returned a bot-protection page. The
accessible PCI parent-site FAQ and named explanatory account therefore support
only the limited comparisons above. They do not establish present submission
eligibility, AI policy, fees, staffing or review times. The attempted Episciences
English page returned a retrieval error; no Episciences feature or availability
claim is made from that failed retrieval.

The first direct RO-Crate provenance-page request failed; following the official
profile page's provenance link subsequently retrieved it successfully. An initially
guessed ORCID trust URL failed; the official navigation link resolved to the page
recorded as S16. These failures were not treated as negative evidence about the
systems' capabilities.

The comparison examined selected core features, not every extension, deployment
or companion standard. “The inspected core does not mandate this profile” must
not become “no existing system can represent it.” In particular, PROV and RO-Crate
are extensible, and local editorial workflows can already carry detailed conditions.

The desired round-trip identity, resource accounting and domain adoption outcomes
remain design hypotheses. No network interoperability, authentication, authority
verification, standards validation, independently developed adapter, or human
adoption experiment was performed for this positioning memo. The toy engine and
public export were left unchanged while these two new documents were written.
