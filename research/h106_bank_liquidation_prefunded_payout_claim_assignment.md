# H106 — prefunded bank-liquidation payout claim assignment

Updated: 2026-08-19
Status: **STRONG MECHANISM VALIDATED / CASH-SEGREGATION + FINAL SCHEDULE PRESENT / ASSIGNEE-RECOGNITION + LIVE DISCOUNT INSTANCE GATED / NOT SUCCESS**

## Thesis
A particularly strong deterministic-cash structure exists inside Azerbaijan bank liquidation law after a creditor claim has passed all insolvency uncertainty:

`confirmed creditor claim -> court-approved final payout schedule -> unpaid scheduled amount deposited in a special Central Bank account -> successor/assignee recognition -> payout to new holder`

The important distinction from ordinary distressed debt is that the target is **not** an unresolved claim against an insolvent bank. The target is a claim for money that has already been allocated under a final court-approved payment schedule and, where the creditor cannot be contacted, has already been segregated into a special account at the Central Bank.

If such a funded payout right can be assigned below its confirmed distributable amount and the liquidator/Central Bank recognize the new holder before buyer funds become irreversible, it can in principle create a strict positive cash floor.

## Primary legal mechanics

### 1. Court-approved payment schedule is final
Current Azerbaijan `Banklar haqqında` Law Article 87 provides:
- confirmed creditor claims are classified and included in the distribution table;
- the liquidator submits a payment schedule for court approval;
- Article 87.3 states the court-approved payment schedule is **final** and cannot be appealed;
- after approval, the liquidator must immediately execute the scheduled payments.

Primary sources:
- Central Bank consolidated Banks Law: https://www.cbar.az/law-1/the-law-on-banks?language=az
- e-qanun consolidated Banks Law: https://frameworks.e-qanun.az/5/f_5825.html

This sharply reduces ordinary insolvency-value uncertainty once the exact creditor amount is already in the final schedule.

### 2. Unpaid scheduled cash is segregated at the Central Bank
Article 87.4 states that where a scheduled creditor cannot be contacted, the unpaid amount is deposited into a **special account at the Central Bank**. The liquidator must publish notice inviting the creditor to collect it.

The same Article says money deposited this way may be collected by the specified creditors **or their legal successors (`hüquq varisləri`)** until the claim limitation period expires; after that it is transferred to the state budget.

Primary sources:
- https://www.cbar.az/law-1/the-law-on-banks?language=az
- https://frameworks.e-qanun.az/5/f_5825.html

The Constitutional Court has independently described this same mechanism: final court-approved schedule, immediate payment, and uncontactable-creditor amounts placed into a Central Bank special account for the creditor or legal successor.

Source:
- https://constcourt.gov.az/az/decision/371

### 3. General assignment law strongly supports transfer of insolvency claims
Civil Code Articles 193–196 provide that:
- an assignable claim/right can be transferred to another person;
- a creditor can assign a claim without debtor consent unless prohibited by the nature of the obligation, agreement or law;
- the new creditor replaces the old creditor;
- existing associated rights transfer with the claim;
- critically, Article 196 states that the new creditor may exercise the priority connected with the claim in **forced enforcement and insolvency**.

Primary source:
- https://frameworks.e-qanun.az/0/c_c_8.html

This is unusually relevant to H106 because the claim is already inside an insolvency procedure.

### 4. Assignment is a form of legal succession in Azerbaijan procedural law
The Constitutional Court has expressly explained that material legal succession can be universal or singular and gives **assignment of a claim (`tələb güzəşt edildikdə`)** as an example of singular succession. It also notes that procedural substitution may occur when a claim is assigned.

Source:
- https://constcourt.gov.az/az/decision/1340

This materially strengthens the interpretation that an assignee can become a `hüquq varisi` of the original creditor. However, bank liquidation has a special statutory procedure, so a terminal theorem still requires the liquidator/court/Central Bank to recognize the specific assignee for the already-segregated Article-87.4 payout before seller payment.

### 5. Current liquidation infrastructure is live
ADIF currently maintains a public list of banks in liquidation and their special liquidation account details at the Central Bank, including Muğan Bank, AG Bank, NBC Bank, Atabank, Amrahbank, Bank Standard, DəmirBank and others.

