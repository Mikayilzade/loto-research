# H317 STATUS — Universal Competitions stop-on-hit cash pool

Updated: 2026-08-27
State: **CLOSED / NO SUCCESS**

## Terminal checkpoint

Current Universal Competitions `£100 CASH!! 1 PRIZE! CAN GO ANYTIME!!!! £100 Cash Jackpot!!` uses a finite 3,999-ticket pool at £0.10 and stops when the instant cash is won, then draws a jackpot winner from entries sold up to that stopping point.

Snapshot checked:
- sold: **1,135 / 3,999**;
- remaining: **2,864**;
- remaining-tail acquisition cost: **£286.40**.

Player-favourable payout bound:
- £100 instant cash;
- plus a deliberately generous separate £100 jackpot upper bound;
- total forced-liability upper bound: **£200**.

Therefore even impossible-perfect ownership of every remaining identifier yields at most

`£200 / £286.40 = 69.83240223% gross`.

The pool is closed by arithmetic before execution issues matter. Atomic checkout, ticket reservation, and operator acceptance cannot turn this live version into strict guaranteed profit.

## Reusable gate

For any finite competition that stops once a special identifier is hit, a necessary takeover condition is:

`total forced liability after monopolizing the remaining tail > remaining ticket count × ticket price`.

If this fails, the stopping-time mechanic is irrelevant to guaranteed profit.

## NEXT ACTION

Do not reopen H317 unless a later stop-on-hit pool crosses the inequality above. Continue searching for a genuinely new finite mechanism with:
- liabilities above exact remaining-tail acquisition cost; or
- electronically reservable prize-bearing identifiers; or
- a deterministic external subsidy that closes the precise takeover gap.

H225-X* remains separately `CLOSED / EXHAUSTED` at X20 and must not be extended without changing the mathematical family.
