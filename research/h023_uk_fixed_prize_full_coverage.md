# H023 — UK fixed-prize full-space coverage: Set For Life + Thunderball

Updated: 2026-08-15
Status: **both current games rejected as guaranteed-profit full-space strategies**

## Goal
Apply the deterministic full-coverage identity to current UK National Lottery fixed-prize games where every legal line can be enumerated and the realized payout mix is invariant to the particular draw.

The test is deliberately favorable to the player: use published headline prize values, ignore tax/execution friction, and where possible grant the full advertised top prize rather than a reduced/capped amount. If full coverage is still below cost, the guaranteed-profit path is closed immediately.

## 1. Set For Life
Official current structure:
- choose 5 main numbers from 1–47;
- choose 1 Life Ball from 1–10;
- £1.50 per play;
- prizes: 5+Life Ball = £10,000/month for 30 years; 5 = £10,000/month for 1 year; 4+LB £250; 4 £50; 3+LB £30; 3 £20; 2+LB £10; 2 £5.

Primary sources:
- https://www.national-lottery.co.uk/games/set-for-life
- https://mobile.national-lottery.co.uk/games/set-for-life/game-specific-rules

Full line space:

`C(47,5) * 10 = 15,339,390` lines.

Acquisition cost:

`15,339,390 * £1.50 = £23,009,085`.

For any realized draw, among the covered lines with exactly m main-number matches there are:

`C(5,m) * C(42,5-m)` main-number sets.

For each such main set exactly one Life Ball choice matches the drawn Life Ball and nine do not.

Deterministic winning counts:
- 5+LB: 1
- 5 without LB: 9
- 4+LB: 210
- 4 without LB: 1,890
- 3+LB: 8,610
- 3 without LB: 77,490
- 2+LB: 114,800
- 2 without LB: 1,033,200.

Using the full headline top-prize nominal cash sum `£10,000 * 12 * 30 = £3,600,000` and second tier `£120,000`, deterministic nominal gross is:

`£12,949,100`.

Nominal full-space return:

`£12,949,100 / £23,009,085 = 56.2782%`.

Guaranteed nominal loss before execution:

`-£10,059,985`.

This is already fatal to a guarantee. It is also optimistic because the top prize is an annuity and the Game Specific Rules contain a capped-prize mechanism when there are multiple winning entries. External duplicates can therefore only worsen a strict guarantee.

Status: **REJECTED**.

## 2. Thunderball
Official current structure:
- choose 5 main numbers from 1–39;
- choose 1 Thunderball from 1–14;
- £1 per play;
- published fixed prizes: 5+TB £500,000; 5 £5,000; 4+TB £250; 4 £100; 3+TB £20; 3 £10; 2+TB £10; 1+TB £5; 0+TB £3.
- National Lottery states the £500,000 top prize is not shared.

Primary source:
- https://www.national-lottery.co.uk/games/thunderball

Full line space:

`C(39,5) * 14 = 8,060,598` lines.

Acquisition cost:

`£8,060,598`.

For any realized draw, exact m-main-match counts are:

`C(5,m) * C(34,5-m)`.

For each main-number set exactly one Thunderball choice matches and 13 do not.

Relevant main-set counts:
- m=5: 1
- m=4: 170
- m=3: 5,610
- m=2: 59,840
- m=1: 231,880
- m=0: 278,256.

Applying the published prize table gives deterministic gross:

`£4,262,568`.

Full-space return:

`£4,262,568 / £8,060,598 = 52.8815%`.

Guaranteed loss before execution:

`-£3,798,030`.

Status: **REJECTED**.

## General conclusion
These two products add another useful class closure: high headline fixed prizes do not imply full-space arbitrage. Once all combinations are bought, the lower-tier payout structure is deterministic and the operator margin remains dominant.

Neither product is remotely close to the 100% deterministic-return threshold, so execution limits, purchase caps, annuity present value, taxes, and operational friction need not be modeled to reject the guarantee.

## Strategic implication
Continue using exact combinatorial screens first. Only deep-dive products whose deterministic full-space return is near or above 100%, or whose guaranteed external subsidy can bridge the exact takeout deficit.
