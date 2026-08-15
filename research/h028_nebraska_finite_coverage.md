# H028 — Nebraska finite-game full-coverage screen

Updated: 2026-08-16
Status: **2by2 and MyDaY guaranteed-profit full coverage REJECTED; Nebraska Pick 5 full-space guarantee REJECTED under current rule structure because lower-tier cash floor is far below cost and jackpot is shareable**

## Goal
Continue the fast analytic screen of current finite lottery products, prioritizing small spaces and deterministic prize tables. This packet covers three Nebraska draw games with materially different mechanics:
1. 2by2 — two independent 2-of-26 selections with fixed/set prizes and a free Double Tuesday feature on qualifying multi-draw purchases;
2. MyDaY — a finite calendar-state game with 36,525 valid MM-DD-YY combinations;
3. Nebraska Pick 5 — 5-of-40 with a growing shareable cash jackpot and fixed-looking lower tiers that may become pari-mutuel.

Primary official sources:
- 2by2 current game page: https://m.nelottery.com/homeapp/lotto/34/gamedetail
- Nebraska 2by2 regulations: https://nelottery.com/homeapp/about/regulations
- MyDaY current game page: https://m.nelottery.com/homeapp/lotto/33/gamedetail
- Nebraska Lottery regulations, Chapter 1500 MyDaY: https://nelottery.com/homeapp/about/regulations
- Nebraska Pick 5 current game page: https://m.nelottery.com/homeapp/lotto/31/gamedetail
- Nebraska Lottery regulations, Chapter 800 Pick 5: https://nelottery.com/homeapp/about/regulations

## 1. 2by2
Current rules/page:
- choose 2 red numbers from 1–26 and 2 white numbers from 1–26;
- $1 per play;
- top published prize $22,000;
- 2+1 / 1+2 pays $100;
- 2+0 / 0+2 / 1+1 pays $3;
- 1+0 / 0+1 pays a free $1 Quick Pick;
- qualifying multi-draw purchases divisible by 7 receive Double Tuesday, doubling Tuesday prizes;
- regulations explicitly say that if more than ten top-prize plays occur, top-prize liability is divided, and if prize-reserve funding is insufficient set prizes can cascade into pari-mutuel treatment.

### Full-space identity
One side has `C(26,2)=325` possible pairs, so the full Cartesian space is:

`325^2 = 105,625 plays`.

Relative to the winning pair on either color, exact overlap counts are:
- overlap 2: 1 pair;
- overlap 1: `C(2,1)C(24,1)=48` pairs;
- overlap 0: `C(24,2)=276` pairs.

Buying every play once therefore fixes the number of each match class for every draw.

Give every published cash prize its full face value and ignore all liability reductions. Also give free-ticket wins **zero terminal cash value**, because a replay can legally end with no cash payout and thus cannot support an all-outcome cash-profit guarantee.

Optimistic deterministic cash gross:

`22,000 + 2*(48*100) + 2*(276*3) + 48^2*3 = 40,168`.

Cost = **$105,625**.

Return = **38.0289%**.

### Double Tuesday package
To qualify, buy the same full-space portfolio across seven consecutive drawings. Six draws pay the normal schedule and Tuesday is doubled.

Cost:

`7 * 105,625 = $739,375`.

Optimistic cash gross:

`6*40,168 + 2*40,168 = $321,344`.

Return = **43.4616%**.

Even the free doubling feature does not remotely close the gap. Any actual pari-mutuel reduction makes it worse.

**Result: REJECTED guaranteed-profit full coverage.**

## 2. MyDaY
Current rules/page:
- choose a valid month, day and two-digit year;
- $1 per play;
- only valid calendar dates are accepted;
- February 29 is accepted for two-digit years divisible by 4, including 00;
- published current prizes: exact Month+Day+Year $5,000; Day+Year $365; Month+Year $52; Month+Day $12; Year $7; Day $4; Month $1;
- a play receives only its highest matching category.

### Exact state space
Across years 00–99 there are 25 leap years under the published rule and therefore:

`75*365 + 25*366 = 36,525`

valid dates. Full-space cost = **$36,525**.

Unlike ordinary k-of-n games, the number of partial matches depends slightly on the realized winning calendar date. The code enumerates every legal winning date and computes exact mutually-exclusive prize counts using month/day/year intersections.

Across all 36,525 legal draw states:
- minimum deterministic gross = **$17,580**;
- maximum deterministic gross = **$21,357**;
- worst return = **48.1314%**;
- best return = **58.4723%**.

Thus even the most favorable possible calendar geometry remains more than 41% below cost before execution friction.

**Result: REJECTED guaranteed-profit full coverage.**

## 3. Nebraska Pick 5
Current rules/page:
- choose 5 of 40;
- $1 per play;
- jackpot starts at $50,000 and rolls;
- jackpot is divided equally among multiple winners;
- published lower prizes: 4/5 = $500, 3/5 = $9, 2/5 = free $1 Quick Pick;
- current rules warn that set prizes can be paid pari-mutuel in unusual circumstances and be lower than the published levels.

Full space:

`C(40,5) = 658,008 plays`, costing **$658,008**.

For any winning 5-set, full coverage contains:
- 1 jackpot line;
- `C(5,4)C(35,1)=175` four-match lines;
- `C(5,3)C(35,2)=5,950` three-match lines.

Optimistically treating the $500 and $9 tiers at full face value gives deterministic non-jackpot cash:

`175*500 + 5,950*9 = $141,050` = **21.4359%** of cost.

Free Quick Picks are zero terminal cash floor for guarantee purposes.

If our jackpot line were the **sole** jackpot winner, the jackpot cash amount would need to exceed:

`658,008 - 141,050 = $516,958`

before tax/execution merely to reach break-even. But a strict guarantee cannot assume sole winner: the official rules divide the jackpot among multiple winners, and there is no useful pre-draw hard cap on external duplicate jackpot plays. Lower tiers can also be reduced pari-mutuel.

Recent July 2026 Nebraska Pick 5 examples shown on the official site were only tens/hundreds of thousands of dollars, well below the sole-winner $516,958 hurdle in the sampled states.

**Result: REJECTED as a current guaranteed-profit full-space construction. A sufficiently large jackpot may become an EV/state lead, but not a strict guarantee without a hard bound on sharing.**

## Code / data
- `src/loto_research/nebraska_coverage.py`
- `tests/test_nebraska_coverage.py`
- `data/derived/h028_nebraska_full_coverage.csv`

## Strategic conclusion
H028 closes three more finite-game families without simulation or brute force:
- fixed pair-product game + deterministic weekly promotion;
- finite calendar-state game;
- small progressive 5-of-40 game.

None produces a guaranteed positive cash floor. The strongest result in this packet is only **58.47%** (best-state MyDaY), while 2by2 Double Tuesday reaches only **43.46%**. Nebraska Pick 5 remains structurally incapable of terminal guarantee under current rules because the jackpot is shareable and lower prize liabilities can be reduced.

Next highest-value work remains:
1. continue fast screens of current finite/final-draw products with unusually high fixed cash floors or genuine deterministic subsidies;
2. return to H020 if executable public order-book data becomes available;
3. revisit H010/H014/H007 only when authoritative data gates open.
