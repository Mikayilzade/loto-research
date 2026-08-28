# H343 STATUS

Updated: 2026-08-28
State: **CLOSED — NOT SUCCESS**

H225-X* was checked first and remains **CLOSED / EXHAUSTED** at H225-X20 with exactly 0 coefficient survivors / 0 legal shift tuples. No X21/X22 continuation was created.

## Completed checkpoint
H343 tested the new cheap-bundle subcase that H337 did not close: a live competition where **every ticket wins**, but a valid postal submission receives multiple low-price tickets.

Candidate: Jackpotz Competitions `Trash or Treasure?`, live to 13 Sep 2026, standard online price **£0.15** per ticket, advertised `Every ticket wins` and `3p to £500 Wins`.

Jackpotz's current postal rules state that each valid free postal submission is credited with ticket value equal to one current Royal Mail Second Class stamp; if ticket price is lower, the ratio is rounded **up** to a whole number of tickets. Royal Mail currently lists a Second Class letter/postcard stamp at **£0.91**. Therefore one accepted submission receives `ceil(0.91 / 0.15) = 7` ticket entries.

For a strict upper-bound closure H343 deliberately grants the entrant the favorable interpretation that the advertised **3p minimum is withdrawable cash on every one of all seven tickets**. Even then the bundle floor is only `7 × £0.03 = £0.21`, against **£0.91 postage**, so net is at most **-£0.70** before postcard/material/labour costs.

This closes the candidate without needing the full prize vector, ticket allocation order, or any mail-loss assumption. If some 3p outcomes are site coins rather than cash, the true cash floor is lower, never higher.

Arithmetic inconclusive: **0**. Route/convertibility inconclusive relevant to closure: **0**.

## NEXT ACTION
For low-price multi-ticket postal routes, apply the new pre-screen `k * minimum_withdrawable_cash > postage` before reconstructing a full prize vector. Deep analysis is warranted only when that strict hurdle is crossed; otherwise the candidate is mathematically closed even if every ticket wins.
