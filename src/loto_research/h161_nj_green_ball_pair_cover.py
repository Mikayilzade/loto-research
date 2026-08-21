from __future__ import annotations

PAIR_OUTCOMES = 100
WAGER = 0.50
PAIR_PRIZE = 25.00
SALES_COMMISSION = 0.05
PAYOUT_COMMISSION = 0.0125


def row(white_removed: int) -> dict[str, float | int]:
    if not 0 <= white_removed <= 6:
        raise ValueError("white_removed must be in 0..6")
    remaining_white = 6 - white_removed
    trigger_probability = 1 / (remaining_white + 1)
    strict_draw_floor = 2 if white_removed == 6 else 1
    face = PAIR_OUTCOMES * WAGER
    gross = strict_draw_floor * PAIR_PRIZE
    sales_comm = face * SALES_COMMISSION
    payout_comm = gross * PAYOUT_COMMISSION
    return {
        "white_balls_removed": white_removed,
        "green_trigger_probability": trigger_probability,
        "strict_draw_count_floor": strict_draw_floor,
        "pair_cover_face_cost_usd": face,
        "strict_prize_gross_usd": gross,
        "strict_gross_ratio": gross / face,
        "sales_commission_5pct_usd": sales_comm,
        "payout_commission_1_25pct_usd": payout_comm,
        "retailer_pre_tax_net_if_self_commission_applies_usd": gross + sales_comm + payout_comm - face,
    }


def main() -> None:
    for k in range(7):
        print(row(k))


if __name__ == "__main__":
    main()
