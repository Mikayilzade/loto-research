# STATUS

Updated: 2026-08-20
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Current lottery stage
**Structural/state-edge search + Azerbaijan 4+4 exceptional carryover closure + TezLoto/RNG bias + deterministic lottery promotions.**

### Strong historical controls
- Cash WinFall rolldown: historical +EV mechanism validated (~+10.69% conservative pre-tax sample ROI), but not a current guaranteed route.
- Kazakhstan 4/20: lower-category zero-winner carryover mechanism validated; sampled state negative.
- Lotto Texas 2023 / H108: syndicate operationally acquired virtually all 25.8m combinations and guaranteed possession of the jackpot line; actual draw profitable, but strict all-outcome guarantee failed due external duplicate-winner sharing. Texas now prohibits all/substantially-all combination purchase facilitation.

### H109–H112 — fixed supply / scratch / sealed-pack routes
- H109 unique-number raffle takeover: Irish fixed raffle full takeover returned only 42.2833% deterministic gross; dynamic raffles retain external-entry ownership risk.
- H110 Texas scratch closing-state bound: buyer-favorable ceiling max 78.2494%.
- H111 Texas guaranteed sealed-pack floor + full 5% retailer commission: max 67.5% strict recovery.
- H112 cross-jurisdiction high-RTP/fixed-pack screen: no current official non-Texas sealed-pack minimum remotely high enough to bridge takeout.

Status: **MATERIALLY CLOSED / NO SUCCESS**.

### H113 — Azerbaijan 4+4 full-space hurdle
Current official 4+4 price is 2 AZN; full space is `C(20,4)^2 = 23,474,025` variants costing **46,948,050 AZN**. Even at a maximally favorable 80% sales-linked prize-fund assumption, strict full-space profit requires external pre-existing value **>9,389,610 AZN before tax/execution**. The observed jackpot around early August 2026 (~1.9m AZN before it was won) was far below this hurdle.

Status: **NAIVE FULL-SPACE ROUTE CLOSED / NO SUCCESS**.

### H114 — TezLoto exact dynamic odds
All 159 published state × bet-type cells were checked against exact uniform-without-replacement fair odds. Best published cell returns only **78.2609% gross**; all complete-coverage constructions are negative. The only remaining TezLoto branch is empirical RNG/virtual-lototron bias, which needs >27.78% multiplicative probability lift merely to cross EV=1 in the best published state and must survive out-of-sample testing.

Status: **BASE ODDS + COMPLETE COVERAGE CLOSED / H007 BIAS DATA BRANCH OPEN / NO SUCCESS**.

### H115 — 4+4 ordinary one-step carryover
Recovered current rule wording indicates zero-winner category II–XI amounts are added to the **next draw's prize fund** and then distributed proportionally among winners, rather than compounding indefinitely in the same category. At reconstructed N≈38k–50k, ordinary II-only zero carryover requires roughly **4.49–4.54x previous/current sales contraction** to bridge the current break-even gap under deliberately maximum-favorable assumptions.

Status: **ORDINARY II-ONLY CARRYOVER MATERIALLY CLOSED / NO SUCCESS**.

### H116 — 4+4 exceptional multi-zero carryover
Exact category-II–VI match probabilities and simultaneous-zero probabilities were derived. At N≈38k–50k:
- II+III both zero occurs only ~3.54%–7.90% under iid selection and still requires **~2.25–2.27x** prior/current sales contraction under maximum-favorable allocation assumptions;
- three-zero states such as II+III+V/VI are roughly 1e-5–2e-4 probability and still require **~1.50–1.51x** contraction;
- all II–VI zero is effectively negligible under iid selection and is the only maximized state capable of bridging the gap without a sales collapse (~0.91x threshold).

Existing detailed 2026 samples and newly indexed draw #800 continue to show the recurring pattern II=0 with III–VI nonzero. Draw #800 X/XI winner counts imply N_hat≈39.0k, consistent with prior sales-scale reconstruction.

Player selection clustering can alter the frequency estimates, but the economic contraction hurdles are upper-bound economics and remain the decisive screen.

