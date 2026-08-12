# STATUS

Updated: 2026-08-12
Branch: `research-work`

## Current stage
**Stage 1 — exact baselines, rule-versioning and structural-edge search**

## Safe checkpoint
This file is the authoritative handoff point. Long research passes must checkpoint frequently; the latest 4+4 category-II and Telegram jackpot findings are included below.

## Foundation / code
- `START_HERE.md`, `PROJECT_RULES.md`, `AGENTS.md`, `RESEARCH_PLAN.md` define handoff and research standards.
- `catalog/games.csv`, `catalog/sources.csv`, `schemas/DATA_MODEL.md` define the first research universe and data model.
- `research/HYPOTHESES.md` contains H001–H016.
- `src/loto_research/probability.py` contains exact combinatorial probability/EV helpers.
- `src/loto_research/collectors/azerbaijan.py` validates/normalizes Azerbaijan draw records.
- `src/loto_research/uk_lotto.py` separates old/current UK Lotto regimes and includes Must-Be-Won screening helpers.
- `src/loto_research/four_plus_four.py` reconstructs the Azerbaijan 4+4 common pool unit, V/VI coupling and independent volume estimates from tail winners.
- `src/loto_research/pari_mutuel.py` contains exact pari-mutuel expected-share helpers for state-dependent pool modelling.
- regression tests exist for probability, Azerbaijan collectors, UK Lotto and 4+4 empirical identities.
- GitHub Actions remains disabled; important arithmetic identities were independently recomputed during research.

## Historically validated mechanism
### Cash WinFall
A preserved May 9, 2011 roll-down gives, using exact 6/46 probabilities and cash-only tiers:
- ticket: $2;
- expected payout: **$2.2137120403**;
- expected ROI: **+10.6856%** before tax/execution costs.

Conclusion: structural +EV lotteries have existed without any need to predict draw numbers.

## Azerbaijan baselines
### Beşdə 5
- exact 5/5 odds: **1 in 376,992**;
- favorable baseline gross payout: **0.535555131 AZN per 1-AZN variant**;
- baseline net before tax/sharing: about **-46.44%**.

### Super Keno
- displayed base-table gross EV: **0.598555794 AZN per 1 AZN**;
- baseline net before tax: about **-40.14%**;
- multiplier economics remain pending.

## Azerbaijan 4+4 — current top local target
### Exact mechanics
- two independent 4/20 boards;
- 11 grouped winning categories;
- jackpot odds: **1 in 23,474,025**;
- probability of any listed winning state: **18.614724%** (~1 in 5.3721);
- official public ticket price: **2 AZN**;
- direct primary wording for the cost of one base variant is still missing.

### Strongly reconstructed lower-tier engine
Seven preserved 2026 payout tables are stored in:
- `data/historical/az_4plus4_payout_samples_2026.csv`

For ordinary sampled draws, a common draw-level unit `U` explains the variable pools:
- III = **11U**
- IV = **5U**
- VII = **9U**
- VIII = **14U**
- IX = **7U**
- V + VI = **2U**

Thus III–IX jointly distribute approximately **48U**.

Draw #790 was added after the pattern was inferred and independently fits it closely, giving a first out-of-sample confirmation.

### V/VI coupling
Empirical rule across the current sample:
- if V winners <= VI winners, pools are approximately U/U;
- if V winners > VI winners, their combined 2U is reallocated so that per-winner V payout is about 1.5× per-winner VI payout.

Zero-winner V/VI cases must still be observed; do not extrapolate the rule there.

### Independent scale validation
Using exact X/XI probabilities and their observed fixed prizes (X=6 AZN, XI=4 AZN), winner counts provide an independent volume estimator.

Across seven sampled draws:
- mean `U/N_hat` ≈ **0.00996205**;
- median ≈ **0.00995043**;
- range ≈ **0.00953821–0.01050994**.

Therefore `U ≈ 0.01 × sold_variants` emerges from data rather than from a chosen round number.

If one base variant costs 2 AZN, one U corresponds to roughly 0.5% of gross sales. This makes **2 AZN per base variant a high-confidence inference**, but not yet a primary-source fact.

### Ordinary economic subtotal
- X/XI exact expected payout: **0.682149737849 AZN / variant**;
- III–IX under empirical scale: about **0.48 AZN / variant**;
- subtotal before category II and jackpot: **~1.16215 AZN per assumed 2-AZN variant** (~58.11% gross return).

So ordinary lower-tier variation is mostly a stable pool formula divided among changing winner counts, not a free edge.

## Azerbaijan 4+4 — corrected jackpot chronology
A previous pass incorrectly treated a migrated website date as the event date for the 530,359-AZN jackpot win.

Correct primary-source chronology:
- **08.07.2023:** 530,359 AZN jackpot won, draw 23276;
- next jackpot stated as **250,000 AZN** for that 2023 rule era.

Do NOT use this as a July-2026 reset.

Current accumulation checkpoints are stored in:
- `data/historical/az_4plus4_jackpot_checkpoints.csv`
- `data/historical/az_4plus4_telegram_checkpoints.csv`

Official site lower-bound checkpoints:
- **15.01.2025:** >500k AZN;
- **19.08.2025:** >800k AZN;
- **26.11.2025:** >1m AZN;
- **26.01.2026:** >1.3m AZN;
- **10.06.2026:** >1.8m AZN in current 4+4/draw-game context.

Official Telegram message ordering adds denser intermediate states:
- message **2335:** jackpot >1.2m AZN;
- message **2344:** jackpot >1.4m AZN;
- message **2353:** jackpot >1.5m AZN and Nizami Tağıyev winner story.

