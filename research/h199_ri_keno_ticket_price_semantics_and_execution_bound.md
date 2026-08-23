# H199 — RI Keno ticket-price semantics and execution bound

Updated: 2026-08-23
Status: **NO SUCCESS; SAME-DRAW DISTINCT-SELECTION CAPACITY STILL UNPROVEN**
Scope: LOTTERY ONLY.

## Target
Continue the H198 execution branch without repeating the already-closed `multiple games on one ticket` shortcut. Test whether Rhode Island's current official Keno rules themselves support the earlier optimistic interpretation that the `$150` maximum ticket price implies up to 150 distinct `$1` same-draw selections can be bundled into one Ticket / Registered Ticketless Play.

## Fresh official evidence
The 2026 Rhode Island Lottery Rules state, in the Keno section:

1. A player chooses `1–10` spots and may use a Play Slip, Quick Pick, or Registered Ticketless Play.
2. **The wagers for a single Keno draw may be `$1`, `$2`, `$5`, or `$10`.**
3. The player may place that wager for **up to 15 consecutive draws**.
4. The maximum price for any Ticket or Registered Ticketless Play is **$150** for base Keno, `$300` with Plus or Overtime, and `$450` with both.
5. Draws occur every four minutes.

The base maximum is exactly `$10 × 15 = $150`. Likewise, the doubled feature ceilings follow the same single-selection/consecutive-draw cost structure.

## Exact interpretation
The rule text does **not** say that `$150` is a capacity for 150 independent same-draw `$1` selections. Its numerical structure is fully explained by one Keno number selection at the maximum `$10` wager repeated across the maximum 15 consecutive draws.

Therefore the earlier H193 conversion `4,336 plays / $150 ≈ 29 tickets` has no rule-level support. H194 correctly withdrew it; H199 now supplies the strongest official textual reason.

This is more than an absence-of-evidence point: the clause explicitly couples a *single-draw wager amount* with a *consecutive-draw count*, producing the exact stated maximum ticket price. The maximum-price rule is consequently a **cost ceiling, not an independently established same-draw selection-count ceiling**.

## Registered Ticketless Play does not rescue the bound
Current rules explicitly apply the same `$150/$300/$450` maxima to `Registered Ticketless Play` and state that iLottery Keno plays according to the same Keno/Plus/Overtime rules. No authoritative current source recovered in this packet states that one Registered Ticketless Play can contain multiple independently specified number selections for the same draw.

Thus the online/ticketless terminology cannot be used to infer a 150-selection basket either.

## Consequence for H173/H175
H173 needs 4,560 distinct same-draw 3-spot selections; H175 needs 4,336.

What is now safe to say:
- `$150` does **not** prove a 29-ticket/transaction execution route.
- `15 consecutive draws` does not help the combinatorial guarantee, because different draws have different outcomes.
- Historical `multiple Keno games on one ticket` doubler wording still does not prove multiple distinct selections in one draw.
- Current public iKeno UI evidence from H195 remains the conservative execution model: one selection → amount → consecutive games/options → Buy Now, with no recovered bulk distinct-selection QTY/cart control.

What remains unproven:
- a hard prohibition on multiple same-draw selections per retailer ticket;
- a retailer terminal batch/replay facility capable of rapidly issuing thousands of distinct selections;
- a registered-ticketless API or hidden basket mechanism with bulk same-draw capacity;
- a hard transaction-rate limit establishing impossibility.

## Kick Back check
Fresh official homepage search still lists `Kick Back with Keno Promotion` as current in August 2026, but this packet again did not recover authoritative mechanics. No new subsidy is inferred from the title alone.

## Verdict
**ЕЩЁ НЕ УСПЕХ.** H199 closes the `$150 => 150 distinct same-draw selections` interpretation: the official maximum is exactly explained by `$10 × 15 consecutive draws`. The H173/H175 same-draw bulk execution gate remains unresolved and must be proven from retailer/ticketless capacity documentation rather than ticket-price arithmetic.

## Sources
- Rhode Island Lottery Rules 2026, Keno section: https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules_2026.pdf
- Rhode Island Lottery Rules 2026, iLottery section: https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules2026.pdf
- Rhode Island Lottery current homepage: https://www.rilot.com/en-us/home.html
- Current Keno interface: https://www.rilot.com/en-us/keno.html
