# H100 — Prefunded notary-deposit claim assignment in Azerbaijan

Updated: 2026-08-19
Status: **MECHANISM VALIDATED IN PRINCIPLE / NO LIVE BELOW-FACE CLAIM FOUND / NOT SUCCESS**

## Goal
Test whether a creditor claim can become a strict deterministic arbitrage **after the debtor has already funded a notary deposit**, by buying that already-funded claim below face value and then collecting the locked deposit as the new creditor.

This is stronger than buying an ordinary receivable because the cash has already been placed with a regulated custodian and, under the notary-deposit rules, the original debtor generally cannot simply retrieve it without the creditor's written consent or a court decision.

## Primary legal sources
1. Azerbaijan Civil Code, Arts. 193–199 (assignment of claims):
   - https://frameworks.e-qanun.az/0/c_c_8.html
2. Law on Notariat, Arts. 74–75:
   - https://frameworks.e-qanun.az/0/f_107.html
3. Instruction on notarial acts, paras. 152–157:
   - https://frameworks.e-qanun.az/0/f_488.html
4. Ministry of Justice current notarial state-fee schedule:
   - https://justice.gov.az/az/government-fees/state-fee-rates-for-notarial-acts-performed-by-notaries-and-state-bodies-issuance-of-a-certificate-to-engage-in-notarial-activities-and-extension-of-its-term

## What is legally validated
### 1. General assignment is broad
Civil Code Art. 193 allows an assignable claim/right to be transferred to another person's ownership. The right passes in the condition it had in the previous owner's hands.

Art. 194 states that a creditor may assign a claim to a third party without the debtor's consent unless the nature of the obligation, agreement, or law forbids it. Claims inseparably linked to the creditor's person are excluded.

Art. 196 is important for the arbitrage theorem: unless otherwise provided, the claim passes to the new creditor in the same amount and on the same terms existing at transfer, together with associated rights.

Arts. 195 and 198 imply an operational requirement: the debtor/custodian must be notified and the new creditor must prove the transfer before performance can be demanded.

### 2. A notary deposit is already-funded performance
Under the Law on Notariat, Art. 74, a notary can receive money/securities deposited by the debtor for delivery to the creditor. The notary informs the creditor and, on the creditor's demand, gives the money/securities to the creditor.

The notarial instruction states that depositing the performance object can be treated as performance to the creditor such that the debtor is discharged from the obligation.

### 3. Debtor clawback is constrained after funding
Law on Notariat Art. 75 / instruction para. 157 states that money/securities deposited by the debtor may be returned to the debtor only with the written consent of the person in whose favor the right was given (creditor) or on the basis of a court decision.

This matters because it removes the ordinary 'seller assigns the claim, then debtor voluntarily withdraws the money' branch, provided the assignee has validly stepped into the creditor's position and the notary recognizes the assignment before purchase becomes irreversible.

## Deterministic-arbitrage construction
Let:
- `D` = amount already deposited with the notary for the creditor;
- `P` = price paid to acquire the claim;
- `F` = all transfer/notarial/bank/tax/collection costs;
- `R` = any legally valid deduction, defense, offset, expiry loss, or other reduction that can still be asserted against the assignee.

A strict pre-funded claim arbitrage exists only if, **before paying the seller**:
1. the notary confirms the deposit exists and identifies the current beneficiary/claim;
2. the claim is legally assignable;
3. the assignment can be registered/notified so that the notary will pay the assignee;
4. no unresolved defenses/offsets/expiry restrictions can reduce the amount;
5. seller payment is conditional on successful assignment/recognition; and
6. `D - R - P - F > 0`.

If `R=0` is locked and `D` is already held by the notary, the construction becomes materially stronger than a normal receivable trade because debtor credit risk is largely replaced by custodian/transaction-legality risk.

## Fees / execution hurdle
The current Ministry of Justice schedule shows that other valued contracts between unrelated parties carry a 100-AZN state fee; whether a particular claim-assignment contract is classified exactly in that category must be confirmed by the notary. Related notarial service fees may also apply under the Notariat Law.

Therefore the live buy threshold is not simply `P < D`; it is approximately:

`P < D - all fixed/variable transfer and collection costs - conservative legal reserve`.

For small claims, fixed notarial cost can erase the spread. The mechanism is much more interesting for larger already-funded claims.

## Important residual risks that prevent terminal SUCCESS today
### 1. No live below-face prefunded claim found
Current public searches did not reveal a verifiable Azerbaijan marketplace/listing for an already-funded notary-deposit claim being sold below its locked deposit value.

### 2. Assignment must be recognized by the custodian before seller payment
Civil Code Art. 198 allows performance to be withheld until proof of assignment is presented. A strict execution design therefore needs the notary to confirm recognition of the new creditor before the acquisition price becomes irreversible.

### 3. Existing defenses survive assignment
Civil Code Art. 199 allows the debtor to assert against the assignee defenses it had against the original creditor when notified. Thus a mere deposit receipt is not enough if the underlying claim can still be challenged, offset, time-barred, or otherwise reduced.

### 4. Deposit retention/expiry rules matter
Legacy/current notarial instructions impose retention periods for unclaimed deposits and transfer of unclaimed amounts to the state budget after the relevant period. A candidate must be well inside all applicable limitation/retention windows.

## Live-market screen
The current official Electronic Auction portal was checked as a possible source of discounted claims. Its rules and public listings are designed for sale of seized debtor **property** to satisfy claims; the public portal does not currently expose a category for already-funded notary-deposit claims.

This does not disprove private claim sales, but it removes the obvious official marketplace route.

## Conclusion
H100 validates a **new deterministic mechanism class**:

> Buy a legally assignable claim only after the debtor has already placed the full amount in a notary deposit, condition seller payment on the notary recognizing the assignment, and buy below locked distributable value net of all costs.

This is stronger than H093's generic 'funded claim' concept because Azerbaijan law provides both:
- broad claim-assignment rules; and
- a specific prefunded notary-deposit structure where debtor clawback is constrained.

However, terminal SUCCESS is not reached because no concrete below-face claim with pre-payment notary confirmation and positive all-in spread has been found.

## Reopen / execution gate
Only spend more research time on this branch when one of the following appears:
1. a seller offers a specific notary-deposit claim below face value;
2. a lawyer/notary confirms an atomic workflow: verify deposit -> execute assignment -> register/notify -> confirm assignee payout -> release purchase price;
3. a public/private marketplace for funded claims is identified;
4. an official procedure explicitly states how a notary pays an assignee of an existing deposit.

Until then status remains **mechanism validated, live-instance gated**.
