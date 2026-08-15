# STATUS

Updated: 2026-08-15
Branch: `research-work`

## Current stage
**Stage 1 — structural-edge search; progressive jackpots**

## GO-mode
Resume from this checkpoint, avoid repeating closed tests, save every meaningful packet to GitHub. Terminal states:
- `SUCCESS` = strictly proven guaranteed positive net profit under explicit executable conditions after all costs/outcome branches.
- `EXHAUSTED` = all defensible registered project/edge classes tested or closed without SUCCESS.

Current terminal state: **NO SUCCESS; NOT EXHAUSTED**.

# NEW — H002 Powerball full threshold packet completed
Files:
- `research/powerball_progressive_threshold.md`
- `research/h002_powerball_demand_proxy.md`
- `src/loto_research/powerball_threshold.py`
- `tests/test_powerball_threshold.py`
- `data/derived/h002_powerball_sharing_threshold_curve.csv`
- `data/derived/h002_powerball_winner_count_sales_proxy.csv`

## Exact baseline and sharing
Current official Powerball structure remains $2, 5/69 + 1/26, `M=292,201,338`, jackpot pari-mutuel when multiple jackpot-winning tickets exist. UK sales began 2026-07-21 and share the common jackpot.

Existing fixed lower-tier EV: **$0.31987825/play**.
Absolute no-tax/no-sharing cash break-even: **$490.934m**.

Exact expected jackpot share conditional on our winning line when there are `n` other lines with exact-combination popularity multiplier `a`:

`q=a/M`

`S=[1-(1-q)^(n+1)]/((n+1)q)`.

Uniform-line sharing-only cash thresholds:
- 25m other lines: **~$512.2m**;
- 50m: **~$534.1m**;
- 100m: **~$579.7m**;
- 200m: **~$678.0m**;
- 300m: **~$785.3m**;
- 500m: **~$1.025bn**.

Illustrative 24%/30% jackpot haircuts push thresholds higher; these are sensitivity columns, not claims about universal final tax liability.

## Observed 2026 participation proxy
Using official overall odds `1 in 24.87` and nationwide result winner counts gives noisy play-count scale anchors:
- 2026-06-20: ~14.42m plays; $135.8m cash; sharing-only threshold ~$503.1m;
- 2026-07-08: ~12.72m; $195.0m cash; threshold ~$501.7m;
- 2026-07-25: ~26.55m; $268.4m cash; threshold ~$513.6m;
- 2026-07-29: ~20.90m; $292.5m cash; threshold ~$508.7m.

Post-UK winner-count proxies may understate the common-jackpot population because lower-tier administration differs. Even so, observed cash values were far below break-even.

## NEW — Powerball full-space guarantee result
Buying all combinations costs **$584,402,676**. Deterministic non-jackpot gross is about **$93,468,852.65**; therefore the ideal zero-tax/no-sharing jackpot break-even is again **$490,933,823.35**.

However full coverage guarantees only that we hold one jackpot-winning line, not that we are the sole jackpot winner. If at most `K` external jackpot-winning tickets were guaranteed, sufficient no-tax jackpot would scale as `490.934m*(K+1)`. The rules do not provide a useful pre-draw cap on exact-combination duplicates.

Conclusion: **Powerball full-space is NOT a terminal guaranteed-profit strategy**. Sharing prevents a strict all-outcome guarantee absent a defensible external-winner cap; scale also requires 292.2m plays / $584.4m acquisition before execution costs.

H002 remains open as a **positive-EV extreme-jackpot** question, not as a current guarantee.

# H005/H009 status
System-package and deterministic-discount work already closed/filtered:
- ordinary additive system packages: no edge;
- Australia Oz Lotto System 8: exactly linear pricing;
- Poland system/fractional structures: no verified constituent-price arbitrage;
- real Poland 13→12 PLN bundle discount exists but has zero-payout outcome, so no guarantee;
- random second chances / nonwithdrawable replay credits / modest zero-floor discounts cannot produce all-outcome profit;
- current deterministic subsidy screen found no surviving terminal candidate.

# Other closed / blocked
- H012a/H004 ordinary additive wheels: CLOSED by expectation theorem.
- Beşdə 5 full coverage: guaranteed loss.
- ONLOTO types 1–10 full coverage: guaranteed loss.
- 4+4 single 5+5/6+6 systems: zero-payout outcomes exist; no guarantee.
- 4+4 full-space: BLOCKED on authoritative system/base pricing + category-II/carryover/pool response.
- H015 anti-crowd standalone: CLOSED as guarantee; useful sharing optimizer only.
- H010 Poz-Qazan remaining-state: data-blocked on live denominator.
- H014 4+4 carryover: data-blocked.

# Safe next priorities
1. **H002a Mega Millions current $5 format**: exact lower-tier EV, sharing curve, cash-jackpot threshold, and full-space guarantee bound.
2. **H002b EuroMillions**: jackpot cap/rolldown, country-specific price/tax/claim differences, sharing and full-space bound.
3. H008 cross-jurisdiction lawful pricing/tax/payout differences, including US vs UK Powerball economics.
4. Broaden Powerball demand anchors only if it materially changes the threshold band; do not repeat generic threshold math.
5. H012 finite/final-draw states only where accumulated guaranteed pools or subsidies break ordinary economics.
6. H012b execution constraints only for candidates that survive economic screening.
7. H006/H007 randomness branches after reliable histories are collected.

Permanent audit ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`.
