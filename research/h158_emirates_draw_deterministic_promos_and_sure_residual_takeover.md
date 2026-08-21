# H158 — Emirates Draw deterministic cart promotions + SURE residual-takeover screen

Updated: 2026-08-21
Status: **CURRENT DETERMINISTIC PROMO CLASS VALIDATED / CURRENT EASY6 & SURE TAKEOVER GUARANTEE REJECTED / NOT SUCCESS**

## Why this packet
H157 established that the highest-value promotion architecture is a subsidy attached deterministically to the player's own purchase rather than a random/Nth-ticket award. Emirates Draw currently provides exactly that architecture through cart-level discounts/free-ticket bundles, so this packet tests whether the live subsidy is large enough to invert a compact lottery cover. It also tests a superficially stronger live opportunity in the SURE fixed-ticket raffles, where the cost of all currently unsold tickets is below the advertised prize pool.

## Current primary/operator sources
- Current Emirates Draw games / homepage: https://emiratesdraw.com/
- EASY6 current game page: https://emiratesdraw.com/games/easy6
- Current Onam EASY6 promotion, published 2026-08-16 and valid through 2026-08-30: https://emiratesdraw.com/news/celebrate-onam-with-easy6
- Recent EASY6 Flash Sale, published 2026-08-06, buy 6 get 3 free: https://emiratesdraw.com/news/easy6-flash-sale
- Emirates Draw terms and conditions: https://emiratesdraw.com/terms-and-conditions
- Emirates Draw responsible-play / transaction-limit page: https://emiratesdraw.com/responsible-play
- Current SURE raffle pages/homepage: https://emiratesdraw.com/
- SURE launch / fixed-ticket mechanics: https://emiratesdraw.com/news/emirates-draw-launches-sure-raffles

## A. Current EASY6 30% deterministic cart discount
The current Onam promotion states that during the promotion period a player adds five EASY6 entries and receives an **automatic 30% discount**, reducing the package from USD 30 to USD 21. It may be used multiple times during the promotion and does not rely on a random message or statewide Nth purchase.

This is structurally the player-owned deterministic subsidy sought after H157.

### Exact full-cover calculation
EASY6 is 6-of-39, USD 6 per entry. Buying every combination requires

`C(39,6) = 3,262,623` entries.

Face cost:

`3,262,623 * $6 = $19,575,738`.

For any realized set of 6 winning numbers, a complete cover contains exactly:
- 1 ticket matching 6;
- 198 matching 5;
- 7,920 matching 4;
- 109,120 matching 3.

Current advertised prize table:
- Match 6: USD 4,000,000, shared;
- Match 5: USD 25,000, shared;
- Match 4: USD 4,000, shared;
- Match 3: USD 1 fixed.

To make the screen maximally favorable to the strategy, assign our complete cover the **entire advertised shared amount** at Match 6/5/4, ignoring all external dilution. Then favorable gross is only:

`4,000,000 + 25,000 + 4,000 + 109,120 = $4,138,120`.

At current 30% discount:

`discounted cost = $19,575,738 * 0.70 = $13,703,016.60`.

Favorable full-cover ratio:

`$4,138,120 / $13,703,016.60 = 30.198606%`.

Therefore even the live deterministic 30% discount is nowhere near a guaranteed-profit threshold. External winners can only reduce the shared tiers further.

### Recent stronger buy-6-get-3-free screen
The August 6 Flash Sale advertised buy 6 EASY6 entries and get 3 free, equivalent to paying for 6 of each 9 entries, i.e. **33.3333% effective face discount** if repeated at full scale.

Even granting that stronger recent offer across a hypothetical complete cover:

`effective cost = $19,575,738 * 2/3 = $13,050,492`.

Favorable return:

`$4,138,120 / $13,050,492 = 31.708536%`.

Thus current/recent EASY6 deterministic cart subsidies are decisively below the full-cover break-even requirement.

## B. Current SURE raffles — the misleading `remaining cost < prize pool` state
A fresh 2026-08-21 homepage snapshot showed approximately:

