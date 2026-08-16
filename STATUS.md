# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H036 Irish Plus + active targeted bonus screen completed**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H036 — Irish Plus coverage + current OLG targeted subsidy screen
Files:
- `research/h036_irish_plus_and_olg_targeted_bonus.md`
- `data/derived/h036_irish_plus_and_olg_promo_screen.csv`
- `src/loto_research/irish_plus_and_promo.py`
- `tests/test_irish_plus_and_promo.py`

## Daily Million Plus — CLOSED
Complete `C(39,6)=3,262,623` coverage at EUR1/line costs EUR3,262,623.
Exact full-space counts against any 6-main+bonus draw reproduce:
- 6: 1
- 5+bonus: 6
- 5: 192
- 4+bonus: 480
- 4: 7,440
- 3+bonus: 9,920
- 3: 99,200.

Even granting our winner the entire EUR500,000 top prize and valuing each EUR2 Scratch Card at full EUR2 face value, gross is only **EUR961,600 = 29.4732%**. Removing the shareable top prize from the strict guaranteed cash floor leaves **EUR461,600 = 14.1481%**.

Status: **REJECTED guaranteed-profit full coverage**.

## EuroMillions Plus — CLOSED
Full 5/50 space = `C(50,5)=2,118,760` Plus entries. Exact own winners for any main draw:
- 5 matches: 1
- 4 matches: 225
- 3 matches: 9,900.

At an EUR1 Plus stake, cost is EUR2,118,760. Granting the full EUR500,000 top prize gives gross **EUR1,148,000 = 54.1826%**. Non-top fixed cash is only **EUR648,000 = 30.5839%**.

Status: **REJECTED guaranteed-profit full coverage**.

## Current OLG targeted bonuses — REAL SUBSIDY, NO CASH GUARANTEE
Fresh official terms show several 2026–2027 offers that are more meaningful than ordinary second-chance promotions:
- targeted LOTTO MAX: spend at least CAD6 -> CAD6 LOTTO MAX bonus;
- targeted LOTTO 6/49: spend at least CAD3 -> CAD3 LOTTO 6/49 bonus;
- targeted LOTTO MAX: spend at least CAD18 -> CAD6 LOTTO MAX bonus;
- current birthday lottery-bonus offers can provide free game-specific bonus value to eligible accounts.

Important structural result:
- these are genuine deterministic **face-value subsidies after eligibility/qualification**;
- they are targeted, generally one-time and tightly capped;
- bonus funds are lottery-use value rather than guaranteed withdrawable cash;
- a bonus-funded ticket can return zero.

Therefore the current offers do not satisfy terminal guaranteed-profit conditions and cannot scale enough to subsidize a full finite-space portfolio. H009 should nevertheless retain **deterministic targeted bonus funds** as a real EV overlay class distinct from random promotions.

# Recently closed branches
- H035 Lotterywest Super66/Cash 3: 54.35% / 36.36% coverage floors; rejected.
- H034 Ontario DAILY KENO Pick 2–10: favorable uncapped return only 42.03%–55.07%; rejected.
- H033 New Zealand Bullseye: real 28.57% multi-draw discount, but shared/capped payouts destroy strict guarantee.
- H032 Canada DAILY GRAND: favorable full coverage 44.35%, strict cash floor 36.21%.
- H031 Georgia/Virginia Cash Pop Cover All: guaranteed win but floor 33.33% of coverage cost.
- H029/H029b Virginia Pick 3/4/5 including FIREBALL: additive-family guarantee rejected.
- H030 Virginia Cash 5 + EZ Match: full-space route negative; sharing blocks strict guarantee.
- H021–H028 compact/fixed/full-space screens: sampled products rejected.
- Beşdə 5 and ONLOTO 1–10 full coverage: rejected.
- Powerball/Mega Millions/EuroMillions main-game terminal guarantees: rejected.
- H012a/H004 ordinary additive wheels: rejected by expectation theorem.
- H015 anti-crowd standalone: rejected as guarantee; overlay only.

# Other active / blocked branches
- H020 lawful two-sided hedging/arbitrage: post-fill surebet mechanism validated; fee/depth scanner implemented; raw live-book acquisition remains runtime/data blocked.
- H019 capped fixed-prize competition saturation: mechanism valid in principle; sampled instances fail cash-floor/full-cap test.
- H007 high-frequency RNG: data-gated; no trustworthy ordered bulk history recovered.
- H018 Lucky Contestant: standalone guarantee rejected; conditional-EV overlay remains data-gated.
- H014 Azerbaijan 4+4 carryover: data-blocked.
- H010 Poz-Qazan remaining inventory: data-blocked.

# Next priorities
1. Continue fast analytic screens beyond H036, emphasizing **deterministic discount/rebate + fixed non-shared cash payouts** or coverage return already near 100%.
2. Expand the deterministic subsidy scan beyond OLG, but distinguish withdrawable cash/rebate from lottery-only bonus credit; prioritize uncapped/repeatable offers.
3. Revisit H020 live arbitrage immediately if raw public order books become retrievable.
4. H019 only when capped-entry cash-floor economics materially improve.
5. H006/H007 only after reliable histories/machine metadata become obtainable.
6. H010/H014 if new authoritative data routes appear.
7. H018 conditional-EV calibration if exact mechanics/live endpoint becomes recoverable.
8. Before EXHAUSTED: additional current products, deterministic cash-rebate scan, Bayesian hidden-state inference, and causal implementation tests.

Permanent master audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
