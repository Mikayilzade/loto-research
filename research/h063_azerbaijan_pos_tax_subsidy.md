# H063 — Azerbaijan POS-linked tax subsidy / merchant-acquiring economics

Updated: 2026-08-17
Status: **VALIDATED DETERMINISTIC INCREMENTAL-PROFIT MECHANISM ON GENUINE BUSINESS RECEIPTS; NOT TERMINAL STANDALONE SUCCESS**

## Goal
Search government/card-network/payment-scheme merchant subsidies where the qualifying payment is independently economically owed, so the benefit is not created by artificial consumption.

## Strong current Azerbaijan result: public-catering POS tax relief
The Azerbaijan State Tax Service confirmed in March 2026 that amendments to the Tax Code provide a tax preference for public-catering taxpayers: for the next three years, **50% of turnover formed from non-cash POS-terminal payments is excluded from taxable general turnover** for the relevant VAT treatment. The relief requires payments through a POS terminal integrated with the cash-register system. The State Tax Service also states that income obtained from the VAT reduction is exempt from profit/income tax.

Primary current confirmation:
- https://www.taxes.gov.az/az/post/4674

The Tax Service's published worked example uses monthly catering revenue of 50,000 AZN, of which 40,000 AZN is POS turnover and 10,000 AZN cash. With 3,000 AZN input VAT credit, VAT payable falls from **6,000 AZN to 2,400 AZN** after the change.

Published example source:
- https://www.taxes.gov.az/az/post/4506

Therefore the official example implies a deterministic tax saving of:

`6,000 - 2,400 = 3,600 AZN`

on 40,000 AZN POS turnover, i.e.:

`3,600 / 40,000 = 9.0% of POS turnover`.

## Compare with a current acquiring tariff
ABB's current public POS tariff for restaurants is **2.5%** for ordinary Azericard/other cards (excluding AMEX/DC-Discover special schedules).

Source:
- https://abb-bank.az/biznes/korporativ/online-xidmetler-korporativ/pos-servisleri

Applied to the Tax Service example:
- POS turnover: 40,000 AZN
- tax saving: 3,600 AZN
- ABB ordinary restaurant acquiring fee at 2.5%: 1,000 AZN
- net incremental policy/acquiring benefit vs the pre-relief tax baseline: **2,600 AZN**
- net benefit ratio: **6.5% of POS turnover**

This is much stronger than the earlier promotion screens because it is statutory, deterministic and tied to genuine merchant revenue rather than lottery/random selection.

## Simplified-tax control
The Tax Service also published that an 8% simplified-tax catering taxpayer's POS turnover rate is reduced to 6% under the reform. In its 50,000 / 40,000 POS example, tax falls from 4,000 to 3,200 AZN: saving **800 AZN = 2% of POS turnover**.

Against ABB's 2.5% ordinary restaurant acquiring tariff, the isolated tax-rate saving would be:

`2.0% - 2.5% = -0.5%`

before any other operational benefits/costs. Therefore the simplified-tax version is **not** automatically profitable on this acquiring route.

## Why this is not terminal SUCCESS
This mechanism does prove a deterministic **incremental business profit/saving** for a qualifying VAT-registered catering merchant when:
1. the customer sale is genuine and independently owed;
2. the payment is made through the legally qualifying integrated POS channel;
3. the merchant is eligible for the statutory relief;
4. acquiring fees are below the realized tax saving;
5. the transaction remains settled/non-reversed and tax documentation is valid.

However it is not a self-starting zero-state arbitrage. The qualifying turnover must come from a real catering business transaction. The project terminal definition requires a standalone executable guaranteed positive net-profit strategy after all branches; opening/operating a catering business introduces uncontrolled demand, gross-margin, chargeback, operating-cost and compliance branches. The tax relief increases the profit of already-owed receipts but does not guarantee that the underlying business itself is profitable.

Therefore:
- **deterministic incremental-profit mechanism: VALIDATED**;
- **standalone guaranteed-profit strategy from zero: NOT VALIDATED**.

## Card-network control
Mastercard Azerbaijan currently advertises SME Easy Savings / merchant-funded rebate ecosystems, but these are discounts/rebates on business spending rather than merchant receipt grants and do not solve the standalone principal-preserving gate.

Sources:
- https://www.mastercard.com/az/az/business/industry-segment/small-medium-business/easy-savings.html
- https://www.mastercard.com/az/az/business/industry-segment/small-medium-business/sme-payment-solutions.html

## Next work
H064 should screen **statutory business subsidies that pay fixed cash/reimbursement without requiring uncertain end-customer demand**: employment/wage subsidies, export rebates, digitalization grants, energy-efficiency reimbursements, tax credits refundable in cash, and state-backed entrepreneur grants accessible in Azerbaijan. Prioritize programs with objective eligibility and formulaic payment rather than competitive selection.
