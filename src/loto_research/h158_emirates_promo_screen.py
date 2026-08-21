from math import comb


def easy6_full_cover():
    n, k = 39, 6
    tickets = comb(n, k)
    face_cost = tickets * 6
    # Favorable screen: assign our cover the entire advertised shared amount
    # in 6/5/4 plus fixed $1 for every 3-match ticket.
    m3 = comb(6, 3) * comb(33, 3)
    favorable_gross = 4_000_000 + 25_000 + 4_000 + m3
    return tickets, face_cost, m3, favorable_gross


def main():
    tickets, face_cost, m3, gross = easy6_full_cover()
    cases = {
        "face": face_cost,
        "onam_30pct": face_cost * 0.70,
        "buy6_get3": face_cost * (6 / 9),
    }
    print("EASY6 tickets", tickets)
    print("match3 tickets", m3)
    print("favorable gross", gross)
    for name, cost in cases.items():
        print(name, "cost", cost, "ratio", gross / cost)

    sure = [
        ("SURE1", 5000, 2623, 10, 30000, 1),
        ("SURE2", 5000, 2666, 15, 50000, 1),
        ("SURE3", 20000, 7857, 30, 360000, 5),
    ]
    for name, total, remaining, price, pool, winners in sure:
        external = total - remaining
        rem_cost = remaining * price
        strict_floor = 0 if external >= winners else None
        expected_gross = remaining / total * pool
        print(
            name,
            "external", external,
            "remaining_cost", rem_cost,
            "nominal_pool_margin", pool - rem_cost,
            "strict_floor", strict_floor,
            "expected_pool_return", expected_gross / rem_cost,
        )


if __name__ == "__main__":
    main()
