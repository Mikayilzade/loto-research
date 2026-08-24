from math import comb

LINES = comb(45, 6)
PRICE = 2
SPEND = LINES * PRICE
CAP = 16_000_000
MATCH3 = comb(6, 3) * comb(38, 3)
MATCH2_BONUS = comb(6, 2) * comb(38, 3)
FIXED_FLOOR = 4 * (MATCH3 + MATCH2_BONUS)


def guaranteed_floor(external_jackpot_winners: int) -> float:
    return CAP / (external_jackpot_winners + 1) + FIXED_FLOOR - SPEND


if __name__ == "__main__":
    print({
        "lines": LINES,
        "spend": SPEND,
        "fixed_floor": FIXED_FLOOR,
        "k0_net_floor": guaranteed_floor(0),
        "k1_net_floor": guaranteed_floor(1),
        "k2_net_floor": guaranteed_floor(2),
    })
