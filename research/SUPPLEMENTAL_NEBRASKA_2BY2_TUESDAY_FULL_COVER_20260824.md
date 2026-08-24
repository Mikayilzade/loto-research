# Supplemental — Nebraska 2by2 Tuesday deterministic 2X full-cover screen (2026-08-24)

This check is intentionally unnumbered because the global numbered lottery stream advances independently.

## Current official mechanics
Nebraska Lottery current 2by2 page:
https://nelottery.com/homeapp/lotto/34/gamedetail

Current Nebraska regulations (effective 2026-02-22):
https://nelottery.com/media/regulations/Nebraska%20Lottery%20Regulations%20Effective%202.22.26.pdf

The game is 2 red numbers from 1–26 plus 2 white numbers from 1–26. Each play costs $1 and drawings occur daily.

**2by2 Tuesday** is genuinely deterministic: if a ticket is purchased for 7, 14, 21, ... consecutive multi-draws, every prize won on Tuesday automatically doubles. A multi-draw count not divisible by 7 is ineligible. Therefore the minimum acquisition unit for the free 2X feature is **seven paid draws**.

Current ordinary / Tuesday prizes:
- 2 red + 2 white: $22,000 / $44,000;
- 2 red + 1 white: $100 / $200;
- 1 red + 2 white: $100 / $200;
- 2 red only: $3 / $6;
- 2 white only: $3 / $6;
- 1 red + 1 white: $3 / $6;
- 1 red only: one free $1 Quick Pick / two on Tuesday;
- 1 white only: one free $1 Quick Pick / two on Tuesday.

The official page also caps grand-prize liability at $220,000 on ordinary days and $440,000 Tuesday; above ten grand-prize winners the grand prize becomes pari-mutuel.

## Exact full-cover counts
The line space is
`C(26,2)^2 = 325^2 = 105,625`.

Against any fixed draw, the number of selected two-number pairs sharing 2/1/0 winning numbers is respectively:
- 2 matches: 1;
- 1 match: `2*24 = 48`;
- 0 matches: `C(24,2) = 276`.

Taking the red × white product gives deterministic full-cover category counts:
- (2,2): 1;
- (2,1): 48;
- (1,2): 48;
- (2,0): 276;
- (0,2): 276;
- (1,1): 2,304;
- (1,0): 13,248;
- (0,1): 13,248;
- (0,0): 76,176.

Total = 105,625 exactly.

## Strict cash floor for the required seven-draw package
Exclude the grand prize from the strict floor because external duplicate grand-prize tickets can trigger the published pari-mutuel liability rule and no hard pre-draw bound on external multiplicity is available. Also give free Quick Picks **zero strict cash value** because their numbers are uncontrolled and they can all lose or duplicate one another.

Fixed cash from one ordinary full cover is therefore:
- 96 three-of-four tickets × $100 = $9,600;
- `(276+276+2,304)=2,856` two-of-four tickets × $3 = $8,568;
- total = **$18,168**.

Tuesday doubles that fixed cash to **$36,336**.

Minimum qualifying seven-draw purchase:
- cost: `7 × 105,625 × $1 = $739,375`;
- guaranteed fixed cash: `6 × $18,168 + $36,336 = $145,344`;
- strict fixed-cash return: **19.6577%**;
- strict deficit before friction/tax: **-$594,031**.

## Deliberately generous upper bounds
Even if the portfolio were credited with the full nominal $22,000 grand prize on every ordinary draw and $44,000 Tuesday (ignoring the published pari-mutuel dilution risk), seven-draw cash becomes only **$321,344 = 43.4616%** of cost.

The portfolio also deterministically generates 26,496 free Quick Pick awards on an ordinary full cover and 52,992 on Tuesday. If every uncontrolled free Quick Pick is incorrectly valued at its full $1 retail face value, add $211,968 across the seven-draw package. Even this impossible-perfect face-value accounting gives only:

`($321,344 + $211,968) / $739,375 = 72.1301%`.

Thus the promotion remains far below break-even under an upper bound substantially stronger than the real strict-cash model.

## Result
**NO SUCCESS.** 2by2 Tuesday is a rare current deterministic 100% prize boost, but its mandatory seven-consecutive-draw qualification dilutes the effective benefit too strongly. It is rejected even after granting full nominal grand prizes and full face value to random free-play prizes.

Reopen only if Nebraska changes eligibility so that the Tuesday 2X can be obtained without paying for the other six draws, or adds a separate deterministic subsidy large enough to cover the remaining gap.
