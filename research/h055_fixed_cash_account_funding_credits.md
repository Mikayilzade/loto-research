# H055 — fixed-cash account-opening / transfer / funding credits

Updated: 2026-08-17
Status: **mechanism class validated; no current Azerbaijan-executable strict guarantee found**

## Goal
Search only for current promotions where a fixed cash reward is triggered by an action that preserves the qualifying principal: opening an account, moving salary/direct deposit, transferring cash/securities, or funding an account while leaving the qualifying assets intact.

Strict accounting gate:

`G = C_min + B_min - P - F`

where `P` is qualifying principal, `C_min` is minimum recoverable principal, `B_min` is minimum irrevocably vested cash bonus, and `F` is all fees/tax/FX/withdrawal costs. Terminal SUCCESS requires `G > 0` under every contractually allowed branch and actual user eligibility.

## 1. Scotia iTRADE Summer Offer — strongest current pure funding example
Official 2026 Summer Offer is live for new accounts opened/enrolled by 31 August 2026 and funded by 30 September 2026. A client who transfers at least CAD 2,500 in net new cash/assets and maintains the qualifying amount through 30 July 2027 receives a **1% cash reward**, capped at CAD 6,000, paid by 31 August 2027.

Primary source:
- https://www.scotiaitrade.com/en/home/summer-offer.html

Important mechanics:
- qualifying assets can be cash, so market exposure is not inherently required;
- withdrawals during the qualifying period reduce the qualifying amount rather than creating a free immediate round trip;
- the reward is explicitly cash;
- the capital must stay for roughly ten months after the funding deadline.

This validates the H055 mechanism class: a regulated broker can offer a deterministic cash credit against preserved cash principal.

Why it is **not terminal SUCCESS**:
1. The product is Canadian and no evidence establishes Azerbaijan-resident eligibility.
2. The reward is not immediately vested; eligibility depends on maintaining the balance until July 2027.
3. The terminal all-outcome proof would still need account/custody protection, tax, transfer/FX and forced-account-closure treatment during the hold.

Status: **MECHANISM VALIDATED; geography/vesting prevent executable strict guarantee**.

## 2. Oriental Bank Cuenta Elite — fixed salary/direct-deposit cash
Current offer through 31 December 2026 pays a fixed tiered cash bonus after three consecutive cycles of qualifying payroll/Social Security/pension direct deposits:
- $1,500–$2,499.99 average: $200;
- $2,500–$4,999.99: $300;
- $5,000+: $400.

Primary source:
- https://orientalbank.com/en/for-you/banking-accounts/elite-account/

No minimum balance is required for the bonus; the account must remain open when credited. This is stronger than an ordinary deposit bonus because salary principal is not consumed merely by arriving in the account.

Why it is not an Azerbaijan-executable terminal strategy:
- the bank/account offer is tied to Oriental Bank's Puerto Rico/U.S. banking footprint;
- qualifying inflow must be genuine payroll/pension/government benefit direct deposit, not an arbitrary self-transfer;
- user-specific eligibility and account-opening jurisdiction are not established.

Status: **fixed-cash principal-preserving mechanism validated, execution/geography blocked**.

## 3. BMO / Old National / other U.S. checking bonuses — same mechanism, geography-gated
Current 2026 U.S. checking campaigns also pay fixed cash after genuine payroll/government direct deposits. Examples include BMO's 2026 digital checking offer and Old National's offer expiring 30 October 2026.

Sources:
- https://www.bmo.com/en-us/main/personal/checking-accounts/digital-offer/
- https://www.oldnational.com/personal/checking/checking-offer/

These are not self-funding arbitrages: the qualifying direct deposit must be employer/government-originated. They remain useful evidence that fixed cash account-switch/salary incentives are a real structural class.

Status: **class evidence only; U.S. account eligibility blocks current Azerbaijan execution**.

