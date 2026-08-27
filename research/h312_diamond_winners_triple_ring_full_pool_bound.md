# H312 — Diamond Winners Triple Ring finite-pool takeover bound

Date checked: 2026-08-27
State: **CLOSED / ARITHMETICALLY BELOW BREAK-EVEN**

## Why this candidate was opened

The current Diamond Winners `The Triple Ring Winner – 3 x £2,150 Rings!` draw has an unusually favourable execution shape for the finite-pool lane:

- 9,999 total tickets;
- published maximum per person is also 9,999, so the nominal user cap does not itself forbid full-pool ownership;
- the operator publishes the instant-win identifiers and their current available/won state;
- ticket price is £1.99;
- draw closes 30 August 2026.

On the 2026-08-27 snapshot the page showed 254/9,999 sold. This already creates execution friction, but H312 intentionally ignores it and gives the player the strictly stronger impossible condition of owning the entire pool from inception. If that ideal takeover is still below break-even, no weaker real acquisition can rescue this draw.

## Published liability schedule

Operator-listed prizes:

- 3 diamond rings stated as insured for £2,150 each;
- 2 × £500 cash;
- 4 × £250 cash;
- 10 × £100 cash;
- 20 × £50 cash;
- 100 × £10 cash;
- 1,000 × £1 cash;
- 1,000 × £0.50 site credit;
- 5,000 × £0.10 site credit.

For an intentionally player-favourable upper bound, rings are valued at the full stated £2,150 each and all site credit at 100% cash-equivalent face value. No resale discount, tax, withdrawal friction, already-won prize loss, or execution cost is applied.

## Exact full-pool arithmetic

Full acquisition cost:

`9,999 × £1.99 = £19,898.01`

Maximum favourable published liability:

`3×2150 + 2×500 + 4×250 + 10×100 + 20×50 + 100×10 + 1000×1 + 1000×0.50 + 5000×0.10 = £13,450.00`

Therefore:

- gross ratio = `£13,450 / £19,898.01 = 0.6759469916840931`;
- gross = **67.5946992%**;
- deficit = **£6,448.01**.

## Conclusion

H312 is closed by arithmetic before execution mechanics matter. Even impossible-perfect ownership of all 9,999 identifiers plus full face valuation of every published prize remains only 67.59% of acquisition cost. The fact that the real snapshot already had sold tickets only makes the achievable position weaker.

This candidate is useful because it verifies that `max_per_user = N` alone is not enough; the deterministic player-facing liabilities must also exceed exact acquisition cost.

## Source

- Diamond Winners current operator page: https://diamondwinners.co.uk/product/the-triple-ring-winner-3-x-2150-rings/

## Reproducible artifacts

- `src/loto_research/h312_diamond_winners_triple_ring_full_pool_bound.py`
- `data/derived/h312_diamond_winners_triple_ring_full_pool_bound.json`