The exact calendar dates for 2335/2344 remain unrecovered. Message 2353 is linked to the Nizami event dated **2026-06-02** by the official winner page; the secondary archive independently places draw **#780** on 2026-06-02.

No jackpot win between the current accumulation checkpoints has yet been established in the captured sources.

### External transfers are real
On 06.01.2025 Azərlotereya officially announced that if the final Meqa 5/36 jackpot was not won, its jackpot would be added to 4+4.

The outcome and exact transferred amount are still unresolved.

Therefore 4+4 jackpot accounting must allow:

`J_t = prior_jackpot + ordinary_4+4_contributions + zero-winner/carryover_transfers + external_transfers - payouts/adjustments`

Do not fit all 2025 jackpot growth to organic 4+4 sales.

## NEW — category II primary-source lead
File:
- `research/4plus4_category2_lead.md`

Official Azərlotereya says **Nizami Tağıyev missed the 4+4 jackpot by only one number and won 8,609 AZN** while jackpot was >1.5m.

For one ordinary variant, one number short of 4+4 means a **4+3 or 3+4** state, i.e. category II. Therefore the ticket definitely appears to contain at least one category-II winning variant.

Important caveat: the game supports 5+5/6+6 combination tickets and one ticket may win several variants/categories. **Do not yet set category-II per-winner payout = 8,609 AZN.** The 8,609 may be aggregate ticket payout.

Decisive next check:
- recover draw #780 full payout table and determine category-II winner count/prize;
- if exactly one category-II winner received 8,609 AZN, category II becomes directly observed and can be integrated into full EV.

## H014 — Azerbaijan zero-winner carryover
This remains **testing** and is still the key local structural question.

Accessible 2026 secondary tables repeatedly show zero winners in rare category II, but do not expose its assigned pre-draw pool.

Required test:
1. identify a zero-winner variable category;
2. infer its ordinary assigned amount from the U-engine where possible;
3. obtain adjacent jackpot/category states;
4. check whether the missing amount appears in the next jackpot/category balance after controlling for normal contributions and external transfers;
5. require the state to be observable before purchase.

Only then does a forward EV trigger exist.

## Kazakhstan 4/20 — validated modern control mechanism
Kazakhstan 4/20 was studied only as a comparator because it uses the same two-board 4/20 combinatorics but exposes more state information. **Do not transfer its rules to Azerbaijan without proof.**

Files:
- `research/kazakhstan_4x20_control.md`
- `data/historical/kz_4x20_transition_samples.csv`
- `src/loto_research/pari_mutuel.py`

### Exact replicated state-transition identity
Three independent consecutive-draw transitions reproduce the same accounting rule exactly.

Example 1545 -> 1546:
- previous superprize: **226,866,699 KZT**;
- zero-winner lower pools in 1545: **99,432 + 149,148 = 248,580 KZT**;
- ordinary current-draw 3% contribution: **132,678 KZT**;
- next superprize: **227,247,957 KZT**.

Identity:

`226,866,699 + 248,580 + 132,678 = 227,247,957`

exactly.

Two additional transitions also close exactly:
- 1499 -> 1500: jackpot growth = unpaid III+V + current 3% contribution;
- 1500 -> 1501: jackpot growth = unpaid II + current 3% contribution.

Conclusion: a **modern active zero-winner-lower-pool -> next-superprize transfer mechanism is empirically validated** in this comparator.

### Kazakhstan economic screen
For sampled draw 1546, a static uniform-selection screen gives approximately:
- lower-category immediate EV: **155.43 KZT**;
- superprize component: **9.68 KZT**;
- total immediate EV: **~165.10 KZT per 300 KZT** (~55.03% gross return);
- simple break-even superprize: **~3.395 billion KZT**, versus observed ~227m.

So the mechanism is real, but the sampled state is nowhere near +EV.

## UK Lotto
H016 Wednesday Must Be Won was stress-tested and downgraded:
- initial demand cushion ~+33.77%;
- seven historical analogues show median uplift ~+42.85%;
- six of seven exceed the cushion;
- status: **inconclusive / materially weakened**.

H015 crowd-choice/sharing remains theoretically interesting but unquantified.

## Current blockers
- official Azərlotereya archive pages are client-rendered;
- underlying historical API/network payload remains undiscovered;
- exact adjacent 4+4 jackpot values are not yet available from the current source set;
- January-2025 external-transfer amount remains unknown;
- draw #780 full payout table remains unrecovered;
- category-II pure per-winner payout remains unresolved;
- secondary draw data require primary reconciliation.

## Next actions
1. Recover **draw #780** full payout table; test whether Nizami's 8,609 AZN is pure category-II payout or aggregate system-ticket payout.
2. Continue searching for exact adjacent Azerbaijan 4+4 jackpot values and test the Kazakhstan-style accounting signature.
3. Expand Azerbaijan 4+4 history toward 50–100 consecutive draws, prioritizing zero-winner II–VI states.
4. Discover the official Azərlotereya archive API/payload.
5. Resolve the final Meqa 5/36 draw outcome and exact January-2025 external transfer amount.
6. Confirm base-variant price directly from primary rules/purchase flow/receipt.
7. Build a forward state-EV trigger only after the balance equation is validated.
8. Then return to H015, Super Keno multipliers, scratch/instant inventory edges and major progressive jackpots.

## Work-session rule
For future long research passes, checkpoint to GitHub frequently rather than accumulating a large unsaved reasoning chain. After every meaningful discovery or roughly every 2–4 research substeps:
- save raw/derived data first;
- update the relevant research note;
- update this `STATUS.md` when the strategic conclusion changes.

A future chat should read `START_HERE.md`, `PROJECT_RULES.md`, this file, `RESEARCH_PLAN.md`, and `AGENTS.md`, then verify the factual branch state before continuing.
