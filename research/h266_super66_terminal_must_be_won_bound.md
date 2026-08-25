# H266 — Australian Super66 terminal / must-be-won screen

Date: 2026-08-25
Status: **REJECTED / CLOSED for strict guaranteed-profit terminal/takeover mechanism**

## Why this game was opened

Super66 is unusually relevant to the current NEXT ACTION because it combines a finite six-digit identifier universe, fixed lower prizes, a jackpot that can accumulate, and a terminal rule after a maximum run of jackpots. Current Lotterywest material states that Super66 costs **A$1 per game**, uses six automatically generated digits, pays fixed lower prizes of A$6,666 / A$666 / A$66 / A$6.60, and jackpots Division 1 when it is not won. Current published game descriptions also state that after the maximum jackpot run the top pool must be distributed to the highest winning division if Division 1 is not won.

Sources checked:
- Lotterywest current Super66 game page: https://www.lotterywest.wa.gov.au/games/super66
- Western Australia current Super66 rules publication (2026 compilation): https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent=&query=mrdoc_38917.pdf
- Current results archive / 22 Aug 2026 draw: https://australia.national-lottery.com/super-66/results and https://australia.national-lottery.com/amp/super-66/results/22-08-2026
- 8 Aug 2026 payout example: https://australia.national-lottery.com/amp/super-66/results/08-08-2026

## Exact impossible-favourable full-cover audit

Grant the player something stronger than Lotterywest actually offers: exact deliberate ownership of each of the **1,000,000** six-digit strings once, at the official Lotterywest A$1/game price. Cost = **A$1,000,000**.

For any drawn six-digit result, higher-division precedence gives invariant counts:
- Division 1: 1 exact identifier;
- Division 2: 18 identifiers;
- Division 3: 180;
- Division 4: 1,800;
- Division 5: 17,901.

The Division-5 union needs care: first-two matches = 10,000 strings, last-two matches = 10,000, and their intersection has 100 strings because the two middle digits remain free. Thus the first2-or-last2 union is 19,900; subtract the 1,999 identifiers already in Divisions 1-4 to obtain 17,901.

Fixed lower-tier gross is therefore:

`18*6666 + 180*666 + 1800*66 + 17901*6.60 = A$476,814.60`.

That is only **47.68146%** of the deliberately favourable A$1m complete-cover cost. The Division-1 share received by our portfolio must therefore exceed **A$523,185.40** merely to reach strict profit.

If the jackpot is `J` and there are `E` external tickets duplicating the winning six-digit identifier, our exact cover receives at most `J/(E+1)` from Division 1. Hence strict profit requires:

`J > A$523,185.40 * (E+1)`.

Examples:
- with zero external duplicates: jackpot must exceed **A$523,185.40**;
- with one external duplicate: jackpot must exceed **A$1,046,370.80**.

The latest completed draw on **22 Aug 2026** showed an A$80,000 jackpot. Even granting our impossible exact cover sole ownership of the winning identifier, gross would be only **A$556,814.60 = 55.68146%** of cost.

A recent much larger draw on **8 Aug 2026** had a Division-1 pool of **A$449,669.85**, actually shared by three winning tickets. Even granting our impossible full cover the entire pool rather than a share would produce only **A$926,484.45 = 92.648445%** of cost.

## Terminal-roll-down incompatibility theorem

The terminal must-be-won branch does not rescue a guaranteed strategy.

Any nonempty fixed portfolio contains at least one six-digit identifier `x`. The legal draw outcome `x` makes that owned entry an exact Division-1 winner. Therefore **no nonempty pre-draw portfolio can force the no-Division-1 branch for every legal draw outcome**. In particular, a complete cover always creates an owned Division-1 winner and therefore cannot simultaneously force a terminal roll-down to Division 2 or below.

External play makes the guarantee weaker still: current material gives no hard pre-draw bound on how many other entries can duplicate the eventual winning identifier, so a jackpot large enough to cross the sole-winner threshold still does not provide a strict floor without a duplicate cap.

Finally, current Lotterywest instructions say Super66 numbers are **automatically generated**. Thus the deliberately favourable exact identifier takeover used above is not established as executable in the first place.

## Result

H266 is closed for the current terminal/takeover lane:
1. fixed lower prizes recover only **47.68146%** under an impossible exact full cover;
2. the latest and recent large 2026 jackpots remain below even the sole-winner break-even threshold in the checked examples;
3. any nonempty portfolio has a legal outcome in which it itself creates a Division-1 winner, so it cannot force the terminal no-D1 rolldown;
4. external duplicate winners have no certified hard cap;
5. exact six-digit ownership is not player-selectable under the checked Lotterywest purchase mechanism.

Reopen only if a future rule change introduces player-selectable/reservable identifiers plus a hard external-duplicate bound, or a jackpot/subsidy structure that creates a strict lower bound above A$523,185.40 per complete A$1m cover after sharing.

Reproducibility files:
- `src/loto_research/h266_super66_terminal_bound.py`
- `data/derived/h266_super66_terminal_bound.json`
- `research/H266_VALIDATION.md`
