"""H236: exact full-space threshold for a doubled 3-spot 20/80 Keno promotion.

For every 3-subset of 80 purchased once, the draw contains 20 winning numbers.
The number of tickets matching j spots is deterministically C(20,j)C(60,3-j).
If only 2/3 and 3/3 pay P2 and P3 dollars per $1 base wager and a promotion
doubles every winning prize without doubling ticket cost, doubled full-space gross is
2*(N2*P2 + N3*P3). This script reports the exact break-even inequality.
"""
from math import comb
import json

N = {j: comb(20, j) * comb(60, 3-j) for j in range(4)}
SPACE = comb(80, 3)
assert sum(N.values()) == SPACE == 82160
# 2*(11400*P2 + 1140*P3) > 82160
# divide by 2280: 10*P2 + P3 > 82160/2280
threshold = SPACE / (2 * N[3])

out = {
    "packet": "H236",
    "game_structure": "3-spot Keno, choose 3 of 80, draw 20",
    "full_space_lines": SPACE,
    "exact_match_counts": {str(k): v for k, v in N.items()},
    "doubled_full_space_gross_formula": "2*(11400*P2 + 1140*P3)",
    "strict_profit_condition": "10*P2 + P3 > 36.03508771929825",
    "threshold_rhs": threshold,
}
print(json.dumps(out, indent=2))
