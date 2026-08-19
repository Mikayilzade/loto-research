# H093 — Azerbaijan pre-funded assigned-claim arbitrage

Updated: 2026-08-19
Status: **MECHANISM VALIDATED IN LAW / NO LIVE BELOW-FACE CLAIM FOUND / NOT SUCCESS**

## Question
Can a transferable monetary claim be bought below its already-secured cash value, producing a strictly positive worst-case cash floor rather than ordinary credit-risk factoring?

This packet separates two very different classes:

1. **ordinary receivable assignment / factoring** — the buyer acquires a claim but still bears debtor non-payment, defenses and set-off risk;
2. **pre-funded claim** — the underlying money has already been deposited with a notary/court for the creditor, so the remaining task is lawful transfer and collection of a cash amount already placed in custody.

## Primary legal findings

### A. Monetary claims are generally transferable
Azerbaijan Civil Code Articles 194 and 513 allow a creditor to assign a claim to a third party without debtor consent unless the law, contract or nature of the obligation prevents it. Article 196 / 515 transfers associated security rights with the claim. The transfer must respect the form required for the underlying transaction.

Source:
- Central Bank of Azerbaijan, Civil Code: https://www.cbar.az/law-169/civil-code-of-the-republic-of-aerbaijan?language=en

### B. Ordinary assigned debt is NOT a guarantee
The same Code prevents treating generic discounted receivables as terminal arbitrage:
- the debtor may raise defenses against the new creditor that existed against the original creditor (Arts. 199 / 541 and factoring provisions);
- the original creditor is responsible for validity of the assigned claim, but **not for debtor performance** unless the creditor separately warrants it (Art. 521);
- current commercial invoice-discounting products in Azerbaijan therefore remain credit/collection finance, not guaranteed cash conversion.

Current examples:
- Bank Respublika invoice discounting advances up to 90% of receivables, with credit/collateral conditions;
- Expressbank factoring finances up to 80% of invoice value and offers recourse factoring.

Sources:
- https://www.bankrespublika.az/en/senedli-emeliyyatlar/invoys-esasinda-maliyyelesme_803
- https://www.expressbank.az/az/service/faktorinq

Conclusion for ordinary factoring: **REJECTED as guaranteed-profit class without an independent performance guarantee or pre-funding.**

## C. Stronger sub-class: money already deposited for the creditor
Civil Code Article 532 allows a debtor, in specified circumstances, to put money or documentary securities on a notary deposit account for the creditor. Article 533 says the court/notary transfers the deposited property to the creditor.

The Law on Notary materially strengthens this structure:
- Article 74: the notary accepts money/securities from the debtor for transfer to the creditor and, on the creditor's demand, gives the money/securities to the creditor;
- Article 75: money/securities deposited by the debtor may be returned to the debtor **only with the written consent of the beneficiary creditor or by court decision**.

Sources:
- Civil Code: https://www.cbar.az/law-169/civil-code-of-the-republic-of-aerbaijan?language=en
- Notary Chamber explanation: https://www.aznotary.az/az/page/notariat-hereketleri/notariat-hereketleri
- Law on Notary: https://frameworks.e-qanun.az/0/c_f_107.html

This removes ordinary debtor-credit risk **only after** the specific deposit and beneficiary entitlement are independently verified.

## Exact arbitrage condition
Let:
- `F` = independently verified amount already on notary/court deposit for the claim;
- `P` = purchase price paid to the current creditor for assignment;
- `C` = all assignment/notary/bank/tax/collection costs;
- `R` = any amount legally removable/returnable/conditional despite the deposit.

Strict cash floor:

`profit_floor = F - R - P - C`.

Terminal SUCCESS for a specific transaction requires:

`F - R > P + C`

**before** irreversible payment to the seller.

## Required atomic execution gates
A candidate is acceptable only if all are locked before seller payment:

1. exact claim exists and seller owns it;
2. assignment is legally permitted by the underlying contract/law;
3. notary/court independently confirms the exact deposited amount `F`;
4. deposit is payable to the creditor without remaining reciprocal condition under Civil Code 532.4;
5. any debtor-return right is either legally blocked or bounded as `R`;
6. debtor has no surviving set-off/defense capable of reducing the deposited entitlement after assignment;
7. assignment is executed in the required written/notarial/registered form;
8. notary/court acknowledges the transferee as the person entitled to receive the deposit;
9. all fees/tax/banking costs are bounded;
10. only then is seller paid, with `profit_floor > 0`.

## Public-web live-instance screen
Fresh searches were run for Azerbaijan listings/auctions of:
- `tələb hüququ` / debt claims for sale;
- auctioned receivables;
- already-deposited notarial claims;
- discounted payment claims.

No current indexed retail-accessible listing was found that simultaneously disclosed:
- face/deposited value;
- purchase ask below that value;
- proof of assignment right;
- pre-payment notary confirmation of funds and transferee payout.

This absence is **not** a theorem that such transactions never exist. It means the current public-web execution layer is missing.

## Strategic result
H093 identifies a substantially stronger deterministic class than ordinary factoring:

**buy a legally assignable claim only after the corresponding cash is already irrevocably deposited/locked for that claim, at a total cost below the verified deposit.**

If a live instance passes the gates above, the mechanism can in principle satisfy the project's strict guarantee criterion without relying on lottery randomness, debtor solvency, resale demand or market price movement.

Current status: **PROMISING MECHANISM / EXECUTION-GATED / NOT SUCCESS**.

Do not repeat generic factoring searches. Re-open H093 only on a concrete below-face claim, auction lot, settlement receivable or notary-deposit right with documents sufficient for pre-payment verification.
