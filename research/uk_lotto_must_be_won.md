# UK Lotto Must Be Won benchmark

Updated: 2026-08-11

## Why this game matters
UK Lotto is a current forced-redistribution comparator for the historical Cash WinFall mechanism. Under the current official procedures retrieved on 2026-08-11, a Lotto entry costs £2, uses 6 numbers from 59, and the jackpot can roll five times. If the fifth rollover draw (the Must Be Won Draw) has no Match 6 winner, Match 2 receives an additional £5 cash plus the normal Lucky Dip and the remaining jackpot is allocated to Match 5 + Bonus (3%), Match 5 (5%), Match 4 (7%) and Match 3 (85%). The official procedures also state that 9.79% of ordinary draw sales is allocated to the jackpot and that, on average, 50% of Lotto sales is available for Lotto prizes, with part of that directed to a reserve fund.

Primary source:
https://www.national-lottery.co.uk/games/lotto/game-procedures

Execution constraint: the official National Lottery site states that online players must be 18+ and physically located in the UK or Isle of Man. This project treats legal/physical availability as a separate execution constraint from mathematical EV.

## Exact probabilities
For one fixed 6-number line:

- Match 6: 1 / 45,057,474
- Match 5 + Bonus: 6 / 45,057,474
- Match 5: 312 / 45,057,474
- Match 4: C(6,4)C(53,2) / C(59,6)
- Match 3: C(6,3)C(53,3) / C(59,6)
- Match 2: C(6,2)C(53,4) / C(59,6) = 0.0974838269895

The ordinary fixed cash tiers, excluding Match 6 and excluding the non-cash Match 2 Lucky Dip, have exact gross EV:

**£0.521453998953 per £2 line.**

## Crowd-average Must Be Won identity
In a Must Be Won draw the jackpot fund J is paid to players in either of two ways:

1. Match 6 exists: jackpot is paid to Match 6 winner(s); or
2. no Match 6 exists: jackpot is redistributed to lower categories.

Therefore, across the sold-entry population, the jackpot-derived aggregate payout is J. If N entries are sold, the simple crowd-average jackpot-derived value is J/N per entry.

This gives a useful benchmark:

`crowd-average gross EV = fixed cash EV + J/N + P(Match2) * value(Lucky Dip)`

This is NOT automatically the EV of a deliberate number-selection strategy. Duplicated/popular combinations can alter an individual entry's expected share of pari-mutuel/rolldown category funds. That difference is now a separate research hypothesis.

### Break-even ratio
Cash-only, setting the Lucky Dip value to zero, break-even requires:

`J/N >= 2 - 0.521453998953 = £1.478546001047 per sold entry.`

If the Lucky Dip is valued at the full £2 face value (an intentionally generous upper bound), break-even requires:

`J/N >= £1.283578347068 per sold entry.`

Thus a large advertised jackpot is not enough by itself; sales surge can destroy the edge.

## Historical 2025 rolldown sample
Secondary archive pages were used for preserved post-draw prize schedules; official procedures remain the authority for mechanics. The sample is stored in `data/historical/uk_lotto_must_be_won_2025.csv`.

### 5 July 2025
Published rolldown schedule:
- Jackpot: £15,000,000; no Match 6 winner
- Match 5 + Bonus: £1,036,946
- Match 5: £4,446
- Match 4: £206
- Match 3: £66
- Match 2: £5 cash + Lucky Dip
- Match 2 winners: 1,522,131

Using the exact Match 2 probability, a simple method-of-moments sales estimate is:

**N ≈ 15,614,190 entries.**

That implies advertised jackpot / estimated entries ≈ **£0.9607 per entry**, well below the cash-only break-even requirement of £1.4785.

For a uniform fixed line evaluated against the published no-jackpot payout schedule:

- cash-only gross EV ≈ **£1.43708**;
- if the Lucky Dip is unrealistically valued at its full £2 retail face value, gross value ≈ **£1.63204**;
- both are below the £2 ticket cost.

A cash-only break-even jackpot at the estimated sales level would have been roughly **£23.09m**, not £15m. Even using the generous £2 Lucky Dip face value, the corresponding threshold is roughly **£20.04m**.

### Other 2025 rolldowns
The same pattern appears in the stored sample. Large jackpots attracted large entry volumes, so the observed rolldowns were still negative under both conservative cash-only and generous face-value diagnostics.

This rejects the naive claim "Must Be Won means positive EV". The correct hypothesis is conditional: a forced redistribution can create +EV only when the accumulated fund is large enough relative to sales and sharing.

## New lead: lower-tier popularity/sharing
The rolldown is not simply a fixed prize table. The jackpot-derived category funds are divided among the actual winners in each category. Player number-selection behaviour can therefore affect conditional payout in Match 3/4/5/5+Bonus, not only Match 6.

This creates a stronger version of the usual jackpot-sharing hypothesis:

- birthdays and common patterns may create excess duplicate/subset collisions;
- unpopular combinations may receive a larger share of a fixed category fund when successful;
- the effect is potentially most economically relevant in Must Be Won draws because 85% of the post-Match-2 residual jackpot is directed to Match 3.

This needs ticket-choice data or a defensible crowd model. Historical winner counts and payout schedules can be used to calibrate the aggregate model, but draw-frequency data alone cannot identify player selection popularity.

## Status
- Cash WinFall: historical +EV mechanism validated.
- UK Lotto Must Be Won: forced redistribution validated, but the tested 2025 rolldown examples are NOT +EV at observed crowd levels.
- Current exploitability: unvalidated.
- Next research target: estimate pre-draw sales response to advertised Must Be Won jackpot and quantify whether anti-popularity number selection can materially improve category sharing.
