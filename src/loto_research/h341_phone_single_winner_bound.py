from dataclasses import dataclass


@dataclass(frozen=True)
class SingleWinnerPhonePromotion:
    name: str
    player_cap: int
    winners: int = 1
    external_entry_possible: bool = True

    @property
    def worst_case_gross(self) -> int:
        # If any external valid entry is legally possible, selecting it is a legal outcome.
        return 0 if self.external_entry_possible and self.winners == 1 else -1

    def strict_positive_guarantee(self, acquisition_cost: float = 0.0) -> bool:
        return self.worst_case_gross - acquisition_cost > 0


def validate():
    global_cash_call = SingleWinnerPhonePromotion("Global Cash Call 700k", 300)
    bauer_mmaw = SingleWinnerPhonePromotion("Bauer Make Me A Winner 400k", 250)

    assert global_cash_call.player_cap == 300
    assert bauer_mmaw.player_cap == 250
    assert global_cash_call.winners == 1 == bauer_mmaw.winners
    assert global_cash_call.external_entry_possible
    assert bauer_mmaw.external_entry_possible
    assert global_cash_call.worst_case_gross == 0
    assert bauer_mmaw.worst_case_gross == 0
    assert not global_cash_call.strict_positive_guarantee(0.0)
    assert not bauer_mmaw.strict_positive_guarantee(0.0)

    return {
        "global": {"cap": 300, "winners": 1, "worst_case_gross_gbp": 0},
        "bauer": {"cap": 250, "winners": 1, "worst_case_gross_gbp": 0},
        "zero_cost_strict_positive_guarantee": False,
        "arithmetic_inconclusive": 0,
        "execution_inconclusive_relevant_to_closure": 0,
    }


if __name__ == "__main__":
    print(validate())
