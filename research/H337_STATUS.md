# H337 STATUS

Updated: 2026-08-28
State: **CLOSED — k=3 POSTAL BUNDLE HAS A LEGAL ALL-ZERO-INSTANT BRANCH**

H225-X* remains CLOSED / EXHAUSTED at X20 and was not extended.

## Candidate
WinWink `MYSTERY CASH! £5,000 Jackpot prize!` is live with 122,667 total identifiers, £0.30 ticket price and 13,673 pre-committed instant-win positions.

Current WinWink Terms clause 3.13 converts one valid postal submission into `floor(second-class stamp / ticket price)` tickets. At the current Royal Mail £0.91 second-class price, this live game gives exactly **3 tickets per postal submission**.

## Exact result
- total identifiers: **122,667**;
- instant-win identifiers: **13,673**;
- zero-instant identifiers: **108,994**;
- bundle size: **3**;
- `108,994 >= 3`, so an all-zero-instant three-ticket allocation is legal;
- worst accepted-bundle withdrawable instant cash: **£0**;
- worst net before card/material/labour: **-£0.91**;
- arithmetic inconclusive: **0**;
- strict guarantee: **FAIL**.

The ordinary-post loss/delay branch remains an additional blocker but is not needed for closure.

## NEXT ACTION
Continue the k>=2 postal-bundle lane only on cheap live games where the exact zero-withdrawable-cash support is **strictly smaller than the postal bundle size**. For those survivors, compute the exact sum of the `k` smallest legal withdrawable-cash outcomes and compare that floor against complete marginal postal cost. Skip any game with zero-support count >= k.
