# CHECKED_PROJECTS_AND_TESTS — H140 append

Updated: 2026-08-21
Scope: LOTTERY ONLY

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H140 Kentucky H136-H139 current promo path** | Audit current iLottery promotional-offer entitlement before nonwithdrawable deposit | Current terms say promotional offers are discretionary, player has no right to any specific offer, offers may be cancelled without notice, and KLC disclaims loss from failure to make/accept an offer | **TERMINAL GUARANTEE CLOSED under current terms**; upstream failure exists even if stacking is later proven; `research/h140_kentucky_discretionary_promo_gate_and_prefunding_architecture.md` |
| **H140 Kentucky deposit ordering** | Determine whether principal can be recovered if promo/coverage fails | Ordinary deposited funds cannot be withdrawn/refunded/transferred except where required by law | **FAILS strict pre-commitment floor**; external cash becomes irreversible before Bonus + full-cover lock |
| **H140 Kentucky purchase acceptance** | Recheck whether full Pick 3 cover can be guaranteed after funding | KLC reserves right to refuse attempted purchases and limit wagers on particular number sets without notice | **FAILS atomic coverage gate**; one refused required selection destroys all-outcome floor |
| **H140 Kentucky stacking** | Ask whether exact Tiki/Summer/referral stacking remains terminal-decisive | No: even perfect stacking evidence cannot cure discretionary promo award + nonwithdrawable funding + purchase refusal ordering | **DEPRIORITIZED**; reopen only if official terms/process materially changes |
| **H140 subsidy threshold theorem** | Fixed-prize complete cover with ratio `r`, external cash `D`, deterministic Bonus `B` | Positive pre-tax floor iff `B/D > 1/r - 1`; for Kentucky Pair `r=.60`, threshold is **66.6667%** | **VALIDATED**; `data/derived/h140_prefunding_architecture_thresholds.csv` |
| **H140 Virginia architecture control** | Can a state lottery let player assemble draw-game cart before cash charge? | Current VA FAQ says draw tickets can be added to cart and paid at checkout by one-time debit; cart can be cleared pre-purchase | **ARCHITECTURE VALIDATED / no qualifying deterministic subsidy found in this packet**; prioritize checkout-level promos |

Primary official sources:
- Kentucky current promotions: https://www.kylottery.com/apps/promotions/promotions.html
- Kentucky Fun Club/iLottery terms: https://www.kylottery.com/apps/funclub/terms.html?pane=terms
- Virginia Lottery FAQ: https://www.valottery.com/aboutus/faq

Terminal state after H140: **NO SUCCESS; NOT EXHAUSTED**.
