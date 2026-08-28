# H343 — Jackpotz every-ticket-wins postal-bundle hurdle

Date: 2026-08-28
State: **CLOSED — NOT SUCCESS**

## Question
H337 closed cheap postal bundles when the number of zero-cash identifiers was at least the postal bundle size. H343 asks a different question: can a cheap competition survive if it advertises that **every ticket wins**, so the zero-support test is unavailable?

## Live candidate
Jackpotz Competitions currently lists `Trash or Treasure?` in its Every Ticket Wins section with:
- end date: 13 September 2026;
- standard entry price: **£0.15**;
- label: **Every ticket wins**;
- advertised outcome range: **3p to £500 Wins**.

The governing Jackpotz postal-entry page states that one valid postal submission receives entry value equal to the current standard Royal Mail Second Class stamp. Where the ticket price is lower than the stamp value, stamp value is divided by ticket price and any fractional result is rounded **up** to the next whole ticket.

Royal Mail's current official Second Class price is **£0.91** for a letter/postcard up to 100g.

Thus the exact allocation count is:
`k = ceil(£0.91 / £0.15) = ceil(6.0666...) = 7 tickets`.

## Strong favorable bound
To avoid relying on ambiguity over cash versus site coins, grant an intentionally stronger-than-published condition: assume **every one of the seven allocated tickets pays the advertised minimum 3p as immediately withdrawable cash**.

Then:
- guaranteed gross upper-bound floor = `7 × £0.03 = £0.21`;
- unavoidable postage = `£0.91`;
- net floor upper bound = `£0.21 - £0.91 = -£0.70`.

This is already negative before the postcard itself, writing/printing, account administration or delivery-risk friction. Therefore no interpretation of the actual game consistent with a 3p minimum can turn this particular postal bundle into a strict guaranteed profit.

## Why this is new
The earlier H337 shortcut was `zero-cash support >= k`. H343 establishes a second independent cheap-bundle rejection rule that works even when **zero-cash support is zero**:

`if k * m <= postage, strict guaranteed profit is impossible`,

where `k` is the maximum tickets allocated by one qualifying postal submission under the binding rule and `m` is a player-favorable upper bound on the minimum withdrawable cash per allocated ticket.

For H343, `k=7`, `m=£0.03`, and `k*m=£0.21 < £0.91`.

## Validation accounting
- allocation arithmetic inconclusive: **0**;
- postage-price inconclusive: **0**;
- prize-vector inconclusive relevant to closure: **0** (full vector unnecessary under the dominating 3p-per-ticket favorable bound);
- cash/site-coin ambiguity relevant to closure: **0** (resolved by assuming the stronger all-cash interpretation);
- mail acceptance/loss inconclusive relevant to closure: **0** (not needed; accepted-entry economics already fail).

## Result
**CLOSED / NOT SUCCESS.** This candidate cannot yield a strict positive postal-entry floor.

## NEXT ACTION
Scan current low-price every-ticket-wins competitions using the hurdle `ceil(S/p) * m > S`, where `S` is binding postal cost/value, `p` ticket price and `m` minimum withdrawable cash. Only reconstruct full vectors for candidates that pass this necessary condition.

Sources:
- https://jackpotzcompetitions.com/app/
- https://jackpotzcompetitions.com/shop/
- https://jackpotzcompetitions.com/postal-entry/
- https://jackpotzcompetitions.com/terms-conditions/
- https://www.royalmail.com/sending/uk/2nd-class
