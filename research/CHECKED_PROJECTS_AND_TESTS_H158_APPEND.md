# H158 audit append — Emirates Draw deterministic promos + SURE residual takeover

Updated: 2026-08-21
Terminal state after packet: **NO SUCCESS; NOT EXHAUSTED**

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H158 Emirates Draw EASY6 — current Onam promo** | Current automatic 30% cart discount, repeatedly applied to exact `C(39,6)` full cover; grant our cover the entire advertised shared Match-6/5/4 pools plus all fixed Match-3 payouts | face cost $19,575,738; discounted cost **$13,703,016.60**; favorable gross only **$4,138,120 = 30.198606%** | **REJECTED guaranteed-profit coverage**; `research/h158_emirates_draw_deterministic_promos_and_sure_residual_takeover.md` |
| **H158 Emirates Draw EASY6 — recent buy 6 get 3 free** | Treat 6-paid/3-free as scalable 33.3333% subsidy across full cover | effective cost **$13,050,492**; favorable gross $4,138,120 = **31.708536%** | **REJECTED even under buyer-favorable shared-pool assumption** |
| **H158 SURE1 residual inventory** | Buy all 2,623 currently remaining of 5,000 at $10; compare $26,230 cost with $30,000 board | 2,377 already-sold external tickets can occupy sole winning slot; strict buyer prize floor **$0** | **REJECTED residual takeover guarantee** |
| **H158 SURE2 residual inventory** | Buy all 2,666 currently remaining of 5,000 at $15; compare $39,990 cost with $50,000 board | 2,334 external tickets can occupy sole winning slot; strict floor **$0** | **REJECTED residual takeover guarantee** |
| **H158 SURE3 residual inventory** | Buy all 7,857 currently remaining of 20,000 at $30; compare $235,710 cost with $360,000 board | 12,143 external tickets exceed 5 winning slots and can occupy all winners; strict floor **$0** | **REJECTED residual takeover guarantee** |
| **H158 general residual-raffle theorem** | Fixed ticket pool `T`, remaining `R`, winning slots `W` | if already-sold external tickets `T-R >= W`, a legal outcome exists with every winner external; buying all remaining tickets has strict prize floor zero absent extra structural constraints | **VALIDATED screening theorem**; use before headline `remaining cost < prize pool` arithmetic |
| **H158 Emirates checkout architecture** | Order acceptance/refund and stated 10,000 ticket-per-order limit | useful transaction architecture, but does not remove external sold tickets or EASY6 payout deficit | **MECHANISM NOT SUFFICIENT** |

Files:
- `research/h158_emirates_draw_deterministic_promos_and_sure_residual_takeover.md`
- `data/derived/h158_emirates_promo_screen.csv`
- `src/loto_research/h158_emirates_promo_screen.py`

Next highest-value branch: search high-winner-count fixed-board raffles where `external sold < W` while remaining ticket cost is below the **forced minimum** payout to the residual buyer; in parallel continue deterministic Keno bundle/universal boost monitor from H157.
