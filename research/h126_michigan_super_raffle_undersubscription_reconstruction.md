# H126 — Michigan Super Raffle 2025 undersubscription reconstruction

Updated: 2026-08-20
Status: **STRONG HISTORICAL +EV NOMINAL OVERLAY VALIDATED / CASH-VALUE EV NEGATIVE / NO GUARANTEE**

## Goal
Test another fixed-board raffle where sales visibly undershot the ticket cap and determine whether the actual eligible denominator crossed the prize-board break-even threshold.

## Official architecture
Michigan Lottery launched the 2025 Super Raffle with:
- maximum tickets: **350,000**;
- ticket price: **$50**;
- fixed advertised prize board: 1 × $6,000,000; 2 × $1,000,000; 12 × $100,000; 3,500 × $500; 15,000 × $100;
- scheduled draw after sales close even if the game did not sell out.

Nominal board value:

`B_nominal = 6,000,000 + 2,000,000 + 1,200,000 + 1,750,000 + 1,500,000 = $12,450,000`.

Break-even denominator on undiscounted advertised prize value:

`N*_nominal = 12,450,000 / 50 = 249,000 tickets`.

Primary sources:
- Michigan Lottery launch release, 2025-06-20: https://milotteryconnect.com/2025/06/20/super-raffle-gives-michigan-lottery-players-a-chance-to-win-millions-in-prizes/
- Michigan Lottery update, 2025-11-05: https://milotteryconnect.com/2025/11/05/super-raffle-gives-michigan-lottery-players-a-chance-to-win-millions-drawing-scheduled-for-nov-19/

The Nov. 5 update said **fewer than 160,000 tickets remained**, so at least 190,001 had sold by that date. It also explicitly stated that if tickets did not sell out, sales would close before the Nov. 19 drawing.

## Final sold-pool reconstruction from the published winner support
A complete published results list contains exactly the advertised 18,515 winning raffle numbers. The largest listed winning number is **219,210**, and the winner support is densely spread from the low numbers through the 219k range with no winners above that point.

Results source used for reconstruction:
- Lottery Post full results archive for 2025-11-19: https://www.lotterypost.com/results/mi/raffle/2025/11/19

The source is secondary, so this is recorded as a reconstruction rather than a claimed official exact sales count.

If the 18,515 winners are sampled uniformly without replacement from sequential sold raffle numbers `1..N`, the maximum observed winner `M=219,210` is an extremely informative estimator of `N`.

Approximate one-sided upper bounds from `P(max <= M | N) ≈ (M/N)^m`, with `m=18,515`:
- 95% upper bound: **N ≈ 219,245**;
- 99% upper bound: **N ≈ 219,265**;
- 99.9% upper bound: **N ≈ 219,292**;
- 99.9999% upper bound: **N ≈ 219,374**.

Thus the observed result support is overwhelmingly inconsistent with a denominator anywhere near the nominal break-even `249,000`. Under the uniform-sold-pool assumption, the final pool was effectively around **219.2k tickets**.

This is not terminal proof of the exact denominator because the official draw procedure / final sales count was not recovered in crawlable primary form.

## Nominal expected-value result
At `N = 219,210`:
- nominal EV per ticket = `12,450,000 / 219,210 = $56.7949`;
- nominal gross return = **113.5897%**;
- nominal pre-tax expected ROI = **+13.5897%**.

Using the conservative 95% reconstructed denominator bound `N=219,245` still gives:
- nominal EV/ticket ≈ **$56.7858**;
- nominal pre-tax ROI ≈ **+13.5716%**.

Therefore H126 is a second major real-world confirmation, after Florida H122, that state-lottery fixed-prize raffles can enter substantial positive-EV undersubscription states.

## Cash-option correction
The advertised multi-million prizes are annuity values rather than immediate cash values. Contemporary winner reports show:
- $6m winner chose about **$4.1m lump sum**;
- $1m winner reports show about **$693,000 lump sum**.

Using those cash options for the three annuity prizes gives an approximate immediate-cash board:

`B_cash ≈ 4,100,000 + 2*693,000 + 1,200,000 + 1,750,000 + 1,500,000 = $9,936,000`.

At `N=219,210`:
- immediate-cash EV/ticket ≈ **$45.3264**;
- immediate-cash gross ≈ **90.6528%**;
- immediate-cash expected ROI ≈ **-9.3472%** before tax.

So the apparent +EV exists on **undiscounted nominal annuity value**, not on the observed lump-sum cash valuation. A economically rigorous strategy must discount the annuity cashflows and apply taxes/claim costs; on the available cash-option evidence this historical state was not a positive immediate-cash edge.

Cash-option controls:
- $6m winner report summarized at https://www.people.com/man-surprises-wife-lottery-news-she-stopped-breathing-found-out-how-much-they-won-11873590
- $1m winner report summarized at https://www.bigrapidsnews.com/news/article/michigan-super-raffle-winner-21220593.php

## Guarantee analysis
Even if nominal EV were positive, one ticket or any incomplete block can lose completely. Strict guaranteed profit would require ownership of all eligible tickets or another deterministic minimum-allocation rule.

Buying the entire reconstructed sold pool after other players already own tickets is impossible; buying all 350,000 from launch costs **$17.5m**, above both the $12.45m nominal board and the ~$9.936m cash-option board.

Therefore:
- **historical undersubscription +EV mechanism: validated on nominal advertised value**;
- **cash-value +EV: rejected on observed cash-option valuation**;
- **strict guaranteed-profit takeover: rejected**.

## Reusable monitor implication
H126 materially strengthens the H122/H123 monitor. For future fixed-board raffles, track two thresholds rather than one:
1. `N*_nominal = advertised board / ticket price`;
2. `N*_cash = economically realizable cash-equivalent board / ticket price`.

A candidate deserves serious execution work only if the live sold denominator is below the **cash-equivalent, tax/cost-adjusted threshold**, not merely the headline annuity threshold.

For a future Michigan-style Super Raffle with the same board:
- nominal break-even: **249,000 sold**;
- observed-cash-option break-even: **198,720 sold**.

The reconstructed 2025 pool (~219.2k) lies between those thresholds, explaining why the headline prize board looks +EV while lump-sum economics remain negative.
