# H306 — On The Podium current free finite-pool blocker

Date checked: 2026-08-27
State: **CLOSED / CURRENT-TAKEOVER-BLOCKED**

## Why this candidate mattered

The current On The Podium Prizes homepage exposes several competitions with a displayed entry price of **Free** and a hard finite maximum of **1,000 tickets**. The most interesting is `FREE TO ENTER £100 CASH!`: if a single eligible entrant could electronically reserve all 1,000 identifiers at zero acquisition cost before anyone else entered, the £100 winner would be deterministic and strict positive profit would be trivial.

This is exactly the mechanism sought after H302/H303: zero-price or subsidized entries consuming the same finite inventory.

## Current evidence

On 2026-08-27 the live homepage displayed:

- `FREE TO ENTER £100 CASH!` — Free, max tickets 1,000, **16.2% sold**;
- `2 BSB tickets ...` — Free, max tickets 1,000, **5.6% sold**;
- `FREE TO ENTER £25 SITE CREDIT` — Free, max tickets 1,000, **6.1% sold**;
- `FREE TO ENTER £50 SITE CREDIT` — Free, max tickets 1,000, **6.5% sold**;
- `FREE TO ENTER £75 SITE CREDIT` — Free, max tickets 1,000, **6.2% sold**.

A strictly positive displayed sold percentage is enough for the takeover proof: at least one eligible identifier is already issued outside a newly arriving entrant's control. Exact rounding of the percentage is irrelevant.

For the £100 cash draw, therefore, a legal outcome remains in which an already-issued external identifier wins. The new entrant's guaranteed cash floor from the draw is **£0** even if every remaining identifier could somehow be acquired for free.

## Independent execution blocker

The competition page's published free-entry instructions describe a **postal** route:

- each free entry must be sent separately;
- proof of posting does **not** guarantee inclusion;
- if the finite cap is reached before the postal entry is received, that entry is not entered;
- the promoter does not acknowledge receipt of the postal entry.

Thus the published rules do not establish an atomic electronic AMOE/full-pool reservation mechanism. The zero-price presentation on the homepage cannot be upgraded into a proof that one entrant can reserve all 1,000 identifiers online.

## Exact conclusion

For the currently visible draw, strict takeover is already impossible because external entries exist. This is stronger than the postal-delay blocker.

Even considering a hypothetical future fresh launch at 0% sold, the evidence checked here still does not certify the two conditions required for rigorous SUCCESS:

1. one entrant may acquire the full 1,000-entry inventory; and
2. the zero-price route reserves those identifiers immediately/atomically rather than using the non-guaranteed postal route.

Therefore H306 is **closed for the current live pool**, while the general mechanism should be reopened only if a future launch supplies explicit electronic zero-price reservation plus a per-player limit equal to the full finite inventory.

## Reproducibility

- `src/loto_research/h306_onthepodium_free_pool_blocker.py`
- `data/derived/h306_onthepodium_free_pool_blocker.json`

## Sources checked

- On The Podium Prizes current homepage, 2026-08-27.
- On The Podium `FREE TO ENTER £100 CASH!` competition page.
- On The Podium published free-entry conditions / site terms.
