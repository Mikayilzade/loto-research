# H194 — Rhode Island Keno same-draw execution correction

Updated: 2026-08-23
Status: **NO SUCCESS; ONLINE H173/H175 EXECUTION GATE MATERIALLY WEAKENED**
Scope: LOTTERY ONLY.

## Target
Re-check H193's interpretation of Rhode Island Keno's `$150` maximum Ticket / Registered Ticketless Play price. H193 used `ceil(4336/150)=29` and `ceil(4560/150)=31` as optimistic lower bounds for purchase objects, implicitly allowing a $150 object to contain 150 distinct $1 same-draw 3-spot selections.

## New official evidence
The current 2026 Rhode Island Lottery rules state:

- Keno: player chooses one to ten numbers from 1–80, on a Play Slip, Quick Pick, or Registered Ticketless Play.
- Wagers for a **single Keno draw** are `$1/$2/$5/$10`.
- The player may place that wager for **up to 15 consecutive draws**.
- Maximum Ticket / Registered Ticketless Play price is `$150` for ordinary Keno.

The arithmetic exactly matches the consecutive-draw mechanism: `15 draws × $10 = $150`.

The current official iKeno purchase UI independently shows a single sequence:
1. `Pick your numbers`
2. `Amount per game`
3. `Consecutive games`
4. game options
5. `Buy Now`

No multi-line / multi-board builder for hundreds of independently specified same-draw selections is exposed in the public flow.

## Correction to H193
The `$150` cap is **not evidence that 150 different $1 selections can be bundled into one same-draw purchase object**. The official text instead explains the cap naturally by repeated play of a selection across up to 15 consecutive draws.

Therefore the H193 `29/31 objects` figures remain only a hypothetical packing bound under an unproven multi-selection-per-object assumption and must not be used as evidence of executable throughput.

For the public Registered Ticketless/iKeno route, the strongest current evidence is consistent with **one independently specified selection per purchase flow**, optionally repeated across consecutive draws. Under that interface model:

- H175 requires 4,336 distinct 3-spot selections for one target draw;
- H173 requires 4,560 distinct 3-spot selections for one target draw.

Consecutive-game replication does not reduce those same-draw counts.

This is not yet a formal impossibility theorem because public documentation does not explicitly state that server-side/cart tooling can never aggregate multiple independent selections into one checkout or that no bulk/API route exists. But the earlier apparent 29/31-object path is no longer supported by official evidence.

## Active promotion check
Fresh official-site retrieval on 2026-08-23 still shows `Kick Back with Keno Promotion` on the Rhode Island Lottery homepage. The current promotions page is dynamically populated and the exact Kick Back terms were not exposed in the retrievable public page text. Searches of the indexed 2026 promotion PDF path did not recover a rules PDF. Therefore no deterministic multiplier/subsidy can be assumed from the promotion name.

## Consequence
The same-draw execution burden for H173/H175 is materially worse than H193 suggested. Until an authoritative multi-selection checkout/bulk mechanism is recovered, online execution should be treated as requiring thousands of distinct selection submissions within one 4-minute draw window, not 29–31 max-price purchase objects.

## Sources
- Rhode Island Lottery Rules 2026, Keno §E: https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules_2026.pdf
- Current Rhode Island Keno purchase UI: https://www.rilot.com/en-us/keno.html
- Current Rhode Island Lottery homepage / active promotion carousel: https://www.rilot.com/en-us/home.html
- Current promotions page: https://www.rilot.com/en-us/player-zone/promotions.html

## Result
**ЕЩЁ НЕ УСПЕХ.** H194 withdraws the optimistic interpretation that the `$150` Keno cap proves 150 arbitrary same-draw $1 selections can be packaged together. Current official online evidence instead points to a single selection repeated over consecutive draws, leaving 4,336/4,560 independently specified same-draw selections as the unresolved execution burden.