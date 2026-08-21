# H156 — universal Keno doubler vs paid-add-on screen

Updated: 2026-08-21
Status: **NO SUCCESS / IMPORTANT CLASS FILTER VALIDATED**

## Question
H155 proved that a true no-cost universal 2x applied to every ticket in a compact Keno full-cover can invert a >50% base cover into a deterministic positive overlay. This packet asks whether current or recent official Keno promotions actually provide that architecture.

## Current BCLC Keno Doubler (July 27–September 7, 2026)
Official retailer rules state that Keno tickets are **randomly** selected to print a `KENO DOUBLER` message. A winning ticket carrying that message pays double, but replaying such a ticket does **not** guarantee another Doubler. Validly issued Keno tickets generally cannot be cancelled during the promotion.

Source: https://www.bclcretailerhub.com/content/dam/retailerhub/promotions/2026/Keno_Doubler_Jul_2026_RIS.pdf

Result: this is a free 2x enhancement but **not universal / not pre-owned**. An undoubled branch remains for every required full-cover ticket. Therefore it cannot establish a strict all-outcome payout floor.

## Michigan Doubler Days control
Michigan's official historical Club Keno Doubler Days likewise says players have a **chance** to receive a Doubler message; only tickets receiving the message double eligible prizes without extra cost.

Source: https://milotteryconnect.com/2019/12/30/doubler-days-returns-to-club-keno-in-january/

Result: same ownership failure as BCLC and current Pennsylvania H155.

## Ohio Double BOOSTER — the important structural control
Ohio's official September 2025 rules are materially different: **all BOOSTERS are doubled** on eligible KENO tickets during fixed promotional windows. The rules explicitly map:

`1X→2X, 2X→4X, 3X→6X, 4X→8X, 5X→10X, 10X→20X`.

Source: https://www.ohiolottery.com/getattachment/be2303f8-361b-4beb-aca7-2b9790a8e8fb/Ohio-Lottery-KENO-Double-Booster_SepPromo_20250819.pdf

This solves the random-ticket ownership problem, but only for players who **buy the BOOSTER add-on**. Current Ohio KENO rules price BOOSTER at another $1 for every $1 wagered.

Current base paytable source: https://www.ohiolottery.com/games/keno

### Paid-add-on cancellation theorem
Let:
- `S` = base full-cover cost,
- `rS` = deterministic gross return of the base full-cover,
- `aS` = mandatory add-on cost,
- `m_min` = minimum guaranteed multiplier under the promotion.

The promoted strict cover ratio is:

`R = m_min * r / (1 + a)`.

For Ohio Double BOOSTER:
- `a = 1` because BOOSTER doubles ticket cost;
- minimum normal BOOSTER is `1X`, doubled by promo to `m_min = 2`.

Therefore:

`R = 2r / 2 = r`.

So the promotion's guaranteed minimum multiplier **exactly cancels the mandatory add-on cost**. It does not improve the deterministic cover ratio at all. Higher realized BOOSTER states improve EV/outcomes, but are not guaranteed before purchase.

### Exact Ohio full-cover checks
Using the current official fixed paytable and the standard 80-number / 20-draw Keno combinatorics, deterministic base full-cover ratios are:

| Spot | Base full-cover ratio | Double-BOOSTER strict floor |
|---:|---:|---:|
| 1 | 50.0000% | 50.0000% |
| 2 | 66.1392% | 66.1392% |
| 3 | 65.2142% | 65.2142% |
| 4 | 64.9439% | 64.9439% |
| 5 | 64.9951% | 64.9951% |
| 6 | 64.7920% | 64.7920% |
| 7 | 65.2984% | 65.2984% |
| 8 | 64.7475% | 64.7475% |
| 9 | 64.8069% | 64.8069% |
| 10 | 63.6694% | 63.6694% |

Best checked Ohio base/full-cover ratio is 2-Spot at about **66.1392%**, still far below 100%.

## Implication for H155 trigger
The high-value trigger must be refined:

A promotion is useful for strict full-cover only if the **guaranteed multiplier net of its mandatory surcharge** satisfies

`m_min/(1+a) > 1/r`.

For a no-cost universal 2x (`a=0`), any base cover `r>50%` crosses 100%.

For a full-price add-on (`a=1`) whose promoted minimum is only 2x, there is **zero deterministic improvement**.

For Pennsylvania 4-Spot (`r≈64.8718%`), a paid add-on would need guaranteed multiplier strictly above `2/r ≈ 3.083x`; a 4x guaranteed multiplier would work, while 2x or 3x would not.

For Virginia 1-Spot (`r=75%`), a paid equal-cost add-on needs `m_min > 2.6667x`; guaranteed 3x would be enough.

For La Vista benchmark (`r≈81.0636%`), paid equal-cost add-on needs `m_min > 2.4672x`; guaranteed 3x would also work.

## Result
- Current BCLC free Doubler: **REJECTED strict guarantee — random ticket assignment**.
- Michigan Doubler Days control: **REJECTED strict guarantee — random ticket assignment**.
- Ohio universal Double BOOSTER architecture: **ownership solved, economics rejected** because the mandatory BOOSTER surcharge cancels the minimum 2x gain.
- General paid-add-on threshold theorem: **VALIDATED** and should be applied before future promo deep-dives.

## Next research
1. Search current/future official Keno promotions with **universal no-cost 2x+** for all wagers in a known time window.
2. Also search universal **paid** multiplier specials, but require `m_min/(1+a) > 1/r`; prioritize guaranteed 3x on base covers ≥75%, or guaranteed 4x on ~65% covers.
3. Search community/Nebraska specials where the enhanced paytable itself is fixed before purchase, avoiding multiplier-assignment risk entirely.
4. For any qualifying candidate, immediately test transaction/basket limits, payout caps, cancellation, tax and physical-jurisdiction execution.