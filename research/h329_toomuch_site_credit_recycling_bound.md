# H329 — Too Much `Every Ticket Wins` site-credit recycling bound

Date: 2026-08-28
State: **CLOSED / CREDIT-RECYCLING DOES NOT FORCE CASH**
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Question
Can a current `Every Ticket Wins` finite pool with guaranteed site-credit outcomes be converted into a strict guaranteed-cash-profit construction by repeatedly recycling site credit into more tickets?

## Current live witness
Too Much Competitions currently lists `£10,000 BANK – INSTANT FLIP – EVERY TICKET WINS (£100 End Prize)` with:
- 75,000 finite tickets;
- £0.25 per ticket;
- current live listing on the operator site;
- current snapshot 1,662/75,000 sold on the operator home page checked 2026-08-28;
- separate £100 end prize.

Current operator source:
- https://toomuchcompetitions.co.uk/

Independent current listing cross-check:
- https://www.competitionshowroom.com/competition/toomuchcompetitions-10000-bank-instant-flip-every-ticket-wins-100-end-prize

The operator's recent instant-win result ledger contains actual £0.05 and £0.10 Site Credit outcomes in late July / early August 2026, proving that site-credit-only outcomes remain an operative prize type on the platform:
- https://toomuchcompetitions.co.uk/draw-results/instant-win/

Historic operator pages for the same `Every Ticket Wins` mechanic explicitly describe residual tickets as site credit rather than withdrawable bank cash, e.g. 38,828 × £0.05 Site Credits in a 39,999-ticket pool:
- https://toomuchcompetitions.co.uk/competition/instantwin39-big-bank-25000-every-ticket-wins-end-prize-500/

The operator also describes site credit as value to spend on other competitions, rather than as a bank withdrawal:
- https://toomuchcompetitions.co.uk/competition/double-or-nothing-10-20-in-too-much-credit-50-50-odds/

## Exact theorem: non-cash credit recycling cannot create a strict cash floor by itself
Let a purchased ticket cost `p` cash or site credit. Suppose a legal ticket outcome can return only non-withdrawable site credit `c` and zero withdrawable cash. If that credit is reinvested into another competition for which a legal zero-withdrawable-cash outcome also exists, then the combined two-stage strategy still has a legal path with zero withdrawable cash.

Inductively, any finite recursive strategy made only from such credit-funded continuations has a legal all-credit/no-cash path unless some reachable continuation has a strictly positive withdrawable-cash floor for **every** legal outcome.

Therefore `every ticket wins something` is not enough. The relevant condition is:

`minimum withdrawable cash over every reachable terminal path > external cash spent`.

Site credit only changes future purchasing power. It does not by itself raise the guaranteed withdrawable-cash floor.

## Application to the current Too Much route
The current live competition is explicitly an `Every Ticket Wins` Instant Flip. The operator's recent result ledger establishes live use of £0.05 / £0.10 Site Credit outcomes, and the platform defines site credit as spendable on other competitions. Thus a site-credit-only branch cannot be counted as current bank cash.

Even granting the strategy perfect reinvestment with no friction, a recursive credit strategy is rigorous only if it eventually enters a continuation whose **every** legal outcome produces enough withdrawable cash. No such continuation is established in the current checked Too Much catalogue; the current catalogue itself contains ordinary random draw / instant-win competitions with legal non-cash or losing branches.

Hence there remains a legal strategy path with zero withdrawable cash from the credit-recycling portion. The separate £100 end draw likewise has zero strict floor for a small portfolio while external valid identifiers exist.

## Stronger arithmetic sanity check
Full paid acquisition of the current 75,000-ticket pool would cost:

`75,000 × £0.25 = £18,750`.

The live third-party listing reports a £10,000 prize-value basis plus a £100 end prize description. Even granting £10,100 as fully withdrawable cash gives only:

`£10,100 / £18,750 = 53.8666667%`.

This is only a sanity check, not the closure proof, because the current full prize decomposition is not published in the live search result. The rigorous closure is the credit-path theorem: site credit cannot be promoted to guaranteed cash without a separately proved positive-cash-floor continuation.

## Zero-inconclusive condition
H329 does **not** require knowing the exact current count of £0.05 versus £0.10 residual IDs, nor does it require assuming a specific current prize decomposition. Its closure claim is limited to the proposed **site-credit recycling mechanism**. The operator documents site credit as non-cash purchasing value and recent legal site-credit-only instant outcomes exist. Therefore the mechanism cannot itself establish a positive withdrawable-cash floor.

## Result
**H329 CLOSED / CREDIT-RECYCLING DOES NOT FORCE CASH.**

Do not treat nominal site-credit recycling as a deterministic subsidy unless a specific continuation is separately proved to have a positive withdrawable-cash floor on every legal outcome.

## NEXT ACTION
Search for a genuinely different live mechanism where either:
1. every possible ticket outcome directly has positive **withdrawable cash** above effective acquisition cost; or
2. site/promotional credit has an explicit cash-withdrawal right; or
3. a credit-funded continuation has a separately proved all-outcome positive withdrawable-cash floor; or
4. exact selectable/reservable winning identifiers eliminate all zero-cash support before payment.
