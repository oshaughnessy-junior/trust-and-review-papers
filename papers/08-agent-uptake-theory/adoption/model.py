"""Exact finite synthetic adoption game; no fitted scientific-agent behavior."""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import json

@dataclass(frozen=True)
class Game:
    base: tuple
    weights: tuple

    def __post_init__(self):
        n = len(self.base)
        if not 1 <= n <= 16 or len(self.weights) != n:
            raise ValueError('Require 1..16 actors and square weights')
        if any(len(row) != n for row in self.weights):
            raise ValueError('Require square weights')
        if any(not isinstance(v, (int, F)) or isinstance(v, bool)
               for v in self.base + tuple(v for row in self.weights for v in row)):
            raise ValueError('Use exact integers or Fractions')
        if any(self.weights[i][i] != 0 for i in range(n)):
            raise ValueError('Self-weight must be zero')

    def states(self):
        return product((0, 1), repeat=len(self.base))

    def margins(self, state):
        if len(state) != len(self.base) or any(v not in (0, 1) for v in state):
            raise ValueError('Invalid binary state')
        return tuple(self.base[i] + sum(w*x for w,x in zip(row,state))
                     for i,row in enumerate(self.weights))

    def response(self, state, forced=()):
        if any(i not in range(len(self.base)) for i in forced):
            raise ValueError('Invalid forced actor')
        return tuple(int(i in forced or margin > 0)
                     for i,margin in enumerate(self.margins(state)))

    def orbit(self, initial, forced=()):
        seen, path, current = {}, [], tuple(initial)
        while current not in seen:
            seen[current] = len(path)
            path.append(current)
            current = self.response(current, forced)
        return path, path[seen[current]:]

    def equilibria(self):
        """Fixed points of the declared ties-to-nonadoption policy."""
        return [x for x in self.states() if self.response(x) == x]

    def potential(self, state):
        self.margins(state)  # Apply the same state validation as response().
        if any(self.weights[i][j] != self.weights[j][i]
               for i in range(len(self.base)) for j in range(len(self.base))):
            raise ValueError('Potential requires symmetric weights')
        return (sum(b*x for b,x in zip(self.base,state)) +
                sum(self.weights[i][j]*state[i]*state[j]
                    for i in range(len(state)) for j in range(i+1,len(state))))

    def cheapest_stable_full_seed(self, costs):
        """Exhaustive toy oracle, not scalable outreach optimization."""
        if (len(costs) != len(self.base) or
            any(not isinstance(c, (int, F)) or isinstance(c, bool) or c < 0
                for c in costs)):
            raise ValueError('Require exact nonnegative actor costs')
        if any(w < 0 for row in self.weights for w in row):
            raise ValueError('Seed closure requires complements')
        target = (1,)*len(self.base)
        feasible = []
        for bits in self.states():
            seeds = tuple(i for i,b in enumerate(bits) if b)
            _,cycle = self.orbit((0,)*len(bits), seeds)
            end = cycle[0]
            if len(cycle)==1 and end==target and self.response(end)==end:
                feasible.append((sum(costs[i] for i in seeds), seeds))
        return min(feasible) if feasible else None


def fixtures():
    z=F(0); one=F(1)
    return {
        'standalone': Game((F(1,10),F(-1,2),F(-1,2)), ((z,z,z),(one,z,z),(z,one,z))),
        'coordination': Game((F(-1,2),)*2, ((z,one),(one,z))),
        'no_retention': Game((F(-2),F(-1,2)), ((z,one),(one,z))),
        'congestion': Game((F(1,2),)*2, ((z,-one),(-one,z))),
    }


def results():
    output={}
    for name,g in fixtures().items():
        lo,lc=g.orbit((0,)*len(g.base)); hi,hc=g.orbit((1,)*len(g.base))
        output[name]={'base':[str(v) for v in g.base],
                      'weights':[[str(v) for v in row] for row in g.weights],
                      'bottom_path':lo, 'bottom_cycle':lc,
                      'top_path':hi, 'top_cycle':hc, 'fixed_points':g.equilibria()}
    g=fixtures()['coordination']
    output['coordination']['mixed_orbit']=g.orbit((1,0))
    output['coordination']['cheapest_stable_full_seed']=g.cheapest_stable_full_seed((3,1))
    output['no_retention']['forced_then_release']={
        'forced':fixtures()['no_retention'].orbit((0,0),(0,)),
        'released':fixtures()['no_retention'].orbit((1,1))}
    return output

if __name__=='__main__':
    print(json.dumps(results(),indent=2))
