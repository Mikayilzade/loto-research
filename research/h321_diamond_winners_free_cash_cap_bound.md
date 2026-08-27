# H321 — Diamond Winners £100 electronic-free-entry cap bound

Date checked: 2026-08-28
State: **CLOSED / CAP-BLOCKED**

## Why this was worth testing

The H320 NEXT ACTION asked for a genuinely different mechanism where a deterministic subsidy is electronic rather than postal and acts on the same finite competition inventory. Diamond Winners currently publishes exactly such a mechanism:

- `£100 Cash! Facebook VIP Group Exclusive`;
- advertised entry price £10;
- a **100% OFF discount code** in the Facebook group, explicitly described as a free entry;
- hard competition cap 1,000 entries;
- main prize £100 cash;
- live draw scheduled for 6 September 2026.

Operator page:
https://diamondwinners.co.uk/product/100-cash-facebook-vip-group-exclusive-3/

Terms:
https://diamondwinners.co.uk/terms-conditions/

This removes the postage-cost and postal-delay defect seen in H302/H306/H308: the promotional route itself is an electronic 100%-discounted purchase path.

## Governing limits and draw rule

The same live page states:

- maximum tickets for the competition: **1,000**;
- maximum tickets per person: **1**.

The governing Terms say a Main draw selects the winner by random draw from all valid Entrants (clause 4.1(a)); auto-draw language likewise selects a winner from all valid entries (4.1(c)). The one-account-per-person rule also prevents multiplying the cap through extra accounts (3.6).

Therefore a strict one-player guarantee would require eliminating every possible external valid entry. The actual person cap makes that impossible once even one external entry exists.

## Fresh live-state check

During H321 the live page showed **178 / 1,000** entries already present. To make the bound stronger than necessary, suppose one of those 178 entries were somehow ours already. At least

`178 - 1 = 177`

valid entries are still necessarily external.

There is therefore a legal draw state in which one of those external entries wins the £100 cash prize. In that state our withdrawable-cash return is exactly £0.

The advertised identifier-space control ceiling is only

`1 / 1000 = 0.1%`.

Even at a £0 effective entry cost, a positive expected value or attractive free chance is not the target criterion: the target is **strict positive profit in every legal outcome**. The legal external-winner outcome keeps the strict cash floor at zero.

## Stronger structural conclusion

The result does not depend on whether the discount code is easy to obtain, whether checkout reservation is atomic, or whether all 1,000 tickets eventually sell.

For a main draw from valid Entrants:

> If a player cannot prevent at least one external valid entrant from existing, then there is a legal external-winner state and the player's guaranteed cash floor from that draw is zero.

Here the explicit one-entry person cap and already-existing entries make that condition decisive.

## Exact result

- effective cost of the one allowed promotional entry: £0 under the advertised 100% code;
- maximum entries controlled by one person: 1;
- observed entries: 178;
- minimum external entries even under the player-favourable assumption that one observed entry is ours: 177;
- strict withdrawable-cash floor: **£0**;
- status: **CLOSED / CAP-BLOCKED**.

## Reproducible files

- `src/loto_research/h321_diamond_winners_free_cash_cap_bound.py`
- `data/derived/h321_diamond_winners_free_cash_cap_bound.json`
- `research/H321_VALIDATION.md`
- `research/H321_STATUS.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H321_APPEND.md`

## NEXT ACTION

Do not reopen one-entry free giveaways as guaranteed-profit candidates merely because the acquisition cost is zero. Continue searching for an electronic deterministic subsidy where the real per-person cap is large enough to eliminate every external winning state, or for a finite guaranteed-liability pool whose worst-case player-facing cash value exceeds exact acquisition cost.
