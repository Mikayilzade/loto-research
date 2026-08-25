"""H264: Uganda LOTTO fixed-tier / special-roll-down structural screen.

Current Uganda LOTTO rules (v1.6) use a 6/52 matrix at UGX 1,000 per entry.
Prize divisions 7 (Match 3) and 8 (Match 2 + Bonus) are fixed at UGX 10,000 and
UGX 4,000 per winning entry. The special jackpot roll-down rule explicitly
excludes fixed-payout divisions, so accumulated jackpot money cannot create the
NEXT-ACTION target of an external pool paid as a deterministic fixed amount per
lower-tier winning selection.
"""
from __future__ import annotations
import json
from math import comb
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data'/'derived'/'h264_uganda_lotto_fixed_tier_rolldown.json'

def main():
    total=comb(52,6); price=1000; losing=45
    counts={
        'match6':1,
        'match5_bonus':comb(6,5),
        'match5':comb(6,5)*losing,
        'match4_bonus':comb(6,4)*losing,
        'match4':comb(6,4)*comb(losing,2),
        'match3_bonus':comb(6,3)*comb(losing,2),
        'match3':comb(6,3)*comb(losing,3),
        'match2_bonus':comb(6,2)*comb(losing,3),
    }
    fixed=counts['match3']*10000+counts['match2_bonus']*4000
    out={'packet':'H264','game':'Uganda National Lottery LOTTO','rules_version':'1.6','matrix':'6/52 + bonus','entry_price_ugx':price,'participant_daily_wager_cap_ugx':500000,'full_cover_entries':total,'full_cover_cost_ugx':total*price,'exact_category_counts_under_one_copy_full_cover':counts,'fixed_tiers':{'division_7_match3_ugx':10000,'division_8_match2_bonus_ugx':4000},'fixed_tier_full_cover_gross_ugx':fixed,'fixed_tier_return_ratio':fixed/(total*price),'special_roll_down_reaches_fixed_tiers':False,'reason':'Rules 7.2 and 7.3 explicitly exclude fixed payout divisions from special Division-1 roll-down; ordinary Division-6 no-winner funds roll to next-draw Division 1, not Division 7.','status':'REJECTED_AS_FIXED_PER_SELECTION_EXTERNAL_SUBSIDY_MECHANISM'}
    assert total==20358520 and counts['match3']==283800 and counts['match2_bonus']==212850
    assert fixed==3689400000
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
