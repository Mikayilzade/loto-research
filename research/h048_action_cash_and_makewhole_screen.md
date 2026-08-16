# H048/H049 — deterministic action cash and make-whole yield screen

Updated: 2026-08-16
Status: **NO SUCCESS; H048 current action-cash screen negative, H049 mechanism class strongly validated historically but current retail profit floor incomplete**

## Goal
After H047 showed that post-settlement betting rebates cannot repair a void branch, search for rewards whose qualifying actions are under the user's control and then inspect a stronger adjacent construction: principal make-whole protection plus positive yield.

## H048 — current deterministic action/reward screen

### OKX Azerbaijan welcome campaign — current through 2026-12-31
Official OKX campaign page states:
- campaign is available to users in Azerbaijan;
- new user must enroll, complete KYC, first deposit and trading-volume tasks;
- first task: deposit $100+ and trade $1,000+ for 10 USDT;
- total rewards are **trading bonuses**, not withdrawable cash;
- reward pool is limited / first-come-first-served;
- OKX may postpone rewards, exclude participants, amend/cancel rules and has final interpretation.

Source: https://www.okx.com/ar/campaigns/welcomeoffer-az

Conclusion: **not vested cash and no contractual positive cash floor**. It cannot satisfy H047/H048 terminal gate.

### OKX CIS community campaign — current through 2026-10-10
Azerbaijan is explicitly eligible. The deterministic tasks yield non-withdrawable trading bonuses and are first-come-first-served; weekly giveaways are random/discretionary.

Source: https://www.okx.com/ua/campaigns/cis-community-2026

Conclusion: **REJECTED for strict guarantee**.

### Bybit fixed first-deposit airdrop — strong mechanism, wrong geography
Current 2026-07-01 to 2026-09-30 LATAM campaign states that a qualifying new user who deposits 100 USDT and maintains it for the required period receives a 10 USDT airdrop. Participation is free; payout goes to Spot/Funding account. However eligibility is restricted to listed Latin-American jurisdictions and does **not** include Azerbaijan. Rewards are also limited/FCFS.

Source: https://www.bybit.com/en/promo/campaign/DepositayGana35USDT

Conclusion: fixed-action withdrawable-token reward mechanism exists, but **not executable for Azerbaijan**.

### Other current/recent action rewards
- Bitget card 10-USDT fixed airdrop required card approval + $30 spend, but campaign ended in June 2026 and quota was FCFS.
- Recent Bitget MEA buy/trade reward ended 2026-08-06 and required trading; no current entitlement.
- Referral/affiliate rewards depend on third-party qualification or prohibit self-referral, so they fail the all-actions-under-user-control gate.

## H048 conclusion
A current Azerbaijan-accessible positive **withdrawable cash/token entitlement** earned only from deterministic user-controlled non-random actions was **not found** in this packet. Current Azerbaijan-specific OKX offers are bonuses rather than vested cash and retain FCFS/discretionary failure branches.

---

# H049 — make-whole principal + yield

## Key construction
Suppose a platform contractually provides:
1. entry conversion of principal P into asset A;
2. after holding period H, exit conversion back to base currency;
3. a make-whole payment equal to `max(0, P - exit_amount)`;
4. positive yield Y earned during H that is explicitly retained by the user;
5. no fee/tax/withdrawal cost exceeding Y;
6. entitlement survives all allowed branches and cannot be cancelled after entry.

Then, ignoring counterparty default but including conversion outcomes:

`terminal base value = exit_amount + max(0, P-exit_amount) + Y >= P + Y`.

If `Y > all nonrecoverable costs`, the construction has a deterministic positive nominal floor.

This is materially stronger than ordinary cashback, bonus bets or loss refunds because the make-whole protects **principal**, while yield supplies the positive margin.

## Bitget USDGO — real historical/current-overlap evidence
Official Bitget USDGO announcements state:
- retail users could hold USDGO and earn daily APR;
- USDT→USDGO→USDT Convert users who held at least 14 days received a slippage bonus exactly equal to the shortfall when the exit USDT amount was below initial USDT principal;
- if exit amount exceeded principal, no bonus was paid (the user kept the conversion gain);
- all interest earned during the holding period remained entirely the user's and did not reduce the slippage bonus.

Most important official announcement:
https://www.bitget.com/support/articles/12560603888534

The July extension paid up to 6% APR through **2026-08-01**, while the Convert-slippage bonus start was 2026-05-17 and its end remained **TBD** in the latest retrieved announcement.

Thus during the overlap period the published mechanics implement the exact H049 economic shape: **principal make-whole + separately retained positive yield**.

At 3.75% APR, 14 days corresponds to about `3.75% * 14/365 = 0.1438%` nominal yield before any external funding/withdrawal costs. At 6%, the same 14 days is about `0.2301%`.

## Why this is not current terminal SUCCESS on 2026-08-16
1. The retail holding-APR extension retrieved from the latest USDGO hold announcement ended **2026-08-01**.
2. The slippage bonus itself still shows end date TBD, but without a currently proven retail yield that is simultaneously eligible, the positive margin is not established today.
3. Bitget states the promotion can end early if the pool is depleted and reserves the right to amend/revise/cancel it and to final interpretation.
4. The announcements do not create a proven lower bound on external funding/withdrawal costs or platform/counterparty failure.
5. A separate USDGO Simple Earn promotion advertises 'up to 10%' with end TBD, but the retrieved rules do not prove that USDGO moved into Simple Earn remains eligible for the retail Convert slippage make-whole. Combining them would therefore be an unsupported assumption.

## Current institutional lead
Bitget's 2026-07-17 institutional-exclusive USDGO plan explicitly states full spot-purchase slippage compensation for eligible institutional users, with end date TBD. This validates that the make-whole mechanism remains active in another user class, but it is not a retail/Azerbaijan executable result.

Source: https://www.bitget.com/support/articles/12560603889284

## H049 status
**PROMISING MECHANISM / NOT SUCCESS.** This is the closest deterministic construction found so far because it can mathematically create a positive floor if make-whole and positive yield are simultaneously irrevocable and eligible. The historical retail overlap is real. The missing current proof is a live retail yield + make-whole combination with entitlement fixed before capital is committed and all costs/withdrawal branches bounded.

## Next test
Prioritize current stablecoin/fiat promotions with:
- explicit 1:1 redemption or make-whole guarantee;
- separately retained fixed positive interest/reward;
- current Azerbaijan/retail eligibility;
- no FCFS pool depletion after entry;
- no discretionary cancellation of already-earned entitlement;
- explicit fee-free entry/exit/withdrawal or enough fixed margin to cover worst-case costs.

Do not treat ordinary variable APR products as guaranteed profit unless a contractual minimum yield and redemption floor are both established.
