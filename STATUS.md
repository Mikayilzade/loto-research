# STATUS

Updated: 2026-08-17
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H060 regulated cross-border payment/funding cash-credit screen completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H060 — regulated cross-border payment / funding cash credits
Files:
- `research/h060_crossborder_payment_cash_credits.md`
- `data/derived/h060_payment_credit_screen.csv`
- `src/loto_research/payment_credit_gate.py`
- `tests/test_payment_credit_gate.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H060_APPEND.md`

## Current result
The mechanism class is real: regulated money-transfer providers currently offer fixed transfer credits, fee waivers, referral cash/credits, and promotional top-ups. No current public candidate passes the strict guaranteed-cash gate for the target execution context.

### Strongest live lead — Paysend Back to School 2026
Official terms run **14 Aug–30 Sep 2026**. New customers in supported sending countries outside UK/EEA/Canada can enter `SEPT5` on each of their first two eligible international transfers of at least USD 100 and receive:
- no Paysend transfer fee; and
- USD 5-equivalent Paysend bonus on each transfer, max USD 10.

But terminal guarantee fails because:
- reward cannot be exchanged for cash;
- same-currency transfers are excluded;
- Paysend FX may include a margin and third-party fees may apply;
- failed/reversed/refunded/compliance-blocked transfers do not qualify;
- Azerbaijan is currently documented as a **receiving** country, not one of Paysend's sending countries.

### Other H060 controls
- Paysend Global Summer: USD 6.50 per USD 200 transfer up to USD 26, but residence excludes Azerbaijan, reward non-cash, global USD 500k prize pool can exhaust.
- Paysend standard referral: genuine withdrawable bonus exists, but published eligible-country list excludes Azerbaijan and reward depends on independent referred-user activity.
- Wise: invite reward/fee discount is referral-dependent; Azerbaijan can use Wise generally but is absent from current balance-holding residence list.
- Remitly: current Azerbaijan routes provide fee/FX discounts, not a fixed withdrawable positive cash reward.
- Western Union 2026 referral: rewards explicitly have no monetary value and cannot be redeemed for cash; third-party/referral dependency and modification rights remain.
- MoneyGram US Invite Friends: USD 25 reward is a discount toward a later transfer, US-only in the checked program and referral-dependent.
- Skrill: public transfer promo-code batch found expired 5 Aug 2026; other current cash reward campaigns are invitation-only/discretionary.

## H060 necessary-condition gate
For committed transfer principal `P`:

`guaranteed_net_floor = R_min + B_min - P - C_max`

where:
- `R_min` = guaranteed cash principal recovery after all legal branches;
- `B_min` = guaranteed **withdrawable cash** reward surviving all legal branches;
- `C_max` = hard-bounded worst-case fees, FX loss, external fees, tax and withdrawal costs.

Strict SUCCESS requires this floor to be `> 0` before commitment. Non-cash, discretionary, first-N/pool-exhaustible, referral-dependent or cancellation-zero rewards contribute `B_min=0` to the terminal proof.

H060 status: **MECHANISM REAL; CURRENT PUBLIC SCREEN CLOSED; NO TERMINAL GUARANTEE**.

# H059 — marketplace / creator / freelancer bonuses
H059 remains closed at current public-screen level:
- AZDO Guaranteed Deal: 3% Umico bonus, not cash-withdrawable.
- Fiverr Freelancer Reward: real fixed cash, but enrollment closed and U.S.-only.
- YouTube Affiliate Partnerships Boost Bonus: invitation/brand-selection dependent and U.S./South Korea only.
- Fiverr referral / Adobe Stock / Upwork controls: non-cash or no applicable reward.

# H052 — upfront insured interest remains strongest unresolved local contract lead
File:
- `research/h052_upfront_insured_interest.md`

