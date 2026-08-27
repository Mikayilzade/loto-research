# H313 — Diamond Winners £15,000 Diamond Spins finite-pool bound

Date: 2026-08-27
State: **CLOSED / ARITHMETICALLY BELOW BREAK-EVEN**

## Why this candidate mattered

This live draw satisfies a structural gate that many earlier finite-pool candidates failed: the published maximum per person equals the full pool size. The operator states 119,999 total tickets and a maximum of 119,999 tickets per person. Therefore the per-player cap alone does not prevent a theoretical total takeover.

Live source: https://diamondwinners.co.uk/product/15000-diamond-spins-win-2000-instantly/

## Published live data

At the checked snapshot the operator page stated:
- £0.20 per entry;
- 119,999 total tickets;
- max 119,999 per person;
- 3,625 / 119,999 sold;
- advertised £15,000 total prize pool;
- 6,662 winning tickets;
- published cash schedule: 2×£2,000, 3×£1,000, 4×£500, 10×£100, 14×£75, 38×£25, 150×£10, plus site-credit prizes.

The published cash schedule totals exactly **£13,500**.

## Exact paid-takeover bound

Full one-copy paid acquisition:

`119,999 × £0.20 = £23,999.80`.

Even granting the impossible strongest case that one fresh player owns every ticket from inception and receives the entire advertised £15,000 prize pool at full face value:

`£15,000 / £23,999.80 = 62.5005208%`.

Deficit:

`£23,999.80 - £15,000 = £8,999.80`.

Cash-only instant prizes are still lower:

`£13,500 / £23,999.80 = 56.2504688%`.

Thus no execution detail can rescue the ordinary paid full-pool takeover: its strongest player-favourable liability bound is already far below break-even.

## Postal-route stress

The operator also offers a free postal-entry route, but requires each free entry separately and states that proof of posting does not guarantee inclusion; entries arriving after a cap is reached are not accepted.

Current Royal Mail 2nd Class letter/postcard postage is £0.91:
https://www.royalmail.com/sending/uk/2nd-class

A hypothetical 119,999-entry postal takeover would therefore have postage cost alone of:

`119,999 × £0.91 = £109,199.09`,

before card/material/time costs. The full advertised £15,000 prize pool is only **13.7363782%** of that postage cost. The nominally free route is therefore much worse economically than paid entry for this pool.

## Existing external identifiers

The live snapshot already had **3,625 sold**. For a fresh entrant, even ignoring the arithmetic failure, total ownership of all identifiers is no longer possible. This is an independent execution blocker for any main-draw or identifier-takeover argument.

## Conclusion

H313 is closed. It passes the rare `max_per_user = N` gate but fails the more fundamental economics gate decisively. Even impossible-perfect paid ownership returns at most 62.5005% at full advertised face value, and postal acquisition is more expensive still.

Do not reopen this exact draw unless ticket price or guaranteed player-facing liabilities change materially.

## NEXT ACTION

Continue searching finite pools where both conditions hold simultaneously:
1. the required winning identifiers can actually be monopolized/reserved by one eligible player; and
2. guaranteed cash/withdrawable liabilities are strictly greater than exact acquisition cost.

Prioritize fresh zero-sold pools, electronic reservation, deterministic cash rather than site credit, or a documented external discount/subsidy large enough to push a near-miss above 100%.
