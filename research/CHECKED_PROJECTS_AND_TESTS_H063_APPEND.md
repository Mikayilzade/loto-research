# H063 append — Azerbaijan POS tax subsidy / merchant-acquiring economics

Updated: 2026-08-17
Merge these rows into `research/CHECKED_PROJECTS_AND_TESTS.md` when a safe patch/append route is available.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H063 Azerbaijan catering VAT POS relief** | official 50k turnover / 40k POS worked example | VAT payable falls 6,000→2,400 AZN; **3,600 AZN saving = 9% of POS turnover** | **VALIDATED statutory deterministic incremental-profit mechanism**; `research/h063_azerbaijan_pos_tax_subsidy.md` |
| **H063 acquiring-fee comparison** | ABB ordinary restaurant cards at 2.5% on 40k POS | 1,000 AZN acquiring fee vs 3,600 AZN tax saving => **+2,600 AZN / +6.5% POS turnover** | **POS tax benefit exceeds sampled acquiring fee** |
| **H063 simplified-tax catering control** | 8%→6% POS rate on same 40k POS | 800 AZN saving = 2%; ABB 2.5% fee => **-200 AZN / -0.5%** isolated net | **NO automatic edge on sampled route** |
| **H063 standalone terminal test** | open/operate catering business solely to capture relief | end-customer demand, business gross margin, reversals/chargebacks, operating/compliance costs remain uncontrolled | **NOT terminal SUCCESS; incremental business optimization only** |
| **H063 Mastercard SME rebate control** | Easy Savings / SME benefits | merchant-funded business-spend rebates exist, but require spending and do not create merchant-receipt cash floor | **REJECTED standalone guarantee** |
