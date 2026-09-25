"""Independent domain counterexamples; synthetic, standard library only.

Run from any directory. Outputs describe model boundaries, not human outcomes.
The additive-label probe records the installed oracle's behavior, so it also
shows a later repair without treating a known counterexample as a failed test.
"""
from fractions import Fraction as F
import copy
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "domains" / "fixtures"))
from domain_models import biology_model, fixtures


def run():
    # E[epsilon]=0 does not imply E[epsilon|T]=0.
    rows = [(F(0), F(-1, 2)), (F(1), F(1, 2))]
    assert sum(e for _, e in rows) / 2 == 0
    assert all(e != 0 for _, e in rows)
    # Equal observed conditional contrasts need not identify a causal effect:
    # Y=10+2B+U, T=U in the observed population, has no T causal coefficient.
    observed = [(t, b, 10 + 2 * b + t) for b in (0, 1) for t in (0, 1)]
    assert observed == [(0, 0, 10), (1, 0, 11), (0, 1, 12), (1, 1, 13)]
    bio = copy.deepcopy(next(c for c in fixtures()["cases"] if c["domain"] == "biology")["evidence"])
    bio["crossed_rows"] = [[0, 0, 10], [1, 0, 11], [0, 1, 12], [1, 1, 15]]
    try:
        oracle = biology_model(bio)
    except ValueError as exc:
        oracle = {"rejected": str(exc)}
    # Selection at reliance can undo any completion-stage representation claim.
    completed_adverse, completed_other = 10, 90
    relied_adverse, relied_other = 10, 0
    return {
        "synthetic_only": True,
        "unconditional_mean_zero_is_insufficient": {
            "mean_error": "0", "conditional_errors": [str(e) for _, e in rows],
            "required_assumption": "E[epsilon|T,B]=0 for the displayed conditional-mean identity",
        },
        "crossed_observations_do_not_establish_causation": {
            "observed_rows": observed, "within_batch_contrasts": [1, 1],
            "structural_countermodel": "Y=10+2B+U; observed T=U; intervention on T leaves U unchanged",
            "causal_effect_under_countermodel": 0,
        },
        "interaction_probe": {"within_batch_contrasts": [1, 3], "average_contrast": 2,
                              "single_exact_additive_effect_exists": False, "installed_oracle": oracle},
        "reliance_selection": {
            "completed_adverse_share": str(F(completed_adverse, completed_adverse + completed_other)),
            "relied_adverse_share": str(F(relied_adverse, relied_adverse + relied_other)),
            "interpretation": "A completion-stage bound is not a reliance-stage bound",
        },
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
