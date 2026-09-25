"""Deterministic domain oracles. Invented inputs; no inference about real data.

Run from any directory. Uses exact rational arithmetic except displayed square
roots. No network, files written, random sampling, or third-party dependencies.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def canonical_digest(evidence):
    raw = json.dumps(evidence, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=True, allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def fixtures():
    return json.loads((HERE / "scenarios.json").read_text())


def rational(value):
    return F(str(value))


def physics_model(evidence):
    n = evidence["n"]
    if type(n) is not int or n <= 0:
        raise ValueError("positive integer repeat count required")
    tau, sigma = map(rational, (evidence["shared_sd"], evidence["individual_sd"]))
    if tau < 0 or sigma < 0:
        raise ValueError("nonnegative standard deviations required")
    shared = tau * tau + sigma * sigma / n
    mistaken = (tau * tau + sigma * sigma) / n
    x, old, new = map(rational, (evidence["raw"], evidence["old_gain"], evidence["new_gain"]))
    if old <= 0 or new <= 0:
        raise ValueError("positive gain required for this model")
    return {"shared_variance": str(shared), "mistaken_variance": str(mistaken),
            "shared_standard_error": math.sqrt(float(shared)),
            "mistaken_standard_error": math.sqrt(float(mistaken)),
            "old_amplitude": str(x / old), "new_amplitude": str(x / new),
            "variance_floor": str(tau * tau)}


def rss(rows, mu, beta, gamma):
    return sum((rational(y) - mu - beta * t - gamma * b) ** 2 for t, b, y in rows)


def crossed_summary(crossed):
    """Exact four-cell arithmetic; does not establish a causal interpretation."""
    cells = {(t, b): rational(y) for t, b, y in crossed}
    if len(cells) != len(crossed) or set(cells) != {(0, 0), (1, 0), (0, 1), (1, 1)}:
        raise ValueError("one row per crossed cell required")
    contrasts = [cells[1, b] - cells[0, b] for b in (0, 1)]
    exact_additivity = contrasts[0] == contrasts[1]
    return {"crossed_within_batch_differences": [str(x) for x in contrasts],
            "crossed_average_contrast": str(sum(contrasts) / len(contrasts)),
            "crossed_exact_additivity": exact_additivity,
            "crossed_additive_effect": str(contrasts[0]) if exact_additivity else None}


def biology_model(evidence):
    rows = evidence["confounded_rows"]
    if not rows or not all(t == b for t, b, _ in rows):
        raise ValueError("this oracle requires the displayed perfect-confounding case")
    controls = [rational(y) for t, _, y in rows if t == 0]
    treated = [rational(y) for t, _, y in rows if t == 1]
    return {"confounded_mean_difference": str(sum(treated) / len(treated) - sum(controls) / len(controls)),
            "rss_treatment_explanation": str(rss(rows, F(10), F(2), F(0))),
            "rss_batch_explanation": str(rss(rows, F(10), F(0), F(2))),
            "separate_effect_identified_in_confounded_design": False,
            **crossed_summary(evidence["crossed_rows"])}


def mixture(effects, weights):
    if set(effects) != set(weights):
        raise ValueError("target support missing: do not silently renormalize")
    w = {s: rational(x) for s, x in weights.items()}
    if any(x < 0 for x in w.values()) or sum(w.values()) != 1:
        raise ValueError("weights must form a probability distribution")
    return sum(w[s] * rational(effects[s]) for s in w)


def economics_model(evidence):
    q, ca, ch = map(rational, (evidence["adverse_offer_share"], evidence["adverse_completion"], evidence["other_completion"]))
    if any(x < 0 or x > 1 for x in (q, ca, ch)):
        raise ValueError("probabilities must lie in [0,1]")
    total = q * ca + (1 - q) * ch
    share = None if total == 0 else q * ca / total
    # Separate finite-count example: final reliance can select again even if
    # allocation and completion already meet their stated representation bound.
    selection = evidence["reliance_selection"]
    counts = [selection[k] for k in ("completed_adverse", "completed_other", "relied_adverse", "relied_other")]
    if any(type(x) is not int or x < 0 for x in counts):
        raise ValueError("nonnegative integer counts required")
    ac, hc, ar, hr = counts
    if ar > ac or hr > hc:
        raise ValueError("relied cases must be drawn from completed cases")
    return {"trial_effect": str(mixture(evidence["effects"], evidence["trial_weights"])),
            "target_effect_conditional_on_transport": str(mixture(evidence["effects"], evidence["target_weights"])),
            "completion_probability": str(total),
            "adverse_completed_share": None if share is None else str(share),
            "adverse_completed_share_float": None if share is None else float(share),
            "separate_reliance_example": {
                "completed_adverse_share": str(F(ac, ac + hc)) if ac + hc else None,
                "relied_adverse_share": str(F(ar, ar + hr)) if ar + hr else None}}


def schedule(jobs, order):
    """One unit-rate nonpreemptive handler, all jobs released at zero."""
    by_id = {j["id"]: j for j in jobs}
    if len(by_id) != len(jobs) or len(set(order)) != len(order) or set(order) != set(by_id):
        raise ValueError("order must contain every distinct job exactly once")
    time, result = 0, []
    for jid in order:
        j = by_id[jid]
        if type(j["effort"]) is not int or j["effort"] <= 0 or type(j["deadline"]) is not int or j["deadline"] <= 0:
            raise ValueError("positive integer effort/deadline required")
        time += j["effort"]
        result.append({"id": jid, "finish": time, "deadline": j["deadline"],
                       "missed": time > j["deadline"]})
    return result


def law_model(evidence):
    jobs = evidence["feasible_jobs"]
    impossible = evidence["infeasible_jobs"]
    return {"fifo": schedule(jobs, ["A", "B"]),
            "deadline_order": schedule(jobs, ["B", "A"]),
            "infeasible_earliest_first": schedule(impossible, ["C", "D"]),
            "all_times_are_synthetic_ticks": True,
            "statutory_calendar_implemented": False}


MODELS = {"physics": physics_model, "biology": biology_model,
          "economics": economics_model, "law": law_model}


def run():
    data = fixtures()
    result = {"schema": "mcrp-domain-oracles/1", "synthetic_only": True,
              "scenario_file_sha256": hashlib.sha256((HERE / "scenarios.json").read_bytes()).hexdigest(),
              "results": {}}
    for case in data["cases"]:
        result["results"][case["domain"]] = {
            "evidence_digest": canonical_digest(case["evidence"]),
            **MODELS[case["domain"]](case["evidence"])}
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
