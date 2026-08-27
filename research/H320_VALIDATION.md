# H320 INDEPENDENT VALIDATION

Date: 2026-08-27
Result: **VALIDATED / CLOSED**

This validation recomputes the decisive H320 quantities independently from the research narrative.

## Source facts checked

Current indexed Prizle `Grab A Prize` material states:

- 8,000 tickets / instant prizes;
- £4.99 per ticket;
- maximum 1,000 entries per person;
- every ticket guarantees an instant win;
- site-credit tiers: 39×£25, 80×£10, 1,600×£5, 502×£3, 1,779×£2, 1,000×£1, 1,000×£0.50, 500×£0.25, 300×£0.10, 100×£0.05, 100×£0.01;
- cash tiers: 1×£100, 20×£10, 50×£5, 400×£2, 500×£1;
- 29 product/gift identifiers in the displayed schedule;
- a separate £500 end draw.

Source checked: `https://prizle.co.uk/competitions/grabaprize-4`.

## Independent arithmetic

Site-credit count:

`39 + 80 + 1600 + 502 + 1779 + 1000 + 1000 + 500 + 300 + 100 + 100 = 7000`.

Cash count:

`1 + 20 + 50 + 400 + 500 = 971`.

Non-site product/gift count: **29**.

Inventory identity:

`7000 + 971 + 29 = 8000`.

Site-credit full face:

`39×25 + 80×10 + 1600×5 + 502×3 + 1779×2 + 1000×1 + 1000×0.5 + 500×0.25 + 300×0.1 + 100×0.05 + 100×0.01 = £16,500`.

Cash instant face:

`1×100 + 20×10 + 50×5 + 400×2 + 500×1 = £1,850`.

The current page's `to be won` counts leave **6,985** site-credit-only identifiers available. Since `6,985 > 1,000`, the complete one-player cap can legally consist only of nonwithdrawable site-credit instant wins.

The current 1,000-cheapest distinct available site-credit identifiers total:

`100×0.01 + 100×0.05 + 298×0.10 + 500×0.25 + 2×0.50 = £161.80`.

Paid maximum:

`1000 × £4.99 = £4,990`.

Site-credit face ratio:

`£161.80 / £4,990 = 0.0324248496993988 = 3.24248497%`.

This is not a withdrawable-cash ratio.

## Guarantee check

A strict cash-profit construction must succeed for every legal allocation/outcome. The following legal joint outcome exists:

1. all 1,000 player instant identifiers are chosen from the 6,985 currently available site-credit-only identifiers;
2. none of those entries receives a cash/product instant prize;
3. an external entry wins the separate £500 end draw.

Player withdrawable cash in that outcome: **£0**.

Therefore the strict withdrawable-cash floor is exactly **£0** and cannot exceed acquisition cost.

## Verdict

H320 is correctly classified **CLOSED / ZERO-WITHDRAWABLE-CASH-FLOOR**.

This does not claim that Prizle site credit is worthless; it states only that positive site-credit face value is not, by itself, a deterministic withdrawable-cash guarantee. A future packet may reopen the broader mechanism only if a separate deterministic site-credit-to-cash conversion construction is established.
