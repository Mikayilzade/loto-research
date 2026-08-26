"""H296: current hard-capped sponsored-lottery/raffle takeover screen.

The model deliberately grants impossible-perfect ownership of every eligible
identifier and uses player-favourable prize valuations.  If even this upper
bound is below acquisition cost, the candidate is closed for strict guaranteed
profit before execution friction.
"""
from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class Candidate:
    name: str
    currency: str
    acquisition_cost: float
    favourable_liability: float
    notes: str

    @property
    def return_ratio(self) -> float:
        return self.favourable_liability / self.acquisition_cost

    @property
    def deficit(self) -> float:
        return self.acquisition_cost - self.favourable_liability


def build():
    # USA Luge: 500 tickets x US$100.  Player-favourable tractor valuation uses
    # a current dealer cash-price reference of US$25,900, above the published
    # 2025 government list-price reference for the GC1725M TLB base package.
    luge = Candidate(
        'USA Luge 2026 tractor raffle', 'USD', 500 * 100, 25_900,
        '500-ticket hard cap; favourable current dealer cash valuation.'
    )

    # ECHO: 1000 tickets x US$100; explicit US$50,000 cash alternative. If fewer
    # than 900 tickets sell, the raffle converts to a 50/50, which cannot improve
    # a perfect-buyout return above 50%.
    echo = Candidate(
        'ECHO 2026 Mercedes raffle', 'USD', 1000 * 100, 50_000,
        'Explicit $50,000 cash alternative; sub-900 fallback is 50/50.'
    )

    # Mater No.327: terms state 13,455,147 to 22,805,334 available tickets and
    # cheapest bundles at A$1/ticket.  The cost below is intentionally impossible-
    # favourable: minimum ticket count multiplied by minimum unit price, even
    # though those two extrema need not occur together.  Liabilities grant the
    # A$5,382,059 first prize + maximum A$60k book-buyer bonus + all A$145k VIP
    # prizes + an extra A$5k early-bird amount visible in the published terms.
    mater = Candidate(
        'Mater Prize Home No.327', 'AUD', 13_455_147 * 1,
        5_382_059 + 60_000 + 145_000 + 5_000,
        'Impossible-favourable min-count x min-unit-price lower bound on takeover cost.'
    )
    return [luge, echo, mater]


def main():
    rows=[]
    for c in build():
        assert c.acquisition_cost > 0
        assert c.favourable_liability >= 0
        assert c.return_ratio < 1.0
        d=asdict(c)
        d.update(return_ratio=c.return_ratio, return_percent=100*c.return_ratio, deficit=c.deficit)
        rows.append(d)
    out={'packet':'H296','state':'CLOSED / NO SUCCESS','candidates':rows,
         'all_impossible_favourable_bounds_below_break_even':all(r['return_ratio'] < 1 for r in rows)}
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
