# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Ignore historical non-lottery automation drift.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

## Current checkpoint
Latest completed numbered lottery packet: **H250 — courier-supported partial-digit exact subsidy floor**.
Exact-family continuation now uses a separate namespace: **H225-X***. See `research/H225_EXACT_STATUS.md`.

### Exact-family state
- H232: 306,450 quotient states screened; 306,098 retained a legal shift tuple; 139,869,763 exact legal shift tuples survived.
- H234: exact balanced counterexamples found for 44/44 sampled H232 survivors.
- H235: after adding H234 witnesses and affine symmetries, 303,802 coefficient states and 90,425,060 legal shift tuples still survive.
- H225-X1: 44/44 actual H235 survivors broken by unrestricted exact separators; 44 unique genuinely new witnesses, 0 inconclusive.
- H225-X2: full 44-way / 306,450-state incremental rescreen explicitly retriggered after diagnosing GitHub Actions token recursion suppression. Missing merged output remains pending only.
- H225-X3 and X4 are armed by explicit `workflow_dispatch` chaining rather than push-recursion.

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

### H250 — courier-supported partial digit exact subsidy floor
H250 directly verifies that the small exact-position digit partition is not only a state-rule abstraction: Lotto.com Maine publicly exposes **First Digit / Second Digit / Third Digit** wagers, 1:10 odds and a $5 payout on its $1 minimum wager. Its public Pick 3 page also permits up to 100 lines/game, so both the 10-line Single Digit cover and 100-line Pair cover are operationally representable on the public courier menu.

Current state evidence confirms the same basic partition in Maine, Vermont and Minnesota. Exact deterministic return for the tested Single Digit / Pair / Straight partitions is **50% before subsidy**.

Key thresholds:
- retail/Jackpocket-like $0.50 Single Digit cover: cost **$5**, gross **$2.50**; for credit `B<=5`, strict profit requires `B > 2.50 + F + A`;
- Lotto.com $1 Single Digit cover: cost **$10**, gross **$5**; for credit `B<=10`, strict profit requires `B > 5 + F + A`;
- percentage discount must be **strictly greater than 50% before fees**. A 25% discount gives -$2.50 before fees; current Lotto.com Mystery Scratch's listed 20% draw discount gives -$3 before fees and the Mystery Scratch reward itself is random.

Recovered Jackpocket $5/$10 lottery-credit offers prove that sufficiently large subsidies have existed and that winnings from credit-funded winning tickets can be withdrawn, but the strong public offers recovered are historical/expired or offer-dependent/discretionary. No current August 2026 deterministic, non-discretionary subsidy above the exact 50% hurdle plus fees/acquisition costs was established.

Result: **NOT SUCCESS / CURRENT SUBSIDY BLOCKED**.

Files:
- `research/h250_partial_digit_courier_subsidy_floor.md`
- `src/loto_research/h250_partial_digit_courier_subsidy_floor.py`
- `data/derived/h250_partial_digit_courier_subsidy_floor.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H250_APPEND.md`

## NEXT ACTION
1. Check H225-X2 merged output first; if positive, follow the explicit X3 -> X4 separator/rescreen chain; if zero, record exact H225 family closure.
2. Reopen H249/H250 immediately on a **current deterministic >50% effective subsidy** (or fixed credit crossing the exact formula after all fees/acquisition costs) in a state/courier with a proven exact-position wager menu.
3. Search current forced-distribution/rolldown mechanisms where external subsidy crosses the H021 hurdle and sharing/execution can be bounded.
4. Search other deterministic lottery entitlements/credits with lower acquisition cost or no discretionary award branch; do not repeat H239-H250 without materially new evidence.
5. Continue until lottery-specific SUCCESS or EXHAUSTED.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H250_APPEND.md`.
Exact-family ledger: `research/H225_EXACT_STATUS.md`.
