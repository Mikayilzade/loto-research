"""H277: exact full-space / portfolio-average bound for Millionaire for Life.

Uses the current 5-of-58 + 1-of-5 matrix and $5 price.  The top two
published cash options are deliberately treated as fixed no-sharing values,
which is player-favourable because official rules allow pari-mutuel reduction.
If even this dominating model has average gross below cost, no nonnegative
portfolio can guarantee strict profit: minimum draw gross <= average draw gross.
"""
from math import comb
import json

WHITE_N = 58
WHITE_PICK = 5
MB_N = 5
PRICE = 5

PAYOUT = {
    (5, 1): 18_000_000,  # published top-prize cash option, dominating no-sharing model
    (5, 0): 2_200_000,   # published second-prize cash option, dominating no-sharing model
    (4, 1): 7_500,
    (4, 0): 500,
    (3, 1): 250,
    (3, 0): 50,
    (2, 1): 25,
    (2, 0): 8,
    (1, 1): 8,
}


def multiplicity(k: int, mb_match: int) -> int:
    white = comb(WHITE_PICK, k) * comb(WHITE_N - WHITE_PICK, WHITE_PICK - k)
    return white if mb_match else white * (MB_N - 1)


def compute():
    universe = comb(WHITE_N, WHITE_PICK) * MB_N
    counts = {(k, mb): multiplicity(k, mb) for k in range(WHITE_PICK + 1) for mb in (0, 1)}
    assert sum(counts.values()) == universe == 22_910_580
    cost = universe * PRICE
    contributions = {key: counts[key] * prize for key, prize in PAYOUT.items()}
    gross = sum(contributions.values())
    ratio = gross / cost
    assert cost == 114_552_900
    assert gross == 60_584_320
    assert ratio < 1
    return {
        "packet": "H277",
        "game": "Millionaire for Life",
        "matrix": {"white_choose": 5, "white_from": 58, "millionaire_ball_from": 5},
        "price_per_play_usd": PRICE,
        "outcome_space": universe,
        "full_cover_cost_usd": cost,
        "dominating_no_sharing_full_cover_gross_usd": gross,
        "dominating_return_ratio": ratio,
        "dominating_return_percent": 100 * ratio,
        "deficit_usd": cost - gross,
        "multiplicities": {f"{k}+{'MB' if mb else 'noMB'}": counts[(k, mb)] for k in range(6) for mb in (1, 0)},
        "gross_contributions_usd": {f"{k}+{'MB' if mb else 'noMB'}": contributions[(k, mb)] for (k, mb) in PAYOUT},
        "proof": "By draw symmetry every single play has the same average gross under the dominating payout table. Any nonnegative portfolio has the same gross/cost average ratio. Since minimum legal-draw gross is at most average gross and average gross is below cost, no such portfolio can guarantee strict profit. Actual pari-mutuel reductions can only weaken this bound.",
    }


if __name__ == "__main__":
    print(json.dumps(compute(), indent=2, sort_keys=True))
