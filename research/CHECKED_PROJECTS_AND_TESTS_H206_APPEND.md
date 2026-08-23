# H206 audit append — RI iLottery cart and purchase-limit gate

Updated: 2026-08-23
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H206 RI iLottery cart architecture** | current official FAQ wording for Keno/draw-game purchases | FAQ explicitly refers to Keno-inclusive wagers resulting from **cart purchases submitted** | **VALID current cart architecture; Keno distinct-line capacity still unknown**; `research/h206_ri_ilottery_cart_and_purchase_limit_gate.md` |
| **H206 H205 rate bound reclassification** | test whether 4,336/240=18.0667/s and 4,560/240=19/s are unconditional | current cart architecture means one checkout may potentially submit multiple wagers; public source does not state Keno lines/cart | **RATE BOUNDS REMAIN CONDITIONAL ONLY** |
| **H206 VIP Plus purchase-limit gate** | current official FAQ Responsible Gambling section | default daily/weekly/monthly purchase limits exist and user limits cannot exceed Lottery maximums; numerical Lottery maximums not published in recovered public FAQ | **NEW NECESSARY EXECUTION GATE; UNRESOLVED** |
| **H206 minimum single-account spend hurdle** | $1 base wagers for H175/H173 | H175 requires at least **$4,336** accepted paid wagers; H173 at least **$4,560**; any paid add-on increases hurdle | **Lottery daily/weekly/monthly caps must exceed required total** |
| **H206 Keno draw-break timing** | current official FAQ + 4-minute Keno cadence | wagering unavailable during each game's draw-break period; duration not published | **240-second rate denominator is optimistic if per-selection fallback is needed** |
| **H206 cart atomicity** | search current official public help/UI | no published guarantee that a large Keno basket is all-or-none, nor a published same-draw Keno cart-line maximum | **UNRESOLVED; strict coverage execution cannot assume atomic acceptance** |

Conclusion: no terminal lottery guarantee. H206 improves execution modeling by proving current cart submission exists while identifying undisclosed purchase maxima, cart capacity/atomicity, and draw-break duration as the next exact RI Keno gates.
