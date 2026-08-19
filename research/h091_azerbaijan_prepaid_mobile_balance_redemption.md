# H091 — Azerbaijan prepaid mobile balance redemption / secondary-market arbitrage

Updated: 2026-08-19
Status: **REJECTED as guaranteed-cash redemption class**

## Question
Can discounted prepaid mobile balance/top-up value be acquired below face value and then converted back to cash or a cash-equivalent at a fixed operator redemption value?

For a strict arbitrage we need all of:
1. lawful acquisition below redemption value;
2. contractual right to cash redemption or a deterministic cash-equivalent exit;
3. all fees bounded before purchase;
4. no operator discretion/clawback that can erase the spread.

## Current operator evidence

### Azercell
Azercell's current prepaid-to-postpaid FAQ explicitly says that remaining AZN balance is carried into the postpaid account, but the subscriber **cannot use that amount as cash**; it may only be used to settle invoice debt and cannot be transferred to another number after conversion.

Primary/current source:
- https://www.azercell.com/en/personal/support/number-purchase-and-operations/how-to-transfer-mobile-number-from-prepaid-to-postpaid.html

Implication: prepaid AZN balance is not an operator-guaranteed cash claim.

### Bakcell
Bakcell currently supports balance transfer between Bakcell subscribers, but only in discrete amounts and with material service fees:
- 1 AZN transfer -> 0.25 AZN fee;
- 3 AZN -> 0.60 AZN fee;
- 5 AZN -> 1 AZN fee.

Current source:
- https://www.bakcell.com/money-transfer

Bakcell's number lifecycle page further states that, after cancellation, remaining prepaid balance is deleted; on subscriber request the deleted amount may be restored after applicable charges, but the wording describes restoration/refund **to the subscriber's number**, not cash redemption to a bank/cash account.

Current source:
- https://www.bakcell.com/en/online-payment

Therefore Bakcell provides a transfer/usage mechanism, not a deterministic cash exit.

## Arbitrage test
Suppose discounted telecom value of face `F` is acquired for `A<F`.

A strict cash arbitrage would require a deterministic cash redemption `R` with:

`R - A - fees > 0`.

For the checked operators, no such `R` exists in the public terms:
- Azercell: explicit non-cash restriction;
- Bakcell: transfer only, with 20–25% fees on the published small transfer denominations, and no fixed cash redemption right found.

Even if a secondary-market buyer values balance near face, that is a resale/liquidity trade, not a guaranteed operator cash floor.

## Result
**REJECTED as standalone guaranteed-profit class.**

Discounted prepaid mobile balance may have ordinary resale/use value, but the operator contract does not create a fixed cash redemption floor that can be locked before acquisition.

## Re-open gate
Only reopen if a current Azerbaijan operator/payment product is found with all of:
- explicit cash/bank redemption of unused prepaid balance;
- transferable ownership or lawful discounted acquisition;
- fixed redemption formula known before acquisition;
- fees/caps small enough to leave positive spread.
