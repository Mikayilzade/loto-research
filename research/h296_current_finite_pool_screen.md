# H296 — current hard-capped sponsored-pool takeover screen

Updated: 2026-08-26
State: **CLOSED / NO SUCCESS**

## Purpose
Continue the finite/reservable-inventory lane after H295. H225-X* is already rigorously exhausted and was not extended.

This packet tests three genuinely new current finite-pool candidates under a deliberately stronger-than-real assumption: the player gets perfect ownership of every eligible identifier and receives player-favourable prize valuation. If that impossible-perfect upper bound is still below full acquisition cost, execution details cannot rescue a strict guaranteed-profit construction.

## 1. USA Luge 2026 Tractor Raffle
Official USA Luge page states:
- US$100 per ticket;
- exactly 500 tickets available;
- Massey Ferguson GC-series tractor with loader/backhoe;
- draw in Fall 2026 or when all tickets sell.

Source: https://www.usaluge.org/usa-luge-tractor-raffle

Full takeover cost = `500 × $100 = $50,000`.

For a player-favourable prize value I used a current dealer cash-price listing of **$25,900** for the Massey Ferguson MF1GC.25B loader/backhoe package, which is above the 2025 public government list-price reference for the GC1725M TLB base package ($23,198 before tire option).

Dealer source: https://patriottractor.com/collections/massey-ferguson-sub-compact-tractors
Government pricing reference: Tennessee state AGCO/Massey pricing PDF, revision MF25-08 (Aug 1 2025).

Impossible-perfect return: **$25,900 / $50,000 = 51.8%**. Deficit: **$24,100**.

Closed arithmetically.

## 2. ECHO 2026 Mercedes-Benz Raffle
Current ECHO page states:
- $100 per ticket;
- hard cap 1,000 tickets;
- winner chooses Mercedes-Benz CLA 250 4Matic Coupe or **$50,000 cash**;
- if fewer than 900 tickets sell, the raffle converts to a 50/50.

Source: https://echoorganization.org/product/mercedes-benz-raffle-2026/

At full issuance, acquisition cost is **$100,000** and the explicit cash alternative is **$50,000**, exactly **50%**. The sub-900 fallback cannot improve a perfect-buyout guarantee above 50%, because it is itself a 50/50.

Closed arithmetically.

## 3. Mater Prize Home Lottery No. 327
Current official Mater terms state:
- sales 13 Jul–20 Oct 2026; draw 23 Oct 2026;
- single ticket $2 with bundles down to **$1 per ticket**;
- ticket availability ranges from **13,455,147** (single purchases) to **22,805,334** (if bundle purchases occur);
- first prize total RRP **A$5,382,059**;
- maximum book-buyer bonus **A$60,000**;
- VIP prize draws total **A$145,000**;
- terms also list an A$5,000 early-bird amount.

Official source: https://www.materlotteries.com.au/mater-prize-home/terms-and-conditions/327

To make the takeover artificially easier, combine two favourable extrema that need not coexist: the **minimum** published ticket count with the **minimum** published unit price. This gives only **A$13,455,147** as an impossible-favourable lower bound on takeover cost.

Then grant the player all counted liabilities:
`5,382,059 + 60,000 + 145,000 + 5,000 = A$5,592,059`.

Impossible-favourable return = **41.5607425%**; deficit = **A$7,863,088**.

Because the proof already mixes incompatible extrema in the player's favour, the real acquisition economics can only be worse for this strict-guarantee purpose.

## Conclusion
All three current candidates fail before execution friction:
- USA Luge: **51.8%**;
- ECHO Mercedes: **50.0%**;
- Mater No.327: **41.5607%** under an impossible-favourable cost bound.

No SUCCESS. Do not revisit these exact 2026 pools unless prize economics, ticket caps, or a deterministic external subsidy materially changes.

## Reproducibility
- `src/loto_research/h296_current_finite_pool_screen.py`
- `data/derived/h296_current_finite_pool_screen.json`
