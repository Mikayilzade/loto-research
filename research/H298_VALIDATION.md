# H298 VALIDATION

Validated: 2026-08-27
Packet: `H298`
Result: **CLOSED for four checked current hard-capped pools; NO SUCCESS globally**

## Independent arithmetic checks

### Chelsea Fire Company Liberty Street
Published cap/cost: 250 x USD 100 = **USD 25,000**.
Published cash schedule:
- 1 x 10,000
- 1 x 2,000
- 2 x 1,000
- 4 x 500
- 10 x 200
- 10 x 150
- 5 x 100

Sum = **USD 20,000** exactly. Ratio = **0.8000000000**; deficit = **USD 5,000**. The five early-bird prizes were scheduled before this validation date, so counting them is conservative in the player's favour.

### PACC St. Jude
500 x USD 10 = **USD 5,000** cost. Published prizes 1,500 + 1,000 + 500 = **USD 3,000**. Ratio = **0.6000000000**; deficit USD 2,000.

### Tour de Cure 100 Club
Cap = 100 entries. Packages `(1,50), (3,120), (6,210)` AUD.
Exact integer search over nonnegative package counts gives minimum exact-100 acquisition:
`16*6 + 1*3 + 1*1 = 100` entries;
`16*210 + 120 + 50 = AUD 3,530`.
Published prizes sum to AUD 1,500. Ratio = **0.42492917847025496**; deficit AUD 2,030.

### Henley Great White
500 x AUD 100 = **AUD 50,000** face acquisition. Published grand-prize cash liability AUD 10,000. Cash-only ratio = **0.2000000000**. Ancillary food/drinks are not treated as withdrawable cash and are not needed for the H298 best-candidate conclusion.

## Cross-check gates
- all four candidate caps are finite and explicitly published by the cited current pages;
- all reported cash liabilities are taken from the cited current pages rather than inferred EV;
- every full-pool cash ratio is strictly below 1;
- strongest ratio = Chelsea Fire at exactly 80%;
- therefore even impossible-perfect ownership of every ticket does not guarantee gross above acquisition cost for any checked candidate.

H225-X* remains independently terminal at X20 and was not modified.
