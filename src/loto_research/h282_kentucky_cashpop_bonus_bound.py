"""H282: Kentucky Cash Pop + August 2026 deposit-bonus worst-case bound.

This packet asks whether the current 100% first-deposit match (and even the
strongest same-day published deposit bonus stacking) can turn CASH POP Cover
All into a strict guaranteed cash profit.

The proof is deliberately stronger than checking one ticket.  In any single
CASH POP draw, a guaranteed-positive portfolio must cover all 15 possible
winning numbers.  Let s_i be total stake placed on number i.  Under the
published prize table, a legal minimum-prize assignment pays exactly 5*s_i
when i is drawn, for every permitted wager size.  Therefore

    min_i payoff_i = 5 * min_i(s_i) <= 5 * sum_i(s_i)/15 = cost/3.

The same bound adds over multi-draw portfolios.  Thus no CASH POP portfolio can
have a strict worst-case gross exceeding one third of its game spend before
external subsidies.  A 100% deposit match funds at most 2x cash deposit, so
withdrawable prize floor is <= 2/3 of deposited cash.  Even granting the
published $50 Tiki Tuesday bonus on top of a $150 first-deposit match gives
$350 playable balance from $150 cash; one-third is only $116.67.
"""
from fractions import Fraction

NUMBERS = 15
MIN_PRIZE_MULTIPLE = 5
FIRST_DEPOSIT_MATCH = Fraction(1, 1)


def cashpop_worst_case_ratio() -> Fraction:
    return Fraction(MIN_PRIZE_MULTIPLE, NUMBERS)


def prize_floor_from_wallet(wallet_spend: Fraction) -> Fraction:
    return wallet_spend * cashpop_worst_case_ratio()


def first_deposit_only(deposit: Fraction) -> tuple[Fraction, Fraction]:
    wallet = deposit * (1 + FIRST_DEPOSIT_MATCH)
    return wallet, prize_floor_from_wallet(wallet)


def tiki_stack_example() -> tuple[Fraction, Fraction, Fraction]:
    deposit = Fraction(150)
    wallet = deposit + deposit + Fraction(50)  # deliberately favorable stacking
    floor = prize_floor_from_wallet(wallet)
    return deposit, wallet, floor


def summer_friday_stack_ratio() -> Fraction:
    # Deliberately grant both first-deposit 100% match and the 25% Friday match.
    return (1 + Fraction(1) + Fraction(1, 4)) * cashpop_worst_case_ratio()


def validate() -> None:
    assert cashpop_worst_case_ratio() == Fraction(1, 3)

    # Published wager/minimum-prize pairs: every minimum is exactly 5x stake.
    for wager, minimum_prize in ((1, 5), (2, 10), (5, 25), (10, 50)):
        assert Fraction(minimum_prize, wager) == MIN_PRIZE_MULTIPLE

    # Ordinary 100% match cannot recover deposited cash in the strict worst case.
    wallet, floor = first_deposit_only(Fraction(250))
    assert wallet == 500
    assert floor == Fraction(500, 3)
    assert floor < 250

    # Even an intentionally favorable stack with the current $50 Tiki bonus fails.
    deposit, wallet, floor = tiki_stack_example()
    assert (deposit, wallet) == (150, 350)
    assert floor == Fraction(350, 3)
    assert floor < deposit

    # Hypothetical stacking of the 25% Friday match also remains below cash break-even.
    assert summer_friday_stack_ratio() == Fraction(3, 4)
    assert summer_friday_stack_ratio() < 1


if __name__ == "__main__":
    validate()
    d, w, f = tiki_stack_example()
    print({
        "packet": "H282",
        "cashpop_worst_case_wallet_return": float(cashpop_worst_case_ratio()),
        "first_deposit_100pct_cash_recovery_ceiling": float(Fraction(2, 3)),
        "tiki_favorable_stack": {"deposit": float(d), "wallet": float(w), "prize_floor": float(f)},
        "summer_friday_favorable_stack_cash_recovery_ceiling": float(summer_friday_stack_ratio()),
        "strict_guaranteed_profit": False,
    })
