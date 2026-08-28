"""H326 exact arithmetic for LLF Games £350 cash finite-pool postal takeover screen."""

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class Case:
    total_tickets: int = 350
    prize_gbp: float = 350.0
    online_price_gbp: float = 1.99
    second_class_postage_gbp: float = 0.91
    max_per_person: int = 35
    sold_snapshot: int = 10


def compute(case: Case = Case()) -> dict:
    full_online_cost = case.total_tickets * case.online_price_gbp
    full_postal_cost = case.total_tickets * case.second_class_postage_gbp
    remaining = case.total_tickets - case.sold_snapshot
    remaining_postal_cost = remaining * case.second_class_postage_gbp
    minimum_external_ids_now = max(0, case.sold_snapshot - case.max_per_person)
    uncontrollable_ids_even_from_zero = case.total_tickets - case.max_per_person

    result = {
        **asdict(case),
        "full_online_cost_gbp": round(full_online_cost, 2),
        "full_online_gross_ratio": case.prize_gbp / full_online_cost,
        "full_postal_cost_gbp": round(full_postal_cost, 2),
        "full_postal_gross_ratio": case.prize_gbp / full_postal_cost,
        "full_postal_surplus_gbp": round(case.prize_gbp - full_postal_cost, 2),
        "remaining_tickets": remaining,
        "remaining_postal_cost_gbp": round(remaining_postal_cost, 2),
        "remaining_postal_gross_ratio_if_all_remaining_controlled": case.prize_gbp / remaining_postal_cost,
        "remaining_postal_surplus_if_all_remaining_controlled_gbp": round(case.prize_gbp - remaining_postal_cost, 2),
        "player_cap_share": case.max_per_person / case.total_tickets,
        "uncontrollable_ids_even_from_zero": uncontrollable_ids_even_from_zero,
        "minimum_external_ids_now_if_all_allowed_entries_were_already_ours": minimum_external_ids_now,
        "strict_one_player_guaranteed_cash_floor_gbp": 0.0,
    }

    assert result["full_postal_gross_ratio"] > 1.0
    assert result["full_online_gross_ratio"] < 1.0
    assert case.max_per_person < case.total_tickets
    assert uncontrollable_ids_even_from_zero > 0
    assert result["strict_one_player_guaranteed_cash_floor_gbp"] == 0.0
    return result


if __name__ == "__main__":
    import json
    print(json.dumps(compute(), indent=2, sort_keys=True))
