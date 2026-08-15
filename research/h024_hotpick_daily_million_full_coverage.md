# H024 — UK HotPicks + Irish Daily Million full-coverage screen

Updated: 2026-08-15
Status: **three additional current fixed-prize families rejected as guaranteed-profit full coverage**

## Method
For a fixed-payout subset game where a draw contains `d` winning main numbers from a universe of `N`, buying every `k`-subset makes the winning-ticket count deterministic: `C(d,k)` out of `C(N,k)` purchased lines. Therefore full-space gross return is known before the draw.

For a 6-of-39 game with an additional bonus ball and prizes separated by bonus status, counts are also deterministic by hypergeometric identities.

## 1. UK Lotto HotPicks
Current National Lottery page (checked 2026-08-15):
- main Lotto draw has 6 main numbers from 59;
- £1.00 per HotPicks play;
- fixed prizes: Pick 1 £6, Pick 2 £60, Pick 3 £800, Pick 4 £13,000, Pick 5 £350,000.

Official sources:
- https://www.national-lottery.co.uk/games/lotto-hotpicks
- draw example confirming 6 main balls and prize table: https://www.national-lottery.co.uk/results/lotto-hotpicks/draw-history/prize-breakdown/3047

Full-space deterministic returns:
- Pick 1: 6 winners / 59 lines => **61.0169%**
- Pick 2: 15 winners / 1,711 lines => **52.6008%**
- Pick 3: 20 winners / 32,509 lines => **49.2171%**
- Pick 4: 15 winners / 455,126 lines => **42.8453%**
- Pick 5: 6 winners / 5,006,386 lines => **41.9464%**

Best case is only 61.02%, so all five variants are strict guaranteed losses before execution.

## 2. UK EuroMillions HotPicks
Current National Lottery page (checked 2026-08-15):
- select 1–5 main EuroMillions numbers from 50;
- £1.50 per play;
- fixed prizes: Pick 1 £10, Pick 2 £100, Pick 3 £1,500, Pick 4 £30,000, Pick 5 £1,000,000.

Official sources:
- https://www.national-lottery.co.uk/games/euromillions-hotpicks
- draw example/prize breakdown: https://www.national-lottery.co.uk/results/euromillions-hotpicks/draw-history/prize-breakdown/1857

Because the EuroMillions main draw contains 5 numbers, full-space winners are `C(5,k)`.

Deterministic returns:
- Pick 1: **66.6667%**
- Pick 2: **54.4218%**
- Pick 3: **51.0204%**
- Pick 4: **43.4216%**
- Pick 5: **31.4649%**

Best case is 66.67%; all variants are strict guaranteed losses before execution.

## 3. Irish Daily Million
Irish National Lottery current rules (checked 2026-08-15):
- choose 6 from 39;
- one bonus number is also drawn;
- price from €1 per line;
- prizes: 6 = €1,000,000 (win or share), 5+Bonus €10,000, 5 €500, 4+Bonus €100, 4 €25, 3+Bonus €10, 3 €3;
- top prize does not roll over.

Official source:
- https://www.lottery.ie/game-information/daily-million

Full space: `C(39,6)=3,262,623` lines, so base acquisition cost is **€3,262,623**.

For any realized 6 main + bonus:
- 6: 1
- 5+Bonus: 6
- 5: 192
- 4+Bonus: 480
- 4: 7,440
- 3+Bonus: 9,920
- 3: 99,200

Even granting our jackpot line the entire €1m (favorable upper bound; real jackpot can be shared), deterministic gross is **€1,786,800**.

Optimistic gross return = **54.7658%**.
Guaranteed pre-execution loss under the favorable sole-jackpot assumption = **€1,475,823**.

Thus Daily Million full coverage is also rejected; sharing can only worsen the strict floor.

## Data
`data/derived/h024_fixed_prize_full_coverage_screen.csv`

## Conclusion
H024 closes three more current fixed-prize families. None is remotely near the 100% deterministic-coverage gate. The fast-screen heuristic remains effective: fixed-payout products with ordinary 45–70% designed payout ratios are not buy-all guarantee candidates unless a large guaranteed external subsidy is layered on top.
