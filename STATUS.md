# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Ignore historical non-lottery automation drift.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

## Current checkpoint
Latest completed numbered lottery packet: **H251 — Irish Lotto 6/45 Lotto Plus full-cover additive closure**.
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

### H251 — Irish Lotto 6/45 Lotto Plus full-cover additive closure
The Irish National Lottery has confirmed that the refreshed Lotto starts **5 September 2026** with 45 balls, unchanged €4 minimum for two Lotto lines and €6 for two lines with Lotto Plus. Thus Lotto Plus remains an incremental **€1 per line** and enters the chosen line in both Plus 1 and Plus 2. Lotto Plus 1 remains €1m; Lotto Plus 2 increases to €1m.

Exact full-space size is `C(45,6)=8,145,060`. Owning every line gives deterministic category counts against any six winning numbers plus one bonus. Applying the current official fixed Plus tables with the announced new €1m Plus 2 top prize, and generously valuing every Match-2+Bonus Daily Million prize at its full €2 face value:

- incremental Plus full-cover cost: **€8,145,060**;
- deterministic Plus 1 gross: **€2,283,240**;
- deterministic Plus 2 gross: **€2,021,240**;
- combined gross: **€4,304,480**;
- deterministic net: **-€3,840,580**;
- return: **52.8477%**.

Therefore the September Plus 2 increase does **not** rescue full coverage. Under the announced/current fixed tables, adding Plus to every combination strictly worsens the guaranteed floor.

Files:
- `research/h251_irish_lotto_45_plus_full_cover.md`
- `src/loto_research/h251_irish_lotto_45_plus_full_cover.py`
- `data/derived/h251_irish_lotto_45_plus_full_cover.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H251_APPEND.md`

## NEXT ACTION
1. Check H225-X2 merged output first; empty/missing output proves nothing. If positive, follow X3 -> X4; if zero, record exact H225 family closure.
2. For the 5 Sep 2026 Irish Lotto refresh, analyze the **main Lotto-only** cap / fifth-cap-draw full-cover economics separately; H251 closes only the Plus add-on.
3. Reopen H249/H250 immediately on a current deterministic >50% effective subsidy crossing the exact formula after all fees/acquisition costs.
4. Search current forced-distribution/rolldown mechanisms where external subsidy crosses the H021 hurdle and sharing/execution can be bounded.
5. Do not repeat H239-H251 without materially new evidence; continue until lottery-specific SUCCESS or EXHAUSTED.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H251_APPEND.md`.
Exact-family ledger: `research/H225_EXACT_STATUS.md`.
