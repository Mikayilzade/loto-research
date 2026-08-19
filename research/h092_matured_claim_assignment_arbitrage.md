# H092 — matured claim / bank-balance assignment arbitrage

Updated: 2026-08-19
Status: **MECHANISM LEGALLY PLAUSIBLE / LIVE DISCOUNTED CLAIM NOT FOUND / NOT SUCCESS**

## Hypothesis
Acquire a legally transferable, already-matured monetary claim for less than its fixed redemption amount, notify the debtor of the assignment, and collect the face amount. This differs from cashback, lottery EV, or resale: if the claim is valid, transferable, payable now, and the debtor is solvent/obligated to pay a fixed amount, the gross spread can be deterministic.

Generic transaction identity:

`net_floor = fixed_claim_payment - acquisition_price - assignment/notary costs - taxes - execution costs`.

A terminal SUCCESS requires all of the following to be locked before irreversible payment to the seller:
1. exact claim amount and validity independently verified;
2. claim is legally assignable and not personal/non-transferable;
3. debtor has acknowledged or is legally bound to honor assignment to the new creditor;
4. no debtor set-off/objection capable of reducing the amount;
5. claim has not already been paid/assigned;
6. all assignment, tax and collection costs are bounded;
7. seller price is below the guaranteed net redemption amount.

## Azerbaijan Civil Code — mechanism exists
Current Civil Code provisions published by the Central Bank establish a broad assignment framework:
- Art. 193.1: assignable rights/claims may be transferred into another person's ownership;
- Art. 194.1: creditor may assign a claim to a third party without debtor consent unless contrary to the nature of the obligation, agreement or law;
- Art. 194.2: the assignee replaces the original creditor;
- Art. 195: until the debtor is notified, payment to the original creditor discharges the debtor;
- Art. 196: the claim transfers in the same amount and on the same terms, including associated rights;
- Art. 198: debtor may require evidence of assignment;
- Art. 199: debtor preserves objections it had against the original creditor;
- Arts. 513–521 restate the assignment framework and formalities;
- Arts. 651–654 expressly apply purchase/sale rules to rights and claims, with the seller responsible for the physical existence of the sold claim.

Primary source:
https://www.cbar.az/law-169/civil-code-of-the-republic-of-aerbaijan?language=en

This is a real legal mechanism for claim purchases; it is not merely theoretical matched betting or probabilistic EV.

## Current concrete target: residual Naxcivanbank balances held at the Central Bank
The Central Bank stated in the Naxcivanbank reorganization notice that balances of customers who had not applied for their funds were transferred to a **special account at the Central Bank**, totaling **342,858.16 AZN equivalent**. The bank's other creditor obligations were reported as performed.

Primary source:
https://cbar.az/press-release-4705/

On 5 May 2026 the Central Bank further announced that Naxcivanbank depositors and other account holders can request return of the remaining balances, including through an online application process. Individuals may receive cash regardless of amount; online applicants can request transfer to a bank account.

Primary source:
https://www.cbar.az/press-release-5477/central-bank-expands-access-to-refunds-for-nakhchivanbank-depositors-and-other-deposit-account-holders?language=en

This creates an unusually attractive research structure:
- the monetary balance already exists;
- the amount should be ledger-verifiable;
- funds are held at the Central Bank rather than dependent on a distressed private debtor's future asset recovery;
- payout is a current administrative process, not a future lottery outcome.

## Why this is not SUCCESS yet
### 1. Current refund procedure is written around the original account holder / representative
The 2026 Central Bank notice asks for the account holder's identity documents, or, for an authorized representative, identity plus power of attorney. It does not explicitly describe a purchaser/assignee of the underlying claim.

General Civil Code assignment rules are strong evidence that monetary claims can be assigned, but a strict executable guarantee requires confirmation that this specific special-account claim is not restricted by the original banking contract, reorganization terms, banking secrecy/identification rules, or the nature of the obligation.

### 2. No live discounted seller was found in the indexed public web
Fresh searches for Naxcivanbank deposit/balance/claim sale listings produced the Central Bank refund notices and historical bank pages, but no current seller offering a verified residual claim below face value.

Without a live acquisition price there is no transaction-level positive cash floor.

### 3. Debtor objections/set-off must be locked
Civil Code Art. 199/517 preserves objections that the debtor had against the original creditor. Therefore a candidate claim must be verified as an unconditional positive balance with no offset, pledge, prior assignment, legal attachment, or repayment already made.

### 4. Tax classification is not yet claim-specific
General Azerbaijan tax guidance shows business income may be taxed on either gross turnover under simplified tax or net income under income-tax regimes depending on status. A specific one-off claim-assignment tax treatment was not found in the current public guidance during this packet. Any live spread must therefore carry a conservative tax reserve until written tax treatment is confirmed.

## Deposit-insurance control
The Deposit Insurance Law also recognizes payment to a third person acting under legal authority/power of attorney, but this is not by itself proof that an insured-deposit compensation right can be sold freely. It is retained only as a control showing that third-party collection is administratively contemplated.

Primary source:
https://www.cbar.az/law-5/law-on-deposit-insurance?language=az

## Execution protocol for any live claim
Do not pay a seller merely against screenshots or a power of attorney. A strict-gate transaction should require:
1. official statement / debtor confirmation of exact unpaid balance;
2. written assignment agreement identifying the exact claim;
3. debtor notification and preferably written acknowledgment before seller payment;
4. confirmation that payment will be made to the assignee's account/cash entitlement;
5. no-offset/no-attachment/no-prior-payment confirmation;
6. seller warranty for claim existence and prior non-assignment;
7. assignment/notary/tax/transfer costs capped;
8. seller paid only after the assignee's legal entitlement is locked.

If a claim with face value `F` is offered at price `P`, the minimum pre-tax spread is `F-P`. For a conservative execution reserve `C` and tax reserve `T`, accept only when `F-P-C-T > 0` under the worst case.

## Result
H092 validates a **new deterministic-arbitrage class** in Azerbaijan: purchase of a matured monetary claim below fixed redemption value. Naxcivanbank residual balances are a particularly strong candidate because the Central Bank publicly states the balances are held on a special account and currently refundable.

However, no live discounted claim and no claim-specific assignee-acceptance confirmation were found. Therefore:

**NO SUCCESS.**

## Next work
1. search other Azerbaijan matured claims with public fixed payout and lawful assignment: court/notary deposits, liquidation distributions, utility/customer refundable deposits, compensation certificates;
2. search for live discounted claim sellers only where claim validity can be independently verified before payment;
3. if a Naxcivanbank seller appears, obtain debtor/administrator acknowledgment of assignment before any purchase;
4. build a reusable transaction-gate calculator once a live face value/ask/cost pair exists.
