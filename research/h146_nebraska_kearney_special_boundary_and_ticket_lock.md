# H146 — Nebraska Kearney special boundary + ticket/paytable lock

Updated: 2026-08-21
Status: **CURRENT DYNAMIC CLASS STRENGTHENED / JULY KEARNEY PICK-1 SPECIAL CLOSED AT BREAK-EVEN / CURRENT AUGUST NUMERIC SPECIAL STILL UNRECOVERED / NO SUCCESS**

## Objective
Continue H144/H145 by recovering a real numeric 2026 Big Red Keno special from a primary/official public record and testing it against the deterministic Pick-1 full-cover threshold.

## Primary current/legal sources
1. Nebraska Gaming Commission county/city lottery regulations:
   - https://nebraskagamingcommission.org/gaming-laws/county-city-lottery-regulations
2. Nebraska Department of Revenue Chapter 35 Keno regulations:
   - https://revenue.nebraska.gov/about/legal-information/regulations/chapter-35-keno
3. Kearney City Council public record containing a Big Red Keno special sheet:
   - https://kearney.granicus.com/MetaViewer.php?event_id=265&meta_id=51617&view_id=1
4. June 24, 2026 Kearney report confirming a Kearney-specific pay table has been used since early April 2026:
   - https://kgfw.com/2026/06/24/410592/
5. Current Big Red/La Vista FAQ confirming Monthly Keno Specials and Official Rules/paybooks are in the app:
   - https://www.lavistakeno.com/frequentlyaskedquestions

## New recovered 2026 numeric special
The Kearney City Council record exposes an official Big Red Keno promotional sheet for **July 2026**. The text is imperfectly indexed but materially clear:

- community: **Kearney**;
- game: **1 Spot / Regular**;
- payout: **Hit 1/1 wins $3**;
- special window text references **5 PM to 6 PM**;
- special ID: **755**;
- the sheet states promotional payouts supersede the Playbook during the promotion;
- the promotion may be withdrawn early at Big Red Keno's discretion;
- multigame tickets whose games occur after the special ends calculate at the regular paytable.

This is direct evidence that Big Red Keno really does publish community/time-specific 2026 numeric specials, not merely generic promotional language.

## Deterministic Pick-1 test
Nebraska Keno draws 20 numbers from 80. Covering all 80 possible Pick-1 selections at equal stake `w` yields exactly 20 winners in every draw.

For a Pick-1 gross payout multiple `p`:

- face spend: `S = 80w`
- deterministic gross: `G = 20pw`
- deterministic return ratio: `G/S = p/4`

For the recovered Kearney July special `p = 3.00`:

- deterministic gross return = **75% of face spend**;
- without subsidy, the full cover loses 25% deterministically;
- at quarter stakes (`w=$0.25`), face cover is $20 and gross is $15.

Under the H145 hypothetical of a genuinely pre-owned $5 free-play credit applicable to the complete $20 cover:

- external cash = $15;
- deterministic gross = $15;
- result = **exact pre-tax break-even, $0**.

Therefore this recovered special does **not** cross the strict positive threshold. It proves the search is operating directly at the economically relevant boundary: any otherwise equivalent Pick-1 special **strictly above 3.00x** plus a usable pre-owned $5 credit would become pre-tax positive; any direct special **strictly above 4.00x** is positive without subsidy.

## Execution-lock implications from Nebraska rules
Current Nebraska rules materially support the H145 execution architecture:

- potential payout must be made known before the player selects numbers (613.03H);
- accepted wagers are documented by an outside ticket / transaction record;
- where multiple paytables exist, the outside ticket must reference the applicable paytable (613.03L(7));
- a player can correct/void a ticket before game closure under the operator's procedures, while no ordinary write/void is allowed after the game closes;
- digital-on-premises wagers are documented when submitted and accepted before game close.

This is much stronger than a discretionary deposit bonus because the applicable paytable is tied to the accepted wager record.

## Important new caveat: promo calendar is not itself a lock
The recovered Kearney special explicitly says it may be withdrawn early at any time before its scheduled expiration. It also states that multigame tickets covering games after the special ends revert to the regular paytable.

Therefore a safe monitor cannot classify a future calendar slot as executable merely because a flyer says the special is scheduled. The candidate state must be checked at the actual wager/game level:

`special currently active -> complete single-game cover accepted -> each outside ticket references the qualifying paytable -> verify all 80 selections before close -> only then allow game to close`.

Do not rely on a long multigame ticket as a way to lock future promotional rates.

## Public-web search result for August 21, 2026
A fresh search did not recover a reliable public-text copy of the **current August 2026** Kearney/Omaha/Lincoln/Fremont/Norfolk/Blair/Beatrice special schedules. Big Red's FAQ still directs players to the app for Monthly Keno Specials and community paybooks. Public results pages confirm the communities are active in August 2026, but do not expose the active special paytable.

Thus the live trigger remains app/in-location data gated rather than mathematically blocked.

## Result
- Real 2026 Kearney numeric special recovered: **VALIDATED**.
- July 2026 Pick-1 special: **3.00x**.
- Direct deterministic overlay: **REJECTED** (75% face return).
- With hypothetical usable $5 free-play on a $20 quarter-stake cover: **exact break-even, not profit**.
- Ticket-level paytable reference / pre-draw verification architecture: **VALIDATED by current regulations**.
- Calendar-only special reservation: **REJECTED** due explicit early-withdrawal / post-special multigame reversion language.
- Current August numeric special above threshold: **NOT RECOVERED from reliable public web**.
- Terminal lottery SUCCESS: **NO**.

## Next action
1. Recover the current Big Red app Monthly Keno Specials / Official Rules for every active community, prioritizing any Pick-1 `p>3.00` with contemporaneous usable free-play or `p>4.00` standalone.
2. Search municipal agenda/minutes repositories for August 2026 special sheets using the Kearney discovery method; public city records can expose promotional PDFs that normal web search misses.
3. If a candidate crosses threshold, verify single-game ticket-level paytable designation, stake minimum, aggregate payout cap, coupon applicability, tax and complete 80-number acceptance before classification.
4. Continue non-Nebraska scan for fixed, non-shareable compact games with deterministic cover ratio >75% plus checkout-level subsidy.
