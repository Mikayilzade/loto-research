# H243 — Irish Lotto 6/45 Plus forward gate

Date: 2026-08-24
Status: NOT A SUCCESS

## Trigger

Follow-up to the prior H251-style observation that the announced September 2026 Irish Lotto Plus redesign is still structurally negative under complete coverage.

## Fresh source check

The Irish National Lottery announced that Lotto will move from 6/47 to 6/45 in autumn 2026. Lotto Plus 2 rises to a EUR 1,000,000 top prize, matching Plus 1. A third weekly draw is also being added. Independent rule summaries report the planned 6/45 Plus fixed tiers as: 6=EUR1,000,000; 5+B=EUR1,000; 5=EUR100; 4+B=EUR25; 4=EUR10; 3+B=EUR6; 3=EUR2; 2+B=EUR3. The first new-format draw is reported for 2026-09-05.

Sources checked:
- https://www.lottery.ie/news/press-releases/national-lottery-unveils-exciting-changes-to-lotto-and-lotto-plus-games
- https://irish.national-lottery.com/2026-irish-lotto-game-changes

## Structural result

Full combination coverage cannot manufacture profit from a fixed-prize add-on whose aggregate payout is below aggregate stake. Ticket selection only redistributes which tickets receive each fixed tier; complete coverage fixes the count of each outcome class.

Therefore the previously computed ~52.85% full-coverage return remains a hard rejection of the naive Plus-cover strategy: roughly 47.15% of the add-on stake is missing before operational costs or prize-limit edge cases.

## New gate

Do not spend further search budget optimizing combinations for ordinary Lotto Plus. Re-open this game only if at least one non-linear mechanism appears:

1. a promotion/rebate/free-ticket offer worth >47.15% of Plus stake;
2. a rule that causes a roll-down/overlay into Plus fixed tiers;
3. a purchase channel discount or loyalty conversion with equivalent economic value;
4. a demonstrable prize-limit interaction that increases rather than clips payout;
5. a cross-product bundle whose incremental cost for Plus is materially below EUR1 per line.

The September launch should be checked again against the final official game-rules PDF, because pre-launch summaries are not enough to certify exact economics.

## Next hypothesis

H244: search active lottery products for deterministic or near-deterministic roll-down / must-be-won events where the marginal prize pool is externally funded and the effective payout can cross 100% at a publicly observable threshold.
