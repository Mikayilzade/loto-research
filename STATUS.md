# STATUS

Updated: 2026-08-12
Branch: `research-work`

## Current stage
**Stage 1 — exact baselines, rule-versioning and structural-edge search**

## Work-session rule
Research runs in short packets. After every meaningful discovery or roughly 2–4 substeps:
1. save raw/derived data;
2. update the relevant research note;
3. update this file when the strategic conclusion changes.

This file is the authoritative handoff checkpoint.

## Foundation / code
- `START_HERE.md`, `PROJECT_RULES.md`, `AGENTS.md`, `RESEARCH_PLAN.md`
- `catalog/games.csv`, `catalog/sources.csv`, `schemas/DATA_MODEL.md`
- `research/HYPOTHESES.md`
- `src/loto_research/probability.py`
- `src/loto_research/collectors/azerbaijan.py`
- `src/loto_research/four_plus_four.py`
- `src/loto_research/pari_mutuel.py`
- `src/loto_research/uk_lotto.py`
- regression tests for probability, Azerbaijan collectors, UK Lotto and 4+4 empirical identities
- GitHub Actions remains disabled.

## Historically validated mechanism — Cash WinFall
A preserved May 9, 2011 roll-down gives, using exact 6/46 probabilities and cash-only tiers:
- ticket $2;
- expected payout **$2.2137120403**;
- expected ROI **+10.6856%** before tax/execution.

Conclusion: structural +EV lotteries have existed without predicting draw numbers.

## Azerbaijan baselines
### Beşdə 5
- exact 5/5 odds: **1 in 376,992**;
- favorable gross baseline: **0.535555131 AZN per 1-AZN variant**;
- net baseline before tax/sharing: about **-46.44%**.

### Super Keno
- displayed base-table gross EV: **0.598555794 AZN per 1 AZN**;
- net baseline before tax: about **-40.14%**;
- multiplier economics remain pending.

# Azerbaijan 4+4 — current top local target

## Exact mechanics
Current primary operator page:
- two independent 4/20 boards;
- balls returned between A and B draw;
- 11 grouped winning categories;
- jackpot odds: **1 in 23,474,025**;
- any listed winning-state probability: **18.614724%** (~1 in 5.3721);
- public ticket price: **2 AZN**;
- registered no. **336 / 17.01.2021**, validity through 31.12.2027;
- current 5+5 / 6+6 system tickets create multiple variants and can win across multiple categories;
- current schedule: **Tuesday / Friday 19:45**.

Direct primary wording for the price of one base variant remains missing. **2 AZN/base variant is a high-confidence empirical inference, not yet a direct rule statement.**

## Strongly reconstructed ordinary pool engine
Data:
- `data/historical/az_4plus4_payout_samples_2026.csv`
- `data/derived/az_4plus4_pool_unit_validation.csv`
- `research/4plus4_economics_inference.md`

For ordinary sampled draws, define common unit `U`:
- III = **11U**
- IV = **5U**
- VII = **9U**
- VIII = **14U**
- IX = **7U**
- V + VI = **2U**

Thus III–IX jointly distribute approximately **48U**.

Draw #790 was added after the pattern was inferred and independently fits it closely (U≈417.6), giving a first out-of-sample confirmation.

### V/VI coupling
Empirical rule:
- if V winners <= VI winners, pools are approximately U/U;
- if V winners > VI winners, combined 2U is redistributed so per-winner V ≈ 1.5× per-winner VI.

Zero-winner V/VI cases are not extrapolated.

### Independent U scale
Using exact X/XI probabilities and observed fixed prizes X=6 AZN, XI=4 AZN, tail winner counts independently estimate sold variants.

Across seven sampled draws:
- mean `U/N_hat` ≈ **0.00996205**;
- median ≈ **0.00995043**;
- range ≈ **0.00953821–0.01050994**.

Therefore `U ≈ 0.01 × sold_variants` emerges from data. If a base variant costs 2 AZN, U is roughly 0.5% of gross sales.

### Primary winner-story cross-check
Official operator stories independently reproduce the category-III scale:
- Samir İmaməliyev: `4+2`, **4,503 AZN** -> `4503/11 = 409.36`;
- Orxan Həsənov: `4+2`, **4,381 AZN** -> `4381/11 = 398.27`.

These lie on the same U scale as the reconstructed 2026 draw tables. The U-engine is therefore no longer supported only by secondary archives.

### Ordinary economic subtotal
- X/XI exact expected payout: **0.682149737849 AZN / variant**;
- III–IX under empirical scale: about **0.48 AZN / variant**;
- subtotal before category II and jackpot: **~1.16215 AZN per assumed 2-AZN variant** (~58.11% gross return).

Ordinary state remains strongly negative.

# Category II — strongest unresolved lead
Files:
- `research/4plus4_category2_lead.md`
- `data/historical/az_4plus4_official_winner_crosschecks.csv`
- `data/derived/az_4plus4_category2_carryover_screen.csv`

Exact category II (`4+3 / 3+4`) probability:
- **0.000005452835634281** ≈ **1 in 183,390.82** per base variant.

Three primary one-number-short tickets:
- **Vəzir Quliyev:** 10,287 AZN, official date 2025-09-19;
- **Nizami Tağıyev:** 8,609 AZN, official date 2026-06-02 / working draw #780;
- **Ümüd Hüseynov:** 15,986 AZN, jackpot >1.8m; exact date/draw still unresolved.

“One number short” establishes at least one category-II variant on each ticket, but reported ticket payout can aggregate multiple system variants/categories.

## ~20U working hypothesis
Normalization:
- Vəzir: `10,287 / 20 = 514.35`;
- Nizami: `8,609 / 20 = 430.45`;
- Ümüd: `15,986 / 40 = 399.65`.

