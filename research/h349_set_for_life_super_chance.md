# H349 — UK Set For Life full-cover / Super Chance cap stress

Date: 2026-08-29
Status: **CLOSED AS STRICT GUARANTEE; IMPORTANT NEAR-CANDIDATE**

## Why this packet
H348 left a concrete next-action: prioritize external subsidy or special-event mechanics that remain additive even when our own portfolio hits the top tier. Set For Life is unusual because a Super Chance draw upgrades Match 5 (without the Life Ball) to the same nominal 30-year top prize as Match 5 + Life Ball.

## Current base game
The official National Lottery page gives £1.50 per play and the eight current prize tiers. The draw space is 5 main numbers from 47 plus one Life Ball from 10, so a one-copy complete cover contains

`C(47,5) * 10 = 15,339,390` lines

and costs **£23,009,085**.

For any draw, the full-cover match multiplicities are invariant:

| class | count |
|---|---:|
| 5 + LB | 1 |
| 5 | 9 |
| 4 + LB | 210 |
| 4 | 1,890 |
| 3 + LB | 8,610 |
| 3 | 77,490 |
| 2 + LB | 114,800 |
| 2 | 1,033,200 |
| all losing classes | 14,103,380 |

The full partition sums exactly to **15,339,390**, so arithmetic inconclusive = 0.

At ordinary advertised prizes, gross is **£12,949,100**, return **56.2782048917%**, deficit **£10,059,985**. Ordinary Set For Life is therefore nowhere near a strict full-cover profit.

## Super Chance special-event mechanism
Current informational sources describe Super Chance as an occasional special draw where both Match 5 + Life Ball and Match 5 win the 30-year top prize; the top-prize pool is capped at **£18m**. No next Super Chance date is currently announced.

A full cover necessarily produces exactly **10 own top-winning entries** in such a draw: 1 matching the Life Ball and 9 with the other Life Balls. The fixed non-top tiers contribute **£8,269,100**.

With zero external top-tier duplicates, our ten winning entries collectively consume the £18m cap, giving:

- gross: **£26,269,100**
- profit: **£3,260,015**
- return: **114.1683817501%**

This is the first checked fixed-cover special-event construction in this lane that crosses 100% in the no-external-duplicate model.

## Exact dilution separator
The cap is shared among all top-winning entries, not reserved to our cover. If `d` external top-winning entries exist, our cap share is

`£18,000,000 * 10 / (10 + d)`.

Stress results:

| external top winners d | our top share | total gross | profit vs cover cost |
|---:|---:|---:|---:|
| 0 | £18,000,000.00 | £26,269,100.00 | +£3,260,015.00 |
| 1 | £16,363,636.36 | £24,632,736.36 | +£1,623,651.36 |
| 2 | £15,000,000.00 | £23,269,100.00 | +£260,015.00 |
| **3** | **£13,846,153.85** | **£22,115,253.85** | **-£893,831.15** |

Therefore only **three legal external top-tier duplicate entries** destroy the strict guarantee. No binding pre-draw mechanism capping external top-tier winners at <=2 was established. Hence Super Chance is not a guaranteed-profit construction even though the isolated full-cover economics are >100%.

## Closure
- Exact partition: validated, 15,339,390 / 15,339,390.
- Arithmetic inconclusive: **0**.
- Closure-relevant inconclusive: **0** for the claimed result.
- Strict guaranteed profit: **NO**.
- Useful new checkpoint: **special-event full cover can cross 100%, but a candidate is actionable only if top-tier external dilution is hard-bounded to at most two equivalent winners (for this exact economics), or if the subsidy is non-dilutable/additive.**

Sources checked 2026-08-29:
- Official National Lottery Set For Life game page / current prize table and £1.50 play price.
- Official Set For Life Game Specific Rules: ordinary top cap £16m and second-tier cap £2m.
- Current third-party Super Chance rules page, cross-checked against the historical Gambling Commission control-sheet approval of the Set For Life Super Chance variation; no next event currently announced.
