# H245 — UK Lotto two-round full-space closure

Date: 2026-08-24
Status: REJECTED FOR STRICT GUARANTEE
Scope: LOTTERY ONLY

## Current mechanism
Since June 2026, each £2 UK Lotto line is entered into two separate 6/59 rounds on the same draw night. The jackpot is shared across both rounds, while non-jackpot prize tiers are fixed and paid per round. Current published prizes are £1,000,000 for 5+Bonus, £1,000 for Match 5, £50 for Match 4, £10 for Match 3 and £1 for Match 2.

## Exact full-space identity
Buying every 6-number subset requires C(59,6)=45,057,474 lines, costing £90,114,948.

For either round, a complete 6/59 cover produces deterministically:
- Match 6: 1
- Match 5 + Bonus: 6
- Match 5: 312
- Match 4: 20,670
- Match 3: 468,520
- Match 2: 4,392,375

Excluding the jackpot, fixed cash per round is:

6*£1,000,000 + 312*£1,000 + 20,670*£50 + 468,520*£10 + 4,392,375*£1 = £16,423,075.

Because the same full-space ticket set is entered in both rounds for the same £90,114,948 spend, two-round deterministic non-jackpot cash is £32,846,150, equal to 36.4491693431% of cost. The fixed-prize deficit is £57,268,798 before execution costs.

## Jackpot and Must-Be-Won gate
Full coverage necessarily contains the winning Match-6 line in Round 1 and again in Round 2. Therefore a Must-Be-Won draw cannot enter the no-jackpot-winner rolldown branch: our own construction guarantees jackpot winners exist.

The jackpot is shared across both rounds and with external Match-6 winners. With no useful pre-draw hard cap on external jackpot-winning tickets, the amount attributable to our two jackpot-winning lines is not bounded below strongly enough to bridge the £57.27m fixed-prize deficit in all allowed outcomes. Thus a large advertised jackpot can create favorable expected-value states but not a strict guaranteed-profit full-space theorem.

## Verdict
REJECTED FOR STRICT GUARANTEE. The new two-round format is a genuine nonlinear improvement because one £2 line participates twice, but exhaustive 6/59 coverage still has only a 36.4492% deterministic fixed-prize floor. Full coverage also self-defeats the Must-Be-Won rolldown condition by guaranteeing a Match-6 winner in each round, while external jackpot sharing prevents a strict jackpot floor.

## Reopen rule
Reopen only if rules introduce a deterministic external subsidy/discount above the uncovered deficit, a hard cap on external jackpot sharing that creates a positive worst-case floor, or a materially different Must-Be-Won allocation rule compatible with owning full coverage.

## Sources
- Allwyn, 14 Apr 2026: https://www.allwyn.co.uk/insights/two-huge-new-national-lottery-games-launching-this-summer-to-create-hundreds-more-millionaires-offer-the-worlds-biggest-jackpots
- Allwyn, 17 Jun 2026: https://www.allwyn.co.uk/insights/double-your-luck-delivers-new-lotto-creates-three-millionaires-in-first-weekend-and-over-3-1-million-winners-in-opening-draws
- UK Gambling Commission current Lotto licence page: https://www.gamblingcommission.gov.uk/public-and-players/guide/page/lotto
- Current-format prize comparison reference: https://www.national-lottery.com/news/changes-to-lotto-on-the-way-twice-as-many-chances-to-win
