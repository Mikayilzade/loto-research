# STATUS

Updated: 2026-08-20
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Current lottery stage
**Structural/state-edge search + Azerbaijan 4+4 exceptional carryover closure + TezLoto/RNG bias + deterministic lottery promotions + capped-supply raffle takeover.**

## Strong historical controls
- Cash WinFall rolldown: historical +EV mechanism validated (~+10.69% conservative pre-tax sample ROI), but not a current guaranteed route.
- Kazakhstan 4/20: lower-category zero-winner carryover mechanism validated; sampled state negative.
- Lotto Texas 2023 / H108: syndicate operationally acquired virtually all 25.8m combinations and guaranteed possession of the jackpot line; actual draw profitable, but strict all-outcome guarantee failed due external duplicate-winner sharing. Texas now prohibits all/substantially-all combination purchase facilitation.

## H109–H112 — fixed supply / scratch / sealed-pack routes
- H109 unique-number raffle takeover: Irish fixed raffle full takeover returned only 42.2833% deterministic gross; dynamic raffles retain external-entry ownership risk.
- H110 Texas scratch closing-state bound: buyer-favorable ceiling max 78.2494%.
- H111 Texas guaranteed sealed-pack floor + full 5% retailer commission: max 67.5% strict recovery.
- H112 cross-jurisdiction high-RTP/fixed-pack screen: no current official non-Texas sealed-pack minimum remotely high enough to bridge takeout.

Status: **MATERIALLY CLOSED / NO SUCCESS**.

## H113–H116 — Azerbaijan 4+4 carryover economics
- H113 full-space: current 2 AZN price makes `C(20,4)^2 = 23,474,025` variants cost **46,948,050 AZN**. Even at a maximally favorable 80% sales-linked prize-fund assumption, external pre-existing value must exceed **9,389,610 AZN** before tax/execution. Observed jackpot around early August 2026 (~1.9m AZN) was far below this.
- H115 ordinary II-only one-step carryover: requires roughly **4.49–4.54x** prior/current sales contraction under deliberately maximum-favorable assumptions.
- H116 II+III zero: still requires ~**2.25–2.27x** contraction. Three-zero states remain extremely rare and still require ~1.50x contraction. All II–VI zero is effectively negligible under iid selection and is the only maximized state capable of bridging the gap without a sales collapse.

Status: **NAIVE FULL-SPACE + ORDINARY/REALISTIC MULTI-ZERO ROUTES MATERIALLY CLOSED / ONLY VERY RARE HIGH-ORDER STATES, EXTREME OBSERVABLE SALES COLLAPSE, OR MATERIALLY BETTER PRIMARY RULES REMAIN**.
Files:
- `research/h116_4plus4_exceptional_multizero_bound.md`
- `data/derived/h116_4plus4_multizero_bounds.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H116_APPEND.md`

## H114 — TezLoto exact dynamic odds
All 159 published state × bet-type cells were checked against exact uniform-without-replacement fair odds. Best published cell returns only **78.2609% gross**; all complete-coverage constructions are negative. The only remaining TezLoto branch is empirical RNG/virtual-lototron bias, which needs >27.78% multiplicative probability lift merely to cross EV=1 in the best published state and must survive pre-registered out-of-sample testing.

Status: **BASE ODDS + COMPLETE COVERAGE CLOSED / H007 BIAS DATA BRANCH OPEN / NO SUCCESS**.

## H117 — Poland Multi Multi recurring +50% promotions
Current official supplemental rules for 19–22 August 2026 were screened with exact full-space identities. Current k=9 promotion yields only **61.3579%** deterministic gross ordinary and **62.9251%** with Plus. Granting the same 1.5x boost to every prize in every k=1..10 column gives a best promoted full-space return of only **63.7187%**.

Status: **CURRENT LIVE PROMOTION + RECURRING 50%-BOOST CLASS CLOSED / NO SUCCESS**.
Files:
- `research/h117_poland_multimulti_50pct_promo_fullspace.md`
- `data/derived/h117_multimulti_promo_fullspace.csv`
- `src/loto_research/multimulti_promo_coverage.py`
- `research/CHECKED_PROJECTS_AND_TESTS_H117_APPEND.md`

## H118 — current capped charity/hospital raffle takeover
A current 2026 screen tested six fixed-supply products under deliberately buyer-favorable assumptions: buy the entire authorized supply at the cheapest published unit price and grant the buyer the entire fixed advertised prize board at full value, ignoring taxes and execution costs.

Results:
- Roughrider & Children Main Lottery: **85.4135%** favorable gross (closest case; current new buyer is actually worse because VIP deadline already passed);
- SickKids 2026 Main: **63.9489%**;
- Alberta Cancer Foundation Main: **59.3469%**;
- SickKids Cash Calendar: **54.4916%**;
- Alberta Win Daily Cash: **34.8941%**;
- Roughrider & Children Cash Calendar: **19.8525%**.

