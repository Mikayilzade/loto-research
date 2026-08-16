# H032 — Canada DAILY GRAND full-space / compact fixed-payout screen

Updated: 2026-08-16
Status: **REJECTED as guaranteed-profit full coverage**

## Target
Canada's current DAILY GRAND, using Western Canada Lottery Corporation's current published rules and prize table.

Primary sources checked 2026-08-16:
- WCLC DAILY GRAND game page: https://www.wclc.com/games/daily-grand.htm
- WCLC DAILY GRAND Combo Play: https://www.wclc.com/combo-play/daily-grand-combo-play.htm
- WCLC FAQ: https://www.wclc.com/faq-7.htm

Current mechanics:
- choose 5 main numbers from 1–49;
- choose Grand Number from 1–7;
- CAD 3 per selection;
- top advertised prize: CAD 1,000/day for life or CAD 7,000,000 lump sum;
- second: CAD 25,000/year for life or CAD 500,000 lump sum;
- lower prizes: 4+GN 1,000; 4 500; 3+GN 100; 3 20; 2+GN 10; 1+GN 4; GN only Free Play;
- if there is more than one winner in either top category, winners split that category's lump-sum pool.

## Exact full-space construction
Buy every `C(49,5)` main selection paired with every one of the 7 Grand Numbers:

`C(49,5) * 7 = 13,348,188` lines.

Cost:

`13,348,188 * CAD 3 = CAD 40,044,564`.

For a fixed winning 5-number set, the number of our distinct main-number selections with exactly m matches is:

`C(5,m) * C(44,5-m)`.

Counts:
- 5 matches: 1 main set;
- 4: 220;
- 3: 9,460;
- 2: 132,440;
- 1: 678,755;
- 0: 1,086,008.

Each main set occurs with all seven Grand Numbers, so exactly one line has the winning GN and six have a non-winning GN.

## Important internal-sharing correction
Full coverage itself creates:
- one 5+GN top-prize line;
- **six** 5-main-only lines, because all six wrong Grand Numbers accompany the winning main 5-set.

The published rules state multiple second-prize winners split the CAD 500,000 lump-sum category. Therefore our six second-prize lines do **not** each get CAD 500,000. With no external winners they share CAD 500,000 total.

For a player-favorable full-space upper bound, also assume no external top/second winners, so our top categories receive at most CAD 7,000,000 + CAD 500,000.

## Deterministic payout
Lower-tier deterministic cash:
- 4-match families: CAD 880,000;
- 3-match families: CAD 2,081,200;
- 2+GN: CAD 1,324,400;
- 1+GN: CAD 2,715,020.

Top categories, favorable no-external-winner cap:
- CAD 7,500,000 total.

Grand-Number-only lines:
- 1,086,008 Free Plays.

### Strict immediate-cash floor
Free Plays are not withdrawable cash and can lose on replay, so their strict guaranteed cash value is zero.

`cash gross = CAD 14,500,620`

`cash gross / cost = 36.2112%`

Guaranteed immediate-cash deficit:

`CAD -25,543,944`.

### Deliberately generous face-value bound
Value every Free Play at its full CAD 3 ticket face value:

`gross = CAD 17,758,644`

`gross / cost = 44.3472%`

Deficit remains:

`CAD -22,285,920`.

### Even impossible overgenerous cross-check
As a robustness check, incorrectly grant **each** of the six 5-main-only lines the full CAD 500,000 headline amount (ignoring the published split rule), and value all Free Plays at face. That impossible player-favorable gross is only:

`CAD 20,258,644 = 50.5902% of cost`.

So no interpretation remotely consistent with the published table can rescue full coverage.

## Combo Play / nonlinear-pricing check
WCLC's 5-Number DAILY GRAND Combo creates the seven Grand-Number variants for one chosen main 5-set and costs CAD 21.

Seven ordinary selections cost exactly:

`7 * CAD 3 = CAD 21`.

Therefore Combo Play is packaging convenience, **not a deterministic discount**. It does not evade the H012a/H004 linear-portfolio impossibility result.

## Conclusion
Current DAILY GRAND full-space coverage is a strict guaranteed loss. The strongest generous bound is only 44.35% of acquisition cost when respecting the top-category liability pools; strict immediate cash is 36.21%.

Status: **H032 CLOSED / REJECTED as guaranteed-profit path.**

Artifacts:
- `src/loto_research/daily_grand.py`
- `tests/test_daily_grand.py`
- `data/derived/h032_daily_grand_full_space.csv`
