# H165 audit append — NC retailer self-play + 2026 tax floor

Updated: 2026-08-22

| ID | Lottery mechanism | Test | Result | Status |
|---|---|---|---|---|
| H165-A | NC Pick 3 retailer overlay | Is a lottery retailer categorically barred from playing? | NCEL directly states lottery retailers can play lottery games; NC has no blanket retailer-play prohibition. | **VALIDATED / gate closed positively** |
| H165-B | NC own-store commission | Does public law/contract explicitly say an owner-personal own-store purchase receives 7%? | Statute/contract pay 7% on tickets sold by retailer; own play is lawful, but exact own-store accounting sentence not recovered publicly. | **PROMISING / narrower gate remains** |
| H165-C | 2026 federal wagering tax | Stress $50 forced Double Draw cover with $50 prizes + $3.50 commission under 90% loss deduction | $50 losses -> max $45 deduction; $5 taxable gambling income. Combined with $3.50 commission gives $8.50 simplified taxable increment. | **VALIDATED tax drag** |
| H165-D | H164 after-tax floor | Solve simple combined-rate break-even | `3.50 / 8.50 = 41.1764706%`. At 37% federal + 3.99% NC, simplified cushion is only **+$0.01585**, before other tax/cost friction. | **TERMINAL GUARANTEE NOT PROVEN** |

Primary sources:
- NCEL retailer-play statement: https://nclottery.com/News/2016/9/21/Some-facts-and-information-on-players-who-beat-the-odds
- NCEL 2018 compliance response: https://nclottery.com/NewsBlogDetails/2018/8/22/Lottery-conducts-checks-on-retailers
- Current Chapter 18C / 7% retailer compensation: https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/ByChapter/Chapter_18c.pdf
- Current NCEL retailer contract: https://nclottery.com/Content/Docs/Retailer_Contract_v1.pdf
- IRS 2026 §165(d) explanation: https://www.irs.gov/irb/2026-19_IRB
- IRS Publication 505 (2026): https://www.irs.gov/publications/p505
- NC 2026 individual rate: https://www.ncdor.gov/taxes-forms/individual-income-tax/tax-rate-schedules

Files:
- `research/h165_nc_retailer_self_play_tax_gate.md`
- `src/loto_research/h165_nc_double_draw_tax.py`
- `data/derived/h165_nc_double_draw_tax_sensitivity.csv`

Do not repeat the broad question whether NC retailers may play: **closed positively**. Reopen only the narrower own-store commission-accounting question with new NCEL/accounting evidence.