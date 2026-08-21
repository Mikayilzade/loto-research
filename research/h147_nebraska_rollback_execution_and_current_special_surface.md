# H147 — Nebraska rollback execution + current special surface

Updated: 2026-08-21
Status: **EXECUTION ARCHITECTURE STRENGTHENED / CURRENT THRESHOLD-CROSSING SPECIAL NOT PROVEN / NO SUCCESS**

## Objective
Continue H146 without repeating the July 3.00x check. Test whether the Big Red app/paybook architecture can remove the fatal incomplete-cover execution branch, and broaden the live search surface for current Nebraska specials.

## Fresh official/current evidence
Big Red/La Vista FAQ currently states:
- app wagers can only be placed inside a licensed location;
- funds can be transferred out of the Play+ account;
- once a ticket is purchased, the app offers a void option before the game has started;
- voided-ticket funds return to the account balance;
- users can prepare/save practice tickets outside the licensed location and later use saved tickets when on-site;
- Monthly Keno Specials and community Official Rules are exposed inside the app.

Source: https://www.lavistakeno.com/frequentlyaskedquestions

Big Red current paybook/search-indexed rules also state that a player may request a refund before the games to which a ticket relates are closed.
Source: https://bigredkeno.com/Content/Media/File/Document/Locations/omaha_paybook.pdf

The current Big Red promo page explicitly points players to the current community keno special, but numeric specials are not exposed as reliable text on the public page.
Source: https://bigredkeno.com/promos

La Vista also currently publishes recurring Keno Specials on its website, but the numeric paytables are rendered as images rather than browser-readable text.
Source: https://www.lavistakeno.com/keno-specials

## New execution theorem: sequential cover with rollback
H145/H146 treated non-atomic acceptance of all 80 Pick-1 selections as a major execution risk. The current refund/void rules materially improve this.

A candidate can be made conditionally safe if the sequence is:
1. Keep principal in withdrawable Play+ balance.
2. Confirm threshold-crossing special is active.
3. Submit required cover tickets for one not-yet-closed game.
4. Verify accepted tickets and applicable paytable.
5. If the complete 80-number partition is accepted, allow game to close.
6. If any required ticket is missing/rejected, void/refund **all accepted cover tickets before game closure**.
7. Withdraw restored balance if abandoning the attempt.

Under this sequence, incomplete acceptance need not create permanent lottery exposure. This is materially stronger than Kentucky H136-H140, where cash became nonwithdrawable before complete coverage could be locked.

## Remaining execution blocker
The rules prove per-ticket pre-close void/refund, but they do **not** publicly prove:
- a single atomic/batch order for all 80 Pick-1 selections;
- a bulk-void command covering all accepted tickets at once;
- that 80 separately accepted/verified tickets can always be voided within one five-minute game window;
- that a saved-ticket workflow can submit the complete 80-number cover fast enough.

Therefore rollback is a genuine risk-control mechanism but not yet a strict terminal execution lock.

## Current special search
A fresh August 21 scan again failed to recover a reliable numeric August 2026 Pick-1 special above the H146 boundary from Kearney/Omaha/Lincoln/Fremont/Norfolk/Blair/Beatrice public text.

The current public-web surfaces now known are:
- Big Red `Promos` -> current community special link;
- Big Red app -> Monthly Keno Specials;
- Big Red app -> Official Rules/paybooks;
- La Vista current Keno Specials page (paytables rendered as images);
- municipal agenda/minutes attachments, proven by H146 to contain exact numeric special sheets.

This is a better monitoring map than H146, but the live numeric threshold remains data-gated.

## Control screen outside Nebraska
Current Pennsylvania Lottery Keno pays $2.50 per $1 on Pick 1, giving deterministic full-cover return `20*2.5/80 = 62.5%`, below Virginia 75% and below the Nebraska 3.00x boundary. It is not a superior target.
Source: https://www.palottery.pa.gov/PaLotteryWebSite/media/Page-Images/Game%20Guide/Game-Guide.pdf

Current BCLC Keno Pick 1 pays $2 per $1, deterministic full-cover return 50%; also inferior.
Source: https://corporate.bclc.com/content/dam/bclccorporate/documents/terms-and-conditions/rules-and-regulations/lotto/keno-keno-bonus-game-conditions.pdf

## Result
- Withdrawable funding: **VALIDATED**.
- Pre-game ticket void/refund with funds restored: **VALIDATED**.
- Saved-ticket preparation outside venue: **VALIDATED**.
- Sequential complete-cover-with-rollback architecture: **VALIDATED CONDITIONALLY**.
- Guaranteed bulk/atomic rollback of an 80-ticket cover: **NOT PROVEN**.
- Current August Pick-1 special `>3.00x` with usable subsidy or `>4.00x` standalone: **NOT FOUND IN RELIABLE PUBLIC TEXT**.
- Pennsylvania/BCLC Pick-1 controls: **INFERIOR TO EXISTING 75% TARGETS**.
- Terminal SUCCESS: **NO**.

## Next action
1. Recover current numeric specials from Big Red app, current promo-linked assets, La Vista special images, or municipal attachments.
2. Search specifically for a single-ticket/way-ticket construction or batch interface that represents all 80 Pick-1 selections, or for a documented bulk-void command.
3. Trigger terminal analysis immediately on any active Pick-1 `p>4.00`, or `p>3.00` with a genuinely pre-owned applicable subsidy.
4. If threshold crossing is found, verify aggregate payout limits, minimum stake, ticket paytable identifier, taxes, complete acceptance, refund deadline and withdrawal before classifying SUCCESS.
