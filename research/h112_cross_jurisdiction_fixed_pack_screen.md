# H112 — cross-jurisdiction fixed-pack / high-payout instant-ticket screen

Updated: 2026-08-20
Status: **HIGH GAME RTP DOES NOT IMPLY SEALED-PACK FLOOR / NO CURRENT NON-TEXAS PACK GUARANTEE FOUND / NO SUCCESS**

## Goal
Continue H111 outside Texas. Search for a current instant-ticket jurisdiction where a complete sealed book/pack has a published deterministic minimum prize value high enough that a lawful deterministic lottery-specific discount/rebate could push the worst-case recovered value above acquisition cost.

This packet deliberately distinguishes three quantities that are often confused:

1. **game-level expected payout / RTP** — average prize dollars over the whole print run;
2. **ticket-level odds** — probability that a random ticket wins something;
3. **sealed-pack minimum payout** — a contractual/printed guarantee that every complete unopened pack contains at least a specified cash value.

Only (3), combined with an executable discount/subsidy, can directly support a strict buy-the-book cash floor.

## Break-even condition
Let:
- `F` = face value of a complete sealed pack;
- `G` = guaranteed cash prizes in every sealed pack;
- `D` = deterministic lawful discount/rebate/subsidy captured on purchase;
- `C` = all execution/tax/claim costs.

Strict guarantee requires:

`G + D - C > F`.

Equivalently, if `g = G/F`, required deterministic subsidy rate is:

`d > 1 - g + C/F`.

H111 Texas sampled `g` only 40.0%–62.5%; even granting a full 5% retailer commission left 45.0%–67.5% floors. H112 searches for a materially higher `g` elsewhere.

## Massachusetts — very high game RTP, but not a pack floor
Massachusetts currently provides unusually high **game-level estimated payout**. Examples:

- `$25,000,000 Mega Money` ($50 instant): official launch states **82.0% overall prize payout**, matching the highest payout percentage offered by Massachusetts Lottery.
- `$500,000 Frenzy` (game #553, launched May 12 2026): official game page lists **82.00% Est. Payout** and a print run of approximately 8,064,000 tickets.

Sources:
- https://www.masslottery.com/about/new-50-instant-ticket-features-25-million-grand-prize-2025
- https://www.masslottery.com/games/draw-and-instants/500000-frenzy

These are strong expected-value controls but do **not** state that each book contains 82% (or any high fixed percentage) in guaranteed cash. Large prizes are distributed across the full print run, so whole-game RTP cannot be used as a deterministic book minimum.

A hypothetical pack guarantee equal to 82% would still require >18% deterministic subsidy before costs. No such pack guarantee was found in the official material reviewed.

Status: **HIGH RTP VALIDATED / PACK-FLOOR INFERENCE REJECTED**.

## North Carolina — pack analytics specifically requested, not published as a standard player metric
The North Carolina Education Lottery has an unusually useful official historical Q&A. A player explicitly asked for the same type of analytics used in H111: odds by prize plus a **guaranteed total prize value for a pack of tickets**. The official lottery response did not provide such a number and instead referred the player to a direct information request for research into whether the information could be provided.

Source:
- https://nclottery.com/NewsBlogDetails/2019/10/30/Get-your-questions-answered/

This is not proof that internal pack construction lacks guarantees. It is evidence that a public, current, player-executable pack-floor table comparable to Texas was not available from the screened official channel.

Status: **PUBLIC PACK-FLOOR DATA NOT ESTABLISHED / NO EXECUTABLE H111 ANALOGUE**.

## California — rich current ticket/prize data, no deterministic pack minimum in screened public pages
California currently publishes current Scratchers price, odds, cash odds, and prizes remaining. Example current pages include 200X (#1740) and other Scratchers. The public Scratchers hub/game pages describe ticket-level/game-level information; the screened official pages do not provide a guaranteed prize amount per complete sealed book.

Sources:
- https://www.calottery.com/en/scratchers/scratchers-hub
- https://www.calottery.com/en/scratchers/$30/200x-1740

California also runs Scratchers 2nd Chance, but a random second-chance drawing has zero worst-case value and therefore cannot bridge a deterministic pack deficit.

Status: **NO PUBLIC DETERMINISTIC PACK FLOOR FOUND; SECOND CHANCE HAS ZERO STRICT FLOOR VALUE**.

## Florida — large prize pools and second chance, but again game-level rather than pack-level floor
Florida's 2026 Scratch-Off releases publish ticket prices, total cash-prize pools and overall odds. For example the May 18 2026 launch describes four games, including Mega 7's, and Florida's X THE CASH promotion awarded random drawing prizes plus a finite set of instant $100 coupons on eligible non-winning tickets.

Sources:
- https://floridalottery.com/news/view?id=2026-05-florida-lotterys-may-scratch-off-lineup-brings-fresh-chances-to-win
- https://secondchance.floridalottery.com/secondchance/prizes_2026-XTheCash

The reviewed official public material did not state a guaranteed minimum cash value in every sealed pack. Random second-chance entries again contribute zero to a strict worst-case floor. A finite instant-coupon mechanic can have deterministic value only if coupon placement/count can be locked before purchase; the current public promotion information does not supply such a pack-level lock.

Status: **NO PUBLIC PACK FLOOR FOUND / PROMO DOES NOT CREATE ALL-OUTCOME GUARANTEE**.

## Cross-jurisdiction result
The important result is negative but high leverage:

- **Texas remains exceptional** in the project because public game reports exposed an exact guaranteed total prize amount per sealed pack.
- Massachusetts shows that even an **82% game RTP** is not enough: RTP is an expectation across the full game, not a worst-case sealed-book guarantee.
- North Carolina's official Q&A confirms that players have specifically sought guaranteed pack-value analytics, but the screened official channel did not supply them.
- California and Florida expose extensive game/ticket data, but no comparable deterministic sealed-pack minimum was found in the current public pages screened.

Therefore H111 cannot be generalized by substituting high published RTP for a pack floor.

## Reopen condition
Reopen this branch only with genuinely new evidence satisfying at least one of:

1. official current rules state a guaranteed minimum cash amount in **every sealed book/pack**;
2. a retailer/lottery contract creates a deterministic lottery-specific rebate large enough to bridge the exact pack deficit;
3. an official inventory system identifies the exact remaining contents of a pack before purchase;
4. a promotion grants deterministic cash to every qualifying complete pack (not a random draw, points, free-play lottery, or conditional winner bonus).

## Result
**NO SUCCESS.** Cross-jurisdiction high-RTP instant tickets do not currently supply a proven H111-style high sealed-pack floor. The strongest screened non-Texas public figure, Massachusetts 82% RTP, is explicitly a game-level expected payout and cannot support an all-outcome book guarantee.
