# H198 — RI doubler multi-game semantics and Kick Back recovery

Updated: 2026-08-23
Status: **NO SUCCESS; CURRENT KICK BACK TERMS STILL UNRECOVERED**
Scope: LOTTERY ONLY.

## Target
Continue the highest-priority H197 checkpoint: recover current Rhode Island `Kick Back with Keno Promotion` terms and test whether historical Lucky 3 Spot doubler mechanics solve the H173/H175 execution bottleneck.

## Fresh official evidence

### 1. `Kick Back with Keno Promotion` is still live/current
The Rhode Island Lottery homepage, freshly crawled in August 2026, explicitly lists **`Kick Back with Keno Promotion`** in its active promotional carousel. This is stronger than treating the title as an old cached artifact.

However, the public `All Promotions` page loads current-promotion cards dynamically and does not expose the card text/target URLs in the static page extraction. Repeated exact-title and official-domain searches did not recover a rules PDF or landing page for this promotion.

Result: existence/currentness is official and current; mechanics remain unresolved.

### 2. Historical Lucky 3 Spot rules clarify what “multiple Keno games on one ticket” means for a doubler
Official RI Lottery Lucky 3 Spot Keno rules (2024 and 2025) state that if the Lucky 3 Spot message appears on a ticket for **multiple Keno games**, eligible prize wins for **all games included on that ticket** may be doubled.

The 2025 launch-alert rules additionally establish:
- only 3-spot Keno tickets at the specified promotion location/time are eligible;
- eligibility is printed on the ticket before the draw;
- eligible tickets cannot be cancelled;
- retailers cannot print tickets in advance of sale.

This continues to validate the H172/H173 premise that a true pre-draw printed 2x entitlement has existed in RI.

### 3. This does NOT yet solve H173/H175 same-draw throughput
The historical wording is about multiple **games** included on a ticket. RI’s current Keno interface separately exposes `Consecutive games`, and official rules describe a Keno game as a wager tied to a drawing. Therefore the historical clause safely proves one printed doubler can apply across multiple games/draws on the same ticket, but it does **not** prove that thousands of independently specified 3-spot selections for one single drawing can share one ticket/transaction.

That distinction is decisive: H173/H175 combinatorial guarantees require all constituent selections to face the **same 20-number draw**. Repeating selections across consecutive draws produces different outcomes and cannot be substituted into the all-outcome same-draw proof.

## Current execution consequence
H195 remains intact:
- H175 needs 4,336 independently specified same-draw 3-spot selections;
- public iKeno UI exposes one number selection followed by amount, consecutive games, options, `Buy Now`;
- no public bulk-QTY/cart control for distinct Keno selections has been recovered.

H198 therefore rejects a tempting but invalid shortcut: historical `multiple games on one ticket` language cannot be interpreted as evidence for `multiple distinct selections in one draw`.

## Search result for current Kick Back
Official/current evidence recovered:
- RI Lottery homepage currently lists `Kick Back with Keno Promotion`.
- `All Promotions` page confirms current promotions are dynamically populated.

Not recovered:
- exact promotion dates;
- retailer vs iLottery eligibility;
- purchase threshold;
- whether reward is a free Keno ticket, Bonus Money, rebate, multiplier, or random award;
- whether any award is deterministic and vested before the underlying Keno draw;
- caps/limits;
- exact cancellation/disqualification language.

No inference is made from unrelated homepage copy such as `Get a free ticket when you buy 2`; the public link associated with that text resolves to Mega Millions, so it is not evidence about Kick Back Keno.

## Verdict
**ЕЩЁ НЕ УСПЕХ.** The historical RI doubler architecture remains genuine, but the multi-game ticket clause does not solve H173/H175 same-draw bulk execution. Current `Kick Back with Keno` is confirmed active, while its exact rules remain the missing high-value evidence.

## Sources
- Rhode Island Lottery homepage, current Aug 2026: https://www.rilot.com/en-us/home.html
- Rhode Island Lottery All Promotions: https://www.rilot.com/en-us/player-zone/promotions.html
- Rhode Island Lottery Keno current interface: https://www.rilot.com/en-us/keno.html
- 2025 Lucky 3 Spot Keno & Bingo Doubler rules: https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2025/LaunchAlertRules-Lucky3SpotKenoBingoDoubler.pdf
- 2024 Lucky 3 Spot Keno rules: https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2024/Lucky3SpotKenoRule091224.pdf
- 2026 Rhode Island Lottery Rules: https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules_2026.pdf
