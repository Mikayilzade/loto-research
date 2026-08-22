# H169 — NC Pick 3 atomicity + liability-limit closure

Updated: 2026-08-22
Status: **STRICT GUARANTEE REJECTED UNDER CURRENT PUBLIC RULES / CONDITIONAL OVERLAY PRESERVED**

## Purpose
H168 left one principal strict-guarantee blocker for the North Carolina Pick 3 forced-Double-Draw overlay: whether a partially issued full-cover basket can always be rolled back if issuance fails. This packet tests that execution gate directly and also checks whether complete acceptance can fail even without a hardware outage.

## Prior validated conditional economics
During an officially observable forced Double Draw evening:
- cover all 100 ordered Front Pair outcomes;
- stake $0.50 per Pair;
- face basket = **$50**;
- each Pick 3 draw necessarily contains exactly one covered Front Pair;
- each $0.50 Pair winner pays **$25**;
- two guaranteed drawings therefore return **$50 prize gross = 100% of face**.

If a retailer pre-commits a lawful promotional discount `d`, pre-tax deterministic surplus conditional on complete acceptance is `50d`. H167's conservative C-corp stress model put modeled after-tax break-even at approximately **2.9004% discount**.

## Finding 1 — cancellation is explicitly tied to the producing/selling terminal
Current NCEL FAQ wording says a retail Carolina Pick 3 ticket can be canceled **on the retailer terminal where it was produced** within 15 minutes of purchase or before draw break, whichever occurs first.

The NCEL retailer reference guide likewise states that the Cancel function permits cancellation **from the selling terminal** within the same time limit.

An official Pick 3 rules publication states that an official ticket may be canceled **on the terminal by the Retailer that issued the Ticket** within the allowed window.

Sources:
- https://nclottery.com/FAQGames
- https://uat.nclottery.com/Content/Docs/Retailer%20Altura%20Retailer%20Reference%20Guide.pdf
- https://qa.nclottery.com/Content/Docs/2.04B%20Carolina%20Pick%203%20Game%20Rules.pdf

### Consequence
The public rules do **not** create a contractual right to cancel an already-issued Pick 3 ticket through another retailer terminal, another store, a central web interface, or a support agent if the selling terminal becomes unavailable.

NCEL does provide a retailer hotline and equipment-service support, but the published support materials do not promise cancellation before draw break after a terminal/power/network failure.

Source:
- https://nclottery.com/RetailerContact

Therefore the sequence cannot be proven as atomic:

`issue tickets 1..k -> terminal/system becomes unavailable -> tickets 1..k remain live -> remaining cover not issued`

is a permitted execution branch under the currently public rules.

Because the 100% prize floor requires the complete 100-Pair partition, any live partial basket can have a legal draw outcome where the winning Pair was among the missing selections. A retailer discount on the issued subset does not repair that missing-outcome branch.

## Finding 2 — liability limits create an acceptance-failure branch even when equipment works
NCEL's current games FAQ expressly says Pick 3 combinations **regularly sell out** because of prize-liability limits. If total prize liabilities for a number combination across play types exceed NCEL's predetermined limit, **no further wagers on that number are accepted for that drawing**. NCEL may modify the limit at its sole discretion.

The published Pick 3 rules contain the same basic liability-limit mechanism: once the relevant prize liability threshold is exceeded, no further wagers on the affected number are accepted for the drawing.

Sources:
- https://nclottery.com/FAQGames
- https://qa.nclottery.com/Content/Docs/2.04B%20Carolina%20Pick%203%20Game%20Rules.pdf

### Consequence
This is more fundamental than outage risk. Even with a perfectly functioning terminal and prepared play slips, complete acceptance is not guaranteed before issuance begins.

A full-cover execution can encounter:

`some required selections accepted -> later required selection rejected by liability limit`

while previously printed tickets remain valid unless individually canceled at the producing terminal within the cancellation window.

No public NCEL mechanism found in H169 lets a player or retailer reserve all 100 required Pair positions against liability limits as one all-or-none order before the first ticket becomes live.

## Finding 3 — customer/vending refunds do not solve the draw-ticket basket problem
NCEL's general FAQ includes limited refund procedures for certain Touch Vending Machine payment/session failures, but those are not a published all-or-none cancellation guarantee for a 100-selection retail Pick 3 basket. The same FAQ separately states Pick 3 cancellation at retail is tied to the terminal where the ticket was produced.

Source:
- https://nclottery.com/faq

Thus payment-session refund language cannot be used as an atomic coverage guarantee.

## Strict execution theorem under current public rules
Let `B` be the required set of 100 Front Pair selections. The prize-floor proof requires every `b ∈ B` to be live for the same forced-Double-Draw evening.

Current public rules establish:
1. wagers may become live sequentially;
2. individual required wagers may cease to be accepted because of liability limits;
3. cancellation rights are terminal-specific and time-limited;
4. no all-or-none reservation/commit transaction for `B` is publicly guaranteed;
5. no cross-terminal/support-channel rollback right is publicly guaranteed.

Therefore there exists a lawful execution branch with a nonempty proper subset `S ⊂ B` live and no guaranteed means to restore the pre-transaction cash state before the draw.

For any proper subset `S`, at least one Pair outcome is uncovered. On a draw whose Front Pair is uncovered, that draw contributes no guaranteed Pair prize. Hence the two-draw $50 floor is no longer guaranteed.

**Conclusion: under the currently published NCEL execution rules, retailer discount + forced Double Draw is a conditional deterministic overlay after complete acceptance, but it is not a strict ex-ante guaranteed-profit strategy.**

## Reopen condition
Do not retest ordinary cancellation mechanics. Reopen this route only if materially new evidence supplies at least one of:
1. official all-or-none/batch acceptance of the complete Pair basket before any wager becomes irrevocable;
2. official reservation of all required Pair selections against liability limits before payment/issuance;
3. guaranteed cross-terminal or central-support cancellation/refund of every already-issued ticket after a selling-terminal failure, with enough time before draw break;
4. a redesigned cover requiring a single atomic wager/ticket that itself partitions every possible outcome and remains >100% net after discount/tax.

## Result
- Same-terminal cancellation: **VALIDATED but insufficient**.
- Cross-terminal/support rollback: **NOT PROVIDED by public rules found**.
- Liability-limit rejection branch: **VALIDATED current**.
- Complete-basket pre-reservation: **NOT FOUND**.
- H168/H167 NC forced-Double-Draw overlay: **CONDITIONALLY VALIDATED AFTER COMPLETE ACCEPTANCE; STRICT GUARANTEE REJECTED UNDER CURRENT PUBLIC RULES**.
- Lottery-project terminal SUCCESS: **NO**.

## Next lottery research
1. Search currently active forced-second-draw / guaranteed-extra-draw mechanisms where the complete deterministic cover can be purchased in one atomic ticket/order or where the cover has very few selections.
2. Continue scheduled Keno special/paytable scans because a single wager class with >100% deterministic full-cover ratio avoids multi-ticket atomicity entirely.
3. Monitor BCLC deterministic paid/free Keno promotions and Nebraska fixed special paytables against stored break-even thresholds.
4. Continue fixed-board raffle residual-takeover scans using H159 worst-case forced-slot theorem.
