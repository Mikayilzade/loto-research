"""H269: exact full-identifier takeover bound for Svenska Spel Joker.

Current Joker uses seven decimal digits.  For a fixed drawn Joker number, a
candidate identifier is characterized only by the 7-bit mask of positions that
match the draw.  Each mask has multiplicity 9**(# mismatches).  A maximal run
of L>=2 matching positions earns the fixed L-right prize; disjoint runs can
both pay, while a digit cannot be reused.  Enumerating the 128 masks therefore
exactly represents all 10,000,000 identifiers without materializing them.
"""
from itertools import product
import json
from pathlib import Path

PRIZE = {2: 40, 3: 80, 4: 500, 5: 10_000, 6: 100_000, 7: 10_000_000}
JOKER_STAKE = 10
MIN_LOTTO_ROW_COST = 4
IDENTIFIERS = 10_000_000


def payout(mask):
    runs = []
    i = 0
    while i < 7:
        if not mask[i]:
            i += 1
            continue
        j = i
        while j < 7 and mask[j]:
            j += 1
        length = j - i
        if length >= 2:
            runs.append(length)
        i = j
    return sum(PRIZE[length] for length in runs)


def calculate():
    distribution = {}
    total_identifiers = 0
    total_gross = 0
    winning_identifiers = 0
    for mask in product((0, 1), repeat=7):
        multiplicity = 9 ** (7 - sum(mask))
        pay = payout(mask)
        distribution[pay] = distribution.get(pay, 0) + multiplicity
        total_identifiers += multiplicity
        total_gross += multiplicity * pay
        if pay:
            winning_identifiers += multiplicity

    assert total_identifiers == IDENTIFIERS
    assert total_gross == 39_664_000
    assert winning_identifiers == 544_870
    joker_cost = IDENTIFIERS * JOKER_STAKE
    minimum_combined_cost = IDENTIFIERS * (JOKER_STAKE + MIN_LOTTO_ROW_COST)
    result = {
        "packet": "H269",
        "game": "Svenska Spel Joker with Lotto",
        "identifier_space": IDENTIFIERS,
        "joker_stake_sek": JOKER_STAKE,
        "mandatory_minimum_lotto_row_cost_sek": MIN_LOTTO_ROW_COST,
        "joker_only_full_cover_cost_sek": joker_cost,
        "minimum_combined_full_identifier_acquisition_cost_sek": minimum_combined_cost,
        "exact_joker_fixed_plan_gross_sek": total_gross,
        "joker_fixed_plan_return_on_joker_stake": total_gross / joker_cost,
        "joker_fixed_plan_return_on_minimum_combined_spend": total_gross / minimum_combined_cost,
        "winning_identifiers_for_any_draw": winning_identifiers,
        "winning_identifier_fraction": winning_identifiers / IDENTIFIERS,
        "payout_distribution_identifier_counts": {str(k): v for k, v in sorted(distribution.items())},
        "closure": "Exact full Joker-identifier takeover is economically below cost even before considering execution; mandatory Lotto base cost only worsens the fixed-plan takeover ratio.",
    }
    return result


if __name__ == "__main__":
    result = calculate()
    out = Path(__file__).resolve().parents[2] / "data" / "derived" / "h269_svenska_spel_joker_full_identifier_bound.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
