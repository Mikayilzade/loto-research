# H318 — SOBO same-pool free-entry / finite-cap bound

Date checked: 2026-08-27
State: **CLOSED / TAKEOVER-BLOCKED**

## Why this was worth checking

The post-H317 NEXT ACTION is to find a finite pool where a free/discount route consumes the same inventory and is reserved electronically, so that cheap entries might monopolize all winning identifiers. SOBO is unusually close to that target: its August 2026 Competition Rules say free entries are allocated from the **same pool** as paid entries, and the rules text describes an on-site free-entry form as an alternative to post.

That lead is not enough for a strict guarantee.

## Current live draw checked

SOBO's current `Win a £200 Local Experience` page publishes:

- advertised prize value: **£200**;
- paid entry price: **£1**;
- finite ticket count: **299**;
- current snapshot: **0/299 sold**;
- maximum entries per person: **25**;
- tickets held for 10 minutes during payment;
- free entry route available;
- ticket numbers allocated randomly.

Source: https://sobocompetitions.com/competitions/200-local-experience

The August 2026 Competition Rules publish two additional gates:

- free route: **one free entry per person per competition**;
- the per-person maximum is enforced across paid and free entries combined;
- entries are allocated ticket numbers from the same finite pool;
- attempts to evade the limit with multiple accounts void the related entries.

Source: https://sobocompetitions.com/competition-rules

The rules page labels itself a draft pending UK-qualified-solicitor review, while the live draw page itself says `free postal entry`. Therefore H318 does **not** rely on the draft's apparent electronic-form wording as an enforceable execution right. The closure below is stronger: even granting same-pool electronic free allocation, the cap still kills takeover.

## Exact one-player bound

For the live draw:

`N = 299`, `M = 25` maximum entries/person.

Therefore at least

`299 - 25 = 274`

valid identifiers remain outside any one player's portfolio.

The winner is selected from valid entries. Hence there is a legal outcome where one of those 274 external identifiers wins. The strict one-player main-draw cash floor is therefore **£0**.

Maximum possible one-person control is only:

`25 / 299 = 8.3612040134%`.

The one-free-entry route does not change this: it is inside the same 25-entry cap and is itself limited to one free entry/person/competition.

## Stronger impossible-perfect economics

Ignore the real 25-entry cap entirely and grant impossible ownership of all 299 tickets at the published £1 paid price:

- full acquisition cost: **£299**;
- advertised prize value: **£200**;
- gross ratio: **200 / 299 = 66.8896321070%**;
- deficit: **£99**.

So even a hypothetical cap-free paid full takeover is below break-even before execution friction. The free route would need to supply at least 100 of the 299 entries at zero marginal cost to make the £200 prize exceed paid acquisition cost; the published free allowance is one.

## Conclusion

**H318 CLOSED / TAKEOVER-BLOCKED.**

SOBO is useful evidence that same-pool free entry plus electronic ticket holding exists as a nearby mechanism class, but this live implementation cannot support deterministic profit because:

1. the one-person cap is only 25/299;
2. free entry is limited to one/person/competition and shares the overall cap;
3. at least 274 external winning identifiers necessarily remain;
4. even impossible cap-free paid full ownership returns only 66.8896% of acquisition cost.

Reusable gate: for a finite single-winner pool, a same-pool subsidy is irrelevant to strict one-player takeover unless the enforceable per-person cap is at least the number of identifiers that must be controlled. If `M < N`, an external winning identifier remains legal unless the payout structure gives every controlled subset a separate deterministic cash floor.

## Reproducibility

- `src/loto_research/h318_sobo_same_pool_free_entry_bound.py`
- `data/derived/h318_sobo_same_pool_free_entry_bound.json`
- `research/H318_STATUS.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H318_APPEND.md`
