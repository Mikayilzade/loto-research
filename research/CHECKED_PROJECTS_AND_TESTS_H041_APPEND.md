# CHECKED_PROJECTS_AND_TESTS — H041 append

Updated: 2026-08-16

This append exists because the connector available in this run can replace but cannot safely patch the large master ledger without reconstructing the entire file. It is authoritative for H041 until merged into `research/CHECKED_PROJECTS_AND_TESTS.md` by a later run with a safe patch/checkout path.

| Class / example | Result | Status |
|---|---|---|
| **H041 stake-not-returned free-bet conversion theorem** | after a free token `F` is valid and an exchange lay is fully matched, equal lay `x=F*(O_b-1)/(O_l-c)` locks cash `F*(O_b-1)*(1-c)/(O_l-c)>0` across both settlement outcomes | **MECHANICAL SURE-CASH CONVERSION VALIDATED**; `research/h041_free_bet_matched_conversion.md`, `src/loto_research/free_bet_conversion.py` |
| **H041 current Sky Bet welcome offer** | 3x£10 free-bet tokens after £5 deposit + 5p qualifying bet at 2.00+; 2.00/2.00 with 2% lay commission gives modeled package floor ~£14.84798 after qualifier | **MECHANICAL FLOOR POSITIVE; STRICT GUARANTEE REJECTED** because incorporated Sky general promo terms prohibit no/limited-risk promotion exploitation and permit withholding/clawback |
| **H041 Smarkets matched-betting mechanism** | Smarkets' own current education/help material explicitly describes bookmaker-free-bet + exchange-lay matched betting as covering outcomes and locking profit | **OPERATIONAL MECHANISM VALIDATED**; exchange-side contract is compatible in principle, but bookmaker-side irrevocability remains unresolved |

Next gate: find a current deterministic free-token offer where the bookmaker contract explicitly permits hedging/matched betting or contains no applicable low-risk/arbitrage clawback, plus lawful jurisdiction/access and fully matchable compatible exchange depth.
