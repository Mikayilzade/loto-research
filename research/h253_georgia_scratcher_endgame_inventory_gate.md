# H253 — Georgia scratcher endgame inventory gate

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: REJECTED STRICT GUARANTEE / CONDITIONAL POSITIVE-EV SIGNAL ONLY

## Question
Can published remaining-prize data on an end-stage scratch/instant ticket create a guaranteed positive net-profit buyout when the nominal remaining prize pool exceeds the estimated cost of remaining tickets?

## Candidate
Georgia Lottery game #1709, **$20 Big Georgia Raffle**.

Current official Georgia Lottery top-prize table shows 3 of 4 $2,000,000 top prizes claimed, i.e. one top prize still unclaimed at the observed snapshot. Georgia Lottery also lists the Big Georgia Raffle family in its ended-games material. Third-party endgame trackers reported sharply positive conditional arithmetic for #1709 before/around end-of-sale, but they explicitly estimate remaining ticket count rather than observe exact unsold inventory.

Sources checked:
- Official Georgia Lottery top-prizes-claimed page: https://www.galottery.com/en-us/games/scratchers/scratchers-top-prizes-claimed.html
- Official Georgia Lottery ended-games material containing game #1709: https://www.galottery.com/content/dam/portal/pdfs/games/scratchers/Ended-Games/20240605-ended-games-website--.pdf
- ScratchIQ #1709 snapshot: https://scratchiq.io/scratch-offs/ga/20-big-georgia-raffle-1709
- ScratchCheck #1709 ended-game page: https://scratchcheck.com/game/ga/20-big-georgia-raffle

## Snapshot arithmetic
The ScratchIQ snapshot listed an estimated 75,511 tickets remaining at $20 each and the following remaining prize counts:

- $2,000,000 x 1
- $10,000 x 4
- $500 x 260
- $200 x 404
- $100 x 530
- $75 x 734
- $50 x 2,265
- $40 x 2,298
- $30 x 4,697
- $25 x 5,194
- $20 ticket-prize x 8,452

Nominal remaining prize value = **$3,003,820**.
Estimated ticket cost = `75,511 * $20 = $1,510,220`.
Naive conditional gross ratio = **198.8995%**, nominal excess **$1,493,600** before tax/acquisition/friction.

This is a genuine signal worth screening, not a guarantee.

## Guarantee failure
The strict execution certificate fails for multiple independent reasons:

1. **Unclaimed is not unsold.** A winning ticket can already have been sold but not yet claimed. Published unclaimed-prize counts therefore do not certify that those prizes remain inside purchasable inventory.
2. **Remaining ticket count is estimated, not official exact live unsold inventory.** The denominator used by third-party EV trackers is inferred from prize depletion/odds and cannot serve as a deterministic buyout bound.
3. **Retail inventory is distributed.** Even if an exact statewide unsold count existed, there is no demonstrated mechanism to identify and acquire every unsold ticket before other buyers.
4. **Ended-game status kills current execution.** Once sales have ended, residual unclaimed prizes can remain outstanding but cannot be captured by buying new tickets.
5. **Claim latency creates adversarial information lag.** A top prize listed as unclaimed can cease being economically available before the public table updates.

Therefore `remaining_prize_value > estimated_remaining_ticket_cost` is at most a conditional EV heuristic. It is not a strict arbitrage certificate.

## General scratcher endgame gate
A scratch-ticket endgame can qualify for terminal SUCCESS only if, at purchase time, all of the following are proven:

- exact number of **unsold and purchasable** tickets is known with a hard upper bound;
- exact prize values embedded specifically in that unsold inventory are known or a worst-case lower bound exceeds total acquisition cost;
- already-sold-but-unclaimed winning tickets are excluded from the claimed prize inventory;
- all required tickets can actually be acquired before competing sales / game termination;
- taxes, claim limits, void/validation rules, travel, retailer limits and financing costs preserve strictly positive net profit.

Public remaining-prize tables alone do not satisfy these conditions.

## Result
**NOT A SUCCESS.** Georgia #1709 demonstrates that scratcher endgames can display very large apparent positive conditional EV, but the missing unsold-inventory certificate prevents a guaranteed-profit conclusion.

## Reopen condition
Reopen the scratcher-endgame class only on new evidence providing an official or otherwise execution-grade mapping/bound for unsold purchasable inventory and prizes, or a retailer/lottery mechanism allowing deterministic acquisition of the complete residual pool before claims/sales change state.
