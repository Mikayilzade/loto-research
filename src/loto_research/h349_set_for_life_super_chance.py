from math import comb

MAIN_N = 47
MAIN_PICK = 5
LIFE_N = 10
LINE_COST = 1.50

PRIZES_REGULAR = {
    (5, 1): 3_600_000,
    (5, 0): 120_000,
    (4, 1): 250,
    (4, 0): 50,
    (3, 1): 30,
    (3, 0): 20,
    (2, 1): 10,
    (2, 0): 5,
}

SUPER_CHANCE_TOP_CAP = 18_000_000


def multiplicity(main_matches: int, life_match: int) -> int:
    main_count = comb(MAIN_PICK, main_matches) * comb(MAIN_N - MAIN_PICK, MAIN_PICK - main_matches)
    return main_count if life_match else main_count * (LIFE_N - 1)


def main():
    total_lines = comb(MAIN_N, MAIN_PICK) * LIFE_N
    cost = total_lines * LINE_COST
    counts = {(k, l): multiplicity(k, l) for k in range(6) for l in (0, 1)}
    assert sum(counts.values()) == total_lines

    regular_gross = sum(counts[key] * prize for key, prize in PRIZES_REGULAR.items())
    lower_gross = sum(
        counts[key] * prize
        for key, prize in PRIZES_REGULAR.items()
        if key[0] < 5
    )

    own_super_top_entries = counts[(5, 1)] + counts[(5, 0)]
    assert own_super_top_entries == 10

    print(f"total_lines={total_lines}")
    print(f"cost={cost:.2f}")
    print(f"regular_gross={regular_gross:.2f}")
    print(f"regular_return={regular_gross / cost:.12f}")
    print(f"lower_gross={lower_gross:.2f}")
    print(f"own_super_top_entries={own_super_top_entries}")

    for external_top_entries in range(0, 6):
        our_top_share = SUPER_CHANCE_TOP_CAP * own_super_top_entries / (own_super_top_entries + external_top_entries)
        gross = lower_gross + our_top_share
        profit = gross - cost
        print(
            f"external_top_entries={external_top_entries} "
            f"top_share={our_top_share:.2f} gross={gross:.2f} profit={profit:.2f}"
        )


if __name__ == "__main__":
    main()
