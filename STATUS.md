# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Ignore historical non-lottery automation drift.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

## Current checkpoint
Latest completed numbered lottery packet: **H256 — New Jersey Quick Draw Progressive 50% Bonus Hours full-cover closure**.
Exact-family continuation uses a separate namespace: **H225-X***. See `research/H225_EXACT_STATUS.md`.

### Exact-family state
- H232: 306,450 quotient states screened; 306,098 retained a legal shift tuple; 139,869,763 exact legal shift tuples survived.
- H234: exact balanced counterexamples found for 44/44 sampled H232 survivors.
- H235: after adding H234 witnesses and affine symmetries, 303,802 coefficient states and 90,425,060 legal shift tuples still survive.
- H225-X1: 44/44 actual H235 survivors broken by unrestricted exact separators; 44 unique genuinely new witnesses, 0 inconclusive.
- H225-X2: complete over all 306,450 states; **295,293** coefficient states and **65,921,861** legal shift tuples survive.
- H225-X3: complete; all **44/44 active X2 chunks** produced exact balanced counterexamples, **0 inconclusive**, **44 genuinely new witnesses** after deduplication.
- H225-X4: full incremental exact rescreen has been triggered from `research-work`; at the start of H256 `data/derived/h225_x4_incremental_exact_rescreen.json` was still empty, so **no X4 result is inferred**.

### Recent lottery closures / blockers
- H236 RI Lucky 3 Spot: universal free 2X clears arithmetic threshold, but universal entitlement/execution not established.
- H238 RI Kick Back: exact current entitlement remains data-blocked.
- H239 Georgia/NC Keno Bonus Hours: rejected by exact full-coverage arithmetic.
- H240-H241 Missouri Club Keno Bonus Hours including Bulls-Eye variants: rejected by stronger-than-real +50% upper bounds.
- H242 Michigan Tripler Time: multiplier status is random, not deterministically allocable.
- H243 Illinois plus FIREBALL: exhaustive Straight-cover upper bounds remain below break-even.
- H244 WinTrillions Powerball discount: terms permit removal of the promotional enhancement in guaranteed-profit constructions.
- H245 UK Lotto current full-space: fixed-prize return too low and full coverage prevents the relevant rolldown branch.
- H246 LOTTO 6/49 Aug. 29 SuperDraw: even a deliberately favorable isolated-pool model returns only 46.5456% of full-cover spend.
- H247 free Quick Pick / BOGO: uncontrolled free selections have zero guaranteed marginal coverage and zero strict cash floor.
- H248 Lotto.com 25% draw discount: below break-even for known finite covers.
- H249 Jackpocket credit × Maine Pick 3 Single Digit: $5 retail-style exact cover guarantees $2.50 gross; current qualifying deterministic credit/fee/entitlement evidence incomplete.
- H250 courier-supported partial-digit exact subsidy floor: exact-position 50% cover verified, but no current deterministic subsidy above the hurdle plus fees.
- H251 Irish Lotto 6/45 Lotto Plus: full-cover incremental Plus return only 52.8477%.
- H252 Irish Lotto 6/45 cap full-cover: sole-jackpot-winner floor can be positive, but one external Match-6 line destroys the strict guarantee; full coverage also prevents the zero-winner cap rolldown branch.
- H253 Georgia scratcher #1709 endgame: apparent >100% residual-prize EV is not executable because unclaimed prizes are not certified unsold/purchasable inventory and live exact inventory cannot be swept deterministically.
- H254 Irish guaranteed raffles: finite Christmas Millionaire Raffle full inventory returns only **42.2833%**; market-wide raffle identifiers cannot be deterministically monopolized at bounded cost.
- H255 UK Lotto lower-tier fixed boost: historical Match-3=£100 plus ordinary fixed higher tiers averages only **62.4667%** of stake; additive covering portfolios cannot yield an everywhere-positive profit.
- H256 NJ Quick Draw Progressive Bonus Hours: current guaranteed +50% fixed-prize uplift remains below break-even for every exact base/BULLSEYE/Double-BULLSEYE full cover; Multiplier has a legal 1X branch and jackpot numbers are uncontrolled.

### H256 — NJ Quick Draw Progressive 50% Bonus Hours
Current official 2026 rules schedule Bonus Hours on selected Thursdays through 2026-12-31, including **2026-08-27, 5–7 p.m.** A qualifying single Quick Draw Progressive ticket with wager at least $10 receives a **50% bonus if it is a winner**, excluding the Progressive Jackpot; BULLSEYE, Double BULLSEYE and Multiplier tickets may qualify.

H256 used exact 20-of-80 combinatorial identities and the current published prize tables for every spot category 1–10:
- best base full-cover promo return: **90.4791%** (5-spot);
- best BULLSEYE full-cover promo return: **82.2389%** (2-spot);
- best Double BULLSEYE full-cover promo return: **84.4937%** (2-spot);
- exact best-base break-even uplift: **>65.7841%**, so the current +50% is insufficient before taxes/execution;
- 9/10 spot $3m liability/pari-mutuel rules can only lower the nominal upper bound.

Multiplier is drawn once per Quick Draw drawing; **1X is a legal 40% branch** while the add-on doubles base wager cost. In that branch the best fixed-prize Bonus Hours return is only **45.2396%** of total Multiplier stake. Progressive Jackpot contribution to the strict floor is **$0** because each ticket's nine jackpot numbers are system-random and the 50% bonus explicitly excludes jackpot wins.

Therefore the current NJ Bonus Hours controlled full-cover class is **REJECTED** without needing to rely on promotion cancellation/discretion clauses.

Files:
- `research/h256_nj_quick_draw_bonus_hours_full_cover.md`
- `src/loto_research/h256_nj_quick_draw_bonus_hours.py`
- `data/derived/h256_nj_quick_draw_bonus_hours.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H256_APPEND.md`

## NEXT ACTION
1. Read and independently validate `data/derived/h225_x4_incremental_exact_rescreen.json` when it becomes non-empty. Missing/empty output proves nothing. If zero survivors, close H225; otherwise continue H225-X5 with actual X4 survivors.
2. Search current forced-distribution/rolldown mechanics where externally accumulated money is paid into lower tiers and the trigger remains compatible with a controlled covering portfolio.
3. Search finite lottery identifiers/ticket pools where all eligible identifiers are actually player-selectable/reservable and total guaranteed cash exceeds complete acquisition cost.
4. Prioritize deterministic current payout boosts **above the exact underlying coverage hurdle**; H256 closes NJ Quick Draw at +50%, with best base requiring >65.7841% before friction.
5. Recheck H252 only when final official post-5-Sep Irish 6/45 rules are published or mechanics materially change.
6. For scratchers/instant tickets, reopen endgame-buyout only on execution-grade evidence of exact unsold purchasable inventory and prize content/bounds.
7. Reopen H249/H250 immediately on a current deterministic >50% effective subsidy crossing the exact formula after all fees/acquisition costs.
8. Continue lottery-only until SUCCESS or EXHAUSTED.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H256_APPEND.md`.
Exact-family ledger: `research/H225_EXACT_STATUS.md`.
