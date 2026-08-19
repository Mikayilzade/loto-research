# STATUS

Updated: 2026-08-19
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is preserved for history but is OUT OF SCOPE and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Current lottery stage
**Structural/state-edge search + scratch exact-pack/inventory search + Azerbaijan 4+4 carryover + RNG/bias + deterministic lottery promotions.**

### Strong validated historical controls
- Cash WinFall rolldown: historical positive-EV mechanism validated (~+10.69% conservative pre-tax sample ROI), but not a current guaranteed-profit route.
- Kazakhstan 4/20: zero-winner lower-category pools feeding next superprize validated on multiple transitions; sampled state still negative.
- Lotto Texas 2023 / H108: organized syndicate operationally acquired virtually all 25.8m combinations and guaranteed possession of the jackpot-winning line. Actual draw had one jackpot winner and was strongly profitable. Strict all-outcome guaranteed-profit theorem fails because external duplicate jackpot winners were not hard-capped. Texas now legally prohibits retailers knowingly facilitating all/substantially-all combination purchases.

### H109 — unique-number raffle takeover class
- Unique raffle/GPD numbers remove duplicate-winner sharing but do not by themselves create a buy-the-pot guarantee.
- Fixed finite unique-ticket supply requires total guaranteed cash prizes `P > N*c + all costs`.
- Irish Christmas Millionaire Raffle control: 600,000 × €25 = €15m spend vs €6.3425m guaranteed prizes = **42.2833%** deterministic gross.
- Canada LOTTO 6/49 Gold Ball remains externally issued; any external entry leaves a branch where our Gold Ball payout is zero.

Status: **H109 materially closed for strict guarantee / NO SUCCESS**.
File: `research/h109_unique_issued_raffle_takeover.md`.

### H110 — Texas scratch closing-inventory bound
Texas provides unusually rich official scratch closing reports: percent sold, pack inventory categories and total outstanding prize liability. This allows a much stronger remaining-state screen than ordinary “top prizes remaining” pages.

Three closing-state controls were tested using the deliberately buyer-favorable assumption that **every outstanding prize dollar is still inside unsold purchasable inventory**:
- X #2590: estimated unsold face cost **$114.867m** vs outstanding liability **$89.883m** → ceiling **78.2494%**.
- Crazy 8s #2656: **$9.052m** cost vs **$6.342m** liability → ceiling **70.0595%**; sealed-pack guaranteed floor **49.6%**.
- Lucky No. 7 #2622: **$6.621m** cost vs **$5.059m** liability → ceiling **76.4089%**; sealed-pack guaranteed floor **55.6%**.

Because outstanding liability also includes prizes on tickets already sold but not yet claimed, actual prize value in unsold inventory is no greater than these ceilings. The percent-sold figure is operator-estimated from pack settlements, so this is a strong rejection screen rather than an exact inventory theorem; all three deficits are nevertheless large.

Status: **H110 TEXAS PUBLIC CLOSING-STATE SCRATCH ROUTE MATERIALLY CLOSED / NO SUCCESS**.
Files:
- `research/h110_texas_scratch_closing_inventory_bound.md`
- `data/derived/h110_texas_scratch_closing_screen.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H110_APPEND.md`

### H111 — fixed sealed-pack guarantee + retailer commission
H111 tested a stronger exact-denominator scratch route: Texas publishes a **guaranteed total prize amount per sealed pack**. Seven pack structures were screened, then the full current 5% Texas retailer sales commission was deliberately granted to the buyer as if it were a deterministic rebate.

Sampled pack guaranteed returns before commission: **40.0%–62.5%** of face value.
After granting the full 5% commission: **45.0%–67.5%**.
Best sampled case, X #2590:
- pack face = $1,000;
- guaranteed pack prizes = $625;
- favorable 5% commission = $50;
- strict recovered floor = **$675 = 67.5%**;
- guaranteed deficit = **$325** before any other costs.

This rejection does not require resolving whether self-purchase commission capture is permitted: the calculation already grants the entire commission in the buyer's favor. Conditional retailer winner bonuses have zero worst-case value and discretionary incentives cannot support a strict floor.

General consequence: a Texas-style fixed pack would need a deterministic external subsidy of roughly **37.5%–60% of face** merely to reach break-even in the sampled set. Ordinary 5–10% retailer commissions/discounts cannot create a guarantee unless another jurisdiction has a pack floor already near 90–95%.

Status: **H111 FIXED-PACK + ORDINARY RETAILER-COMMISSION ROUTE MATERIALLY CLOSED / NO SUCCESS**.
Files:
- `research/h111_texas_scratch_pack_commission_floor.md`
- `data/derived/h111_texas_scratch_pack_commission_floor.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H111_APPEND.md`

### Azerbaijan live branches
- 4+4: combinatorics + payout-unit engine strongly reconstructed; category II/carryover remains data-blocked and high priority.
- Poz-Qazan scratch: ordinary initial states negative; remaining-prize conditional edge remains data-blocked because exact live unsold denominator/registration state is unavailable. H110 strengthens the requirement not to infer edge from remaining-prize counts alone.
- Beşdə 5 / Super Keno / ONLOTO: ordinary/full-space screens negative; no guarantee found.

### Global lottery branches already screened
- Powerball / Mega Millions / EuroMillions: jackpot thresholds and full-space economics quantified; strict guarantee blocked by cost/sharing/caps and/or current rules.
- UK Lotto Must Be Won: sampled current states negative after sales-response stress; historical Cash WinFall-style mechanism remains proof that rolldown edge can exist.
- Multiple finite fixed-prize games: full-space deterministic returns below cost.
- H015 anti-crowd/unpopular-number selection: useful EV/share optimizer only; not standalone guarantee.
- Additive wheels/partial covering: strict all-outcome positive guarantee impossible when constituent tickets are all nonpositive-EV and payoff/cost remain linear.
- H109 fixed/dynamic unique-number raffles: fixed supply fails prize-pool hurdle in tested recurring control; dynamic issued-number games fail ownership lock when external entries exist.
- H110 ordinary remaining-prize scratch ranking: materially closed unless exact unsold inventory/prize mapping or deterministic pack subsidy exists.
- H111 Texas-style sealed-pack guarantees: exact pack floor exists, but ordinary retailer commission is far too small to bridge the pack takeout.

## NEXT ACTION
1. **Cross-jurisdiction fixed-pack search after H111:** only pursue jurisdictions where sealed-book/pack minimum payout is published and unusually high, or where a deterministic lottery-specific discount/rebate exceeds the exact break-even subsidy hurdle. Do not repeat ordinary 5% retailer-commission overlays.
2. **Global buy-the-pot search:** reopen only where fixed/capped eligible supply can legally be acquired in full AND total guaranteed cash/external subsidy exceeds acquisition cost.
3. **4+4 Azerbaijan H014:** continue category-II/carryover reconstruction and exact per-variant pricing/pool state.
4. **RNG/physical bias H007:** collect high-frequency games/draw hardware or RNG data where persistent bias can be tested out-of-sample.
5. **Lottery promotions:** deterministic rebates/discounts/second-chance only where they can alter worst-case cash floor.
6. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master: `research/CHECKED_PROJECTS_AND_TESTS.md` plus connector-safe authoritative append files.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H111_APPEND.md`.
Latest case: `research/h111_texas_scratch_pack_commission_floor.md`.
