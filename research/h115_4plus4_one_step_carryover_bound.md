# H115 — Azerbaijan 4+4 one-step zero-category carryover bound

Updated: 2026-08-20
Status: **RECURRING CATEGORY-II CARRYOVER EDGE MATERIALLY WEAKENED / EXCEPTIONAL MULTI-ZERO STATE STILL OPEN / NO SUCCESS**

## Question
H014 previously treated repeated zero-winner category-II draws as a possible multi-draw accumulation source. This packet tests the stronger rule interpretation recovered from a current indexed copy of the 4+4 rules and asks whether the ordinary recurring zero-II state can by itself create positive EV for a selective portfolio.

## Recovered rule text — important correction
A current indexed rule mirror states:

- category II winners receive the part of the current prize fund allocated to category II;
- if there are no winners in categories II–XI, the amount allocated to the zero-winner category is **added to the next draw's prize fund**;
- that carried amount is then distributed **proportionally among winners in the next draw**.

Source recovered in this packet:
- https://idman-az.com/az-lotereya/4-4-lotereya

This is not yet a primary Azərlotereya-hosted registration document, so it is treated as **medium-confidence rule recovery**, not terminal legal proof. The wording is nevertheless specific enough to change the working H014 model.

### Consequence
The ordinary zero-II amount does **not** appear to remain in category II and compound across many consecutive zero-II draws. It is a **one-step overlay** into the next draw's general prize fund.

Therefore the old mental model

`zero II -> same II balance grows -> zero II -> grows again -> ...`

is materially weakened. The recovered model is instead

`zero II at t -> II allocation enters total prize fund at t+1 -> paid proportionally to t+1 winners`.

Because categories X/XI have thousands of winners in every preserved 2026 sample, the carried amount is not expected to survive beyond the immediately following draw in the normal state.

## Empirical recurring state
All preserved detailed 2026 payout samples currently available in the repository show:

- category II: zero winners;
- categories III–XI: at least one winner.

Thus the normal observed carryover packet is **II only**, not a large stack of several zero categories.

The exact category-II allocation percentage is still not recovered from the primary registered conditions. A current indexed rule mirror gives an allowed category-II range of **1–10% of the draw prize fund**.

Separately, the Azerbaijan Lottery Law bound already used in H113 caps a sales-linked prize-fund parameter at 80% of relevant sales. For a 2-AZN variant, a deliberately player-favorable upper bound for the current category-II allocation is therefore:

`II_pool <= 2 * N * 0.80 * 0.10 = 0.16 N AZN`,

where `N` is sold variants in that draw.

## Current-draw category-II EV upper bound
Let category-II match probability per base variant be

`pII = 0.000005452835634281`.

With `N` sold variants, the probability that the draw has at least one category-II winner is

`1 - (1-pII)^N`.

For a fixed pari-mutuel pool, exchangeability gives the aggregate per-ticket expected payout identity

`EV_II = pool/N * P(at least one II winner)`.

Using the deliberately maximal pool `0.16N`, the category-II EV upper bound is

`EV_II <= 0.16 * [1-(1-pII)^N]`.

At representative reconstructed sales volumes:

| N | P(no II winner) | maximum current-II EV / ticket |
|---:|---:|---:|
| 38,000 | 81.2850% | 0.02994 AZN |
| 40,000 | 80.4034% | 0.03135 AZN |
| 42,000 | 79.5313% | 0.03275 AZN |
| 45,000 | 78.2409% | 0.03481 AZN |
| 50,000 | 76.1365% | 0.03818 AZN |

The reason this is much smaller than the nominal pool-per-ticket bound is simple: in roughly 76–81% of these draws nobody hits category II, so the category-II allocation is not paid in that same draw.

## One-step carryover upper bound
Suppose draw `t` has zero category-II winners. Under the recovered rule, at most `0.16 N_t` of category-II money can enter draw `t+1` as external carryover under the maximally favorable 80% prize-fund / 10% category-II assumptions.

If the next draw sells `N_{t+1}` variants and the full carryover is eventually paid to its winners, the **average** extra value available per next-draw ticket is at most

`EV_carry <= 0.16 * N_t / N_{t+1}`.

This is the key state variable: the overlay becomes large only if sales collapse sharply from the zero-II draw to the following draw.

## Break-even contraction hurdle
The current reconstructed lower-tier subtotal excluding category II is

`1.1621497378485368 AZN / 2-AZN variant`.

At a 1.9m-AZN jackpot, jackpot-only EV is

`1,900,000 / 23,474,025 = 0.080940529 AZN`.

So before category II / prior carryover, the remaining gap to 2 AZN is approximately

`0.75691 AZN per ticket`.

Even giving the current draw the **maximum legally favorable** category-II EV above, the prior zero-II carryover must still cover roughly 0.719–0.727 AZN per ticket.

That requires the previous-to-current sales ratio to satisfy approximately:

`N_t / N_{t+1} > 4.49–4.54`.

Representative thresholds:

| Current N | required prior/current sales ratio |
|---:|---:|
| 38,000 | >4.544x |
| 40,000 | >4.535x |
| 42,000 | >4.526x |
| 45,000 | >4.513x |
| 50,000 | >4.492x |

This is an intentionally optimistic hurdle because it assumes simultaneously:

1. the prize-fund fraction is at its statutory maximum 80%;
2. category II receives the maximum 10% of that fund;
3. the previous draw has zero category-II winners;
4. every manat of that allocation is carried into the next draw;
5. the player captures average carryover value without adverse crowd effects;
6. the jackpot is already 1.9m AZN;
7. no tax, transaction cost, purchase limit or execution loss;
8. no reduction of other current category allocations when carryover is redistributed.

## Interpretation
For the **normal recurring state observed in the preserved 2026 tables** — zero II, winners in III–XI — a selective H014 strategy cannot plausibly become positive merely because the prior draw had no category-II winner unless the next draw's sales fall by roughly **4.5x or more** relative to the previous draw under maximally favorable allocation assumptions.

No such contraction is currently evidenced in the reconstructed 2026 sales proxies. Ordinary draw-to-draw variation is far smaller.

This materially weakens the recurring category-II carryover branch.

## What remains open
H014 is not fully closed because several exceptional states can still create more external value:

1. **multiple zero categories in the same prior draw** — especially III–VI — could create a larger one-step overlay;
2. an operator-funded jackpot/promo addition can create external value independent of current sales;
3. a documented special redistribution rule may target a favorable category rather than the general proportional fund;
4. a very large observable sales contraction after a zero-category draw could theoretically satisfy the ratio hurdle;
5. the primary registered 4+4 conditions may differ from the current indexed mirror and must override this note if recovered.

The correct scanner is therefore no longer "count consecutive zero-II draws". It is:

`observe prior draw zero categories + estimate their bounded allocated pools + observe current sales/fund + calculate one-step external overlay per current variant`.

## New research priority
1. Recover the primary registered conditions for registration no. 336 and verify the exact zero-category carryover wording and percentages.
2. Build a consecutive-draw table with winner counts for categories II–VI and sales proxies.
3. Flag only **exceptional multi-zero** prior draws or >4.5x sales-contraction states.
4. Treat ordinary repeated zero-II streaks as non-compounding unless primary rules prove otherwise.

## Result
**NO SUCCESS.** The ordinary recurring zero-category-II mechanism is materially weakened from a potential multi-draw accumulator to a one-step overlay whose maximally favorable economics require an extreme ~4.5x previous/current sales ratio to reach break-even at a 1.9m jackpot.
