# Agent-only launch: independent adversarial probe plan

The launch interface is a local bounded simulation entry point, not an
authenticated network service. The blue author is implementing a separately
loaded policy with principal/control/qualification/role declarations and
agent-to-principal delegation. Requests may exercise that policy but must not
create privileges or infer real independence.

The independent probes will check:

1. One hundred internal workers or several aliases for one principal cannot
   create extra independent groups or separately spend the same capacity.
2. Requests cannot add actors, change role grants, lower offered coverage or
   reinterpret scientific checks as legal/publication authority.
3. Old checks, old targets, replayed aliases and post-amendment reliance retain
   exact identity, scope, expiry and currentness requirements.
4. Rejected commands leave clock, events, resources and alias state unchanged;
   batch output distinguishes rejected work from accepted work.
5. JSON duplicate keys, type confusion, unsupported fields, non-finite values,
   oversized input and deep nesting are rejected within stated bounds.
6. Evidence content and declared target digest cannot disagree; an unavailable
   dependency cannot silently count as checked evidence.
7. Public onboarding names the actual trust boundary. A caller asserting an
   operator's agent ID is not authenticated merely because a policy contains it.

The author has excluded the runtime's combinatorial panel enumerator from the
CLI surface. This avoids pretending that small JSON input alone bounds an
exponential panel search. Policy limits and input limits remain subject to
independent tests once the runnable interface is available.

No pass result or release assent is implied by this plan. Actual probes and
their results will be saved beside it.
