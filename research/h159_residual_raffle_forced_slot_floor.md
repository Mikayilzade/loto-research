# H159 — fixed-board raffle residual takeover: forced-slot worst-case floor

Updated: 2026-08-21
Status: **NO SUCCESS / GENERAL SCREENING THEOREM VALIDATED / VIRGINIA 2026 HIGH-WINNER DESIGN CLOSED FOR EVERY SALES STATE**

## Objective
H158 showed that buying every remaining raffle ticket does not guarantee any prize when already-sold external tickets can occupy all winner slots. H159 strengthens that result for the only potentially interesting regime: **external sold `e < W`**, where `W` is the number of guaranteed winning slots.

The goal is to compute the exact strict payout floor rather than compare remaining ticket cost with the headline prize board.

## Exact theorem
Let:
- `T` = total possible raffle tickets;
- `c` = price per ticket;
- `e` = tickets already sold to external players before our takeover;
- `R = T-e` = all remaining tickets purchased by us;
- `W` = fixed number of winning slots;
- prizes sorted ascending `p1 <= p2 <= ... <= pW`.

If we acquire **every remaining ticket**, then:

- if `e >= W`, all winning slots can legally belong to external tickets, so strict buyer payout floor is **0**;
- if `e < W`, at least `W-e` winners must belong to us, but the external tickets can occupy the `e` **largest** prizes. Therefore the exact worst-case buyer payout is

`F(e) = p1 + ... + p_(W-e)`.

Remaining acquisition cost is

`C(e) = c(T-e)`.

Strict pre-tax margin is

`G(e) = F(e) - C(e)`.

A residual takeover can be a strict pre-tax guarantee only if **some observable pre-purchase state `e` has `G(e) > 0`**, before taxes/fees/execution are applied.

This is stronger than the H158 zero-floor test and is the correct first-pass screen for all fixed-board residual buyouts.

## Virginia 2026 Commanders Golden Pass Raffle
Official current Virginia Lottery archive/page:
- https://www.valottery.com/lotteryonline/504008

The official page states:
- ticket price: **$20**;
- top prize: one experiential prize valued at **$950,000**;
- 5 prizes of **$10,000**;
- 500 prizes of **$500**;
- 3,000 prizes of **$100**;
- top-prize odds `1 in 150,000`, implying a fixed pool of **150,000 tickets** for the single top-prize slot;
- the raffle sold out.

For buyer-favorable screening, H159 credits the entire stated $950,000 experiential value as if it were fully cash-equivalent. This overstates, rather than understates, takeover value.

Thus:
- `T = 150,000`;
- `c = $20`;
- `W = 3,506`;
- total face acquisition cost from zero sales = **$3,000,000**;
- entire advertised board value = **$1,550,000**.

### Exact all-sales-state result
The scanner evaluates every `e` from 0 through the point where external tickets can consume all winning slots.

The **best** strict state is actually `e=0`:
- forced payout = entire board = **$1,550,000**;
- acquisition cost = **$3,000,000**;
- strict margin = **-$1,450,000**;
- return = **51.6667%**.

Once even one external ticket exists, it can take the $950,000 top prize. At `e=1`:
- our forced payout collapses to **$600,000**;
- remaining cost = **$2,999,980**;
- strict margin = **-$2,399,980**.

Selected checkpoints are in `data/derived/h159_virginia_residual_raffle_floor.csv`.

Because every prize in this board exceeds the $20 ticket price, replacing one of our tickets by one external ticket saves only $20 of acquisition cost while allowing the adversarial allocation to remove a prize worth at least $100 from our forced payout. Hence after `e=0`, `G(e)` only worsens. The design is therefore mathematically closed for **every possible residual sales state**, not merely the final sold-out state.

## Virginia Capitals Career In A Year control
Official Virginia Lottery page:
- https://www.valottery.com/lotteryonline/504009

The page publishes the same 2026 winner-count structure and prize ladder:
- one $950,000-value experiential prize;
- five $10,000;
- 500 $500;
- 3,000 $100;
- top-prize odds 1 in 150,000.

Therefore the same `T=150,000`, `W=3,506`, `$20`-ticket design family has the same structural residual-takeover failure. This is independent of where in the sales cycle the takeover is attempted.

## Michigan online raffle architecture — future-monitor note
Official Michigan Lottery FAQ:
- https://faq.michiganlottery.com/online-games-information-286703b2/online-raffles-faq-c254e42f/online-raffles-overview-189c4315

Michigan explicitly supports finite online raffles with:
- limited ticket pools;
- fixed ticket cost;
- predetermined prize counts;
- random winner selection from sold tickets;
- **no overall limit on tickets a player may purchase** (250 can be placed in the cart at a time, with repeated cart additions allowed).

This is unusually favorable execution architecture for a future H159 candidate. A fresh August 2026 public search did not surface a current active Michigan raffle with a prize board and live sold/remaining state that passes `G(e)>0`, so no terminal candidate is claimed in this packet.

## Reusable screening consequences
1. `remaining cost < total prize board` is not sufficient.
2. `external sold < W` is only the first gate. It merely forces **some** wins.
3. Exact guarantee requires the sum of the **cheapest forced winning slots**, not average prize value, to exceed remaining acquisition cost.
4. If all prizes are greater than ticket price and `G(0) <= 0`, then `G(e)` strictly decreases for `0 <= e < W`; the entire residual-takeover family is closed immediately.
5. If low-tier prizes are below ticket price, `G(e)` need not be monotone; run the exact scanner across every `e`.

## Result
- **General forced-slot residual raffle theorem: VALIDATED.**
- **Virginia Commanders 2026: REJECTED for every sales state.**
- **Virginia Capitals 2026: REJECTED by identical board structure.**
- **Michigan online raffle platform: execution architecture promising for monitoring, no current qualifying board found in this run.**
- **Terminal SUCCESS: NO.**

## Files
- `src/loto_research/h159_residual_raffle_floor.py`
- `data/derived/h159_virginia_residual_raffle_floor.csv`
- `research/CHECKED_PROJECTS_AND_TESTS_H159_APPEND.md`

## Next action
1. Apply `G(e)` to live/announced fixed raffles with many low-tier winners and visible remaining inventory before any EV work.
2. Prioritize online platforms with no aggregate purchase cap (Michigan-style) and boards where full-board payout ratio is near/above 100% or external subsidy is added.
3. Continue deterministic Keno bundle/special monitor in parallel; these remain stronger than ordinary fixed raffles unless a subsidized board is found.