Status: **EXCEPTIONAL MULTI-ZERO ROUTE MATERIALLY NARROWED / ONLY VERY RARE HIGH-ORDER STATES OR EXTREME SALES COLLAPSE REMAIN / NO SUCCESS**.
Files:
- `research/h116_4plus4_exceptional_multizero_bound.md`
- `data/derived/h116_4plus4_multizero_bounds.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H116_APPEND.md`

### H117 — Poland Multi Multi recurring +50% promotions
A current deterministic promotion was screened because Multi Multi allows a mathematically exact full-space portfolio: for a fixed k, owning all `C(80,k)` subsets fixes the count of j-hit tickets under every possible 20-of-80 draw.

Current official supplemental rules for **19–22 August 2026** boost the k=9 prize column by 50%. Exact full-space results:
- k=9 ordinary Multi Multi: **61.3579%** deterministic gross;
- k=9 with Plus: **62.9251%** deterministic gross.

The entire recurring promotion class was then closed prospectively by granting the same 1.5x boost to every prize in each k=1..10 column:
- best ordinary promoted full-space return: **61.7421%** at k=5;
- best Plus promoted full-space return: **63.7187%** at k=6.

Therefore the current and same-structure future `win 50% more` rotations remain far below break-even even under complete coverage. Reopen only for a materially larger boost (~2.35x–2.60x depending on k/Plus), a deterministic cash rebate, or a major price/payout redesign.

Status: **CURRENT LIVE PROMOTION + RECURRING 50%-BOOST CLASS CLOSED / NO SUCCESS**.
Files:
- `research/h117_poland_multimulti_50pct_promo_fullspace.md`
- `data/derived/h117_multimulti_promo_fullspace.csv`
- `src/loto_research/multimulti_promo_coverage.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H117_APPEND.md`

### Azerbaijan live branches
- **4+4 / H014/H115/H116:** ordinary II-only and realistic II+III carryover states are economically too weak absent extreme observable sales contraction. Reopen only on >=3 prior zero categories, a two-zero state plus >2.25x observable contraction, major operator-funded external addition, or materially more favorable primary registration rules.
- **TezLoto / H007/H114:** only bulk-history RNG/bias testing remains; no dependable public bulk archive/API has yet been recovered.
- **Poz-Qazan:** ordinary initial states negative; remaining-prize conditional edge remains data-blocked because exact live unsold denominator/registration state is unavailable.
- **Beşdə 5 / Super Keno / ONLOTO:** ordinary/full-space screens negative.

### Global lottery branches already screened
Powerball, Mega Millions, EuroMillions, UK Lotto Must Be Won, numerous finite fixed-prize games, additive wheels, anti-crowd selection, unique raffles, scratch closing-inventory, sealed-pack guarantees, recurring 50%-boost fixed-prize promotions, and current full-space constructions have all failed strict all-outcome net-profit guarantees under current rules/economics. Historical Cash WinFall and Lotto Texas remain proof that structural lottery edges can exist, but neither supplies a current executable guarantee.

## NEXT ACTION
1. **Primary-rule closure for 4+4:** continue searching only for the actual detailed registration no. 336 conditions. If recovered, verify exact percentages and zero-category redistribution; reopen economics only if materially more favorable than H115/H116 bounds.
2. **H007 TezLoto / high-frequency RNG history:** pursue only if a reliable bulk draw-history/API route becomes available; then run pre-registered out-of-sample bias tests against the >27.78% lift hurdle.
3. **Global rolldown / buy-the-pot search:** target only current games with legally acquirable fixed/capped eligible supply and observable external subsidy large enough to clear the H021/H113 takeout hurdle after sharing/taxes/limits.
4. **Lottery promotions:** H117 closes recurring +50% Multi Multi prize-table boosts. Continue only with promotions whose deterministic subsidy can raise the exact worst-case/full-space floor above 100%, especially cash rebates, >~2.4x fixed-prize boosts, or fixed external pools allocated across a capped purchasable supply.
5. **Fixed-pack instant tickets:** reopen only with official current evidence of an unusually high per-pack guaranteed minimum or deterministic subsidy above exact break-even.
6. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master: `research/CHECKED_PROJECTS_AND_TESTS.md`; connector-safe append packets are authoritative additions when full master replacement is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H117_APPEND.md`.
Latest case: `research/h117_poland_multimulti_50pct_promo_fullspace.md`.
