# H101 — prefunded execution-service deposit claim assignment

Updated: 2026-08-19
Status: **MECHANISM VALIDATED IN PRINCIPLE / STRONGER THAN H100 / LIVE BELOW-FACE INSTANCE GATED / NOT SUCCESS**

## Goal
Test whether an Azerbaijan enforcement claim becomes a stronger deterministic cash-floor asset after the debtor's money has already reached the state enforcement service deposit account, and whether the creditor can assign that claim before payout.

## Primary legal findings

### 1. Assignment is recognized inside an active enforcement proceeding
Current `İcra haqqında` law, Article 31, explicitly states that when a party exits during enforcement because, among other things, **the claim is assigned (`tələb güzəşt edildikdə`)**, the enforcement officer issues a decision replacing that party with the successor/right-holder. Actions completed before substitution remain binding on the successor.

Source:
- https://frameworks.e-qanun.az/1/f_1406.html — Article 31.

This is materially stronger than merely inferring assignability from the Civil Code: the enforcement statute itself contemplates claim assignment and procedural substitution.

### 2. Money already received by the enforcement service is tied to the case and paid to the claimant
Article 81-1 provides that money payable under enforcement documents is received/paid only through enforcement-service deposit accounts. Transfers are linked to the specific enforcement case registration number. Under Article 81-1.3, once payable funds have entered the deposit account, the claimant supplies bank-account details and the enforcement officer orders the bank to disburse the money in the claimant's favor on the claimant's application.

Source:
- https://frameworks.e-qanun.az/1/f_1406.html — Articles 81-1.1 to 81-1.4.

The Ministry of Justice FAQ independently confirms that debtors may pay the enforcement-service deposit account and that payment is electronic, not cash.

Source:
- https://justice.gov.az/index.php/az/faq?tab=4

### 3. General civil-law assignment layer still applies
Civil Code Articles 193–194 provide that assignable claims/rights can be transferred to another owner; the claim passes in the condition held by the old owner, and (subject to exceptions) a creditor may assign without debtor consent.

Source:
- https://frameworks.e-qanun.az/0/c_c_8.html

## Deterministic-cash theorem
For a **specific enforcement case where the debtor's money has already been credited to the enforcement-service deposit account and is legally payable to the claimant**, a below-face acquisition can create a strict positive cash floor if all gates are locked before seller payment becomes irreversible.

Let:
- `D` = funds already credited to the case-specific enforcement-service deposit account and distributable to claimant;
- `S` = surviving senior deductions, offsets, enforcement expenses or legally prior claims that can still reduce claimant payout;
- `P` = acquisition price paid to old claimant;
- `F` = assignment/notary/legal/bank/tax costs;
- `R` = any residual reversal/litigation reserve that cannot be eliminated before closing.

Strict floor:

`guaranteed_net = D - S - P - F - R`.

SUCCESS condition:

`D - S - P - F - R > 0`

**and** the buyer is formally substituted/recognized as claimant before `P` becomes irreversible.

## Strong atomic workflow
1. Obtain enforcement-case number and original enforcement document.
2. Enforcement officer confirms in writing that amount `D` has actually cleared to the correct case-specific deposit account, not merely been promised or initiated.
3. Confirm exact amount legally payable to claimant after all deductions/priority claims and that no stay, cancellation, competing claim, appeal, restitution or seizure can still divert it.
4. Execute assignment agreement in legally sufficient form.
5. Submit assignment to enforcement officer.
6. **Enforcement officer issues Article-31 substitution decision naming buyer as successor claimant.**
7. Buyer provides own bank details under Article 81-1.3 and obtains written confirmation that the credited `D-S` will be disbursed to buyer.
8. Only after steps 2–7 are locked, release seller payment `P` from escrow/notary/bank-controlled closing.
9. Receive deposit-account payout.

This is stronger than H100 because the enforcement statute explicitly supplies both the **procedural substitution rule** and the **case-specific deposit-account payout mechanism**.

## Remaining failure branches that must be eliminated per deal
- Article 31 says substitution is done by enforcement-officer decision; there may be processing delay or a challenge to the assignment.
- General Civil Code assignment rules preserve pre-existing defenses/limitations; a real candidate must be screened for non-assignable/personal claims.
- A deposit-account balance may include amounts not yet distributable to this claimant or amounts subject to priority, enforcement costs, seizure, restitution, stay or competing claimants.
- The underlying enforcement document can potentially be challenged/cancelled in legally permitted cases; strict closing requires confirming that no such branch can claw back or redirect already credited funds.
- Taxes and legal/notarial/bank costs are case-specific.
- No public API/marketplace was found that exposes `already funded + distributable + offered below face` status.

## Live-market search
A current Azerbaijan example confirms that **claims themselves are actively sold by formal competitive process**: Aqrarkredit announced sale of the United Textiles FZE debt claim in July–August 2026, with applications open through 19 August 2026 and winner determination scheduled for 25 August 2026. This proves an institutional claim-sale market exists, but the advertised claim is not shown to be already prefunded in an enforcement-service deposit account and therefore is **not H101 SUCCESS**.

Source:
- https://www.xalqqazeti.az/az/reklam-ve-elan/269331-aqrarkredit-qapali-sehmdar-cemiyyeti-bank

## Strategic conclusion
H101 is currently the strongest legal deterministic-cash structure in the project:

`already-funded state enforcement deposit + legally assignable claim + Article-31 successor substitution + payout to successor + below-face price`.

The legal mechanism is stronger than H100, but terminal SUCCESS still requires one concrete live transaction where the enforcement service confirms **cleared distributable funds and successor payout before buyer money is released**.

## Next action
Search specifically for:
1. claims already paid into state enforcement deposit accounts but not yet distributed;
2. creditors willing to sell those claims below distributable face value for immediate liquidity;
3. a closing structure where enforcement-officer Article-31 substitution is completed before seller payment;
4. court/private-executor equivalents with the same prefunding + successor-recognition property.
