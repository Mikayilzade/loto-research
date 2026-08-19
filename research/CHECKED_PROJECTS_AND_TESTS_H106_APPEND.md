# CHECKED_PROJECTS_AND_TESTS — H106 append

Updated: 2026-08-19
Terminal state after this packet: **NO SUCCESS; NOT EXHAUSTED**.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H106 Azerbaijan bank-liquidation prefunded payout claim** | creditor claim already in a court-approved Article-87 payment schedule | schedule is final and non-appealable; liquidator must execute it | **VALIDATED deterministic maturity gate**; `research/h106_bank_liquidation_prefunded_payout_claim_assignment.md` |
| **H106 Article-87.4 segregated cash** | scheduled payment cannot be delivered to creditor | unpaid amount is deposited in a special Central Bank account and may be claimed until limitation expires | **VALIDATED prefunded/segregated-cash mechanism**; same note |
| **H106 successor route** | assign already-funded creditor payout to a new holder | Civil Code 193–196 permits assignment and expressly carries insolvency priority; Constitutional Court recognizes claim assignment as singular legal succession; Article 87.4 pays creditor or `hüquq varisi` | **STRONG LEGAL BRIDGE, but bank-liquidation assignee-recognition workflow not yet explicit** |
| **H106 terminal arbitrage** | buy Article-87.4 already-segregated payout below confirmed face and redirect payout before seller payment | no live below-face funded claim located; no written ADIF/CBA pre-payment assignee-redirection procedure located | **PROMISING / EXECUTION-GATED / NOT SUCCESS** |

## Permanent gate
Do not reopen ordinary unresolved failed-bank creditor claims as H106. The only relevant H106 target is:

`final court-approved payout amount + cash already segregated at CBA + transferable/right-successor recognition lockable before purchase + price below net payout`.

If any of those are missing, it remains insolvency speculation rather than a guaranteed-cash arbitrage.
