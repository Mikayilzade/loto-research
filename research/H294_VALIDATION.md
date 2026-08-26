# H294 VALIDATION

Validated: 2026-08-26
Packet: H294 — current Australian finite-raffle takeover screen

## Independent checks
1. Every pool has an explicit finite ticket cap and positive per-ticket acquisition price.
2. Full-takeover cost is `max_tickets × ticket_price`.
3. Prize-side values deliberately overcount in the player's favour where multiple bonus/member liabilities have narrower real eligibility.
4. For every screened pool, total counted player-facing liabilities are strictly below full-takeover cost.
5. Therefore no execution assumption can rescue the complete-identifier takeover construction for the checked pool as currently priced.

## Recomputed values
- yourtown Home 559: 470,000 × A$15 = **A$7,050,000**; generous liabilities **A$3,020,000**; return **42.8368794326%**; deficit **A$4,030,000**.
- yourtown Car 1158: 130,000 × A$10 = **A$1,300,000**; generous liabilities **A$271,000**; return **20.8461538462%**; deficit **A$1,029,000**.
- RSPCA 92: 160,000 × A$10 = **A$1,600,000**; counted liabilities **A$323,000**; return **20.1875%**; deficit **A$1,277,000**.
- MS QLD Cash Grab 2: 10,000 × A$5 = **A$50,000**; liability **A$10,000**; return **20.0%**; deficit **A$40,000**.

Best checked return is yourtown Home 559 at **42.8368794326%**, still 57.1631205674 percentage points below break-even.

## Closure criterion
Since the analysis already grants complete ownership of every issued identifier, any real-world partial ownership, ticket competition, channel restriction, ineligible bonus, gold-sale friction, or prize-valuation haircut can only weaken the guaranteed floor. H294 is therefore closed for the tested full-takeover mechanism without requiring a CI search or probabilistic argument.

Validation result: **PASS — CLOSED / REJECTED BY ARITHMETIC**.
