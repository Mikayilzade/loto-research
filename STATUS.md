# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Ignore historical non-lottery automation drift.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

## Current checkpoint
Latest completed numbered lottery packet: **H258 — EuroMillions €250m cap flow-down one-external-duplicate closure**.
Exact-family continuation uses a separate namespace: **H225-X***. See `research/H225_EXACT_STATUS.md`.

### Exact-family state
- H232: 306,450 quotient states screened; 306,098 retained a legal shift tuple; 139,869,763 exact legal shift tuples survived.
- H234: exact balanced counterexamples found for 44/44 sampled H232 survivors.
- H235: after adding H234 witnesses and affine symmetries, 303,802 coefficient states and 90,425,060 legal shift tuples still survive.
- H225-X1: 44/44 actual H235 survivors broken by unrestricted exact separators; 44 unique genuinely new witnesses, 0 inconclusive.
- H225-X2: complete over all 306,450 states; **295,293** coefficient states and **65,921,861** legal shift tuples survive.
- H225-X3: complete; all **44/44 active X2 chunks** produced exact balanced counterexamples, **0 inconclusive**, **44 genuinely new witnesses** after deduplication.
- H225-X4: full incremental exact rescreen has been triggered from `research-work`; at the start of H258 `data/derived/h225_x4_incremental_exact_rescreen.json` was still empty, so **no X4 result is inferred**.

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
- H257 LOTTO MAX 2026: complete coverage would hit every MAXPLUS/MAXMILLIONS exact-match series, but those prizes and the Main Jackpot are shared among all duplicate winning selections; no useful hard pre-draw external-duplicate cap exists.
- H258 EuroMillions cap flow-down: ordinary cap overflow **is compatible with full coverage even when rank 1 wins**, but one legal external 5+2 duplicate destroys the strict guarantee even under a dominating all-current-prize-money upper bound.

### H257 — LOTTO MAX 2026 overlay full-cover screen
Current Game Conditions effective April 10, 2026 use 4 selections of 7 numbers from 1–52 per C$6 play. Under an intentionally player-favorable assumption that every one of the four slots can be packed perfectly, complete 7/52 coverage needs `C(52,7)=133,784,560` selections, at an idealized minimum cost of **C$200,676,840**.

Against every Main Draw, one-copy full coverage deterministically creates:
- **463,540** fixed C$20 Match-4 winners;
- **463,540** fixed C$20 Match-3+Bonus winners;
- total strict immediate cash floor **C$18,541,600 = 9.2395%** of idealized cost.

The Main Jackpot, upper main tiers, every MAXPLUS prize and every MAXMILLIONS prize are divided by the number of matching winning selections. Although full coverage guarantees that our portfolio contains each drawn seven-number overlay series, published rules give no useful hard pre-draw cap on external duplicate matching selections. Therefore those shared headline prizes cannot be assigned a positive worst-case contribution to a strict guarantee.

Files:
- `research/h257_lotto_max_overlay_full_cover.md`
- `src/loto_research/h257_lotto_max_overlay_full_cover.py`
- `data/derived/h257_lotto_max_overlay_full_cover.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H257_APPEND.md`

### H258 — EuroMillions cap flow-down one-external-duplicate bound
Official current Belgian EuroMillions material confirms an important distinction from H002b: once the €250m jackpot cap is reached, money that would exceed the cap flows to rank 2 (or the first lower winning rank) **even if rank 1 itself has a winner**. Thus complete coverage does not conflict with ordinary cap flow-down; it conflicts only with the separate terminal no-jackpot-winner roll-down.

H258 then tests the strict guarantee under the legal branch containing exactly one external 5+2 duplicate. Full 5/50+2/12 coverage costs **€349,595,400**. The duplicate limits our jackpot share to **€125m**. To create a decisive player-favorable upper bound, H258 gives our portfolio every euro of the official 50% current-draw prize allocation from our full-cover purchase plus that external €2.50 line: **€174,797,701.25**.

Even this impossible grant yields only:
- gross upper bound **€299,797,701.25**;
- net upper bound **-€49,797,698.75**;
- return upper bound **85.7556%**.

Equivalently, after granting all current-draw prize money, a two-way shared jackpot would need to exceed **€349,595,397.50** to break even; the actual cap is only €250m.

Therefore ordinary EuroMillions cap flow-down remains an economically interesting nonlinear EV mechanism but is **REJECTED as a strict full-cover guarantee**. One external jackpot duplicate is already decisive before taxes, execution constraints or lower-tier sharing.

Files:
- `research/h258_euromillions_cap_flowdown_external_duplicate_bound.md`
- `src/loto_research/h258_euromillions_cap_flowdown_bound.py`
- `data/derived/h258_euromillions_cap_flowdown_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H258_APPEND.md`

## NEXT ACTION
1. Read and independently validate `data/derived/h225_x4_incremental_exact_rescreen.json` when it becomes non-empty. Missing/empty output proves nothing. If zero survivors, close H225; otherwise continue H225-X5 with actual X4 survivors.
2. Search current forced-distribution/rolldown mechanics where externally accumulated money is paid as **fixed per-winning-selection** lower-tier prizes rather than shareable pools.
3. Search finite lottery identifiers/ticket pools where all eligible identifiers are actually player-selectable/reservable and total guaranteed cash exceeds complete acquisition cost.
4. Prioritize deterministic current payout boosts above exact coverage hurdles; H256 closes NJ Quick Draw at +50%, H257 closes shared LOTTO MAX overlays without an external-duplicate cap, and H258 closes EuroMillions cap flow-down against just one external 5+2 duplicate.
5. Recheck H252 only when final official post-5-Sep Irish 6/45 rules are published or mechanics materially change.
6. For scratchers/instant tickets, reopen endgame-buyout only on execution-grade evidence of exact unsold purchasable inventory and prize content/bounds.
7. Reopen H249/H250 immediately on a current deterministic >50% effective subsidy crossing the exact formula after all fees/acquisition costs.
8. Continue lottery-only until SUCCESS or EXHAUSTED.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H258_APPEND.md`.
Exact-family ledger: `research/H225_EXACT_STATUS.md`.
