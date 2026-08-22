# H169 audit append

Updated: 2026-08-22

| ID | Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|---|
| H169 | NC Pick 3 forced Double Draw + retailer discount | Cross-terminal / support rollback after selling-terminal failure | Public NCEL materials tie Pick 3 cancellation to the producing/selling terminal; retailer support exists but no published guarantee of central/cross-terminal cancellation before draw break was found | **STRICT ATOMIC ROLLBACK NOT PROVEN; adverse partial-basket branch remains**; `research/h169_nc_pick3_atomicity_liability_limit_closure.md` |
| H169 | NC Pick 3 forced Double Draw + retailer discount | Liability-limit acceptance risk | Current NCEL FAQ/rules state Pick 3 combinations can sell out and further wagers can be refused when liability thresholds are reached | **VALIDATED independent acceptance-failure branch** |
| H169 | NC Pick 3 deterministic Pair cover | Complete-basket pre-reservation/all-or-none order | No public mechanism found to reserve/accept all 100 required Front Pair selections before any ticket becomes live | **NOT FOUND; strict ex-ante guarantee rejected under current public rules** |
| H169 | NC Pick 3 rollback | Touch-vending/session refund rules | Limited payment/session refunds do not create an all-or-none Pick 3 basket guarantee | **REJECTED as atomicity solution** |
| H169 | NC Pick 3 conditional overlay | $50 Pair cover on officially forced two-draw state with retailer discount | Complete accepted basket still guarantees $50 gross from $50 face and discount creates conditional surplus | **CONDITIONAL OVERLAY PRESERVED; reopen only on materially new atomic/reservation evidence** |
