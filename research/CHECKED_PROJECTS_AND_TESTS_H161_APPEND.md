# CHECKED PROJECTS AND TESTS — H161 APPEND

Updated: 2026-08-21
Scope: LOTTERY ONLY
Terminal state after packet: **NO SUCCESS; NOT EXHAUSTED**

| ID | Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|---|
| H161 | New Jersey Pick-3 Green Ball cumulative trigger | Six white balls + one green; white balls removed nightly; test state after all six whites removed | next promo draw is forced Green Ball; same Pick-3 wager receives second full-prize draw | **VALIDATED deterministic trigger state**; official 2026 rules; `research/h161_nj_green_ball_forced_state_retailer_commission.md` |
| H161 | NJ Pick-3 Pair cover on forced Green Ball state | Cover all 100 ordered Pair outcomes at $0.50 | cost $50; each draw guarantees $25 Pair winner; forced two draws guarantee $50 = **100% gross** | **VALIDATED break-even cover**; `data/derived/h161_nj_green_ball_pair_cover.csv` |
| H161 | Public state observability | Verify whether player can know remaining white-ball count before purchase | official 2025 NJ release says homepage reports number of white balls remaining | **VALIDATED recurring monitor architecture** |
| H161 | Retailer commission overlay | Apply published 5% sales + 1.25% payout commission to forced-green Pair cover | if commissions apply to retailer's own purchase: $50 prize + $2.50 sales commission + $0.625 payout commission - $50 face = **+$3.125 pre-tax** | **PROMISING / entitlement not locked** |
| H161 | Retailer self-purchase legality screen | Search whether NJ retailer owner can purchase own tickets | official NJ Lottery 2023 release documents licensed retailer owner Jay Shortway buying a CASH4LIFE ticket for himself at his own lottery location and being paid as winner | **SELF-PURCHASE DEMONSTRATED**, but commission-on-self-sale not expressly confirmed |
| H161 | Coupon/promotion stacking | Check 2026 Green Ball rules | rules expressly say Green Ball is not valid with another NJ Lottery promotion or coupon | **CLOSED coupon-stacking route** |
| H161 | Whole-basket/liability gate | Review official Pick-3 rules | Lottery can stop further wagers when liability for a number exceeds internal limit; limit can change at Director discretion | **STRICT ACCEPTANCE GATE OPEN** |
| H161 | Promotion irrevocability | Review official Green Ball rules | Lottery may cancel/terminate/modify/suspend promotion without prior notice, including payout-budget reason | **TERMINAL GUARANTEE BLOCKER unless ticket issuance fixes rights** |
| H161 | Current execution | Check current date vs latest promo | Jul 6-Aug 2 2026 cycle has ended; Aug 18 release confirms eight Green Ball triggers and $2.55m extra prizes | **NOT CURRENTLY EXECUTABLE / recurring monitor** |

## New non-duplicate conclusion
H160's forced-second-draw theorem generalizes to New Jersey and becomes operationally easier: the NJ Pair cover requires only **100 wagers / $50 face** rather than 1,000 Straights / $500. More importantly, NJ publishes a **5% ticket-sales commission + 1.25% small-prize payout commission** and has officially documented a retailer owner purchasing a winning ticket for himself at his own licensed location. This produces a conditional **+$3.125 pre-tax deterministic overlay** if self-purchase commissions are contractually earned.

Terminal SUCCESS is not recorded because self-sale commission entitlement, post-purchase promotion irrevocability, full-basket acceptance and after-tax positivity are not yet proven, and the latest promotion is over.

## Next test
Prioritize official retailer contract/manual evidence on self-purchase commission entitlement and whether an issued eligible ticket retains Green Ball rights if the promotion is later modified/cancelled. In parallel search other cumulative-trigger Pick-3 promotions with expressly protected retailer commissions or player discounts.
