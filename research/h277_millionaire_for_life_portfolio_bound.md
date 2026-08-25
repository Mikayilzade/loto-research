# H277 — Millionaire for Life exact portfolio-average bound

Status: **REJECTED / CLOSED for ordinary ticket portfolios under the current game**.

## Why this game was opened

Millionaire for Life launched in February 2026 as a new multi-state game replacing Lucky for Life in many jurisdictions. It has a finite symmetric draw space, fixed lower-tier prizes, and large life-prize cash options, so it is a useful candidate for an exact full-space and portfolio-wide guarantee test.

Current official / primary-source facts checked on 2026-08-26:

- Powerball/MSLA game page: $5 per play; choose 5 numbers from 1–58 and one Millionaire Ball from 1–5; daily drawings; top prize $1,000,000/year for life. https://www.powerball.com/millionaire-for-life
- Virginia 2026 game rules: prize fund approximately 55% of wagers; top and second prize can be pari-mutuel; fixed lower tiers; cash options $18,000,000 and $2,200,000. https://cdnprodpaasmedia-valottery-com.azureedge.net/-/media/images/game-rules/2026/millionaire-for-life-197-2025.pdf
- Massachusetts current game page independently confirms the same 5/58 + 1/5 matrix, $5 wager, and lower-tier prize table. https://mobile.masslottery.com/games/draw-and-instants/millionaire-for-life

## Exact dominating full-cover model

Outcome / ticket space:

`C(58,5) * 5 = 22,910,580` plays.

At $5 per play, one-copy complete cover costs:

**$114,552,900**.

To make the rejection stronger than reality, H277 treats the published top-two cash options as if they were fixed and never diluted by external winners:

- 5 + MB: $18,000,000;
- 5 without MB: $2,200,000 per covered play;
- all lower tiers at their published fixed values.

That is deliberately favourable to the player because the official rules permit pari-mutuel reductions in the top two levels.

For any fixed draw, the one-copy cover contains exactly:

| Match | Covered plays | Gross contribution |
|---|---:|---:|
| 5 + MB | 1 | $18,000,000 |
| 5, wrong MB | 4 | $8,800,000 |
| 4 + MB | 265 | $1,987,500 |
| 4, wrong MB | 1,060 | $530,000 |
| 3 + MB | 13,780 | $3,445,000 |
| 3, wrong MB | 55,120 | $2,756,000 |
| 2 + MB | 234,260 | $5,856,500 |
| 2, wrong MB | 937,040 | $7,496,320 |
| 1 + MB | 1,464,125 | $11,713,000 |

Total dominating gross:

**$60,584,320**.

Return ratio:

**52.8876353196%**.

Deficit versus acquisition cost:

**$53,968,580**.

## Stronger portfolio-wide impossibility result

The useful result is stronger than “full cover loses”. The game is transitive/symmetric over legal plays and legal draw outcomes. Under the deliberately dominating payout table above, every single play therefore has the same average gross over all legal draws.

For any portfolio with nonnegative integer multiplicities, linearity gives the same average gross/cost ratio, **52.8876353196%**. For every finite set of legal draw outcomes:

`minimum portfolio gross <= average portfolio gross`.

Since the average is strictly below portfolio cost, there must be at least one legal draw in which gross is below cost. Therefore **no ordinary nonnegative portfolio of current Millionaire for Life plays can guarantee strict profit**, even before applying the real pari-mutuel weakening of top prizes.

This closes not merely complete coverage but every additive ticket portfolio under the checked payout structure.

## Reopen conditions

Reopen only if a future deterministic promotion/subsidy changes the player-facing payoff by enough to push the symmetry-average bound above 100%, or if a genuinely non-additive entitlement becomes available that is not represented by ordinary paid plays.

Reproducible calculation:
- `src/loto_research/h277_millionaire_for_life_portfolio_bound.py`
- `data/derived/h277_millionaire_for_life_portfolio_bound.json`
