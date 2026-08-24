# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Ignore historical non-lottery automation drift.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

## Current checkpoint
Latest completed numbered lottery packet: **H253 — Georgia scratcher endgame inventory gate**.
Exact-family continuation uses a separate namespace: **H225-X***. See `research/H225_EXACT_STATUS.md`.

### Exact-family state
- H232: 306,450 quotient states screened; 306,098 retained a legal shift tuple; 139,869,763 exact legal shift tuples survived.
- H234: exact balanced counterexamples found for 44/44 sampled H232 survivors.
- H235: after adding H234 witnesses and affine symmetries, 303,802 coefficient states and 90,425,060 legal shift tuples still survive.
- H225-X1: 44/44 actual H235 survivors broken by unrestricted exact separators; 44 unique genuinely new witnesses, 0 inconclusive.
- H225-X2: complete over all 306,450 states; **295,293** coefficient states and **65,921,861** legal shift tuples survive. The former empty legacy publication path has been replaced by an audited manifest; compact summary and 44-chunk survivor seed are authoritative.
- H225-X3: complete; all **44/44 active X2 chunks** produced exact balanced counterexamples, **0 inconclusive**, **44 genuinely new witnesses** after deduplication.
- H225-X4: full incremental exact rescreen has been triggered from `research-work` using the X3 witness packet. **No result is inferred until the merged X4 output exists and is re-read.**

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
- H253 Georgia scratcher #1709 endgame: third-party residual-prize arithmetic can show apparent >100% conditional EV, but **unclaimed prizes are not certified unsold/purchasable prizes**, remaining-ticket counts are estimated, distributed inventory is not deterministically acquirable, and the game is ended. Public remaining-prize tables alone cannot certify guaranteed scratcher arbitrage.

### H253 — Georgia scratcher endgame inventory gate
Georgia Lottery #1709 `$20 Big Georgia Raffle` was used as a hard endgame test because a third-party snapshot implied unusually strong conditional economics:
- estimated remaining tickets: **75,511**;
- estimated residual ticket cost: **$1,510,220**;
- nominal listed remaining prize value: **$3,003,820**;
- naive conditional gross ratio: **198.8995%**;
- naive nominal excess: **$1,493,600** before tax/friction.

The strict guarantee fails because the published prize state is based on **unclaimed** prizes, not a certified mapping of prizes embedded in **unsold purchasable** tickets; the residual ticket denominator is estimated rather than an exact official live inventory; retail inventory cannot be deterministically swept statewide; and the game is already ended. Therefore this is a conditional EV signal only, not executable guaranteed arbitrage.

Files:
- `research/h253_georgia_scratcher_endgame_inventory_gate.md`
- `data/derived/h253_georgia_scratcher_1709_endgame.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H253_APPEND.md`

## NEXT ACTION
1. Read and independently validate `data/derived/h225_x4_incremental_exact_rescreen.json` when it appears. Missing output proves nothing. If zero survivors, close H225; otherwise continue H225-X5 with actual X4 survivors.
2. Recheck H252 only when the final official post-5-Sep 6/45 Irish rules PDF is published or materially new mechanics appear.
3. For scratchers/instant tickets, reopen endgame-buyout only on execution-grade evidence of exact **unsold purchasable inventory** and prize content/bounds, not merely unclaimed-prize tables or estimated ticket counts.
4. Search current forced-distribution/rolldown mechanisms where the subsidy can be captured **without requiring zero jackpot winners while simultaneously forcing full coverage**.
5. Reopen H249/H250 immediately on a current deterministic >50% effective subsidy crossing the exact formula after all fees/acquisition costs.
6. Continue lottery-only until SUCCESS or EXHAUSTED.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H253_APPEND.md`.
Exact-family ledger: `research/H225_EXACT_STATUS.md`.
