# STATUS

Updated: 2026-08-25
Branch: `research-work`
Scope: **LOTTERY ONLY**. Ignore historical non-lottery automation drift.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

## Current checkpoint
Latest completed numbered lottery packet: **H265 — New Jersey Pick-3 Green Ball terminal Double Draw bound**.
Exact-family lane `H225-X*` is now **CLOSED / EXHAUSTED**. See `research/H225_EXACT_STATUS.md` and `research/H225_X19_X20_VALIDATION.md`.

### Exact-family state
- H232: 306,450 quotient states screened; 306,098 retained a legal shift tuple; 139,869,763 exact legal shift tuples survived.
- H234/H235 established the cutting-plane baseline at **303,802** coefficient states / **90,425,060** legal shift tuples.
- H225-X1 through X18 iteratively added exact balanced separator cuts and full 44-way rescans, reducing the family to **3,300 states / 71,392 shift tuples** at X18.
- H225-X19: only 12 of 44 chunks remained active; all **12/12** returned exact `n3<=2` balanced counterexamples, **0 inconclusive**, yielding **12 new cuts**.
- **H225-X20:** full exact rescreen over **44 canonical shards / 11 sectors / exactly 306,450 quotient states** left **0 coefficient survivors / 0 legal shift tuples**.
- Therefore the unchanged H225 general cyclic-affine family is rigorously **exhausted**. Do not create X21/X22 unless the mathematical family itself is broadened.

### Recent lottery closures / blockers
- H236 RI Lucky 3 Spot: universal free 2X clears arithmetic threshold, but universal entitlement/execution not established.
- H238 RI Kick Back: exact current entitlement remains data-blocked.
- H239 Georgia/NC Keno Bonus Hours: rejected by exact full-coverage arithmetic.
- H240-H241 Missouri Club Keno Bonus Hours including Bulls-Eye variants: rejected by stronger-than-real +50% upper bounds.
- H242 Michigan Tripler Time: Doubler/Tripler status is random, not deterministically allocable.
- H243 Illinois plus FIREBALL: exhaustive Straight-cover upper bounds remain below break-even.
- H244 WinTrillions Powerball discount: terms permit removal of the promotional enhancement in guaranteed-profit constructions.
- H245 UK Lotto current full-space: fixed-prize return too low and full coverage prevents the relevant zero-winner rolldown branch.
- H246 LOTTO 6/49 Aug. 29 SuperDraw: even a deliberately favorable isolated-pool model returns only 46.5456% of full-cover spend.
- H247 free Quick Pick / BOGO: uncontrolled free selections have zero guaranteed marginal coverage and zero strict cash floor.
- H248 Lotto.com 25% draw discount: below break-even for known finite covers.
- H249 Jackpocket credit × Maine Pick 3 Single Digit: $5 exact cover guarantees $2.50 gross; current qualifying deterministic credit/fee/entitlement evidence incomplete.
- H250 courier-supported partial-digit exact subsidy floor: exact-position 50% cover verified, but no current deterministic subsidy above the hurdle plus fees.
- H251 Irish Lotto 6/45 Lotto Plus: full-cover incremental Plus return only 52.8477%.
- H252 Irish Lotto 6/45 cap full-cover: sole-jackpot-winner floor can be positive, but one external Match-6 line destroys the strict guarantee; full coverage also prevents the zero-winner cap rolldown branch.
- H253 Georgia scratcher #1709 endgame: apparent >100% residual-prize EV is not executable because unclaimed prizes are not certified unsold/purchasable inventory.
- H254 Irish guaranteed raffles: finite Christmas Millionaire Raffle full inventory returns only 42.2833%; market-wide raffle identifiers cannot be deterministically monopolized at bounded cost.
- H255 UK Lotto lower-tier fixed boost: historical Match-3=£100 plus ordinary fixed higher tiers averages only 62.4667% of stake; additive covering portfolios cannot yield an everywhere-positive profit.
- H256 NJ Quick Draw Progressive Bonus Hours: current guaranteed +50% fixed-prize uplift remains below break-even for every exact base/BULLSEYE/Double-BULLSEYE full cover; Multiplier has a legal 1X branch and jackpot numbers are uncontrolled.
- H257 LOTTO MAX 2026: complete coverage hits every MAXPLUS/MAXMILLIONS exact-match series, but those prizes and the Main Jackpot are shared among duplicate winning selections; no useful hard pre-draw external-duplicate cap exists.
- H258 EuroMillions cap flow-down: ordinary cap overflow is compatible with full coverage even when rank 1 wins, but one legal external 5+2 duplicate destroys the strict guarantee even under a dominating all-current-prize-money upper bound.
- H259 Wisconsin fixed pull-tab box: complete predetermined pack removes RNG and sharing but returns only **62.8571%** of retail cost; no deterministic subsidy crossing the exact **59.0909%** uplift hurdle was established.
- H260 Canada DAILY GRAND Bonus Draw cover: a one-copy `C(49,5)` cover guarantees all three promotional bonus combinations, but even an impossible no-sharing C$1.5m bonus grant plus favorable base-game cash reaches only **68.6750%** of cover cost.
- H261 Hospital Research Foundation capped raffles: even impossible-perfect ownership of every issued identifier yields only **52.6122%** Home Lottery, **29.7070%** Cash Calendar, and **37.5317%** Holiday for Life at exact cheapest package costs.
- H262 LOTTO 6/49 terminal Gold Ball: the final one-ball state creates a real C$68m unique-identifier takeover theorem with a Gold-Ball-only strict cost ceiling of **22,666,666 paid plays**, but open computer-generated issuance (including Free Plays) prevents certifying ownership of every eligible identifier.
- H264 Uganda LOTTO: current v1.6 special jackpot roll-down explicitly excludes fixed payout Divisions 7/8; exact full-cover fixed-tier return is only **18.1221%**.
- H265 NJ Pick-3 Green Ball: the elimination chamber can make a free second Pick-3 draw deterministic after six white removals, but the strongest portfolio-wide average-return ceiling is exactly **100%** without FIREBALL and **77%** with FIREBALL, so strict guaranteed profit is impossible under the checked rules.

