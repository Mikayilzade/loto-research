# 4+4 — current baseline

Updated: 2026-08-12
Status: **exact probability model validated; ordinary payout engine strongly reconstructed; special carryover states still under test**

Primary game source:
- https://www.azerlotereya.com/game/fourplus

Detailed empirical reconstruction:
- `research/4plus4_economics_inference.md`

## Official mechanics
- public ticket price: **2 AZN**;
- A board: choose 4 from 20;
- B board: choose 4 from 20;
- A draw is made, balls are returned, then B is drawn;
- 11 winning categories;
- 4+4 wins the jackpot;
- jackpot rolls when unwon;
- current public tax note: 10% after subtracting ticket price and 500 AZN from the win amount.

The public page still does not explicitly expose a separate sentence saying “one base variant costs 2 AZN”. However the payout/winner-count reconstruction now makes 2 AZN per base variant a high-confidence inference consistent with the displayed ticket price. It remains labelled inference until confirmed by detailed registered rules, purchase flow or receipt.

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

## Jackpot contribution
Official operator news has documented a 250,000 AZN post-win reset and jackpot states of 530,359 AZN, 913,072 AZN and above 1m/1.3m.

At jackpot probability 1/23,474,025, jackpot-only gross EV per base variant before tax/sharing is small:
- 250k -> ~0.01065 AZN;
- 530,359 -> ~0.02259 AZN;
- 913,072 -> ~0.03890 AZN;
- 1.3m -> ~0.05538 AZN.

The observed jackpot range alone cannot make an ordinary 2-AZN variant profitable.

## Empirical lower-tier engine
The earlier observation that categories III–IX have variable per-winner payouts is now largely explained.

Across preserved 2026 draw tables, define one common draw-level unit `U`:
- III ≈ 11U
- IV ≈ 5U
- VII ≈ 9U
- VIII ≈ 14U
- IX ≈ 7U
- V + VI ≈ 2U

Thus III–IX jointly distribute approximately **48U**.

Draw #790 (2026-07-07) was added only after this ratio had been inferred from other draws and independently fits it closely, providing a first out-of-sample confirmation.

Observed fixed categories X and XI pay 6 AZN and 4 AZN per winner in the sample. Their exact expected contribution is:

**0.6821497378485368 AZN per variant.**

The working scaling `U ≈ 0.01 × sold_variants` is consistent with observed X/XI winner counts and with a 2-AZN base variant. Under this scale:
- III–IX aggregate ≈ **0.48 AZN / variant**;
- X/XI ≈ **0.68215 AZN / variant**;
- subtotal before category II and jackpot ≈ **1.16215 AZN per 2-AZN variant** (~58.11% gross return).

So an ordinary 4+4 state remains strongly negative. The floating per-winner numbers are mostly an accounting consequence of variable pool size and winner count, not a free edge.

## H014 — what remains interesting
The live question is now specifically **zero-winner carryover**.

For a draw where a variable low-probability category receives no winners, determine whether its normally assigned money:
- carries to the same category;
- transfers to another category;
- joins the jackpot;
- enters a reserve;
- or is redistributed immediately.

If an accumulated balance survives into a future draw and is visible before ticket purchase, it can be plugged into an exact forward EV model. If unpaid balances are not carried or are not observable, H014 likely dies.

## Current data
- `data/historical/az_4plus4_payout_samples_2026.csv`
- `src/loto_research/four_plus_four.py`
- `tests/test_four_plus_four.py`

Next milestone: 50–100 consecutive draws with emphasis on zero-winner categories II–VI and t→t+1 transition reconstruction.
