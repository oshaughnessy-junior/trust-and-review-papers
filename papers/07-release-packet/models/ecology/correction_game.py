"""A one-step correction-credit deviation test, not a repeated-game equilibrium."""
from dataclasses import dataclass, asdict, replace
import hashlib
import json
import math
from pathlib import Path
from .ecology import probabilities

@dataclass(frozen=True)
class Game:
    scores: tuple[float,...]=(0.,0.,0.)
    author: int=0
    repairer: int=1
    exploration: float=.15
    beta: float=4.
    memory: float=.4
    attention_value: float=100.
    clean_credit: float=0.
    manufacture_cost: float=1.
    repair_units: float=20.
    effort_utility_per_unit: float=1.
    author_repair_share: float=.1
    coalition_repair_share: float=.1
    intent_detection_probability: float=0.
    enforceable_loss: float=0.
    temporary_harm: float=5.
    repair_capacity: float=20.

    def validate(self):
        if len(self.scores)<2 or any(not math.isfinite(x) or not 0<=x<=1 for x in self.scores):raise ValueError('bounded scores')
        if type(self.author) is not int or type(self.repairer) is not int or self.author==self.repairer or not 0<=self.author<len(self.scores) or not 0<=self.repairer<len(self.scores):raise ValueError('distinct valid roles')
        for field in ('exploration','memory','clean_credit','author_repair_share','coalition_repair_share','intent_detection_probability'):
            x=getattr(self,field)
            if not math.isfinite(x) or not 0<=x<=1:raise ValueError(field)
        for field in ('beta','attention_value','manufacture_cost','repair_units','effort_utility_per_unit','enforceable_loss','temporary_harm','repair_capacity'):
            x=getattr(self,field)
            if not math.isfinite(x) or x<0:raise ValueError(field)
        if self.author_repair_share>self.coalition_repair_share:raise ValueError('coalition share must include author share')


def updated_scores(game, rewards):
    return tuple((1-game.memory)*s+game.memory*min(1,max(0,r)) for s,r in zip(game.scores,rewards))


def outcome(game=Game(), policy='author_and_repairer'):
    game.validate()
    if policy not in {'author_and_repairer','repairer_only','no_correction_credit'}:raise ValueError('policy')
    n=len(game.scores); clean=[0.]*n; clean[game.author]=game.clean_credit
    manufactured=[0.]*n
    if policy=='author_and_repairer':manufactured[game.author]=1.
    if policy!='no_correction_credit':manufactured[game.repairer]=1.
    clean_scores=updated_scores(game,clean)
    changed_scores=updated_scores(game,manufactured)
    clean_p=probabilities(clean_scores,game.exploration,game.beta)
    changed_p=probabilities(changed_scores,game.exploration,game.beta)
    feasible=game.repair_units<=game.repair_capacity
    author_gain=game.attention_value*(changed_p[game.author]-clean_p[game.author])
    coalition_gain=game.attention_value*sum(changed_p[i]-clean_p[i] for i in (game.author,game.repairer))
    expected_loss=game.intent_detection_probability*game.enforceable_loss
    author_cost=game.manufacture_cost+game.author_repair_share*game.repair_units*game.effort_utility_per_unit+expected_loss
    coalition_cost=game.manufacture_cost+game.coalition_repair_share*game.repair_units*game.effort_utility_per_unit+expected_loss
    # Resource harm is a separate social-cost proxy. The attention reward merely
    # redistributes a fixed opportunity pool and is not counted as social benefit.
    social_cost=game.manufacture_cost+game.repair_units*game.effort_utility_per_unit+game.temporary_harm
    return {'config':asdict(game),'policy':policy,'feasible_completed_repair':feasible,
            'clean_probabilities':clean_p,'manufactured_probabilities_if_repaired':changed_p,
            'clean_scores':clean_scores,'manufactured_scores_if_repaired':changed_scores,
            'author_attention_gain':author_gain,'author_private_cost':author_cost,
            'author_deviation_gain_if_repaired':author_gain-author_cost,
            'coalition_attention_gain':coalition_gain,'coalition_private_cost':coalition_cost,
            'coalition_deviation_gain_if_repaired':coalition_gain-coalition_cost,
            'author_manufacture_profitable':feasible and author_gain>author_cost,
            'coalition_manufacture_profitable':feasible and coalition_gain>coalition_cost,
            'scarce_repair_units_if_completed':game.repair_units,
            'remaining_repair_capacity_if_completed':game.repair_capacity-game.repair_units if feasible else None,
            'incremental_social_cost_proxy_if_repaired':social_cost,
            'note':'Conditional completed-repair payoffs only. Infeasibility blocks this path, not every deviation. Intent detection is not ordinary defect detection.'}


def main():
    root=Path(__file__).parent
    cases={'default':Game(), 'full_internalization':replace(Game(),author_repair_share=1,coalition_repair_share=1),
           'credible_enforcement':replace(Game(),intent_detection_probability=.5,enforceable_loss=50),
           'insufficient_independent_capacity':replace(Game(),repair_capacity=15),
           'verified_clean_baseline':replace(Game(),clean_credit=1),
           'full_exploration':replace(Game(),exploration=1)}
    results={name:{p:outcome(g,p) for p in ('author_and_repairer','repairer_only','no_correction_credit')} for name,g in cases.items()}
    source_paths=[Path(__file__),root/'ecology.py',root/'tests/test_correction_game.py']
    artifact={'schema':'mcrp-correction-game/0.1','evidence_class':'T/I conditional one-step model',
              'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths},'results':results}
    (root/'results/correction-game.json').write_text(json.dumps(artifact,indent=2,sort_keys=True)+'\n')
    print('Wrote correction-game.json; one-step incentives, not equilibrium or human behavior.')

if __name__=='__main__':main()
