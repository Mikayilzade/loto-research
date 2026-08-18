# H072 — Azerbaijan electronic-money / stored-value redemption arbitrage

Updated: 2026-08-18
Status: **mechanism validated; no current strict executable instance**

## Question
Can an already-funded electronic-money or stored-value instrument be acquired below its legally redeemable residual value and then immediately redeemed for a deterministic cash profit?

This is a different class from lottery EV. The desired structure is:

`profit_floor = redeemable_balance - acquisition_price - redemption_fee - other_irreversible_costs > 0`

with all validity, ownership, transfer, KYC, fee, blocking and settlement gates locked before irreversible payment.

## 1. Statutory base: Azerbaijan electronic money has a redemption right
Primary law:
- https://president.az/az/articles/view/60819

Law on Payment Services and Payment Systems, Article 13:
- issuer must disclose residual-value redemption procedure and any applicable fee before issuance;
- Article 13.5: issuer must return the residual value of electronic money **immediately on the holder's request**;
- Article 13.7 limits contractual redemption fees to specified timing cases;
- if the issuer's license is revoked, residual values must be returned without fee.

This validates the mechanism class: a genuinely owned, valid, redeemable e-money balance has a legal face-redemption anchor rather than uncertain resale value.

Current licensed-issuer register:
- https://www.cbar.az/page-853/electronic-money-institutions?language=en

The current register includes PashaPay/m10, Portmanat, BakıKart and other licensed e-money institutions.

## 2. m10 concrete current mechanics
Primary current pages:
- https://m10.az/transfers
- https://m10.az/rates
- https://m10.az/istifade-qaydalari

Current published mechanics:
- wallet-to-wallet transfer: **0 fee**;
- wallet-to-card: published as **free up to 5,000 AZN/month** on the dedicated rate page;
- QR cash-out: **0.5%, minimum 1 AZN**;
- KYC/FIN is required for sending/receiving/transferring money;
- the agreement covers electronic-money issuance and residual-value repayment.

Mechanical thresholds, ignoring contract/execution blockers:
- receive 100 AZN m10 and cash to card within free tier: any acquisition price `<100` creates nominal spread;
- 100 AZN via QR cash-out: fee = 1 AZN, so price must be `<99`;
- 500 AZN via QR cash-out: fee = 2.50 AZN, so price must be `<497.50`.

Code:
- `src/loto_research/stored_value_redemption.py`
- `tests/test_stored_value_redemption.py`

Data:
- `data/derived/h072_azerbaijan_stored_value_screen.csv`

### Why this is not SUCCESS
The current m10 agreement preserves blocking/refusal branches that matter for a terminal all-outcome guarantee. In particular the operator may block accounts/transactions for agreement breaches, business use, security/AML concerns, unusual/non-standard operations and other stated internal-rule/law cases. The contract also restricts ordinary consumer accounts from business purposes.

Therefore a systematic OTC business of buying m10 balances at a discount cannot be promoted to strict guaranteed profit merely from the statutory face-redemption rule. A compliant isolated private transfer may work economically, but a terminal proof still needs:
1. a current lawful discounted seller/source;
2. proof the transfer settles irrevocably to our identified account before our payment becomes irreversible (or equivalent escrow/atomic settlement);
3. proof the specific acquisition/use is permitted and not subject to a blocking/business-use branch;
4. actual redemption fee shown/locked before execution;
5. taxes and any payment/withdrawal fees included.

No current indexed public market offering m10 balance below face on those terms was found in this packet.

## 3. BakıKart — unusually strong ownership/redemption mechanics, but paid resale is prohibited
Primary current terms:
- https://www.bakikart.az/Home/CardTerms

Important terms:
- unlimited BakıKart balances can be refunded immediately on written application at Card-Analysis centers when the card number is identifiable and the card/identity document are presented;
- cards are anonymous;
- a person who receives or finds the card becomes its user under the terms;
- **resale of the card is expressly not permitted**.

This creates an interesting but non-reproducible edge:
- a freely gifted valid card with positive balance can be redeemed by the holder;
- but buying such cards below balance as a systematic arbitrage violates the operator's stated resale condition.

Therefore BakıKart is **not** a current paid-acquisition guarantee path.

## 4. Portmanat control
Primary current FAQ:
- https://portmanat.az/page/faq

Portmanat supports transfers between users and cash-out through a Portmanat card. That confirms the broader transfer/redeem architecture exists locally. However this packet did not recover a sufficiently current complete cash-out fee/terms package plus a lawful discounted balance source, so Portmanat is not yet an executable candidate.

## 5. General H072 theorem
A strict stored-value arbitrage exists only if all are simultaneously true:
1. `B` is legally/contractually redeemable cash value owned by us;
2. acquisition price `P` is known and irreversible only after ownership/validity is locked;
3. total known redemption/transfer/other costs are `C`;
4. `B-P-C > 0`;
5. no allowed operator/issuer branch can block, claw back, expire, revoke or reassign the acquired value after the lock;
6. taxes do not erase the positive floor.

The law supplies (1) for qualifying e-money, but current public data does **not** supply a live instance satisfying (2)–(6).

## Conclusion
**H072 validates a new deterministic redemption class, but does not reach SUCCESS.**

Best reopen conditions:
- a live discounted m10/other licensed e-money balance offered through compliant escrow/atomic transfer;
- an issuer-sanctioned marketplace or transferable voucher explicitly permitting resale and immediate cash redemption;
- a fixed promotion that creates redeemable e-money above the user's irreversible funding cost without clawback/business-use restrictions.

Do not repeat generic e-money-law searching without one of those new execution facts.
