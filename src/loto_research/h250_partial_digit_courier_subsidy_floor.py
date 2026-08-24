"""H250: exact subsidy floors for courier-supported partial digit wagers.

The decisive structure is a finite exact partition.  A Single Digit wager fixes
one position and chooses one of ten digits, so buying all ten values guarantees
exactly one winner.  Pair and Straight covers have the same 50% deterministic
base return in the current Tri-State Pick 3 table but require more lines/capital.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'data'/'derived'/'h250_partial_digit_courier_subsidy_floor.json'


def cover(name,outcomes,line_cost,winning_payout):
    cost=outcomes*line_cost
    gross=winning_payout
    base_return=gross/cost
    return {
        'name':name,'outcomes':outcomes,'line_cost':line_cost,
        'full_cover_cost':cost,'deterministic_gross':gross,
        'deterministic_base_return':base_return,
        'strict_discount_break_even_fraction':1-base_return,
    }


def fixed_credit_net(cost,gross,credit,fees=0.0,acquisition_cost=0.0):
    return gross-max(0.0,cost-credit)-fees-acquisition_cost


def run():
    maine_retail=[
        cover('Pick3 Single Digit',10,0.50,2.50),
        cover('Pick3 Front/Back Pair',100,0.50,25.00),
        cover('Pick3 Straight',1000,0.50,250.00),
        cover('Pick4 Single Digit',10,0.50,2.50),
    ]
    lotto_me=[
        cover('Lotto.com Maine Pick3 First/Second/Third Digit',10,1.00,5.00),
        cover('Lotto.com Maine Pick3 Pair',100,1.00,50.00),
        cover('Lotto.com Maine Pick4 Single Digit',10,1.00,5.00),
    ]
    return {
        'packet':'H250','date':'2026-08-24',
        'method':'exact_full_partition_coverage_and_subsidy_threshold',
        'maine_state_minimum_wager_covers':maine_retail,
        'lotto_com_maine_minimum_wager_covers':lotto_me,
        'jackpocket_like_50cent_single_digit_formula':{
            'cost':5.0,'gross':2.5,
            'guaranteed_net':'2.50 - max(0, 5.00-B) - F - A',
            'strict_profit_for_B_le_5':'B > 2.50 + F + A',
        },
        'lotto_com_1dollar_single_digit_formula':{
            'cost':10.0,'gross':5.0,
            'guaranteed_net':'5.00 - max(0, 10.00-B) - F - A',
            'strict_profit_for_B_le_10':'B > 5.00 + F + A',
            'percentage_discount_strict_profit_before_fees':'discount > 50%',
            '25_percent_discount_net_before_fees':-2.5,
            '20_percent_discount_net_before_fees':-3.0,
        },
        'execution_observations':{
            'lotto_com_pick3_single_digit_order_menu_publicly_exposed':True,
            'lotto_com_max_lines_per_game_public_page':100,
            'pair_full_cover_fits_100_line_limit':True,
            'current_lotto_com_mystery_scratch_reward_is_random':True,
            'current_public_deterministic_subsidy_above_50_percent_found':False,
            'historical_jackpocket_5_and_10_credit_offers_expired':True,
        },
        'result':'NOT_SUCCESS_DATA_BLOCKED',
        'reason':'Courier-native exact partial-digit coverage is now evidenced, but no current deterministic non-discretionary subsidy above the 50% arithmetic hurdle (plus fees/acquisition costs) was established.',
    }


def main():
    d=run(); OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps(d,indent=2))

if __name__=='__main__': main()
