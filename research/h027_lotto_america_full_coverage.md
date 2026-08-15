# H027 — Lotto America full-space coverage

Updated: 2026-08-15
Status: **REJECTED as current guaranteed-profit full coverage**

## Question
Can the relatively small Lotto America combination space make a buy-every-line strategy strictly profitable when the jackpot is large?

## Current official structure
Primary/current operator sources used:
- Minnesota Lottery Lotto America page;
- Iowa Lottery Lotto America results/prize table;
- Minnesota Lottery July 2026 jackpot-winner page/current-site capture.

Verified structure:
- choose 5 of 52 white numbers + 1 Star Ball of 10;
- base play costs $1;
- All Star Bonus costs an additional $1 and multiplies non-jackpot prizes by 2x–5x;
- base fixed-prize table: 5=$20,000; 4+SB=$1,000; 4=$100; 3+SB=$20; 3=$5; 2+SB=$5; 1+SB=$2; SB-only=$2;
- jackpot is shared among multiple jackpot winners;
- published lower-tier amounts can be reduced pari-mutuel under game rules.

## Exact full-space identity
Total base lines:

`C(52,5) * 10 = 25,989,600`.

Base full-space cost:

`$25,989,600`.

For any realized draw, buying every line once gives the same exact non-jackpot outcome counts. The deterministic base non-jackpot payout is:

- 5 without SB: 9 × $20,000 = $180,000
- 4+SB: 235 × $1,000 = $235,000
- 4 without SB: 2,115 × $100 = $211,500
- 3+SB: 10,810 × $20 = $216,200
- 3 without SB: 97,290 × $5 = $486,450
- 2+SB: 162,150 × $5 = $810,750
- 1+SB: 891,825 × $2 = $1,783,650
- 0+SB: 1,533,939 × $2 = $3,067,878

Total deterministic non-jackpot gross, before any pari-mutuel reduction:

`$6,991,428` = **26.9009% of base full-space cost**.

Therefore a sole-winner jackpot cash value would need to exceed:

`$25,989,600 - $6,991,428 = $18,998,172`

just to reach break-even before tax, execution, capital cost, lower-tier pari-mutuel reduction, or external jackpot sharing.

## Strong historical/current-regime stress test
The July 18, 2026 drawing had an advertised annuity jackpot of **$34.12m** and produced a Minnesota jackpot winner. Minnesota Lottery reported the cash option as **$15,154,248**.

Even granting our hypothetical full-space portfolio the **entire** cash jackpot and granting every lower-tier prize at the unreduced published amount:

`$15,154,248 + $6,991,428 = $22,145,676`.

Against $25,989,600 cost:
- optimistic gross return = **85.2098%**;
- deterministic deficit = **$3,843,924**.

Thus a recent very large Lotto America jackpot still failed the full-space cash hurdle even before sharing/tax/execution.

## All Star Bonus
If every line also buys All Star Bonus:
- total cost doubles to **$51,979,200**;
- jackpot is not multiplied;
- worst legal multiplier is 2x, so deterministic non-jackpot floor is at most **$13,982,856** before any pari-mutuel reduction;
- sole-winner jackpot cash hurdle becomes **$37,996,344**.

The July 18, 2026 $15,154,248 cash jackpot is far below that hurdle. ASB therefore worsens the strict guaranteed-coverage threshold in the worst legal multiplier state.

## Guarantee theorem / rejection
Even if a future jackpot cash value eventually exceeds the sole-winner hurdle, strict guaranteed profit still fails under current rules because:
1. the jackpot is divided among multiple jackpot winners;
2. no useful pre-draw hard cap on external duplicate jackpot winners was found;
3. lower-tier published amounts may themselves be paid pari-mutuel and reduced;
4. execution of 25.99m retail lines has enormous operational/capital friction.

So a future high jackpot could create an **EV / conditional sole-winner lead**, but not a strict all-outcome guarantee under the current rule structure.

## Data / code
- `data/derived/h027_lotto_america_full_coverage.csv`
- generic exact engine: `src/loto_research/special_ball_coverage.py`
- regression tests: `tests/test_special_ball_coverage.py`

## Conclusion
**H027 REJECTED as a current guaranteed-profit full-space strategy.**

Notable result: Lotto America is much closer than Powerball on raw full-space economics because its combination space is far smaller, but the strongest recent verified cash jackpot still produced only 85.21% optimistic full-space return, and sharing/pari-mutuel rules block a strict guarantee even if a larger future cash jackpot crosses the sole-winner arithmetic hurdle.
