# Azerbaijan 4+4 — category II primary-source lead

Updated: 2026-08-12
Status: **three primary one-number-short tickets; ~20U baseline hypothesis strengthened; system-vs-carryover mechanism unresolved**

## Why category II matters
Category II is `4+3 / 3+4`. Exact probability per base variant:

`0.000005452835634281` = about **1 in 183,390.82**.

Preserved 2026 secondary tables repeatedly show zero category-II winners but do not reveal the assigned pre-draw category-II pool. Category II is therefore central to both full ordinary EV and H014 zero-winner state research.

## Primary one-number-short cases
### Nizami Tağıyev
- official winner page: https://www.azerlotereya.com/winners/nizami-tagiyev-128
- Telegram: https://t.me/Azerlotereya/2353
- reported payout: **8,609 AZN**
- jackpot: >1.5m AZN in the official Telegram post
- working event: **2026-06-02 / draw #780**

### Ümüd Hüseynov
- Telegram: https://t.me/Azerlotereya/2516
- reported payout: **15,986 AZN**
- jackpot: >1.8m AZN
- exact draw/date still unresolved

### Vəzir Quliyev
- official winner page: https://www.azerlotereya.com/winners/vazir-quliyev-108
- official date: **2025-09-19**
- reported payout: **10,287 AZN**
- operator explicitly says he missed the 4+4 jackpot by one number
- contemporaneous operator material places jackpot above ~800k AZN

For one ordinary variant, “one number short of 4+4” means exactly seven of eight required numbers matched, so each ticket contains at least one category-II winning variant.

## ~20U baseline hypothesis
Independent official category-III (`4+2`) winner stories reproduce the already reconstructed `III = 11U` scale. Against that same scale, the category-II ticket payouts are suggestive:

- Nizami: `8,609 / 20 = 430.45`
- Vəzir: `10,287 / 20 = 514.35`
- Ümüd: `15,986 / 40 = 399.65`

The first two are naturally compatible with **one ~20U category-II component** if their draw-level U values were near 430 and 514 respectively. Ümüd's amount is compatible with roughly **two 20U-sized components** at U≈400.

This strengthens, but does not prove, an ordinary category-II allocation around **20U**.

## Competing explanations for Ümüd's ~40U ticket
Do not choose between these without draw/ticket evidence.

### A — system-ticket aggregation
The current official game page explicitly confirms 5+5 and 6+6 combination play and says such a ticket can win across multiple categories. Ümüd may therefore have had multiple category-II variants plus lower-category wins, with 15,986 AZN being the aggregate ticket payout.

### B — category-II state/carryover
If ordinary category II is ~20U and a prior zero-winner category-II balance survives, a later winning state could pay current ~20U plus accumulated money, producing something near ~40U when neighboring U values are similar.

This would be directly relevant to H014, but is **not established**. Carryover is only one competing explanation.

### C — other aggregation/state rules
Additional lower-tier wins, hierarchy adjustments, tax/reporting conventions or other rule mechanics could also explain the ticket-level amount.

## Conditional carryover scale screen
This section tests only whether the proposed mechanism is large enough to matter. It does **not** establish that Azerbaijan transfers a zero-winner category-II pool to jackpot.

Assumptions for the screen:
- ordinary category II = **20U**;
- empirical scale `U ≈ 0.01 × sold_variants`;
- representative volume = roughly 38k–50k variants, consistent with the reconstructed 2026 scale;
- if category II has zero winners, its full assigned pool survives into a future state;
- current Tue/Fri schedule is approximated as 104 draws/year.

For category-II probability `p = 0.000005452835634281`, zero-winner probability is `(1-p)^N`.

Results:
- N=38k: P(0 II winners) ≈ **81.29%**; assumed II pool 7,600 AZN; expected unpaid ≈ **6,178 AZN/draw**;
- N=40k: P0 ≈ **80.40%**; pool 8,000; expected unpaid ≈ **6,432 AZN/draw**;
- N=42k: P0 ≈ **79.53%**; pool 8,400; expected unpaid ≈ **6,681 AZN/draw**;
- N=45k: P0 ≈ **78.24%**; pool 9,000; expected unpaid ≈ **7,042 AZN/draw**;
- N=50k: P0 ≈ **76.14%**; pool 10,000; expected unpaid ≈ **7,614 AZN/draw**.

Annualized at 104 draws, this is roughly **0.64m–0.79m AZN/year** of expected zero-winner II money *if* the full assumed 20U pool is retained and transferred.

Interpretation: the carryover hypothesis is **not too small by orders of magnitude**. Its scale is capable of contributing materially to a million-AZN jackpot over a long cycle. This is only a plausibility result; the actual destination of the unpaid pool is still unknown and external cross-game transfers also exist.

Derived data:
- `data/derived/az_4plus4_category2_carryover_screen.csv`

## Search blockers from the latest bounded packet
- the public search index still does not expose the full 2025-09-19 Vəzir draw payout table, so independent U≈514.35 has not been tested;
- Ümüd's exact draw/date is still not exposed in indexed winner pages; the official Telegram post itself is confirmed;
- registration no. 336 is visible on the official game page, but the detailed registered allocation document has not been found in open search;
- a guessed old draw number must **not** be promoted from calendar arithmetic without an independently recovered result page.

## Economic implication if ordinary II=20U is confirmed
With empirical `U/N≈0.01`, 20U corresponds to about **0.20 AZN of aggregate sales-funded category-II pool per sold variant**.

Because category II is rare, immediate expected payout is not simply +0.20 AZN per ticket unless the whole pool is guaranteed to be paid each draw. At observed tens-of-thousands-of-variant volume, zero-winner category-II draws are likely, so destination of the unpaid amount is strategically decisive.

## Decisive next evidence
Priority order:
1. discover the official archive/API payload so historical payout tables stop depending on search-engine indexing;
2. recover draw #780 full payout table and draw-level U;
3. recover the 2025-09-19 Vəzir draw payout table and test whether independent U≈514.35;
4. recover Ümüd exact draw and previous draw;
5. establish whether any of the three tickets were ordinary vs 5+5/6+6 system entries;
6. find a fourth primary one-number-short case;
7. obtain registered rules explicitly stating category-II allocation/carryover.

A direct draw where one category-II winner receives a total near **20U reconstructed independently from III/IV/VII/VIII/IX** would materially validate the weight. A transition showing an unpaid ~20U amount entering a later jackpot/category state would then validate the carryover mechanism separately.

Data:
- `data/historical/az_4plus4_official_winner_crosschecks.csv`
- `data/historical/az_4plus4_payout_samples_2026.csv`
- `data/derived/az_4plus4_category2_carryover_screen.csv`
