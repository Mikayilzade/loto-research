# H348 — South Africa PowerBall 2026 fixed-tier / XTRA cascade screen

Date: 2026-08-29

## Scope
Screen the post-1-Jun-2026 South Africa PowerBall matrix against global NEXT ACTION #1, then test whether the new PowerBall XTRA monthly Jackpot Cascade can create a deterministic additive subsidy.

## Current rules used
- Main matrix: choose 5 of 50 plus 1 PowerBall of 16.
- Main PowerBall price: R10 per board.
- Main lower fixed prizes: 4=R2,000; 3+PB=R500; 3=R100; 2+PB=R100; 1+PB=R20; PB-only=R10.
- XTRA uses the same selected board for an additional R5; its corresponding fixed tiers are exactly half: R1,000/R250/R50/R50/R10/R5.
- XTRA final/terminal monthly draw cascades an unwon jackpot to Division 2, then Division 3 if needed.

## Exact one-copy cover
Legal boards = C(50,5)*16 = **33,900,160**.

Relative to any draw, exact board counts are:
- 5+PB: 1
- 5 without PB: 15
- 4+PB: 225
- 4 without PB: 3,375
- 3+PB: 9,900
- 3 without PB: 148,500
- 2+PB: 141,900
- 1+PB: 744,975
- PB only (0 main + PB): 1,221,759
- all remaining non-winning patterns complete the partition.

All 12 exact (main-match count 0..5) x (PB hit/miss) cells sum to **33,900,160 / 33,900,160**.

Main fixed-tier gross = **R67,857,090** against **R339,001,600** cost, return **20.0167465284%**.

If every board also buys XTRA, XTRA fixed-tier gross = **R33,928,545**, while XTRA incremental cost is R169,500,800. Combined main+XTRA fixed gross = **R101,785,635** against **R508,502,400**, the same **20.0167465284%** fixed-tier return.

## Cascade theorem
The new XTRA cascade is real, but it cannot be forced by any nonempty chosen-number portfolio. Every purchased board is itself a legal XTRA Division-1 outcome. Therefore every nonempty portfolio preserves at least one legal draw state in which the player creates a D1 winner and the no-D1 cascade condition is false.

A complete cover makes this stronger: it guarantees exactly one own D1 board for every XTRA draw, so complete coverage prevents the cascade rather than harvesting it.

Thus the accumulated jackpot is not a deterministic additive subsidy to the fixed tiers. External duplicate/winner counts only weaken any strict guarantee further.

## Result
**CLOSED / NOT SUCCESS.** Fixed lower tiers are only ~20.0167% of acquisition cost, and the monthly XTRA cascade cannot be forced by a nonempty portfolio.

Arithmetic inconclusive: **0**.
Closure-relevant inconclusive: **0**.

Sources checked: current 2026 South Africa PowerBall/PowerBall XTRA rule summaries and post-June-2026 cascade reporting; see H348 validation/status for the exact checkpoint.
