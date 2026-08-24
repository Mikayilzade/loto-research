# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Ignore historical non-lottery automation drift.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

## Current checkpoint
Latest completed numbered lottery packet: **H248 — Lotto.com 25% draw-discount full-cover upper-bound closure**.
Latest completed exact-family packet: **H235**.
Current exact-family continuation: **H237**; expected merged outputs remain absent:
- `data/derived/h237_h235_first_survivor_separation.json`
- `data/derived/h237_new_witnesses.json`
Missing output proves nothing.

### Exact-family state
- H232: 306,450 quotient states screened; 306,098 retained a legal shift tuple; 139,869,763 exact legal shift tuples survived.
- H234: exact balanced counterexamples found for 44/44 sampled H232 survivors.
- H235: after adding H234 witnesses and affine symmetries, 303,802 coefficient states and 90,425,060 legal shift tuples still survive. H225 remains open.

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

### H248 — Lotto.com 25% draw-discount full-cover upper bound
Fresh current evidence from Lotto.com Promotional Terms confirms percentage discounts are a real lottery-ticket promotion class, but promotions are one-use, service fees remain, and product/state/time/cap restrictions may apply. A current indexed NY Lotto.com homepage displays a `25% off $30` offer.

H248 intentionally grants this observed 25% discount a much stronger scope than published: **25% off the entire controlled full-space stake, zero service fees, no cap, deterministic eligibility, no cancellation**. Even under that dominating assumption, known finite-space constructions remain below strict break-even:

- Ohio KENO 3-spot: **86.9507%**;
- Nebraska MyDaY best case: **77.9631%**;
- Millionaire for Life optimistic full-cover bound: **70.5168%**;
- Nebraska 2by2: **50.7052%**;
- Lotto America strict non-jackpot floor: **35.8678%**.

General exact gate: for base deterministic return `r`, a percentage discount must satisfy **`d > 1-r`** before fees/caps. Thus 25% cannot rescue these constructions.

Files:
- `research/h248_lotto_com_25pct_discount_full_cover_upper_bound.md`
- `src/loto_research/h248_lotto_com_discount_upper_bound.py`
- `data/derived/h248_lotto_com_discount_upper_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H248_APPEND.md`

## NEXT ACTION
1. Check H237 merged output first.
2. If H237 returns new exact balanced witnesses, deduplicate against H234 and feed only new cuts into the next H225 exact rescreen.
3. Do not repeat H239-H248 without materially new rules/evidence.
4. Next independent lottery packet should prioritize active deterministic **player-selectable** discounts/subsidies exceeding the exact game-specific deficit, or a newly identified controlled finite-space game with strict full-cover return above 75%.
5. Also prioritize current forced-distribution/rolldown mechanics where external subsidy is large enough to cross the H021 hurdle and sharing/execution can be bounded.
6. Continue until lottery-specific SUCCESS or EXHAUSTED.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H248_APPEND.md`.
