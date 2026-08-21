# H160 audit append — Michigan Red Ball forced double-draw state

Updated: 2026-08-21
Terminal state after packet: **NO SUCCESS; NOT EXHAUSTED**.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H160 Michigan Daily 3 Red Ball Double Draw** | cumulative white-ball removal state | With five white balls already removed, only the red ball remains, so the next eligible promo day has a **guaranteed second Daily 3 evening drawing before ticket purchase** | **VALIDATED deterministic promotion state**; `research/h160_michigan_red_ball_forced_double_draw_cover.md` |
| **H160 Daily 3 full Straight cover** | all 1,000 ordered outcomes at $0.50; $250 Straight prize | one draw: cost $500, guaranteed gross $250 = 50%; forced-red day: two draws, guaranteed gross $500 = **100%** | **BREAK-EVEN ONLY / no standalone positive floor**; `data/derived/h160_red_ball_state_cover.csv` |
| **H160 subsidy corollary** | combine forced-red 100% gross cover with pre-locked compatible free play/coupon/rebate | any strictly positive compatible subsidy creates positive **pre-tax** arithmetic because draw coverage itself is break-even | **PROMISING CONDITIONAL CLASS; NOT CURRENT SUCCESS** due July promo expiry, subsidy compatibility/acceptance/tax gates |
| **H160 current Michigan screen** | August 2026 promotions and bonus channels | August Club Keno Tripler Time multiplier is random; account bonuses/coupons exist but no current universally documented compatible Daily 3 subsidy + complete-basket lock was found | **NO CURRENT EXECUTABLE GUARANTEE** |

Reusable rule: promotional trigger states that evolve by removing failed outcomes must be screened for a final state where the desired bonus event becomes certain **before** betting closes. If that certain bonus multiplies the number of independent draws by `m`, a compact game's deterministic full-cover ratio is multiplied by `m` (subject to prize/payment rules). Michigan Daily 3 reaches exactly 1.0 at `m=2`, so a future compatible deterministic subsidy is unusually high-value.
