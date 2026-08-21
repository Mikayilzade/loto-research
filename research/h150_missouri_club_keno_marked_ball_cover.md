# H150 — Missouri Club Keno marked-ball full-cover theorem

Updated: 2026-08-21
Scope: LOTTERY ONLY
Status: **MARKED-BALL COVER THEOREM VALIDATED / CURRENT MISSOURI FIXED-PAYTABLE ADD-ONS REJECTED AS GUARANTEED-PROFIT COVERS**

## Why this branch
H149 gives an exact full-cover formula for ordinary 20-of-80 Keno paytables. Missouri Club Keno adds a useful new structure: after 20 winning numbers are drawn, one winning number is designated the red Bulls-Eye; with Double Bulls-Eye a second drawn number is designated green. This creates a new combinatorial class where prize amount depends not only on total matches but on whether the ticket contains zero, one, or two distinguished winning balls.

Current official sources:
- Missouri Lottery current Club Keno page and prize tables: https://www.molottery.com/club-keno/club-keno.jsp
- Current Club Keno rules: https://www.molottery.com/club-keno/rules.jsp

The current page states:
- 20 numbers are drawn from 80;
- Bulls-Eye doubles ticket cost;
- Double Bulls-Eye triples ticket cost;
- a Bulls-Eye ticket can win with no Bulls-Eye match under the ordinary base table, with the red marked ball under the Bulls-Eye table, and Double Bulls-Eye tickets can win under base / one-mark / two-mark cases;
- only one add-on can be used on a play;
- the Multiplier add-on doubles cost and its legal wheel includes 1x;
- the maximum prize on a Club Keno ticket is $1m, and a special $5m split rule applies when more than five players win $1m on the same Spot in one drawing;
- progressive bonuses on 6/7/8 Spot are pari-mutuel and are therefore not counted in the fixed guaranteed floor here.

## Exact one-mark theorem — Bulls-Eye
Buy every `k`-subset of the 80 numbers for one drawing. Let the realized 20-number draw be `D` and let `b in D` be the red Bulls-Eye.

For a ticket with exactly `j` total drawn-number matches:
- tickets **without** `b`: `C(19,j) C(60,k-j)`;
- tickets **with** `b`: `C(19,j-1) C(60,k-j)`.

Let:
- `A_j` = ordinary Club Keno payout for j matches;
- `B_j` = Bulls-Eye payout for j matches including the marked ball.

Then for every legal draw and every possible choice of Bulls-Eye ball:

`G_BE(k) = sum_j [A_j C(19,j)C(60,k-j) + B_j C(19,j-1)C(60,k-j)]`.

At a $1 base stake the Bulls-Eye add-on costs another $1, so:

`S_BE(k)=2 C(80,k)` and `R_BE=G_BE/S_BE`.

This is a deterministic all-outcome identity, not an expected-value approximation.

## Exact two-mark theorem — Double Bulls-Eye
Let red and green marked balls be two distinct members of the 20-number draw. For tickets with j total matches, the exact numbers containing m marked balls are:

- `m=0`: `C(18,j) C(60,k-j)`;
- `m=1`: `2 C(18,j-1) C(60,k-j)`;
- `m=2`: `C(18,j-2) C(60,k-j)`.

If `D_j` is the published Double Bulls-Eye payout when both marked balls are matched, nominal fixed-table gross is:

`G_DBE(k)=sum_j [A_j C(18,j)C(60,k-j) + 2 B_j C(18,j-1)C(60,k-j) + D_j C(18,j-2)C(60,k-j)]`.

Double Bulls-Eye triples the ticket cost:

`S_DBE(k)=3 C(80,k)`.

The calculation below deliberately labels this ratio **nominal**, because the official $1m-per-ticket / $5m same-Spot liability language can only reduce the strict floor in liability-triggering states. Since the nominal ratios already fail badly, no liability-cap optimization is needed to reject the class.

## Exact current Missouri screen
Using the current official $1 prize tables:

| k | ordinary R | Bulls-Eye R | Double Bulls-Eye nominal R |
|---:|---:|---:|---:|
| 1 | 50.0000% | 55.0000% | 56.6667% |
| 2 | 60.1266% | 59.9367% | 60.3059% |
| 3 | **62.4391%** | 60.6500% | 60.9640% |
| 4 | 61.2678% | 60.5142% | 61.6110% |
| 5 | 62.2542% | 59.9948% | 61.3532% |
| 6 | 60.0292% | 59.8923% | 62.5448% |
| 7 | 60.4173% | 60.6457% | 63.9839% |
| 8 | 58.2033% | 59.0106% | 63.2694% |
| 9 | 58.4969% | 60.2907% | **65.3369%** |
| 10 | 60.1555% | 60.0678% | 64.3802% |

Best fixed-table results:
- ordinary: 3-Spot, **62.4391%**;
- Bulls-Eye: 3-Spot, **60.6500%**;
- Double Bulls-Eye nominal: 9-Spot, **65.3369%**.

Thus even the best *nominal* marked-ball cover is far below H142 Virginia Keno's already-known 75% deterministic benchmark. The best Missouri DBE case still needs a pre-owned deterministic subsidy of **34.6631% of face spend** merely to reach break-even; liability/share rules can only increase that requirement.

## Multiplier add-on closure
The Multiplier costs an additional $1 per each $1 base wager. The current official wheel contains a legal **1x** state (32 of 80 wheel slots). Therefore in the worst legal outcome the gross payout is just the ordinary base payout while external cost doubles.

For a strict guarantee the Multiplier full-cover ratio is therefore at most `R_base/2`. Since the best ordinary fixed-table cover above is 62.4391%, the best strict Multiplier floor is at most **31.2196%**. It cannot create a guaranteed-positive cover.

## What is and is not closed
Closed by this packet:
- current Missouri fixed-paytable Bulls-Eye full covers for Spots 1–10;
- current Missouri fixed-paytable Double Bulls-Eye full covers for Spots 2–10 (even before adverse liability adjustment);
- current Missouri Multiplier as a strict-guarantee modifier.

Not claimed closed:
- a future promotional Missouri paytable materially richer than today's table;
- a separately bounded progressive/rolldown state with hard sharing limits;
- deterministic external coupons large enough to exceed the exact deficit.

## Result
**NO SUCCESS.** The marked-ball combinatorics are now solved exactly and produce no current guaranteed-profit Missouri Club Keno cover. The strongest current nominal result is only **65.3369%**, below the existing 75% Virginia benchmark.

Files:
- `src/loto_research/keno_marked_ball_cover.py`
- `data/derived/h150_missouri_bullseye_full_cover.csv`
