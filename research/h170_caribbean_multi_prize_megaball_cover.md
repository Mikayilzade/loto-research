# H170 — Caribbean multi-prize / Mega Ball deterministic coverage screen

Updated: 2026-08-22
Status: **CONDITIONAL >100% STATE FOUND / STRICT GUARANTEE REJECTED BECAUSE MEGA BALL STATE IS RANDOM; MULTI-PRIZE BASE GAMES NEGATIVE**

## Purpose
H169 closed the current North Carolina forced-Double-Draw route because a 100-selection Pair basket cannot be atomically reserved/rolled back against liability limits. The next highest-value class is a lottery where one paid number participates in multiple prize drawings or where an add-on can lift a compact full cover above 100% with fewer selections.

This packet screens current Barbados Pick 3/Pick 4 multi-prize draws plus Mega Ball, and uses Curaçao Wega di Number as a regulated three-prize control.

## Source set
Current official Barbados Pick 3 rules/prize table:
- https://www.mybarbadoslottery.com/games/pick-3

Current official Barbados Pick 4 rules/prize table and liability-limit language:
- https://www.mybarbadoslottery.com/games/pick-4

Current Barbados results/home page showing Mega Ball can be `NONE`:
- https://www.mybarbadoslottery.com/

Supreme Ventures current Mega Ball mechanism description (same Caribbean Mega Ball feature architecture):
- https://supremeventures.com/game/mega-ball/
- chamber described as 2 white balls + 1 gold ball; Mega Ball draw follows main game.

Curaçao Gaming Authority Wega di Number regulation/explanation:
- https://www.cga.cw/regulation/numbers-lottery

## Barbados Pick 3 — ordinary three-prize full cover
Each Pick 3 draw produces three separate 3-digit prize numbers (1st, 2nd, 3rd). A $1 Straight pays:
- first: 400
- second: 75
- third: 50

Cover all 1,000 ordered 000–999 Straights:
- spend = **1,000**
- every draw guarantees one covered first-prize number, one covered second-prize number, one covered third-prize number
- deterministic base gross = `400 + 75 + 50 = 525`
- deterministic return = **52.50%**

So the fact that one paid panel participates in three prize outcomes does not by itself cross break-even.

## Barbados Pick 3 + Mega Ball — important conditional >100% state
Mega Ball doubles the base ticket price. If Mega Ball is successfully drawn, the official Pick 3 table gives Straight totals:
- first: 1,400 = 400 base + 1,000 MB
- second: 375 = 75 base + 300 MB
- third: 250 = 50 base + 200 MB

All-1,000 Straight cover with MB:
- spend = **2,000**
- if Mega Ball succeeds: deterministic gross = `1,400 + 375 + 250 = 2,025`
- conditional return = **101.25%**
- conditional pre-tax surplus = **+25 = +1.25%**

This is a real mathematical inversion: the published MB prize schedule turns exact full coverage positive **conditional on the MB-success state**.

### Pair cover is stronger and much smaller
Current Pick 3 Pair payouts are:
- first base 40, MB 120, total 160
- second base 8, MB 24, total 32
- third base 5, MB 15, total 20

Cover all 100 Front Pair outcomes with MB:
- 100 Pair wagers × 2 total price = **200**
- if MB succeeds, gross = `160 + 32 + 20 = 212`
- conditional return = **106.00%**
- conditional pre-tax surplus = **+12 = +6.00%**

Without MB success, the same 200 spend receives only base prizes `40+8+5=53`, i.e. **26.50%**.

Thus H170 identifies a materially better conditional overlay than the Straight version and reduces the complete-cover basket from 1,000 selections to 100.

## Why this is NOT a strict guarantee
The current Barbados site explicitly describes Mega Ball as an add-on drawn after Pick 3 and current results can show Mega Ball `NONE`. There is no current official Barbados rule found that makes the next Mega Ball outcome certain/forced after prior misses.

The current Supreme Ventures Mega Ball mechanism description gives the relevant random-state architecture directly: the chamber contains **2 white balls and 1 gold ball**, with the Mega Ball draw after the main draw. Nothing in the current mechanism provides cumulative removal of losing balls or a publicly observable forced-gold state before betting closes.

Therefore a legal outcome branch remains:

`complete 100-Pair MB cover accepted -> Mega Ball does not succeed -> gross 53 on spend 200`.

That branch is a 73.5% loss before any tax/friction, so terminal guarantee fails decisively.

