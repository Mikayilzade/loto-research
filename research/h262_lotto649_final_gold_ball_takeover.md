# H262 — LOTTO 6/49 final Gold Ball takeover screen

Date: 2026-08-24
Status: **PROMISING MECHANISM, NOT EXECUTABLE AS A STRICT GUARANTEE**
Scope: lottery-only; Canadian LOTTO 6/49 Gold Ball Draw.

## Question
Can the elimination-style Gold Ball Draw create a genuine guaranteed-profit lottery takeover on the terminal draw, when only the gold ball remains?

## Current official mechanics
WCLC's current LOTTO 6/49 material states:

- each C$3 LOTTO 6/49 selection automatically receives one Gold Ball Draw selection;
- the Gold Ball selection is computer-generated;
- the winning Gold Ball selection is drawn at random from **all Gold Ball Draw selections issued for that draw**;
- each Gold Ball selection is unique, so the winning identifier cannot be shared by two tickets;
- Free Plays also receive Gold Ball entries;
- the elimination sequence starts with 29 white balls and one gold ball;
- a white ball pays C$1m and is removed; the Gold Ball jackpot rises by C$2m each draw;
- after 29 consecutive white-ball draws, only the gold ball remains, so the next Gold Ball prize is certain to be the jackpot.

Primary current sources:
- WCLC LOTTO 6/49: https://www.wclc.com/games/lotto-649.htm
- WCLC 2026 Lotto Facts: https://www.wclc.com/display-on/display-on-downloads/lotto-facts-2026.htm

The current WCLC page on 2026-08-24 showed the upcoming Aug. 26 draw at C$18m or guaranteed C$1m with 26 balls remaining. That live state is **not** the target of this theorem; the target is the eventual one-ball terminal state.

## Exact terminal arithmetic
Start jackpot: C$10,000,000.

If all 29 white balls are drawn before the gold ball, the jackpot after the 29th white draw is:

`10,000,000 + 29 * 2,000,000 = C$68,000,000`.

On the following draw only the gold ball remains, so the selected Gold Ball identifier receives C$68m with probability 1 **conditional on the official sequence reaching that state**.

Suppose a player could own every Gold Ball identifier issued for that terminal draw. Because identifiers are unique and the winner is selected from the issued set, the Gold Ball component alone would then have a deterministic gross floor of C$68m.

At C$3 per selection, the Gold-Ball-only acquisition break-even count is:

`floor((68,000,000 - epsilon) / 3) = 22,666,666 selections` for strict positive profit.

Thus this is materially different from an ordinary shareable jackpot. **If** every issued terminal-draw identifier could be monopolized and total acquired plays were <=22,666,666, the Gold Ball component by itself would prove positive gross profit before considering any Classic Draw prizes.

For comparison, on any white-ball state the guaranteed Gold Ball prize is only C$1m, giving a Gold-Ball-only strict break-even ceiling of 333,333 paid selections.

## Why this is not SUCCESS
The crucial takeover condition is not player-controllable under the published mechanics.

1. Gold Ball identifiers are **computer-generated**, not player-selectable/reservable.
2. The winning identifier is drawn from **all selections issued for that draw**, including other players' purchases.
3. The game is an open national sale until cutoff; no official finite pre-draw issuance cap or exclusive reservation mechanism was found that lets one buyer certify ownership of the entire eligible identifier set before sales close.
4. Free Plays also create eligible Gold Ball entries, so controlling ordinary cash purchases would not by itself certify full ownership.
5. One legal external issued identifier is enough to create a draw outcome in which the external identifier wins, collapsing the deterministic C$68m floor of our portfolio to zero from the Gold Ball component.

Therefore the terminal one-ball state creates a **real conditional takeover theorem**, but not an executable strict guarantee under current public-sale rules.

## Closure / reopen condition
Do not repeat this screen unless new evidence establishes at least one of:

- a hard finite issuance cap for a specific terminal Gold Ball draw together with a mechanism to reserve/buy every remaining eligible identifier;
- an operator-approved exclusive/closed sales channel allowing all issued identifiers to be controlled;
- a deterministic subsidy or Classic-Draw coverage floor that remains positive even when an external Gold Ball identifier wins.

Absent one of those conditions, H262 is closed as **structurally promising but execution-blocked**.
