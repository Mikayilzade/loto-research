# H172 — Rhode Island pre-locked Keno doubler architecture

Updated: 2026-08-22
Status: **PRE-PURCHASE MULTIPLIER ENTITLEMENT ARCHITECTURE VALIDATED / CURRENT 2026 TERMS + EXECUTABLE COVER NOT PROVEN / NOT SUCCESS**

## Purpose
H170-H171 found compact games whose full-cover return exceeds 100% only when a favorable random modifier is drawn after purchase. H172 searches for the stronger architecture: the modifier entitlement is known on the ticket at purchase, before the underlying Keno draw.

## Current 2026 signal
The current Rhode Island Lottery homepage (crawled in August 2026) explicitly lists a **“Kick Back with Keno Promotion”** in its live promotion carousel:
- https://www.rilot.com/

The exact 2026 promotion rules/details were not recoverable from the indexed public pages in this run. Therefore no assumption is made that the current “Kick Back with Keno” promotion is identical to the older Lucky 3 Spot doubler.

## Official recurring doubler architecture
Rhode Island Lottery official promotion rules document a recurring **Lucky 3 Spot Keno** promotion in 2024-2025. Examples:
- https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2025/LaunchAlertRules-Lucky3SpotKenoBingoDoubler.pdf
- https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2025/Lucky3SpotKenoRulesBradleyCafe-3-22-25.pdf
- https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2024/Lucky3SpotKenoRule091224.pdf

The official rules establish the key execution pattern:
- only 3-spot Keno tickets purchased at the specified location/time qualify;
- if the ticket wins, the corresponding Keno prize(s) are **doubled**;
- eligibility is printed directly on the ticket at purchase (“If this ticket wins a prize, it will be DOUBLED”);
- if the message appears on a ticket containing multiple eligible Keno games, all eligible wins on that ticket may be doubled;
- retailers may not pre-print the qualifying Keno tickets;
- qualifying Lucky 3 Spot tickets cannot be cancelled;
- the Lottery retains broad rights to modify/suspend/postpone/cancel a promotion.

This solves a major structural problem from H170-H171: the 2x entitlement itself can be known **before the Keno outcome** rather than being a random post-purchase modifier.

## Current Rhode Island Keno execution rules
Official 2026 rules:
- https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules_2026.pdf

They state:
- choose 1-10 spots from 1-80; 20 numbers are drawn;
- base wagers are $1/$2/$5/$10;
- up to 15 consecutive draws;
- ordinary Keno ticket / Registered Ticketless Play maximum price is $150;
- draws occur every 4 minutes;
- ordinary retail tickets can generally be cancelled from the same terminal before the draw, while Registered Ticketless Play cannot be cancelled.

The current online Keno page also states online ticket purchases cannot be cancelled/refunded:
- https://www.rilot.com/en-us/keno.html

Historical Lucky 3 Spot rules override ordinary cancellation by making qualifying doubled tickets non-cancellable.

## 3-spot full-cover screen
A public Keno paytable source matching the standard 80/20 3-spot structure gives, per $1 wager:
- match 3: $25;
- match 2: $2.50;
- implied published odds approximately 1:72.07 and 1:7.21.

Cross-check source used only for the numerical paytable because the current RI web page's dynamic prize table was not exposed to the crawler:
- https://www.kenosuccess.com/keno_odds.htm

**Important:** this paytable is not treated as current-primary-verified Rhode Island evidence. The calculation below is a conditional screen pending a primary current RI prize-table recovery.

For all `C(80,3) = 82,160` distinct 3-spot selections in one draw:
- cost at $1 each = **$82,160**;
- for any 20-number draw, exactly `C(20,3)=1,140` selected triples match all 3;
- exactly `C(20,2)*60 = 11,400` selected triples match exactly 2;
- ordinary deterministic gross = `1,140*$25 + 11,400*$2.50 = $57,000`;
- ordinary deterministic ratio = **69.3768%**;
- if every prize on every covered selection is deterministically doubled at no extra cost, deterministic gross = **$114,000**;
- doubled deterministic ratio = **138.7537%**;
- conditional pre-tax surplus = **+$31,840**.

Thus a genuine all-ticket 2x promotion on this paytable crosses break-even by a very large margin.

## Execution bottleneck for naive full cover
Even before tax, the naive all-triples strategy is not presently executable under the documented retail-promotion architecture.

The 2026 maximum ordinary Keno ticket price is $150. Therefore $82,160 of $1 wager units requires at least:
- `ceil(82160/150) = 548` physical tickets, even under the unrealistically favorable assumption that every ticket can be packed to the monetary cap with distinct qualifying plays.

Keno draws every 4 minutes. To place the entire naive cover for one draw inside one draw interval would require at least:
- **137 full-capacity tickets per minute**;
- **2.28 full-capacity tickets per second**.

Historical Lucky 3 Spot promotions were location-specific and explicitly prohibit advance pre-printing. No official bulk-upload/system interface capable of atomically accepting 82,160 distinct 3-spot combinations for one qualifying draw was found.

Multi-draw does not solve the core issue: it repeats a selection across consecutive draws rather than atomically loading all distinct 3-spot combinations into one target draw.

## New mathematical branch: reduced guaranteed portfolio
Naive full-space coverage is sufficient but may not be necessary.

For a selected family `F` of 3-subsets and a draw-set `S` of 20 numbers, under the doubled `$25/$2.50` table the payout is:

`50 * n3(S) + 5 * n2(S)`

where `n3` is the number of selected triples fully inside `S` and `n2` is the number intersecting `S` in exactly two points.

A smaller block-design / integer-programming portfolio could in principle guarantee payout greater than `|F|` while using far fewer than 82,160 tickets. This has not yet been solved. It is the highest-value mathematical continuation if current or future RI rules confirm an active pre-locked 2x 3-spot offer.

## Current “Kick Back with Keno” gate
The live Rhode Island homepage confirms a current Keno promotion exists, but indexed public evidence in this run did **not** reveal whether it is:
- a Lucky 3 Spot-style deterministic 2x prize promotion;
- a second-chance promotion;
- free-play / buy-X-get-Y;
- or another mechanic.

Therefore H172 does not count the current promotion as a live 138.75% cover.

## Result
- **Pre-purchase printed multiplier entitlement: VALIDATED as a real Rhode Island Lottery promotion architecture.**
- **Conditional 3-spot doubled full-cover theorem: 138.7537%** under the screened `$25/$2.50` table.
- **Current 2026 “Kick Back with Keno” exact mechanic: UNRESOLVED.**
- **Naive 82,160-line full cover: operationally non-executable under the documented 4-minute/location/pre-print constraints absent a bulk mechanism.**
- **Terminal SUCCESS: NO.**

## Reopen / next conditions
1. Recover official 2026 “Kick Back with Keno” rules and current primary RI 3-spot paytable.
2. If current promotion is a deterministic 2x 3-spot offer, solve the reduced-portfolio minimax/block-design problem and test exact retail/online acceptance throughput.
3. Search other lotteries for the same pre-printed/pre-locked free multiplier on smaller state spaces where exact coverage is operationally feasible.
