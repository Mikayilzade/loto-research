"""H284: Virginia Pick 3 + advertised 50% first-deposit-match bound.

Purpose: test whether a deterministic 50% playable-balance subsidy can turn
standard Virginia Pick 3 covering portfolios into strict guaranteed cash profit.

Official Pick 3 prize table checked 2026-08-26:
https://www.valottery.com/data/draw-games/pick3
Current 50% welcome-match claim checked 2026-08-26 from multiple current
Virginia-lottery offer listings. The result below is a rejection even granting
that match in full, so uncertainty in offer entitlement cannot create a false
negative strategy claim.
"""
from fractions import Fraction
import json

# Exact base-game average gross per $1 cost from the published fixed paytable.
# For 50/50, exact-order prize includes the any-order component, so the other
# permutations receive only the any-order amount shown.
BASE = {
    "exact": Fraction(500,1000),
    "pair": Fraction(50,100),
    "any_order_3way": Fraction(3*160,1000),
    "any_order_6way": Fraction(6*80,1000),
    "fifty_fifty_3way": Fraction(330 + 2*80,1000),
    "fifty_fifty_6way": Fraction(290 + 5*40,1000),
    "combo_3way": Fraction(3*500,1000*3),
    "combo_6way": Fraction(6*500,1000*6),
}

MATCH = Fraction(1,2)
PLAYABLE_PER_CASH = 1 + MATCH
BEST_BASE = max(BASE.values())
BEST_CASH_RECOVERY = PLAYABLE_PER_CASH * BEST_BASE

# A deliberately generous FIREBALL-only ceiling. The currently published
# Pair FIREBALL line is $20 at stated odds 1 in 36; Exact is $200 at 1 in 357.
# Using 57% as an upper bound on the add-on gross ratio is more favorable than
# either of those displayed primitive ratios and still cannot cross the hurdle
# when blended with the base wager at equal stake.
FIREBALL_GENEROUS_CEILING = Fraction(57,100)
BLENDED_BASE_FIREBALL = (BEST_BASE + FIREBALL_GENEROUS_CEILING) / 2
BLENDED_CASH_RECOVERY = PLAYABLE_PER_CASH * BLENDED_BASE_FIREBALL

assert BEST_BASE == Fraction(1,2)
assert BEST_CASH_RECOVERY == Fraction(3,4)
assert BLENDED_CASH_RECOVERY < 1

out = {
    "packet":"H284",
    "game":"Virginia Pick 3",
    "assumed_deposit_match":float(MATCH),
    "base_average_gross_ratios":{k:float(v) for k,v in BASE.items()},
    "best_base_average_gross_ratio":float(BEST_BASE),
    "best_base_cash_recovery_per_deposit":float(BEST_CASH_RECOVERY),
    "fireball_generous_addon_ratio_ceiling":float(FIREBALL_GENEROUS_CEILING),
    "best_generous_blended_average_gross_ratio":float(BLENDED_BASE_FIREBALL),
    "best_generous_blended_cash_recovery_per_deposit":float(BLENDED_CASH_RECOVERY),
    "strict_profit_possible_under_tested_additive_class":False,
    "proof":"For a symmetric fixed-pay additive ticket class, minimum outcome gross <= average gross. A 50% subsidy scales playable balance by 1.5. Base Pick 3 primitives have average gross <=0.50, so any nonnegative mixture has average cash recovery <=0.75 of deposit. Even granting FIREBALL a favorable 0.57 standalone gross ceiling, equal-stake base+FIREBALL blends remain below 0.8025 of deposit."
}
print(json.dumps(out,indent=2,sort_keys=True))
