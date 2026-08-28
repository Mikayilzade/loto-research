from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class H345Result:
    total_ids: int = 20_000
    ticket_price_gbp: float = 10.00
    per_person_cap: int = 1_000
    advertised_min_prize_gbp: float = 2.00
    second_class_postage_gbp: float = 0.91
    accepted_entry_postage_only_floor_gbp: float = 1.09
    dispatch_without_acceptance_floor_gbp: float = -0.91
    arithmetic_inconclusive: int = 0
    closure_relevant_acceptance_inconclusive: int = 0
    state: str = "CLOSED_NOT_SUCCESS"


def compute() -> H345Result:
    accepted = round(2.00 - 0.91, 2)
    rejected = round(0.00 - 0.91, 2)
    assert accepted == 1.09
    assert rejected == -0.91
    assert 20_000 > 1_000 > 0
    return H345Result(
        accepted_entry_postage_only_floor_gbp=accepted,
        dispatch_without_acceptance_floor_gbp=rejected,
    )


if __name__ == "__main__":
    print(json.dumps(asdict(compute()), indent=2, sort_keys=True))
