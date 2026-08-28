# H329 VALIDATION

Date: 2026-08-28

Independent validation for `h329_toomuch_site_credit_recycling_bound`.

## Current live inputs
- Live Too Much pool: 75,000 tickets.
- Ticket price: £0.25.
- Operator home-page snapshot checked 2026-08-28: 1,662 sold.
- Competition title: `£10,000 BANK – INSTANT FLIP – EVERY TICKET WINS (£100 End Prize)`.
- Recent operator result ledger contains £0.05 and £0.10 Site Credit outcomes.
- Operator describes site credit as value to spend on other competitions, not direct bank cash.

## Recomputed arithmetic
- Full paid acquisition: `75,000 × £0.25 = £18,750`.
- Deliberately favourable headline stress: `£10,000 + £100 = £10,100`.
- Stress ratio: `£10,100 / £18,750 = 0.5386666667`.

This full-pool arithmetic is only a sanity check because the current live prize decomposition is not fully exposed in the indexed page.

## Credit-path proof
Let a legal outcome return site credit and zero withdrawable cash. If site credit is not directly withdrawable, using it to buy another random competition does not itself create cash. If that continuation also has a legal zero-withdrawable-cash branch, then the two-step strategy retains a legal zero-cash terminal path. Repeating the argument proves the same for any finite recursive credit chain.

Therefore credit recycling can only establish a positive strict cash floor if some reachable continuation is separately proved to pay positive withdrawable cash on every legal outcome.

The checked current Too Much catalogue does not provide such a certified continuation. Thus H329 closes the **credit-recycling mechanism**, not every conceivable future Too Much promotion.

## Zero-inconclusive condition
No unresolved count of specific residual instant-win IDs is needed for this mechanism-level closure. The only required facts are:
1. legal site-credit-only outcomes exist on the platform;
2. site credit is purchasing value rather than directly withdrawable bank cash;
3. no separately certified all-outcome positive-cash continuation is supplied.

Validated result: **site-credit recycling alone has strict guaranteed withdrawable-cash floor £0; H329 CLOSED for this mechanism.**
