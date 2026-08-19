# H104 — Azerbaijan sovereign fixed-income control

Updated: 2026-08-19
Status: **CONTRACTUAL POSITIVE YIELD VALIDATED / NOT TERMINAL GUARANTEE**

## Thesis
Before continuing more exotic prefunded-claim arbitrage, close the obvious local fixed-income control: Azerbaijan Ministry of Finance government bonds can provide a contractually specified positive nominal return when bought and held to maturity. This is a useful low-risk benchmark, but it is not the project's terminal `SUCCESS` because the positive return is conditional on issuer performance and execution at the quoted/allotted price; it is not an all-outcome arbitrage with prefunded principal plus locked surplus.

## Current 2026 benchmark
A 26 May 2026 auction of Azerbaijan Ministry of Finance 3600-day coupon government bonds had:
- ISIN `AZ0301250012`;
- nominal value: **100 AZN**;
- coupon rate: **7.0%**;
- maturity: **26 May 2036**;
- cut-off price: **100.0000 AZN (7.0000% yield)**;
- weighted-average price: **100.0043 AZN (6.9993% yield)**;
- placed volume: **200,000,000 AZN**.

Independent market reporting and ABB Invest's weekly review both reproduce the ~7% auction result.

Sources:
- https://www.abbinvest.az/az/kapital-valyuta-ve-emtee-bazarlarinin-heftelik-icmali-25-29-may-2026-ci-il
- https://www.financetime.az/news/news-view.php?id=43336

## Legal payment structure
Azerbaijan budget-execution rules state that state-debt servicing — principal and interest — must be carried out fully and on time regardless of budget revenue volume/allocation level, in accordance with the credit agreement or state-security terms.

Primary legal source:
- https://versions.e-qanun.az/6/f_6038.html

This establishes a strong contractual/statutory payment obligation and makes government bonds a far stronger credit instrument than ordinary unsecured corporate bonds.

## Tax treatment relevant in 2026
Tax guidance states that from **1 February 2023 for five years**, dividend, discount and interest income on shares/bonds that were publicly offered and admitted to trading on a regulated market are exempt from income tax.

For qualifying exchange-traded bonds, this means the current exemption window runs through **31 January 2028**, subject to the exact instrument and investor status.

Primary tax guidance:
- https://taxes.gov.az/az/post/1947
- https://taxes.gov.az/az/page/suallar-ve-cavablar?page=63

## Why this is not terminal SUCCESS
The project's terminal standard is stronger than ordinary 'low-risk fixed return'. A strict all-outcome guarantee would need `cash_received - all_costs > purchase_price` under every allowed execution branch.

Government bonds fail that absolute theorem for at least four reasons:
1. **issuer-performance branch** — payment is a sovereign obligation, not cash already segregated for this individual holder in a bankruptcy-remote escrow;
2. **execution-price branch** — auction orders may be rejected/partially filled and secondary-market acquisition price can vary;
3. **intermediary/transaction-cost branch** — exact broker/custody/settlement fees must be known before purchase for a strict net-profit floor;
4. **time/liquidity branch** — early sale exposes the holder to market price risk; the positive contractual yield is locked only if the bond is successfully acquired at an acceptable price and held through payment/maturity.

Thus this is **not arbitrage**. It is conventional sovereign fixed income with a positive contractual yield conditional on issuer performance.

## Conditional return identity
If a qualifying bond is acquired at all-in price `P`, future contractual coupons/redemption total `F`, and all costs/taxes are `C`, then the hold-to-maturity nominal profit is:

`G_conditional = F - P - C`.

For the May 2026 10-year issue, an allocation near par creates an approximately 7% annual nominal yield before investor-specific costs. The tax exemption materially improves the 2026 after-tax result for qualifying regulated-market instruments.

But the project may not label this `SUCCESS` because `F` is an issuer obligation rather than a prefunded, irrevocably segregated cash amount already assigned to the buyer.

## Strategic conclusion
H104 closes the broad class **ordinary positive-yield bonds / deposits / fixed income** as a terminal-guarantee candidate.

Use these instruments only as:
- a low-risk benchmark for opportunity cost;
- a place to park capital while searching;
- a comparator for any exotic strategy's net yield and operational burden.

Do not spend further research cycles trying to rebrand ordinary coupon yield as guaranteed arbitrage unless a new structure adds a genuinely prefunded or third-party-insured all-outcome cash floor.

## Next priority
Return to the stronger deterministic-cash classes H103/H101/H102: prefunded claims where the cash is already inside a state/custodial payment system and successor recognition can be locked before seller payment.