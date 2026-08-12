# STATUS

Updated: 2026-08-12
Branch: `research-work`

## Current stage
**Stage 1 — exact baselines, rule-versioning and structural-edge search**

## Safe checkpoint
This is the authoritative handoff point. Research now runs in short packets: after every meaningful discovery or roughly 2–4 research substeps, save raw/derived data, update the research note, then update this file if the strategic conclusion changed.

## Foundation / code
- `START_HERE.md`, `PROJECT_RULES.md`, `AGENTS.md`, `RESEARCH_PLAN.md` define handoff and research standards.
- `catalog/games.csv`, `catalog/sources.csv`, `schemas/DATA_MODEL.md` define the research universe and data model.
- `research/HYPOTHESES.md` contains H001–H016.
- `src/loto_research/probability.py`: exact combinatorics/EV.
- `src/loto_research/collectors/azerbaijan.py`: Azerbaijan normalization/validation.
- `src/loto_research/four_plus_four.py`: Azerbaijan 4+4 common-pool reconstruction and V/VI coupling.
- `src/loto_research/pari_mutuel.py`: exact shared-pool expected-share helpers.
- `src/loto_research/uk_lotto.py`: UK Lotto regime-specific Must-Be-Won work.
- regression tests exist for probability, Azerbaijan collectors, UK Lotto and 4+4 empirical identities.
- GitHub Actions remains disabled; critical arithmetic has been independently recomputed during research.

## Historically validated mechanism
### Cash WinFall
A preserved May 9, 2011 roll-down gives, using exact 6/46 probabilities and cash-only tiers:
- ticket: $2;
- expected payout: **$2.2137120403**;
- expected ROI: **+10.6856%** before tax/execution costs.

Conclusion: structural +EV lotteries have existed without predicting draw numbers.

## Azerbaijan baselines
### Beşdə 5
- exact 5/5 odds: **1 in 376,992**;
- favorable gross payout baseline: **0.535555131 AZN per 1-AZN variant**;
- net baseline before tax/sharing: about **-46.44%**.

### Super Keno
- displayed base-table gross EV: **0.598555794 AZN per 1 AZN**;
- baseline net before tax: about **-40.14%**;
- multiplier economics remain pending.

## Azerbaijan 4+4 — current top local target
### Exact mechanics
- two independent 4/20 boards;
- 11 grouped winning categories;
- jackpot odds: **1 in 23,474,025**;
- any listed winning-state probability: **18.614724%** (~1 in 5.3721);
- official public ticket price: **2 AZN**;
- direct primary wording for the price of one base variant is still missing.

### Strongly reconstructed ordinary pool engine
Seven preserved 2026 payout tables:
- `data/historical/az_4plus4_payout_samples_2026.csv`

For ordinary sampled draws, a common unit `U` explains variable pools:
- III = **11U**
- IV = **5U**
- VII = **9U**
- VIII = **14U**
- IX = **7U**
- V + VI = **2U**

Thus III–IX jointly distribute approximately **48U**.

Draw #790 was added after the pattern was inferred and independently fits it closely, giving a first out-of-sample confirmation.

### V/VI coupling
Empirical rule across current sample:
- if V winners <= VI winners, pools are approximately U/U;
- if V winners > VI winners, combined 2U is reallocated so per-winner V payout is about 1.5× per-winner VI payout.

Zero-winner V/VI cases are not extrapolated.

### Independent U scale validation
Using exact X/XI probabilities and observed fixed prizes (X=6 AZN, XI=4 AZN), tail-winner counts give independent volume estimates.

Across seven sampled draws:
- mean `U/N_hat` ≈ **0.00996205**;
- median ≈ **0.00995043**;
- range ≈ **0.00953821–0.01050994**.

Therefore `U ≈ 0.01 × sold_variants` emerges from data. If one base variant costs 2 AZN, one U corresponds to roughly 0.5% of gross sales. This makes 2 AZN per base variant a high-confidence inference, not yet a direct primary-rule fact.

### NEW — primary operator winner stories cross-check the U-engine
Data:
- `data/historical/az_4plus4_official_winner_crosschecks.csv`
- `research/4plus4_economics_inference.md`

