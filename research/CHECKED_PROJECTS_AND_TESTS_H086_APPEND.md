# CHECKED_PROJECTS_AND_TESTS — H086 append

Updated: 2026-08-19
Terminal state: **NO SUCCESS; NOT EXHAUSTED**

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H086 Baku tantalum-capacitor acquisition** | current Tap.Az #45905589 nominal 0.20 AZN capacitor listing + Baku tantalum-capacitor buyer rate 174–187 AZN/kg | exact zero-fixed-cost break-even accepted mass only **1.070–1.149 g/unit** at 0.20 AZN ask | **PROMISING / EXECUTION-GATED**; `research/h086_baku_tantalum_capacitor_break_even.md` |
| H086 seller-price validity gate | indexed listing explicitly says tantalum among available capacitor types but does not prove tantalum units themselves are sold at 0.20 AZN or selectable | exact unit price/class remains unbound | **NOT SUCCESS** |
| H086 buyer gate | Baku public price is dynamic/non-binding; exact selected lot still requires buyer-side classification and binding payout before seller payment | no binding exact-lot payout yet | **NOT SUCCESS** |
| H086 bulk fixed-cost sensitivity | `m_avg_g > 1000*(A+F/n)/P`; at A=0.20, P=174, F=2 AZN threshold falls from 2.299 g/unit at n=10 to 1.264 g/unit at n=100 | bulk materially improves deterministic floor if exact units qualify | **VALIDATED algebraically**; `data/derived/h086_tantalum_break_even_mass.csv` |

Next priority: exact K52/K53-marked Azerbaijan seller lot with fixed ask/count/weight, then a binding Baku buyer quote for the same lot before purchase.
