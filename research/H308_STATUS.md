# H308 STATUS — CrazyWins zero-sold finite-pool / postal free-entry takeover

Updated: 2026-08-27
Branch: `research-work`
State: **CLOSED / EXECUTION-BLOCKED**

## Why this packet was opened

After H306-H307, the next target class was a fresh finite pool with zero observed sales and a free/discounted route that might reserve the same identifiers cheaply enough for deterministic takeover.

CrazyWins surfaced an indexed current candidate, **HAMSTER FRENZY**, advertised at £0.10 per paid ticket with a 2,000-entry finite pool and an indexed snapshot showing 0 tickets sold, closing 29 Aug 2026.

## Exact acquisition comparison

For a 2,000-entry pool:

- paid full-pool acquisition at £0.10 each = **£200.00**;
- CrazyWins free route requires each free entry to be submitted separately by post;
- current Royal Mail 2nd Class letter/postcard price = **£0.91**;
- postage-only cost for 2,000 separate free entries = **£1,820.00**;
- therefore the nominally 'free' route costs **9.1x** the paid-ticket face cost before postcard/material/time costs.

So this free-entry route is not a cheap takeover mechanism even under perfect acceptance.

## Rigorous execution blocker

CrazyWins Terms independently prevent certifying deterministic full ownership:

1. Free entries must be posted separately; bulk entries count as one.
2. Proof of posting does **not** guarantee inclusion.
3. If the pool reaches its cap before a postal entry is received, that entry is not admitted.
4. Paid entrants are randomly allocated entry numbers after completion/payment; free entrants are also allocated numbers by RNG.
5. The terms allow competition-specific maximum entries per entrant.

Thus an observed zero-sold snapshot is not equivalent to a reservable zero-owned pool. There is no published atomic transaction that locks all 2,000 identifiers before outsiders can enter, and the postal route expressly leaves nonreceipt/cap-race branches.

A single externally controlled eligible identifier is enough to preserve a legal main-draw outcome where our portfolio loses the final prize. Therefore no strict guaranteed-profit takeover can be certified from this mechanism.

## Terminal conclusion

**H308 CLOSED / EXECUTION-BLOCKED.**

Do not reopen CrazyWins postal-free finite pools unless a materially different route appears that:

- electronically and immediately reserves the same finite identifier inventory;
- permits enough entries per eligible player to control the full required set;
- has deterministic acquisition cost below the guaranteed player-facing liability; and
- cannot be partially displaced by competing entrants before confirmation.

## Files

- `research/h308_crazywins_zero_sold_postal_takeover.md`
- `src/loto_research/h308_crazywins_zero_sold_takeover.py`
- `data/derived/h308_crazywins_zero_sold_takeover.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H308_APPEND.md`