### H260 — DAILY GRAND Bonus Draw exact main-space cover bound
The official June 18/22, 2026 DAILY GRAND promotion added **three 5/49 Bonus Draws** at no extra cost, each with a C$500,000 lump-sum liability for the winning five-number selection. This is a genuine external subsidy and unlike ordinary DAILY GRAND it can be deterministically hit by covering only the main-number space.

Cheapest one-copy main-space cover:
- `C(49,5) = 1,906,884` selections;
- C$3 each;
- acquisition cost **C$5,720,652**.

For any assignment of Grand Numbers to those covered main combinations, the player-favorable no-external-sharing ordinary-draw cash average is invariant at **C$2,428,660**. Hence at least one legal ordinary draw state pays no more than that average. Even ignoring the actual Bonus Draw sharing rule and granting our portfolio the full C$500,000 on all three bonus draws adds only **C$1,500,000**.

Total impossible-favorable upper bound:
- gross **C$3,928,660**;
- return **68.6750%**;
- deficit **C$1,791,992**.

Files:
- `research/h260_daily_grand_bonus_draw_cover_bound.md`
- `src/loto_research/h260_daily_grand_bonus_draw_bound.py`
- `data/derived/h260_daily_grand_bonus_draw_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H260_APPEND.md`

### H261 — Hospital Research Foundation capped-raffle full-buyout screen
Current 2026 No 3 terms publish hard issuance caps and package prices for three active Australian charity-lottery products. H261 grants the player the impossible stronger condition of owning every issued ticket from inception, so every winning identifier is controlled.

Exact cheapest complete-issuance results:
- **Home Lottery:** 170,000 tickets; minimum acquisition **A$11,900,000**; stated total prize retail value **A$6,260,851.86**; return **52.6122%**, deficit **A$5,639,148.14**. Even double-counting the separately described A$87,986 Membership Draw gives only **53.3516%**.
- **Cash Calendar:** 146,888 tickets; minimum exact acquisition **A$1,346,485**; five guaranteed cash prizes total **A$400,000**; return **29.7070%**.
- **Holiday for Life:** 239,778 tickets; minimum exact acquisition **A$639,460**; immediate cash alternative **A$240,000**; return **37.5317%**.
- Combined impossible-perfect takeover: cost **A$13,885,945** vs prize value **A$6,900,851.86**, only **49.6967%** gross.

Thus these current hard-capped finite raffles validate the takeover mechanism structurally but decisively fail the economics even before real execution/eligibility/valuation friction.

Files:
- `research/h261_hospital_research_foundation_capped_raffle_buyout.md`
- `src/loto_research/h261_capped_raffle_buyout.py`
- `data/derived/h261_capped_raffle_buyout.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H261_APPEND.md`

### H262 — LOTTO 6/49 terminal Gold Ball takeover screen
Current WCLC rules make each Gold Ball identifier unique and draw the winner from all issued identifiers. After 29 consecutive white balls, the only remaining ball is gold and the jackpot arithmetic reaches **C$68,000,000**. If one player could own every issued identifier for that terminal draw, the Gold Ball prize itself would be deterministic and strict positive gross would hold for up to **22,666,666 paid C$3 plays**.

This is a genuine nonlinear lottery mechanism, but not yet executable as a strict guarantee: identifiers are computer-generated, public issuance remains open until cutoff, other players can create eligible entries, and Free Plays also receive Gold Ball entries. A single external eligible identifier preserves a legal outcome where our portfolio receives no Gold Ball prize.

