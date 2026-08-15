# H012a / H004 — linear-portfolio impossibility theorem

Updated: 2026-08-15
Status: **standalone guaranteed-profit covering/wheel path rejected for additive fixed-payout negative-EV games**

## Goal
Determine whether a clever multi-ticket covering design, wheel, portfolio, or partial-space construction can create a **guaranteed positive net profit** in an otherwise ordinary fixed-payout lottery.

## The theorem
Consider a finite lottery outcome space Ω with strictly positive outcome probabilities. Let ticket type `i` cost `c_i > 0` and pay `r_i(ω)` in outcome `ω`.

Assume:
1. ticket payouts add linearly across our portfolio;
2. ticket acquisition costs add linearly;
3. buying our portfolio does not change the payout rule, prize pool, promotion, or other players' payouts;
4. for every available ticket type, expected profit is non-positive:
   `E[r_i] - c_i <= 0`.

For any portfolio with non-negative integer multiplicities `x_i`:

`Profit(ω) = Σ_i x_i r_i(ω) - Σ_i x_i c_i`.

Taking expectations:

`E[Profit] = Σ_i x_i (E[r_i] - c_i) <= 0`.

If the same portfolio guaranteed **strictly positive** profit for every possible outcome,

`Profit(ω) > 0 for all ω`,

then because every outcome has positive probability we would necessarily have:

`E[Profit] > 0`,

contradicting the previous inequality.

Therefore:

> **No wheel, covering design, partial-space portfolio, duplicate pattern, or staking allocation composed only of non-positive-EV additive fixed-payout tickets can guarantee positive profit.**

This proof is independent of the size of the combinatorial space and eliminates the need to brute-force millions or trillions of wheels when the assumptions hold.

## What this closes
### Azerbaijan Beşdə 5
Current official rules give 1-AZN variants with fixed payouts by match count. Existing exact favorable gross EV is about 0.53556 AZN per 1-AZN variant before tax/sharing deterioration.

Consequences:
- arbitrary collections of ordinary variants cannot have guaranteed positive profit;
- wheels / partial coverings cannot create positive EV;
- a combination ticket that is merely the sum of generated variants cannot change this conclusion unless the operator provides a genuine nonlinear discount/subsidy.

Full-space coverage was already separately rejected at ~53.56% deterministic return.

### Azerbaijan Super Keno
Base and 1x/2x/5x/10x mechanics have already been shown to scale stake and displayed prizes proportionally, with gross payout ratio about 59.8556% and worse favorable after-tax ratios at larger multipliers.

Under additive purchase/payout rules, no wheel or mixture of those negative-EV variants can produce a strict all-outcomes profit guarantee.

### Azerbaijan ONLOTO
All ten base bet types have exact deterministic full-space returns below 78%. For any subset/portfolio built from the same additive fixed multiplier tickets, negative individual EV implies the same impossibility result for guaranteed positive profit.

System play remains economically equivalent to a bundle of generated variants unless a nonlinear discount or promotion exists. The current public rules describe system play as generation of multiple variants; no evidence of a subsidy has been found.

## What this does NOT close
The theorem intentionally does not cover games/states where portfolio economics are nonlinear or externally subsidized, including:
- pari-mutuel/shared pools where our own volume changes sharing;
- progressive or roll-down jackpots with accumulated external money;
- promotions, cashback, free-ticket subsidies, coupons or loyalty conversion;
- system-ticket pricing below the cost of constituent base variants;
- finite scratch inventories with observable remaining-state information;
- operator errors / lawful pricing inconsistencies;
- cross-market arbitrage;
- a physical/RNG predictability edge that changes outcome probabilities.

Those are precisely the branches that remain relevant after this theorem.

## Strategic consequence
H004 wheels and H012a partial-covering designs may still be useful for **variance / hit-probability / bankroll-shape optimization**, but in an ordinary additive negative-EV game they are no longer a terminal guaranteed-profit candidate.

Future combinatorial work should therefore focus only on cases where at least one assumption above is broken by a genuine structural overlay or nonlinear pricing rule.

## Primary current-rule anchors
- Beşdə 5: https://www.azerlotereya.com/lotereya/besde5
- Super Keno: https://www.azerlotereya.com/lotereya/superkeno
- ONLOTO: https://www.azerlotereya.com/lotereya/onloto
- 4+4 (nonlinear/shared-state exception remains open): https://www.azerlotereya.com/lotereya/4-4
