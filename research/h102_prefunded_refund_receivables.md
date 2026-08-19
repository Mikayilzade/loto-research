# H102 — prefunded statutory refund receivables

Updated: 2026-08-19
Status: **MECHANISM CLASS VALIDATED / TRANSFERABILITY + LIVE DISCOUNT INSTANCE GATED / NOT SUCCESS**

## Goal
Search for short-maturity cash claims where the money is already prefunded, the refund amount and deadline are fixed by rule/law, and a buyer could in principle acquire the receivable below face value after the entitlement has become unconditional.

This class is adjacent to H101 but differs from debt enforcement: the underlying cash is originally the claimant's own refundable deposit/overpayment rather than money recovered from a debtor.

## 1. Azerbaijan enforcement e-auction losing-bid deposits
Current `herrac.gov.az` rules provide:
- participants must pay a bid deposit (`beh`) before joining;
- when an auction is unsuccessful, a registered participant withdraws before start, or a participant does not win, the deposit is returned;
- current portal terms state return within **5 working days** for these cases;
- the Ministry/portal FAQ also describes losing-bid deposits as refundable and gives a 7-calendar-day formulation in its FAQ.

Primary sources:
- https://herrac.gov.az/terms-conditions
- https://herrac.gov.az/faq

This creates a clean post-event cash receivable once `loss/non-winning + refundable status` is fixed.

Let:
- `D` = refundable deposit already paid;
- `P` = price paid to the original participant for the refund claim;
- `F` = transfer/notary/bank/tax costs;
- `R` = residual non-payment/recognition reserve.

Strict floor candidate:

`guaranteed_net = D - P - F - R`.

A positive deterministic spread would require `P + F + R < D` and legal recognition of the assignee before seller payment becomes irreversible.

### Current blocker
The public e-auction rules describe the refund as going back to the participant and do not publish a procedure for assigning/redirection of this refund claim to a third-party purchaser. General Civil Code Articles 193–194 support assignment of transferable claims unless prohibited by law/contract/nature, but no operator-specific assignee-recognition procedure was found.

Therefore this is **not yet equivalent to H101**, where Article 31 expressly provides successor substitution inside the enforcement proceeding.

## 2. State-property auction deposits
The State Service on Property Issues FAQ states that a 10% auction deposit is refunded if the applicant does not participate, participates and does not win, or cancels before auction; the refund is made to the person's bank account after application and supporting documents.

Source:
- https://www.emlak.gov.az/az/page/view/43

Again, the cash claim is deterministic after the relevant condition occurs, but public materials tie the refund to the original payer and do not establish pre-payment assignee recognition.

Status: **deterministic refund validated / transferability gated**.

## 3. Excess/incorrect state-fee refunds
The Law on State Duty provides that incorrectly or excessively paid state duty is refundable on application, with a statutory refund mechanism and multi-year claim window.

Source:
- https://frameworks.e-qanun.az/2/f_2860.html

This is another prefunded government receivable. However, no operator-specific route was found for buying the already-accrued refund right below face and redirecting payment to an assignee before consideration is released.

Status: **deterministic refund mechanism validated / live assignment execution gated**.

## General assignment layer
Civil Code Articles 193–194 allow an assignable claim/right to pass to a new owner in the state held by the old owner and generally permit assignment without debtor consent unless the obligation, agreement, or law forbids it.

Source:
- https://frameworks.e-qanun.az/0/c_c_8.html

This supports the legal *possibility* of receivable transfer but does not by itself prove that a specific government/auction operator will redirect the refund to an assignee through a sufficiently atomic closing process.

## Comparison with H101
H102 improves on ordinary unsecured claims because:
- cash is already prefunded;
- amount is typically fixed;
- maturity is short;
- debtor-credit risk is mostly replaced by administrative-recognition risk.

H101 remains stronger because the enforcement statute explicitly recognizes assignment-driven party substitution and routes case-specific deposited funds to the recognized claimant.

## Live execution theorem
H102 becomes a strict candidate only if, for one concrete refund:
1. entitlement is already unconditional and documented;
2. exact refundable amount `D` is confirmed;
3. the operator confirms the receivable may be assigned/redirection accepted;
4. assignee recognition + payout destination are locked before paying seller;
5. seller accepts `P < D - all costs/reserves`.

No such live below-face instance was located in this packet.

## Strategic conclusion
The **prefunded statutory refund receivable** is a valid deterministic-cash asset class, but current public rules do not yet provide the assignee-recognition gate needed for strict arbitrage. Do not treat ordinary auction deposits themselves as profit opportunities; only post-entitlement, below-face, transferable refund claims qualify.

## Next action
Prioritize:
1. refund systems with explicit third-party/assignee payment rules;
2. escrow/notary/court deposits where successor recognition is statutory;
3. current sellers of already-accrued refundable claims at a discount;
4. H101 live prefunded enforcement claims, which remain stronger whenever Article-31 substitution can be locked before payment.
