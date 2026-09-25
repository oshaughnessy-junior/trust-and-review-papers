"""Run four synthetic domain adapters against the actual toy receipt engine.

The adapter performs only the explicitly coded checks below; it does not infer
science from receipt labels. Control groups and appointed roles are trusted.
No live language-model calls, people, notices or external services are involved.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from toy_agents.protocol import Actor, Protocol, Rejected, Target
from domain_models import canonical_digest, fixtures, MODELS, rational, mixture, crossed_summary


def setup(case, team_size=1, declare_dependency=True):
    scope = frozenset(case["scope"])
    actors = [Actor("author", "author-control", scope, internal_size=team_size),
              Actor("checker", "external-control", scope),
              Actor("editor", "editor-control", frozenset(), frozenset({"scientific", "publication"}))]
    protocol = Protocol(actors, {"checker": 20}, {("checker", s): 20 for s in scope})
    dep = Target(case["dependency"].split("@")[0], "1",
                 canonical_digest({"synthetic_dependency": case["dependency"], "evidence": case["evidence"]}))
    protocol.offer(dep, "author", {"dependency_record"})
    target = Target(case["target"]["claim_id"], "1", canonical_digest(case["evidence"]))
    offer = protocol.offer(target, "author", scope, (dep,) if declare_dependency else ())
    return protocol, target, dep, offer


def rejection(action):
    try:
        action()
    except Rejected as exc:
        return str(exc)
    raise AssertionError("unsafe or unsupported action unexpectedly accepted")


def replay_case(case):
    p, target, dep, offer = setup(case)
    domain = case["domain"]
    calculated = MODELS[domain](case["evidence"])
    # These outcomes are supplied by narrow deterministic domain computations,
    # not by a language model's unexamined interpretation of the paper.
    checks, scope = [], set(case["scope"])
    if domain == "biology":
        scope = {"arithmetic"}
        checks.append(p.check(offer, "checker", scope, "exact means from four invented rows",
                              "support", case["limits"], now=1))
        p.check(offer, "checker", {"additive_model_identification"}, "treatment column equals batch column",
                "unknown", "Separate treatment and batch effects are unidentified", now=1)
    else:
        methods = {"physics": "exact division of raw scalar by stipulated gain",
                   "economics": "exact weighted sum and named synthetic trial estimand",
                   "law": "literal quotation is present in fictional policy"}
        if domain == "law":
            assert case["evidence"]["quotation"] in case["evidence"]["policy_text"]
        checks.append(p.check(offer, "checker", scope, methods[domain], "support", case["limits"], now=1))
    kind = "publication" if domain == "law" else "scientific"
    rid = p.rely(offer, "editor", checks, "Use as bounded synthetic teaching calculation",
                 scope, kind, expires=20, now=1)
    before = p.currentness(rid, now=2, observed_at=2, max_age=3)
    blocked = None
    if domain == "biology":
        blocked = rejection(lambda: p.rely(offer, "editor", checks,
            "Unsupported additive-model coefficient upgrade", {"arithmetic", "additive_model_identification"}, "scientific", expires=20, now=2))
    elif domain == "law":
        blocked = rejection(lambda: p.rely(offer, "editor", checks,
            "Unsupported institutional decision", scope, "legal_operational", expires=20, now=2))
    p.amend(dep, "Synthetic material change to a declared premise", now=3)
    pending = p.currentness(rid, now=3, observed_at=3, max_age=3)
    # Recompute actual amended evidence, rather than stamping an empty v2 wrapper.
    evidence = case["evidence"]
    if domain == "physics":
        new_evidence = {"raw": evidence["raw"], "gain": evidence["new_gain"]}
        amended_result = str(rational(new_evidence["raw"]) / rational(new_evidence["gain"]))
        method = "Exact revised raw/gain division = " + amended_result
    elif domain == "biology":
        new_evidence = {"rows": evidence["crossed_rows"], "model": "additive treatment plus batch"}
        summary = crossed_summary(new_evidence["rows"])
        amended_result = summary["crossed_average_contrast"]
        scope = {"arithmetic"}
        if summary["crossed_exact_additivity"]:
            scope.add("additive_model_identification")
        method = ("Crossed-cell average contrast = " + amended_result +
                  "; exact additive fit = " + str(summary["crossed_exact_additivity"]) +
                  "; no causal identification inferred")
    elif domain == "economics":
        new_evidence = {"effects": evidence["effects"], "weights": evidence["target_weights"],
                        "assumption": "Within-type effects transfer unchanged; not empirically checked"}
        amended_result = str(mixture(new_evidence["effects"], new_evidence["weights"]))
        scope = {"arithmetic"}
        method = "Exact target-mixture weighted sum conditional on supplied effects = " + amended_result
    else:
        new_evidence = {"policy_text": evidence["policy_text"].replace("officer", "committee"),
                        "quotation": evidence["quotation"].replace("officer", "committee")}
        amended_result = new_evidence["quotation"] in new_evidence["policy_text"]
        assert amended_result
        method = "Revised quotation found literally in revised fictional policy"
    dep2 = Target(dep.claim_id, "2", canonical_digest(new_evidence))
    p.offer(dep2, "author", {"dependency_record"})
    target2 = Target(target.claim_id, "2", canonical_digest({"evidence": new_evidence, "result": amended_result}))
    offer2 = p.offer(target2, "author", scope, (dep2,))
    c2 = p.check(offer2, "checker", scope, method,
                 "support", "New narrow classroom record only; no real measurement or decision", now=4)
    r2 = p.rely(offer2, "editor", [c2], "Revised synthetic teaching record",
                scope, kind, expires=20, now=4)
    renewed = p.currentness(r2, now=4, observed_at=4, max_age=3)
    return {"domain": domain, "calculated": calculated, "before": before,
            "after_amendment": pending, "new_version": renewed,
            "blocked_upgrade": blocked, "amended_calculation": amended_result,
            "amended_scope": sorted(scope), "events": p.events,
            "limits": case["limits"]}


def hidden_dependency_control(case):
    """Known negative control: a missing declaration cannot be traversed."""
    states = {}
    for declared in (True, False):
        p, _, dep, oid = setup(case, declare_dependency=declared)
        scope = set(case["scope"])
        c = p.check(oid, "checker", scope, "scalar rerun", "support", case["limits"], now=1)
        r = p.rely(oid, "editor", [c], "synthetic example", scope, "scientific", expires=20, now=1)
        p.amend(dep, "known planted shared calibration change", now=2)
        states["declared" if declared else "hidden"] = p.currentness(r, now=2, observed_at=2, max_age=2)
    return {"states": states, "ground_truth_affected": 2,
            "affected_marked_pending": 1, "recall": "1/2",
            "interpretation": "Declared-graph success does not imply real dependency completeness"}


def run():
    cases = fixtures()["cases"]
    return {"schema": "mcrp-domain-replay/1", "synthetic_only": True,
            "cases": [replay_case(case) for case in cases],
            "hidden_dependency_negative_control": hidden_dependency_control(cases[0])}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
