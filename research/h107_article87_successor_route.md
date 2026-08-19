# H107 — Article 87.4 successor route / assignee-recognition theorem

Updated: 2026-08-19
Status: **LEGAL ROUTE MATERIALLY STRENGTHENED / LIVE EXECUTION STILL GATED / NOT SUCCESS**

## Goal
Resolve the largest remaining legal blocker in H106: whether a purchaser/assignee of an already-final bank-liquidation payout right can plausibly qualify to collect Article 87.4 cash after assignment, rather than the right being collectible only by the original creditor or hereditary heir.

## Primary-source findings

### 1. Bank law explicitly protects collection by successors
Current Azerbaijan `Banklar haqqında` Article 87.4 states that after a court-approved payment schedule is final, if the scheduled creditor cannot be contacted, the unpaid amount is deposited into a special account at the Central Bank. It then states that the deposited money may be collected before limitation expiry by the stated creditors **or their `hüquq varisləri`**.

Primary source:
- https://www.cbar.az/law-1/the-law-on-banks?language=az

Relevant current text is around Article 87.4.

### 2. Civil Code makes a voluntary assignee replace the original creditor
Current Civil Code Articles 193–196 materially strengthen the interpretation that an assignee is a legal successor to the claim:
- 193.1: an assignable claim/right may be transferred to another person's ownership; rights pass in the condition held by the previous owner;
- 194.1: a creditor may assign a claim to a third person without debtor consent unless prohibited by the obligation/agreement/law;
- 194.2: by the assignment agreement, **the third person takes the place of the first owner/creditor**;
- 196: the claim transfers in the same scope and conditions, including connected rights, and the new creditor may exercise the claim's priority in **forced enforcement and insolvency**.

Primary source:
- https://frameworks.e-qanun.az/46/f_46944.html

### 3. Debtor/operator notification is the key operational step
Civil Code Article 195 provides that until the debtor is notified of the assignment, it may validly perform to the original creditor. Article 198 permits the debtor to withhold performance until proof that the claim passed to the new creditor is presented.

This changes the practical gate from a vague `is assignment legally possible?` question into a concrete execution requirement:

`assignment signed -> operator/liquidator/CBA-side recipient notified -> proof accepted -> successor recipient locked -> only then seller paid`.

### 4. Current liquidation infrastructure is active and centralized
ADIF currently maintains a public page of banks in liquidation and their special liquidation-account details at the Central Bank, including current liquidation contacts (notably hotline 941 for multiple banks). This confirms the administrative counterparty and special-account infrastructure are not merely historical abstractions.

Primary sources:
- https://adif.gov.az/az/cancelletion/
- https://adif.gov.az/az/announcements

ADIF has also publicly routed liquidation-creditor payments through an identified payout bank in prior creditor-payment programs, showing that creditor payout is operationally identity/document based rather than technically inseparable from the original bank account.

Historical operational example:
- https://adif.gov.az/az/news/2019-10-30-1100-8

## Legal inference
The strongest current reading is:

1. Article 87.4 expressly allows collection by a creditor's `hüquq varisi`.
2. Civil Code 194.2 expressly replaces the old creditor with the new creditor after assignment.
3. Civil Code 196 expressly preserves insolvency-related rights for the new creditor.
4. Therefore a valid civil assignee has a strong statutory basis to be treated as the successor holder of the Article-87.4 claim.

This is an inference from the combined statutes; no public ADIF/CBA form or instruction was found that says verbatim `cession assignee = Article 87.4 hüquq varisi`.

## What is now closed
The broad legal objection `Article 87.4 might be hereditary-successor-only and exclude cession` is **materially weakened and no longer the main blocker**.

The remaining strict-SUCCESS blockers are operational and transaction-specific:
- identify an actual Article-87.4 amount already segregated at CBA;
- verify exact payable amount and limitation deadline;
- verify no attachment, set-off, competing assignment, identity defect or tax leakage;
- obtain written acknowledgment from ADIF/liquidator/payout operator that the named assignee will be recognized as recipient after specified documents are filed;
- structure seller consideration so it is released only after that acknowledgment;
- buy below `R - C - T - X`.

## Atomic execution theorem
Let:
- `R` = exact confirmed Article-87.4 segregated payout;
- `P` = seller price;
- `C` = all notary/assignment/bank/execution costs;
- `T` = conservative tax reserve;
- `X` = residual encumbrance/admin reserve.

A strict guaranteed-profit transaction requires:

`G = R - P - C - T - X > 0`

**and**, before `P` becomes irreversible:
- court schedule final and non-appealable;
- `R` already deposited/segregated under Article 87.4;
- assignment valid and documented;
- assignee-recipient status accepted in writing;
- limitation and encumbrances checked.

## Result
H106 is stronger than before: the legal-successor bridge is now supported directly by Article 87.4 plus Civil Code 194.2/196. The project still lacks a concrete discounted live claim and pre-payment written recipient lock, so this is **NOT SUCCESS**.
