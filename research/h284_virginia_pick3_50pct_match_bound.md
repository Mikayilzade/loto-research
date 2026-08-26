# H284 — Virginia Pick 3 + 50% welcome-match bound

Checked: 2026-08-26
Status: **CLOSED for the tested additive Pick 3 subsidy class; NO GLOBAL SUCCESS**

## Why this packet

After H283 closed the Pennsylvania referral-cover idea on operator stop-play authority, the next useful filter is a deterministic playable-balance subsidy combined with a symmetric fixed-pay draw game. Current August 2026 Virginia Lottery welcome-offer listings consistently advertise a **50% first-deposit match up to roughly $100** plus free games. This packet deliberately grants the 50% match in full; therefore any uncertainty in offer eligibility only makes the real position weaker.

Official Virginia Lottery sources checked:
- live online Pick 3 page and current prize table: https://www.valottery.com/data/draw-games/pick3
- online Pick games availability: https://www.valottery.com/lotteryonline/pickgamesonline
- generic official Online Gaming Promotion Rules: https://www.valottery.com/-/media/images/game-rules/2022/online-gaming-promotion-rules-78-2022-11-28-22.ashx?la=en

Current offer evidence checked:
- PlayVirginia August 2026 welcome-offer listing: 50% match up to $100 plus 20 free games.
- FootballWhispers July/August 2026 listing: same 50% match structure.
- LegalSportsReport August 2026 listing: same 50% structure (reported cap varies across listings).

The cap discrepancy is irrelevant to the theorem below because only the **match rate** matters.

## Exact base-game arithmetic

Virginia's current Pick 3 table is fixed-pay. For $1 base plays:

| primitive | exact average gross / cost |
|---|---:|
| Exact | 500 / 1000 = **50%** |
| Pair | 50 / 100 = **50%** |
| 3-way Any Order | 3×160 / 1000 = **48%** |
| 6-way Any Order | 6×80 / 1000 = **48%** |
| 3-way 50/50 | (330 + 2×80) / 1000 = **49%** |
| 6-way 50/50 | (290 + 5×40) / 1000 = **49%** |
| 3-way Combo | 3×500 / (1000×3) = **50%** |
| 6-way Combo | 6×500 / (1000×6) = **50%** |

Thus every nonnegative mixture of these additive base plays has average gross no greater than **50% of stake**.

For any finite portfolio over a finite outcome space,

`minimum legal-outcome gross <= average legal-outcome gross`.

Therefore no such portfolio can have a worst-case gross above 50% of its playable stake.

## Apply the 50% deposit subsidy

Let cash deposit be `D`. A 50% match creates at most `1.5D` playable balance.

Even if every dollar of both deposit and bonus can be routed into the best Pick 3 primitive class:

- playable stake: `1.5D`;
- average gross ceiling: `0.50 × 1.5D = 0.75D`;
- hence worst-case gross `<= 0.75D`.

So **at least one legal draw state loses at least 25% of the original cash deposit**. Strict guaranteed cash profit is impossible for the tested base-play additive class.

## FIREBALL stress

The live table also publishes FIREBALL payouts. Rather than rely on rounded displayed odds for a delicate exact theorem, H284 grants the add-on an intentionally favorable standalone gross ceiling of **57%**, above the simple displayed Pair (`20/36 ≈55.56%`) and Exact (`200/357 ≈56.02%`) ratios.

Since FIREBALL is an additional wager at the base wager amount, an equal-stake base+FIREBALL blend is then bounded by

`(0.50 + 0.57)/2 = 0.535` average gross per total dollar staked.

After a 50% deposit match:

`1.5 × 0.535 = 0.8025`.

Even this deliberately player-favorable stress leaves worst-case cash recovery below **80.25% of deposit**, far below strict profit.

## Result

**H284 is CLOSED** for the current 50%-match + Virginia Pick 3 symmetric additive-cover mechanism.

This is stronger than rejecting one particular 100-line Pair cover: the base-game argument applies to every nonnegative mixture of the listed fixed-pay primitive wagers. FIREBALL also fails under a deliberately favorable ceiling.

Do not reopen this packet unless either:
1. the deterministic subsidy exceeds the relevant hurdle materially (base-only requires >100% match because 50% game return needs >2× playable balance), or
2. the Pick 3 payout table materially improves, or
3. a separate deterministic cash-equivalent reward adds value outside the wager-return symmetry.

Reproducibility:
- `src/loto_research/h284_virginia_pick3_50pct_match_bound.py`
- `data/derived/h284_virginia_pick3_50pct_match_bound.json`
