# H266 VALIDATION — Super66 terminal exact bound

Date: 2026-08-25
Result: **VALIDATED REJECTION**

## Independent arithmetic checks

Universe: 6 ordered decimal digits = `10^6 = 1,000,000` possible identifiers.

For any fixed winning result, with higher winning divisions taking precedence:
- D1 = 1.
- D2 raw union = `10 + 10 - 1 = 19`; remove D1 => **18**.
- D3 raw union = `100 + 100 - 1 = 199`; remove D1+D2 = 19 => **180**.
- D4 raw union = `1000 + 1000 - 1 = 1999`; remove D1-D3 = 199 => **1,800**.
- D5 raw union = `10000 + 10000 - 100 = 19,900`; remove D1-D4 = 1,999 => **17,901**.

The D5 intersection is 100 because matching both the first two and last two digits fixes four positions and leaves two positions free.

Using current Lotterywest fixed lower prizes A$6,666, A$666, A$66, A$6.60:
- D2 gross = A$119,988.00;
- D3 gross = A$119,880.00;
- D4 gross = A$118,800.00;
- D5 gross = A$118,146.60;
- total fixed lower gross = **A$476,814.60**.

At the current Lotterywest A$1/game price, the impossible exact one-copy full cover costs **A$1,000,000**, leaving **A$523,185.40** to be supplied by the player's Division-1 share before strict profit is possible.

Checked thresholds:
- sole winning D1 entry: `J > 523,185.40`;
- one external duplicate: `J/2 > 523,185.40`, so `J > 1,046,370.80`;
- general `E` external duplicates: `J > 523,185.40*(E+1)`.

Current/recent examples independently recomputed:
- 22 Aug 2026 A$80,000 pool: favourable sole-owner full-cover gross = **A$556,814.60 = 55.68146%**.
- 8 Aug 2026 A$449,669.85 pool: impossible grant of the entire D1 pool gives **A$926,484.45 = 92.648445%**. Published results actually show three D1 winning tickets, making the real share smaller.

## Structural checks

1. Any nonempty deterministic portfolio owns some identifier `x`.
2. `x` itself is a legal six-digit draw result.
3. Under that outcome the portfolio has a D1 winner.
4. Therefore no nonempty portfolio can guarantee the terminal **no-D1** branch for every draw result.
5. A complete identifier cover always has exactly one owned D1 identifier before external duplicates and therefore cannot force a D1-to-lower-division rolldown.
6. Current Lotterywest public instructions say the six digits are automatically generated; player-selectable exact takeover is not established.
7. No hard pre-draw cap on external duplicate entries was found in the checked current material.

## Source checks

- Lotterywest current Super66 page: A$1/game, automatically selected digits, current fixed lower payouts and minimum D1 payout.
- WA 2026 rules compilation: ordered six-digit criteria and higher-division precedence.
- Current results pages: 22 Aug 2026 A$80,000 jackpot; 8 Aug 2026 D1 pool A$449,669.85 shared by three winners.

The code/data pair reproduces the arithmetic:
- `src/loto_research/h266_super66_terminal_bound.py`
- `data/derived/h266_super66_terminal_bound.json`

Conclusion: **H266 closed under checked current rules; no strict guaranteed-profit construction established.**
