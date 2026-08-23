# H205 audit append — RI Registered Ticketless Play execution bound

Updated: 2026-08-23
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H205 RI Keno Registered Ticketless Play** | current Feb. 20 2026 official rules + current public Keno purchase UI | Keno is expressly allowed via Registered Ticketless Play; one play selects 1–10 spots; per-draw wager $1/$2/$5/$10; up to 15 consecutive draws; Ticket/RTP cap $150 base, $300 with Plus or Overtime, $450 with both | **VALID electronic Keno architecture; bulk same-draw capacity NOT PROVEN**; `research/h205_ri_registered_ticketless_play_execution_bound.md` |
| **H205 price-cap bulk shortcut** | test whether `$150 max Ticket/RTP` implies up to 150 different $1 same-draw selections | cap is fully explained by `$10 × 15 consecutive draws`; optional equal-cost Plus/Overtime explain $300/$450; rules do not publish number of independently selected same-draw lines per RTP | **REJECTED as capacity proof** |
| **H205 current iKeno public UI** | inspect exposed purchase controls | one number-selection / amount / consecutive-games / options flow and one Buy Now; no exposed add-line/quantity/import control in public page text | **SINGLE-SELECTION-SHAPED PUBLIC FLOW; absence is not impossibility proof** |
| **H205 app Favorites / digital play slips** | current official app page + FAQ + official app-store listing | Keno is online; favorite draw-game wagers can be saved/replayed; digital play slips can be scanned at retail | **VALID selection-preparation architecture; per-QR/per-scan distinct-Keno-selection capacity still unknown** |
| **H205 H175/H173 same-draw rate bound** | if one distinct selection requires one completed purchase in the 240-second draw interval | H175: `4,336/240 = 18.0667/s`; H173: `4,560/240 = 19/s` | **CONDITIONAL EXECUTION LOWER BOUND; batch mechanism could reduce it if explicitly proven** |

Conclusion: no terminal lottery guarantee. The next execution target is an explicit Keno multi-selection/panel capacity for one digital play slip/QR/transaction or vendor terminal documentation; do not infer capacity from monetary ticket limits.
