"""H267: exact full-ticket-pool worst-case bound for Lucky Lotteries.

Uses the current Tattersall's Rules of Authorised Lotteries in force from
18 May 2025.  The calculation intentionally grants an impossible-perfect
one-player buyout of every unique ticket identifier in a draw.  The jackpot
is *not* guaranteed by ownership of all identifiers: it is won only when the
separately drawn Jackpot Number is one of the cash-prize Winning Numbers.
Therefore the legal no-jackpot branch gives a rigorous full-buyout floor.

Free-ticket consolation prizes are valued at their rules-defined cash
equivalent excluding commission, which is favourable to the player.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h267_lucky_lotteries_full_buyout_bound.json"


def product(name, tickets, retail_price, subscription, cash_levels, cash_consolation,
            free_ticket_multiplicity, free_ticket_subscription):
    cash_prizes = sum(amount * count for amount, count in cash_levels)
    free_entries = sum(mult * count for mult, count in free_ticket_multiplicity)
    # This branch is the legal branch in which the Jackpot Number is not itself
    # one of the cash-prize Winning Numbers, so the jackpot-number consolation
    # is included and the accumulated Jackpot Prize is not paid.
    guaranteed_nonjackpot_gross = cash_prizes + cash_consolation + free_entries * free_ticket_subscription
    retail_full_buyout_cost = tickets * retail_price
    subscription_full_buyout_cost = tickets * subscription
    return {
        "name": name,
        "ticket_pool": tickets,
        "retail_price": retail_price,
        "subscription_excluding_commission": subscription,
        "retail_full_buyout_cost": retail_full_buyout_cost,
        "subscription_full_buyout_cost": subscription_full_buyout_cost,
        "cash_prizes": cash_prizes,
        "cash_consolation": cash_consolation,
        "free_ticket_equivalent_entries": free_entries,
        "free_ticket_cash_equivalent": free_entries * free_ticket_subscription,
        "legal_no_jackpot_full_buyout_gross": guaranteed_nonjackpot_gross,
        "retail_floor_return": guaranteed_nonjackpot_gross / retail_full_buyout_cost,
        "subscription_only_floor_return": guaranteed_nonjackpot_gross / subscription_full_buyout_cost,
        "retail_deficit": retail_full_buyout_cost - guaranteed_nonjackpot_gross,
        "jackpot_not_forced_by_full_buyout": True,
    }


def main():
    super_jackpot = product(
        "Lucky Lotteries Super Jackpot",
        270_000,
        2.20,
        2.00,
        [
            (100_000, 1), (10_000, 1), (5_000, 1), (500, 2), (200, 10),
            (100, 20), (50, 100), (25, 600), (15, 750), (10, 2_480),
        ],
        2_000,  # two $1,000 consolation prizes around 1st Prize
        [
            (25, 2), (15, 2), (10, 4), (5, 20), (3, 40), (2, 200),
            (1, 1_200), (1, 1_500), (1, 4_960), (10, 1),
        ],
        2.00,
    )
    mega_jackpot = product(
        "Lucky Lotteries Mega Jackpot",
        200_000,
        5.50,
        5.00,
        [
            (200_000, 1), (20_000, 1), (5_000, 1), (1_000, 5), (500, 10),
            (100, 25), (75, 75), (40, 600), (20, 700), (12, 2_800),
        ],
        2_000,
        [
            (25, 2), (15, 2), (10, 10), (5, 20), (3, 50), (2, 150),
            (1, 1_200), (1, 1_400), (1, 5_600), (10, 1),
        ],
        5.00,
    )
    out = {
        "packet": "H267",
        "mechanism": "finite unique ticket-pool full-buyout / accumulated jackpot",
        "rules_effective_from": "2025-05-18",
        "products": [super_jackpot, mega_jackpot],
        "strict_result": "REJECTED",
        "reason": (
            "Even impossible ownership of every unique identifier has a legal draw branch where the "
            "Jackpot Number is not a cash-prize Winning Number. On that branch the accumulated jackpot "
            "is not paid, and guaranteed cash plus cash-equivalent free tickets is far below acquisition cost."
        ),
    }
    assert super_jackpot["cash_prizes"] == 176_050
    assert super_jackpot["free_ticket_equivalent_entries"] == 8_410
    assert super_jackpot["legal_no_jackpot_full_buyout_gross"] == 194_870
    assert abs(super_jackpot["retail_floor_return"] - 0.32806397306397306) < 1e-15
    assert mega_jackpot["cash_prizes"] == 314_725
    assert mega_jackpot["free_ticket_equivalent_entries"] == 8_940
    assert mega_jackpot["legal_no_jackpot_full_buyout_gross"] == 361_425
    assert abs(mega_jackpot["retail_floor_return"] - 0.3285681818181818) < 1e-15
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
