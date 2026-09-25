# Publication is a decision followed by a separate observation

**D/I:** `release_cycle.py` is an in-memory, trusted-input model. Its roles are
fixture labels. It does not authenticate humans or agents, cryptographically
attest decisions, enforce process isolation, serve a website, detect private
content or create legal permission. Required-check booleans model externally
provided results; the script does not perform those checks itself.

Let the candidate binding be

\[
b=H(r,s,H(x),e,p,c,u),
\]

where \(r\) is a release identifier, \(s\) a source revision, \(x\) the bytes,
\(e\) the evidence-set digest, \(p\) the policy version, \(c\) a content class and
\(u\) the destination. Canonical JSON fixes the encoding in this model. The
delegation has a separate digest binding publisher, scope, destination, policy
and validity interval. The verifier's decision names both digests and its expiry.

**T (model invariant):** publication can occur through the model's `publish`
method only if its current candidate/delegation pair matches a recorded decision,
the publisher matches the configured fixture role, required scope and policy
match, and neither decision nor delegation has expired or been revoked. This
follows from the guards preceding the only insertion into `deliveries`. It
assumes trusted unmodified runtime state and use of the public methods; direct
mutation of Python dictionaries defeats the boundary and is outside the claim.
Hash collision resistance is assumed when a digest is used as a binding.

Publication first produces `delivered_unobserved`. A separate observer reports
`missing`, `binding_mismatch`, `mismatch` or `matches` about retrieved fixture bytes. A matching
historical receipt remains a valid description of that observation even after
the authority expires. Currentness is computed separately and names the last
observation rather than asserting continuous monitoring.

The demo walks through failed delivery, a missing observation, successful retry,
idempotent repeat, observation, correction requiring a new decision, and later
revocation. The tests mutate each bound component, expand a delegation, reuse
expired authority, roll time backward, omit checks, substitute a verifier and
tamper with the delivered bytes.

```sh
python3 papers/07-release-packet/models/release_cycle.py
python3 -m unittest discover -s papers/07-release-packet/models -p 'test_release_cycle.py' -v
```

This canary closes an explanatory gap in the prior dossier: it demonstrates a
complete *synthetic* sequence and several failures. It does not close the
operational gap between the toy model and the hosted Commons or public website.
Real deployment needs authenticated decisions, independent credentials and
observation, immutable artifacts, transactional delivery, rights handling and
an accountable operator.

Red-team repairs additionally bind amendment successors, reject identifier cycles/rebinding, and prevent rejected future-dated calls from advancing the toy clock.
