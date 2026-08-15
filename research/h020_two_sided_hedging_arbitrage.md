# H020 — lawful two-sided hedging / arbitrage

Updated: 2026-08-15
Status: **mechanism validated; no current terminal SUCCESS; structural same-market complete-set subsidy rejected on screened venues**

## Question
Can mutually exclusive outcome positions be locked before resolution so that the minimum net payoff across every legal outcome exceeds total acquisition cost?

This is stronger than positive EV: once every leg is fully matched and settlement definitions align, a true surebet has a deterministic payoff floor.

## Core theorem — complete-set dutching
For exhaustive mutually exclusive outcomes with effective decimal odds `O_i`, choose stakes so each outcome returns the same amount `R`:

`stake_i = R / O_i`.

Total capital is:

`C = R * sum_i(1/O_i)`.

Therefore a strict pre-outcome surebet exists iff:

`sum_i(1/O_i) < 1`

after embedding all commissions, taxes and other unavoidable costs in the effective prices.

For binary token markets whose complete set redeems/merges to exactly `$1`, the equivalent condition is:

`cost(YES) + cost(NO) + all fees/gas < $1`.

The mathematical guarantee begins only **after all legs are actually filled and remain valid under compatible settlement/void rules**.

## 1. Smarkets / bookmaker-exchange arbitrage — mechanism VALIDATED
Smarkets' own help material explicitly describes arbitrage as covering all outcomes at prices that lock a profit and gives back-to-lay examples.

Official sources:
- https://help.smarkets.com/hc/en-gb/articles/115001199231-Back-to-lay-arbitrage-betting-strategy
- https://help.smarkets.com/hc/en-gb/articles/115001175531-How-to-calculate-arbitrage-betting
- https://help.smarkets.com/hc/en-gb/articles/115001555052-How-to-bet-on-a-betting-exchange

Published-style identity with exchange commission `c`:

`lay_stake = back_odds * back_stake / (lay_odds - c)`.

Example reproduced from Smarkets' educational numbers:
- bookmaker back odds 2.20;
- back stake £200;
- exchange lay odds 1.98;
- commission 2%;
- equalizing lay stake ≈ £224.4898;
- profit if backed selection wins = £20;
- profit if it loses = £20.

A second Smarkets example (9.00 back, 8.00 lay, £500 back, 2% commission) reproduces ~£52.63 on either branch.

### What this proves
**Once both wagers are fully accepted at the stated prices and share compatible settlement rules, deterministic positive profit is mathematically real.**

### Why this is not terminal SUCCESS yet
The cited odds are educational examples, not a current executable live quote. Before both legs are confirmed, the user can face:
- price movement / partial fill;
- bookmaker stake limits or rejection;
- exchange liquidity shortfall;
- different void/cancellation/dead-heat rules;
- account/eligibility/geographic restrictions;
- commission/tax differences;
- settlement-source mismatch.

So H020 validates the mechanism class but does not yet provide a reproducible current executable opportunity satisfying the project's strict terminal criterion.

## 2. Kalshi — same-market binary buy-both structural arb REJECTED
Official Kalshi documentation states that each trade pairs opposing participants and the combined Yes/No investment equals `$1` for the binary contract pair. It also states that Kalshi charges transaction fees, with some markets also charging maker fees.

Official sources:
- https://help.kalshi.com/en/articles/13823836-how-are-prices-determined
- https://help.kalshi.com/en/articles/13823805-fees
- https://help.kalshi.com/en/articles/13823828-the-orderbook

Therefore there is no platform-funded structural subsidy from simply buying both sides of the same binary market: the complete set is `$1` before fees and worse after positive fees/spread.

Kalshi's **collateral return** for mutually exclusive/directional groups can reduce locked capital because some positions cannot all lose simultaneously, but it does not increase settlement payout and therefore is not itself a guaranteed-profit subsidy.

Source:
- https://help.kalshi.com/en/articles/13823816-collateral-return

Status: **same-market complete-set arb REJECTED structurally; cross-market pricing discrepancies remain conditional/live-state only.**

## 3. Polymarket — complete-set token theorem VALIDATED, subsidy not structural
Polymarket's current documentation makes the complete-set accounting explicit:
- `$1 pUSD` can be split atomically into `1 Yes + 1 No`;
- equal Yes/No quantities can be merged back into `$1 pUSD` before resolution;
- after resolution, winning tokens redeem for `$1` and losing tokens for `$0`.

Official sources:
- https://docs.polymarket.com/concepts/positions-tokens
- https://docs.polymarket.com/trading/ctf/split
- https://docs.polymarket.com/trading/ctf/merge
- https://docs.polymarket.com/concepts/resolution

Hence if a trader could acquire an equal Yes+No pair for a combined all-in cost below `$1`, merging would create deterministic gross arbitrage. But the split/merge mechanism itself anchors the complete set to `$1`; it does not subsidize it.

Current Polymarket fees are market-dependent and taker fees apply to many categories; makers are documented as fee-free under the current schedule, while intermediaries/builder fees may add costs.

Source:
- https://docs.polymarket.com/trading/fees

### Negative-risk multi-outcome markets
Polymarket's negative-risk adapter allows `1 No` on one mutually-exclusive outcome to convert atomically into `1 Yes` in every other outcome. This is capital-efficient but, like Kalshi collateral return, is an accounting/conversion mechanism rather than a guaranteed payout subsidy.

Source:
- https://docs.polymarket.com/advanced/neg-risk

Status: **complete-set arbitrage condition validated; no structural same-market profit; live crossed-book opportunities require real-time executable screening.**

## 4. Execution theorem / terminal gate
For H020 to qualify as project `SUCCESS`, all of the following must be true simultaneously:
1. positions are exhaustive over every legal settlement branch;
2. each leg is accepted/matched at a known price and quantity;
3. minimum net payout after commissions/taxes/FX/gas exceeds total capital committed;
4. settlement definitions, void/dead-heat/cancellation rules and authoritative source are compatible;
5. no unilateral operator rule can turn one leg void while the hedge leg stands in a loss-making way;
6. account, jurisdiction, stake and withdrawal limits permit execution;
7. the opportunity is current/reproducible, not merely a historical or illustrative quote.

A useful distinction is therefore:
- **post-fill guarantee:** mathematically valid and demonstrated by exchange documentation;
- **pre-trade repeatable guarantee:** not established, because the profitable price pair is itself a transient market state and both legs may not execute atomically across venues.

## Code/data
- `src/loto_research/two_sided_arb.py`
- `tests/test_two_sided_arb.py`
- `data/derived/h020_two_sided_arb_screen.csv`

## Conclusion
H020 is the first still-open class in this phase where a genuine deterministic profit floor is explicitly supported by current operator documentation **after both sides are filled**. However no current live, legally executable, fully matched cross-venue opportunity has been established in this packet, so terminal state remains **NO SUCCESS; NOT EXHAUSTED**.

Next research should prioritize either:
- a public live-data venue pair where executable quotes can be screened atomically enough to verify a current complete-set cost `< guaranteed payout`; or
- another finite/final-draw product with a deterministic external subsidy large enough to overcome full coverage cost.
