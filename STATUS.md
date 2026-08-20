# STATUS

Updated: 2026-08-20
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Current lottery stage
Structural/state-edge search, live fixed-prize undersubscription monitoring, cumulative early-ticket/cohort-local overlays, deterministic late-takeover floors, deterministic block/tranche allocation, rare Azerbaijan 4+4 carryover closure, TezLoto/RNG-bias data recovery, lottery-specific promotions/loyalty, capped/fixed-supply raffle economics, and global rolldown/buy-the-pot screens only where external subsidy can plausibly cross the exact coverage deficit.

## Strong historical / structural controls
- Cash WinFall rolldown: historical +EV mechanism validated (~+10.69% conservative pre-tax sample ROI), not current guaranteed route.
- Kazakhstan 4/20: lower-category zero-winner carryover mechanism validated; sampled state negative.
- Lotto Texas 2023 / H108: near-full combination acquisition operationally validated and actual draw profitable; strict guarantee fails on external duplicate jackpot sharing; Texas now blocks all/substantially-all combination facilitation.

## H109-H112 — fixed supply / scratch / sealed-pack
- H109 unique-number raffle full takeover: Irish fixed raffle only **42.2833%** deterministic gross; dynamic raffles retain external-entry ownership risk.
- H110 Texas scratch closing-state buyer-favorable ceiling: **78.2494%**.
- H111 Texas sealed-pack floor + full 5% retailer commission: max **67.5%** strict recovery.
- H112 non-Texas fixed-pack/high-RTP screen: no official guaranteed per-pack minimum near break-even.
Status: **MATERIALLY CLOSED / NO SUCCESS**.

## H113-H116 — Azerbaijan 4+4 carryover
- Full space `C(20,4)^2 = 23,474,025`; at 2 AZN cost = **46,948,050 AZN**.
- Even under favorable 80% sales-linked prize-fund assumption, external value hurdle exceeds **9,389,610 AZN**.
- Ordinary II-only one-step carryover needs ~**4.5x** prior/current sales contraction.
- II+III zero still needs ~**2.25x** contraction; >=3 zero categories become very rare.
Status: **ORDINARY/REALISTIC CARRYOVER GUARANTEE ROUTES MATERIALLY CLOSED**. Reopen only on materially better primary rules, >=3 prior zero categories, extreme observable sales collapse, or explicit operator-funded additions.

## H114 — TezLoto
All 159 published state × bet-type cells checked against exact fair odds. Best published gross return only **78.2609%**. Complete coverage negative. Remaining branch is H007 empirical RNG/virtual-lototron bias; required probability lift is >**27.78%** in best state and must survive preregistered out-of-sample testing. Reliable bulk history/API still missing.

## H117-H121 — promotion / raffle takeover closure
- H117 Poland Multi Multi +50% prize boosts: best full-space promoted return **63.7187%**.
- H118 six capped hospital/charity products: best buyer-favorable full takeover **85.4135%**.
- H119 EuroDreams guaranteed-winner top-up: buyer-favorable full-space **44.6670%**.
- H120 FDJ Grand LOTO forced distribution: buyer-favorable full-space **77.4243%**; full coverage itself removes the no-jackpot redistribution branch.
- H121 micro-capped/donated-prize raffles: best optimistic full takeover **71.725%**.
Status: **STANDARD CAPPED-SUPPLY/FIXED-BOARD TAKEOVER CLASS MATERIALLY CLOSED unless a genuine prize-board inversion or deterministic portfolio floor appears**.

## H122-H128 — fixed-board undersubscription overlays
### Florida Millionaire Raffle 2026
- Final official sales **369,180 tickets at $20**.
- Fixed nominal board **$12.818m** for the last-window structure; aggregate overlay **+$5.4344m** versus ticket revenue.
- Last-window pre-tax EV **$28.9953 on $20 = +44.9767% ROI**.
- A ticket bought before the first interim draw remained eligible for four interim boards plus final: conservative pre-tax EV floor **$34.7202 on $20 = +73.6010% ROI** at the final denominator.
- Strict guarantee fails because external tickets can occupy all winning slots; full launch ownership costs $40m vs max board $22.818m.

### Calibration / monitor class
- H123 Maryland/Virginia/Michigan calibration: only sufficiently large fixed boards plus low denominators create +EV.
- H125 Jersey 2026 near-threshold state: ~**96.30% nominal gross**, still negative.
- H126 Michigan Super Raffle 2025: ~**+13.59% headline nominal EV**, but cash-equivalent valuation ~**-9.35%**.
- H127 Pennsylvania weekly-cohort overlay theorem validated; recovered cohorts negative.
- H128 cumulative early-ticket duration overlay validated; Florida early tickets were much stronger than last-window tickets.
Status: **STRONG +EV MONITOR CLASS VALIDATED / STRICT GUARANTEE REJECTED**.

## H124 — official lottery loyalty/reward rebate
Ohio MyLotto Rewards gives deterministic points on non-winning tickets but is capped at 1,200 points/month. Exact complementary-cover controls top out at **78.125%** package gross. Status: **GUARANTEED-PROFIT COVERAGE REJECTED**.