Working hypothesis only:
- ordinary II may be about **20U**;
- Nizami/Vəzir may each contain one ~20U component;
- Ümüd may contain two ~20U components or a larger state-dependent amount.

Do **not** promote II=20U to a rule yet.

### Competing explanations for Ümüd
1. **System-ticket aggregation** — explicitly plausible because the official page confirms 5+5/6+6 tickets can create multiple winning variants/categories.
2. **Category-II carryover/state** — an ordinary ~20U current pool plus accumulated zero-winner money.
3. Other aggregation/hierarchy/reporting rules.

## NEW — conditional category-II carryover scale screen
This tests whether the proposed carryover mechanism is large enough to matter; it does **not** prove the transfer rule.

Assume:
- II = 20U;
- U = 0.01N;
- N roughly 38k–50k variants;
- a zero-winner II pool is retained/transferred intact.

Then:
- P(no II winner) ≈ **81.3% at N=38k** down to **76.1% at N=50k**;
- assumed II pool ≈ **7,600–10,000 AZN**;
- expected unpaid amount ≈ **6,178–7,614 AZN per draw**.

At the current Tue/Fri cadence (~104 draws/year), that is roughly **0.64m–0.79m AZN/year** *if* the full assumed zero-winner II pool transfers forward.

Interpretation: **the carryover idea survives an order-of-magnitude test.** It is large enough to contribute materially to a million-AZN jackpot over a long cycle. This is a plausibility result only; actual destination of the unpaid pool remains unknown and external cross-game transfers also exist.

# H014 — zero-winner state edge
Status: **testing**.

Required proof sequence:
1. infer ordinary assigned pool for a zero-winner variable category;
2. obtain adjacent jackpot/category states;
3. show the missing amount in the next balance after normal contributions/external transfers;
4. repeat across multiple transitions;
5. require the state to be observable before purchase.

Only then build a forward EV trigger.

# Kazakhstan 4/20 comparator
Do **not** transfer Kazakhstan rules to Azerbaijan. It is a methodological comparator using the same two-board 4/20 combinatorics.

Files:
- `research/kazakhstan_4x20_control.md`
- `data/historical/kz_4x20_transition_samples.csv`

Three independent transitions reproduce exactly:
`next superprize = previous superprize + unpaid zero-winner lower pools + current ordinary contribution`.

Example 1545→1546:
`226,866,699 + 248,580 + 132,678 = 227,247,957` KZT exactly.

Economic screen remains poor:
- ~165.10 KZT EV per 300 KZT;
- break-even superprize ~3.395bn KZT vs observed ~227m.

Thus a modern transfer mechanism is validated, but not a profitable sampled state. It provides a signature to test independently in Azerbaijan.

# Corrected Azerbaijan jackpot chronology
Files:
- `data/historical/az_4plus4_jackpot_checkpoints.csv`
- `data/historical/az_4plus4_telegram_checkpoints.csv`

Important correction:
- 530,359 AZN jackpot win was **08.07.2023**, draw 23276;
- next jackpot was stated as 250,000 AZN for that historical rule era;
- do NOT treat migrated 2026 CMS metadata as a July-2026 reset.

Current accumulation lower bounds:
- 15.01.2025: >500k;
- 19.08.2025: >800k;
- 26.11.2025: >1m;
- 26.01.2026: >1.3m;
- June/July 2026 operator material: >1.5m then >1.8m.

### External transfers
On 06.01.2025 the operator announced that if the final Meqa 5/36 jackpot was not won, it would be added to 4+4. Outcome and amount remain unresolved.

Therefore jackpot accounting must allow:
`J_t = J_(t-1) + ordinary contributions + zero-winner/carryover transfers + external transfers - payouts/adjustments`.

# UK Lotto
H016 Wednesday Must Be Won was stress-tested and downgraded:
- initial demand cushion ~+33.77%;
- seven historical analogues median uplift ~+42.85%;
- six of seven exceed cushion;
- status: **inconclusive / materially weakened**.

H015 crowd-choice/sharing remains theoretically interesting but unquantified.

# Current blockers / negative search results
- Azərlotereya archive is client-rendered; hidden API/payload remains undiscovered.
- Search index does not expose draw #780 full payout table.
- Search index does not expose Vəzir's 2025-09-19 draw payout table; independent U≈514.35 test remains blocked.
- Ümüd exact date/draw remains unresolved despite bounded official-site/Telegram search.
- registration no. 336 is public, but detailed registered allocation document remains unfound in open search.
- exact adjacent Azerbaijan 4+4 jackpot values remain unavailable.
- January-2025 external-transfer amount remains unknown.
- category-II 20U remains unvalidated.
- secondary draw data still require primary reconciliation.

# Next actions
1. **Prioritize discovery of the official archive/API payload** rather than repeating manual old-page searches.
2. Recover draw #780 and independently test II≈20U.
3. Recover Vəzir 2025-09-19 draw and independently test U≈514.35.
4. Recover Ümüd exact draw/previous draw and distinguish system aggregation vs carryover.
5. Find a fourth primary one-number-short case / detailed registered rules.
6. Obtain exact adjacent jackpot states and test Kazakhstan-style accounting.
7. Expand 4+4 history toward 50–100 consecutive draws once collection is reliable.
8. Resolve the final Meqa 5/36 outcome / external transfer amount.
9. Confirm base-variant price directly.
10. Only after the balance equation is validated, build a forward state-EV trigger; then return to H015, Super Keno multipliers, scratch/instant inventory states and major progressive jackpots.

## Handoff
A future chat should read `START_HERE.md`, `PROJECT_RULES.md`, this file, `RESEARCH_PLAN.md`, and `AGENTS.md`, then verify the factual `research-work` branch state before continuing.
