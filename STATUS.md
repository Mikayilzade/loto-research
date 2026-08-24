# STATUS

Updated: 2026-08-24
Branch: `research-work`
Scope: **LOTTERY ONLY**. Ignore historical non-lottery automation drift.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

## Current checkpoint
Latest completed numbered lottery packet: **H249 — Jackpocket lottery credits × Maine Pick 3 Single Digit full-cover conversion**.
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
- H248 Lotto.com 25% draw discount: even a dominating full-stake 25% interpretation leaves known finite covers below break-even.

### H249 — Jackpocket credits × Maine Pick 3 Single Digit
Current official Maine Pick 3 rules expose an unusually small controlled partition:
- Single Digit wager: **$0.50**;
- payout: **$2.50**;
- choose one exact digit position;
- covering all `0..9` values for that position costs **$5.00** and guarantees exactly one **$2.50** winner.

Therefore, for deterministic lottery credit `B`, all service/checkout fees `F`, and irreversible promo-acquisition cost `A`, the strict guaranteed net is:

`G = 2.50 - max(0, 5-B) - F - A`.

For `B <= 5`, strict profit requires:

`B > 2.50 + F + A`.

This is the lowest verified promo-subsidy hurdle found so far for a controllable draw-lottery partition in the current courier search. Recent Jackpocket terms prove two important mechanism facts:
- Jackpocket offers Maine Pick 3 at game level;
- winnings from lottery-credit-funded winning tickets can be withdrawn.

Recent/historical Jackpocket $5/$10 draw-credit offers were arithmetically sufficient before fees. However **H249 is NOT SUCCESS** because:
1. no current public Maine-eligible deterministic credit above the threshold was proven on 2026-08-24;
2. current Maine Jackpocket UI support for the **Single Digit** bet type is not proven;
3. exact Maine service fee is unresolved;
4. recent promo contracts retain broad discretionary cancellation/abuse/eligibility gates incompatible with a strict all-branches guarantee.

Files:
- `research/h249_jackpocket_credits_maine_pick3_single_digit.md`
- `src/loto_research/h249_maine_pick3_credit_conversion.py`
- `data/derived/h249_maine_pick3_credit_conversion.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H249_APPEND.md`

## NEXT ACTION
1. Check H237 merged output first.
2. If H237 returns new exact balanced witnesses, deduplicate against H234 and feed only genuinely new cuts into the next H225 exact rescreen.
3. Reopen H249 immediately only on new primary evidence establishing a **current** Maine-eligible credit/discount, actual Jackpocket Single Digit order support, exact fee, and non-discretionary entitlement.
4. Do not repeat H239-H249 without materially new rules/evidence.
5. Next independent lottery packet should systematically search courier-supported/state-supported **partial digit wager menus** (Single Digit / pair / other exact partitions) for an even lower deterministic subsidy hurdle paired with a currently active, player-selectable lottery credit/discount.
6. Also prioritize current forced-distribution/rolldown mechanics where external subsidy crosses the H021 hurdle and sharing/execution can be bounded.
7. Continue until lottery-specific SUCCESS or EXHAUSTED.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H249_APPEND.md`.
