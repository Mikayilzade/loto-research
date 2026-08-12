# Azerbaijan Poz-Qazan — remaining-prize state edge (H010)

Updated: 2026-08-12
Status: **initial EV quantified; denominator exists institutionally but no public live series-level access found**

## Research question
Can a physical instant-ticket series become unusually favorable or +EV after some prizes have been claimed, if the remaining prize inventory and remaining unsold ticket count are observable before purchase?

Key conditional-state identity:

`current EV = remaining after-tax prize value / remaining purchasable tickets`

A list of remaining prizes without a defensible denominator is not enough.

## Exact initial-state data
Azərlotereya publishes by registered physical Poz-Qazan series:
- ticket price;
- registration and validity;
- total tickets issued;
- total winning tickets;
- full prize-count table;
- gross prize fund and payout percentage;
- after-tax amounts for taxable prize tiers.

Derived dataset:
- `data/derived/az_poz_qazan_initial_ev_2026.csv`

## Current-series initial after-tax ranking
1. **Prestij reg.317** — ~69.9060% after-tax payout ratio; EV 6.990595 AZN per 10-AZN ticket.
2. **Meqa 7 reg.365** — ~66.8758%; EV 3.34378775 AZN per 5-AZN ticket.
3. **Qoşa 2 reg.383** — ~66.3051%; EV 1.326102 AZN per 2-AZN ticket.
4. **4 Fəsil reg.375** — ~62.9775%; EV 0.629775 AZN per 1-AZN ticket.

All ordinary initial states are materially negative EV.

## Denominator blocker — refined
A bounded official-domain search did not find a public live counter giving:
- remaining unsold tickets by active registration/batch; or
- a complete registration-specific remaining-prize table updated as claims occur.

However, the denominator is **not conceptually unavailable**.

### Daily sales data exists in the state information system
A current tax-law provision requires the lottery organizer to transmit lottery-ticket sales data and seller remuneration information **daily** from the organizer's information system to the designated state body's information system.

This is important: sales-to-date data exists institutionally and can in principle support a remaining-ticket denominator.

### Physical unsold inventory is formally tracked
The Lottery Law states, among other things, that:
- lottery tickets carry a number and/or series;
- unsold tickets are returned to the organizer under applicable procedures;
- unsold/returned tickets are destroyed by an organizer commission;
- the organizer must announce the end of an instant lottery.

So a physical-series closeout denominator also exists operationally.

### Public access search result
The State Tax Service has a public open-data page and annual/monthly reporting pages, but the public open-data page did not contain searchable entries for `lotereya`, `bilet`, or `satış` in the current crawl.

A 2025 annual-report PDF exists on the tax-service report page, but the current web tool timed out fetching it. It has **not** been analyzed, so no series-level sales content is claimed from it.

## Series identity is mandatory
Game-name matching is unsafe.

Current Prestij is registration **317**, valid from 12.06.2025. Its page surfaces historical Prestij winners, including Hüseyn Bünyatov with an official 500,000-AZN winning date of **22.07.2024**, before registration 317 existed.

Therefore winner carousels mix releases/registrations. Never decrement current-series inventory by game name alone.

Required matching before inventory decrement:
1. exact registration/batch;
2. winner date inside the relevant sale regime;
3. ideally ticket serial/series or explicit operator linkage.

The same caution applies to `Qoşa` vs `Qoşa 2` and any reused game name.

## Practical H010 routes from here
The web-search route for a public live denominator is currently exhausted. Higher-value routes are now:

1. **Official data request** to the operator and/or relevant state authority for sold-ticket count to date by registration (for example reg.317/365/375/383), plus current remaining prize counts if held.
2. Inspect operator/regulator reports or batch-close announcements when a series ends.
3. Investigate retailer/warehouse/pack information only if it can be tied defensibly to the whole registered series; local shop stock alone is not a global denominator.
4. Match current large-prize winner claims to exact registration/serial before adjusting the numerator.
5. If both numerator and denominator become observable, compute exact after-tax conditional EV and uncertainty bounds before any purchase conclusion.

## H010 status
**testing / data-blocked**.

The mathematical edge remains valid in principle. For current Azerbaijan physical Poz-Qazan games, exact initial EV is known, and institutional sales tracking is confirmed, but no public registration-specific live denominator has yet been recovered. Therefore no executable +EV state is validated.
