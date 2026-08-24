# H248 — Lotto.com 25% draw-discount full-cover upper bound

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: REJECTED as a guaranteed-profit full-coverage subsidy at the observed 25% level

## Question
Can a current deterministic lottery-courier percentage discount be large enough to turn an otherwise losing controlled full-space lottery construction into a strict guaranteed-profit strategy?

## Current primary evidence
Lotto.com's current Promotional Terms define promotions as reductions or waivers of official lottery-ticket cost and/or convenience fee, including percentage discounts and promotional codes. The same terms state:

- only one promotion may be used per order;
- promotions are limited to one use per customer;
- service fees still apply to discount/free-ticket promotions;
- promotions may be limited by product, state, time, availability, limits, and caps;
- Lotto.com may modify or cancel a promotion without notice.

A current indexed New York Lotto.com homepage displays `25% off $30` as an offer. Separately, the current Mystery Scratch prize table includes a `20% Discount (Draws)` prize, but that 20% entitlement is RNG-awarded rather than deterministic and therefore is not used as a guaranteed input here.

## Dominating upper-bound test
To avoid relying on missing checkout details, H248 gives the observed 25% offer a deliberately stronger interpretation than the published terms establish:

1. the player receives 25% off **the entire controlled full-space wager cost**, not merely a $30-sized order;
2. the discount is deterministic and usable on the target game;
3. all service/convenience fees are set to zero;
4. there is no promotional cap;
5. no cancellation/modification occurs after commitment.

Thus effective spend is at best `0.75*S`. If a known deterministic gross floor is `G`, discounted guaranteed return is bounded above by:

`G / (0.75*S) = base_return / 0.75`.

If this stronger-than-real quantity remains below 100%, the real 25% promotion cannot create a strict full-cover guarantee for that construction.

## Exact/authoritative prior constructions rescreened
| Construction | Prior guarantee-relevant gross return | Stronger-than-real 25%-discount return | Result |
|---|---:|---:|---|
| Ohio KENO 3-spot full cover | 65.2130% | 86.9507% | REJECTED |
| Nebraska 2by2 full cover | 38.0289% | 50.7052% | REJECTED |
| Nebraska MyDaY best all-state full-cover case | 58.4723% | 77.9631% | REJECTED |
| Millionaire for Life optimistic full-cover gross upper bound | 52.8876% | 70.5168% | REJECTED |
| Lotto America strict non-jackpot floor | 26.900868% | 35.867824% | REJECTED |

For Lotto America, the previously reported 85.2098% optimistic full-share cash return is not a strict guarantee because external jackpot sharing is unbounded by a useful pre-draw cap. The correct guaranteed-discount screen therefore uses the fixed non-jackpot gross only.

## Threshold theorem
For any controlled full-cover construction with base deterministic return ratio `r=G/S`, a percentage discount `d` can only make the strict floor profitable if:

`r/(1-d) > 1`, equivalently `d > 1-r`.

Therefore the exact no-fee discount hurdle is the construction's deterministic loss fraction. Examples:

- Ohio KENO 3-spot requires **>34.787%**;
- Nebraska MyDaY best case requires **>41.5277%**;
- Millionaire for Life optimistic bound requires **>47.1124%**;
- Nebraska 2by2 requires **>61.9711%**;
- Lotto America strict non-jackpot floor requires **>73.0991%**.

Real service fees, caps, one-use limits and product restrictions only increase these hurdles.

## Verdict
**REJECTED at 25%.** Even granting the current observed Lotto.com 25% discount a substantially stronger scope than the published terms establish, it cannot rescue the tested controlled finite-space lottery constructions. Reopen this courier-discount branch only for a materially larger deterministic player-selectable discount that exceeds the exact game-specific loss fraction after fees and caps, or for a newly identified game whose strict deterministic full-cover return already exceeds 75%.

## Sources
- Lotto.com current Promotional Terms: https://www.lotto.com/promoterms
- Current indexed NY Lotto.com homepage showing `25% off $30`: https://ny.lotto.com/
- Prior project calculations: `research/h026_millionaire_for_life_full_coverage.md`, `research/h028_nebraska_finite_coverage.md`, H240/H239 Keno calculations, and `research/h027_lotto_america_full_coverage.md`.