Expressbank and VTB Azerbaijan remain the strongest unresolved local principal-preserving lead. Strict success is still blocked on product-specific contract language proving prepaid interest does not become a matured depositor obligation/offset against insured principal on an insurance event or forced maturity. Do not repeat blind searches without a genuinely new route.

# Other important branches
- H058 business-volume/payment-rail rebates: current public screen closed.
- H057 fixed-cash geography-compatible rewards: current public screen closed.
- H056 IBKR USD 200 referrer cash: conditional mechanism; third-party dependency/amendment/anti-abuse discretion prevent strict guarantee.
- H053 deterministic retail cashback: qualifying spend consumes principal.
- H054 principal-preserving funding bonuses: market/vesting risk remains.
- H051 ordinary insured deposits: immediate-event gate rejects strict reward floor.
- H049/H050 principal-protected yield: no current fixed retail reward proven.
- H037 Irish Lotto Plus Million Euro Raffle: strong +EV overlay, strict guarantee rejected.
- H020 two-sided arbitrage: mechanism validated; no current fully vested live terminal setup.
- H019 capped fixed-prize saturation: valid in principle; sampled instances fail economics.
- H007 high-frequency RNG: data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# General terminal gates
Any SUCCESS must prove all of:
1. contract permission / irrevocability;
2. complete execution/fill;
3. settlement compatibility where relevant;
4. strictly positive cancellation/void floor;
5. commissions, taxes, funding/FX, limits and withdrawals included;
6. promotion/rebate entitlement survives every allowed branch;
7. principal redemption/make-whole and positive reward simultaneously fixed before capital commitment;
8. dynamic APR or vague `up to` yield is insufficient;
9. ordinary post-opening accrued interest is insufficient if an immediate insurance event can reduce reward to ~0;
10. prepaid-interest deposit reward must remain separately vested and not reduce/offset insured principal under insolvency/forced liquidation;
11. retail cashback consumption/resale value is not a cash guarantee;
12. funding bonus must have a fixed positive cash floor after vesting/clawback/market-risk branches;
13. foreign fixed-cash reward needs explicit lawful executable eligibility;
14. referral rewards cannot rely on control of an independent referred account and must survive amendment/anti-abuse branches;
15. business-volume rebates count only when underlying payment/receipt is independently economically owed;
16. first-N quotas, invitation-only status, private targets or sole-discretion eligibility prevent strict pre-commitment guarantee unless entitlement is irrevocably locked;
17. creator/marketplace bonuses must be withdrawable cash and not require uncontrolled selection;
18. cross-border payment promotions require hard-bounded principal recovery/FX/external costs and a withdrawable cash reward; non-cash transfer credits are insufficient.

# Permanent audit ledger
`research/CHECKED_PROJECTS_AND_TESTS.md` remains the master ledger. Because the connector still lacks safe append/patch semantics for the large file, the H059 and H060 rows are preserved in:
- `research/CHECKED_PROJECTS_AND_TESTS_H059_APPEND.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H060_APPEND.md`

These are authoritative append packets until merged through a safe patch route.

# Next priorities
1. **H061 same-currency/no-FX account-opening or funding cash rewards** — search regulated bank/e-wallet programs where principal remains in the user's own account and a fixed cash reward vests after deterministic self-controlled funding/direct-deposit/account-opening actions.
2. Prioritize public Azerbaijan-eligible or globally eligible programs with fixed cash, no referral dependency and hard-bounded withdrawal conditions.
3. Search same-currency transfer-fee rebates that are cash-withdrawable and do not require consumption or third-party activity.
4. Recover H052 product-specific agreements only through a genuinely new route.
5. H020 live executable arbitrage where raw books/settlement can be fetched.
6. H019 only when guaranteed cash floor exceeds full effective capped-entry acquisition cost.
7. H006/H007 after reliable histories/machine metadata become available.
8. H010/H014 when new authoritative data routes appear.
9. Before EXHAUSTED: Bayesian hidden-state inference, additional current products, deterministic cash-rebate scans, and causal implementation tests.
