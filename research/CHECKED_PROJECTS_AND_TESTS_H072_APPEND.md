# CHECKED_PROJECTS_AND_TESTS — H072 append

Updated: 2026-08-18

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H072 Azerbaijan electronic-money redemption** | statutory residual-value right | Article 13.5 requires issuer to return qualifying e-money residual value immediately on holder request; Article 13.8 requires fee-free return if license revoked | **DETERMINISTIC REDEMPTION MECHANISM VALIDATED**; `research/h072_azerbaijan_stored_value_redemption.md` |
| **H072 m10 discounted-balance concept** | acquire transferred m10 balance below face, then redeem | P2P transfers published at 0 fee; wallet-to-card dedicated rates page says free up to 5,000 AZN/month; QR cash-out 0.5%, min 1 AZN | **MECHANICALLY POSITIVE IF `B-P-C>0`, but NOT terminal** because no live lawful discounted source/atomic lock and contract permits blocking for business/unusual/other specified cases |
| H072 m10 100 AZN QR example | buy balance then QR cash-out | fee 1 AZN; nominal strict spread requires acquisition `<99 AZN` before other costs/tax | threshold quantified; `data/derived/h072_azerbaijan_stored_value_screen.csv` |
| H072 m10 500 AZN QR example | buy balance then QR cash-out | fee 2.50 AZN; nominal strict spread requires acquisition `<497.50 AZN` before other costs/tax | threshold quantified |
| **H072 BakıKart unlimited balance** | receive valid anonymous card and redeem balance | current terms permit immediate unlimited-card balance refund; possessor/recipient can become user | **REDEMPTION/TRANSFER-BY-POSSESSION MECHANISM VALIDATED** |
| H072 BakıKart paid secondary acquisition | buy card below balance, redeem | operator terms expressly prohibit card resale | **REJECTED paid-arbitrage route by contract gate** |
| H072 Portmanat | user transfer + cash-out architecture | transfers and Portmanat-card cash-out confirmed; current complete fee/terms + discounted source not recovered | **INCOMPLETE / no executable instance** |

## Strategic update
H072 is a real new deterministic class but **not SUCCESS**. Reopen only with an issuer-permitted discounted acquisition source plus irrevocable/escrow settlement and locked redemption terms. Generic e-money-law searching is now closed.
