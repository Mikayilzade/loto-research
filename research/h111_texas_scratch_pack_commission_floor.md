# H111 — Texas scratch fixed-pack guarantee + retailer-commission overlay

Updated: 2026-08-19
Status: **FIXED-PACK GUARANTEE CLASS TESTED WITH GENEROUS RETAILER SUBSIDY / NEGATIVE / NO SUCCESS**

## Goal
Test a stronger scratch-ticket variant than H110: instead of estimating the remaining unsold game population, use Texas scratch games where the operator publishes a **guaranteed total prize amount per sealed pack**. Then ask whether a deterministic retailer sales commission or similar fixed subsidy can lift the pack's worst-case cash return above acquisition cost.

This avoids the main H110 denominator problem because the guaranteed pack payout is already attached to a bounded pack.

## Primary sources
Texas official scratch game pages publish ticket price, pack size and guaranteed total prize amount per pack. Sampled controls include:
- X #2590: https://www.texaslottery.com/export/sites/lottery/Games/Scratch_Offs/details.html_252700419.html
- Extreme Multiplier #2655: https://www.texaslottery.com/export/sites/lottery/Games/Scratch_Offs/details.html_252699577.html
- Diamond 7s #2685: https://www.texaslottery.com/export/sites/lottery/Games/Scratch_Offs/details.html_252699484.html
- Loteria Azul #2765: https://www.texaslottery.com/export/sites/lottery/Games/Scratch_Offs/details.html
- 500X Loteria Spectacular #2659: https://www.texaslottery.com/export/sites/lottery/Games/Scratch_Offs/details.html_252699573.html
- 500X #2349: https://www.texaslottery.com/export/sites/lottery/Games/Scratch_Offs/details.html_252702487.html
- 20Xtra #2355: https://www.texaslottery.com/export/sites/lottery/Games/Scratch_Offs/details.html_252702460.html

Texas retailer compensation is at least 5% of retail ticket sales under Government Code §466.358 / current state accounting guidance; current retailer rules also state 5.0% compensation on lottery-game sales. Sources:
- https://fmcpa.cpa.state.tx.us/fiscalmoa/exp.jsp?num=7260
- https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-401-353

## Strict theorem
Let:
- `F` = sealed pack face cost = ticket price × pack size;
- `G` = operator-published guaranteed total prize amount for the pack;
- `c` = deterministic sales commission/subsidy fraction on pack face value;
- `B` = any additional deterministic fixed cash bonus that survives every outcome;
- `C` = all other costs/tax/fees.

Worst-case net:

`W = G + cF + B - F - C`.

For guaranteed positive profit:

`G/F + c + B/F > 1 + C/F`.

A conditional retailer bonus for selling a high-tier winner cannot enter `B` because there are sealed packs with no qualifying high-tier prize. Likewise discretionary incentive programs cannot support a strict floor.

## Deliberately favorable assumption
Whether a retailer can lawfully/economically capture its own sales commission on self-purchased scratch packs is not needed to reject the sampled class. H111 grants the buyer the **entire 5% retailer commission as if it were a deterministic rebate**, which is strictly more favorable than an ordinary player purchase. If the floor remains far below 100% under this subsidy, the pack cannot be a guaranteed-profit route through ordinary purchase or the 5% commission alone.

## Sampled pack floors
| Game | Ticket | Pack | Face `F` | Guaranteed `G` | Pack floor | Floor + full 5% commission |
|---|---:|---:|---:|---:|---:|---:|
| X #2590 | $50 | 20 | $1,000 | $625 | 62.50% | **67.50%** |
| Extreme Multiplier #2655 | $20 | 25 | $500 | $280 | 56.00% | **61.00%** |
| Diamond 7s #2685 | $20 | 25 | $500 | $270 | 54.00% | **59.00%** |
| 500X #2349 | $20 | 25 | $500 | $270 | 54.00% | **59.00%** |
| Loteria Azul #2765 | $5 | 75 | $375 | $200 | 53.33% | **58.33%** |
| 20Xtra #2355 | $2 | 125 | $250 | $145 | 58.00% | **63.00%** |
| 500X Loteria Spectacular #2659 | $50 | 20 | $1,000 | $400 | 40.00% | **45.00%** |

Best sampled buyer-favorable floor is X #2590 at **67.5%** after granting the full 5% commission. It still guarantees a **32.5% loss before any other costs**.

## Required subsidy hurdle
For each pack, the deterministic subsidy needed merely to reach break-even is:

`required_subsidy = 1 - G/F`.

The sampled hurdle ranges from **37.5% to 60% of pack face value**. The ordinary 5% retailer commission is an order of magnitude too small.

Even for the strongest sampled X pack:
- face cost = $1,000;
- guaranteed prizes = $625;
- full 5% commission = $50;
- guaranteed recovered value = $675;
- remaining guaranteed deficit = **$325**.

No ordinary retailer winning-ticket bonus fixes this because it is contingent on a qualifying winner and therefore has a zero worst-case contribution.

## Strategic consequence
H111 materially closes the most promising fixed-pack deterministic scratch route in Texas:
- exact bounded pack exists;
- guaranteed pack payout is public;
- fixed retailer commission is public;
- even granting that commission fully to the buyer leaves a large guaranteed loss.

A future pack-level scratch SUCCESS now requires a genuinely exceptional **deterministic discount/rebate/subsidy of roughly 35%+** on a high-floor pack, or another jurisdiction whose guaranteed sealed-pack payout is already near face value. Ordinary 5–10% retailer commissions/loyalty discounts are insufficient unless the pack floor itself is above roughly 90–95%.

## Terminal result
**NO SUCCESS.** Fixed sealed-pack composition solves the denominator problem, but sampled Texas guaranteed pack payouts are only 40%–62.5% of face value. Even after granting a full 5% retailer commission as a deterministic rebate, the strongest sampled floor is only 67.5%.