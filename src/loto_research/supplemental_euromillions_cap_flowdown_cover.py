"""Supplemental EuroMillions cap-overflow lower-tier deterministic cover.

For a fixed exact 5-main-number set, guaranteeing at least one Match 5+1 Lucky
Star line for every possible winning Lucky-Star pair is total edge domination
of K_12. The exact optimum is 8 edges.
"""
from __future__ import annotations
import json, math
from itertools import combinations
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data'/'derived'/'supplemental_euromillions_cap_flowdown_cover.json'

def construction():
    return [(0,1),(1,2),(3,4),(4,5),(6,7),(7,8),(9,10),(10,11)]

def verify(chosen):
    bad=[]
    for e in combinations(range(12),2):
        if not any(len(set(e)&set(f))==1 for f in chosen): bad.append(e)
    return bad

def run():
    chosen=construction(); assert not verify(chosen)
    assert 7+7//2==10  # lower-bound certificate: m=7 cannot cover required >=11 vertices
    main_sets=math.comb(50,5); lines=main_sets*8
    return {
      'packet':'SUPPLEMENTAL-EUROMILLIONS-CAP-FLOWDOWN-20260824',
      'minimum_star_pairs_per_exact_main_set':8,
      'explicit_cover':[list(x) for x in chosen],
      'verified_all_66_winning_star_pairs':True,
      'main_number_space':main_sets,
      'deterministic_match5_plus1_cover_lines':lines,
      'irish_mandatory_cost_per_line_eur':2.5,
      'irish_total_cover_cost_eur':lines*2.5,
      'full_line_space':main_sets*math.comb(12,2),
      'strict_profit_guarantee':False,
      'blocker':'cap excess has no fixed positive minimum and Match5+1 is pari-mutuel with no hard external-winner multiplicity bound'
    }

def main():
    out=run(); OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))

if __name__=='__main__': main()
