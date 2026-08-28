from dataclasses import dataclass


@dataclass(frozen=True)
class H339Input:
    total_ids: int = 37_500
    instant_win_ids: int = 18_750
    second_class_postage_gbp: float = 0.91


def compute(inp: H339Input = H339Input()):
    zero_instant_ids = inp.total_ids - inp.instant_win_ids
    assert inp.total_ids == 37_500
    assert inp.instant_win_ids == 18_750
    assert zero_instant_ids == 18_750
    assert zero_instant_ids / inp.total_ids == 0.5

    # A single postal entry can legally receive any zero-instant ID.
    single_postal_worst_instant_cash_gbp = 0.0
    single_postal_worst_net_gbp = (
        single_postal_worst_instant_cash_gbp - inp.second_class_postage_gbp
    )
    assert single_postal_worst_net_gbp == -0.91

    return {
        "total_ids": inp.total_ids,
        "instant_win_ids": inp.instant_win_ids,
        "zero_instant_ids": zero_instant_ids,
        "zero_instant_fraction": zero_instant_ids / inp.total_ids,
        "second_class_postage_gbp": inp.second_class_postage_gbp,
        "single_postal_worst_instant_cash_gbp": single_postal_worst_instant_cash_gbp,
        "single_postal_worst_net_gbp": single_postal_worst_net_gbp,
        "arithmetic_inconclusive": 0,
        "full_multi_entry_candidate_closed": False,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(compute(), indent=2, sort_keys=True))