Do not value the conditional 106% state as guaranteed EV without the actual MB-success probability and current operator-specific draw rules. For terminal-guarantee purposes probability is irrelevant: one allowed non-MB branch is enough to reject.

## Barbados Pick 4 control
A $1 Straight pays base:
- first 4,000
- second 1,000
- third 250

Full 10,000-number Straight cover:
- base spend 10,000
- base gross 5,250 = **52.50%**

With MB, ticket cost doubles to 20,000; successful-MB totals are:
- first 14,000
- second 4,000
- third 1,250

Successful-MB full-cover gross = 19,250 = **96.25%**, still below break-even even in the favorable state.

So Pick 4 is **rejected even conditional on MB success** for Straight full coverage.

## Liability-limit execution note
The current Barbados Pick 4 page explicitly states per-draw liability limits and automatic rejection of further transactions once a sequence/bet-type limit is reached, with pari-mutuel treatment possible. The Pick 3 public materials also carry liability-limit language in current mirrored game information.

Therefore even if a future forced-gold state were discovered, a strict proof would still need:
1. all required 100 Pair selections accepted before any become irrevocable, or an all-or-none rollback right;
2. no liability-limit reduction affecting the payout floor;
3. tax/claim/transaction costs below the 6% Pair margin.

This is analogous to H169 but with a better conditional 106% gross ratio.

## Curaçao Wega di Number — regulated three-prize control
The Curaçao Gaming Authority states that each Wega di Number drawing draws three four-digit numbers: first, second, third prize. Regulated series include 2-digit, 3-digit and 4-digit tickets.

Using the published prize structure summarized by the regulator/current game data:
- 2-digit: 40 + 20 + 10 over 100-number full cover = **70%** nominal return before ticket surcharge/tax;
- 3-digit: 400 + 200 + 100 over 1,000-number cover = **70%**;
- 4-digit: 3,000 + 1,500 + 750 over 10,000-number cover = **52.5%**.

The regulator additionally states a nominal NAf 1 ticket is sold for NAf 1.13 including extra-draw participation and sales tax, so actual cash return ratios are lower than those nominal cover ratios.

Result: **REJECTED deterministic full-cover guarantee**.

## General theorem / reusable screen
For a digit lottery where one wager participates in `m` fixed prize numbers in the same draw, a full Straight cover over `N` states at unit cost `c` has deterministic ratio:

`R = (sum_j p_j) / (N*c)`.

If a binary add-on costs an extra `a` per covered state and pays extra prizes `b_j` only in a favorable add-on state, then:

`R_favorable = sum_j(p_j+b_j) / (N*(c+a))`

but the strict all-state guarantee is bounded by the unfavorable state:

`R_strict <= sum_j p_j / (N*(c+a))`.

Therefore a random multiplier/add-on cannot create a strict guaranteed overlay unless the unfavorable state itself is >=100%, or the favorable state is known/forced before purchase.

H170 Barbados Pick 3 Pair illustrates this exactly:
- favorable MB state: 106%
- unfavorable state: 26.5%
- strict floor: 26.5%, not 106%.

## Result
- Barbados Pick 3 ordinary three-prize full cover: **52.5%, REJECTED**.
- Barbados Pick 3 Straight + successful MB: **101.25% conditional, NOT GUARANTEED**.
- Barbados Pick 3 Pair + successful MB: **106.0% conditional, strongest H170 lead, NOT GUARANTEED**.
- Barbados Pick 4 Straight + successful MB: **96.25%, REJECTED even in favorable state**.
- Curaçao Wega di Number multi-prize cover: **<=70% nominal before surcharge, REJECTED**.
- Lottery terminal SUCCESS: **NO**.

## Reopen condition
Reopen Barbados Pick 3 + MB only with materially new evidence that the Mega Ball success state is **known/forced before ticket purchase** (for example a cumulative physical-ball mechanism with losing balls removed and a final forced gold state), or with a deterministic promotion/subsidy that raises the non-MB branch itself above 100% after execution/tax.

## Next lottery research
1. Search other current Caribbean/number-lottery `multiple prize numbers per paid wager` products for fixed tables where the sum of guaranteed prize payouts already exceeds cover cost without a random add-on.
2. Search forced/cumulative colored-ball mechanics specifically for a pre-purchase forced state paired with a compact Pair/1-Spot cover.
3. Continue scheduled Keno special-paytable search for deterministic >100% coverage states known before purchase.
4. Continue fixed-board raffle residual takeover monitor using H159 theorem.
