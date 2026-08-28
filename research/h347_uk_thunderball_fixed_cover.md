# H347 — UK Thunderball exact fixed-prize full-cover screen

Date: 2026-08-29
State: **CLOSED FOR THIS SCREEN — NOT SUCCESS**

## Why this packet
`STATUS.md` NEXT ACTION #1 asks for current mechanisms where payouts are fixed per winning selection rather than shareable pools. H346 showed that a fixed top prize is insufficient when the lower tiers needed for economics are pari-mutuel. Thunderball is a stronger structural candidate because the advertised prize table is fixed per winning line across all winning categories.

H225-X* was checked before opening H347 and remains terminal CLOSED / EXHAUSTED; H225-X20 has 0 coefficient survivors / 0 legal shift tuples, so no X21/X22 was created.

## Current public parameters
Official National Lottery material currently states that Thunderball costs £1 per line and uses 5 main numbers from 1-39 plus one Thunderball from 1-14. A 14 Jan 2026 official prize breakdown shows the live advertised tiers: Match 5 + Thunderball top prize £500,000; Match 5 £5,000; Match 4 + TB £250; Match 4 £100; Match 3 + TB £20; Match 3 £10; Match 2 + TB £10; Match 1 + TB £5; Match 0 + TB £3. The same official page warns that in exceptional circumstances certain prizes may be less than stated.

Sources:
- https://www.responsible-play.national-lottery.co.uk/ — current matrix and £1 line price.
- https://www.national-lottery.co.uk/results/thunderball/draw-history/prize-breakdown/3835 — official 14 Jan 2026 prize table and current prize-reduction caveat.
- https://assets.ctfassets.net/j16ev64qyf6l/ZJ2fdCyUs8ony1FhVo2kn/a4f68e9e322d0456110d5900baf7f763/Thunderball_Licence_I3_V1.pdf — historical regulator licence confirming the same 5/39 + 1/14 matrix and £1 entry structure; used only as structural cross-check, not as current-law authority.

## Exact one-copy full cover
The complete outcome-space cover contains

`C(39,5) * 14 = 8,060,598` lines,

so at £1 each the acquisition cost is **£8,060,598**.

For any fixed draw, symmetry gives the exact number of covered lines in each `(main matches, Thunderball match)` category as

`C(5,k) * C(34,5-k) * (1 if TB matched else 13)`.

This yields:

| category | exact lines | advertised prize/line | gross |
|---|---:|---:|---:|
| 5 + TB | 1 | £500,000 | £500,000 |
| 5 | 13 | £5,000 | £65,000 |
| 4 + TB | 170 | £250 | £42,500 |
| 4 | 2,210 | £100 | £221,000 |
| 3 + TB | 5,610 | £20 | £112,200 |
| 3 | 72,930 | £10 | £729,300 |
| 2 + TB | 59,840 | £10 | £598,400 |
| 2 | 777,920 | £0 | £0 |
| 1 + TB | 231,880 | £5 | £1,159,400 |
| 1 | 3,014,440 | £0 | £0 |
| 0 + TB | 278,256 | £3 | £834,768 |
| 0 | 3,617,328 | £0 | £0 |

Validation totals:
- category-count sum = **8,060,598**, exactly the universe;
- advertised fixed-prize gross = **£4,262,568**;
- acquisition cost = **£8,060,598**;
- deficit = **£3,798,030**;
- return = **52.8815355883%**;
- arithmetic inconclusive = **0**;
- closure-relevant inconclusive = **0**.

## Closure
This candidate has exactly the structural property H346 was missing — fixed advertised per-winning-selection lower tiers — but the exact arithmetic is decisively below break-even. Even granting the full advertised prize amount in every category, the complete cover returns only 52.88% of cost.

The official current caveat that exceptional circumstances can reduce certain prizes is one-sided against the player. Therefore advertised-prize arithmetic is already a player-favourable upper bound for this screen; any prize-cap reduction can only lower the guaranteed floor further.

No external-duplicate modelling, rolldown assumption, CI chunking, or stochastic simulation is required to close H347. The exact category partition exhausts all 8,060,598 covered lines with zero inconclusive arithmetic.

## NEXT ACTION
Continue `STATUS.md` NEXT ACTION #1 but raise the gate: prioritize fixed-per-winning-selection games only when an exact full-cover first-pass bound can plausibly exceed roughly 100% of acquisition cost, ideally because an external subsidy/forced-distribution amount is additive to ordinary fixed tiers. Pure fixed-prize games around ordinary lottery payout ratios can be rejected before deeper execution analysis.
