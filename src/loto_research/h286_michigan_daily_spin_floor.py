"""H286: strict cash-floor model for Michigan Daily Spin to Win."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data'/'derived'/'h286_michigan_daily_spin_floor.json'

prize_classes={
    'in_store_free_play': {'guaranteed_withdrawable_cash_floor': 0.0, 'reason':'noncash free-play coupon'},
    'online_free_play_or_bonus': {'guaranteed_withdrawable_cash_floor': 0.0, 'reason':'not guaranteed Bonus Cash; free-play/bonus value requires play'},
    'monthly_giveaway_entry': {'guaranteed_withdrawable_cash_floor': 0.0, 'reason':'legal later drawing outcome in which entry is not selected'},
}

floor=min(v['guaranteed_withdrawable_cash_floor'] for v in prize_classes.values())
assert floor == 0.0

out={
    'packet':'H286',
    'mechanism':'Michigan Lottery Daily Spin to Win guaranteed-reward cash-floor audit',
    'every_spin_wins_a_prize':True,
    'prize_classes':prize_classes,
    'strict_withdrawable_cash_floor_per_spin':floor,
    'strict_positive_cash_floor':floor>0,
    'conclusion':'CLOSED / REJECTED for strict guaranteed-profit use',
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
