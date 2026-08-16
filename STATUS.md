# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H046 same-clearing-venue + deterministic-cash subsidy gate completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H046 — same-clearing venue + deterministic cash subsidy gate
Files:
- `research/h046_same_venue_and_cash_subsidy_gate.md`
- `data/derived/h046_gate_screen.csv`

## Same-market exchange arbitrage theorem
For a mutually-exclusive/exhaustive market with fully matched back odds `o_i`, equalized dutching yields ordinary-state positive profit when

`q = sum_i(1/o_i) < 1`.

With total stake `S`, equalized gross profit is

`P = S * (1/q - 1)`.

Betfair charges commission on net winnings on a market, so with effective commission `c`, ordinary-state net becomes `(1-c)P` when positive.

Current Betfair Exchange rules explicitly support cross-selection matching and normal back/lay matching. Thus **same-market post-fill surebet is mechanically real** and avoids H045's cross-operator settlement mismatch.

## Decisive strict-guarantee failure
Betfair's current General Terms / Exchange framework also preserves reachable states where a whole market can be voided. In a whole-market void, stakes are returned and net wagering profit collapses to **0**.

Because terminal SUCCESS requires **strictly positive** net profit in every reachable branch, same-market arbitrage is:
- ordinary-settlement/post-fill surebet mechanism: **VALIDATED**;
- strict terminal guaranteed-profit route: **REJECTED**.

This closes the main same-clearing workaround to H045: settlement isomorphism is no longer the blocker; the common rulebook itself contains a zero-profit state.

## Deterministic cash-subsidy screen
Current official Betfair material was screened for cash-like overlays:
- Betfair Points / Discount Rate: reduces future commission; not withdrawable cash and cannot repair a full-void 0-profit branch.
- My Betfair Rewards: conditional on monthly wagering goals / package / region; no Azerbaijan-specific irrevocable cash entitlement established.
- Refer and Earn: current UK/ROI offer genuinely pays £10 cash per qualified referral, but is jurisdiction-restricted, third-party dependent, excludes reduced-liability qualifying bets and retains anti-abuse/guaranteed-profit clawback language.
- Affiliate CPA: real commercial referral income class, but approval + third-party acquisition are separate business activity rather than deterministic own-wager subsidy.

H046 result: **no Azerbaijan-executable irrevocable deterministic cash subsidy found that survives wager void/cancellation and alone leaves strictly positive net profit.**

# H045 — eTopaz contract + settlement gate
Files:
- `research/h045_etopaz_contract_settlement_gate.md`
- `data/derived/h045_contract_settlement_gate.csv`

H045 rejected eTopaz -> Betfair as strict guarantee because:
- eTopaz contract contains income/loss-avoidance and discretionary cancellation/limit language;
- eTopaz and Betfair have materially different void/reschedule windows, so one hedge leg can void while the other stands.

# H041/H042 — matched promotion mechanics
Mechanical theorem remains valid: an already-earned stake-not-returned token can be converted into a positive normal-outcome floor after compatible opposing liquidity is matched. H045/H046 establish two independent terminal gates:
1. cross-operator settlement identity and contract permission;
2. even on one venue, no allowed whole-market-void/cancellation state may reduce profit to zero unless a separate vested subsidy survives it.

# Strongest non-terminal positive-EV result
## H037 Irish Lotto Plus Million Euro Raffle
Six recovered special-event raffle-winner counts remain far below the modeled break-even participation threshold. Gamma-Poisson posterior and event-day upper bounds continue to support a strong +EV overlay, but the extra €1m recipient is random and external tickets remain, so strict guarantee is rejected.

# Other active / blocked branches
- H020 lawful two-sided hedging/arbitrage: post-fill surebet mechanism validated; fee/depth scanner implemented; raw live-book acquisition remains runtime/data blocked; H046 now proves ordinary same-market arbitrage still fails strict terminal guarantee because of whole-market void.
- H019 capped fixed-prize competition saturation: mechanism valid in principle; sampled instances fail cash-floor/full-cap test.
- H007 high-frequency RNG: data-gated; no trustworthy ordered bulk history recovered.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay remains data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# Permanent audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` remains the permanent master trail. Connector reads of the large file are currently truncated, so replacing it from an incomplete payload would risk deleting prior audit history. H046 dedicated note + data + this STATUS are authoritative for this packet until a safe full-file append route is available; do not overwrite the ledger from a truncated fetch.

# General gates now established
Any terminal arbitrage/promotion SUCCESS must prove all of:
1. **contract permission / irrevocability** — no relevant anti-arbitrage, income-seeking, clawback or discretionary subsidy-cancellation branch;
2. **execution completeness** — all required price/depth legs actually filled, not merely quoted;
3. **settlement isomorphism** for cross-product/cross-operator hedges;
4. **strict void/cancellation floor** — every reachable common-void or cancellation state still leaves positive net profit, usually requiring an independently vested cash subsidy that survives the void;
5. all commissions, taxes, funding/FX costs, limits and withdrawal conditions included.

# Next priorities
1. **H047 vested-cash-entitlement screen:** search Azerbaijan-accessible regulated rewards/rebates/referrals where cash becomes legally/contractually vested before any subsequent wager and explicitly survives void/cancellation.
2. Search commission/rebate structures paid as withdrawable cash rather than points/fee discounts, especially exchange/agent programs available to individual Azerbaijan residents.
3. Search non-wagering contractual arbitrage / guaranteed bounty mechanisms adjacent to lotteries/betting where all qualifying acts are under the user's control and no rescission/zero-profit branch remains.
4. H020 live executable arbitrage only as non-terminal EV/profit mechanism unless paired with an H047-style vested subsidy.
5. H037 broaden special-event controls / prepare autumn-2026 rule-change recalculation.
6. H019 only if capped-entry cash-floor economics materially improve.
7. H006/H007 only after reliable histories/machine metadata become obtainable.
8. H010/H014 if new authoritative data routes appear.
9. Before EXHAUSTED: additional current products, deterministic cash-rebate scans, Bayesian hidden-state inference, and causal implementation tests.
