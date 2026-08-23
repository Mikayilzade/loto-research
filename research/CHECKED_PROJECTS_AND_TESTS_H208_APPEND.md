# H208 audit append — RI retail/SSVM strict execution

Updated: 2026-08-23
Scope: LOTTERY ONLY.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H208 RI retailer/SSVM Keno execution** | ask whether physical terminal/SSVM can force complete same-draw acquisition of H173/H175 | current $150 ordinary Keno ticket cap implies at least **29 tickets** for 4,336 $1 plays and **31 tickets** for 4,560 $1 plays even under maximally favorable packing | exact lower bound; `research/h208_ri_retail_ssvm_strict_execution_failure.md` |
| **H208 terminal-failure branch** | require successful issuance of every prescribed physical ticket before one 4-minute Keno draw | official Retailer FAQ explicitly contemplates terminal jams/misprints; Keno misprints should be voided before draw and credit may be discretionary | **STRICT EXECUTION GUARANTEE FAILS** |
| **H208 QR/SSVM route** | use app-generated QR selections at retailer terminal or SSVM | physical QR purchase path is real, but no recovered rule provides atomic all-or-none issuance for thousands of selections | **PRACTICAL CHANNEL REAL; STRICT ATOMICITY NOT ESTABLISHED** |
| **H208 current physical channel conclusion** | combine minimum multi-ticket requirement + recognized terminal-failure branch + four-minute draw cadence | at least one required issuance can fail/misprint without a guaranteed successful correction before target draw | **CLOSED as sole strict-guarantee execution channel** |

Conclusion: current RI iLottery (H207) and ordinary retail/SSVM (H208) both fail as sole strict execution channels for H173/H175. Continue current Keno-promotion recovery and H175 mathematics; reopen physical execution only on evidence of an operator-backed atomic/bulk facility or materially different rules.