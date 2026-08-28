# H327 — KRAZED COSMIC CASH postal subsidy / random-allocation bound

Date checked: 2026-08-28
Branch: `research-work`
State: **CLOSED / RANDOM-ALLOCATION-AND-FREE-ROUTE-CAP BLOCKED**

## Why this packet

H326 found a real >100% arithmetic postal-takeover near miss but failed because the per-person cap was only 10% of the pool. H327 searched for a fresh finite pool where the free postal route itself is a genuine subsidy rather than merely matching the paid ticket price.

KRAZED `COSMIC CASH` is useful because the current page shows:

- 99,999 total tickets;
- £0.10 paid price per ticket;
- 316 sold on the checked snapshot;
- max 999 paid tickets per user;
- only **one free postal entry per person per competition**;
- that one valid postal entry receives **10 tickets**;
- valid postal entries are processed later and tickets are allocated to the account;
- the instant-win section says tickets are **randomly allocated**;
- current advertised instant tiers sum to 12,029 prize-bearing identifiers.

Source: https://krazed.co.uk/competition/cosmic-cash

Royal Mail currently prices a standard 2nd Class letter/postcard at **£0.91**.
Source: https://www.royalmail.com/sending/uk/2nd-class

## Step 1 — deterministic postal discount

Ten paid tickets cost exactly:

`10 × £0.10 = £1.00`.

One postal entry costs £0.91 and receives 10 tickets, so the effective acquisition cost is:

`£0.91 / 10 = £0.091 per ticket`.

That is a real deterministic **9% discount** versus buying the same ten tickets online.

This matters: unlike many postal-bundle cases, H327 really does contain an external acquisition subsidy.

## Step 2 — exact instant-win inventory

The live prize schedule checked on 2026-08-28 contains:

- 5 × £100
- 4 × £50
- 20 × £20
- 70 × £10
- 180 × £5
- 350 × £2
- 400 × £1
- 1,500 × £0.50
- 1,500 × £0.20
- 8,000 × £0.10

Exact totals:

- prize-bearing identifiers = **12,029**;
- advertised instant cash face value = **£5,650**.

The same snapshot showed 41 lower-tier prizes already found (4 × £2, 1 × £1, 5 × £0.50, 5 × £0.20, 26 × £0.10), with no higher-tier finds shown.

Therefore:

- remaining tickets = `99,999 - 316 = 99,683`;
- remaining instant-win IDs = `12,029 - 41 = 11,988`;
- remaining zero-instant IDs = `99,683 - 11,988 = 87,695`.

## Step 3 — strict worst-case allocation

The free route gives only 10 tickets and the competition states that identifiers are randomly allocated.

Because:

`87,695 remaining zero-instant IDs >= 10 postal tickets`,

there exists a fully legal allocation in which **all ten** postal tickets land in the zero-instant set.

Hence the strict withdrawable-cash floor of the subsidised 10-ticket postal bundle is:

**£0**.

No expected-value assumption is needed.

## Step 4 — takeover gate

The free route is even more restrictive than the ordinary paid cap: only one free postal entry per person per competition. So the deterministic 9% subsidy is limited to ten randomly allocated identifiers.

Even the ordinary max of 999 tickets is far below the 99,999-ticket universe. Thus one player cannot remove the external/zero-cash support.

Postal processing is also non-atomic: the rules say processing may take up to 10 working days, late/capped-out entries are not accepted, and the promoter does not accept responsibility for delayed/lost mail. These execution facts only strengthen the closure; they are not required for the core zero-floor proof.

## Result

**H327 CLOSED.**

This is a useful negative result rather than a trivial one: a real deterministic acquisition subsidy exists (9%), but random allocation plus the one-postal-entry cap leaves a legal all-zero bundle outcome. Therefore the strict guaranteed cash floor remains £0.

Reusable gate:

> A deterministic discount on a random finite bundle is insufficient for guaranteed profit whenever the remaining zero-cash identifier support is at least the maximum subsidised bundle size.

## Reproducibility

- `src/loto_research/h327_krazed_cosmic_cash_postal_subsidy.py`
- `data/derived/h327_krazed_cosmic_cash_postal_subsidy.json`
- `research/H327_VALIDATION.md`
- `research/H327_STATUS.md`
