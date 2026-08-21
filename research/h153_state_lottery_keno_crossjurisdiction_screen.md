# H153 — State-lottery Keno cross-jurisdiction deterministic-cover screen

Updated: 2026-08-21
Status: **NO SUCCESS / ORDINARY STATE-LOTTERY KENO FIXED-PAYTABLE CLASS MATERIALLY WEAKENED**

## Objective
Continue from H149-H152 by testing whether current non-Nebraska state-lottery Keno paytables can beat the **81.0636%** deterministic complete-cover benchmark established by La Vista Quarter Madness, or create a much smaller subsidy hurdle.

For standard Keno with 80 numbers, 20 drawn, and a fixed payout table for a k-spot wager, buying **every C(80,k) k-subset at the same stake for one draw** makes the payout invariant to the realized draw. The deterministic complete-cover return equals the expectation of one fixed k-spot wager under the hypergeometric distribution:

`R_k = sum_j payout(k,j) * C(20,j) * C(60,k-j) / C(80,k)`.

This is exact for non-progressive fixed payouts before any liability cap that could reduce payouts. Therefore a paytable can be screened analytically without enumerating all combinations.

## Current official sources checked
### Ohio Lottery KENO
Official current game page (crawled August 2026):
https://www.ohiolottery.com/games/keno

Current $1 base prizes include, among others:
- 1-spot: match 1 = $2;
- 2-spot: match 2 = $11;
- 3-spot: 3=$27, 2=$2;
- 4-spot: 4=$72, 3=$5, 2=$1;
- 5-spot: 5=$410, 4=$18, 3=$2;
- 6-spot: 6=$1,100, 5=$57, 4=$7, 3=$1.

Exact complete-cover ratios:
- Pick 1: 50.0000%
- Pick 2: **66.1392%**
- Pick 3: 65.2142%
- Pick 4: 64.9439%
- Pick 5: 64.9951%
- Pick 6: 64.7920%
- Pick 7: 65.2984%
- Pick 8: 64.7475%
- Pick 9: 64.8069%
- Pick 10: 63.6694%

Best current Ohio fixed-paytable cover = **66.1392% (Pick 2)**, requiring a deterministic subsidy >33.8608% of face cost before tax/friction.

### New York Lottery Quick Draw
Official current game page:
https://nylottery.ny.gov/draw-game?game=quickdraw

Current $1 base prizes were taken from the official Odds and Prizes table. Exact complete-cover ratios:
- Pick 1: 50.0000%
- Pick 2: 60.1266%
- Pick 3: 59.6641%
- Pick 4: 59.7361%
- Pick 5: **60.3194%**
- Pick 6: 60.0292%
- Pick 7: 59.3947%
- Pick 8: 59.5558%
- Pick 9: 59.8360%
- Pick 10: 60.1555%

Best current New York fixed-paytable cover = **60.3194% (Pick 5)**, requiring >39.6806% deterministic subsidy.

### Maryland Lottery Keno
Official current payout table:
https://www.mdlottery.com/skinless/keno/payouts/

Exact complete-cover ratios:
- Pick 1: 50.0000%
- Pick 2: 60.1266%
- Pick 3: **62.4391%**
- Pick 4: 58.2045%
- Pick 5: 54.2733%
- Pick 6: 55.6276%
- Pick 7: 59.5358%
- Pick 8: 58.8053%
- Pick 9: 56.3650%
- Pick 10: 57.1241%

Best current Maryland fixed-paytable cover = **62.4391% (Pick 3)**, requiring >37.5609% deterministic subsidy.

### West Virginia KENO GO
Official current game page:
https://wvlottery.com/games/draw-games/keno

Visible low-spot table is structurally similar to Maryland/New York (1-spot $2, 2-spot $10, 3-spot $25/$2, 4-spot $50/$5/$1, 5-spot $400/$15/$2), so its compact fixed-cover ratios do not approach the Nebraska benchmark. It was not used to claim a new exact 1-10 maximum because the full current table was not required once low-spot rates were already dominated.

## Comparison
Current exact best fixed-paytable complete-cover ratios in this packet:
- Ohio: **66.1392%**
- Maryland: **62.4391%**
- New York: **60.3194%**

Existing project benchmarks:
- Virginia Keno 1-Spot: **75.0000%** (H142)
- La Vista Quarter Madness: **81.0636%** (H151)

None of the major current state-lottery paytables screened here improves the H151 threshold. The smallest new subsidy hurdle is Ohio Pick 2 at **33.8608%**, still far worse than La Vista's **18.9364%** raw deficit (and the H152 compact execution hurdle already being monitored).

## Result
**NO SUCCESS.** This packet materially closes ordinary fixed-paytable state-lottery Keno as the likely source of a >81% deterministic cover. Nebraska special-rate/community tables remain the highest-value live Keno branch because special paytables can deviate materially from ordinary state-lottery payout ratios.

## Reopen condition
Reopen a non-Nebraska state-lottery Keno only if there is:
1. a current promotional/special paytable materially different from the ordinary table;
2. a deterministic player-owned discount/free-play subsidy large enough to bridge the exact computed deficit;
3. a fixed payout change producing >81.0636% deterministic complete-cover return; or
4. an execution feature that reduces external cost without reducing the guaranteed payout.

## Next priority
Return to Nebraska/community special-rate recovery, especially numeric Pick-1/Pick-2 tables and small-ticket specials where a $5-$25 deterministic promotion could bridge the exact deficit.