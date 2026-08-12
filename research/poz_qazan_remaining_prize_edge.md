# Azerbaijan Poz-Qazan — remaining-prize state edge (H010)

Updated: 2026-08-12
Status: **initial EV quantified; current conditional EV blocked by missing live denominator**

## Research question
Can a physical instant-ticket series become unusually favorable or +EV after some prizes have been claimed, if the remaining prize inventory and remaining unsold ticket count are observable before purchase?

The key conditional-state formula is conceptually:

`current EV = remaining after-tax prize value / remaining purchasable tickets`

A list of remaining prizes without a defensible denominator of remaining tickets is not enough.

## Current operator data is unusually useful for the initial state
Azərlotereya publishes, by registered Poz-Qazan series:
- ticket price;
- registration number and validity;
- total tickets issued;
- total winning tickets;
- full prize-count table;
- total gross prize fund and payout percentage;
- after-tax amount for prize tiers where tax applies.

This allows exact initial-series gross and after-tax EV.

Derived dataset:
- `data/derived/az_poz_qazan_initial_ev_2026.csv`

## Four current-series baselines
### Prestij — registration 317 / 03.06.2025
- ticket: 10 AZN
- tickets: 2.4m
- gross prize fund: 16.916m AZN
- gross payout ratio: **70.4833%**
- after-tax prize total: **16.777428m AZN**
- after-tax payout ratio: **69.9060%**
- expected after-tax payout per initial ticket: **6.990595 AZN**
- top tier: 2 × 500,000 AZN; displayed after-tax value 450,051 AZN each

### Meqa 7 — registration 365 / 02.03.2026
- ticket: 5 AZN
- tickets: 4m
- gross prize fund: 13.4m AZN
- gross payout ratio: **67.00%**
- after-tax prize total: **13.375151m AZN**
- after-tax payout ratio: **66.8758%**
- expected after-tax payout per initial ticket: **3.34378775 AZN**
- top tier: 2 × 100,000 AZN; displayed after-tax value 90,050.50 AZN each

### Qoşa 2 — registration 383 / 02.06.2026
- ticket: 2 AZN
- tickets: 4m
- gross prize fund: 5.3184m AZN
- gross payout ratio: **66.48%**
- after-tax prize total: **5.304408m AZN**
- after-tax payout ratio: **66.3051%**
- expected after-tax payout per initial ticket: **1.326102 AZN**
- top tier: 40 × 4,000 AZN; displayed after-tax value 3,650.20 AZN each

### 4 Fəsil — registration 375 / 15.04.2026
- ticket: 1 AZN
- tickets: 20m
- gross prize fund: 12.6m AZN
- gross payout ratio: **63.00%**
- after-tax prize total: **12.5955m AZN**
- after-tax payout ratio: **62.9775%**
- expected after-tax payout per initial ticket: **0.629775 AZN**
- top tier: 10 × 5,000 AZN; displayed after-tax value 4,550 AZN each

Initial ranking among these four by after-tax payout ratio:
1. Prestij ~69.91%
2. Meqa 7 ~66.88%
3. Qoşa 2 ~66.31%
4. 4 Fəsil ~62.98%

All ordinary initial states remain materially negative EV.

## Critical blocker: no public live remaining-ticket denominator found
A bounded official-domain search for terms equivalent to remaining prizes / remaining tickets did not reveal a public live counter that states:
- tickets remaining unsold in a current registration/batch; or
- a complete registration-specific remaining-prize table updated as prizes are claimed.

Without the remaining-ticket denominator, current conditional EV cannot be calculated reliably.

Even knowing that some top prizes were claimed is insufficient: a top-prize depletion can make EV worse, while a sales-heavy remaining inventory with unusually many prizes left could make EV better. Both numerator and denominator are required.

## Series identity is mandatory — game-name matching is unsafe
A major data-quality trap was found on the current Prestij page.

The current series is registration **317**, starting 12.06.2025. Its table contains exactly two 500,000-AZN top prizes. The page's winner carousel also surfaces historical Prestij 500,000-AZN winners. However at least one such winner, Hüseyn Bünyatov, has an official winning date in **2024**, before registration 317 existed.

Therefore the current game's winner carousel mixes winner stories from earlier Prestij releases/registrations. It would be incorrect to infer that a current-series top prize has been exhausted merely because a same-name historical winner appears on the page.

The same caution applies to similarly named products such as Qoşa vs Qoşa 2.

Required matching before decrementing inventory:
1. exact registration/batch;
2. sale-validity window;
3. winner date;
4. ideally ticket serial/series or explicit operator statement linking the win to that registration.

## H010 status
The mathematical mechanism remains valid in principle:
- if remaining prize values and remaining tickets are observable, conditional EV can be computed exactly;
- an initial negative payout ratio does not imply every late state is equally negative.

But for the current Azerbaijan physical Poz-Qazan products examined here, **the necessary live remaining-ticket denominator has not been found publicly**.

Therefore H010 for these series is currently:
- **testing / data-blocked**;
- not executable as a current +EV strategy;
- worth revisiting if a retailer/pack/serial system, official remaining-prize page, sales counter, batch-close report, or another defensible denominator becomes available.

## Highest-value next checks
1. Search current winner/news posts for explicit registration or batch identifiers rather than game name alone.
2. Investigate whether physical ticket serial/pack ranges reveal how many tickets in a registered series remain purchasable.
3. Look for operator/regulator batch-close or sales-progress reporting.
4. If a denominator becomes observable, build registration-specific conditional EV with after-tax prizes and uncertainty bounds.
5. Do not infer remaining inventory from a promotional winner carousel.
