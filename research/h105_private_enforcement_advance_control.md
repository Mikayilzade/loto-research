# H105 — Azerbaijan private-enforcement advance: deterministic-refund control

Updated: 2026-08-19
Status: **MECHANISM QUANTIFIED / REJECTED AS PREFUNDED GUARANTEED-REFUND CLASS**

## Why this branch matters
H103 identified a strong state-enforcement structure: cash can already be in the state enforcement-service deposit account, statutory refund states exist, and Article 31 gives an explicit successor route when the underlying claim is assigned.

A natural follow-up is whether Azerbaijan's new private-enforcement regime (`xüsusi icra məmuru`), operational from 2026 for qualifying enforcement documents, creates an even cleaner transferable advance-refund claim.

It does **not**. The current private-enforcement advance is economically different: it is an advance against the private enforcement officer's standard fee, and its return depends on recovery of that fee from the debtor. Therefore it is not an independently prefunded state-custody refund.

## Primary current law
Official Presidential publication of the Law on Private Enforcement Officers:
- https://president.az/az/articles/view/69667

Current Ministry of Justice guidance:
- https://justice.gov.az/az/activities/13
- https://justice.gov.az/index.php/az/government-fees/criteria-and-limits-for-calculating-the-standard-fee-of-a-special-enforcement-officer

## Core mechanics
### 1. Standard fee is primarily a debtor liability
Article 25.3 provides that for money claims the standard fee is collected from the debtor together with the amount due to the claimant. If collected funds are insufficient, the standard fee is paid first.

Article 25.5 says that if the debtor does not voluntarily pay the standard fee, the private enforcement officer enforces the standard-fee decision within the same proceeding. If collection remains impossible despite enforcement measures, enforcement-action costs fall on the claimant.

This is already a major distinction from a matured state-custody refund: recovery depends on debtor collectability.

### 2. Claimant must advance part of the standard fee
Article 26.1 requires the claimant to advance the standard fee before the private enforcement proceeding begins, subject to statutory exceptions.

The Ministry of Justice currently states that, for money claims, the advance is **20% of the fixed component of the standard fee**.

### 3. Refund is conditional on debtor collection
Article 26.4 is decisive:
- when the standard fee is fully collected from the debtor, the advance is returned to the claimant;
- if the standard fee exceeds the advance and is only partially collected, the recovered amount and advance are combined and only any amount above the full standard fee is returned;
- if the standard fee cannot be collected from the debtor, the advance is **not returned** in the high-fee case;
- where the standard fee is lower than the advance, partial collection can reduce the amount consumed from the advance and the remainder is returned.

Therefore the nominal `advance` is not itself a matured refundable cash claim merely because it was paid.

## Current fee schedule and capital exposure
The Ministry of Justice publishes the fixed standard-fee schedule. For money claims the current examples are:

| Claim amount (AZN) | Fixed standard fee (AZN) | 20% claimant advance (AZN) |
|---:|---:|---:|
| 1,000 | 173.00 | 34.60 |
| 5,000 | 693.00 | 138.60 |
| 10,000 | 1,243.00 | 248.60 |
| 50,000 | 4,843.00 | 968.60 |
| 100,000 | 8,343.00 | 1,668.60 |
| 500,000 | 28,343.00 | 5,668.60 |
| 1,000,000 | 43,343.00 | 8,668.60 |

For claims above 1,000,000 AZN, the fixed component is 43,343 AZN + 1% of the excess over 1,000,000 AZN, capped at 50,000 AZN, implying a maximum ordinary 20% advance of roughly 10,000 AZN before enforcement-action expenses.

These figures are useful for future distressed-claim economics, but they do not create a guaranteed refund.

## Impossibility theorem for standalone guarantee
Let:
- `A` = claimant advance;
- `S` = standard fee due;
- `D` = amount of standard fee actually collectible from debtor;
- `R(A,S,D)` = amount of advance ultimately returned.

Current Article 26.4 explicitly permits a legal outcome with `D = 0` in which some or all of `A` is not returned.

For any strategy that pays positive consideration `P > 0` to acquire only the right to this advance/refund stream, a legal zero/low-return branch remains unless debtor recovery is already irrevocably completed and the refund has matured.

Thus:

`min_outcome cash from unresolved private-enforcement advance <= A consumed/lost`

and no strictly positive all-outcome profit can be proven merely from the existence of the advance.

### Important exception
If debtor collection of the standard fee has **already completed** and the private enforcement officer has issued/finalized a fixed refund payable to the claimant, the economic object changes. It is no longer an unresolved advance; it becomes a matured payment receivable. Such a receivable can be screened under the broader H101/H103-style framework if:
- assignability is confirmed;
- assignee payout is locked before purchase;
- refund amount is final;
- no set-off/fee/encumbrance remains;
- purchase price + costs + tax reserve are below confirmed payout.

No public live below-face instance of that matured subtype was found in this packet.

## Relation to H103
H105 should **not replace H103**.

H103 remains stronger because it combines:
- cash already held in the state enforcement-service deposit account;
- explicit statutory full/surplus refund states;
- Article-31 successor substitution within the same state enforcement proceeding.

H105's unresolved advance instead contains debtor-credit risk until fee recovery is completed.

## Current operational context
The Ministry of Justice states that the private-enforcement framework applies to qualifying enforcement documents issued after 1 January 2026; older documents can be transferred only under specified conditions and with the private officer's consent.

This confirms the branch is current and live, not merely historical legislation.

## Result
**REJECTED as a standalone prefunded guaranteed-refund class.**

Do not treat `xüsusi icra məmuru avansı` as equivalent to H103 state-enforcement advance refunds. Reopen only for a concrete case where the standard fee has already been collected from the debtor and the claimant's refund amount has become a final, assignable, redirectable receivable.

## Next implication
The search priority stays with **already matured/prefunded claims**, not advances whose repayment still depends on a debtor. Highest-value next searches:
1. final H103 state-enforcement advance refunds;
2. H101 money already cleared into enforcement-service deposit accounts;
3. other public/notarial/court custody claims where cash is already segregated and successor payout can be locked before seller payment.
