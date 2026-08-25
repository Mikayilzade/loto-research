"""H280: conditional New Hampshire 200% promo + Pick 3 Front Pair cover arithmetic.

This module deliberately separates arithmetic from execution certification.
The currently advertised third-party NHMAX offer is not treated as authoritative
Lottery terms; see research/H280_STATUS.md.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'data' / 'derived' / 'h280_nh_200pct_match_pick3_cover.json'

PAIR_COUNT = 100
WAGER = 1.0
PAIR_PRIZE = 50.0
MATCH_RATE = 2.0
BONUS_CAP = 100.0


def evaluate(deposit: float) -> dict:
    bonus = min(MATCH_RATE * deposit, BONUS_CAP)
    wallet = deposit + bonus
    cover_cost = PAIR_COUNT * WAGER
    feasible_wallet = wallet >= cover_cost
    guaranteed_prize = PAIR_PRIZE if feasible_wallet else 0.0
    return {
        'deposit': deposit,
        'bonus': bonus,
        'wallet': wallet,
        'cover_cost': cover_cost,
        'feasible_wallet': feasible_wallet,
        'guaranteed_prize_if_full_cover_accepted': guaranteed_prize,
        'cash_profit_if_full_cover_accepted': guaranteed_prize - deposit if feasible_wallet else None,
        'profit_pct_on_deposit': ((guaranteed_prize / deposit) - 1.0) * 100 if feasible_wallet else None,
    }


def main():
    # $34 is the smallest whole-dollar deposit that funds a $100 cover under a 200% match.
    r = evaluate(34.0)
    assert r['bonus'] == 68.0
    assert r['wallet'] == 102.0
    assert r['cover_cost'] == 100.0
    assert r['guaranteed_prize_if_full_cover_accepted'] == 50.0
    assert r['cash_profit_if_full_cover_accepted'] == 16.0
    assert abs(r['profit_pct_on_deposit'] - 47.058823529411775) < 1e-12
    payload = {
        'packet': 'H280',
        'model': 'conditional 200% deposit match + one-copy 00-99 Front Pair cover',
        'official_pick3_fact': 'NH Pick 3 Front Pair pays $50 on a $1 bet; 100 possible pairs.',
        'conditional_offer_fact': 'Third-party current advertisement claims 200% deposit match up to $100.',
        'example': r,
        'execution_certified': False,
        'reason_not_success': 'NH official terms reserve purchase refusal/number-limit rights; offer-specific 200% code terms are not authoritative public Lottery terms.',
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + '\n')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
