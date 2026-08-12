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

This file is the authoritative handoff checkpoint. Read `START_HERE.md`, `PROJECT_RULES.md`, `RESEARCH_PLAN.md` and `AGENTS.md` before code work.

## Foundation / code
- `catalog/games.csv`, `catalog/sources.csv`, `schemas/DATA_MODEL.md`
- `research/HYPOTHESES.md`
- `src/loto_research/probability.py`
- `src/loto_research/collectors/azerbaijan.py`
- `src/loto_research/four_plus_four.py`
- `src/loto_research/pari_mutuel.py`
- `src/loto_research/uk_lotto.py`
- regression tests exist for exact probability, Azerbaijan normalization, UK Lotto and 4+4 empirical identities.
- GitHub Actions remains disabled.

## Historically validated structural +EV benchmark
### Cash WinFall
A preserved 2011 roll-down gives, with exact 6/46 probabilities and cash-only tiers:
- ticket: $2;
- expected payout: **$2.2137120403**;
- expected ROI: **+10.6856%** before tax/execution.

Conclusion: structural +EV lotteries have existed without predicting numbers.

## Azerbaijan baseline games
### Beşdə 5
- exact jackpot odds: **1 in 376,992**;
- favorable gross baseline: **0.535555131 AZN per 1-AZN variant**;
- net baseline before tax/sharing: about **-46.44%**.

### Super Keno
- displayed base-table gross EV: **0.598555794 AZN per 1 AZN**;
- net baseline before tax: about **-40.14%**;
- multiplier economics remain pending.

# Azerbaijan 4+4 — current top local target

## Exact mechanics
Current primary operator page establishes:
- two independent 4/20 boards, with balls returned between A and B;
- 11 grouped winning categories;
- jackpot odds **1 in 23,474,025**;
- any listed winning-state probability **18.614724%** (~1 in 5.3721);
- public ticket price **2 AZN**;
- registration no. **336 / 17.01.2021**, validity through 31.12.2027;
- 5+5 / 6+6 system entries generate multiple variants and can win multiple categories;
- current draw schedule **Tuesday / Friday 19:45**.

Direct primary wording for one base-variant price is still missing. **2 AZN/base variant remains a high-confidence empirical inference, not a direct rule fact.**

## Strongly reconstructed ordinary pool engine
Files:
- `data/historical/az_4plus4_payout_samples_2026.csv`
- `data/derived/az_4plus4_pool_unit_validation.csv`
- `research/4plus4_economics_inference.md`

For ordinary sampled draws, one common unit `U` explains lower pools:
- III = **11U**
- IV = **5U**
- VII = **9U**
- VIII = **14U**
- IX = **7U**
- V + VI = **2U**

Thus III–IX jointly distribute approximately **48U**.

Draw #790 was added after discovery and independently fits the formula closely (U≈417.6), providing the first out-of-sample confirmation.

### V/VI coupling
Empirical rule:
- if V winners <= VI winners, pools are approximately U/U;
- if V winners > VI winners, combined 2U is redistributed so per-winner V ≈ 1.5× per-winner VI.

Zero-winner V/VI behavior is deliberately not extrapolated.

### Independent U scale
Exact X/XI probabilities plus observed fixed prizes X=6 AZN, XI=4 AZN provide an independent volume estimator. Across seven samples:
- mean `U/N_hat` ≈ **0.00996205**;
- median ≈ **0.00995043**;
- range ≈ **0.00953821–0.01050994**.

Therefore `U ≈ 0.01 × sold_variants` emerges from data. If a base variant costs 2 AZN, U is roughly 0.5% of gross sales.

### Primary winner-story cross-check
Official operator stories independently reproduce category III = 11U:
- Samir İmaməliyev: `4+2`, 4,503 AZN -> `4503/11 = 409.36`;
- Orxan Həsənov: `4+2`, 4,381 AZN -> `4381/11 = 398.27`.

These lie on the same U scale as reconstructed 2026 draw tables. The U-engine therefore has primary-operator cross-checks, not only secondary archive support.

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
- **Ümüd Hüseynov:** 15,986 AZN, jackpot >1.8m; exact date/draw unresolved.

“One number short” proves at least one category-II variant on each ticket, but system tickets can aggregate multiple winning variants/categories.

## ~20U working hypothesis
Normalization:
- Vəzir: `10,287 / 20 = 514.35`;
- Nizami: `8,609 / 20 = 430.45`;
- Ümüd: `15,986 / 40 = 399.65`.

Working hypothesis only:
- ordinary II may be approximately **20U**;
- Nizami/Vəzir may each contain one ~20U component;
- Ümüd may contain two ~20U components or a larger state-dependent amount.

Competing explanations for Ümüd remain open:
1. system-ticket aggregation (explicitly plausible under official 5+5/6+6 mechanics);
2. category-II carryover/state;
3. other hierarchy/aggregation/reporting mechanics.

## Conditional carryover scale screen
Assumptions only: II=20U, U=0.01N, N≈38k–50k, and zero-winner II pool survives intact.

Then:
- P(no II winner) ≈ **81.3% at N=38k** down to **76.1% at N=50k**;
- assumed II pool ≈ **7,600–10,000 AZN**;
- expected unpaid amount ≈ **6,178–7,614 AZN per draw**;
- at ~104 Tue/Fri draws/year, conditional scale ≈ **0.64m–0.79m AZN/year**.

