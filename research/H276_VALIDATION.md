# H276 VALIDATION — UK Thunderball fixed-prize bound

Validated: 2026-08-25
Result: **REJECTED / CLOSED for strict guaranteed-profit nonnegative portfolios under checked rules**

## Independent arithmetic checks
- `C(39,5) = 575,757` main selections.
- Multiplying by 14 Thunderball choices gives **8,060,598** legal lines.
- Exact tier multiplicities for a fixed draw sum back to **8,060,598**.
- Exact fixed-prize gross over one complete one-copy cover is **£4,262,568**.
- Cost at £1 per line is **£8,060,598**.
- Deficit is **£3,798,030**.
- Return ratio is **0.5288153558830251 = 52.8815355883%**.

## Tier audit
- 5+TB: 1 × £500,000 = £500,000
- 5: 13 × £5,000 = £65,000
- 4+TB: 170 × £250 = £42,500
- 4: 2,210 × £100 = £221,000
- 3+TB: 5,610 × £20 = £112,200
- 3: 72,930 × £10 = £729,300
- 2+TB: 59,840 × £10 = £598,400
- 1+TB: 231,880 × £5 = £1,159,400
- 0+TB: 278,256 × £3 = £834,768
- all other match classes: £0
- total: **£4,262,568**

## Portfolio-wide proof check
The draw action is transitive on legal lines: every chosen 5/39 + 1/14 line has the same payoff distribution over the complete outcome universe. Hence every primitive line has average return 52.8815355883% of stake. A nonnegative linear combination of such lines has the same average return ratio. Since minimum payoff cannot exceed average payoff, an everywhere-positive profit would imply average gross > cost, contradicting the exact ratio < 1.

This certificate therefore closes not merely the complete-cover construction but **all nonnegative portfolios of ordinary Thunderball lines** under the checked paytable.

## Source checks
Official National Lottery pages checked for current £1 price, 5/39 + 1/14 matrix, £500k top prize, and the fixed prize schedule. A 2026 official result page was also checked to guard against stale historical rules.
