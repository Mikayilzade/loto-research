# 4+4 — current baseline

Updated: 2026-08-12
Status: **exact probability model validated; ordinary payout engine strongly reconstructed; special carryover states still under test**

Primary game source:
- https://www.azerlotereya.com/game/fourplus

Detailed empirical reconstruction:
- `research/4plus4_economics_inference.md`

Corrected jackpot timeline:
- `data/historical/az_4plus4_jackpot_checkpoints.csv`

## Official mechanics
- public ticket price: **2 AZN**;
- A board: choose 4 numbers from 20;
- B board: choose 4 numbers from 20;
- A draw is made, balls are returned, then B is drawn;
- 11 winning categories;
- 4+4 wins the jackpot;
- jackpot rolls when unwon;
- current public tax note: 10% after subtracting ticket price and 500 AZN from the win amount.

The public page still does not explicitly expose a separate sentence saying “one base variant costs 2 AZN”. However payout/winner-count reconstruction makes 2 AZN per base variant a high-confidence inference consistent with the displayed ticket price. It remains labelled inference until confirmed by detailed registered rules, purchase flow or receipt.

## Exact probabilities
| Category | Match states | Probability | Approx. 1 in N |
|---|---|---:|---:|
| I | 4+4 | 0.000000042600278393 | 23,474,025 |
| II | 4+3 / 3+4 | 0.000005452835634281 | 183,390.82 |
| III | 4+2 / 2+4 | 0.000061344400885660 | 16,301.39 |
| IV | 4+1 / 1+4 | 0.000190849247199830 | 5,239.74 |
| V | 4+0 / 0+4 | 0.000155065013349862 | 6,448.91 |
| VI | 3+3 | 0.000174490740296988 | 5,730.97 |
| VII | 3+2 / 2+3 | 0.003926041656682226 | 254.71 |
| VIII | 3+1 / 1+3 | 0.012214351820789148 | 81.87 |
| IX | 3+0 / 0+3 | 0.009924160854391182 | 100.76 |
| X | 2+2 | 0.022083984318837523 | 45.28 |
| XI | 2+1 / 1+2 | 0.137411457983877900 | 7.28 |

Any listed prize state: **0.186147241472223** (~18.614724%, 1 in 5.372091).

## Corrected jackpot chronology
A prior research pass misread migrated website metadata and incorrectly treated a historical 530,359-AZN jackpot win as a July-2026 event. The primary article text is explicit: the win occurred **08.07.2023**, draw **23276**. It stated that the next jackpot would be 250,000 AZN. Therefore the 250k reset is evidence for the **2023 rule era**, not evidence of a 2026 reset.

The current accumulation is instead supported by these official lower-bound checkpoints:
- **15 Jan 2025:** >500,000 AZN;
- **19 Aug 2025:** >800,000 AZN;
- **26 Nov 2025:** >1,000,000 AZN;
- **26 Jan 2026:** >1,300,000 AZN;
- **10 Jun 2026:** >1,800,000 AZN contextually advertised for the current draw games/4+4 jackpot.

No jackpot win between those checkpoints has been established in the sources currently captured. Do not infer a continuous organic 4+4-only accumulation yet, because an external transfer event was explicitly announced in January 2025.

### External jackpot transfers are a real operator mechanism
On 6 Jan 2025 Azərlotereya announced that if the final Meqa 5/36 jackpot was not won, **the remaining jackpot would be added to the 4+4 jackpot**. The repository has not yet established whether the final Meqa 5/36 jackpot was won or the exact amount transferred.

This means any jackpot state equation must allow:

`J_t = prior_jackpot + ordinary_4+4_contributions + zero-winner/carryover_transfers + external_transfers - payouts/adjustments`

rather than assuming every increase came from 4+4 sales.

A similar historical policy existed in 2022 when Azərlotereya announced that an unwon final 6/40 jackpot would transfer to Meqa 5/36, confirming that cross-game jackpot migration is not a one-off conceptual possibility.

## Jackpot contribution to one variant
At jackpot probability 1/23,474,025, jackpot-only gross EV per base variant before tax/sharing is small even at the current million-AZN scale:
- 500k -> ~0.02130 AZN;
- 1.0m -> ~0.04260 AZN;
- 1.3m -> ~0.05538 AZN;
- 1.8m -> ~0.07668 AZN;
- 1.9m -> ~0.08094 AZN.

Therefore even a visually large ~1.8–1.9m jackpot cannot by itself turn an assumed 2-AZN base variant positive.

## Empirical lower-tier engine
Across preserved 2026 payout tables, define one common draw-level unit `U`:
- III ≈ 11U
- IV ≈ 5U
- VII ≈ 9U
- VIII ≈ 14U
- IX ≈ 7U
- V + VI ≈ 2U

Thus III–IX jointly distribute approximately **48U**.

Draw #790 was added only after this ratio had been inferred from other draws and independently fits it closely, providing a first out-of-sample confirmation.

Observed fixed categories X and XI pay 6 AZN and 4 AZN per winner in the sample. Their exact expected contribution is:

**0.6821497378485368 AZN per variant.**

Independent sales-volume estimates from X/XI winner counts give median `U/N ≈ 0.00995`, supporting the working scale `U ≈ 0.01 × sold_variants`. Under this scale:
- III–IX aggregate ≈ **0.48 AZN / variant**;
- X/XI ≈ **0.68215 AZN / variant**;
- subtotal before category II and jackpot ≈ **1.16215 AZN per assumed 2-AZN variant** (~58.11% gross return).

At a 1.8m jackpot, adding only the jackpot component raises this subtotal to about **1.23883 AZN / 2 AZN** before category II. At 1.9m it is about **1.24309 AZN / 2 AZN**. Category II therefore remains a critical missing economic component, but a very large additional overlay would still be needed to reach break-even.

## H014 — what remains interesting
The live question is specifically **zero-winner carryover plus external transfers**.

In all currently accessible sampled secondary draw tables, category II has zero winners, but the archive displays 0 rather than the category's assigned pre-draw fund. This makes II a prime candidate for an unobserved recurring transfer mechanism.

For any variable category with zero winners, determine whether its normally assigned money:
- transfers to jackpot;
- carries to the same category;
- moves to another category;
- enters a reserve;
- or is redistributed immediately.

The Kazakhstan 4/20 comparator now provides a replicated modern accounting signature: on three independent transitions, zero-winner lower-category pools moved into the next visible superprize exactly, together with the ordinary contribution. Azerbaijan must be tested independently; do not import Kazakhstan's rule.

If an accumulated balance survives into a future draw and is visible before purchase, it can be plugged into an exact forward EV model. If transfers are not observable or not retained, H014 weakens substantially.

## Current data
- `data/historical/az_4plus4_payout_samples_2026.csv`
- `data/derived/az_4plus4_pool_unit_validation.csv`
- `data/historical/az_4plus4_jackpot_checkpoints.csv`
- `src/loto_research/four_plus_four.py`
- `src/loto_research/pari_mutuel.py`
- `tests/test_four_plus_four.py`

Next milestone: obtain exact adjacent 4+4 jackpot values and/or the hidden official archive payload, then test whether zero-winner category money closes a t→t+1 jackpot accounting identity after explicitly controlling for external transfers.
