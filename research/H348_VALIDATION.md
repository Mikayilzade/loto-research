# H348 VALIDATION

Date: 2026-08-29
State: CLOSED / NOT SUCCESS

## Independent exact checks
For matrix 5/50 + 1/16:
- C(50,5)*16 = 33,900,160 legal boards.
- Exact partition over k=0..5 main matches and PB hit/miss sums to 33,900,160.
- Winning-cell counts: D1 1; D2 15; D3 225; D4 3,375; D5 9,900; D6 148,500; D7 141,900; D8 744,975; D9 1,221,759.
- Main fixed gross: 3,375*2,000 + 9,900*500 + 148,500*100 + 141,900*100 + 744,975*20 + 1,221,759*10 = R67,857,090.
- Main full-cover cost: 33,900,160*R10 = R339,001,600.
- Fixed-tier return = 20.0167465284%.
- XTRA fixed table is half the main fixed table and costs half as much (R5), therefore its fixed-tier return is identically 20.0167465284%.

## Cascade validation
The XTRA cascade requires no Division-1 winner. Any nonempty portfolio contains at least one legal board b; draw outcome b makes that portfolio a Division-1 winner. Hence no nonempty portfolio can guarantee the no-D1 prerequisite across all legal outcomes. Full cover guarantees D1 on every outcome and therefore blocks cascade activation from the player's perspective.

Arithmetic inconclusive: 0.
Closure-relevant inconclusive: 0.
