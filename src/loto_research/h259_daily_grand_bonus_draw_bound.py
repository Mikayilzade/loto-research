from math import comb

N_MAIN = comb(49, 5)
COST_PER_SELECTION = 3
BONUS_DRAWS = 3
BONUS_LUMP_SUM = 500_000

# Outcome counts for one fixed DAILY GRAND selection over all C(49,5)*7 draw states.
# Free Play is omitted because it is not immediate cash.
TERMS = [
    (1, 7_000_000),
    (6, 500_000),
    (comb(5,4)*comb(44,1), 1_000),
    (comb(5,4)*comb(44,1)*6, 500),
    (comb(5,3)*comb(44,2), 100),
    (comb(5,3)*comb(44,2)*6, 20),
    (comb(5,2)*comb(44,3), 10),
    (comb(5,1)*comb(44,4), 4),
]

N_STATES = N_MAIN * 7
PER_SELECTION_AVG = sum(count * prize for count, prize in TERMS) / N_STATES
COVER_COST = N_MAIN * COST_PER_SELECTION
BASE_PORTFOLIO_AVG = N_MAIN * PER_SELECTION_AVG
BONUS_MAX = BONUS_DRAWS * BONUS_LUMP_SUM
TOTAL_UPPER = BASE_PORTFOLIO_AVG + BONUS_MAX
DEFICIT = COVER_COST - TOTAL_UPPER
RATIO = TOTAL_UPPER / COVER_COST


def summary():
    return {
        'main_combinations': N_MAIN,
        'ordinary_draw_states': N_STATES,
        'cover_cost': COVER_COST,
        'per_selection_favorable_cash_average': PER_SELECTION_AVG,
        'base_portfolio_favorable_cash_average': BASE_PORTFOLIO_AVG,
        'bonus_draw_count': BONUS_DRAWS,
        'bonus_lump_sum_each': BONUS_LUMP_SUM,
        'impossible_no_sharing_bonus_max': BONUS_MAX,
        'total_average_state_upper_bound': TOTAL_UPPER,
        'gross_upper_ratio': RATIO,
        'deficit': DEFICIT,
        'strict_guaranteed_profit_possible': TOTAL_UPPER > COVER_COST,
    }


if __name__ == '__main__':
    import json
    print(json.dumps(summary(), indent=2))
