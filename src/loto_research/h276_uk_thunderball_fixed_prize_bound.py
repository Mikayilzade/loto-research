"""H276: exact UK Thunderball fixed-prize portfolio bound.

Current checked structure: choose 5 of 39 main numbers and 1 of 14 Thunderballs,
GBP 1 per line. All prize tiers are fixed per winning line. By symmetry every
line has the same average gross over the complete draw universe, so any
nonnegative portfolio has the same average return ratio. Therefore its minimum
legal-outcome gross cannot exceed that average.
"""
from math import comb
import json

MAIN_N=39
MAIN_K=5
TB_N=14
PRICE=1
PAYOUT={(5,1):500000,(5,0):5000,(4,1):250,(4,0):100,
        (3,1):20,(3,0):10,(2,1):10,(1,1):5,(0,1):3}


def solve():
    universe=comb(MAIN_N,MAIN_K)*TB_N
    rows=[]; gross=0; count_sum=0
    for k in range(MAIN_K,-1,-1):
        main_count=comb(MAIN_K,k)*comb(MAIN_N-MAIN_K,MAIN_K-k)
        for tb_match in (1,0):
            count=main_count*(1 if tb_match else TB_N-1)
            prize=PAYOUT.get((k,tb_match),0)
            tier_gross=count*prize
            rows.append({"main_matches":k,"thunderball_match":bool(tb_match),
                         "ticket_count":count,"prize_gbp":prize,
                         "full_cover_gross_gbp":tier_gross})
            count_sum += count; gross += tier_gross
    assert universe==8_060_598
    assert count_sum==universe
    assert gross==4_262_568
    ratio=gross/(universe*PRICE)
    assert 0.5288 < ratio < 0.5289
    return {
        "packet":"H276",
        "game":"UK National Lottery Thunderball",
        "matrix":{"main":"5/39","thunderball":"1/14"},
        "line_price_gbp":PRICE,
        "draw_universe":universe,
        "one_copy_full_cover_cost_gbp":universe*PRICE,
        "one_copy_full_cover_gross_gbp":gross,
        "fixed_return_ratio":ratio,
        "fixed_return_percent":ratio*100,
        "deficit_gbp":universe*PRICE-gross,
        "portfolio_theorem":"Every allowed line has the same average gross over the complete draw universe. Any nonnegative portfolio therefore has average gross/cost equal to this ratio, hence at least one legal draw has gross no greater than the average; because the ratio is <1, strict guaranteed profit is impossible for every nonnegative portfolio under the checked fixed paytable.",
        "tiers":rows,
    }

if __name__=='__main__':
    print(json.dumps(solve(),indent=2))
