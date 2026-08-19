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

### 3. 2025 amendment adds an explicit three-working-day payout clock
A later amendment inserted Article 74.1-1: money already transferred by the debtor to the relevant enforcement-service deposit account, or collected by the enforcement body, **and payable to the claimant must be transferred to the claimant's supplied bank account within 3 working days**.

Sources:
- https://president.az/az/articles/view/68886/print
- consolidated law: https://frameworks.e-qanun.az/1/f_1406.html — Article 74.1-1.

This materially improves H101. Once successor substitution is complete and the amount is legally classified as payable to the claimant, the remaining payout timing is no longer an open-ended administrative assumption; the statute supplies a short deadline.

### 4. General civil-law assignment layer still applies
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
7. Buyer provides own bank details under Articles 74.1-1/81-1.3 and obtains written confirmation that the credited `D-S` is payable to buyer.
8. Only after steps 2–7 are locked, release seller payment `P` from escrow/notary/bank-controlled closing.
9. Statutory payout clock is then up to 3 working days for money already classified as payable to claimant.

This is stronger than H100 because the enforcement statute explicitly supplies the **procedural substitution rule**, the **case-specific deposit-account payout mechanism**, and now a **short payout deadline** for payable claimant funds.

## Remaining failure branches that must be eliminated per deal
- Article 31 says substitution is done by enforcement-officer decision; there may be processing delay or a challenge to the assignment.
- General Civil Code assignment rules preserve pre-existing defenses/limitations; a real candidate must be screened for non-assignable/personal claims.
- A deposit-account balance may include amounts not yet distributable to this claimant or amounts subject to priority, enforcement costs, seizure, restitution, stay or competing claimants.
- The underlying enforcement document can potentially be challenged/cancelled in legally permitted cases; strict closing requires confirming that no such branch can claw back or redirect already credited funds.
- Taxes and legal/notarial/bank costs are case-specific.
- No public API/marketplace was found that exposes `already funded + distributable + offered below face` status.

## Live-market evidence — claim discounts are institutionally real
Aqrarkredit's public 2026 claim-sale competitions demonstrate that debt claims are actually sold as assets in Azerbaijan. The United Textiles FZE claim was advertised in May 2026 with an initial sale value of USD **23,109,412.64**, and a later July–August 2026 competition advertised USD **19,643,000**. That is an announced price reduction of roughly **15%** from the earlier sale value.

Sources:
- https://xalqqazeti.az/az/reklam-ve-elan/265099-aqrarkredit-qapali-sehmdar-cemiyyeti-bank
- https://www.xalqqazeti.az/az/reklam-ve-elan/269331-aqrarkredit-qapali-sehmdar-cemiyyeti-bank

Cabinet rules for these Aqrarkredit claim sales expressly permit first-competition pricing down to 70% of initial value and second-competition pricing down to 50%, while a third competition may use different pricing when recovery prospects are weak.

Source:
- https://xalqqazeti.az/az/nazirler-kabinetinin-qerarlari/134989-azerbaycan-respublikasi-nazirler-kabinetinin-qerari

This is important market evidence: **below-prior-value claim acquisition is not merely hypothetical**. However, the advertised United Textiles claim is not shown to be already prefunded into the enforcement-service deposit account, so it does not satisfy the H101 cash-floor theorem.

## Strategic conclusion
H101 remains the strongest legal deterministic-cash structure in the project:

`already-funded state enforcement deposit + legally assignable claim + Article-31 successor substitution + payout to successor + statutory short payout clock + below-face price`.

The legal mechanism is strong, and institutional claim discounting is now independently evidenced. Terminal SUCCESS still requires one concrete live transaction where the enforcement service confirms **cleared distributable funds and successor payout before buyer money is released**.

## Next action
Search specifically for:
1. claims already paid into state enforcement deposit accounts but not yet distributed;
2. creditors willing to sell those claims below distributable face value for immediate liquidity;
3. a closing structure where enforcement-officer Article-31 substitution is completed before seller payment;
4. court/notary/auction-refund equivalents with the same prefunding + successor-recognition property;
5. operator-specific refund/escrow systems with explicit assignee payout rules.
