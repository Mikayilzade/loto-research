"""H292: exact full-buyout screen for selected live 2026 finite RaffleTix raffles.

Inputs are copied from public raffle terms/pages checked 2026-08-26.  The test is
player-favourable: assume one eligible player can buy every issued identifier at
the cheapest published bundle rate and thereby collect the entire advertised
prize pool.  If even that impossible-perfect takeover is below cost, the raffle
cannot furnish a strict guaranteed-profit full-buyout construction.
"""
from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class Raffle:
    name: str
    tickets: int
    bundle_tickets: int
    bundle_cost: float
    prize_pool: float
    source: str

RAFFLES = [
    Raffle('Waves & Wheels',125000,100,500.0,481993.59,'https://www.raffletix.com.au/waves-and-wheels'),
    Raffle('The 6e Gold Rush',65000,100,500.0,111682.00,'https://www.raffletix.com.au/the-6e-gold-rush'),
    Raffle('Bruthen FNC Toyota Corolla Cross',5000,1,25.0,50300.00,'https://www.raffletix.com.au/bruthenfnc2026'),
    Raffle('Norwood FC 2026 Major Lottery',30000,1,5.0,58382.00,'https://www.raffletix.com.au/norwoodfcmajorlottery2026'),
    Raffle('TRG 2026 Major Raffle',2500,1,10.0,6018.00,'https://www.raffletix.com.au/trgmajorraffle2026'),
]

def evaluate(r: Raffle):
    assert r.tickets % r.bundle_tickets == 0
    cost = (r.tickets // r.bundle_tickets) * r.bundle_cost
    ret = r.prize_pool / cost
    return {
        **asdict(r),
        'perfect_full_buyout_cost': round(cost,2),
        'perfect_full_buyout_gross': round(r.prize_pool,2),
        'return_ratio': ret,
        'return_percent': 100*ret,
        'deficit': round(cost-r.prize_pool,2),
        'strict_profit_even_under_perfect_takeover': r.prize_pool > cost,
    }

def main():
    rows=[evaluate(r) for r in RAFFLES]
    assert all(not x['strict_profit_even_under_perfect_takeover'] for x in rows)
    best=max(rows,key=lambda x:x['return_ratio'])
    assert best['name']=='Waves & Wheels'
    assert abs(best['perfect_full_buyout_cost']-625000.0)<1e-9
    assert abs(best['perfect_full_buyout_gross']-481993.59)<1e-9
    assert abs(best['return_percent']-77.1189744)<1e-9
    out={'packet':'H292','checked_on':'2026-08-26','model':'impossible-perfect full identifier takeover at cheapest published bundle rate','raffles':rows,'best_return_name':best['name'],'best_return_percent':best['return_percent'],'all_below_break_even':True}
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
