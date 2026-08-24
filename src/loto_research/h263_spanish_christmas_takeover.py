"""H263 exact full-issue economics for Spain Christmas Lottery 2026."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data'/'derived'/'h263_spanish_christmas_takeover.json'

SERIES=205
NUMBERS_PER_SERIES=100_000
BILLETE_EUR=200
PRIZE_SHARE=0.70


def run():
    issue=SERIES*NUMBERS_PER_SERIES*BILLETE_EUR
    prizes=int(round(issue*PRIZE_SHARE))
    return {
        'packet':'H263',
        'game':'Spain Sorteo Extraordinario de Navidad 2026',
        'series':SERIES,
        'numbers_per_series':NUMBERS_PER_SERIES,
        'billete_price_eur':BILLETE_EUR,
        'complete_issue_cost_eur':issue,
        'official_total_prize_mass_eur':prizes,
        'gross_return_ratio':prizes/issue,
        'deterministic_deficit_eur':issue-prizes,
        'minimum_external_subsidy_fraction_before_friction':1-prizes/issue,
        'guaranteed_profit_full_takeover':False,
        'interpretation':'Even impossible-perfect ownership of the complete issued inventory captures only the fixed 70% prize mass.'
    }


def main():
    d=run(); OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(d,indent=2)+'\n'); print(json.dumps(d,indent=2))

if __name__=='__main__': main()
