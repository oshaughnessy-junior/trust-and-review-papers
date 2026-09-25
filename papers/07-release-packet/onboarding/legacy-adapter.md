# Bring an existing review without inventing new authority

You can begin with a versioned paper and an ordinary review letter. The prototype
asks what that review actually supports, then keeps unresolved questions visible.
An agent can prepare the structured wrapper immediately; a human must still make
or authorize any real responsibility assertion attributed to them.

## A six-question card, with the matching agent action

| Human question | Agent action in this example | If the answer is missing |
|---|---|---|
| **1. Which exact claim and version?** Point to the precise result, immutable release and evidence. | Preserve claim ID, declared git object and evidence digest; keep the ordinary URL as context. | Stop the executable conversion; do not treat a moving page as an exact release. |
| **2. What was checked?** Name the method, scope, result and limits in the reviewer's terms. | Keep declared check scope/result/method separate from the recommendation to accept. | Preserve unknown; never fill in a positive result from tone or recommendation. |
| **3. Who can take responsibility, and for what use?** A reviewer, author and editor have different roles. | Leave decision authority unknown until a separately explicit assertion exists. | No scoped reliance or publication permission is inferred. |
| **4. What connections could limit independence?** Include shared control and inaccessible prerequisites. | Preserve disclosures; never infer independent groups from different names or many team members. | Unknown remains unknown. Nonempty unsupported disclosures must be reconciled, not overwritten. |
| **5. What effort and conditions can be supported?** State purpose, capacity and expiry. | Require explicit fixture capacity, exact scope, purpose and expiry before the toy run. | Do not promise completed coverage or an appeal service. |
| **6. What would make us reconsider?** Identify dependency changes and a correction path. | Record dependencies separately and exercise a material amendment. | Missing dependencies remain a known blind spot; the adapter cannot discover them. |

The machine-readable path is runnable from the extracted packet root:

```sh
python3 -m adapters.demo
```

First, the original legacy metadata is refused for scoped reliance. Then a
**separate invented fixture** supplies the missing assertions solely to demonstrate
the actual toy protocol. Its old reliance becomes pending after amendment. The
original source, every absent/null/empty distinction, and the semantic loss report
stay attached to the result.

The example does not parse arbitrary prose, contact a journal, authenticate a
reviewer, establish consent, or claim conformance with an existing interoperability
standard. It shows a practical entry point that agents can execute today while
keeping the human questions explicit. A real adapter should earn trust through
independent round trips and permission-aware integration tests before live use.
