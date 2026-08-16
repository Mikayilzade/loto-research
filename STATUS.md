# STATUS

Updated: 2026-08-16
Branch: `research-work`

## Current stage
**Stage 1 — structural/state-edge search; H037 Irish Lotto Plus Million Euro Raffle quantified**

Terminal definitions:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# H037 — Irish Lotto Plus Million Euro Raffle
Files:
- `research/h037_lotto_plus_million_raffle.md`
- `data/derived/h037_lotto_plus_million_raffle_screen.csv`
- `src/loto_research/lotto_plus_raffle.py`
- `tests/test_lotto_plus_raffle.py`

## Strict guarantee — CLOSED
Published mechanics defeat terminal guarantee in two ways:
- each Plus line receives a four-digit raffle number rather than letting the player choose one, so finite purchases cannot force deterministic coverage of all 10,000 raffle codes;
- in a Million Euro Raffle event, all tickets with the winning raffle number enter a second random draw and one ticket owner gets the extra €1m, so external qualifying tickets preserve a legal outcome where another player receives it.

Status: **REJECTED as strictly guaranteed-profit strategy**.

## Strong positive-EV overlay lead
Current pre-autumn-2026 6/47 Plus tables imply approximately:
- Plus 1 fixed-prize EV: **€0.22902755/line**;
- Plus 2 fixed-prize EV: **€0.13263705/line**;
- normal €500 raffle EV: **€0.05/line**;
- total ordinary Plus package EV: **€0.41166460 per €1 Plus add-on**.

The special event adds a guaranteed-to-be-distributed external €1m. Under entry symmetry, event subsidy EV is `€1,000,000 / T` per eligible Plus line, where `T` is total Plus entries.

Incremental Plus break-even:
- `T ≈ 1,699,710.73` eligible Plus lines;
- equivalent expected ordinary-raffle winner count ≈ **169.97**.

The operator says the Lotto Plus Raffle typically sees **60–120** €500 winners, heuristically corresponding to about **600k–1.2m** Plus entries. In that range modeled incremental Plus EV is approximately **€2.078–€1.245 per €1 add-on**.

This is **not terminal SUCCESS** because payout is random and zero-return outcomes remain. It is now one of the strongest live +EV leads and merits event-specific participation calibration.

# H036 — Irish Plus coverage + current OLG targeted subsidy screen
## Daily Million Plus — CLOSED
Complete `C(39,6)=3,262,623` coverage at EUR1/line costs EUR3,262,623. Even granting our winner the entire EUR500,000 top prize and valuing each EUR2 Scratch Card at full EUR2 face value, gross is only **EUR961,600 = 29.4732%**. Removing the shareable top prize from the strict guaranteed cash floor leaves **EUR461,600 = 14.1481%**.

## EuroMillions Plus — CLOSED
Full 5/50 space = `C(50,5)=2,118,760` Plus entries. At an EUR1 Plus stake, cost is EUR2,118,760. Granting the full EUR500,000 top prize gives gross **EUR1,148,000 = 54.1826%**. Non-top fixed cash is only **EUR648,000 = 30.5839%**.

## Current OLG targeted bonuses — REAL SUBSIDY, NO CASH GUARANTEE
Fresh official terms show current targeted offers with deterministic face-value bonus funds after qualification, but they are targeted, generally one-time/tightly capped and lottery-use value rather than guaranteed withdrawable cash. A bonus-funded ticket can return zero.

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
1. **H037 calibration:** recover event-specific Lotto Plus Raffle winner counts / sales proxies for special €1m dates; estimate event-day participation uplift and test whether `T < 1.70m` holds.
2. Confirm ticket-level versus line-level mechanics in the once-off €1m selection and quantify effect on multi-line entries.
3. Continue deterministic subsidy/rebate scan, prioritizing uncapped/repeatable withdrawable cash rather than lottery-only credit.
4. Revisit H020 live arbitrage immediately if raw public order books become retrievable.
5. H019 only when capped-entry cash-floor economics materially improve.
6. H006/H007 only after reliable histories/machine metadata become obtainable.
7. H010/H014 if new authoritative data routes appear.
8. Before EXHAUSTED: additional current products, deterministic cash-rebate scan, Bayesian hidden-state inference, and causal implementation tests.

Permanent master audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. H037 must be reflected there; if connector-size limits prevent safe in-place replacement during a run, `research/h037_lotto_plus_million_raffle.md` is the authoritative packet until the next successful ledger compaction/update.
