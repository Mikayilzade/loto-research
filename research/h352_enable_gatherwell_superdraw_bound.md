# H352 — Enable Lottery / Gatherwell Super Draw strict-floor bound

## Candidate
Enable Lottery is a £1 weekly Small Society Lottery administered by Gatherwell. Its current 29 Aug 2026 promotion gives each qualifying weekly ticket one entry into a separate £2,000 Luxury Holiday-or-Cash Super Draw. The promotion is additive to the weekly lottery and explicitly has no per-person entry limit.

This is structurally relevant after H351 because it adds an external promotional prize instead of merely enlarging a shared jackpot.

## Binding mechanics checked
Game rules state that each weekly ticket is unique and the guaranteed weekly winner is selected at random from all eligible tickets, irrespective of the chosen six-digit Game Number. The ordinary prize table advertises a £25,000 jackpot and a guaranteed prize equal to 24% of weekly ticket sales.

The Super Draw rules state that every weekly ticket purchased before the deadline supplies one entry, entries can also come from other participating lotteries, there is no per-person limit, and exactly one winner is selected by RNG from all eligible entries.

Sources:
- https://www.enablelottery.org.uk/game-rules
- https://www.enablelottery.org.uk/

## Exact strict-floor argument
Let N be the number of new £1 weekly tickets bought by the target player. External eligible tickets already exist before this hypothetical purchase.

1. Weekly guaranteed prize: because at least one external eligible weekly ticket exists, there is a legal RNG outcome where that external ticket receives the guaranteed weekly prize. Player floor from this component: £0.
2. Super Draw: because external qualifying entries exist and the draw is over all eligible entries, there is a legal RNG outcome where an external entry receives the single £2,000 prize. Player floor from this component: £0.
3. Six-digit jackpot: for N<1,000,000, even under the favorable interpretation that chosen Game Numbers can be used as a complete six-digit cover, a player with fewer than one million distinct numbers need not cover every six-digit outcome, so a legal non-jackpot outcome remains. For N>=1,000,000, grant the player the full advertised £25,000 jackpot as a guaranteed upper bound.

Therefore a player-favorable upper bound on strict guaranteed cash is

G(N) <= 0, if 0<N<1,000,000;
G(N) <= £25,000, if N>=1,000,000.

Cost C(N)=£N, so

G(N)-C(N) <= -N < 0 for 0<N<1,000,000,
and
G(N)-C(N) <= £25,000-N <= -£975,000 for N>=1,000,000.

This closes every positive integer N without requiring assumptions about sales volume after purchase, duplicate six-digit choices, or expected value.

## Additional execution blocker
The live rules restrict participation to eligible UK/Great Britain residents depending on the component. This is not needed for the mathematical closure above.

## Validation
Boundary points were independently checked at N=1, 267, 999999, 1000000, 1000001 and 2000000. All strict net upper bounds are negative. Arithmetic inconclusive=0; closure-relevant inconclusive=0.
