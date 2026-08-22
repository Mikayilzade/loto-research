# H168 — NC Pick 3 retailer discount authority + current Double Draw availability

Updated: 2026-08-22
Status: **DISCOUNT-AUTHORITY GATE MATERIALLY RESOLVED / CURRENT EXECUTION UNAVAILABLE / ATOMICITY STILL OPEN**

## Purpose
H167 identified a potentially deterministic overlay: on a forced Pick 3 Double Draw evening, a full 100-outcome Front Pair cover costs $50 face and guarantees $50 in prizes; any pre-agreed retailer discount creates deterministic pre-tax profit. H167 left three major execution questions: whether a Pick 3 retailer discount needs separate NCEL pre-approval, whether Double Draw is currently active, and whether a partial 100-selection basket can always be rolled back.

This packet attacks those gates directly with current NCEL materials.

## 1. Current Pick 3 rules explicitly place discount authorization with the retailer
The current Carolina Pick 3 Game Rules, revised 2025-09-05 and published by NCEL, state in Section D.2:

- subject to governing laws/regulations, **Retailers may authorize sale of Official Carolina Pick 3 Tickets at a discount for promotional purposes**;
- discounted sales must be reported to NCEL at full gross sales value.

Source:
- https://nclottery.com/Content/Docs/2.04B_Carolina_Pick_3_Game_Rules_v1.pdf

This is stronger than the generic H167 reading because it is Pick-3-specific and current. The text says the **Retailer** may authorize the discount; it does not say the NCEL must separately approve each ordinary Pick 3 discount. By contrast, current Powerball/Mega Millions rules use different wording: **NCEL may authorize** a promotional discount. That contrast materially weakens the prior concern that every Pick 3 retailer discount necessarily requires separate NCEL pre-approval.

Supporting contrast:
- Powerball: https://nclottery.com/Content/Docs/2.04A_Powerball_Game_Rules_with_Double_Play.pdf
- Mega Millions: https://nclottery.com/Content/Docs/2.04G_Mega_Millions_Game_Rules_6.24.25.pdf

Conclusion: **H167 Gate 2 is materially narrowed.** A terminal execution still needs a real retailer willing to commit the exact discount and comply with reporting/accounting, but the game rule itself provides explicit retailer authority.

## 2. The 2026 Double Draw promotion is not currently active on 2026-08-22
NCEL's 2026 promotions page lists Pick 3 Double Draw for **July 1-31**. A July 16, 2026 NCEL article confirms the active mechanism: six white balls plus one yellow; each white-ball draw removes a white ball for the next evening; when yellow is drawn, a second Pick 3 drawing occurs and the machine resets. NCEL states that a Double Draw is guaranteed to occur once every seven days during the promotion.

Sources:
- https://nclottery.com/Promotions
- https://nclottery.com/NewsBlogDetails/2026/7/16/Double-Draw-pays-off-for-Pick-3-players

Therefore the H167/H168 forced-state cover is **not executable today, 2026-08-22**, because the verified 2026 promotion ended July 31. Historical NCEL records show the promotion has recurred in different months (for example November 2025), so this should remain a monitored recurring lottery opportunity rather than be permanently rejected.

Historical recurrence evidence:
- https://nclottery.com/NewsBlogDetails/2025/10/31/Pick-3-players-can-double-the-fun-with-Double-Draw-
- https://nclottery.com/NewsBlogDetails/2025/11/17/Two-Pick-3-drawings-guaranteed-tonight

## 3. Forced state is publicly observable when the yellow ball is the only ball left
NCEL has previously published same-day notices explicitly stating that **two Pick 3 drawings are guaranteed tonight** because only the Yellow Ball remains in the Double Draw machine. This validates the key state-observability assumption: during an active recurrence, the forced second draw can be known before ticket purchase from an official source.

Source:
- https://nclottery.com/NewsBlogDetails/2025/11/17/Two-Pick-3-drawings-guaranteed-tonight

Thus H167 Gate 1 is structurally solvable during an active promotion: wait until NCEL officially confirms a forced yellow-only evening, then execute only in that state.

## 4. Cancellation mechanics are stronger than previously recorded, but not atomic
NCEL's current Pick 3 how-to-play page states that a retail Pick 3 ticket can be canceled by the retailer on the same terminal where it was produced within **15 minutes of purchase or before draw break, whichever comes first**.

NCEL's retailer reference guide gives the operational steps:
1. press Cancel on the terminal;
2. scan the ticket;
3. a cancellation notice prints automatically;
4. retain the canceled ticket and notice for end-of-day balancing.

Sources:
- https://nclottery.com/pick3-how-to-play
- https://nclottery.com/Content/Docs/RRG_Updated_Version.pdf

This confirms ticket-by-ticket rollback is an ordinary terminal function, not merely a discretionary customer-service possibility.

However it still does **not** prove a strict all-or-none 100-selection transaction. The public guide does not promise that every previously issued ticket can be canceled after a terminal, communications, power, printer, or system failure. Therefore an adverse branch remains where some tickets are issued/paid and later cancellation becomes unavailable before the full cover is accepted.

Conclusion: **atomicity remains the principal strict-guarantee blocker.**

## 5. Current deterministic math remains unchanged
On a forced Double Draw evening:
- 100 ordered Front Pair outcomes;
- $0.50 each;
- face basket = $50;
- each draw guarantees exactly one winning Front Pair;
- each $0.50 Pair win = $25;
- two guaranteed draws = $50 prize gross.

With retailer discount `d`:
- customer cost = `50(1-d)`;
- guaranteed prize = `$50`;
- deterministic pre-tax surplus = `50d`.

Under the deliberately conservative H167 C-corp stress model, break-even remains approximately **2.9004%**. A 5% locked discount gives about **+$0.8325 modeled after tax** per $50 cover under those assumptions.

## Result
- **Pick-3-specific retailer discount authority: VALIDATED current.** The rules themselves say retailers may authorize promotional discounts.
- **Forced-state observability: VALIDATED structurally** from official same-day NCEL guaranteed-Double-Draw notices.
- **Current execution on 2026-08-22: UNAVAILABLE.** Verified 2026 Double Draw ended July 31.
- **Ticket-by-ticket cancellation: VALIDATED operationally.**
- **Whole-basket atomicity / guaranteed rollback under outage: NOT PROVEN.**
- **Terminal SUCCESS: NOT PROVEN.**

## Next action
1. Monitor for the next official NC Pick 3 Double Draw recurrence; on activation, wait only for an official yellow-only/guaranteed-two-draw state.
2. Before any execution, obtain a written retailer promotional discount >2.9004% (preferably 5%-6%) under current Pick 3 Rule D.2.
3. Highest-value unresolved research: recover retailer terminal/support procedures for outage recovery and whether issued Pick 3 tickets can be canceled through another terminal/support channel if the selling terminal fails.
4. Search for a comparable active lottery promotion with the same forced-second-draw = 100% cover architecture that is live now and requires fewer issued tickets.
