# H160 — Michigan Red Ball Double Draw: forced-state deterministic coverage

Updated: 2026-08-21
Status: **NO SUCCESS / FORCED EXTRA-DRAW STATE VALIDATED / BASE COVER REACHES 100% GROSS BUT NOT >100%**

## Objective
Search lottery promotions where the promotional state is not merely random but becomes observable and deterministic before ticket purchase. Michigan's recurring Daily 3 `Red Ball Double Draw` is structurally interesting because white balls are removed after each failed trigger.

## Official promotion mechanics
Michigan Lottery's July 2026 promotion used a separate drum containing **five white balls and one red ball**. After each evening Daily 3 draw Monday-Saturday:
- if a white ball is selected, that white ball is removed and the process continues the next eligible day;
- if the red ball is selected, a **second Daily 3 evening draw** is conducted using the same eligible tickets;
- after a red-ball trigger, all six balls are restored.

Official 2026 source: https://milotteryconnect.com/2026/06/30/red-ball-double-draw-gives-daily-3-players-extra-chances-to-win-in-july/

Historical official posts show the same removal mechanic in 2016 and 2018, so this is a recurring promotion architecture rather than a one-off rule accident.

## Deterministic trigger theorem
Let `k` be the number of white balls already removed since the last reset (`0 <= k <= 5`). The next promo draw contains one red ball and `5-k` white balls.

- Trigger probability on the next day: `1/(6-k)`.
- Strict pre-purchase guarantee of a second Daily 3 draw exists **only at k=5**, because then only the red ball remains.

Thus a state that begins probabilistic eventually becomes fully deterministic if five consecutive white outcomes occur.

## Daily 3 Straight coverage
Current 2026 Daily 3 payout reporting confirms:
- $0.50 Straight wager;
- $250 Straight prize;
- 1,000 ordered three-digit outcomes.

A complete $0.50 Straight cover costs:
- `1000 * $0.50 = $500`.

For one Daily 3 draw exactly one covered Straight wins, so deterministic gross is:
- `$250`, i.e. **50%** of full-cover cost.

On a guaranteed-red (`k=5`) promo day the same ticket set participates in two Daily 3 drawings. Each draw independently contains exactly one covered Straight winner, therefore deterministic total gross is:
- `$250 + $250 = $500`;
- strict gross cover ratio = **100%**.

The duplicate draw therefore eliminates the game's 50% deterministic takeout for a complete Straight cover, but does **not** create positive pre-tax profit by itself.

## State table
See `data/derived/h160_red_ball_state_cover.csv`.

For `k<5`, the strict floor remains 50% because a white ball can still be drawn and there may be no second Daily 3 draw. Expected gross rises with `k`, but this project does not treat positive expectation as a guarantee.

## Subsidy corollary
The forced-red state is unusually important because the incremental subsidy hurdle collapses from roughly 50% to **anything strictly above zero** before taxes/friction.

If an independently guaranteed, compatible discount/free-play/rebate of cash-equivalent value `B>0` is locked before the full $500 cover is purchased, then the pre-tax arithmetic becomes:
- external net cost `500-B`;
- guaranteed draw gross `500`;
- pre-tax floor `+B`.

This is materially stronger than H142-H157, where large >20-40% subsidies were needed to cross break-even.

## Current execution screen
No terminal SUCCESS is claimed for 2026-08-21:
1. The specific 2026 Red Ball promotion ran in **July** and is no longer active today.
2. Michigan's current August promotion is Club Keno `Tripler Time`, whose Doubler/Tripler message is randomly assigned after purchase and therefore does not provide a pre-locked universal multiplier.
3. Michigan does have account bonus-credit, in-store free-play, coupon and Daily Spin-to-Win architectures. Some rewards are observable before play, but public pages do not establish a current universal coupon that is both usable on retail Daily 3 and large enough to survive taxes/fees.
4. Current Michigan FAQ material is inconsistent on whether Daily 3/Daily 4 are available through every online purchase interface. Therefore online bonus-credit compatibility with a complete Daily 3 basket is not treated as proven.
5. Complete 1,000-line acceptance/liability limits and after-tax treatment would still require pre-execution verification before any terminal claim.

## Important recurring-monitor condition
Reopen immediately during any future Red Ball Double Draw cycle if:
- five white balls have been removed and this state is publicly observable before sales close for the next eligible evening draw; AND
- the player already holds a deterministic compatible in-store/online free-play, coupon, cashback or other lottery subsidy; AND
- all 1,000 Straight selections can be accepted before draw close; AND
- the subsidy plus any other guaranteed cash-equivalent benefit exceeds all tax/fee/execution drag.

At `k=5`, unlike ordinary promotion states, **the promotional second draw itself is certain before purchase**.

## Result
- **Forced extra-draw state theorem: VALIDATED.**
- **Michigan Daily 3 full Straight cover on forced-red day: exactly 100% pre-tax gross.**
- **Standalone guaranteed profit: REJECTED (break-even, not positive).**
- **Subsidized forced-red branch: PROMISING RECURRING MONITOR, not current SUCCESS.**

## Sources
- Michigan Lottery Connect, 2026 Red Ball Double Draw: https://milotteryconnect.com/2026/06/30/red-ball-double-draw-gives-daily-3-players-extra-chances-to-win-in-july/
- Michigan Lottery Connect, 2018 recurrence: https://milotteryconnect.com/2018/07/30/red-ball-double-draw-gives-daily-3-players-extra-chances-to-win-2/
- Michigan Lottery Connect, 2016 recurrence: https://milotteryconnect.com/2016/07/28/red-ball-double-draw-gives-daily-3-players-extra-chances-to-win/
- Current Michigan bonus architecture: https://faq.michiganlottery.com/account-information-d9a19100/online-bonuses-f2b270a4/types-of-online-bonus-offers-08356151
- Current Daily Spin-to-Win architecture: https://faq.michiganlottery.com/promotions-giveaways-and-offers-information-62f7cc/daily-spin-to-win-c6e5ee/daily-spin-to-win-information-c6418a

## Next action
1. Search other `free second draw` or cumulative-trigger promotions where the trigger becomes deterministic before purchase and the base compact-game coverage ratio exceeds 50%.
2. During future Michigan Red Ball periods, monitor the public white-ball state and simultaneously inspect deterministic coupons/free-play already credited to the player.
3. Continue H159 live fixed-raffle screens and H157 deterministic Keno bundle monitor in parallel.
