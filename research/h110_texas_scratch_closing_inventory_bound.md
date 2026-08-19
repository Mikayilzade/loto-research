# H110 — Texas scratch closing-inventory / remaining-liability bound

Updated: 2026-08-19
Status: **SUBSTANTIAL SCRATCH-STATE SCREEN / THREE CLOSING GAMES NEGATIVE EVEN UNDER BUYER-FAVORABLE LIABILITY UPPER BOUND / NO SUCCESS**

## Goal
Test the strongest version of the scratch-ticket remaining-state idea: use an official lottery that publishes not only remaining/claimed prizes, but also closing-analysis data with percent sold, pack inventory and outstanding prize liability. Ask whether buying all remaining inventory can ever produce a strict positive worst-case cash floor.

Texas is unusually useful because official game pages publish:
- ticket price and approximate total print run;
- pack size and a guaranteed total prize amount per pack;
- prizes printed and prizes claimed;
- for games being closed, a downloadable `Scratch Ticket Game Closing Analysis` with percent sold, active/warehouse/returned/confirmed packs and the operator's outstanding prize liability.

Primary sources:
- Texas Lottery game X #2590: https://www.texaslottery.com/export/sites/lottery/Games/Scratch_Offs/details.html_252700419.html
- X closing analysis: https://www.texaslottery.com/export/sites/lottery/Documents/scratchoffs/2590closinganalysis.pdf
- Crazy 8s #2656: https://www.texaslottery.com/export/sites/lottery/Games/Scratch_Offs/details.html_252699576.html
- Crazy 8s closing analysis: https://www.texaslottery.com/export/sites/lottery/Documents/scratchoffs/2656closinganalysis.pdf
- Lucky No. 7 #2622: https://www.texaslottery.com/export/sites/lottery/Games/Scratch_Offs/details.html_252699673.html
- Lucky No. 7 closing analysis: https://www.texaslottery.com/export/sites/lottery/Documents/scratchoffs/2622closinganalysis.pdf
- Texas games ending soon: https://www.texaslottery.com/export/sites/lottery/Games/Scratch_Offs/closing.html

## Key theorem
Let:
- `N` = printed tickets;
- `s` = official fraction sold at closing-analysis date;
- `c` = ticket price;
- `L` = operator-reported **outstanding prize liability**, including all unclaimed winning tickets whether still unsold or already sold but not yet claimed.

Approximate all-unsold acquisition cost from the official closing report is:

`C_unsold ~= N * (1-s) * c`.

The **actual prize value contained in unsold inventory cannot exceed L**, because `L` also includes prizes on already-sold but unclaimed tickets. Therefore `L/C_unsold` is deliberately buyer-favorable as a ceiling on the gross return from taking all remaining inventory at face value.

If even this ceiling is below 1, the game cannot be a guaranteed-profit all-remaining-inventory acquisition at that state. The approximation caveat on `s` means this is not an exact ticket-count theorem by itself, but large deficits are still decisive screening evidence; a SUCCESS candidate would need a much stronger margin plus exact inventory ownership/availability.

## Three official closing-state screens

### 1. X #2590 — $50
Closing analysis dated 2026-07-16:
- printed tickets: 6,119,700;
- percent sold: 62.46%;
- printed payout: 78.21%;
- outstanding prize liability: $89,882,600;
- one $1,000,000 top prize remained at the closing-analysis date.

Buyer-favorable screen:
- estimated unsold tickets = `6,119,700 * 37.54% = 2,297,335.38`;
- face cost = **$114,866,769**;
- maximum possible prize value if every outstanding dollar were magically located in unsold tickets = **$89,882,600**;
- optimistic liability/cost ceiling = **78.2494%**;
- optimistic deficit = **$24,984,169** before logistics, retailer availability, taxes, claim timing or sold-unclaimed contamination.

The same game also states a pack size of 20 and guaranteed total prize amount of $625 per pack. A sealed pack costs $1,000, so the guaranteed pack floor is only **62.5%**.

