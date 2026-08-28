# H345 STATUS

Updated: 2026-08-29
State: **CLOSED — NOT SUCCESS**

H225-X* was checked first and remains **CLOSED / EXHAUSTED** at H225-X20 with exactly 0 coefficient survivors / 0 legal shift tuples. No X21/X22 continuation was created.

## Completed checkpoint
H345 tested a materially stronger live postal candidate than H344: Palladium Competitions `Always A Winner™️ | Every Ticket Wins | Over £100,000 Worth of Instant Wins`, scheduled to close/draw 8 Sep 2026.

Published live parameters:
- total identifiers: **20,000**;
- ticket price: **£10.00**;
- per-person cap: **1,000**;
- page states **every ticket is a winner**;
- advertised prize range: **£2 to £2,000**;
- free postal entry is explicitly available;
- current Royal Mail Second Class letter/postcard postage: **£0.91**.

This is the first checked candidate in the current lane whose advertised minimum nominal prize exceeds postage for a single postal allocation: `£2.00 - £0.91 = +£1.09` before postcard/material cost. H345 therefore crosses the H344 arithmetic screening hurdle at the advertised-value level.

## Strict guarantee blocker
The governing Palladium T&C 6.12-6.13 expressly preserve a legal dispatch-without-entry branch:
- entries may be lost, damaged, delayed, destroyed, incomplete or misdirected;
- proof of posting does not guarantee entry;
- each postal entry must be sent separately;
- an entry received only after the competition reaches its cap is automatically voided;
- no refund of incurred entry-related costs is due.

Therefore a compliant entrant can incur at least the £0.91 postage cost and receive **zero allocated ticket / zero prize**. Strict dispatch-to-settlement floor is consequently at most:

`£0.00 - £0.91 = -£0.91`

before the postcard/material/labour cost.

This closes H345 even under the stronger hypothetical assumption that every accepted ticket pays at least £2 as immediately withdrawable cash.

## Additional source warning
The competition page currently renders the explicit banner `This is a demo store for testing purposes — no orders shall be fulfilled.` This is independently incompatible with certifying live executable fulfillment. H345 does not need this warning for the mathematical closure because the governing postal non-acceptance branch already suffices.

## Validation state
- H225 exact-family inconclusive: **0** (terminal certificate unchanged).
- H345 dispatch-cost arithmetic inconclusive: **0**.
- H345 acceptance-branch inconclusive relevant to closure: **0** (branch is explicit in governing terms).
- Full instant-prize class vector / cash convertibility: **not reconstructed and not required for closure**.
- Overall result: **NOT SUCCESS**.

## NEXT ACTION
Do not spend exact-vector effort on another ordinary postal candidate merely because its accepted-entry minimum exceeds postage. The next useful candidate must remove the dispatch-without-entry branch itself: prioritize a **binding zero-cost digital/telephone/free-web route with confirmed accepted allocation**, then require every reachable allocation to have strictly positive withdrawable-cash floor after all unavoidable costs. Postal candidates should only reopen if the governing mechanism itself guarantees acceptance or refunds all dispatch cost on non-acceptance.
