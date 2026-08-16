# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H048 action-cash gate screened, H049 make-whole + yield mechanism identified**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H048/H049 — newest packet
Files:
- `research/h048_action_cash_and_makewhole_screen.md`
- `data/derived/h048_h049_screen.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H048_H049_APPEND.md`

## H048 current Azerbaijan deterministic action cash
### OKX Azerbaijan welcome — active through 2026-12-31
Official current campaign is explicitly Azerbaijan-accessible, but rewards are **trading bonuses**, not vested withdrawable cash; supply is FCFS and OKX retains postponement/exclusion/amendment/cancellation discretion.

Status: **REJECTED strict-guarantee entitlement**.

### OKX CIS community — active through 2026-10-10
Azerbaijan is eligible, but deterministic task rewards are nonwithdrawable trading bonuses and weekly giveaways remain random/discretionary.

Status: **REJECTED strict guarantee**.

### Bybit LATAM fixed first-deposit airdrop
Current 2026-07-01 to 2026-09-30 promotion proves a stronger mechanism: qualifying new users who make/maintain a 100-USDT deposit receive a 10-USDT airdrop to Spot/Funding account. However listed eligible jurisdictions are Latin America and exclude Azerbaijan; rewards are also limited/FCFS.

Status: **fixed-action cash/token mechanism validated, not executable for user**.

## H049 — principal make-whole + positive yield
A materially stronger construction was identified in Bitget USDGO promotions.

Published retail mechanics during the overlapping 2026 campaign:
1. convert USDT → USDGO through Convert;
2. hold at least 14 days;
3. convert USDGO → USDT;
4. if exit USDT < original USDT principal, Bitget pays the exact shortfall as a slippage bonus;
5. if exit is higher, user keeps the gain;
6. **all interest earned during the holding period remains entirely the user's and does not reduce the slippage bonus**.

Therefore, under irrevocable eligibility and ignoring external/platform default, terminal value satisfies:

`exit + max(0, principal-exit) + yield >= principal + yield`.

This is the first discovered mechanism that directly has the mathematical shape needed for a deterministic positive floor: **principal make-whole + separately retained positive yield**.

### Why not SUCCESS today
- latest retail holding-APR extension ended **2026-08-01**;
- Convert slippage bonus still has end date **TBD** in the latest retrieved announcement, but a simultaneously eligible current retail positive-yield floor is not proven;
- a separate USDGO Simple Earn offer advertises `up to 10%` with end TBD, but rules retrieved do not prove that moving the USDGO into Simple Earn preserves Convert make-whole eligibility;
- promotion pool can deplete and Bitget reserves amendment/cancellation/final-interpretation rights;
- all funding/withdrawal/platform-failure branches are not yet bounded.

At the historical retail floor of 3.75% APR, 14-day nominal yield was about **0.1438%** before external costs; at 6%, about **0.2301%**.

### Institutional control
Bitget's institutional USDGO plan launched 2026-07-17 and explicitly provides full slippage compensation with end date TBD, proving the mechanism remains live in another user class. It is not a retail/Azerbaijan terminal result.

H049 status: **STRONG PROMISING MECHANISM; NOT CURRENT SUCCESS**.

# H047 — vested cash entitlement / rebate screen
H047 showed that post-settlement rebates/refunds do not repair whole-market void branches when they are earned only from valid settled activity. The subsidy must be vested before the voidable/random branch or survive it contractually.

# H046 — prior same-venue gate
Same-market exchange dutching with `sum(1/o_i)<1` remains a real ordinary-settlement surebet after matched execution, but exchange rules permit reachable whole-market void/cancellation states. Without an independent vested subsidy, terminal strict profit floor is 0.

# Strongest non-terminal positive-EV lottery result
## H037 Irish Lotto Plus Million Euro Raffle
Six recovered special-event raffle-winner counts remain materially below modeled break-even participation. Strong +EV overlay remains, but recipient selection is random and external tickets remain, so strict guarantee is rejected.

# Other active / blocked branches
- H020 live two-sided arbitrage: mechanism validated; non-terminal without vested subsidy.
- H019 capped fixed-prize saturation: valid in principle; sampled instances fail full-cap cash-floor economics.
- H007 high-frequency RNG: data-gated; trustworthy ordered bulk history missing.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# Audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` remains the permanent master trail. Because connector reads of that large file are truncated, recent rows are preserved in continuation shards rather than risking destructive replacement. Latest shard: `research/CHECKED_PROJECTS_AND_TESTS_H048_H049_APPEND.md`.

# General terminal gates now established
Any SUCCESS must prove all of:
1. contract permission / irrevocability;
2. complete execution/fill;
3. settlement isomorphism for cross-product hedges where relevant;
4. strictly positive void/cancellation floor;
5. commissions, taxes, funding/FX, limits and withdrawals included;
6. promotion/rebate entitlement survives every allowed branch;
7. for H049-like constructions, principal redemption/make-whole and a strictly positive reward must be simultaneously eligible and fixed before capital is committed.

# Next priorities
1. **H050 current principal-protected yield / make-whole scan:** search live retail Azerbaijan-accessible stablecoin/fiat products with explicit redemption floor or make-whole plus separately retained fixed positive reward.
2. Determine whether the still-TBD Bitget USDGO Convert slippage bonus can currently coexist with any retail HodlerYield/Simple Earn product without breaking make-whole eligibility; retrieve current product terms rather than infer.
3. Bound deposit/convert/withdrawal/network/FX costs and minimum position size for any H050 candidate.
4. Search bank/e-money/regulated-exchange signup/deposit rewards where principal is withdrawable and fixed reward vests after user-controlled actions without wagering.
5. H020 live arbitrage only if paired with H047/H049-style vested subsidy.
6. H037 broaden controls / recalculate after autumn-2026 rule change.
7. H019 only if capped-entry economics materially improve.
8. H006/H007 after reliable histories/machine metadata become obtainable.
9. H010/H014 if new authoritative data routes appear.
10. Before EXHAUSTED: additional deterministic action/rebate scans, Bayesian hidden-state inference and causal implementation tests.
