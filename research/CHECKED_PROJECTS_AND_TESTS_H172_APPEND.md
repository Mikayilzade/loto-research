# H172 audit append — Rhode Island pre-locked Keno doubler

Updated: 2026-08-22
Terminal status after packet: **NO SUCCESS; NOT EXHAUSTED**.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| H172 Rhode Island Lucky 3 Spot Keno | official 2024-2025 location/time-specific promotion architecture | qualifying 3-spot winners are doubled; entitlement message prints on ticket at purchase; qualifying doubled tickets cannot be cancelled; retailer cannot pre-print | **PRE-PURCHASE MULTIPLIER ENTITLEMENT VALIDATED**; `research/h172_rhode_island_prelocked_keno_doubler.md` |
| H172 RI current 2026 promo monitor | current RILOT homepage promotion carousel | `Kick Back with Keno Promotion` is live/current on homepage, but exact mechanic/rules not recovered from indexed public pages | **OPEN / TERMS-BLOCKED**; do not assume it is the Lucky 3 Spot doubler |
| H172 3-spot doubled full-space screen | conditional on $25 match-3 / $2.50 match-2 paytable and deterministic free 2x | all `C(80,3)=82,160` selections: ordinary gross $57,000 = 69.3768%; doubled gross $114,000 = **138.7537%**, +$31,840 pre-tax | **MATHEMATICAL OVERLAY VALIDATED CONDITIONALLY; current RI paytable still needs primary confirmation**; `data/derived/h172_ri_keno_doubler_fullcover.csv` |
| H172 naive retail execution | current RI Keno $150 max ticket, draw every 4 min; historical promotion location-specific + no pre-print | at least 548 full-capacity tickets; >=137 tickets/minute (2.28/sec) to load naive one-draw cover | **NAIVE FULL COVER OPERATIONALLY REJECTED absent bulk/system interface** |
| H172 reduced Keno block-design portfolio | seek smaller family of 3-subsets with doubled payout `50*n3+5*n2 > |F|` for every 20-number draw | not solved in this packet | **NEW OPEN BRANCH**; use integer programming/block design only if current/future deterministic 2x promo confirmed |

### No-repeat rule
Do not rerun the 82,160-line naive full-cover arithmetic unless the paytable changes. Reopen Rhode Island only with (a) current 2026 promotion terms, (b) primary current 3-spot paytable, (c) a bulk/atomic execution mechanism, or (d) a materially smaller rigorously guaranteed block-design portfolio.
