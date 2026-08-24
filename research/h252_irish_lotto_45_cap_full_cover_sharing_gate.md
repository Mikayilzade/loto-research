# H252 — Irish Lotto 6/45 cap full-cover sharing gate

Date: 2026-08-24
Scope: lottery only
Status: NOT A SUCCESS

## Question
Can the 5 September 2026 Irish Lotto 6/45 refresh create a strict guaranteed-profit full-cover opportunity near the jackpot cap / fifth-cap-draw regime?

## Current evidence
Official Irish National Lottery material confirms the new format begins 5 September 2026, reduces the matrix from 6/47 to 6/45, keeps price at €2 per line (€4 minimum two-line purchase), and retains Lotto as a pari-mutuel jackpot game. The current 6/47 rules also establish the cap mechanism: excess prize fund above the cap rolls down to the next winning tier; after at most five successive cap draws, an unwon jackpot itself rolls down.

A current pre-launch comparison published in August 2026 reports the new cap as €16,000,000 and fixed €4 awards for Match 3 and Match 2 + Bonus, with the intermediate tiers remaining variable/pari-mutuel. These launch values should be rechecked against the final official 6/45 rules PDF once published.

Sources:
- https://www.lottery.ie/news/press-releases/national-lottery-unveils-exciting-changes-to-lotto-and-lotto-plus-games
- https://www.lottery.ie/lotto-lotto-plus-and-lotto-5-4-3-2-1-game-change-faq
- https://cdn2.lottery.ie/uploads/Issue_9_RULES_LOTTO_6_OF_47_OCT_2024_29_10_d1d5da4a58.pdf
- https://irish.national-lottery.com/2026-irish-lotto-game-changes

## Exact full-cover arithmetic
For 6/45 there are C(45,6)=8,145,060 lines. At €2 per line, full cover costs:

- Spend S = €16,290,120.

Against any draw, a full cover contains exactly one Match-6 line. The deterministic counts of the two reported fixed €4 categories are:

- Match 3: C(6,3) C(38,3) = 168,720 lines;
- Match 2 + Bonus: C(6,2) C(38,3) = 126,540 lines.

So the fixed lower-tier floor is:

- F = 4 × (168,720 + 126,540) = €1,181,040.

At a €16m capped jackpot, if our one Match-6 line is the sole jackpot winner, jackpot + fixed floor is:

- €16,000,000 + €1,181,040 = €17,181,040;
- floor net before middle-tier pari-mutuel prizes and execution costs = **+€890,920**.

This is a real arithmetic near-miss / conditional overlay, not a guaranteed strategy.

## Sharing gate
Let k be the number of external Match-6 winning lines. Ignoring all positive middle-tier pari-mutuel receipts (favorable to proving a hard lower bound), our jackpot share is €16m/(k+1). The conservative floor is:

G(k) = €16,000,000/(k+1) + €1,181,040 - €16,290,120.

- k=0: +€890,920;
- k=1: -€7,109,080;
- k=2: -€9,775,746.67.

Therefore **one external jackpot-winning line is enough to destroy the strict full-cover profit floor**. Current rules provide no useful pre-draw hard cap forcing k=0.

## Fifth-cap-draw incompatibility
A full cover necessarily contains the realized Match-6 combination. Therefore the branch required for an unwon fifth-cap jackpot to roll down — zero jackpot winners — cannot occur when a valid full cover is successfully purchased. Full coverage cannot simultaneously force ownership of every outcome and trigger the no-jackpot-winner fifth-cap rolldown.

The ordinary cap excess-roll-down mechanism may still add value on capped draws, but it does not repair the guarantee: excess amounts are allocated into shared winning tiers, and external winner counts are not bounded tightly enough pre-draw to establish a positive all-outcome floor.

## Conclusion
**REJECTED as a strict guaranteed-profit full-cover strategy.** The 6/45 redesign creates a notable sole-jackpot-winner conditional floor above cost at the reported €16m cap, but jackpot sharing immediately breaks it and fifth-cap jackpot rolldown is logically incompatible with complete coverage.

Reopen only if final official 6/45 rules introduce a non-sharing top prize, a deterministic cap-excess allocation with a hard winner-count bound, a purchase subsidy exceeding the sharing deficit, or a mechanism that allows guaranteed capture of a roll-down without forcing a Match-6 winner.