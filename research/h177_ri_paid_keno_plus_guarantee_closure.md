# H177 — Rhode Island paid Keno Plus guarantee closure

Updated: 2026-08-22
Status: **REJECTED AS STRICT GUARANTEE MECHANISM**

## Question
Can ordinary paid Rhode Island `Keno Plus` replace the unresolved free pre-locked 2X promotion assumption behind H172-H175 and make the reduced 3-spot covers executable as a strict guaranteed-profit strategy?

## Fresh primary evidence

Official Rhode Island Lottery rules currently published as `RILotteryRules2025.pdf`, Keno subsection F, state:

- the Plus feature is an extension of Keno;
- the player opts in on the play slip;
- **the Plus wager must equal the base Keno wager**;
- the Plus drawing occurs just prior to the Keno drawing;
- the resulting multiplier can be **No Plus, 2X, 3X, 4X, 5X, or 10X**.

Current official Keno purchase UI on 2026-08-22 independently exposes KENO / PLUS / KENO OVERTIME and states ticket purchases cannot be canceled or refunded. The same page describes Keno Plus as multiplying prizes by the Plus number drawn.

Primary sources:
- https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules2025.pdf
- https://www.rilot.com/en-us/keno.html

## Strict-floor consequence

Let base cover spend be `S` and its ordinary-Keno worst-case gross be `G_min`.

Buying Plus on every wager changes spend to:

`S_total = 2S`

because the Plus wager must equal the base wager.

Since `No Plus` is an explicitly legal outcome, the strict all-outcome payoff floor cannot assume any multiplier >1. In the `No Plus` branch:

`G_plus_floor <= G_min`

so the paid-Plus strict gross-return ratio is at most:

`G_min / (2S)`.

For H173, the conditional free/pre-locked 2X result was 109.6491% of base spend. Under that same payout model, removing the 2X factor implies an ordinary worst-case gross of about 54.82455% of base spend. Purchasing Plus on all wagers therefore gives a `No Plus` strict-floor ratio of only about:

`54.82455% / 2 = 27.412275%` of total paid spend.

Thus ordinary paid Keno Plus is not merely unproven: it is structurally incompatible with the H173 strict guarantee because a legal `No Plus` outcome doubles cost without improving the base payout.

The same logic applies to any H175 descendant whose profitability relies on a guaranteed multiplier while ordinary gross remains below twice the total paid stake. A random post-purchase multiplier can improve EV but cannot establish an all-outcome guarantee when `No Plus` remains legal.

## Timing caveat

The rules say the Plus drawing occurs just prior to the Keno drawing, but this packet does **not** claim that a player could observe that result and still buy the immediately following Keno draw. No authoritative sales-cutoff/atomic post-Plus purchasing rule has been recovered. Until such a mechanism is proven, the multiplier is not a pre-commitment entitlement.

## Impact on H172-H175

- **CLOSED:** substituting ordinary paid Keno Plus for the historical/free pre-locked 2X mechanism.
- **STILL OPEN:** a genuinely free or already-assigned pre-draw doubler promotion such as the historical Lucky 3 Spot architecture, if current rules and execution allow it.
- **STILL OPEN:** H175 combinatorial balanced-transversal problem as pure mathematics, because a smaller cover could matter for any future genuine pre-locked subsidy/doubler.
- **STILL BLOCKED:** current `Kick Back with Keno` exact terms, current primary 3-spot paytable extraction, and multi-thousand same-draw execution.

## Verdict

**ЕЩЁ НЕ УСПЕХ.** H177 closes the ordinary paid Keno Plus substitution route: its equal-cost surcharge plus legal `No Plus` outcome destroys the strict guaranteed-profit floor.
