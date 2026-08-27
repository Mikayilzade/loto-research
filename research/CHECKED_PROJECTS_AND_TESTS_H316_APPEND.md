# Checked projects/tests — H316 append

## H316 — Punter Prizes CASH DASH 3 postal-bundle mechanism

Date checked: 2026-08-27
Disposition: **CLOSED / arithmetic + execution blocked**

Tested hypothesis: Punter Prizes' rule giving multiple entries per postal item for sub-postage ticket prices might create a deterministic acquisition subsidy for a finite no-margin competition.

Result:
- 20,000 tickets × £0.10 = £2,000 full paid acquisition;
- favourable total advertised liability = £2,000 face (10×£100 cash + 10×£100 ticket bundles; no end prize);
- full paid takeover therefore only breaks even;
- 91p second-class postage credits at most 9 ten-pence entries, so 20,000 postal entries require 2,223 letters costing £2,022.93;
- current residual pool is already below break-even: £1,800 favourable prize face vs £1,818.90 paid acquisition of all remaining tickets;
- 1,811 tickets were already externally sold;
- postal processing is non-atomic and can lose to paid cap fill.

Reusable rule learned: when a promoter credits no more than `floor(postage / ticket_price)` entries per separately posted item, the free postal route cannot have a lower effective per-entry acquisition cost than buying tickets normally.

Do not retest this exact Punter postal-value bundling unless terms or economics materially change.
