"""Small conditional MCRP models, not identity, truth, or governance services.

Standard library only. Group labels are declared; all numerical units are explicit
at the call site. Exact panel probabilities use Fraction. No network or filesystem
side effects occur on import.
"""
from fractions import Fraction
from itertools import combinations
import math


def finite(value, name, lower=0.0, upper=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number, not a boolean")
    if not math.isfinite(value) or value < lower or (upper is not None and value > upper):
        raise ValueError(f"{name} outside permitted interval")
    return float(value)


def integer(value, name, lower=1):
    if isinstance(value, bool) or not isinstance(value, int) or value < lower:
        raise ValueError(f"{name} must be an integer >= {lower}")
    return value


def panel_distribution(group_counts, size, policy="group_first"):
    """Exact distribution over declared-group panels after eligibility filtering.

    Baseline group_first samples uniform size-k group subsets then representatives.
    naive samples uniform feasible representative panels (one per declared group).
    Counts model interchangeable eligible representatives, not fresh expertise.
    """
    integer(size, "panel size")
    if not isinstance(group_counts, dict) or not group_counts:
        raise ValueError("nonempty group mapping required")
    for group, count in group_counts.items():
        if not isinstance(group, str) or not group:
            raise ValueError("group keys must be nonempty strings")
        integer(count, "representative count")
    if size > len(group_counts):
        raise ValueError("coverage unavailable: too few declared groups")
    if policy not in ("group_first", "naive"):
        raise ValueError("unknown panel policy")
    weights = {}
    for panel in combinations(sorted(group_counts), size):
        weights[panel] = 1 if policy == "group_first" else math.prod(group_counts[g] for g in panel)
    total = sum(weights.values())
    return {panel: Fraction(weight, total) for panel, weight in weights.items()}


def inclusion(distribution, group):
    return sum((p for panel, p in distribution.items() if group in panel), Fraction(0))


def completion_bound(offered_cap, risky_completion_upper, other_completion_lower):
    """Bound completed-category share under a strictly positive other completion floor."""
    epsilon = finite(offered_cap, "offered cap", upper=1)
    upper = finite(risky_completion_upper, "completion upper", upper=1)
    lower = finite(other_completion_lower, "completion lower", upper=1)
    if epsilon >= 1 or lower <= 0:
        raise ValueError("require offered cap < 1 and other completion floor > 0")
    return epsilon*upper/(epsilon*upper+(1-epsilon)*lower)


def retry_summary(offer_risk, risk_completion, other_completion, max_attempts,
                  invitation_cost=1.0, completion_cost=0.0):
    """IID reoffers, stop at first completed panel or deterministic attempt limit.

    Costs are units per attempted invitation and per completed panel. Setup and
    stand-by costs need separate additions. Category is an artificial binary label.
    """
    p = finite(offer_risk, "offered risk", upper=1)
    a = finite(risk_completion, "risk completion", upper=1)
    b = finite(other_completion, "other completion", upper=1)
    limit = integer(max_attempts, "max attempts")
    ci = finite(invitation_cost, "invitation cost")
    cc = finite(completion_cost, "completion cost")
    success = p*a + (1-p)*b
    attempts = sum((1-success)**j for j in range(limit))
    completed = success*attempts
    return {"offered_risk": p, "success_per_attempt": success,
            "completed_risk": p*a/success if success else None,
            "completion_probability": completed,
            "unresolved_probability": (1-success)**limit,
            "expected_attempts": attempts,
            "expected_refusals": attempts-completed,
            "expected_retry_attempts": attempts-1,
            "expected_cost": ci*attempts+cc*completed}


def row_mul(vector, matrix):
    return [sum(vector[i]*matrix[i][j] for i in range(len(vector)))
            for j in range(len(vector))]


def validated_family(matrices, weights):
    if not isinstance(weights, (list, tuple)) or not weights:
        raise ValueError("nonempty weight vector required")
    w = [finite(x, "weight") for x in weights]
    if min(w) <= 0:
        raise ValueError("weights must be strictly positive")
    if not isinstance(matrices, (list, tuple)) or not matrices:
        raise ValueError("nonempty matrix family required")
    family = []
    for matrix in matrices:
        if not isinstance(matrix, (list, tuple)) or len(matrix) != len(w):
            raise ValueError("matrix shape mismatch")
        if any(not isinstance(row, (list, tuple)) or len(row) != len(w) for row in matrix):
            raise ValueError("matrix shape mismatch")
        family.append([[finite(x, "matrix entry") for x in row] for row in matrix])
    return family, w


def envelope(matrices, weights):
    """Find contraction factor for supplied positive linear Lyapunov witness.

    Failure of this witness does not establish instability or nonexistence of any
    other witness. Workloads must use the same row-vector orientation as row_mul.
    """
    family, w = validated_family(matrices, weights)
    ratios = [sum(row[j]*w[j] for j in range(len(w)))/w[i]
              for matrix in family for i, row in enumerate(matrix)]
    r = max(ratios)
    return {"factor": r, "certified": r < 1,
            "meaning": "conditional expected weighted offspring contraction"}


def repair_bound(initial, matrices, weights):
    family, w = validated_family(matrices, weights)
    if not isinstance(initial, (list, tuple)) or len(initial) != len(w):
        raise ValueError("initial shape mismatch")
    z = [finite(x, "initial work") for x in initial]
    certificate = envelope(family, w)
    if not certificate["certified"]:
        raise ValueError("supplied common envelope is not subcritical")
    return sum(x*y for x, y in zip(z, w))/(1-certificate["factor"])


def shared_capacity(commitments, capacities):
    """Check aggregate commitments by (person, epoch), across all declared lanes.

    A commitment is (person, epoch, lane, hours). Skills/authority/deadlines are
    external feasibility conditions, not inferred here. Never drop unknown people.
    """
    if not isinstance(capacities, dict):
        raise ValueError("capacity mapping required")
    caps = {}
    for key, value in capacities.items():
        if not isinstance(key, tuple) or len(key) != 2 or any(not isinstance(x, str) or not x for x in key):
            raise ValueError("capacity key must be (person, epoch)")
        caps[key] = finite(value, "capacity")
    used = {key: 0.0 for key in caps}
    for row in commitments:
        if not isinstance(row, (list, tuple)) or len(row) != 4:
            raise ValueError("commitment requires person, epoch, lane, hours")
        person, epoch, lane, hours = row
        if not all(isinstance(x, str) and x for x in (person, epoch, lane)):
            raise ValueError("commitment identifiers required")
        key = (person, epoch)
        if key not in caps:
            raise ValueError("commitment has no declared capacity")
        used[key] += finite(hours, "hours")
    return {"feasible": all(used[k] <= caps[k] for k in caps),
            "rows": [{"person": k[0], "epoch": k[1], "used": used[k],
                      "capacity": caps[k], "slack": caps[k]-used[k]} for k in sorted(caps)]}


def audit_interval(effort_cost, reward, loss, false_positive, detection,
                   outside, invitations, audit_cost, budget):
    """One-shot honest vs shirk vs abstain interval under expected audit spending.

    A funded audit is assumed actually delivered; detection and enforceable loss
    are exogenous. The result is weak best-response feasibility, not an equilibrium.
    """
    c, R, F, u = [finite(x, n) for x, n in
                  ((effort_cost, "effort cost"), (reward, "reward"), (loss, "loss"), (outside, "outside"))]
    alpha = finite(false_positive, "false positive", upper=1)
    beta = finite(detection, "detection", upper=1)
    n = integer(invitations, "invitations")
    a, B = finite(audit_cost, "audit cost"), finite(budget, "budget")
    discrimination = (beta-alpha)*F
    lower = 0.0 if c == 0 else (c/discrimination if discrimination > 0 else math.inf)
    participation = ((R-c-u)/(alpha*F) if alpha*F else (1.0 if R-c >= u else -math.inf))
    upper = min(1.0, B/(n*a) if a else 1.0, participation)
    if c == 0 and discrimination < 0:
        upper = min(upper, 0.0)
    feasible = 0 <= lower <= upper
    return {"feasible": feasible, "minimum_audit": lower if math.isfinite(lower) else None,
            "maximum_audit": upper if math.isfinite(upper) else None,
            "budget_kind": "expected audit expenditure",
            "reason": "nonempty weak best-response interval" if feasible else "incentive, participation or budget conflict"}


def action_utilities(q, effort_cost, reward, loss, false_positive, detection, outside=0.0):
    vals = [finite(x, n) for x, n in ((effort_cost,"effort"),(reward,"reward"),(loss,"loss"),(outside,"outside"))]
    c, R, F, u = vals
    q, alpha, beta = [finite(x, n, upper=1) for x,n in ((q,"audit"),(false_positive,"false positive"),(detection,"detection"))]
    return {"honest": R-c-q*alpha*F, "shirk": R-q*beta*F, "abstain": u}


def wilson(successes, trials, z=1.959963984540054):
    integer(trials, "trials")
    integer(successes, "successes", lower=0)
    if successes > trials:
        raise ValueError("successes exceed trials")
    finite(z, "z")
    p = successes/trials
    den = 1+z*z/trials
    center = (p+z*z/(2*trials))/den
    half = z*math.sqrt(p*(1-p)/trials+z*z/(4*trials*trials))/den
    return [0.0 if successes == 0 else max(0,center-half),
            1.0 if successes == trials else min(1,center+half)]


def exact_nonnegative(value, name, upper=None):
    """Exact decimal/rational input semantics; floats are parsed by displayed decimal."""
    if isinstance(value, bool) or not isinstance(value, (int, float, str, Fraction)):
        raise ValueError(name + ' must be a finite decimal or rational')
    try:
        result = value if isinstance(value, Fraction) else Fraction(str(value))
    except (ValueError, ZeroDivisionError, OverflowError) as error:
        raise ValueError(name + ' must be finite') from error
    if result < 0 or (upper is not None and result > upper):
        raise ValueError(name + ' outside permitted interval')
    return result


def hard_audit_interval(effort_cost, reward, loss, false_positive, detection,
                        outside, invitations, audit_cost, budget):
    """Exact weak-incentive interval for a blinded, identical-cost hard audit cap.

    Use the *_exact rational strings for decisions. Float fields are convenience
    displays; maximum_audit is rounded downward to remain sampler-compatible.
    """
    c, R, F, u, a, B = [exact_nonnegative(x, n) for x, n in
        ((effort_cost,'effort'),(reward,'reward'),(loss,'loss'),(outside,'outside'),
         (audit_cost,'audit cost'),(budget,'budget'))]
    alpha = exact_nonnegative(false_positive, 'false positive', 1)
    beta = exact_nonnegative(detection, 'detection', 1)
    n = integer(invitations, 'invitations')
    max_count = n if a == 0 else min(n, int(B // a))
    discrimination = (beta-alpha)*F
    lower = Fraction(0) if c == 0 else (c/discrimination if discrimination > 0 else None)
    upper = Fraction(max_count, n)
    if alpha*F:
        upper = min(upper, (R-c-u)/(alpha*F))
    elif R-c < u:
        upper = Fraction(-1)
    if c == 0 and discrimination < 0:
        upper = min(upper, Fraction(0))
    feasible = lower is not None and 0 <= lower <= upper
    upper_display = float(upper)
    while Fraction(str(upper_display)) > upper:
        upper_display = math.nextafter(upper_display, -math.inf)
    return {'feasible': feasible,
            'minimum_audit': None if lower is None else float(lower),
            'maximum_audit': upper_display,
            'minimum_audit_exact': None if lower is None else str(lower),
            'maximum_audit_exact': str(upper),
            'maximum_audit_count': max_count,
            'budget_kind': 'hard identical-cost audit count cap',
            'numeric_semantics': 'exact fields authoritative; decimal floats interpreted via str',
            'reason': 'nonempty weak best-response interval' if feasible else
                      'incentive, participation or hard budget conflict'}


def blinded_audit_sample(invitations, q, audit_cost, budget, rng):
    """Equal marginal rational q; pathwise count cost <= budget under fixed cost.

    Mix adjacent integer counts using an exact rational Bernoulli draw, then a
    uniform subset. Caller supplies concealment and actual audit delivery.
    """
    n = integer(invitations, 'invitations')
    q = exact_nonnegative(q, 'q', 1)
    a, B = exact_nonnegative(audit_cost, 'audit cost'), exact_nonnegative(budget, 'budget')
    max_count = n if a == 0 else min(n, int(B // a))
    target = q*n
    if target > max_count:
        raise ValueError('marginal exceeds hard audit count cap')
    low = target.numerator//target.denominator
    remainder = target-low
    count = low + int(rng.randrange(remainder.denominator) < remainder.numerator)
    return sorted(rng.sample(range(n), count))