A hard cap alone therefore does not create a buy-the-pot guarantee; the fixed external prize board must exceed minimum all-ticket acquisition cost. Open 50/50 draws remain unsuitable because external eligible tickets are uncapped and the prize is sales-linked.

Status: **CURRENT CAPPED HOSPITAL/CHARITY TAKEOVER CLASS MATERIALLY CLOSED / NO SUCCESS**.
Files:
- `research/h118_current_capped_charity_raffle_takeover.md`
- `data/derived/h118_current_capped_raffle_screen.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H118_APPEND.md`

## H119 — EuroDreams Ireland guaranteed-winner promotion
Current EuroDreams uses `C(40,6)*5 = 19,191,900` lines at €2.50, so full-space spend is **€47,979,750**. The Ireland-only event adds one extra €2,000/month for 5 years prize to one normal Irish winner.

A deliberately buyer-favorable full-space upper bound values the Tier 1 annuity at its full undiscounted €7.2m cashflow, all four Tier 2 annuities at €120k each, treats displayed average lower-tier prizes as exact, and grants the entire extra €120k promotional annuity to the buyer. Even then total gross is only **€21,431,110 = 44.66699%** of spend. The promotion itself contributes at most **0.2501%** of full-space cost.

Status: **GUARANTEED-WINNER FIXED TOP-UP PROMOTION REJECTED AS FULL-SPACE GUARANTEE / NO SUCCESS**.
Files:
- `research/CHECKED_PROJECTS_AND_TESTS_H119_APPEND.md`
- `data/derived/h119_eurodreams_guaranteed_winner_fullspace.csv`

## Azerbaijan live branches
- **4+4 / H014/H115/H116:** ordinary II-only and realistic II+III carryover states are economically too weak absent extreme observable sales contraction. Reopen only on >=3 prior zero categories, a two-zero state plus >2.25x observable contraction, major operator-funded external addition, or materially more favorable primary registration rules.
- **TezLoto / H007/H114:** only bulk-history RNG/bias testing remains; no dependable public bulk archive/API has yet been recovered.
- **Poz-Qazan:** ordinary initial states negative; remaining-prize conditional edge remains data-blocked because exact live unsold denominator/registration state is unavailable.
- **Beşdə 5 / Super Keno / ONLOTO:** ordinary/full-space screens negative.

## Global lottery branches already screened
Powerball, Mega Millions, EuroMillions, UK Lotto Must Be Won, numerous finite fixed-prize games, additive wheels, anti-crowd selection, unique raffles, scratch closing-inventory, sealed-pack guarantees, recurring 50%-boost fixed-prize promotions, current Canadian capped hospital/charity takeovers, guaranteed-winner fixed top-up promotions, and current full-space constructions have all failed strict all-outcome net-profit guarantees under current rules/economics. Historical Cash WinFall and Lotto Texas remain proof that structural lottery edges can exist, but neither supplies a current executable guarantee.

## NEXT ACTION
1. **Primary-rule closure for 4+4:** continue searching only for the actual detailed registration no. 336 conditions. If recovered, verify exact percentages and zero-category redistribution; reopen economics only if materially more favorable than H115/H116 bounds.
2. **H007 TezLoto / high-frequency RNG history:** pursue only if a reliable bulk draw-history/API route becomes available; then run pre-registered out-of-sample bias tests against the >27.78% lift hurdle.
3. **Global rolldown / buy-the-pot search:** target current games with legally acquirable fixed/capped eligible supply and an observable external subsidy large enough to clear the H021/H113 takeout hurdle after sharing/taxes/limits. H118 closes ordinary current Canadian hospital/charity capped-supply examples; H119 closes small fixed winner-top-up promotions. Prioritize operator/sponsor-funded final-draw overlays, must-be-won fixed pools, and unsold-inventory structures where prior tickets are excluded from the relevant prize pool.
4. **Lottery promotions:** H117 closes recurring +50% Multi Multi prize-table boosts and H119 closes a €120k winner-top-up against ~€48m full-space cost. Continue only with promotions whose deterministic subsidy can raise the exact worst-case/full-space floor above 100%, especially cash rebates, >~2.4x fixed-prize boosts, or fixed external pools allocated across a capped purchasable supply.
5. **Fixed-pack instant tickets:** reopen only with official current evidence of an unusually high per-pack guaranteed minimum or deterministic subsidy above exact break-even.
6. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master: `research/CHECKED_PROJECTS_AND_TESTS.md`; connector-safe append packets are authoritative additions when full master replacement is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H119_APPEND.md`.
Latest case: `research/CHECKED_PROJECTS_AND_TESTS_H119_APPEND.md`.