| Raffle | Total ticket pool | Tickets left | Price | Advertised prize board | Cost to buy every remaining ticket |
|---|---:|---:|---:|---:|---:|
| SURE1 | 5,000 | 2,623 | $10 | $30,000 | $26,230 |
| SURE2 | 5,000 | 2,666 | $15 | $50,000 | $39,990 |
| SURE3 | 20,000 | 7,857 | $30 | $360,000 | $235,710 |

Nominally this looks extraordinary: in all three cases the total advertised prize pool exceeds the cash needed to purchase every currently unsold ticket.

However, this is **not** a residual-inventory takeover in the H129 sense, because previously sold tickets remain eligible in the draw.

Already sold external tickets in the snapshot are:
- SURE1: `5,000 - 2,623 = 2,377` external tickets;
- SURE2: `5,000 - 2,666 = 2,334` external tickets;
- SURE3: `20,000 - 7,857 = 12,143` external tickets.

SURE1 and SURE2 each have a one-winner top board in the current product family. SURE3 has five winning slots (one USD 300k plus four USD 15k). In every case the number of already-sold external tickets is greater than or equal to the number of winning slots.

Therefore a legal draw outcome exists in which **all winning positions belong to already-sold external tickets**. If we bought every remaining ticket, our strict worst-case payout would still be **$0**.

So:

`strict takeover floor = $0 - remaining-ticket cost < 0`.

The apparent positive nominal margins (`$3,770`, `$10,010`, `$124,290`) are not guarantees because they incorrectly assign the entire prize board to the residual buyer.

As a sanity check, the random-draw expected share from buying all remaining tickets simply scales with ownership fraction. Before tax/costs the corresponding prize-pool-only expected returns are approximately:
- SURE1: 60%;
- SURE2: 66.6667%;
- SURE3: 60%.

That confirms the visual `remaining cost < prize pool` state is not an arbitrage.

## C. Execution architecture — useful but not sufficient
Emirates Draw terms are nevertheless operationally interesting:
- an order becomes accepted after Order Confirmation;
- the operator may reject an order, but rejected-order payment is refunded under the terms;
- Responsible Play material states a 10,000-ticket per-order limit.

This is closer to a safe checkout architecture than H136 Kentucky, where external funds could become nonwithdrawable before complete-cover acceptance was locked.

But it cannot cure the SURE problem: even an atomic purchase of all remaining tickets cannot remove already-sold external tickets from the draw. For EASY6, it also cannot cure the enormous payout deficit.

## General theorem reinforced
For a fixed-ticket raffle with `T` total tickets, `R` remaining tickets, and `W` winning positions:

- buying all `R` remaining tickets guarantees at least one prize **only if** the number of already sold external tickets `T-R < W` (or if prize assignment has another structural constraint forcing a residual ticket to win);
- if `T-R >= W`, there exists an outcome where every winner is external, so the residual buyer's strict cash-prize floor is zero.

This should be applied before comparing `R * ticket_price` to headline prize-pool value.

## Result
- **Current Onam EASY6 30% discount: VALIDATED deterministic/player-owned, but full-cover favorable ratio only 30.20%; REJECTED.**
- **Recent buy-6-get-3-free EASY6: stronger 33.33% subsidy, but favorable full-cover ratio only 31.71%; REJECTED.**
- **Current SURE1/SURE2/SURE3 residual buyout: headline remaining-cost/prize-pool inversion is real, but strict payout floor remains $0 because previously sold external tickets can occupy all winner slots; REJECTED as guarantee.**
- **Terminal state remains NO SUCCESS; NOT EXHAUSTED.**

## Next research
1. Keep the Emirates cart-level promo architecture on the monitor, but prioritize products whose deterministic cover ratio is already >67–75%; EASY6 cannot be rescued by ordinary 30–50% discounts.
2. Search raffles where the residual unsold inventory is so dominant that `external sold < number of winning slots`; only then can a buy-all-remaining theorem force at least one prize.
3. Search fixed-board raffles with many guaranteed winners and observable live remaining inventory, applying H129/H158 worst-case winner-slot allocation before EV arithmetic.
4. Continue scheduled deterministic Keno free-draw bundles/universal boosts from H157, where cover ratios are much closer to break-even.