Official Azərlotereya stories provide two direct **4+2** winners, corresponding to category III. The empirical engine says category III = 11U:
- Samir İmaməliyev: **4+2, 4,503 AZN** -> `4503/11 = 409.36`;
- Orxan Həsənov: **4+2, 4,381 AZN** -> `4381/11 = 398.27`.

These implied U values sit in the same ~400–430 AZN band as the reconstructed 2026 payout tables (e.g. draw #790 U≈417.6, draw #781 U≈418.2).

Conclusion: the U-engine is no longer supported only by a secondary archive; **independent primary operator winner stories reproduce the category-III scale.** This materially raises confidence in the empirical payout reconstruction.

Caveat: winner stories report ticket-level winnings and system tickets can create multiple variants. Treat the observations as high-value cross-checks, not yet as complete rule documentation.

### Ordinary economic subtotal
- X/XI exact expected payout: **0.682149737849 AZN / variant**;
- III–IX under empirical scale: about **0.48 AZN / variant**;
- subtotal before category II and jackpot: **~1.16215 AZN per assumed 2-AZN variant** (~58.11% gross return).

Ordinary payout variation is therefore mostly stable pool accounting divided among changing winner counts, not a free edge.

## Category II — strongest new unresolved lead
Files:
- `research/4plus4_category2_lead.md`
- `data/historical/az_4plus4_official_winner_crosschecks.csv`

Exact category II (`4+3 / 3+4`) probability:
- **0.000005452835634281** ≈ **1 in 183,390.82** per base variant.

Two official Azərlotereya winner stories say the player missed the jackpot by one number, proving each ticket contained at least one category-II winning variant:
- Nizami Tağıyev: **8,609 AZN**, jackpot >1.5m; official winner page links event to **2026-06-02**, working draw **#780**;
- Ümüd Hüseynov: **15,986 AZN**, jackpot >1.8m; exact draw/date not yet recovered.

### NEW ~20U working hypothesis
The amounts produce a striking same-scale pattern:
- `8,609 / 20 = 430.45`;
- `15,986 / 40 = 399.65`.

Both are on the same U scale as the direct category-III cross-checks.

Working hypothesis only:
- ordinary category-II pool may be approximately **20U**;
- Nizami could represent one ~20U category-II variant;
- Ümüd could represent two ~20U category-II variants or another system-ticket aggregate.

**Do not promote 20U to a rule yet.** 5+5/6+6 system tickets can generate multiple winning variants, and category II may itself be state-dependent.

If 20U is eventually confirmed and `U/N≈0.01`, the sales-funded category-II pool would represent roughly **0.20 AZN per sold variant** in aggregate. Because category II is rare, however, many draws have zero winners; the destination of the unpaid pool remains decisive for immediate EV and carryover.

Decisive evidence needed:
1. full payout table for draw #780;
2. exact Ümüd draw and payout table;
3. original ticket/system structure for either winner;
4. another one-number-short winner with known ticket structure;
5. detailed registered rules stating category-II allocation.

## Azerbaijan 4+4 — corrected jackpot chronology
A previous pass incorrectly treated migrated website metadata as the event date for a historical jackpot.

Correct primary chronology:
- **08.07.2023:** 530,359 AZN jackpot won, draw 23276;
- next jackpot stated as **250,000 AZN** for that 2023 rule era.

Do NOT use this as a July-2026 reset.

Current accumulation files:
- `data/historical/az_4plus4_jackpot_checkpoints.csv`
- `data/historical/az_4plus4_telegram_checkpoints.csv`

Official site lower-bound checkpoints:
- **15.01.2025:** >500k AZN;
- **19.08.2025:** >800k AZN;
- **26.11.2025:** >1m AZN;
- **26.01.2026:** >1.3m AZN;
- **10.06.2026:** >1.8m AZN in current draw-game/4+4 context.

Official Telegram ordering adds:
- message 2335: >1.2m;
- message 2344: >1.4m;
- message 2353: >1.5m, Nizami story;
- message 2516: >1.8m, Ümüd story;
- message 2490: Samir 4+2 / 4,503 AZN;
- message 2529: Orxan 4+2 / 4,381 AZN.

Exact dates of several Telegram messages remain unrecovered.

### External transfers are real
On 06.01.2025 Azərlotereya announced that if the final Meqa 5/36 jackpot was not won, its jackpot would be added to 4+4. Outcome and exact transferred amount remain unresolved.

Therefore jackpot accounting must allow:

`J_t = prior_jackpot + ordinary_4+4_contributions + zero-winner/carryover_transfers + external_transfers - payouts/adjustments`

Do not fit all 2025 jackpot growth to organic 4+4 sales.

## H014 — Azerbaijan zero-winner carryover
Status: **testing**; still the key structural question.

Accessible 2026 tables repeatedly show zero winners in rare category II but do not expose its assigned pre-draw pool.

Required test:
1. identify a zero-winner variable category;
2. infer ordinary assigned amount from U where possible;
3. obtain adjacent jackpot/category states;
4. check whether the missing amount appears in the next balance after controlling for normal contributions and external transfers;
5. require the state to be observable before purchase.

Only then does a forward EV trigger exist.

## Kazakhstan 4/20 — validated modern comparator
Do **not** transfer Kazakhstan rules to Azerbaijan. It is used only because the same two-board 4/20 combinatorics expose more state information.

Files:
- `research/kazakhstan_4x20_control.md`
- `data/historical/kz_4x20_transition_samples.csv`
- `src/loto_research/pari_mutuel.py`

Three independent consecutive-draw transitions reproduce the same accounting rule exactly: zero-winner lower-category pools move into the next superprize together with the ordinary contribution.

Example 1545 -> 1546:
`226,866,699 + 248,580 + 132,678 = 227,247,957` exactly.

Economic screen for sampled draw 1546:
- total immediate EV ≈ **165.10 KZT per 300 KZT** (~55.03%);
- simple break-even superprize ≈ **3.395bn KZT** vs observed ~227m.

Thus the modern transfer mechanism is real, but sampled state is nowhere near +EV. It gives a concrete accounting signature to search for in Azerbaijan.

## UK Lotto
H016 Wednesday Must Be Won was stress-tested and downgraded:
- initial demand cushion ~+33.77%;
- seven historical analogues median uplift ~+42.85%;
- six of seven exceed cushion;
- status: **inconclusive / materially weakened**.

H015 crowd-choice/sharing remains theoretically interesting but unquantified.

## Current blockers
- Azərlotereya historical archive is client-rendered; underlying API/network payload remains undiscovered;
- draw #780 full payout table remains unrecovered;
- Ümüd exact draw/date remains unrecovered;
- exact adjacent 4+4 jackpot values remain unavailable;
- January-2025 external-transfer amount remains unknown;
- direct primary base-variant price statement remains missing;
- category-II 20U hypothesis remains unvalidated;
- secondary draw data require primary reconciliation.

## Next actions
1. Recover **draw #780** full payout table and test the ~20U category-II hypothesis.
2. Recover Ümüd's exact draw/date and determine whether 15,986 AZN reflects two category-II variants/system play.
3. Find another official category-II / one-number-short winner or detailed rule document.
4. Continue exact adjacent-jackpot search and test Kazakhstan-style state accounting in Azerbaijan.
5. Expand 4+4 history toward 50–100 consecutive draws, prioritizing zero-winner II–VI states.
6. Discover the official Azərlotereya archive API/payload.
7. Resolve final Meqa 5/36 outcome / January-2025 external transfer amount.
8. Confirm base-variant price directly.
9. Build forward state-EV trigger only after balance equation and category II are validated.
10. Then return to H015, Super Keno multipliers, scratch/instant inventory edges and major progressive jackpots.

## Work-session rule
Checkpoint frequently. Never accumulate a large unsaved research chain. After every meaningful discovery or roughly every 2–4 substeps:
- save raw/derived data first;
- update the research note;
- update this STATUS if the strategic conclusion changes.

A future chat should read `START_HERE.md`, `PROJECT_RULES.md`, this file, `RESEARCH_PLAN.md`, and `AGENTS.md`, then verify the factual branch state before continuing.
