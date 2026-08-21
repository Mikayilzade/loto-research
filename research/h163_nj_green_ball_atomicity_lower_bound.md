# H163 — New Jersey Pick-3 Green Ball atomicity lower bound

Updated: 2026-08-22
Status: **NO SUCCESS / ONE-TICKET COMPRESSION REJECTED / 10-TICKET MINIMUM PROVEN**

## Objective
Resolve the highest-value H162 execution question: can the forced Green Ball Pick-3 cover be redesigned with another official Pick-3 bet type so the entire deterministic basket fits on one ticket and therefore avoids the multi-ticket acceptance/rollback risk?

## Primary-source rules used
Current official Pick-3 rules (effective November 14, 2022):
- one Pick-3 Ticket can contain at most **10 Plays**;
- each Play selects a Bet Type;
- available bet types are Straight, Wheel, Box, Pair, plus Straight+Box on one Play;
- Pair bets select Front, Back, or Split Pair and therefore fix two ordered digits while leaving one digit free;
- a Pair winner therefore covers exactly **10** of the 1,000 ordered three-digit outcomes;
- Straight covers 1 outcome;
- 3-way Wheel/Box covers at most 3 permutations;
- 6-way Wheel/Box covers at most 6 permutations;
- the Lottery may refuse further wagers on a number when prize-liability limits are reached;
- a Ticket may only be cancelled at the time of purchase.

Official rules:
- https://www.njlottery.com/content/dam/portal/pdfs/drawgames/pick3/Pick-3_Rules_Fixed_Prizes_APPROVED-06.16.22.pdf

Official retailer page also states ordinary retailers earn 5% on every ticket sold and 1.25% on qualifying prize payouts:
- https://www.njlottery.com/en-us/retailer/becomeretailer/full-service-retailer.html

Official self-purchase precedent preserved from H161/H162:
- NJ Lottery reported that licensed retailer owner Jay Shortway bought a CASH4LIFE ticket for himself at his own retail location.
- https://www.njlottery.com/en-us/newsandevents/newsinput/2023/press-releases/C4L_GrandPrize_042123.html

## Support-size theorem
Pick-3 has exactly 1,000 ordered outcomes, `000` through `999`.

For any single official Play, define its support as the set of draw outcomes on which that Play pays a positive prize.

Maximum support sizes:
- Straight: 1;
- Straight/Box or 3-way Wheel/Box: <=3;
- 6-way Wheel/Box: <=6;
- Pair: 10.

Therefore **no legal single Play has support larger than 10 outcomes**.

For a portfolio of `n` Plays, even with zero overlap between supports, the union of all positive-prize outcomes is at most `10n`.

To guarantee at least one positive-prize Play for every possible Pick-3 outcome requires:

`10n >= 1000`, hence `n >= 100`.

The Pair construction from H161/H162 attains this lower bound exactly: the 100 ordered Front-Pair (or Back-Pair or Split-Pair) wagers partition all 1,000 outcomes into 100 disjoint sets of 10.

Thus the existing 100-Pair cover is not merely convenient; it is **play-count optimal** among the published Pick-3 bet types.

## Ticket-count lower bound
A Pick-3 Ticket can contain at most 10 Plays.

Since at least 100 Plays are required:

`ceil(100 / 10) = 10 tickets`.

Therefore any exact all-outcome Pick-3 coverage portfolio under the current official bet menu requires **at least 10 separate tickets**.

No choice of Straight, Wheel, Box, Pair, or Straight+Box can compress the deterministic cover into one ticket, or fewer than ten tickets.

## Why the second Green Ball draw does not remove this lower bound
At the forced Green Ball state used in H161/H162, an eligible ticket gets a second Pick-3 draw. The strict strategy needs a guaranteed payout floor across all legally possible regular/Green-Ball winning-number realizations.

If a three-digit outcome is outside the support union of the purchased portfolio, a legal branch in which that outcome is drawn leaves the portfolio without the needed payout on that draw. Even under a hypothetical restriction that the second draw could not exactly repeat the first, a 10-Play one-ticket portfolio covers at most 100 outcomes and leaves at least 900 uncovered outcomes, so two uncovered distinct outcomes remain available. Hence the second drawing cannot turn a one-ticket portfolio into a strict all-state cover.

The 100-Pair construction remains the minimum-support exact solution.

## Consequence for H162 atomicity
H162's execution problem is structural:
1. the first accepted ticket can become a valid irreversible wager;
2. at least nine additional tickets are still required;
3. official rules permit liability-based refusal of later wagers;
4. public rules only guarantee cancellation `at the time of purchase`, not a guaranteed rollback of all earlier completed tickets when a later required ticket is refused.

Therefore the strategy still has a legal partial-cover branch unless an official batch transaction, reservation, or multi-ticket rollback right is found.

This packet closes the idea that a smarter choice of Pick-3 bet type can solve atomicity by fitting the full deterministic basket on a single ticket.

## Self-sale evidence update
The public evidentiary chain remains strong but not terminal:
- NJ Lottery says full-service retailers earn 5% on **every ticket sold**;
- Pick-3 game rules make the 5% commission mandatory on gross sales dollars;
- New Jersey statutes permit the licensed `person` to be a corporation/company as well as an individual;
- NJ Lottery has publicly documented a retailer owner purchasing a lottery ticket for himself at his own licensed location.

However, no public accounting/audit sentence found in this packet explicitly states that an owner-personally-purchased ticket at the owner's licensed entity is commission-bearing gross sales. H163 therefore does not upgrade H162 to SUCCESS.

## Result
- 100-Pair cover play-count optimality: **PROVEN**.
- Minimum ticket count under current official rules: **10**.
- One-ticket/system compression route: **REJECTED**.
- Multi-ticket atomicity/rollback gate: **MATERIALLY STRENGTHENED AS STRUCTURAL BLOCKER**.
- Retailer self-sale commission: **PROMISING BUT STILL NOT EXPLICITLY LOCKED**.
- Terminal lottery state: **NO SUCCESS; NOT EXHAUSTED**.

## Next action
1. Search official NJ terminal/retailer manuals or written retailer support material for a true multi-ticket batch transaction/reservation or explicit rollback right covering earlier tickets in the same requested basket.
2. Search for another cumulative-trigger lottery promotion whose forced-state exact coverage fits in **one ticket** or one atomic system transaction.
3. Search jurisdictions with a one-ticket combinatorial/system wager plus mandatory retailer commission, fixed discount, or deterministic free-play subsidy.
4. Monitor future NJ Green Ball cycles; only execution-reopen at forced state if the atomicity and self-sale gates are independently solved.
