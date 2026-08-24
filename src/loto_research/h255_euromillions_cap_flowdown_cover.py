"""H255: EuroMillions cap-overflow lower-tier deterministic cover.

At a flow-down cap draw, excess Jackpot Pool money above the cap is allocated to
the next lower prize tier with at least one winner.  This script computes the
smallest Lucky-Star edge family that, for a fixed exact 5-main-number set,
guarantees at least one Match 5 + 1 Lucky Star play for every possible winning
Lucky-Star pair.

The star problem is total edge domination of K_12: every winning edge e must
have a purchased edge f sharing exactly one endpoint with e.  The optimum is 8.
A simple lower bound is certificate-grade: selected edges must cover >=11
vertices (else an edge between two uncovered vertices is undominated), and no
selected-edge component may consist of one isolated edge (a selected edge must
itself have an adjacent selected edge).  With m edges, components have >=2
edges, so they cover at most m + floor(m/2) vertices.  m<=7 covers at most 10;
therefore m>=8. Four disjoint P3 components attain 8 while covering all 12
vertices, hence the bound is tight.
"""
from __future__ import annotations
import json, math
from itertools import combinations
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data'/'derived'/'h255_euromillions_cap_flowdown_cover.json'
STAR_VERTICES=12
IRISH_LINE_COST=2.50
CORE_GAME_COMPONENT=2.20

def construction():
    # Four disjoint 2-edge paths on all 12 Lucky-Star vertices.
    return [(0,1),(1,2),(3,4),(4,5),(6,7),(7,8),(9,10),(10,11)]

def verify_total_edge_domination(chosen):
    all_edges=list(combinations(range(STAR_VERTICES),2))
    bad=[]
    for e in all_edges:
        if not any(len(set(e)&set(f))==1 for f in chosen):
            bad.append(e)
    return bad

def run():
    chosen=construction(); bad=verify_total_edge_domination(chosen); assert not bad
    lower_bound=8
    # Proof: m<=7 -> at most m+floor(m/2)<=10 covered vertices, but >=11 required.
    assert 7+7//2==10
    main_sets=math.comb(50,5)
    lines=main_sets*len(chosen)
    full_space=main_sets*math.comb(12,2)
    return {
        'packet':'H255',
        'mechanism':'EuroMillions flow-down-cap excess to next lower winning tier',
        'main_number_space':main_sets,
        'lucky_star_pairs':math.comb(12,2),
        'full_line_space':full_space,
        'minimum_star_pairs_per_exact_main_set_for_guaranteed_match5_plus1':lower_bound,
        'explicit_star_pair_cover':[list(x) for x in chosen],
        'star_cover_verified_for_all_66_winning_pairs':True,
        'deterministic_match5_plus1_cover_lines':lines,
        'irish_mandatory_cost_per_line_eur':IRISH_LINE_COST,
        'irish_total_cover_cost_eur':lines*IRISH_LINE_COST,
        'core_game_component_cost_eur':CORE_GAME_COMPONENT,
        'core_component_equivalent_cost_eur':lines*CORE_GAME_COMPONENT,
        'strict_profit_guarantee':False,
        'blocking_reasons':[
            'rules specify flow-down of the amount above the cap but no positive fixed minimum excess amount',
            'Match 5+1 prizes are pari-mutuel and depend on the number of winning external plays, so captured share has no execution-grade positive lower bound',
            'Irish purchase is bundled with Ireland Only Raffle at 2.50 EUR per line; EuroMillions cannot be bought alone',
            'operator rules permit restricting participation that interferes with other players reasonable access, adding an execution blocker at 16,950,080 lines'
        ]
    }

def main():
    out=run(); OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
