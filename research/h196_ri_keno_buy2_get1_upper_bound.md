# H196 — Rhode Island Keno active-promo upper bound

Updated: 2026-08-23
Status: **NO SUCCESS**
Scope: LOTTERY ONLY

## Target
Resolve the highest-priority Rhode Island Keno promotion branch as far as current official evidence permits, and test the strongest homepage subsidy phrase as an optimistic upper bound without falsely attributing it to Keno.

## Fresh official evidence
1. The current Rhode Island Lottery homepage still displays a carousel item titled **`Kick Back with Keno Promotion`**.
2. A separate current homepage rendering contains the phrase **`Get a free ticket when you buy 2`**.
3. The public HTML does not establish that the buy-2/get-1 phrase belongs to the Keno carousel item; clicking the exposed phrase resolves to Mega Millions in the current page structure. Therefore the phrase is **not treated as an established Keno term**.
4. Rhode Island's 2025 Lucky 3 Spot Keno promotion provides an authoritative control for how a genuine deterministic Keno doubler is documented: eligible 3-spot tickets carried a printed pre-draw message, winning prizes were doubled, eligible tickets could not be cancelled, and the promo was tightly limited by venue/time.

## Optimistic subsidy bound
Even granting, purely as an upper-bound hypothesis, that the current Keno promo meant **one completely free equivalent Keno ticket for every two paid tickets**, the effective purchase cost would fall to `2/3` of ordinary face cost.

H173's validated doubled 3-spot cover has worst-case gross return `109.6491%` *with* a true 2x prize doubler. Removing the 2x condition halves that floor to:

`54.82455%` of ordinary face cost.

Applying an idealized buy-2/get-1 discount gives at most:

`54.82455% / (2/3) = 82.236825%`

of effective paid cost.

Thus a simple deterministic **buy 2, get 1 free** Keno subsidy would still be materially insufficient to turn H173 into a strict guaranteed-profit strategy unless the free ticket also carries an additional prize multiplier or some stronger nonlinear benefit.

## Consequence
The unresolved current `Kick Back with Keno Promotion` remains worth recovering, but one prominent homepage subsidy phrase can now be bounded: even under the most favorable attribution and perfect equivalence assumptions, buy-2/get-1 alone cannot close the H173 guarantee gap.

This does not close stronger possibilities such as a genuine printed 2x doubler, free-ticket-plus-multiplier structure, or another deterministic pre-draw overlay.

## Sources
- Current Rhode Island Lottery homepage: https://www.rilot.com/en-us/home.html
- 2025 official Lucky 3 Spot Keno & Bingo Doubler rules: https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2025/LaunchAlertRules-Lucky3SpotKenoBingoDoubler.pdf

## Result
**ЕЩЁ НЕ УСПЕХ.** Even an idealized Keno `buy 2, get 1 free` interpretation yields only an 82.236825% H173 worst-case floor without a separate 2x prize multiplier.