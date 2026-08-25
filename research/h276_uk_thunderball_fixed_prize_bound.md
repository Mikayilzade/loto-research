# H276 — UK Thunderball fixed-prize exact portfolio bound

Updated: 2026-08-25
State: **CLOSED / REJECTED for strict guaranteed-profit portfolio under checked rules**

## Why this candidate
Thunderball is unusually clean for strict-guarantee analysis because its published prizes are fixed per winning line rather than share-based. That removes the usual external-duplicate dilution problem and lets us test the full finite outcome space exactly.

Official/current evidence checked:
- National Lottery responsible-play page: Thunderball lines cost **£1**, choose **5 numbers from 1–39** and **1 Thunderball from 1–14**, top prize £500,000: https://www.responsible-play.national-lottery.co.uk/
- National Lottery Thunderball game-procedures page: https://www.national-lottery.co.uk/games/thunderball/game-procedures
- Official prize-breakdown pages show the fixed schedule: Match 5+TB £500,000; Match 5 £5,000; Match 4+TB £250; Match 4 £100; Match 3+TB £20; Match 3 £10; Match 2+TB £10; Match 1+TB £5; Match 0+TB £3. Example official result: https://www.national-lottery.co.uk/results/thunderball/draw-history/prize-breakdown/3801
- A 2026 official result page was also checked to confirm the game remained live in 2026: https://www.national-lottery.co.uk/results/thunderball/draw-history/prize-breakdown/3832

## Exact full-cover calculation
The complete ticket universe has

`C(39,5) * 14 = 8,060,598` lines.

At £1 each, a one-copy full cover costs **£8,060,598**.

For any fixed draw, the number of covered tickets with `k` main-number matches is `C(5,k) C(34,5-k)`. For the Thunderball component, exactly one of the 14 TB choices matches and 13 do not. Applying the fixed paytable to every resulting tier gives total gross **£4,262,568**.

Therefore:
- full-cover cost: **£8,060,598**;
- invariant fixed gross: **£4,262,568**;
- deficit: **£3,798,030**;
- gross return: **52.8815355883%**.

## Stronger theorem: this closes every nonnegative portfolio, not only full cover
Every legal Thunderball line is symmetric under the complete uniform draw universe. Consequently every individual £1 line has the same average gross, equal to the full-cover gross divided by the number of lines:

`£4,262,568 / 8,060,598 = 0.528815355883...` per £1 stake.

For any portfolio made from nonnegative integer or real multiplicities of legal lines, linearity preserves the same average gross/cost ratio: **52.8815355883%**.

For any finite set of legal outcomes,

`minimum outcome gross <= average outcome gross`.

Since the portfolio average is strictly below its cost, at least one legal draw must return less than cost. Thus **no nonnegative Thunderball portfolio can guarantee strict positive profit** under the checked fixed paytable. This is stronger than rejecting one particular cover and is unaffected by other players because the relevant prizes are fixed per winning line.

## Reopen gate
Reopen only if the rules materially change, for example a deterministic subsidy/free extra draw/discount large enough to lift the line-level average above 100%, or a new fixed bonus paid on covered selections.

## Reproducibility
- `src/loto_research/h276_uk_thunderball_fixed_prize_bound.py`
- `data/derived/h276_uk_thunderball_fixed_prize_bound.json`
