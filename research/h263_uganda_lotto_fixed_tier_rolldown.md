# H263 — Uganda LOTTO fixed-tier / special-roll-down screen

## Question

`STATUS.md` NEXT ACTION prioritizes current forced-distribution or roll-down mechanics where externally accumulated money can become a **fixed per-winning-selection** lower-tier payout rather than a shareable pari-mutuel pool.

Uganda National Lottery LOTTO is a particularly relevant candidate because its current published rules contain both:

- fixed lower prize divisions; and
- an explicit special jackpot roll-down feature.

## Current official rules checked

Source: Uganda National Lottery, `LOTTO GAME RULES`, current published v1.6:
https://www.nationallottery.go.ug/assets/documents/LOTTO_RULES_AND_REGULATIONS.pdf

Key mechanics:

- LOTTO is 6 numbers from 1–52, with a bonus number; one entry costs **UGX 1,000**.
- A participant is limited to **UGX 500,000 of LOTTO wagers per day**.
- Divisions 1–6 are pari-mutuel.
- Division 7 (Match 3) is fixed at **UGX 10,000 per winning entry**.
- Division 8 (Match 2 + Bonus) is fixed at **UGX 4,000 per winning entry**.
- If ordinary Division 6 has no winner, its accumulated fund does **not** fall into fixed Division 7; rule 6.5.3 sends it to Division 1 of the next draw.
- Under the special jackpot roll-down, rule 7.2 permits the jackpot to descend through lower divisions only **excluding fixed payout divisions**.
- Rule 7.3 likewise allows discretionary allocation across lower prize divisions only **excluding fixed payout divisions**.

That exclusion is decisive for the mechanism being searched: accumulated jackpot money cannot be converted into an enlarged deterministic fixed amount on Match 3 or Match 2 + Bonus tickets.

## Exact full-cover audit

A one-copy complete 6/52 cover contains

`C(52,6) = 20,358,520` entries,

costing **UGX 20,358,520,000** before considering the participant wager cap.

For any draw (six mains plus one bonus), exact fixed-tier winning-entry counts are invariant:

- Match 3: `C(6,3) * C(45,3) = 283,800` entries;
- Match 2 + Bonus: `C(6,2) * C(45,3) = 212,850` entries.

Therefore the guaranteed gross from the two genuinely fixed tiers is exactly:

- Match 3: `283,800 * 10,000 = UGX 2,838,000,000`;
- Match 2 + Bonus: `212,850 * 4,000 = UGX 851,400,000`;
- total fixed-tier gross = **UGX 3,689,400,000**;
- fixed-tier return = **18.1221424740%** of one-copy full-cover cost.

This calculation is not intended as a practical full-cover proposal. The official rules additionally cap a participant at UGX 500,000 of LOTTO wagers per day, far below a one-draw full cover.

## Result

**REJECTED for the fixed-per-selection external-subsidy search.**

Uganda LOTTO looks structurally promising at first glance because the same rules contain fixed lower tiers and a jackpot roll-down. But the rules explicitly wall those two mechanisms off from each other: the special roll-down excludes fixed payout divisions, and an empty Division 6 goes back to next-draw Division 1 rather than into Division 7.

Accordingly no accumulated Division-1/pari-mutuel pool can be certified as a deterministic fixed-per-winning-entry enhancement to the two fixed tiers under the current rules.

This does **not** claim that every possible Uganda LOTTO strategy is mathematically exhausted; it closes this specific NEXT-ACTION mechanism under current v1.6 rules.

## Reopen condition

Reopen only if official rules change so that accumulated/forced-distribution money is paid into Division 7 or 8 on a per-winning-entry basis, or a new deterministic promotion adds a fixed payout to those categories.