**Result: REJECTED.** Even the impossible buyer-favorable assumption that all outstanding prizes are still unsold leaves a large loss.

### 2. Crazy 8s #2656 — $2
Closing analysis dated 2026-06-22:
- printed tickets: 9,052,375;
- percent sold: 50.00%;
- printed payout: 65.20%;
- outstanding prize liability: **$6,342,053**;
- two $30,000 top prizes remained.

Buyer-favorable screen:
- estimated unsold face cost = **$9,052,375**;
- liability/cost ceiling = **70.0595%**;
- optimistic deficit = **$2,710,322**.

Pack floor:
- 125 tickets × $2 = $250 pack cost;
- guaranteed total prize amount = $124;
- strict sealed-pack floor = **49.6%**.

**Result: REJECTED.** Large deficit even before subtracting prizes already sold but unclaimed.

### 3. Lucky No. 7 #2622 — $2
Closing analysis dated 2026-06-29:
- printed tickets: 9,293,500;
- percent sold: 64.38%;
- printed payout: 65.08%;
- outstanding prize liability: **$5,058,796**;
- four $30,000 top prizes remained at the closing-analysis date.

Buyer-favorable screen:
- estimated unsold face cost = **$6,620,689.40**;
- liability/cost ceiling = **76.4089%**;
- optimistic deficit = **$1,561,893.40**.

Pack floor:
- 125 × $2 = $250 cost;
- guaranteed total prize amount = $139;
- sealed-pack guaranteed floor = **55.6%**.

**Result: REJECTED.** Again the total outstanding liability is already below estimated unsold acquisition cost.

## Why this is stronger than ordinary “remaining prizes” websites
Many lotteries publish prize counts remaining, but those counts usually mix:
- tickets still in distribution/warehouse/retail inventory;
- winning tickets already sold but not yet claimed;
- tickets in partially sold packs;
- sometimes reordered ticket populations.

Texas closing reports expose a materially better state: percent sold, pack inventory categories and an operator-side liability table. That lets us build an explicit **upper bound** rather than pretending all remaining prizes are available for purchase.

The tested states show an important structural pattern: closing a scratch game with attractive top prizes remaining does not imply a buyout edge. The aggregate remaining liability can still sit well below the face value of remaining inventory.

## Exact-denominator requirement for future scratch SUCCESS
A strict guaranteed-profit scratch strategy now requires all of these before purchase:
1. exact set/number of tickets still legally purchasable;
2. proof that prize amounts counted as “remaining” are attached to that purchasable set, not sold-unclaimed tickets;
3. worst-case total payout of the purchasable set greater than its acquisition cost + tax/fees/logistics;
4. ability to acquire the whole bounded set before other buyers remove tickets or claims change the state;
5. no pack-return/reorder/reallocation branch that expands or changes the denominator.

Ordinary public “remaining prize” counts fail #1-2. Texas closing analysis improves #1 materially but still does not identify which outstanding prizes are in unsold inventory; moreover the three sampled closing states fail the economics even under the maximal favorable allocation of liability.

## Strategic consequence
H010/Poz-Qazan remains data-blocked for the same fundamental reason: remaining prize counts without a live exact unsold denominator do not support a deterministic guarantee. H110 demonstrates a jurisdiction where a much richer denominator exists and still finds no edge.

Future scratch search should therefore prioritize only:
- fixed packs/books with a **guaranteed pack composition** whose minimum cash return exceeds purchase cost after a deterministic subsidy/discount; or
- end-game inventory where the operator publishes exact remaining ticket count **and** prize liability tied specifically to unsold tickets; or
- a lawful liquidation/recall mechanism that lets one acquire the entire known unsold set below its guaranteed payout.

Do not spend further cycles merely ranking games by top-prizes-remaining ratios without denominator ownership evidence.

## Terminal result
**NO SUCCESS.** Texas H110 materially closes the richest public closing-inventory scratch dataset sampled: X, Crazy 8s and Lucky No. 7 are negative even under an intentionally impossible buyer-favorable assumption that every outstanding prize dollar is still inside purchasable unsold inventory.