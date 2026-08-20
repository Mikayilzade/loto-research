# H128 — Florida Millionaire Raffle 2026 early-ticket cumulative overlay

Updated: 2026-08-20
Status: **STRONG HISTORICAL +EV EARLY-BIRD OVERLAY VALIDATED / STRICT GUARANTEE REJECTED / REUSABLE MONITOR CLASS STRENGTHENED**

## Question
H122 quantified only the last purchase window (fourth interim draw + final draw). Because the official rules keep an early ticket alive for every remaining draw, how much stronger was the economics for tickets bought earlier, and does cumulative eligibility create a guaranteed-profit route?

## Primary-source facts
Florida Lottery Emergency Rule 53ER26-16 states that:
- tickets cost **$20**;
- there are four interim drawings;
- each interim drawing pays a fixed **$704,500** across 2,498 winners;
- a ticket bought before a drawing remains entered in **all remaining drawings**, whether it wins or loses earlier;
- the final drawing pays at least **10 × $1,000,000** while total sales are <=1,000,000.

Official rule:
- https://secondchance.flalottery.com/secondchance/millionaireraffle/rules

Observed final sales from H122: **369,180 tickets**.

Because the interim draw pools are cumulative, the eligible denominator for every earlier interim draw is <= the final denominator. Therefore, using the final denominator for every draw produces a conservative lower bound on the expected value of an early ticket; actual earlier-draw EV can only be higher.

## Cumulative fixed-board ladder
Let `Nf = 369,180` be final sales and `B = 704,500` the fixed board per interim draw.

For a ticket bought early enough to participate in `k` remaining interim draws plus the final 10 × $1m draw, a conservative pre-tax EV lower bound is:

`EV_k >= (10,000,000 + k*704,500) / Nf`.

The corresponding break-even final denominator is:

`N*_k = (10,000,000 + k*704,500) / 20`.

| Purchase timing | Remaining interim draws `k` | Fixed board still eligible | Conservative EV at `Nf=369,180` | Gross return | Pre-tax ROI | Final-sales break-even `N*` |
|---|---:|---:|---:|---:|---:|---:|
| Before draw 1 / March ticket | 4 | $12,818,000 | **$34.7202** | **173.6010%** | **+73.6010%** | **640,900** |
| Before draw 2 | 3 | $12,113,500 | **$32.8119** | **164.0595%** | **+64.0595%** | **605,675** |
| Before draw 3 | 2 | $11,409,000 | **$30.9036** | **154.5181%** | **+54.5181%** | **570,450** |
| Before draw 4 | 1 | $10,704,500 | **$28.9953** | **144.9767%** | **+44.9767%** | **535,225** |

These values are deliberately conservative for the earlier rows because their actual interim denominators were below or equal to 369,180.

## Important structural result
The Florida 2026 architecture had an **early-ticket duration premium** that was not merely promotional language. Each earlier purchase added another fixed $704,500 prize board without increasing the ticket price.

At the observed final denominator, the weakest possible March-ticket EV consistent with the rules was already **$34.72 on a $20 ticket**, or about **+73.6% pre-tax expected ROI**. This is materially stronger than the +44.98% last-window state documented in H122.

The reusable monitor should therefore rank fixed-board raffles by **remaining fixed-board value per eligible ticket**, not just final-draw prize board.

## Why cumulative +EV still does NOT create terminal SUCCESS
The cumulative structure increases expectation, but it does not remove the zero-payout branch for an incomplete portfolio.

For the final draw there are only 10 winning numbers. If more than 10 tickets are already held by external players before a candidate portfolio is purchased, there exists a legal outcome in which all 10 final winners are external. The same logic applies to each interim drawing when the external ticket count is at least 2,498.

Buying additional tickets near the deadline cannot change ownership of already-sold tickets. Therefore an undersubscribed late state can be extremely +EV while still having a strict portfolio floor of zero.

At launch, buying the complete 2,000,000-ticket cap would solve external ownership but costs **$40,000,000**, while the maximum board at sellout is only **$22,818,000**. So complete ownership remains structurally negative.

Thus:
- **expected-value overlay:** strongly validated;
- **early-purchase cumulative overlay:** newly quantified and materially stronger;
- **strict all-outcome guarantee:** rejected.

## Reusable monitor upgrade
For any raffle with cumulative eligibility, define for a ticket bought at time `t`:

`remaining_board(t) = sum of all fixed cash-equivalent boards for draws the ticket will still enter`.

If `N_final` can be bounded, use:

`EV_lower_bound(t) = remaining_board(t) / N_final_upper_bound`.

A candidate is pre-tax +EV whenever:

`N_final_upper_bound < remaining_board(t) / ticket_price`.

This is stronger than evaluating each early-bird/weekly draw in isolation because a single ticket can stack multiple fixed boards.

## Monitoring implication
Future fixed-board raffle screens should capture:
1. cumulative eligibility across future draws;
2. fixed cash-equivalent board remaining at each purchase date;
3. current sold count and any defensible upper bound on final sales;
4. whether a prize won earlier remains eligible later (Florida explicitly did via continuation tickets);
5. tax/claim/travel cost reserve;
6. external-ticket count relative to winner count, to separate +EV from guarantee.

## Conclusion
H128 upgrades Florida Millionaire Raffle 2026 from a +44.98% last-window positive-control to a much stronger **cumulative early-ticket overlay**: a March ticket had a conservative rule-based pre-tax EV floor of about **$34.72 on $20 (+73.6%)** at the observed final denominator. This is a powerful reusable +EV monitor class, but it still cannot satisfy the project's terminal guaranteed-profit condition because external tickets can capture all winning numbers in a legal outcome.
