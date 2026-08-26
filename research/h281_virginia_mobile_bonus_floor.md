# H281 — Virginia current bonus-value worst-case screen

Updated: 2026-08-26
Branch: `research-work`
State: **CLOSED / NO STRICT GUARANTEED-PROFIT FLOOR**

## Scope

H225-X* was checked first and remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. H281 therefore follows the global lottery lane and does not create X21/X22.

This packet tests a different mechanism from H279/H280: instead of relying on a large subsidized all-number checkout, it asks whether a currently published Virginia Lottery promotional award itself creates a deterministic positive cash floor, and whether it can close the 50% hole in the smallest exact Pick 3 Pair cover.

## Authoritative facts checked

Virginia Lottery currently advertises that a player cashing a first-ever winning ticket through the mobile app / mobile website receives **10 free Jackpot Spectacular online games**. The offer is one per account and the bonus games expire after 24 hours.

The official Jackpot Spectacular page publishes overall odds of winning any prize of **1 in 3.99** and stakes from $0.50 to $50. Thus a non-winning game is an allowed outcome; the ten promotional games are not a covering design and no rule promises that at least one of the ten wins.

Virginia Pick 3 currently pays **$50 on a $1 Pair wager**, with 50-cent wagers receiving half. There are exactly 100 Front Pair values 00-99 (and likewise 100 Split/Back Pair values).

Virginia account terms additionally state that only prizes are withdrawable, deposits/promotional value generally are not, and the Lottery may refuse attempted purchases. H281 does not need the refusal clause for its main arithmetic closure because the checked promotion already has zero positive worst-case cash value.

## Exact arithmetic

For a complete one-copy Pair cover:

| Stake per Pair | 100-pair cost | guaranteed winning Pair prize | fixed gross ratio | bonus needed merely to break even vs cash outlay |
|---:|---:|---:|---:|---:|
| $0.50 | $50 | $25 | 50% | $25 |
| $1.00 | $100 | $50 | 50% | $50 |

Exactly one covered Pair wins for every three-digit draw, so these are deterministic, probability-free figures.

The current mobile-cashing promotion supplies ten **random instant games**, not $25+ of deterministic withdrawable value. Since Jackpot Spectacular has legal non-winning outcomes, the promotional bundle has a legal all-losing realization and therefore its strict guaranteed cash floor is **$0**.

Hence combining this offer with any Pair cover cannot improve the strict floor above the Pair cover's own 50% gross ratio. The mobile-cashing trigger itself requires a pre-existing winning ticket; the value of that ticket is not an external subsidy created by the promotion and is not counted as strategy profit.

## Stronger conclusion

This closes more than one guessed checkout size. Any strategy whose only deterministic Virginia promotional increment is these ten free Jackpot Spectacular games must assign them worst-case value zero. They can increase EV, but they cannot repair a deterministic deficit in a cover.

The same logic applies to a first-deposit offer consisting only of a finite number of uncontrolled bonus games: unless the promotion guarantees a minimum aggregate prize, the strict bonus floor remains zero.

## Verdict

**H281 CLOSED for strict guaranteed-profit use of the checked Virginia free-game bonus mechanic.**

Reopen only if Virginia publishes either:
- deterministic withdrawable Bonus Cash / fixed-value credit large enough to clear an exact-cover deficit; or
- a bonus-game bundle with a binding positive minimum aggregate prize.

## Sources

- Virginia Lottery, Mobile Ticket Cashing: current first-mobile-cashing offer of 10 free Jackpot Spectacular games.
- Virginia Lottery, Jackpot Spectacular: published 1-in-3.99 overall win odds and permitted price points.
- Virginia Lottery, Pick 3: Pair prize $50 per $1 play; 50-cent play pays half.
- Virginia Lottery Terms and Conditions: prize-withdrawal and purchase-processing rules.

## Reproducibility

- `src/loto_research/h281_virginia_mobile_bonus_floor.py`
- `data/derived/h281_virginia_mobile_bonus_floor.json`