## 4. Swissquote transfer-bonus controls — fixed cash exists, but current public general offer not found
Swissquote Bank Europe has used fixed EUR cash transfer bonuses while requiring transferred asset value to remain for 12 months. Current indexed pages in August 2026 are either expired general offers or partner/employee-specific offers. A live universal new-client cash-transfer promotion accessible from Azerbaijan was not recovered in this run.

Sources:
- https://www.swissquote.com/en-lu/terms-and-conditions-our-transfer-offer
- https://www.swissquote.com/de-lu/gp-bullhound
- https://www.swissquote.com/en-lu/boston-consulting-group-inc

The terms also reserve discretion to charge the account for the offer cost if the required asset level is not maintained, so principal cannot be immediately withdrawn while keeping the bonus.

Status: **historical/current restricted mechanism evidence; no current universal executable candidate**.

## 5. Azerbaijan local-bank screen
Fresh current Azerbaijan search found new-business fee discounts and free banking services (AccessBank, Yelo Bank), plus ordinary cashback/yield campaigns already covered by H053/H054, but **no fixed withdrawable cash account-opening/salary-switch/funding gift** attached to preserved principal.

Current examples:
- AccessBank new-business campaign through 1 September 2026: fee discounts, not cash;
- Yelo Bank new-business campaign through 30 September 2026: 0% fees / free card, not cash;
- XalqKart: 7% annual balance yield, but reward accrues with time rather than vesting as immediate cash.

Sources:
- https://www.accessbank.az/en/biznes/endirim50/
- https://www.yelo.az/en/news/yelo-bank-extends-welcome-to-business-campaign/
- https://www.xalqbank.az/en/personal/campaigns/xalqkart-i-indi-pulsuz-elde-edin-en

Status: **NO LOCAL H055 TERMINAL CANDIDATE FOUND**.

## 6. H055 classification theorem
The screen separates four promotion types that look similar but have different guarantee status:

1. **Salary/direct-deposit cash bonus** — principal-preserving if genuine income can be routed there; terminal only if account eligibility and bonus vesting are deterministic.
2. **Asset-transfer/funding cash bonus** — principal-preserving if cash may remain cash; terminal only if hold/withdrawal/clawback and custody/insolvency branches preserve both principal and bonus.
3. **Fee discount / service credit** — lowers costs but has no separately withdrawable `B_min`; cannot create guaranteed cash profit alone.
4. **Market-valued reward** — free shares/crypto fail a fixed cash floor unless immediately liquidatable and the minimum liquidation value after all costs is contractually positive.

A current H055 candidate can be promoted toward SUCCESS only if all are proven before commitment:
- Azerbaijan-resident (or otherwise actually executable) eligibility;
- fixed cash amount, not `up to`, random, points or shares;
- principal may stay in cash/protected form;
- no trading/spending loss requirement;
- reward cannot be denied under a permitted discretionary branch after conditions are met;
- hold period and early/forced closure rules are explicit;
- principal recovery and reward survival are simultaneously bounded;
- taxes, FX, transfer and account fees are below the fixed reward.

## Current conclusion
H055 found **real, current examples of the exact economic mechanism**: deterministic cash paid for salary routing or maintaining transferred cash/assets. This is stronger than H054's free-share/asset bonuses.

However the current high-quality examples are jurisdiction-gated (Canada/U.S./Puerto Rico) or restricted/expired, while the Azerbaijan search produced discounts/yield rather than fixed cash. Therefore no current strategy yet satisfies the project's executable all-outcome guarantee standard.

**Terminal state remains: NO SUCCESS; NOT EXHAUSTED.**

## Next research
1. Search fintechs/brokers/banks that explicitly onboard Azerbaijan residents for **fixed cash** transfer/funding bonuses, prioritizing regulated entities and cash-only qualification.
2. Screen salary-account switching bonuses in Azerbaijan/Türkiye/Georgia where an Azerbaijan resident can lawfully open the account.
3. Return to H052 only through a genuinely new document route for the prepaid-interest product agreement.
4. If a geography-compatible H055 candidate appears, immediately run exact `G=C_min+B_min-P-F` proof including custody/insolvency/forced-closure and tax/FX.
