# H166 audit append — NC Double Draw corporate tax + liability limits

Updated: 2026-08-22

| ID | Lottery mechanism | Test | Result | Status |
|---|---|---|---|---|
| H166-A | NC Pick 3 forced Double Draw + retailer overlay | Can 2026 tax drag be reduced under a lawful same-entity C-corp retailer/player structure? | At a conservative simple 21% federal + 2% NC corporate income-tax screen, $50 face -> $50 guaranteed prizes + $3.50 commission leaves **+$1.545 after income tax** if all income/losses belong to the same C corp. | **NUMERICALLY VALIDATED / execution entity not yet proven** |
| H166-B | NC Pick 3 scaling | Can fixed retailer/franchise costs be amortized by repeating the same complete cover? | NCEL explicitly imposes unpublished number-level prize-liability limits; combinations can sell out and further wagers are refused. Unlimited duplicate scaling is not guaranteed. | **REJECTED as guaranteed scaling assumption** |
| H166-C | Standalone new retailer | Does opening a new C-corp retailer solely for the overlay have a strict positive floor? | Minimum NC franchise tax alone is $200; simplified $50-cover after-tax edge is ~$1.545, needing ~130 completed covers before other setup/operating costs, while liability limits and intermittent forced states prevent guaranteed volume. | **REJECTED on current evidence** |
| H166-D | Existing licensed C-corp retailer | Can H164 remain alive after tax? | Yes conditionally: 23% simple income-tax screen is below the 41.1765% break-even tax rate. Still blocked by own-store commission attribution, corporate ticket ownership, atomic rollback, liability limits and active forced-state availability. | **PROMISING / NOT SUCCESS** |

Primary sources:
- NC G.S. 18C-142 / current Chapter 18C: https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/ByChapter/Chapter_18C.html
- Current NCEL retailer contract: https://nclottery.com/Content/Docs/Retailer_Contract_v1.pdf
- NCEL 2026 revenue/retailer commission explanation: https://nclottery.com/NewsBlogDetails/2026/1/2/Where-does-the-money-go
- Current Pick 3 FAQ / liability limits and cancellation: https://nclottery.com/FAQGames
- Current Pick 3 play/prize rules: https://nclottery.com/pick3-how-to-play
- IRS 2026 wagering-loss rule: https://www.irs.gov/pub/irs-irbs/irb26-19.pdf
- 26 USC 11 corporate rate: https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title26-section11
- NC corporate income/franchise tax rates: https://www.ncdor.gov/taxes-forms/corporate-income-franchise-tax/corporate-income-and-franchise-tax-rates

Files:
- `research/h166_nc_double_draw_corp_tax_and_liability.md`
- `src/loto_research/h166_nc_double_draw_corp_tax.py`
- `data/derived/h166_nc_double_draw_corp_tax.csv`

Do not treat the C-corp structure as executable until authoritative NCEL evidence establishes that the retailer legal entity may own the tickets and that its own recognized retail purchase is commission-bearing.