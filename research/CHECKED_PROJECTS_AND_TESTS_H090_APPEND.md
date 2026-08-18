# H090 append — Azerbaijan VAT cashback return-cycle control

Updated: 2026-08-19

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H090 ƏDV geri al circular arbitrage** | buy eligible item, receive VAT cashback, then return item | official rule reduces merchandise refund by cashback already paid, so `cashback + adjusted refund = original purchase price` exactly | **REJECTED BY ACCOUNTING IDENTITY**; `research/h090_vat_cashback_return_cycle.md` |
| **H090 return before cashback** | return purchase before rebate is paid | full purchase amount may be refunded, but cashback is not retained | **ZERO PROFIT BEFORE FRICTION** |

General rule added: for reversible-purchase subsidies, test cancellation/return clawback or offset before treating cashback as independent value.
