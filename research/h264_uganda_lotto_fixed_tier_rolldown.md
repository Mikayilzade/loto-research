# H264 — Uganda LOTTO fixed-tier / special-roll-down screen

## Question
`STATUS.md` prioritizes current forced-distribution/roll-down mechanics where externally accumulated money becomes a **fixed per-winning-selection** lower-tier payout rather than a shareable pool.

Uganda National Lottery LOTTO is a strong candidate because its current published rules contain both fixed lower divisions and a special jackpot roll-down.

## Current official rules checked
Primary source: Uganda National Lottery, `LOTTO GAME RULES`, published v1.6:
https://www.nationallottery.go.ug/assets/documents/LOTTO_RULES_AND_REGULATIONS.pdf

Relevant mechanics:
- 6 numbers from 1–52 plus a bonus number; **UGX 1,000** per entry.
- Participant daily LOTTO wager cap: **UGX 500,000**.
- Divisions 1–6 are pari-mutuel.
- Division 7 (Match 3) is fixed at **UGX 10,000 per winning entry**.
- Division 8 (Match 2 + Bonus) is fixed at **UGX 4,000 per winning entry**.
- Ordinary rule 6.5.3 sends an empty Division 6 pool to Division 1 of the next draw rather than into fixed Division 7.
- Special roll-down rule 7.2 allows Division-1 money to descend through lower divisions only **excluding fixed payout divisions**.
- Rule 7.3 repeats that discretionary jackpot allocation across lower divisions also **excludes fixed payout divisions**.

That exclusion directly blocks the target mechanism: accumulated jackpot money cannot become an enlarged deterministic fixed amount on Match 3 or Match 2+Bonus tickets.

## Exact full-cover audit
One-copy complete 6/52 coverage contains `C(52,6) = 20,358,520` entries and costs **UGX 20,358,520,000**.

For any six-main-plus-bonus result, the fixed-tier counts are invariant:
- Match 3: `C(6,3) * C(45,3) = 283,800` entries;
- Match 2 + Bonus: `C(6,2) * C(45,3) = 212,850` entries.

Fixed-tier gross therefore equals:
- Match 3: **UGX 2,838,000,000**;
- Match 2 + Bonus: **UGX 851,400,000**;
- total: **UGX 3,689,400,000**;
- return: **18.1221424740%** of one-copy full-cover cost.

This is an audit bound, not a practical proposal; the official participant wager cap is far below a one-draw full cover.

## Result
**REJECTED for the fixed-per-selection external-subsidy search.**

The attractive-looking combination of fixed lower tiers plus jackpot roll-down is explicitly separated by the rules. Accumulated Division-1 money cannot be certified as a deterministic fixed-per-winning-entry enhancement to Divisions 7 or 8.

This closes this specific current-v1.6 mechanism, not every conceivable Uganda LOTTO strategy.

## Reopen condition
Reopen if official rules are amended so accumulated/forced-distribution funds can enter Division 7 or 8 on a per-winning-entry basis, or if a deterministic promotion adds a fixed enhancement to those categories.
