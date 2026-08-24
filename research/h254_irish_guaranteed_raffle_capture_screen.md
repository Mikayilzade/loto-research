# H254 — Irish guaranteed-raffle capture screen

Date: 2026-08-24
Status: NOT A SUCCESS
Scope: lottery-only

## Question
Can a guaranteed-prize raffle or a special raffle overlay avoid the jackpot-sharing/full-cover incompatibility by forcing an external subsidy into a finite or otherwise coverable lottery outcome space?

## Fresh mechanisms checked

### A. Irish National Lottery Christmas Millionaire Raffle 2025
Official rules state that at most **600,000 unique tickets** are offered. Ticket price is **€25**. The published guaranteed prize schedule is:
- 1 × €1,000,000
- 6 × €100,000
- 15 × €10,000
- 45 × €5,000
- 302 × €1,000
- 8,131 × €500

Total guaranteed prize pool = **€6,342,500**.
Maximum full-inventory cost = `600,000 × €25 = €15,000,000`.
Even under impossible-perfect execution in which one buyer acquires every ticket, gross deterministic return is only:

`€6,342,500 / €15,000,000 = 42.2833%`

Guaranteed deficit before execution friction = **€8,657,500**.

This is a clean finite-space rejection: unlike jackpot games, sharing is not the blocker; the fixed guaranteed prize pool itself is far below total ticket cost.

Official sources:
- https://www.lottery.ie/game-information/millionaire-raffle
- https://cdn1.lottery.ie/uploads/Millionaire_Raffle_Rules_2025_e5472fe182.pdf

### B. EuroMillions Ireland Only Raffle special draw
The Irish National Lottery special draw guarantees that ten normal Ireland Only Raffle winners each receive €5,000 and one of those ten receives an **additional €1,000,000**. Entry is generated only by buying EuroMillions lines.

The €1m overlay is real and externally funded from the Ireland Only Raffle Reserve Fund, but it is not deterministically capturable by a finite player-owned cover:
- raffle codes are generated with EuroMillions purchases across the entire market;
- the special €1m winner is selected from the ten winning IOR codes;
- a player cannot preselect or reserve the entire market-wide set of issued IOR codes;
- there is no useful pre-draw hard cap on other issued entries that allows a guaranteed monopoly of the ten winning codes at bounded cost.

Therefore the overlay can improve EV but does not produce a strict all-outcome positive-profit guarantee.

Official source:
- https://www.lottery.ie/game-information/euromillions/euromillions-ireland-only-raffle

### C. Lotto Plus Million Euro Raffle
The special event similarly adds **€1,000,000** to one ticket among all tickets carrying the winning Lotto Plus Raffle number. The ordinary winning raffle number can have many winners; historical 2026 events typically produced roughly 60–120 €500 winners before one of them received the extra €1m.

Again, the external subsidy is genuine, but capture requires controlling the market-wide set of tickets carrying the winning raffle number. Buying Lotto Plus lines does not deterministically assign all possible raffle-number ownership to the buyer, and no finite pre-draw market cap guarantees sole ownership of the candidate set.

Official sources:
- https://www.lottery.ie/game-information/lotto-plus/million-euro-raffle
- https://www.lottery.ie/news/winners-stories/lotto-player-in-cork-becomes-4th-national-lottery-millionaire-of-2026

## Result
Three distinct guaranteed-prize/overlay structures were tested:
1. **finite fixed-ticket raffle** — fully coverable in principle, but total guaranteed prizes are only 42.2833% of full ticket cost;
2. **market-generated raffle overlay** — €1m external subsidy exists, but the player cannot deterministically own the full eligible code population;
3. **winning-number overlay** — €1m external subsidy exists, but ownership of all tickets sharing the winning raffle number cannot be guaranteed at bounded cost.

Thus forced raffle distribution avoids the zero-jackpot-winner incompatibility, but current Irish examples fail on either payout-ratio arithmetic or uncontrollable market-entry ownership.

## Reopen conditions
Reopen this class only if a current lottery offers at least one of:
- a finite, fully purchasable ticket inventory with total guaranteed cash prizes strictly above total remaining acquisition cost after fees/taxes;
- an externally funded raffle overlay where all eligible identifiers can be deterministically purchased or reserved before draw;
- a hard pre-draw cap on external eligible entries that allows a provable worst-case positive-profit cover.

## Conclusion
**NOT A SUCCESS.** Guaranteed raffle overlays are a valid nonlinear subsidy class, but the tested Irish structures do not provide a strict executable guaranteed positive net-profit strategy.
