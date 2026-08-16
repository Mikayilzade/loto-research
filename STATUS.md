# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H047 vested-cash entitlement gate completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H047 — vested cash entitlement / rebate screen
Files:
- `research/h047_vested_cash_entitlement_screen.md`
- `data/derived/h047_vested_cash_screen.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H047_APPEND.md`

## Key theorem
H046 proved ordinary same-market post-fill arbitrage still has a reachable whole-market-void branch with zero wagering profit.

H047 now proves that a post-settlement rebate/refund cannot repair that branch when the promotion pays only on valid settled activity. If the qualifying market is void, both the arbitrage profit and qualifying rebate are zero.

Therefore the remaining subsidy target must be **withdrawable/real cash vested before any event-dependent or voidable wager branch**, with no anti-arbitrage rescission and with Azerbaijan eligibility.

## Current candidates screened
### BETDAQ DAQBACK
- current page advertises up to £1,000 first-month commission back as **withdrawable funds**;
- validates that exchange commission rebates can be real cash, not just points;
- but cashback is generated from settled commission, so whole-market void produces no qualifying commission/rebate.

Status: **cash-rebate mechanism validated; strict guarantee repair rejected**.

### BETDAQ Healthy Betting cashback
- 10% eligible sportsbook/casino net-loss cashback credited as real money;
- cancelled/void bets are ineligible;
- therefore void branch remains zero.

Status: **REJECTED strict guarantee repair**.

### Betfair Azerbaijan risk-free Exchange offer
- Azerbaijan is explicitly among eligible countries on the current international offer;
- refund applies only when qualifying first bet settles and loses;
- unmatched, unsettled or voided bets do not qualify.

Status: **Azerbaijan-accessible contingent subsidy validated; strict guarantee rejected**.

### Smarkets SailGP predictor — historical stronger mechanism
- 2026 promotion paid £50 cash credit if prediction correct and £25 if wrong;
- no wager was required to make the prediction;
- this proves that a positive cash floor independent of prediction outcome can exist.

But it is not executable now: UK/Ireland only, sign-up deadline 2026-08-02, expiry/eligibility conditions, operator discretion.

Status: **mechanism class validated historically; not current SUCCESS**.

### Current free-prediction screen
- Betfair free prediction prizes remain random/competitive;
- cTrader Store Football Cup rewards are explicitly non-withdrawable/non-cash/discretionary.

Status: **no current universal positive withdrawable-cash floor found**.

# H046 — prior same-venue gate
Same-market exchange dutching with `sum(1/o_i)<1` remains a real ordinary-settlement surebet after matched execution, but current exchange rules allow reachable whole-market void/cancellation states. Without an independent vested subsidy, terminal strict profit floor is 0.

# Strongest non-terminal positive-EV result
## H037 Irish Lotto Plus Million Euro Raffle
Six recovered special-event raffle-winner counts remain materially below modeled break-even participation. Strong +EV overlay remains, but recipient selection is random and external tickets remain, so strict guarantee is rejected.

# Other active / blocked branches
- H020 live two-sided arbitrage: mechanism validated; live raw-book acquisition remains data/runtime constrained and is non-terminal without vested subsidy.
- H019 capped fixed-prize saturation: mechanism valid in principle; sampled instances fail full-cap cash-floor economics.
- H007 high-frequency RNG: data-gated; trustworthy ordered bulk history still missing.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# Audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` remains the permanent master trail. Current connector reads of the large file are truncated, so destructive replacement is unsafe. H047 is recorded in a continuation shard `research/CHECKED_PROJECTS_AND_TESTS_H047_APPEND.md`; future consolidation must preserve all prior history.

# General terminal gates now established
Any SUCCESS must prove all of:
1. contract permission / irrevocability;
2. complete execution/fill;
3. settlement isomorphism for cross-product hedges;
4. strictly positive void/cancellation floor;
5. commissions, taxes, funding/FX, limits and withdrawals included;
6. if relying on promotion/rebate, cash must already be vested or otherwise survive every void/cancellation branch.

# Next priorities
1. **H048 non-wagering contractual bounty/referral/action payments:** search betting/lottery-adjacent programs where all qualifying actions are under the user's control and a positive cash amount becomes owed without a random event, third-party performance or later wager settlement.
2. Search current Azerbaijan-accessible signup/action cash awards where deposit may be reversible principal but reward is cash and requires no wager/turnover.
3. Search regulated affiliate/bounty micro-actions with fixed CPA only where self-qualification is expressly permitted; reject third-party acquisition dependency for terminal guarantee.
4. H020 live arbitrage only as non-terminal profit mechanism unless paired with a true H047/H048 vested subsidy.
5. H037 broaden controls / recalculate after autumn-2026 rule change.
6. H019 only if capped-entry economics materially improve.
7. H006/H007 only after reliable histories/machine metadata become obtainable.
8. H010/H014 if new authoritative data routes appear.
9. Before EXHAUSTED: additional deterministic cash-rebate/action scans, Bayesian hidden-state inference and causal implementation tests.
