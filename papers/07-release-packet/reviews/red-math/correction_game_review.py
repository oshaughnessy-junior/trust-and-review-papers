"""Independent payoff reconstruction for the correction-credit deviation game."""
from pathlib import Path
import hashlib,json,math,sys
ROOT=Path(__file__).resolve().parent;PACKET=ROOT.parent.parent
sys.path.insert(0,str(PACKET))
from models.ecology.correction_game import Game,outcome

def independent(game,policy):
    g=game;n=len(g.scores)
    clean_score=[(1-g.memory)*s+g.memory*(g.clean_credit if i==g.author else 0) for i,s in enumerate(g.scores)]
    rewarders=({g.author,g.repairer} if policy=='author_and_repairer' else ({g.repairer} if policy=='repairer_only' else set()))
    deviation_score=[(1-g.memory)*s+g.memory*(i in rewarders) for i,s in enumerate(g.scores)]
    def allocation(score):
        terms=[math.exp(g.beta*s) for s in score];normalizer=sum(terms)
        return [g.exploration/n+(1-g.exploration)*x/normalizer for x in terms]
    p0,p1=allocation(clean_score),allocation(deviation_score)
    author=g.attention_value*(p1[g.author]-p0[g.author])-g.manufacture_cost-g.author_repair_share*g.repair_units*g.effort_utility_per_unit-g.intent_detection_probability*g.enforceable_loss
    coalition=g.attention_value*sum(p1[i]-p0[i] for i in (g.author,g.repairer))-g.manufacture_cost-g.coalition_repair_share*g.repair_units*g.effort_utility_per_unit-g.intent_detection_probability*g.enforceable_loss
    return p0,p1,author,coalition

def main():
    source=PACKET/'models/ecology/correction_game.py'
    saved=json.loads((source.parent/'results/correction-game.json').read_text());checks=[]
    for case,policies in saved['results'].items():
        for policy,old in policies.items():
            cfg=old['config'].copy();cfg['scores']=tuple(cfg['scores']);g=Game(**cfg)
            fresh=outcome(g,policy)
            assert json.loads(json.dumps(fresh))==old
            p0,p1,author,coalition=independent(g,policy)
            assert max(abs(x-y) for x,y in zip(p0,old['clean_probabilities']))<1e-12
            assert max(abs(x-y) for x,y in zip(p1,old['manufactured_probabilities_if_repaired']))<1e-12
            assert abs(author-old['author_deviation_gain_if_repaired'])<1e-12
            assert abs(coalition-old['coalition_deviation_gain_if_repaired'])<1e-12
            assert abs(sum(p1)-sum(p0))<1e-12
            assert old['feasible_completed_repair']==(g.repair_units<=g.repair_capacity)
            checks.append({'case':case,'policy':policy,'author_gain':author,'coalition_gain':coalition})
    report={'interpretation':'Independent reconstruction of conditional one-step payoffs; not equilibrium verification','checked_outcomes':len(checks),'all_outcomes':checks,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
    (ROOT/'correction-game-review-results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
