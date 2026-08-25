"""H278: Georgia Lottery 50% first-deposit bonus exact-cover screen.

Reproducible arithmetic for small/finite fixed-payout draw constructions under
the current iHOPE first-deposit promotion.  The promotion turns D dollars of
cash deposit into at most 1.5*D dollars of restricted lottery purchasing power.
For a strict cash-profit guarantee, a construction spending matched funds must
therefore have a deterministic payout ratio > 2/3 of wagered funds.
"""
from math import comb
import json

BONUS_MULTIPLIER = 1.5
BREAK_EVEN_WAGER_RATIO = 1 / BONUS_MULTIPLIER

# Georgia FIVE exact mutually-exclusive payout classification relative to a
# fixed winning 5-digit outcome.  Symmetry makes the full-cover gross invariant.
def georgia_five_payout(ticket):
    m = [d == 0 for d in ticket]
    if all(m): return 10000
    if all(m[:4]) or all(m[1:]): return 225
    if all(m[:3]) and m[4]: return 21
    if m[0] and all(m[2:]): return 21
    if all(m[:2]) and all(m[3:]): return 20
    if all(m[:3]) or all(m[2:]): return 20
    if all(m[:2]) and m[4]: return 11
    if m[0] and all(m[3:]): return 11
    if all(m[:2]) or all(m[3:]): return 10
    if m[0] and m[4]: return 2
    if m[0] or m[4]: return 1
    return 0

# Current base KENO! table, $1 wager.  Missing matches pay zero.
KENO_BASE = {
    10:{10:100000,9:5000,8:500,7:50,6:10,5:2,0:5},
    9:{9:30000,8:3000,7:150,6:25,5:5,4:1},
    8:{8:10000,7:500,6:75,5:10,4:2},
    7:{7:4000,6:125,5:15,4:3,3:1},
    6:{6:1200,5:50,4:7,3:1},
    5:{5:400,4:17,3:2},
    4:{4:70,3:5,2:1},
    3:{3:25,2:2},
    2:{2:10},
    1:{1:2},
}

# Total KENO! + BULLS-EYE payout when selected combination contains the
# BULLS-EYE among its matched winning numbers.  Add-on doubles base cost.
KENO_BULLSEYE_TOTAL = {
    10:{10:300000,9:25000,8:2000,7:150,6:35,5:7,4:3,3:2,2:2,1:5},
    9:{9:80000,8:7000,7:500,6:70,5:20,4:5,3:2,2:2,1:5},
    8:{8:50000,7:1400,6:200,5:30,4:10,3:2,2:2,1:5},
    7:{7:10000,6:400,5:80,4:15,3:5,2:2,1:5},
    6:{6:3000,5:140,4:30,3:10,2:3,1:5},
    5:{5:1000,4:70,3:15,2:5,1:5},
    4:{4:350,3:25,2:12,1:5},
    3:{3:125,2:20,1:8},
    2:{2:65,1:15},
    1:{1:50},
}

# Current online CASH POP minimum assigned prize is 5x wager.  Covering all 15
# draw numbers therefore has an exact worst-case ratio 5/15 = 1/3 regardless
# of the random prize assignments revealed after purchase.
CASH_POP_WORST_COVER_RATIO = 1/3


def keno_base_cover_ratio(k):
    gross = 0
    for t, prize in KENO_BASE[k].items():
        if 0 <= t <= k:
            gross += comb(20, t) * comb(60, k-t) * prize
    return gross / comb(80, k)


def keno_bullseye_cover_ratio(k):
    gross = 0
    for t in range(k+1):
        non_be = comb(19, t) * comb(60, k-t) if t <= 19 else 0
        has_be = comb(19, t-1) * comb(60, k-t) if t >= 1 else 0
        gross += non_be * KENO_BASE[k].get(t, 0)
        gross += has_be * KENO_BULLSEYE_TOTAL[k].get(t, 0)
    return gross / (2 * comb(80, k))


def main():
    from itertools import product
    gf_gross = sum(georgia_five_payout(t) for t in product(range(10), repeat=5))
    gf_ratio = gf_gross / 100000
    rows = []
    for k in range(1,11):
        b = keno_base_cover_ratio(k)
        be = keno_bullseye_cover_ratio(k)
        rows.append({
            'spot': k,
            'base_cover_ratio': b,
            'base_ratio_vs_cash_deposit_with_50pct_bonus': BONUS_MULTIPLIER*b,
            'bullseye_cover_ratio': be,
            'bullseye_ratio_vs_cash_deposit_with_50pct_bonus': BONUS_MULTIPLIER*be,
        })
    best_base = max(rows, key=lambda r:r['base_cover_ratio'])
    best_be = max(rows, key=lambda r:r['bullseye_cover_ratio'])
    out = {
        'packet':'H278',
        'bonus_multiplier':BONUS_MULTIPLIER,
        'strict_profit_wager_ratio_hurdle':BREAK_EVEN_WAGER_RATIO,
        'georgia_five_full_cover_gross':gf_gross,
        'georgia_five_full_cover_cost':100000,
        'georgia_five_cover_ratio':gf_ratio,
        'georgia_five_ratio_vs_cash_deposit':BONUS_MULTIPLIER*gf_ratio,
        'cash_pop_all15_worst_cover_ratio':CASH_POP_WORST_COVER_RATIO,
        'cash_pop_ratio_vs_cash_deposit':BONUS_MULTIPLIER*CASH_POP_WORST_COVER_RATIO,
        'keno':rows,
        'best_base_keno':best_base,
        'best_bullseye_keno':best_be,
        'multiplier_guarantee_note':'MULTIPLIER doubles cost and has a legal None branch, so it cannot improve the deterministic floor.',
        'closure':'No checked compact exact-cover route crosses the >2/3 wager-return hurdle required by a 50% matched restricted bankroll.',
    }
    assert gf_gross == 53650
    assert abs(gf_ratio-0.5365) < 1e-12
    assert best_base['spot'] == 7
    assert best_base['base_cover_ratio'] < BREAK_EVEN_WAGER_RATIO
    assert best_be['bullseye_cover_ratio'] < BREAK_EVEN_WAGER_RATIO
    assert CASH_POP_WORST_COVER_RATIO < BREAK_EVEN_WAGER_RATIO
    print(json.dumps(out, indent=2))

if __name__ == '__main__':
    main()
