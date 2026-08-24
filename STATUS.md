# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Ignore historical non-lottery automation drift.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

## Current checkpoint
Latest completed numbered lottery packet: **H252 — Irish Lotto 6/45 cap full-cover sharing gate**.
Exact-family continuation now uses a separate namespace: **H225-X***. See `research/H225_EXACT_STATUS.md`.

### Exact-family state
- H232: 306,450 quotient states screened; 306,098 retained a legal shift tuple; 139,869,763 exact legal shift tuples survived.
- H234: exact balanced counterexamples found for 44/44 sampled H232 survivors.
- H235: after adding H234 witnesses and affine symmetries, 303,802 coefficient states and 90,425,060 legal shift tuples still survive.
- H225-X1: 44/44 actual H235 survivors broken by unrestricted exact separators; 44 unique genuinely new witnesses, 0 inconclusive.
- H225-X2: target merged file exists only as an empty placeholder at this checkpoint; therefore no result is inferred. Full 44-way / 306,450-state incremental rescreen remains pending.
- H225-X3 and X4 remain armed by explicit `workflow_dispatch` chaining.

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

### H252 — Irish Lotto 6/45 cap full-cover sharing gate
The new Irish Lotto begins 5 September 2026 with 45 balls and unchanged €2-per-line economics. A current August 2026 launch comparison reports the new jackpot cap at **€16m** and Match-3 / Match-2+Bonus at fixed **€4** each; recheck these two launch values against the final official 6/45 rules PDF when it appears.

Exact full-space size is `C(45,6)=8,145,060`, so full cover costs **€16,290,120**. Against every draw, full cover has 168,720 Match-3 lines and 126,540 Match-2+Bonus lines. At the reported €4 fixed awards these create a deterministic lower-tier floor of **€1,181,040**.

At a €16m cap:
- with zero external jackpot-winning lines, jackpot + fixed floor gives **+€890,920** before middle-tier pari-mutuel receipts and execution costs;
- with one external jackpot-winning line, the conservative floor becomes **−€7,109,080**;
- therefore one external Match-6 line destroys the strict guarantee.

Additionally, full coverage necessarily owns the realized Match-6 combination, so the **zero-jackpot-winner fifth-cap rolldown branch cannot occur** under successful full coverage. This is the same incompatibility class previously identified for capped multi-draw lotteries.

Files:
- `research/h252_irish_lotto_45_cap_full_cover_sharing_gate.md`
- `src/loto_research/h252_irish_lotto_45_cap_sharing.py`
- `data/derived/h252_irish_lotto_45_cap_sharing.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H252_APPEND.md`

## NEXT ACTION
1. Check H225-X2 merged output first; empty/missing output proves nothing. If positive, follow X3 -> X4; if zero, record exact H225 family closure.
2. Recheck H252 when the final official post-5-Sep 6/45 rules PDF is published; do not otherwise repeat the full-cover cap test.
3. Search current forced-distribution/rolldown mechanisms where the subsidy can be captured **without requiring zero jackpot winners while simultaneously forcing full coverage**.
4. Reopen H249/H250 immediately on a current deterministic >50% effective subsidy crossing the exact formula after all fees/acquisition costs.
5. Continue lottery-only until SUCCESS or EXHAUSTED.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H252_APPEND.md`.
Exact-family ledger: `research/H225_EXACT_STATUS.md`.
