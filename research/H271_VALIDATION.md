# H271 validation certificate

Validated: 2026-08-25
Packet: `H271`
Result: **CLOSED / REJECTED**
Global result: **NO SUCCESS; NOT EXHAUSTED**

## Rule facts independently checked

1. UK Millionaire Maker is a separate raffle attached automatically to each UK EuroMillions entry.
2. The raffle number is automatically generated; the player does not select it.
3. The winning raffle number is selected from the valid generated raffle numbers.
4. Current UK EuroMillions line price is £2.50.
5. The ordinary Millionaire Maker winner-facing prize is £1,000,000.

## Arithmetic gates

- raffle-only break-even count: `1,000,000 / 2.50 = 400,000` paid lines;
- strict raffle-only positive-gross ceiling: **399,999 lines**;
- exact EuroMillions main matrix: `C(50,5) * C(12,2) = 139,838,160`;
- one-copy main-space cover cost: **£349,595,400**;
- one £1m raffle prize / that cover cost: **0.0028604495368074064 = 0.2860449537%**.

## Guarantee gate

Let `P` be the portfolio-owned set of generated raffle codes and `E` the externally owned valid generated codes. If `E` is nonempty, choose any `e in E`. Because the raffle draw is made from valid generated codes, `e` is a legal winning outcome. On that outcome the portfolio's Millionaire Maker payout is zero.

Therefore a positive worst-case Millionaire Maker payout requires `E = empty`, i.e. certified ownership of every eligible generated code. The checked rules expose no reservation/buyout mechanism that can enforce this while public sales remain open and new codes are generated for outside purchases.

This blocker is independent of main-number coverage and independent of the size of the syntactic raffle-code namespace.

## Closure scope

Closed: strict guaranteed-profit constructions that rely on monopolizing the ordinary UK Millionaire Maker guaranteed winner under the checked issuance rules.

Not claimed: that Millionaire Maker has negative expected value in every promotional configuration; that future special events cannot change the result; or that a future hard-capped reservable code issuance would fail.

Reopen only on a material rules change establishing a hard pre-draw cap plus executable ownership/reservation of all eligible codes, or a deterministic subsidy that pays each owned selection independently of which raffle code wins.
