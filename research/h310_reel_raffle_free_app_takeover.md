# H310 — Reel Raffle free app finite-pool takeover screen

Checked: 2026-08-27
State: **CLOSED / TAKEOVER-BLOCKED**

## Why this candidate mattered

The active Reel Raffle app-exclusive draw is a genuinely zero-price finite-pool cash competition: the page advertises **£0.00** entry, a **£1,000 cash** prize, a finite advertised maximum of **99,999 tickets**, and says app users may enter free once every day. This is the right structural direction after H309 because acquisition cost itself is not the blocker.

## Current authoritative snapshot

Source: https://reelraffle.com/product/app-exclusive-win-1000-cash-for-free-2/

At the checked live page:

- prize: 1 × £1,000 cash, paid by bank transfer;
- ticket price: £0.00;
- total ticket cap: 99,999;
- maximum entries per person: 50;
- current entered/sold count: 10,585;
- closing date: 27 September 2026.

The same page states that the winner is drawn from entrants and the competition has a per-person maximum of 50.

## Exact takeover blocker

For any one player, at most 50 of the 10,585 entries already present can belong to that player. Therefore at least

`10,585 - 50 = 10,535`

current entries are necessarily external to that single player.

A legal draw can select any one of those external entries. In that legal outcome the candidate player receives **£0**.

Thus:

- entry cost can be £0;
- expected value may be positive because the ticket is free;
- but **strict guaranteed cash floor = £0**;
- therefore **strict guaranteed profit is not established**.

This conclusion does not depend on postal delay, checkout atomicity, or the exact future number of entrants. The current snapshot plus the hard 50-entry personal cap already supplies an unavoidable external-winner state.

## Stronger structural form

Even before using the current entered count, the player can control at most

`50 / 99,999 = 0.000500005... = 0.0500005%`

of the advertised finite identifier capacity. The current 10,585 entries make the external-entry existence concrete rather than hypothetical.

## Postal route

The site also publishes a free postal route, but this cannot rescue takeover because the same competition limit applies. Its terms additionally say each postal entry must be sent separately, proof of posting does not guarantee inclusion, and entries received after a cap fills are excluded.

## Result

H310 is **CLOSED / TAKEOVER-BLOCKED** for rigorous guaranteed-profit research. Reopen only if a future zero-price pool is found where one eligible player can reserve/control every relevant identifier (or every possible winning identifier) before any external entry exists.

## Reproducibility

- `src/loto_research/h310_reel_raffle_free_app_cap.py`
- `data/derived/h310_reel_raffle_free_app_cap.json`
