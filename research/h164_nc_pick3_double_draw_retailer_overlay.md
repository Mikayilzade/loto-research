# H164 — North Carolina Pick 3 forced Double Draw + retailer commission overlay

Updated: 2026-08-22
Status: **PROMISING RECURRING DETERMINISTIC OVERLAY / NOT TERMINAL SUCCESS**

## Why this packet matters
H161-H163 found a structurally positive New Jersey Pick-3 Green Ball overlay if a licensed retailer can count the ordinary sales commission on its own valid cover, but New Jersey's public cancellation language does not provide a clear multi-ticket rollback window.

North Carolina has a closely analogous Pick 3 **Double Draw** promotion with two stronger public execution facts:

1. The promotion uses a depleting white-ball process and can reach an observable state where a second Pick 3 drawing is **guaranteed** that evening. NC Lottery explicitly announced such guaranteed nights in prior cycles, including November 17 and November 24, 2025. The latest completed 2026 cycle ran in July 2026 and produced multiple Double Draws.
2. NC Lottery's official game FAQ states that a retail Carolina Pick 3 ticket can, at the purchaser's request, be canceled on the issuing retailer terminal **within 15 minutes of purchase or before the draw break, whichever comes first**. This is materially stronger rollback language than the NJ `at the time of purchase` formulation.

Official sources used:
- NC Pick 3 how-to-play/prize table: https://nclottery.com/pick3-how-to-play
- NC Pick 3 game FAQ / cancellation rule: https://nclottery.com/FAQGames
- 2026 Double Draw evidence: https://nclottery.com/NewsBlogDetails/2026/7/16/Double-Draw-pays-off-for-Pick-3-players
- Guaranteed Double Draw example: https://nclottery.com/NewsBlogDetails/2025/11/17/Two-Pick-3-drawings-guaranteed-tonight
- NC retailer application (7% commission): https://nclottery.com/RetailerApplication
- Current retailer contract v. 05-27-2026: https://nclottery.com/Content/Docs/Retailer_Contract_v1.pdf
- NC statute G.S. 18C-142: https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/ByArticle/Chapter_18C/Article_5.html

## Exact deterministic cover
Current Carolina Pick 3 Pair rules:
- Pair is an exact ordered two-digit match (Front or Back).
- A $0.50 Pair play pays **$25**.
- Odds are **1 in 100**.

Choose one pair position, e.g. Front Pair, and buy every ordered pair `00` through `99`:

- 100 plays × $0.50 = **$50 face spend**.
- In one ordinary Pick 3 drawing, exactly one of the 100 Pair plays wins.
- Guaranteed base payout per drawing = **$25**.
- Ordinary deterministic cover ratio = **50%**.

On a forced Double Draw evening the same valid ticket selections participate in two separate Pick 3 drawings and prizes are paid on both sets of numbers.

Therefore for the same $50 cover:
- first draw guarantees one $25 Pair prize;
- Double Draw guarantees another $25 Pair prize;
- total guaranteed gross prizes = **$50**;
- deterministic prize-only return = **100%**.

This remains true even if both drawings produce the same winning pair; that same covered Pair wins once in each separate drawing.

## Retailer overlay
North Carolina law and the current retailer contract state that retailers receive **7% of the retail price of tickets or shares sold by the retailer** for each lottery game.

If a licensed retailer's own otherwise-valid $50 Pick-3 purchase is included in commission-bearing sales, then:

- ticket face sales = $50.00
- guaranteed Double Draw Pair prizes = $50.00
- 7% retailer commission = **$3.50**
- combined pre-tax deterministic value = **$53.50**
- pre-tax surplus = **+$3.50**
- deterministic pre-tax return on face spend = **107.00%**

This is the same broad mechanism as H161/H162 but with a larger sales commission (7% versus NJ 5%) and a materially better published cancellation window.

## Execution improvement versus New Jersey
NC Lottery's FAQ says retail Pick-3 tickets may be canceled on the terminal where produced within 15 minutes of purchase or before draw break, whichever occurs first.

This creates a plausible rollback protocol:
1. wait for an officially/observably guaranteed Double Draw state;
2. prepare all 100 distinct Pair selections before approaching the terminal;
3. begin issuing the cover sufficiently before draw break;
4. if any required selection is unavailable/refused, request cancellation of already issued cover tickets while every ticket is still inside the 15-minute cancellation window;
5. proceed only if the complete cover is accepted.

Unlike NJ, this is not merely `cancel at time of purchase`; NC publicly defines a clock window.

## Why this is still NOT SUCCESS
### Gate 1 — no current active forced state
The latest identified 2026 Double Draw promotion ran in July 2026. As of this packet date (2026-08-22), there is no verified current active forced-yellow-ball evening. The mechanism is recurring and executable only when the promotion returns and the state reaches zero white balls.

### Gate 2 — retailer self-purchase commission is not explicit
The statute and contract say 7% of tickets/shares `sold by Retailer`; the public application says 7% on each ticket sold. Public eligibility rules do not reveal a blanket prohibition on an adult retailer owner buying lottery tickets. But this packet did **not** find an explicit NCEL sentence saying that a retailer's own personal ticket purchased through its licensed location remains commission-bearing sales for accounting purposes.

Because the +7% overlay is the entire pre-tax edge, this must be confirmed before terminal SUCCESS.

### Gate 3 — rollback is strong but not atomic
The 15-minute cancellation right materially reduces execution risk, but the public rule is still ticket-by-ticket. It does not explicitly promise an atomic `all prior tickets roll back if any later required ticket fails` basket operation.

A terminal/system outage after some cover tickets are issued could, in principle, prevent cancellation before the 15-minute/draw-break deadline. Therefore the current public documentation does not prove a zero-loss execution branch under every allowed operational failure.

### Gate 4 — taxes and entity separation
The gross deterministic overlay is only $3.50 on $50. If the player and retailer are different tax persons (e.g. owner personally buys while business receives commission), 2026 wagering-loss rules and business income tax can alter the combined result. A terminal theorem requires a lawful taxpayer/entity configuration with an after-tax floor > $0.

### Gate 5 — promotion rules can change between cycles
The forced-state theorem depends on the returning promotion retaining the same `remove white ball until Yellow remains / prizes paid on both draws` structure. Recheck the rules each cycle.

## Result
- **Forced Double Draw state:** validated historical/current-2026 recurring mechanism.
- **100-Pair exact cover:** validated, $50 cost -> $50 guaranteed prizes on a forced two-draw evening.
- **NC retailer commission:** validated at 7% of retail ticket/share sales by statute and current contract.
- **Cancellation window:** validated at retail as up to 15 minutes / before draw break.
- **Conditional pre-tax overlay:** **107% / +$3.50** if self-purchased valid tickets are commission-bearing.
- **Terminal SUCCESS:** not yet; inactive current state + self-sale accounting + non-atomic outage/tax gates remain.

## Reopen / execution checklist
Reopen immediately when NC Pick 3 Double Draw returns. Highest-value checks:
1. wait until NC Lottery publicly indicates only Yellow Ball remains / Double Draw is guaranteed;
2. obtain written NCEL retailer/accounting confirmation that an owner/retailer personal valid Pick-3 purchase is included in commission-bearing gross sales;
3. obtain current terminal manual language on batch cancellation and whether all tickets from a customer sequence can be cancelled after intervening transactions within the 15-minute window;
4. confirm no promotion-specific prohibition on retailer participation;
5. model the exact player/retailer taxpayer configuration under current federal + NC tax rules.

If items 1-5 all lock before play, H164 can become a genuine terminal candidate.