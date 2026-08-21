# H149 audit append — general Nebraska Keno full-paytable theorem

Updated: 2026-08-21
Scope: LOTTERY ONLY

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H149 general Nebraska Keno full-cover theorem** | Buy every k-subset and include every fixed exact-hit payout tier `P_j` | For every draw, exact-hit count is `C(20,j)C(60,k-j)`; deterministic gross `G=sum_j P_j C(20,j)C(60,k-j)`; return `R=G/[s C(80,k)]` | **VALIDATED exact all-outcome screen**; `research/h149_nebraska_keno_general_full_paytable_theorem.md`, `src/loto_research/keno_full_cover.py` |
| **H149 Hit-k-only break-even atlas** | Derive standalone payout multiple for k=1..10 | thresholds: 4x, 16.631579x, 72.070175x, 326.435501x, 1550.568627x, 7752.843137x, 40979.313725x, 230114.607843x, 1380687.647059x, 8911711.176471x | **VALIDATED**; `data/derived/h149_keno_hitk_break_even_thresholds.csv` |
| **H149 subsidy theorem** | Add deterministic pre-owned credit/discount fraction `d` | fixed-paytable cover becomes positive iff `R_k + d > 1` under dollar-for-dollar credit and unchanged payout eligibility | **VALIDATED necessary/sufficient arithmetic condition** |
| **H149 H148 reproduction** | Omaha August 2026 `$2` 3-Spot / Hit-3 `$102` through generalized code | 82,160 tickets; deterministic gross `$116,280`; return `70.764484%` | **REPRODUCED**, confirms H148 closure |

Live-search note: fresh public web search returned transient service errors during this packet, so no new community paytable was claimed or inferred without evidence. The next run should resume current-special recovery and apply H149 immediately.
