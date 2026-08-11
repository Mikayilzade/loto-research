# UK Lotto — 2026 two-round regime

Updated: 2026-08-11
Status: **current rule regime identified; exact primary lower-tier rules document still to capture**

## Rule-version boundary
Allwyn, operator of The National Lottery, announced the largest Lotto format change since launch. Tickets for the new format went on sale on 7 June 2026 and the first two-round draw took place on Wednesday 10 June 2026.

Primary operator sources:
- https://www.allwyn.co.uk/insights/double-your-luck-new-lotto-gives-players-two-chances-to-win-more-than-double-the-number-of-millionaires-expected-to-be-made
- https://www.allwyn.co.uk/insights/allwyn-readies-retailers-for-new-lotto-rollout-ahead-of-tickets-going-on-sale-on-sunday
- https://www.allwyn.co.uk/insights/two-huge-new-national-lottery-games-launching-this-summer-to-create-hundreds-more-millionaires-offer-the-worlds-biggest-jackpots

Key confirmed mechanics from Allwyn:
- one Lotto line still costs £2;
- player still selects 6 numbers from 59;
- every purchased line is automatically entered into two separate rounds on the same draw night;
- two independent sets of six main numbers plus a Bonus Ball are drawn using two separate draw machines;
- a ticket can win in Round 1, Round 2, or both;
- jackpot begins at £2m and can roll up to five times before a Must Be Won event on the sixth draw;
- the jackpot is shared across both rounds;
- lower prize tiers are fixed cash prizes paid per round;
- Match 5 + Bonus remains £1m;
- Allwyn states overall odds of any prize improve from roughly 1-in-9.3 to 1-in-4.9.

Allwyn explicitly stated that the final old-format draw on 6 June 2026 was a £12m Must Be Won draw and that prizes for pre-change tickets continue to be paid under the old prize tiers. This creates a clean rules boundary for data analysis.

## Exact probability check
The underlying one-round 6/59 category probabilities do not change. With two independent rounds, a £2 ticket has probability

`1 - (1 - P(any prize in one round))^2`

of winning at least one prize across the night.

Using the exact 6/59 combinatorics including Match 6 gives:

- probability any prize across two rounds: **0.204956584524**;
- approximate odds: **1 in 4.879082086**.

This independently reproduces Allwyn's rounded public claim of approximately 1 in 4.9.

## Observed current lower-tier schedule
The exact updated lower-tier amounts have not yet been captured from a primary National Lottery rules/procedures document because the public indexed procedures still expose the pre-June-2026 edition. Contemporary independent result archives consistently show the current regular per-round cash schedule as:

- Match 5 + Bonus: £1,000,000 (also confirmed directly by Allwyn);
- Match 5: £1,000;
- Match 4: £50;
- Match 3: £10;
- Match 2: £1.

Example current archive:
https://www.lotterystats.co.uk/lotto/results

These lower-tier values are therefore used as **observed secondary-source parameters**, not hard-coded as permanent official constants in the probability library. `two_round_fixed_cash_ev()` accepts the values explicitly.

With that observed schedule, excluding the shared jackpot:

**gross fixed cash EV = £0.728983386863 per £2 ticket.**

So the format doubles the number of rounds but also lowers the non-millionaire fixed prizes. The ordinary fixed-cash layer remains strongly negative on its own.

## Current Must Be Won case: 18 July 2026
Secondary historical result archive:
https://www.lottery.co.uk/lotto/results-18-07-2026

Published state:
- advertised jackpot: **£9,559,451**;
- no Match 6 winner in either round -> rolldown;
- Match 5 + Bonus: no winners;
- Match 5: 87 total round-winners, £1,000 each;
- Match 4: 6,932 total round-winners, £50 each;
- Match 3: 169,438 total round-winners, rolldown prize £24 each;
- Match 2: 1,756,390 total round-winners, rolldown prize £5 each;
- total published prize fund: £13,282,062.

### Post-draw schedule diagnostic
Using exact one-round category probabilities, two rounds per ticket, and the realized no-jackpot payouts above:

**gross EV for a uniform fixed line ≈ £1.533679184945 per £2 ticket.**

This specific rolldown was therefore still negative under the realized payout schedule.

### Approximate ticket sales
Because the archive reports Match-2 winners separately by round, a method-of-moments estimate is:

`N_hat = total Match-2 round-wins / (2 * P(Match2 in one round))`

Using 1,756,390 Match-2 round-wins:

**N_hat ≈ 9,008,623 purchased lines.**

This is an estimate, not an official sales count. It can be distorted by sampling noise and non-uniform player selections.

### Crowd-average break-even benchmark
Using the observed regular fixed-prize cash baseline of £0.728983386863, a forced-redistribution crowd-average benchmark reaches the £2 ticket cost when:

`J / N >= 2 - 0.728983386863 = £1.271016613137 per sold ticket.`

At the estimated July 18 crowd size this corresponds to a jackpot of roughly:

**£11.4501m.**

The actual advertised jackpot was £9.559451m, around **£1.89m below** this simple crowd-average threshold.

Important: this J/N benchmark assumes the jackpot amount is the relevant distributable overlay and abstracts from detailed current rolldown allocation/capping rules. The realized payout-schedule diagnostic (£1.5337) is the stronger post-draw evidence that this particular event was not +EV.

## Strategic implication
The 2026 redesign moves the current game somewhat closer to the structural-edge zone than the old fixed-cash schedule because one £2 line receives two rounds. But a Must Be Won label still does not imply positive EV. The critical state variable remains:

**overlay / final ticket volume**, adjusted for category sharing and exact current rolldown rules.

The main research opportunity is therefore predictive rather than retrospective: estimate final sales before the sales cutoff from the observable jackpot, day, rollover count and promotion state; then place a conservative lower confidence bound on J/N.

## Research blockers / next work
1. Capture the official 2026 Lotto Online/Retail Game Procedures or player leaflet showing exact new lower-tier prizes and current Must Be Won allocation rules.
2. Build a 2026 draw dataset with jackpot, round-level winner counts and payouts.
3. Estimate final ticket sales from multiple high-frequency categories and reconcile against any official sales figures.
4. Fit sales response as a function of jackpot and draw state.
5. Calculate pre-draw lower-confidence-bound EV, not hindsight EV.
6. Quantify number-popularity/collision effects under the two-round shared jackpot and rolldown categories.
