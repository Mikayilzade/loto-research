"""H256: exact NJ Quick Draw Progressive Bonus Hours full-cover screen."""
from math import comb
import json

BASE = {
10:{10:100000,9:5000,8:300,7:45,6:10,5:2,0:5},
9:{9:30000,8:3000,7:125,6:22,5:5,4:1},
8:{8:10000,7:400,6:60,5:10,4:2},
7:{7:2500,6:100,5:15,4:3,3:1},
6:{6:1000,5:45,4:7,3:1},
5:{5:300,4:20,3:2},
4:{4:55,3:5,2:1},
3:{3:23,2:2},
2:{2:10},
1:{1:2},
}
BULL = {
10:{10:200000,9:15000,8:1200,7:105,6:15,5:4,4:3,3:2,2:2,1:5},
9:{9:40000,8:2000,7:175,6:38,5:15,4:4,3:2,2:2,1:5},
8:{8:15000,7:800,6:140,5:20,4:6,3:2,2:2,1:5},
7:{7:5500,6:200,5:45,4:11,3:4,2:2,1:5},
6:{6:1500,5:85,4:18,3:7,2:3,1:5},
5:{5:450,4:30,3:13,2:5,1:5},
4:{4:245,3:15,2:9,1:5},
3:{3:77,2:16,1:8},
2:{2:45,1:15},
1:{1:44},
}
BOTH = {
10:{10:900000,9:45000,8:2700,7:255,6:70,5:14,4:8,3:5,2:5},
9:{9:120000,8:7000,7:1075,6:128,5:30,4:14,3:5,2:5},
8:{8:90000,7:3100,6:440,5:40,4:13,3:5,2:5},
7:{7:27500,6:900,5:160,4:25,3:7,2:5},
6:{6:6500,5:355,4:83,3:17,2:8},
5:{5:2200,4:180,3:43,2:12},
4:{4:945,3:95,2:44},
3:{3:477,2:73},
2:{2:390},
1:{},
}


def C(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def screen(k):
    n = C(80, k)
    base_gross = bull_gross = double_gross = 0
    for m in range(k + 1):
        # Ordinary full cover.
        base_gross += C(20, m) * C(60, k - m) * BASE[k].get(m, 0)

        # One Bullseye among the 20 drawn numbers.
        with_bull = C(19, m - 1) * C(60, k - m)
        without_bull = C(19, m) * C(60, k - m)
        bull_gross += with_bull * BULL[k].get(m, 0)
        bull_gross += without_bull * BASE[k].get(m, 0)

        # Two Bullseyes among the 20 drawn numbers.
        for b in (0, 1, 2):
            count = C(2, b) * C(18, m - b) * C(60, k - m)
            prize = BASE[k].get(m, 0) if b == 0 else BULL[k].get(m, 0) if b == 1 else BOTH[k].get(m, 0)
            double_gross += count * prize

    base_return = base_gross / n
    bull_return = bull_gross / (2 * n)
    double_return = double_gross / (3 * n)
    return {
        "spot": k,
        "combinations": n,
        "base_return": base_return,
        "base_promo_return": 1.5 * base_return,
        "bullseye_return": bull_return,
        "bullseye_promo_return": 1.5 * bull_return,
        "double_bullseye_return": double_return,
        "double_bullseye_promo_return": 1.5 * double_return,
    }


def main():
    rows = [screen(k) for k in range(1, 11)]
    best_base = max(rows, key=lambda r: r["base_promo_return"])
    best_bull = max(rows, key=lambda r: r["bullseye_promo_return"])
    best_double = max(rows, key=lambda r: r["double_bullseye_promo_return"])
    out = {
        "hypothesis": "NJ Quick Draw Progressive 50% Bonus Hours can create guaranteed-profit controlled full coverage",
        "status": "rejected",
        "bonus_multiplier": 1.5,
        "rows": rows,
        "best_base": best_base,
        "best_bullseye": best_bull,
        "best_double_bullseye": best_double,
        "required_base_uplift_best": 1 / best_base["base_return"] - 1,
        "multiplier_worst_legal_factor": 1,
        "multiplier_worst_branch_best_fixed_return": best_base["base_promo_return"] / 2,
        "progressive_jackpot_guaranteed_floor": 0,
        "all_fixed_full_covers_below_one": all(
            r[x] < 1
            for r in rows
            for x in ("base_promo_return", "bullseye_promo_return", "double_bullseye_promo_return")
        ),
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
