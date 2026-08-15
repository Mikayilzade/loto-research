# H007 — Azerbaijan high-frequency RNG/history source discovery

Updated: 2026-08-15
Status: **official high-frequency mechanisms confirmed; bulk machine-readable history not yet recovered, so statistical anomaly testing is gated**

## Official sources
- Results hub: https://www.azerlotereya.com/lotereya-neticeleri
- Ekspres Keno archive UI: https://www.azerlotereya.com/neticeler/ekspres-keno
- Ekspres Keno game page: https://www.azerlotereya.com/lotereya/ekspres-keno
- Şanslı 6 FAQ: https://www.azerlotereya.com/faq/sansli-6
- ONLOTO page: https://www.azerlotereya.com/lotereya/onloto

## Confirmed current mechanics relevant to H007
### Ekspres Keno
Official page states:
- 80-number pool;
- 20 numbers drawn;
- a draw every **5 minutes**;
- archive-results UI exists publicly.

The public archive page is client-rendered. In the current retrieval environment, opening a dated Ekspres Keno archive page returns placeholder fields (`undefined`, `NaN`) instead of the draw payload. Therefore we do not yet have a reliable bulk history suitable for frequency/serial/spectral tests.

### ONLOTO
Official page states:
- 50 balls;
- 36 drawn;
- draw every **3 minutes**;
- current registration validity shown through 03.05.2027.

This is a high-sample-rate candidate, but no public machine-readable historical endpoint was recovered in this packet.

### Şanslı 6
Official FAQ states:
- 48-number pool, 35 numbers drawn;
- multiple bet types based on order/parity/color/sums;
- a random `Çarpan` multiplier bonus is automatically determined after the game;
- when active it is x1.5 or x2;
- operator says it is active on average in about **170 draws per day**;
- Lucky Clover positions are also randomly selected each draw.

This is unusually useful for H007 because there are multiple random streams to test if history becomes available:
1. number/order stream;
2. Clover-position stream;
3. multiplier activation stream;
4. multiplier magnitude stream.

A causal cross-stream test could be stronger than generic hot/cold-number screening, but only with timestamped draw history and strict holdout controls.

## Scientific gate
Do **not** run anomaly fishing on screenshots or a handful of draws.

Minimum acceptable dataset before H007 testing:
- exact draw ID and timestamp;
- complete ordered output, not only sorted numbers;
- bonus state where applicable;
- stable game-rule/version interval;
- enough consecutive draws for train/holdout split;
- provenance from official archive/API or independently reproducible capture.

## Planned tests once data exists
1. marginal frequency chi-square with multiplicity correction;
2. position-by-number independence;
3. serial/lags and transition matrix tests;
4. runs and entropy/compression controls;
5. time-of-day / modulo-cadence effects only as preregistered hypotheses;
6. change-point tests around version/deployment changes;
7. Şanslı 6 bonus activation: Bernoulli/overdispersion + periodicity + dependence on number stream;
8. strict forward holdout; any candidate edge must survive without retuning.

## Current conclusion
H007 remains **OPEN but data-gated**. The operator publishes enough mechanism detail to justify serious testing, especially Şanslı 6's separate random bonus streams, but this packet did not recover a trustworthy bulk historical endpoint. Blind pattern claims remain prohibited.