Files:
- `research/h262_lotto649_final_gold_ball_takeover.md`
- `src/loto_research/h262_lotto649_gold_ball_takeover.py`
- `data/derived/h262_lotto649_gold_ball_takeover.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H262_APPEND.md`

### H264 — Uganda LOTTO fixed-tier / roll-down screen
Current Uganda National Lottery LOTTO rules v1.6 contain two fixed per-winning-entry lower tiers, but the special Division-1 roll-down explicitly excludes fixed payout divisions. Ordinary no-winner funds from Division 6 also roll into next-draw Division 1 rather than into fixed Division 7.

Exact one-copy `C(52,6)` cover arithmetic:
- 20,358,520 entries at UGX 1,000;
- total cost **UGX 20,358,520,000**;
- fixed Match-3 + Match-2+Bonus gross **UGX 3,689,400,000**;
- fixed-tier return **18.1221424740%**.

Thus H264 is closed for the target fixed-per-selection external-subsidy mechanism under current rules.

Files:
- `research/H264_VALIDATION.md`
- `research/h264_uganda_lotto_fixed_tier_rolldown.md`
- `src/loto_research/h264_uganda_lotto_fixed_tier_rolldown.py`
- `data/derived/h264_uganda_lotto_fixed_tier_rolldown.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H264_APPEND.md`

### H265 — NJ Pick-3 Green Ball terminal Double Draw bound
The July 6–August 3, 2026 Green Ball promotion used six white balls and one Green Ball. White balls were removed after selection; therefore after six consecutive white removals the next promotion result is deterministic and the same base Pick-3 wager receives a free second Pick-3 draw.

This is a real terminal/elimination mechanic, but exact current fixed-prize arithmetic closes it globally rather than only for one hand-picked cover. For a $0.50 base wager, Straight and Pair have 50% one-draw average return while 3-Way/6-Way Box have 48%. Two guaranteed base draws therefore cap primitive terminal averages at **100%** and **96%** respectively. Since `minimum legal-outcome gross <= average gross`, no nonnegative portfolio can guarantee gross strictly above cost. Straight/Box and Wheel are nonnegative decompositions and inherit the bound.

Adding FIREBALL does not help: it doubles cost, is excluded from Green Ball second-draw winner determination, and yields at most **77%** terminal average return on Straight/Pair (75% on Box). Instant Match has a legal nonwinning outcome and no positive worst-case floor.

The checked promotion is now over, and even its strongest known-terminal state cannot cross strict break-even. Reopen only on a future material payout/discount/promotion change that pushes the deterministic terminal average strictly above 100%.

Files:
- `research/h265_nj_pick3_green_ball_terminal_bound.md`
- `research/H265_VALIDATION.md`
- `src/loto_research/h265_nj_pick3_green_ball_bound.py`
- `data/derived/h265_nj_pick3_green_ball_bound.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H265_APPEND.md`

## NEXT ACTION
1. Search current forced-distribution/rolldown mechanics where externally accumulated money is paid as **fixed per-winning-selection** lower-tier prizes rather than shareable pools.
2. Search terminal/elimination lottery mechanics analogous to H262 **only where the eligible identifier set is hard-capped, player-selectable/reservable, or otherwise monopolizable before cutoff**; H262 shows the economics can cross 100% if execution can be certified.
3. For finite capped raffles, prioritize only products with unusually high prize-to-minimum-full-issuance-cost ratios or an external deterministic subsidy; H261 closes ordinary hard-cap charity-raffle buyouts at ratios <=52.6122%.
4. Search finite lottery identifiers/ticket pools where all eligible identifiers are player-selectable/reservable and total guaranteed cash exceeds complete acquisition cost.
5. For bonus-draw promotions, prioritize cases where maximum deterministic external subsidy divided by exact-cover cost materially exceeds H260's DAILY GRAND ratio.
6. Prioritize deterministic current payout boosts above exact coverage hurdles; random ticket-level Doubler/Tripler tags remain non-guaranteed because a legal no-tag branch exists.
7. Specifically reopen Green Ball/Double Draw style elimination promotions only if the known-terminal benefit exceeds H265's exact two-draw break-even ceiling: more than one guaranteed extra draw, higher fixed payouts, or a deterministic acquisition discount/subsidy.
8. Recheck H252 only when final official post-5-Sep Irish 6/45 rules are published or mechanics materially change.
9. For ordinary scratchers/instant tickets, reopen endgame-buyout only on execution-grade evidence of exact unsold purchasable inventory and prize content/bounds.
10. Reopen H249/H250 immediately on a current deterministic >50% effective subsidy crossing the exact formula after all fees/acquisition costs.
11. Continue lottery-only until SUCCESS or EXHAUSTED.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
Latest numbered lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H265_APPEND.md`.
Exact-family ledger: `research/H225_EXACT_STATUS.md`.
Exact-family terminal validation: `research/H225_X19_X20_VALIDATION.md`.