## H129 — deterministic late-takeover floor
Exact theorem for buying **all unsold tickets** in a fixed-board raffle after `E` tickets are already externally owned:

`G(E) = max(0, total_board - sum(E highest prize values))`

Takeover cost is `(cap-E)*ticket_price`. If `E >= number_of_prize_slots`, strict floor is zero.

### North Carolina Celebrate America Raffle 2026
- cap **25,000** tickets × **$10**;
- board: **20×$2,500 + 250×$250 + 2,000×$25 = $162,500**;
- **2,270** winning slots;
- best all-remaining takeover at launch: **65.0% strict gross**;
- strict floor falls to zero once external ownership reaches 2,270 tickets;
- random-ticket +EV threshold: final sales `<16,250`, but reliable official final sold denominator was not recovered.

Status: **LATE-TAKEOVER THEOREM VALIDATED / NC GUARANTEE REJECTED / MONITOR UPGRADED**.
Files: `research/h129_nc_raffle_late_takeover_floor.md`, `src/loto_research/raffle_takeover_floor.py`, `data/derived/h129_nc_raffle_takeover_floor.csv`, `research/CHECKED_PROJECTS_AND_TESTS_H129_APPEND.md`.

## H130 — NJ Fast Play Progressive finite-grid interpretation
The published `500,000-ticket jackpot grid` initially looked like a possible finite-deck buy-the-pot path. Official game pages explicitly state that prizes **instantly replenish after every purchase** and every ticket retains the same odds. Therefore the grid is a probability denominator, not depleting inventory; buying 500,000 tickets does **not** guarantee the jackpot.

Exact favorable nominal break-even common-jackpot thresholds from sampled current games:
- $10 U.S. Soccer: **$1.948m**;
- $20 Max Win: **$3.797m**;
- $30 Jersey Jackpot: **$5.555m** despite the +$25k jackpot bonus;
- $5 Perfectly Pear: **$2.107m** common jackpot at 50% share;
- $1 Jersey Jackpot: **$2.313m** common jackpot at 10% share.

2026 scale control: official indexed jackpot **$459,619** on July 26; a July 29 $30 ticket then won **$160,474** (100% jackpot state). These are far below the sampled +EV thresholds.

Status: **FINITE-GRID TAKEOVER REJECTED / HIGH-JACKPOT +EV MONITOR ONLY / NO GUARANTEE**.
Files: `research/h130_nj_fast_play_progressive_grid.md`, `src/loto_research/fastplay_progressive.py`, `data/derived/h130_nj_fastplay_thresholds.csv`, `research/CHECKED_PROJECTS_AND_TESTS_H130_APPEND.md`.

## Azerbaijan live branches
- **4+4:** only rare high-order carryover states / material primary-rule improvement remain.
- **TezLoto:** only bulk-history RNG/bias testing remains; public bulk archive/API still unresolved.
- **Poz-Qazan:** remaining-prize conditional edge data-blocked because exact live unsold denominator/registration state unavailable.
- **Beşdə 5 / Super Keno / ONLOTO:** ordinary/full-space screens negative.

## NEXT ACTION
1. **Deterministic block/tranche allocation:** search lottery promotions/raffles where every purchased block/tranche receives a guaranteed minimum prize, rebate, free-ticket bundle, or ring-fenced allocation. This is now the highest-value escape from the external-ticket zero-floor theorem.
2. **Prize-board inversion monitor using H129 theorem:** search current/upcoming official fixed-board raffles with public remaining counts and compute both +EV denominator thresholds and exact all-remaining worst-case floor. Prioritize unusually flat boards, very high winner-count/cap ratios, and operator-funded boards near/above ticket revenue.
3. **Live cumulative/cohort-local undersubscription monitor:** search current official raffles with cumulative early-ticket eligibility, weekly/ring-fenced boards, or early-bird cash pools; compute cash/tax-adjusted remaining-board and cohort EV.
4. **Progressive instant/Fast Play monitor:** only reopen H130 if a common jackpot approaches exact game-specific +EV thresholds or if primary rules reveal a non-replenishing finite grid.
5. **Historical support reconstruction:** where final sold counts are missing but complete winning-number support exists, use order-statistic bounds only as secondary evidence, then seek primary confirmation.
6. **Azerbaijan 4+4:** search specifically for detailed registration no. 336 conditions; reopen only if rules materially improve H115/H116 bounds.
7. **H007 TezLoto/RNG:** pursue only on recovery of reliable bulk draw history/API, then preregister and run out-of-sample bias tests against >27.78% probability-lift hurdle.
8. Continue global rolldown/buy-the-pot search only where verified external subsidy is large relative to full-space spend, or a deterministic minimum allocation exists.
9. Fixed-pack instant tickets: reopen only with official evidence of guaranteed per-pack minimum or deterministic subsidy above exact break-even.
10. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master: `research/CHECKED_PROJECTS_AND_TESTS.md`; connector-safe append packets are authoritative additions when direct replacement of the very large master ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H130_APPEND.md`.
Latest case: `research/h130_nj_fast_play_progressive_grid.md`.
