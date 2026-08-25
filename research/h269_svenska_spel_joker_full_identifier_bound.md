# H269 — Svenska Spel Joker full-identifier takeover bound

Date checked: 2026-08-25
Status: **REJECTED / CLOSED for the fixed-plan full-identifier takeover mechanism**

## Why this candidate was checked
`STATUS.md` asks for finite player-selectable/reservable identifier spaces and fixed per-winning-selection payouts. Svenska Spel Joker is unusually clean on both dimensions: the result is a seven-digit decimal number, some play methods allow the customer to enter an arbitrary Joker number, and the Joker prize plan is fixed rather than pari-mutuel.

Current official rules (effective for draws from 3 September 2025 onward) state:
- Joker draws one number from `0000000` through `9999999`;
- under some play methods a customer may enter an arbitrary Joker number;
- Joker cannot be played standalone with Lotto: participation requires the corresponding Lotto draw;
- Joker stakes are SEK 10/20/30;
- at SEK 10 the fixed prizes are SEK 10,000,000 / 100,000 / 10,000 / 500 / 80 / 40 for 7/6/5/4/3/2 consecutive correct positions;
- disjoint winning runs can both pay, but a digit position cannot be reused for more than one claimed win;
- 39.66% of Joker stakes are allocated to Joker prize payments;
- first- and second-tier aggregate liabilities are capped at SEK 60m and SEK 10m respectively, which can only reduce a mass-cover payout if triggered.

Official sources:
- https://cdn1.svenskaspel.net/content/cms/documents/779afe3f-0363-4c36-b79c-1881549a8cbc/1.29/spelregler-lotto-och-joker.pdf
- https://www.svenskaspel.se/lotto/spelguide/joker

## Exact full-space calculation
For any fixed drawn Joker number, each candidate identifier is represented by a 7-bit mask indicating which positions match. A mask with `m` matching positions represents exactly `9^(7-m)` identifiers. There are only 128 masks, so the entire 10,000,000-identifier universe is enumerated exactly without approximation.

For each maximal contiguous run of matched positions of length at least two, the corresponding fixed prize is awarded. Summing all masks gives the exact invariant full-cover distribution:

| Total payout on identifier | Number of identifiers |
|---:|---:|
| SEK 0 | 9,455,130 |
| SEK 40 | 494,262 |
| SEK 80 | 46,413 |
| SEK 120 | 486 |
| SEK 160 | 9 |
| SEK 500 | 3,402 |
| SEK 540 | 18 |
| SEK 10,000 | 261 |
| SEK 100,000 | 18 |
| SEK 10,000,000 | 1 |

Checks:
- counts sum to **10,000,000**;
- winning identifiers = **544,870**;
- exact fixed-plan gross = **SEK 39,664,000**.

At the minimum SEK 10 Joker stake, literal ownership of all 10,000,000 Joker identifiers costs **SEK 100,000,000 in Joker stakes alone**, so the deterministic fixed-plan return is exactly **39.664%**.

Joker must be combined with Lotto. A Lotto row currently costs SEK 4 per draw. Even granting the impossible-favourable execution assumption that every one of the 10,000,000 distinct Joker identifiers can be entered and paired with only the minimum one Lotto row, acquisition cost is at least **SEK 140,000,000**. The exact Joker fixed-plan gross is then only **28.3314286%** of combined minimum spend.

This is already a stronger-than-real rejection of the target takeover mechanism: adding the mandatory base-game cost cannot improve the economics of the fixed Joker payout schedule itself. Any attempted rescue must rely on Lotto/Drömvinsten outcomes and is therefore a different joint-game construction, not a profitable full-Joker-identifier takeover.

## Structural notes
- Current rules do permit arbitrary Joker number entry only in **some** play methods, so operationally buying the complete set is not established. H269 deliberately grants this stronger execution assumption before rejecting the economics.
- Aggregate caps on Joker prize groups 1 and 2 are adverse to mass duplication and cannot raise the full-cover floor.
- The fixed 25m Drömvinsten is a joint Lotto+Joker event requiring the same play to have Lotto 7-right and at least one Joker win; it is not automatically forced by owning the Joker identifier universe. A separate joint covering problem would be required before treating that fund as deterministic subsidy.

## Conclusion
**Closed:** the current Svenska Spel Joker fixed-prize identifier space is finite and partially player-selectable, but a complete one-copy takeover returns only **39.664% of Joker stake** and at most **28.3314% of the minimum mandatory Lotto+Joker acquisition spend** from the Joker fixed plan. It does not meet the guaranteed-profit target.

Reopen only if the fixed prize schedule, acquisition subsidy, mandatory-base pricing, or a deterministic joint Lotto/Joker promotion changes enough to add more than the current >60% Joker-stake deficit.
