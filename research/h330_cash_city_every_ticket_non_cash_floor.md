# H330 — Cash City `EVERY TICKET WINS` non-cash floor

Checked: 2026-08-28
State: **CLOSED / NON-CASH EVERY-TICKET-WINS**

## Live witness

Cash City Draws currently lists `Cash City Ticket Bundle – EVERY TICKET WINS`, closing 31 Aug 2026, at **£2.50 per entry** with **150 total IDs**, **53 sold / 97 left**, and **15 max entries per person**.

The complete published instant-prize taxonomy is:

- 40 IDs: 3 Paw Patrol competition entries + 1 site-credit competition entry;
- 20 IDs: 3 Paw Patrol competition entries + 1 Dior competition entry;
- 36 IDs: 14 SnoozeBand competition entries;
- 22 IDs: 7 Dior competition entries;
- 32 IDs: £2.50 site credit.

These counts sum exactly to **150**. Their current `Tickets Left` counts are 28 + 14 + 25 + 12 + 18 = **97**, exactly matching the page-level 97 remaining IDs. No category is missing from the published instant schedule.

The competition description explicitly says that for £2.50 the player wins money back **in site credit or competition entries**, and the separate main prize is **£20 site credit**. It also says that when downstream entry limits are exceeded, the replacement is equivalent **site credit**.

## Governing cash gate

Cash City's general Terms distinguish an ordinary Prize from an optional alternative `Cash Prize`. Clause 6.5 says that an alternative cash prize is available only for some competitions and, where offered, its amount is stated in the prize description. This H330 prize description states no cash alternative.

Therefore H330 has no documented deterministic path from every legal instant outcome to withdrawable cash. The terminal main prize is also site credit. At least one legal player path is consequently:

`paid entry -> site credit / downstream competition entry -> no guaranteed bank cash`.

The strict withdrawable-cash floor is therefore **£0**.

## Exact validation

The executable audit checks:

- class totals = 150;
- live class-left totals = 97;
- sold + left = 150;
- max-per-person 15 < total pool 150;
- strict cash floor = £0;
- inconclusive arithmetic checks = 0.

The max-person cap is not needed for the zero-cash proof, but independently prevents one player from taking over the finite pool.

## Conclusion

`EVERY TICKET WINS` is insufficient when the guaranteed outcomes are only reusable site credit or entries into other random competitions. Unless site credit itself is explicitly withdrawable as cash, or every reachable continuation is independently proved to have a positive cash floor, recursive prize recycling does not create a strict guaranteed-profit strategy.

## Reopen condition

Reopen only if Cash City publishes one of:

1. explicit site-credit-to-bank withdrawal rights;
2. a cash alternative for this exact competition;
3. a downstream entry route whose every legal outcome has positive withdrawable cash above effective acquisition cost.

Sources checked: live competition page and Cash City governing Terms, 2026-08-28.
