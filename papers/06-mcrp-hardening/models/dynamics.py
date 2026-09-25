"""Small analytical models, not a calibrated model of scientific communities.

Python standard library only. No identity, correctness, or adoption inference.
"""
from __future__ import annotations

import math


def probability(x: float, name: str) -> float:
    if not math.isfinite(x) or not 0 <= x <= 1:
        raise ValueError(f"{name} must be finite in [0,1]")
    return x


def imported_mass(alpha: float, ingress: float, egress: float = 0,
                  root_contamination: float = 0) -> float:
    """Exact two-block stationary mass; upper bound if ingress is a row cap.

    The bound uses egress=0 absent a guaranteed lower bound on egress.
    """
    for name, x in locals().copy().items():
        probability(x, name)
    if alpha == 1:
        raise ValueError("restart requires alpha < 1")
    return ((1-alpha)*root_contamination + alpha*ingress) / (
        1-alpha + alpha*(ingress+egress))


def stationary(transition: list[list[float]], restart: list[float],
               alpha: float, tol: float = 1e-13) -> list[float]:
    probability(alpha, "alpha")
    if alpha == 1:
        raise ValueError("restart requires alpha < 1")
    n = len(restart)
    if n == 0 or len(transition) != n:
        raise ValueError("shape")
    for row in transition + [restart]:
        if len(row) != n or any(not math.isfinite(x) or x < 0 for x in row):
            raise ValueError("shape or invalid probability")
        if abs(sum(row)-1) > 1e-10:
            raise ValueError("rows and restart must sum to one")
    p = restart[:]
    for _ in range(100000):
        nxt = [(1-alpha)*restart[j] + alpha*sum(
            p[i]*transition[i][j] for i in range(n)) for j in range(n)]
        if sum(abs(a-b) for a,b in zip(p,nxt)) < tol:
            return nxt
        p = nxt
    raise RuntimeError("not converged")


def softmax(values: list[float]) -> list[float]:
    m = max(values)
    z = [math.exp(v-m) for v in values]
    return [v/sum(z) for v in z]


def assignment(x: list[float], beta: float, chi: float,
               exploration: float, evidence: list[float]) -> list[float]:
    """Fixed K equal-sized groups; no identity creation in this toy model."""
    probability(chi, "chi")
    probability(exploration, "exploration")
    if not math.isfinite(beta) or beta < 0 or len(x) != len(evidence) or not x:
        raise ValueError("invalid feedback parameters")
    if any(not math.isfinite(v) for v in x+evidence):
        raise ValueError("nonfinite input")
    if any(v < 0 for v in x) or abs(sum(x)-1)>1e-10:
        raise ValueError("x must be a probability vector")
    p = softmax([beta*(chi*a+(1-chi)*b) for a,b in zip(x,evidence)])
    return [(1-exploration)*v+exploration/len(x) for v in p]


def trajectory(initial: list[float], beta: float, chi: float,
               exploration: float, evidence: list[float],
               steps: int = 4000, dt: float = .02) -> list[float]:
    """Euler convex updates for dx/dt = assignment(x)-x; dt in (0,1]."""
    if not 0 < dt <= 1 or steps < 1:
        raise ValueError("invalid integration")
    if any(v < 0 or not math.isfinite(v) for v in initial) or abs(sum(initial)-1)>1e-10:
        raise ValueError("initial must be a probability vector")
    x = initial[:]
    for _ in range(steps):
        a = assignment(x,beta,chi,exploration,evidence)
        x = [(1-dt)*v+dt*w for v,w in zip(x,a)]
    return x


def effective_reviewers(n: int, correlation: float) -> float:
    """Variance-equivalent sample size for equal variance/equicorrelation.

    Restrict to nonnegative correlations; not a probability of correctness.
    """
    if isinstance(n,bool) or not isinstance(n,int) or n < 1:
        raise ValueError("n must be positive integer")
    probability(correlation,"correlation")
    return n/(1+(n-1)*correlation)


def reconsideration_load(branching: float, susceptibility: float,
                         coalesce: float = 0) -> float:
    """Expected total tickets incl. initiating ticket, Galton-Watson idealization."""
    probability(susceptibility,"susceptibility")
    probability(coalesce,"coalesce")
    if not math.isfinite(branching) or branching < 0:
        raise ValueError("branching must be nonnegative")
    reproduction = branching*susceptibility*(1-coalesce)
    return 1/(1-reproduction) if reproduction < 1 else math.inf
