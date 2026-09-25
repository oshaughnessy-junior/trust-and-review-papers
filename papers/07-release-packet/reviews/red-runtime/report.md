# Runtime red-team report

**Reviewer:** internal AI adversarial lane; same operator as authors, not external
security audit. **Date:** 25 September 2026. **Verdict:** acceptable to publish as
an explicitly synthetic research prototype after the concrete repairs below;
not evidence that the Commons service is secure or institutionally authorized.

## What was attacked

Reviewed the toy runtime, publication boundary model, their claims and tests,
agent-framework manuscript, public introduction, and dossier 06 collective
assessment. All probes use ordinary public API methods and valid fixture roles.
No finding relies on editing runtime dictionaries, forging real credentials,
pretending supplied group labels were authenticated, or executing hostile code
inside the trusted Python process. Files were changing during review; the
baseline and repaired observations are distinguished explicitly.

The red reviewer independently ran the author suites, wrote seven additional
regression tests, and executed seven diagnostic probes. The original author
suites passed while the initial semantic counterexamples remained possible.
Passing unit tests was therefore not accepted as dispositive evidence.

## Findings and disposition

Severity is relative to **the prototype's advertised semantics**, not CVSS or
production exploitability. P2 means materially misleading state or ordinary API
failure that should be repaired before presenting a positive demonstration.

| ID | Severity | Counterexample and affected claim | Disposition |
|---|---|---|---|
| RR-1 | P2 | A support check creates reliance; a later direct overlapping contradiction blocks a new identical reliance but leaves the old one `current_under_toy_policy`. A user sees inconsistent application of the conservative contradiction policy. | Repaired. Existing reliance now reports `contradiction_pending`; negative probe and independent regression pass. This does not automatically adjudicate science or propagate every disputed premise as a material amendment. |
| RR-2 | P2 | Query expiry at time 10, then query time 2: toy runtime restores `current_under_toy_policy`. Its original event-only time check differed from the publication model's clock and invited accidental historical/current confusion. | Repaired. Successful currentness queries advance the monotone clock. Earlier queries reject. Prior documentation narrowly spoke about timed events, so this is semantic hardening, not a falsified theorem about historical databases. |
| RR-3 | P2 | Deliver candidate A; verify B with the same release ID and bytes but different source/evidence metadata; observing B returns `matches`, and its currentness returns `last_observation_matches`, although publishing B rejects rebinding. | Repaired. Observation records actual binding and returns `binding_mismatch`; currentness returns `release_binding_mismatch`. The original publication guard itself was not bypassed. The defect was a misleading observer/candidate composition. |
| RR-4 | P2 | An invalid publication request at time 1,000,000 rejects but advances the clock, preventing a valid request at time 2. | Repaired. Failed validation does not commit time. Independent tests cover failed publish, verify, observe and amend calls and compare complete pre/post state. External denial of service is not thereby solved. |
| RR-5 | P2 | Amendment links allow A→B→A and overwrite A's successor. The original link also discards the replacement's complete binding, retaining only its release ID. | Repaired with deliberately narrower policy: successor must be a new release ID; old successors cannot be overwritten; replacement binding is recorded and enforced during authorization. Independent probes reject cycles, overwrite and differently bound replacement. This is not a general branching/merging correction protocol. |
| RR-6 | P2 / specification gap | `required_groups` is supplied at each reliance call and originally absent from its stored record. A caller can ask for two groups, fail, then choose one. | Offer now records a minimum floor; reliance cannot weaken it and records the actual threshold. Red regression sets an explicit floor of two and rejects a one-group call. An earlier stronger *one-off reliance request* should not silently redefine the offer's policy. The author still chooses the offer floor: no external approval of contract adequacy is implemented. |
| RR-7 | Known excluded premise | Two actor IDs representing one real person each receive a full capacity key. The ledger accepts two units against a real-person capacity of one, even when both IDs share a control group. | Retained negative control. The capacity theorem explicitly assumes correct consolidated person keys. Control groups and resource identities solve different problems. This is not a discovered arithmetic defect. |

The exact baseline observations appear in `baseline-probes.json`. That file is a
compact transcription of the initial reviewer tool outputs, not a claim that
current source reproduces unfixed behavior. Its original six-result output file
was overwritten during a concurrent author repair and rerun; the transcription
preserves what was observed and labels the inferred replacement-binding issue.
The contract probe was revised after the explicit offer-floor API was introduced.
`repaired-probes.json` is generated from the current runnable probe. Intermediate
hashes describe an intermediate review state only; final hashes identify the
reviewed source at verdict time.

## Independent verification

From the repository root:

```sh
python3 papers/07-release-packet/reviews/red-runtime/probes.py
python3 -m unittest discover -s papers/07-release-packet/reviews/red-runtime -p test_adversarial_runtime.py -v
python3 -m unittest discover -s papers/07-release-packet/models -p test_release_cycle.py -v
python3 -m unittest discover -s papers/07-release-packet/domains/fixtures -p test_domain_models.py -v
(cd papers/07-release-packet && python3 -m unittest discover -s toy_agents/tests -v)
```

At verdict: 7 red regression methods, 9 publication methods, 19 toy-runtime
methods and 15 domain methods pass. These 50 methods are a subset of the full
release's tests; do not add them to a global count twice. Logs are retained in
this directory. Source hashes accompany the final verdict; generated results are
synthetic outputs, not observations of a hosted service.

## Remaining boundaries worth making prominent

1. **Policy validity is separate from policy preservation.** A frozen two-group
   threshold can be enforced, but the API does not establish that two groups are
   enough, independent, competent, or appropriate. A person granted both author
   and decision roles by the trusted fixture can decide their own reliance after
   external checks. Typed authority alone is not separation of duty.
2. **A stage invariant does not automatically survive composition.** The static
   group sampler, shared capacity ledger, completed-review population and final
   reliance selection have different distributions. A correct sampler plus a
   reservation rejection is not a fair scheduler. Publish the denominator trace
   through actual reliance and charge refusals, retries and repair.
3. **Observation is bounded.** Caller-supplied observation time is not a signed
   freshness witness. The synthetic publication observer consults an in-memory
   delivery map, not an independent destination with independent credentials.
   A matching receipt is dated evidence, never continuous monitoring.
4. **Corrections still require judgment and resources.** A free-form amendment
   reason does not establish materiality, resolve a dispute, or create recheck
   labor. Authority over amendment and revocation is a trusted fixture-operator
   decision, not an authenticated legal or scientific procedure.
5. **Negative controls belong in the release.** Hidden dependencies, common
   control and duplicate capacity identities should stay visible. Renaming their
   outputs as bugs fixed by this review would misstate the scope of the model.

## Collective contribution

The strongest common conclusion is **small records make assumptions inspectable;
they do not create the missing institution**. The runtime preserves selected
contracts, the math analyzes conditional behavior, domain fixtures demonstrate
specific inferential limits, and legal analysis identifies authority and duties.
None alone establishes the end-to-end result. The next useful experiment couples
selection, reservations, completion, actual reliance and correction under one
resource budget, with a plain structured-template baseline.

I support publication of this repaired, candid research seed. I do not support
claims of production security, externally reviewed correctness, legal clearance,
autonomous scientific judgment, lower human labor, or an operationally validated
review commons. Licensing, human attribution and the exact export decision remain
outside this technical assent.