Source:
- https://adif.gov.az/az/cancelletion/

ADIF also maintains creditor announcements and an electronic creditor portal for banks in liquidation.

Source:
- https://adif.gov.az/az/announcements

Historical/current-process evidence therefore confirms that this is not merely a dormant statutory construct.

## Strict construction
Define:
- `R` = exact cash amount in the final court-approved schedule and already segregated for the creditor in the Article-87.4 Central Bank special account;
- `P` = purchase price paid to the current creditor;
- `C` = assignment/notary/court/liquidator/bank/verification costs;
- `T` = conservative tax reserve on the spread;
- `X` = residual reserve for any legally surviving set-off, attachment, limitation, identity or administrative risk.

Worst-case profit floor:

`G = R - P - C - T - X`

A terminal SUCCESS candidate requires **before P becomes irreversible**:
1. liquidator confirms the creditor claim and exact scheduled amount;
2. court-approved schedule is final under Article 87.3;
3. liquidator confirms that the exact unpaid amount has already been deposited into the Article-87.4 Central Bank special account;
4. limitation period has not expired;
5. assignment is valid and not restricted by the specific claim documents;
6. assignee is formally recognized as the successor/new creditor in the liquidation file;
7. liquidator/Central Bank provide written confirmation that `R` will be paid to the assignee/new holder rather than the original creditor;
8. no attachment, set-off, lien, competing assignment or seller-side encumbrance can divert `R`;
9. taxes/fees are bounded and `G > 0` strictly;
10. seller payment is released only after gates 1–9 are locked, ideally through conditional notarial/escrow closing.

## Atomic closing design
Preferred sequence:

`verify final schedule -> verify exact CBA-segregated cash -> verify limitation/encumbrances -> sign conditional assignment -> obtain liquidator/court successor update -> obtain written payout-to-assignee confirmation -> release seller price -> collect R`

This is stronger than buying an ordinary bank creditor claim before distribution because insolvency recovery risk must already have been converted into a fixed segregated cash amount.

## Comparison with H101/H103
### Versus H101 ordinary enforcement-service deposit proceeds
H101 already has cash in the enforcement-service deposit account plus explicit claimant substitution under Article 31. H106 has an even stronger **final-court-schedule + Central Bank special-account segregation** state, but does not yet have an equally explicit operator workflow saying that a civil assignee of an Article-87.4 payment is automatically substituted in the bank-liquidation file.

### Versus H103 enforcement-advance refund
H103 has explicit Article-31 assignment succession in the same enforcement proceeding and a statutory refund trigger. H106 potentially has cleaner cash finality after Article-87.4 segregation, but specific assignee recognition remains the missing bridge.

Therefore H106 is one of the strongest deterministic-cash leads, not yet superior enough to close H101/H103.

## Live-market screen
Fresh searches on 2026-08-19 found:
- a live ADIF liquidation infrastructure and multiple banks still listed in liquidation;
- public evidence of creditor payments and liquidation creditor processes;
- no public listing located for a **specific Article-87.4 already-segregated creditor payout right offered below face value**;
- no public ADIF/CBA procedure located that expressly states how a post-schedule civil assignee updates the payout recipient for an already-segregated Article-87.4 amount.

A live instance therefore remains the main economic blocker, while formal assignee-recognition is the main legal/operational blocker.

## Why this is not SUCCESS yet
The mechanism has all the ingredients of a deterministic arbitrage except two execution facts that cannot be assumed:
1. a real current seller willing to transfer a confirmed, already-funded payout right for `P < R - all costs/reserves`;
2. written pre-payment recognition by the liquidation authority that the assignee will receive the segregated amount.

Without both, the project cannot claim guaranteed profit.

## Next test
Search directly for creditors of banks in liquidation whose payout is already on a final schedule but remains unclaimed/undelivered, and test whether ADIF/liquidator will process a Civil-Code assignment as successor substitution before purchase-price release.

Best target is an old creditor who values immediate liquidity/convenience and has a payment already segregated at the Central Bank, not an unresolved ordinary bankruptcy claim.
