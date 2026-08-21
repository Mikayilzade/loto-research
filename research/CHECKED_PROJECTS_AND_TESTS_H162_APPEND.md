# H162 audit-ledger append — NJ Green Ball retailer commission lock

Updated: 2026-08-22
Terminal state after packet: **NO SUCCESS; NOT EXHAUSTED**.

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H162 NJ Pick-3 Green Ball + licensed retailer commission** | forced `k=6` Green Ball state; full 100-outcome Pair cover; apply official Pick-3 §8(b) retailer commission | base forced-state Pair cover = **100%** prize gross; official Pick-3 rules prescribe **5% of gross sales dollars** to retailers and **1.25%** cashing commission on qualifying prizes; conditional economics become **105.00%** with sales commission and **106.25%** if cashing commission also applies | **PROMISING / NOT TERMINAL SUCCESS**. Primary-source commission rule materially strengthens H161, but explicit self-sale commission classification, atomic 10-ticket rollback/acceptance, promo irrevocability, active-cycle and tax gates remain. `research/h162_nj_green_ball_retailer_commission_lock.md`, `src/loto_research/h162_nj_retailer_greenball.py`, `data/derived/h162_nj_greenball_retailer_scenarios.csv` |

## New evidence preserved
- Official Pick-3 rules §8(b): mandatory 5% commission on gross sales dollars; 1.25% cashing commission for qualifying prizes.
- Official Pick-3 rules §8(e): cancelled bets earn no commission, supporting the interpretation that completed uncancelled sales are the commission base.
- N.J.A.C. 17:20-6.1(c): agent remits face value less commissions/bonuses/reimbursements to which entitled.
- Retailer owners are not in the public prohibited-player list; H161's official retailer-owner self-purchase winner example remains relevant.
- Green Ball rules explicitly mention licensed retailers participating, but preserve discretionary retailer disqualification and promotion cancellation/modification.

## Do not repeat without new evidence
Do not repeat generic NJ retailer commission pages. Reopen only with one of:
1. explicit self-purchase/self-sale commission treatment;
2. terminal/batch feature proving whole 100-Pair cover is atomic or fully rollbackable;
3. legal/rule evidence that issued Green Ball tickets retain vested second-draw rights after later promotion cancellation;
4. a new active Green Ball `k=6` state;
5. a stronger forced-trigger promotion with one-ticket/system coverage.