Interpretation: if the transfer rule exists, it is large enough to matter by order of magnitude. This does **not** prove that Azerbaijan transfers category-II money.

# H014 — zero-winner state edge
Status: **testing**.

Required proof sequence:
1. infer an ordinary assigned pool for a zero-winner category;
2. obtain adjacent jackpot/category states;
3. show the missing amount enters the next state after normal contributions/external transfers;
4. repeat across multiple transitions;
5. require state visibility before purchase.

Only then build a forward EV trigger.

# Kazakhstan 4/20 comparator
Do **not** transfer Kazakhstan rules to Azerbaijan. It is a methodological comparator with the same two-board 4/20 combinatorics.

Files:
- `research/kazakhstan_4x20_control.md`
- `data/historical/kz_4x20_transition_samples.csv`

Three independent consecutive-draw transitions close exactly as:
`next superprize = previous superprize + unpaid zero-winner lower pools + current ordinary contribution`.

Example 1545→1546:
`226,866,699 + 248,580 + 132,678 = 227,247,957` KZT exactly.

Economic screen remains poor (~165.10 KZT EV per 300 KZT; break-even ~3.395bn KZT vs observed ~227m). The mechanism is real but sampled state is not +EV.

# Corrected Azerbaijan jackpot chronology
Files:
- `data/historical/az_4plus4_jackpot_checkpoints.csv`
- `data/historical/az_4plus4_telegram_checkpoints.csv`

Important correction:
- 530,359 AZN jackpot win was **08.07.2023**, draw 23276;
- next jackpot was 250,000 AZN for that historical era;
- do not treat migrated 2026 CMS metadata as a July-2026 reset.

Current accumulation lower bounds include:
- 15.01.2025 >500k;
- 19.08.2025 >800k;
- 26.11.2025 >1m;
- 26.01.2026 >1.3m;
- later operator material >1.5m and >1.8m.

### External transfers
On 06.01.2025 the operator announced that an unwon final Meqa 5/36 jackpot would be added to 4+4. Outcome/amount remain unresolved.

Therefore model:
`J_t = J_(t-1) + ordinary contributions + zero-winner/carryover transfers + external transfers - payouts/adjustments`.

# Archive/API discovery — bounded packet completed
New note:
- `research/azerlotereya_archive_api_discovery.md`

Confirmed:
- official current-results page renders current numbers/data;
- official 4+4 archive shell exposes `Tiraj undefined` to the crawler;
- game page has intermittently exposed missing/Invalid Date state while dedicated current-results remains populated.

Bounded attempts completed without finding an authoritative endpoint:
- official-domain searches for `api`, `drawNo`, `lotteryId`, `fourplus`, exact draw IDs;
- robots/sitemap attempts;
- parsed page/link inspection;
- likely API host / Swagger searches;
- public GitHub repository searches for Azerlotereya / implementation vendor terms;
- previous direct-container network approach was blocked by environment DNS/network limitations.

Implementation clue only: a public project participant credits **Şanstech + Kartega** for the revamped Azerlotereya.com/CMS architecture. No endpoint was exposed.

**Conclusion: do not guess undocumented API URLs.** Revisit only with new evidence/tooling, ideally browser DevTools Network/HAR or a browser-capable network inspector.

Official current-results page remains a useful primary reconciliation anchor; on 2026-08-12 it showed televised draw **26332**, dated **11.08.2026 18:45**.

# UK Lotto
H016 Wednesday Must Be Won was stress-tested and downgraded:
- initial demand cushion ~+33.77%;
- seven historical analogues median uplift ~+42.85%;
- six of seven exceed cushion;
- status: **inconclusive / materially weakened**.

H015 crowd-choice/sharing remains theoretical and unquantified.

# Current blockers
- official historical archive payload/API not discovered;
- draw #780 full payout table unrecovered;
- Vəzir 2025-09-19 draw-level U unrecovered;
- Ümüd exact date/draw unresolved;
- exact adjacent 4+4 jackpot values unavailable;
- January-2025 external-transfer amount unknown;
- detailed registered no.336 allocation document unfound;
- direct primary base-variant price statement missing;
- category-II 20U hypothesis unvalidated;
- secondary historical data require primary reconciliation.

# Next actions
1. **Do not repeat blind API searches.** Use new tooling/evidence only (DevTools Network/HAR/browser network inspector).
2. In parallel, pursue primary winner/news evidence that can resolve category II or jackpot transitions without the archive API.
3. Recover draw #780 and independently test II≈20U when a historical source becomes available.
4. Recover Vəzir 2025-09-19 draw and independently test U≈514.35.
5. Recover Ümüd exact draw/previous draw; distinguish system aggregation vs carryover.
6. Find a fourth primary one-number-short case or detailed registered rules.
7. Obtain exact adjacent jackpot states and test Kazakhstan-style accounting.
8. Expand 4+4 to 50–100 consecutive draws once collection is reliable.
9. Resolve final Meqa 5/36 outcome/external-transfer amount and direct base-variant price.
10. Only after state accounting is validated, build a forward EV trigger; then return to H015, Super Keno multipliers, scratch/instant inventory states and major progressive jackpots.
