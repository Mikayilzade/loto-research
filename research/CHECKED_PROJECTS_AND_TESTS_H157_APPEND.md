# H157 audit append — BCLC Keno Value Bundle deterministic subsidy

Updated: 2026-08-21
Terminal status after packet: **NO SUCCESS; NOT EXHAUSTED**.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **BCLC Keno Value Bundles** | current rules permit `X` paid advance draws + `Y` free draws on the purchaser's ticket | deterministic player-owned subsidy mechanism validated; unlike random Doubler/Tripler | **PROMISING CLASS / no current qualifying 2026 X:Y bundle found**; `research/h157_bclc_keno_value_bundle_threshold.md` |
| **BCLC Pick 2 full cover** | all `C(80,2)=3,160` selections under current paytable | guaranteed gross 1,900 per draw = **60.1266%**; needs `Y/X > 66.3158%`; buy-3-get-2 gives **100.21097%** conditional gross | **FUTURE BUNDLE TRIGGER VALIDATED** |
| **BCLC Pick 3 full cover** | all `C(80,3)=82,160` selections | guaranteed gross 51,300 = **62.4391%**; needs `Y/X > 60.1559%`; buy-3-get-2 gives **104.0652%** conditional gross | **FUTURE BUNDLE TRIGGER VALIDATED** |
| BCLC Pick 5 apparent overlay | base ratio 67.1718%; buy-2-get-1 appears to give 100.7576% uncapped | full-cover gross CAD 16.1481m/draw exceeds current CAD 2m combined-liability statement; strict uncapped theorem invalid | **REJECTED via liability cap** |
| Current BCLC retail promo Jul 27-Sep 7 2026 | Keno Doubler | selection is random; replay does not guarantee another Doubler | **REJECTED strict guarantee; H156 remains controlling** |

Primary sources:
- BCLC Keno game conditions: https://corporate.bclc.com/content/dam/bclccorporate/documents/terms-and-conditions/rules-and-regulations/lotto/keno-keno-bonus-game-conditions.pdf
- BCLC current Keno paytable / rules: https://www.playnow.com/keno/learn/
- BCLC current 2026 Doubler promotion: https://www.bclcretailerhub.com/content/dam/retailerhub/promotions/2026/Keno_Doubler_Jul_2026_RIS.pdf

Reproducible calculator: `src/loto_research/h157_bclc_value_bundle_cover.py`.

Master ledger note: this connector-safe append is an authoritative extension of `research/CHECKED_PROJECTS_AND_TESTS.md`; H157 should be consolidated into the master file on the next full-ledger rewrite.