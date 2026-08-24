from math import comb
import json

N = 45
space = comb(N, 6)
counts = {
    "match6": 1,
    "match5_bonus": comb(6, 5),
    "match5": comb(6, 5) * (N - 7),
    "match4_bonus": comb(6, 4) * (N - 7),
    "match4": comb(6, 4) * comb(N - 7, 2),
    "match3_bonus": comb(6, 3) * comb(N - 7, 2),
    "match3": comb(6, 3) * comb(N - 7, 3),
    "match2_bonus": comb(6, 2) * comb(N - 7, 3),
}

plus1 = {
    "match6": 1_000_000,
    "match5_bonus": 5_000,
    "match5": 500,
    "match4_bonus": 50,
    "match4": 20,
    "match3_bonus": 10,
    "match3": 3,
    "match2_bonus": 2,  # generous face-value treatment of Daily Million prize
}
plus2 = {
    "match6": 1_000_000,  # announced Sep-2026 top prize
    "match5_bonus": 2_500,
    "match5": 250,
    "match4_bonus": 25,
    "match4": 10,
    "match3_bonus": 5,
    "match3": 3,
    "match2_bonus": 2,
}

def gross(table):
    return sum(counts[k] * table[k] for k in counts)

p1 = gross(plus1)
p2 = gross(plus2)
cost = space  # €1 Plus add-on per line, includes both Plus draws
out = {
    "matrix": "6/45",
    "full_space_lines": space,
    "category_counts": counts,
    "incremental_plus_cost_eur": cost,
    "plus1_gross_eur": p1,
    "plus2_gross_eur": p2,
    "combined_plus_gross_eur": p1 + p2,
    "net_eur": p1 + p2 - cost,
    "deterministic_return": (p1 + p2) / cost,
    "closed": p1 + p2 <= cost,
}
print(json.dumps(out, indent=2))
