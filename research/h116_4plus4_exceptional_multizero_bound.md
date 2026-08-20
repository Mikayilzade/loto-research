# H116 — Azerbaijan 4+4 exceptional multi-zero carryover bound

Updated: 2026-08-20
Status: **EXCEPTIONAL MULTI-ZERO ROUTE MATERIALLY NARROWED / ONLY VERY RARE HIGH-ORDER STATES REMAIN / NO SUCCESS**

## Goal
H115 left one high-value residual branch: a prior 4+4 draw with several zero-winner categories II–VI could create a larger one-step external overlay than the ordinary II-only state. This packet derives exact match probabilities, exact iid zero-category probabilities, and the sales-contraction hurdle for 1–5 simultaneous zero categories.

## Current rule/control evidence
The current official Azərlotereya game page confirms the 2 AZN ticket price and registration no. 336 dated 17.01.2021. A current indexed rule mirror states that when categories II–XI have no winners, the amount assigned to the empty category is added to the next draw's prize fund and distributed proportionally among next-draw winners.

Sources:
- https://www.azerlotereya.com/game/fourplus
- https://idman-az.com/az-lotereya/4-4-lotereya

The primary detailed registration document itself was not recovered in this packet, so the zero-category transfer wording remains medium-confidence pending a primary copy.

## Exact category probabilities
Each board is a 4-of-20 hypergeometric match. For one ticket:

- `pII = P(4+3 or 3+4) = 0.000005452835634281` = about 1 in 183,391;
- `pIII = P(4+2 or 2+4) = 0.000061344400885660` = about 1 in 16,301;
- `pIV = P(4+1 or 1+4) = 0.000190849247199830` = about 1 in 5,240;
- `pV = P(4+0 or 0+4) = 0.000155065013349862` = about 1 in 6,449;
- `pVI = P(3+3) = 0.000174490740296988` = about 1 in 5,731.

Under iid ticket selections, the probability that every category in a set `S` has zero winners among `N` sold variants is exact:

`P(zero in every category S) = (1 - sum_{c in S} p_c)^N`,

because a ticket belongs to at most one prize category.

## Rare-state frequency
At reconstructed sales scale `N≈38k–50k`:

- II-only zero is ordinary: ~76.1%–81.3%;
- II+III both zero is uncommon but realistic: ~3.54%–7.90%;
- II+III+V all zero: ~0.00152%–0.0218%;
- II+III+VI all zero: ~0.000575%–0.0104%;
- II+III+IV all zero is similarly rarer;
- all II–VI zero is effectively negligible under iid selection (about `2.0e-10` at N=38k, lower at larger N).

Thus the only exceptional state likely to occur with meaningful frequency is **II+III zero**. Three-or-more zero categories are already extreme tail events at current volume.

## Economic hurdle
H115 reconstructed the pre-carryover break-even gap using:
- lower-tier subtotal excluding II = 1.1621497378 AZN per 2-AZN variant;
- jackpot = 1.9m AZN;
- maximally favorable current category-II allocation;
- zero tax/costs.

At the statutory-maximizing assumptions used in H115, each zero category among II–VI can contribute at most:

`2 AZN × 80% prize fund × 10% category allocation = 0.16 AZN × N_prior`

to the next draw.

Therefore, with `k` prior zero categories, the most optimistic one-step overlay per current ticket is:

`0.16*k*(N_prior/N_current)`.

Representative required prior/current sales ratios are:

- 1 zero category: ~4.49–4.54x;
- 2 zero categories: ~2.25–2.27x;
- 3 zero categories: ~1.50–1.51x;
- 5 zero categories: ~0.90x under the same deliberately extreme assumptions.

The detailed table is in `data/derived/h116_4plus4_multizero_bounds.csv`.

## Empirical scale control
The existing X/XI fixed-prize winner-count estimator gives sampled 2026 sales volumes roughly 38.2k–43.8k variants in preserved payout tables. Newly indexed draw #800 gives X=841 and XI=5,381, implying `N_hat≈39.0k`, consistent with the same scale. Draw #800 again has II=0 but III–VI all nonzero.

Sources/data:
- `data/historical/az_4plus4_payout_samples_2026.csv`
- https://statlotto.com/lottery/az/4-4/1786463100000

Across the preserved detailed payout samples, the recurring observed state remains zero II with winners in III–VI. No multi-zero II–VI sample is currently preserved.

## Interpretation
The important result is not that multi-zero states are impossible. It is that the plausible two-zero state still needs an **extreme >2.25x prior/current sales collapse** even after simultaneously granting maximum prize-fund percentage, maximum 10% allocation to both empty categories, full carryover, a 1.9m jackpot, and no taxes/costs.

Three-zero states reduce the contraction hurdle to ~1.5x, but their iid frequency at current volume is roughly 1e-4 to 1e-5 for the most plausible II+III+V/VI combinations. Any realistic category allocations below the maximum 10%, or taxes/costs, raise the hurdle further.

A five-zero state could theoretically clear the optimistic bound without a sales collapse, but its iid probability at current volume is effectively negligible and no empirical example has been found.

Player number-selection clustering can alter the iid zero probabilities, so these frequencies are not terminal proof. However, the **economic ratio hurdles are deterministic upper bounds** under the recovered rule/allocation limits and remain valid regardless of how tickets are selected.

## Result
**NO SUCCESS.** H014's exceptional multi-zero branch is materially narrowed:

1. ordinary II-only is already closed by H115;
2. realistic II+III zero still requires >~2.25x sales contraction;
3. three-zero states require >~1.5x contraction but are extremely rare at current sales scale;
4. only very high-order multi-zero states can bridge the gap without contraction under maximally favorable assumptions, and no such state is observed.

## Remaining H014 trigger
Reopen this branch only when a future prior draw visibly has at least **three zero categories II–VI**, or when a two-zero draw is followed by an independently observable >2.25x sales contraction / sufficiently large operator-funded external addition, or when primary registration no. 336 rules reveal materially more favorable allocation/redistribution mechanics.
