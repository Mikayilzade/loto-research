# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Ignore historical non-lottery automation drift.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

## Current checkpoint
Latest completed numbered lottery packet: **H255 — UK Lotto lower-tier boost covering-design impossibility**.
Exact-family continuation uses a separate namespace: **H225-X***. See `research/H225_EXACT_STATUS.md`.

### Exact-family state
- H232: 306,450 quotient states screened; 306,098 retained a legal shift tuple; 139,869,763 exact legal shift tuples survived.
- H234: exact balanced counterexamples found for 44/44 sampled H232 survivors.
- H235: after adding H234 witnesses and affine symmetries, 303,802 coefficient states and 90,425,060 legal shift tuples still survive.
- H225-X1: 44/44 actual H235 survivors broken by unrestricted exact separators; 44 unique genuinely new witnesses, 0 inconclusive.
- H225-X2: complete over all 306,450 states; **295,293** coefficient states and **65,921,861** legal shift tuples survive. The former empty legacy publication path has been replaced by an audited manifest; compact summary and 44-chunk survivor seed are authoritative.
- H225-X3: complete; all **44/44 active X2 chunks** produced exact balanced counterexamples, **0 inconclusive**, **44 genuinely new witnesses** after deduplication.
- H225-X4: full incremental exact rescreen has been triggered from `research-work`; the current merged path is still empty, so **no result is inferred yet**.

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
- H254 Irish guaranteed raffles: finite Christmas Millionaire Raffle full inventory returns only **42.2833%**; EuroMillions Ireland Only Raffle and Lotto Plus €1m overlays are genuine external subsidies but market-wide eligible raffle entries cannot be deterministically monopolized at bounded cost.
- H255 UK Lotto lower-tier fixed boost: even a historical Match-3=£100 boost plus ordinary fixed higher tiers yields only **£1.24933324 average fixed cash per £2 line = 62.4667%**, so arbitrary additive covering portfolios cannot be strictly profitable on every draw by the averaging/linearity theorem.

### H255 — UK Lotto lower-tier boost covering-design impossibility
A lower-tier boost is structurally attractive because it does not require a zero-jackpot-winner branch. The historical UK Lotto special-event structure with **Match 3 = £100** was therefore tested as a generic partial-covering candidate rather than by enumerating individual wheels.

For any fixed 6-number ticket over all `C(59,6)=45,057,474` possible main-number draws, exact Match-3 probability is **0.010398274878880249**. Thus a £100 Match-3 award contributes only **£1.0398274879** average cash per £2 line. Adding Match 4 £140, Match 5 £1,750 and Match 5+Bonus £1m fixed cash in the player's favor raises total average fixed cash only to **£1.2493332405 = 62.4667% of stake**.

Therefore no multiset, wheel, partial covering design, or unequal multiplicity portfolio composed solely of these additive ticket payoffs can guarantee positive cash profit on every possible draw: an everywhere-positive portfolio would necessarily have average payout greater than cost, contradicting the exact average below cost.

Files:
- `research/h255_uk_lotto_match3_boost_impossibility.md`
- `src/loto_research/h255_uk_lotto_match3_boost_impossibility.py`
- `data/derived/h255_uk_lotto_match3_boost_impossibility.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H255_APPEND.md`

## NEXT ACTION
1. Read and independently validate `data/derived/h225_x4_incremental_exact_rescreen.json` when it becomes non-empty. Missing/empty output proves nothing. If zero survivors, close H225; otherwise continue H225-X5 with actual X4 survivors.
2. Search current forced-distribution/rolldown mechanics where externally accumulated money is paid into lower tiers **and the trigger does not conflict with owning a covering portfolio**; H255 closes fixed additive boosts without such nonlinear money.
3. Search finite lottery identifiers/ticket pools where all eligible identifiers are actually player-selectable/reservable and total guaranteed cash exceeds complete acquisition cost.
4. Recheck H252 only when the final official post-5-Sep 6/45 Irish rules PDF is published or materially new mechanics appear.
5. For scratchers/instant tickets, reopen endgame-buyout only on execution-grade evidence of exact **unsold purchasable inventory** and prize content/bounds, not merely unclaimed-prize tables or estimated ticket counts.
6. Reopen H249/H250 immediately on a current deterministic >50% effective subsidy crossing the exact formula after all fees/acquisition costs.
7. Continue lottery-only until SUCCESS or EXHAUSTED.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H255_APPEND.md`.
Exact-family ledger: `research/H225_EXACT_STATUS.md`.
