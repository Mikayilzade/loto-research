# H103 — prefunded enforcement-advance refund claim assignment

Updated: 2026-08-19
Status: **MECHANISM VALIDATED IN PRINCIPLE / EXPLICIT SUCCESSOR ROUTE / LIVE DISCOUNT INSTANCE GATED / NOT SUCCESS**

## Thesis
A claimant (`tələbkar`) may pre-fund enforcement actions by transferring an advance to the state enforcement-service deposit account. Current Azerbaijan enforcement law then creates a statutory refund claim in specified states. Separately, the same enforcement proceeding expressly supports claimant substitution when the underlying claim is assigned.

This creates a stronger subclass than generic auction/refund receivables:

`already-prefunded cash -> matured statutory refund -> assigned claimant right -> Article 31 successor substitution -> refund to successor`

If a matured, fully refundable advance can be bought below its confirmed distributable amount and successor recognition is locked before seller payment, the structure can in principle create a positive deterministic cash floor.

## Primary legal mechanics

### 1. Advance is prefunded into the enforcement-service deposit account
Current `İcra haqqında` Article 80.1 states that, to ensure enforcement actions, the claimant may transfer an advance to the enforcement-service deposit account.

Source: official consolidated law on e-qanun:
- https://frameworks.e-qanun.az/1/f_1406.html

### 2. Refund is statutory
Article 80.3 states:
- when enforcement actions are completed, the advance is returned **in full** to the claimant;
- when the enforcement document is returned under Article 23.1.2–23.1.5, the portion exceeding actual enforcement-action costs is returned.

Article 23.4 independently states that when the claimant itself requests return of the enforcement document under Article 23.1.1, the Article-80 advance payment is returned to the claimant.

Article 23.7 requires the enforcement officer to issue a decision on return of the enforcement document and return of the advance; that decision is checked/approved by the head of the enforcement body.

Primary source:
- https://frameworks.e-qanun.az/1/f_1406.html

This gives three useful maturity states:
1. **completed enforcement actions -> full refund**;
2. **claimant-requested document return -> refund**;
3. **other specified document-return states -> refund of confirmed unused surplus**.

The first two are economically strongest because the nominal refundable amount can be fixed without estimating future enforcement costs once the refund decision/state is locked.

### 3. Assignment has an explicit successor mechanism inside enforcement
Article 31 expressly states that when a claim is assigned (`tələb güzəşt edildikdə`), the enforcement officer issues a decision replacing the party with its successor. Prior enforcement acts bind the successor to the same extent as the prior party.

This is materially stronger than H102 auction/refund receivables, where public operator rules were tied to the original payer and no specific assignee-redirection process was found.

Primary source:
- https://frameworks.e-qanun.az/1/f_1406.html

General Civil Code control also supports assignment of assignable claims without debtor consent unless the nature of the obligation, contract, or law forbids it (Civil Code Articles 193–194).

Primary source:
- https://frameworks.e-qanun.az/0/c_c_8.html

### 4. Deposit-account operating environment is current and electronic
The Ministry of Justice currently states that enforcement payments are electronic and may be directed to the enforcement-service deposit account; cash payments to the enforcement officer are not permitted.

Source:
- https://justice.gov.az/az/faq?tab=2

This reduces physical-cash/custody ambiguity but does not by itself prove the exact successor refund-payment workflow.

## Strict guaranteed-profit construction
Define:
- `R` = amount already in the enforcement-service deposit account and legally refundable after a final/approved refund state;
- `D` = any surviving deductions or unpaid enforcement costs;
- `P` = purchase price paid to current claimant;
- `C` = assignment/notary/bank/verification costs;
- `T` = conservative tax reserve on the realized spread;
- `X` = residual reversal/administrative reserve needed for any non-final decision or challenge branch.

Strict worst-case floor:

`G = R - D - P - C - T - X`

A terminal SUCCESS candidate requires all of the following **before P becomes irreversible**:
1. enforcement body confirms the deposit/advance amount actually received;
2. the enforcement state makes the refundable amount final and quantifiable;
3. any expense deduction is already fixed (`D` known), ideally `D=0` under a full-refund state;
4. assignment is valid under Civil Code and the underlying obligation;
5. Article-31 successor substitution is completed or made atomic with closing;
6. enforcement body confirms that the refund will be paid to the recognized successor / successor bank account;
7. no competing seizure, set-off, priority, pledge, tax lien, or seller-side encumbrance can divert the refundable amount;
8. all taxes and transaction costs are bounded;
9. `G > 0` strictly.

## Atomic closing design
Preferred sequence:

`verify deposit -> verify final refundable amount -> sign conditional assignment -> Article 31 successor decision -> written payout-recipient confirmation -> release purchase price -> receive refund`

Escrow/notarial conditional release would be preferable if available, because seller payment should not occur merely on an assignment promise.

## Strongest variants
### H103-A — completed enforcement actions, full advance refund
Best variant. Article 80.3 says the advance is returned in full once enforcement actions are complete. If the enforcement body confirms both completion and the full refund amount, `R` is largely state-independent.

### H103-B — claimant-requested document return, advance returned
Article 23.4 provides a separate refund rule when the claimant requests return under Article 23.1.1. This can create a controllable maturity trigger, but the exact operational timing and whether any costs can still survive should be confirmed on the real case.

### H103-C — unused-surplus refund
Article 80.3 / 23.5 permit refund of the amount remaining after enforcement costs in specified document-return states. This is weaker because `D` must be finally determined before purchase.

## Tax control
Tax treatment of the purchaser's spread is not yet fully resolved. Azerbaijan tax guidance confirms that assignment of a claim is a recognized taxable transaction category and that VAT timing can be triggered at assignment for relevant VAT taxpayers. Therefore no SUCCESS theorem may assume zero tax.

Source:
- https://taxes.gov.az/az/page/vergi-beledcisi

For a live case, the purchaser's status (individual vs entrepreneur/legal person), nature of the acquired claim, acquisition cost basis, and resulting income/turnover treatment must be confirmed.

## Live-market screen
Fresh searches on 2026-08-19 found:
- active institutional sale of claim rights in Azerbaijan, confirming a real market for discounted receivables/claims;
- no public listing specifically advertising an **already funded enforcement-service advance refund** or a claimant willing to sell such a matured refund below confirmed face value.

Aqrarkredit's 2026 claim-sale competitions remain proof that claim-right sale at discounts is institutionally real, but those assets are ordinary recovery claims, not prefunded refund claims.

Market control:
- https://fed.az/az/biznes/azerbaycanda-ilk-defe-sirketlerin-ozu-deyil-borcu-satisa-cixarildi-etrafli-256083
- https://fed.az/az/biznes/azerbaycan-sirketi-dubaydaki-sirkete-verilen-borcu-geri-ala-bilmedi-borcu-satisa-cixardi-260625

## Result
H103 is a **materially stronger deterministic-cash class** than H102 because it combines:
- cash already prefunded into the enforcement system;
- statutory refund entitlement;
- explicit Article-31 successor substitution when the claim is assigned.

It still fails terminal SUCCESS today because no concrete live case satisfies all execution gates, especially:
- confirmed matured refundable amount;
- seller discount below that amount;
- successor substitution and payout-recipient confirmation before seller payment;
- complete deduction/tax/encumbrance lock.

## Next test
Search specifically for claimants whose enforcement case has a refundable advance already sitting in the state enforcement-service deposit account and whose refund decision/state is final. The target is not an ordinary distressed debt; it is a **matured cash refund receivable** with an original claimant who values immediate liquidity enough to sell below face.
