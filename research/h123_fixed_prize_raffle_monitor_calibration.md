# H123 — fixed-prize raffle undersubscription monitor calibration

Updated: 2026-08-20
Status: **MONITOR CLASS VALIDATED / FLORIDA +EV REPRODUCED / MARYLAND & VIRGINIA NEGATIVE CONTROLS / NO CURRENT TERMINAL GUARANTEE**

## Goal
Generalize H122 into a reusable official-lottery monitor and test whether the Florida 2026 result was a one-off artifact or part of a broader class of fixed-prize raffles whose economics can be screened from public ticket counts.

## Screening identity
For any ticket purchased at time `t`, define:
- `P` = ticket price;
- `B_t` = total fixed prize board from still-eligible future drawings for that ticket;
- `N` = final eligible sold-ticket denominator;
- `C` = bounded tax/execution reserve per ticket.

Pre-tax expected gross per ticket is `B_t / N` when each sold ticket is equally eligible for the remaining fixed board. The clean pre-tax break-even denominator is:

`N* = B_t / P`.

A live +EV signal exists when `N < N*` (or conservatively `B_t/N > P + C`). This is an EV test only. A strict guarantee still requires a positive minimum portfolio payout in every legal draw outcome.

## Case 1 — Florida Millionaire Raffle 2026 (positive control)
Official rules fixed four interim prize boards of **$704,500** each and, for <=1,000,000 final sales, **10 × $1,000,000** final prizes. Final official sales were **369,180** tickets at **$20**.

For a ticket bought in the last window before the fourth interim drawing, the still-eligible fixed board was:

`B = $704,500 + $10,000,000 = $10,704,500`.

Break-even denominator:

`N* = 10,704,500 / 20 = 535,225`.

Observed final denominator `369,180 < 535,225`, giving:

`EV gross = 10,704,500 / 369,180 = $28.9953`

or **+44.9767% pre-tax expected ROI** on the $20 ticket.

This reproduces H122 and validates the monitor logic on a real operator-funded overlay.

Primary sources:
- Florida Lottery Emergency Rule 53ER26-16 / Millionaire Raffle rules.
- Florida Lottery official final winners/results page.

## Case 2 — Maryland Holiday Raffle 2025/26 (negative control despite undersubscription)
Maryland offered at most **325,000** sequential $20 tickets. Final official sales were only **237,206**, so the game was materially undersubscribed.

Final drawing fixed board:
- 1 × $1,000,000 = $1,000,000
- 10 × $100,000 = $1,000,000
- 1,000 × $500 = $500,000
- 3,000 × $100 = $300,000
- 6,000 × $50 = $300,000

Total final board: **$3,100,000**.

A late ticket bought after all three Early Bird drawings was therefore worth at the realized denominator:

`3,100,000 / 237,206 = $13.0688` gross on a $20 ticket = **65.3440% gross return**.

Final-draw break-even denominator:

`3,100,000 / 20 = 155,000 tickets`.

Even if one unrealistically assigns all three earlier $50,000 Early Bird prizes to every ticket's eligible board, the total board is only **$3,250,000**, corresponding to **68.5059%** of realized ticket revenue. Thus simple undersubscription alone is insufficient; the fixed external board must be large enough relative to the final denominator.

Primary sources:
- Maryland Lottery Holiday Raffle official game page.
- Maryland Lottery January 2, 2026 official result announcement stating 237,206 tickets sold.

## Case 3 — Virginia Commanders / Capitals online raffles (negative sellout controls, useful monitor architecture)
Virginia's 2026 Commanders Golden Pass and Capitals Career in a Year raffles each used:
- **150,000** tickets;
- **$20** price;
- drawing at sellout or fixed deadline, whichever came first;
- winners selected from **sold** raffle numbers;
- fixed published prize board including a headline experiential prize valued at **$950,000**, plus 5 × $10,000, 500 × $500, and 3,000 × $100.

Nominal board value:

`950,000 + 50,000 + 250,000 + 300,000 = $1,550,000`.

Nominal break-even denominator would therefore be **77,500 sold tickets** if the $950,000 experiential valuation were accepted at face value. Cash-only lower-tier board is only **$600,000**, giving a much more conservative break-even denominator of **30,000 tickets** when the non-transferable experiential prize is assigned zero cash-resale value.

Both 2026 raffle pages now show **0 tickets left / sold out**, so their realized denominator was 150,000 and they were clearly negative at face-value economics:
- nominal board gross = **51.6667%** of ticket spend;
- lower-tier cash-only gross = **20.0000%**.

The important reusable fact is structural: Virginia's rules explicitly allow a deadline drawing from the pool of tickets actually sold. A future Virginia raffle with slow sales could therefore become an undersubscription overlay, but only if the observable sold count falls below a defensible cash-value break-even threshold before sales close.

Primary sources:
- Virginia Lottery Commanders Golden Pass Raffle official rules and game page.
- Virginia Lottery Capitals Career in a Year Raffle official rules/game page.

## Michigan monitor architecture
Michigan Lottery's current official Online Raffles FAQ confirms a useful future monitoring class:
- limited ticket supply;
- fixed ticket price;
- predetermined prize count;
- draw either after sellout or at a predetermined deadline;
- no aggregate purchase limit (250 per cart, repeat carts allowed).

No current crawlable official active raffle with a favorable live ticket-count/prize-board state was found in this packet, so Michigan is a **monitor target**, not a candidate.

## General result
H123 establishes three separate facts:
1. **Undersubscription can create very large genuine +EV** when the operator-funded fixed board is large enough (Florida positive control).
2. **Undersubscription by itself is not an edge** (Maryland negative control).
3. Deadline-drawn, fixed-board online raffles with public tickets-remaining counters are the best live-monitor architecture (Virginia/Michigan), but the prize's real cash value must be conservatively bounded.

## Strict guarantee status
Still **NO SUCCESS**. For all incomplete ownership portfolios, a legal draw outcome exists in which every prize-winning number belongs to external holders, so minimum portfolio payout can be zero. Full ownership is only a guarantee candidate when the full eligible acquisition cost is below a fixed cash prize floor; none of the calibrated cases satisfy that condition.

## Next action
Build the recurring monitor around the inequality `remaining fixed cash-value board / expected final eligible denominator > ticket price + costs`, with priority to:
- state lotteries publishing live `tickets remaining` counters;
- deadline drawings that proceed even if inventory is unsold;
- fixed cash prizes rather than hard-to-value experiential prizes;
- late-entry tickets that remain eligible for a large fixed board;
- any rule giving a deterministic minimum prize per block or allowing complete ownership of all eligible sold entries.
