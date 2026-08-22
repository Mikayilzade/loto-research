from math import comb

INF = 10**18


def group_payout(group_size: int, hits: int) -> int:
    """Doubled 3-spot payout contribution under $25/$2.50 base table."""
    n3 = comb(hits, 3) if hits >= 3 else 0
    n2 = (comb(hits, 2) if hits >= 2 else 0) * (group_size - hits)
    return 50 * n3 + 5 * n2


def evaluate_partition(parts: tuple[int, ...]) -> tuple[int, int]:
    """Return (cost, exact worst-case gross) over every 20-hit allocation."""
    cost = sum(comb(g, 3) if g >= 3 else 0 for g in parts)
    dp = [INF] * 21
    dp[0] = 0
    for g in parts:
        ndp = [INF] * 21
        for used, value in enumerate(dp):
            if value >= INF:
                continue
            for hits in range(min(g, 20 - used) + 1):
                cand = value + group_payout(g, hits)
                if cand < ndp[used + hits]:
                    ndp[used + hits] = cand
        dp = ndp
    return cost, dp[20]


def partitions_k(total: int, k: int, minimum: int = 1):
    """Yield nondecreasing positive integer partitions of total into exactly k parts."""
    if k == 1:
        if total >= minimum:
            yield (total,)
        return
    for first in range(minimum, total // k + 1):
        for rest in partitions_k(total - first, k - 1, first):
            yield (first,) + rest


def main():
    for k in range(1, 9):
        tested = 0
        positive = 0
        cheapest_positive = None
        best_ratio = None
        for parts in partitions_k(80, k):
            tested += 1
            cost, gross = evaluate_partition(parts)
            ratio = gross / cost if cost else 0.0
            row = (cost, gross, ratio, parts)
            if gross > cost:
                positive += 1
                if cheapest_positive is None or cost < cheapest_positive[0]:
                    cheapest_positive = row
            if best_ratio is None or ratio > best_ratio[2]:
                best_ratio = row
        print(k, tested, positive, cheapest_positive, best_ratio)


if __name__ == "__main__":
    main()
