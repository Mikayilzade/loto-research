# H324 — Click Competitions free/multi-winner + low-odds finite-pool screen

Date checked: 2026-08-28
Status: CLOSED for the checked one-player takeover constructions; global research remains NO SUCCESS / NOT EXHAUSTED.

## Why this packet

The prior finite-pool work showed that cheap or free entry only matters for a strict guarantee if one player can eliminate every legal zero-cash outcome. H324 checks a different live operator pattern: (a) a genuinely free multi-winner cash draw, and (b) unusually cheap / unusually low-odds guaranteed cash draws.

## Live evidence

Click Competitions currently lists a free `£10,000 Giveaway! *40 WINNERS OF £250 TAX FREE CASH*` with a 300,000-entry cap. The operator page states a maximum of 49 entries per person and showed 2,367 entries at the checked snapshot. The same operator currently lists a £1,000 low-odds cash draw at £9.99 with 149 total entries and a 5-entry per-person cap. Current £10,000-for-2p and £20,000-for-2p draws have finite pools of 1,189,995 and 1,749,999 entries respectively, each with a 50,000-entry per-person cap.

Sources checked:
- Click operator page / free giveaway rules: https://www.clickcompetitions.co.uk/prizes/10-000-Giveaway-40-WINNERS-OF-250-CASH-31-09-26
- Click operator £1,000 low-odds page: https://www.clickcompetitions.co.uk/prizes/1-000-Tax-Free-Cash-Recurring
- Competition Showroom current Click snapshots for exact pool/cap arithmetic.

## Exact multi-winner blocker

For a draw choosing `k` winning entries without needing to choose any of ours, if at least `k` valid external entries can remain, there is a legal winner set consisting entirely of external entries. Therefore our strict cash floor from that draw is zero.

For the free £10,000 / 40-winner draw:
- total pool: 300,000;
- max one player: 49;
- checked entries: 2,367;
- even if all 49 allowed entries were already ours, at least `2,367 - 49 = 2,318` checked entries are external;
- 2,318 > 40 winner slots.

Hence there is a legal outcome in which all 40 £250 prizes go to external entries. The fact that our entries cost £0 does not create a guaranteed positive cash result; the strict floor remains £0.

## Stronger-than-real paid-draw checks

### £1,000 LOW ODDS
- 149 total IDs × £9.99 = £1,488.51 full-pool cost;
- prize = £1,000;
- impossible full-buyout gross ratio = 67.1813%;
- real cap is only 5 / 149 IDs.

So even removing the cap would still leave the full takeover below break-even.

### £10,000 for 2p
- 1,189,995 IDs × £0.02 = £23,799.90;
- prize = £10,000;
- impossible full-buyout gross ratio = 42.0170%;
- real cap = 50,000 IDs.

### £20,000 for 2p
- 1,749,999 IDs × £0.02 = £34,999.98;
- prize = £20,000;
- impossible full-buyout gross ratio = 57.1429%;
- real cap = 50,000 IDs;
- checked sold snapshot already leaves at least 1,005,034 external sold entries even under the most player-favourable attribution of the cap.

All three paid constructions are therefore closed twice: the one-player cap prevents deterministic takeover, and even impossible full-pool ownership is below strict break-even.

## Reusable gate

For a finite random-winner pool with `k` prizes, a one-player guaranteed-positive claim requires more than positive EV or cheap/free entries. At minimum, the player must force fewer than `k` external eligible identifiers to remain (and for a single-winner draw, zero external identifiers). If this fails, an all-external winner set remains legal and the player's strict cash floor from the draw is zero.

## Conclusion / NEXT ACTION

H324 is CLOSED for these current Click constructions. Do not repeat generic free multi-winner or 1p/2p cash draws unless the per-player cap / reservation mechanism changes enough to eliminate all legal external-winning sets, or the mechanism pays every eligible entry a positive deterministic cash amount.

Next useful search: electronic finite pools where the player can reserve essentially the whole winning support, or prize schedules that produce a positive per-entry cash floor rather than only a random winner set.
