# H156 audit append — universal Keno doubler / paid add-on screen

Updated: 2026-08-21
Terminal status after packet: **NO SUCCESS; NOT EXHAUSTED**.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **BCLC Keno Doubler 2026** | July 27–Sep 7, 2026; free double-prize message | ticket is randomly selected for Doubler; replay does not guarantee another message; valid tickets generally non-cancellable | **REJECTED strict guarantee — random ownership state**; `research/h156_universal_keno_doubler_paid_addon_screen.md` |
| **Michigan Club Keno Doubler Days** | historical free Doubler control | player only has a chance to receive Doubler message | **REJECTED strict guarantee — random ownership state** |
| **Ohio KENO Double BOOSTER 2025** | all BOOSTERS doubled during fixed promo window; BOOSTER costs another $1 per $1 base wager | universal ownership validated, but `1X→2X` minimum combined with 100% add-on surcharge leaves deterministic cover ratio unchanged | **REJECTED economics; universal-paid-add-on theorem validated** |
| Ohio Keno 1–10 Spot | exact current fixed-paytable full-cover screen | base ratios 50.0000%, 66.1392%, 65.2142%, 64.9439%, 64.9951%, 64.7920%, 65.2984%, 64.7475%, 64.8069%, 63.6694%; Double BOOSTER strict floors identical | **NO guaranteed overlay**; `src/loto_research/h156_ohio_double_booster_cover.py` |
| **H156 paid-add-on theorem** | base cover ratio `r`, add-on surcharge `aS`, guaranteed promo multiplier `m_min` | promoted strict ratio `R=m_min*r/(1+a)`; profitable iff `m_min/(1+a)>1/r` | **VALIDATED general filter** |
| H155 trigger refinement | no-cost universal 2x vs paid multiplier | no-cost 2x crosses any `r>50%`; equal-cost paid add-on needs >3.083x for PA 4-Spot, >2.667x for Virginia 1-Spot, >2.467x for La Vista benchmark | **NEXT SEARCH THRESHOLDS ESTABLISHED** |

Sources:
- BCLC current rules: https://www.bclcretailerhub.com/content/dam/retailerhub/promotions/2026/Keno_Doubler_Jul_2026_RIS.pdf
- Ohio Double BOOSTER rules: https://www.ohiolottery.com/getattachment/be2303f8-361b-4beb-aca7-2b9790a8e8fb/Ohio-Lottery-KENO-Double-Booster_SepPromo_20250819.pdf
- Ohio current Keno paytable: https://www.ohiolottery.com/games/keno
- Michigan control: https://milotteryconnect.com/2019/12/30/doubler-days-returns-to-club-keno-in-january/

Master ledger note: this connector-safe append is an authoritative extension of `research/CHECKED_PROJECTS_AND_TESTS.md` until the next full-file consolidation.