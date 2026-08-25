# H264 audit append — Uganda LOTTO fixed-tier / special-roll-down screen

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| H264 Uganda National Lottery LOTTO v1.6 | Forced jackpot distribution into fixed per-winning-selection lower tiers; independent one-copy 6/52 fixed-tier full-cover audit | Div. 7 Match 3 = UGX 10,000 fixed; Div. 8 Match 2+Bonus = UGX 4,000 fixed. Special jackpot roll-down rules 7.2/7.3 explicitly exclude fixed payout divisions, and empty Div. 6 rolls to next-draw Div. 1. One-copy full cover has 20,358,520 entries, costs UGX 20,358,520,000, and exact fixed-tier gross is UGX 3,689,400,000 = **18.1221%**. | **REJECTED FOR FIXED-PER-SELECTION EXTERNAL SUBSIDY.** Current rules structurally prevent accumulated jackpot money from enhancing fixed tiers. `research/h264_uganda_lotto_fixed_tier_rolldown.md`; `src/loto_research/h264_uganda_lotto_fixed_tier_rolldown.py`; `data/derived/h264_uganda_lotto_fixed_tier_rolldown.json`. |

Reopen only if official rules route accumulated/forced-distribution funds into fixed Div. 7/8 per winning entry, or a deterministic promotion does so.
