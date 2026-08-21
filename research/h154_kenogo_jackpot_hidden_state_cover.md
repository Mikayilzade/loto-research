# H154 — KenoGO Jackpot hidden-state deterministic-cover screen

Updated: 2026-08-21
Status: **APPARENT MINOR/MAJOR FULL-COVER ARBITRAGE IDENTIFIED / STRICT GUARANTEE REJECTED BECAUSE TOP-PRIZE LEVEL IS DETERMINED AFTER SALES CUTOFF**

## Why this packet matters
H142-H153 searched for fixed Keno paytables whose deterministic complete-cover return approaches or exceeds 100%. A materially different mechanism exists in Australia's licensed KenoGO Jackpot: the same 1-Spot wager can pay a Regular, Minor or Major top prize.

At first glance the current public play page appears spectacular for deterministic coverage:
- every Jackpot ticket costs AUD 2;
- 20 numbers are drawn from 80;
- 1-Spot top prize is AUD 3 Regular, AUD 10 Minor, AUD 25 Major;
- therefore buying all 80 one-number tickets costs AUD 160 and always produces exactly 20 winning tickets.

This yields:
- Regular: 20 × 3 = AUD 60 = **37.5%** of cover cost;
- Minor: 20 × 10 = AUD 200 = **125.0%**, apparent guaranteed profit **+AUD 40**;
- Major: 20 × 25 = AUD 500 = **312.5%**, apparent guaranteed profit **+AUD 340**.

If the Minor/Major state were known while tickets for that same draw were still purchasable, this would be a direct deterministic overlay without any number-prediction problem.

## Current official/operator sources
Current KenoGO How To Play / Jackpot pages publish the 1-Spot prizes and state frequencies:
- https://www.kenogo.com.au/how-to-play
- https://www.kenogo.com.au/play/jackpot

Current FAQ confirms tickets can only be cancelled while the upcoming draw is still open, and accepted numbers are logged into the system:
- https://www.kenogo.com.au/faq/gameplay

Current Terms (last update 4 September 2025) state that KenoGO accepts Entries and guarantees Winnings for valid accepted Entries; however they also reserve player-specific stake limits and broad account/entry discretion:
- https://www.kenogo.com.au/terms-and-conditions

Most importantly, the Victorian Government's formal approval of KenoGO Jackpot states:
- the Top Prize level is **determined at the conclusion of the game**;
- determination is based on the **sum of all 20 drawn numbers**;
- entries for the next draw close up to **5 seconds before the start of that draw**;
- after entry closes, players may immediately purchase only the *following* draw.

Primary regulatory source:
- Victoria Government Gazette S342, 1 July 2022, KenoGO Jackpot approval: https://www.gazette.vic.gov.au/gazette/Gazettes2022/GG2022S342.pdf

The public marketing wording that the active tier is "announced before each live draw" does **not** imply it is knowable before ticket cut-off. The regulator defines the level as a function of the completed draw itself. Therefore the economically valuable state is revealed too late to enter that same game.

## Exact one-spot cover theorem
Let `P` be the 1-Spot top prize for the realized Jackpot level.

For a complete one-spot cover:
- number of selections = 80;
- ticket price = AUD 2;
- total cost `C = 160`;
- exactly 20 selected numbers are drawn;
- gross payout `G = 20P`.

So deterministic return is:

`R = G/C = 20P/160 = P/8`.

Thus break-even requires `P > 8`.

This explains the state split exactly:
- Regular `P=3`: R=37.5%;
- Minor `P=10`: R=125%;
- Major `P=25`: R=312.5%.

The mathematical overlay is real **conditional on knowing the state before entry**. The execution sequence, however, is the reverse:

`buy/close entries -> draw occurs -> drawn-number sum determines jackpot level -> level/prizes become known`.

Therefore a player cannot condition purchase of the 80-ticket cover on Minor/Major for that same draw.

## Why ordinary full cover is not a guarantee
Because Regular is a permitted realized state, the all-state strict floor of an unconditional one-spot Jackpot cover is only AUD 60 against AUD 160 spend, i.e. **37.5%**.

The public page gives approximate level frequencies:
- Regular: 1 in 1.5;
- Minor: 1 in 4.2;
- Major: 1 in 11.

Those frequencies can make the product interesting on an EV basis, but frequency does not change the strict all-outcome floor. Terminal SUCCESS requires every lawful realized state to return positive net cash.

## Prize-sharing / payout-cap secondary gate
KenoGO's current FAQ says that if multiple Tier One Top Prize winners across Classic/Bonus/Jackpot in the same draw cause total payout to exceed the maximum payout, prizes are prorated. Therefore even a hypothetical pre-announced Minor/Major state would still require the exact current maximum-payout rule and external winner exposure to be bounded before terminal SUCCESS.

For the one-spot package alone the nominal own payout is small (AUD 200 or AUD 500), but the rule is draw-wide, so external higher-spot top-prize winners can matter. This is a secondary blocker; the post-cutoff state determination already kills the direct arbitrage.

## Deposit-match interaction
KenoGO's current Terms explicitly support targeted deposit-match promotions in principle, with bonus cash non-withdrawable. Historical player reports document 100% match offers in 2024-2025. A 100% match would make Classic 1-Spot complete coverage mathematically positive before discretionary/eligibility gates:
- Classic cover face cost AUD 80;
- 100% match means AUD 40 external cash + AUD 40 bonus could fund AUD 80 face;
- exactly 20 winners × AUD 3 = AUD 60 gross;
- conditional surplus = **+AUD 20 on AUD 40 external cash**.

However no public, current, universally claimable August 2026 100% match was found in this run. Offers are player-specific and current Terms allow suspension/cancellation for perceived bonus abuse and player-specific stake limits. Therefore this is a monitor branch, not current SUCCESS.

## Result
1. **New strongest raw Keno paytable state found:** KenoGO Jackpot Major 1-Spot complete cover = 312.5% nominal deterministic return; Minor = 125%.
2. **Direct live arbitrage rejected:** the Victorian regulator states the Jackpot level is determined only at conclusion of the game from the drawn-number sum, after the same-draw entry cutoff.
3. **Unconditional strict floor:** 37.5% because Regular remains possible.
4. **Secondary cap/sharing gate:** draw-wide top-prize prorating must be bounded for any future conditional-state strategy.
5. **Promotion branch remains open only on new evidence:** a current pre-locked >=33.34% effective subsidy on Classic 1-Spot, or >=62.5% on unconditional Jackpot 1-Spot, plus no discretionary clawback, could cross strict break-even.

## Next action
- Search lottery/Keno products where the enhanced paytable state is **observable before sales close**, not derived from the draw itself.
- Prioritize pre-announced boosted Keno draws, scheduled double-prize periods, fixed promotional paytables and venue specials with a published future game/time ID.
- Continue Nebraska/community special recovery, but add this timing test: `boosted state known -> full basket accepted -> only then draw`.
- Search current Australian Keno/KenoGO targeted promotions only if the offer is publicly claimable and contractually pre-locked; historical personalised offers alone are insufficient.
