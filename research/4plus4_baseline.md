# 4+4 — exact probability baseline and state-dependent payout lead

Updated: 2026-08-11
Status: **probability model validated; economic EV not yet validated**

## Official mechanics captured
Primary source: https://www.azerlotereya.com/lotereya/4-4

Current public rules state:
- two boards, A and B;
- player selects 4 numbers from 1–20 on each board;
- 4 numbers are drawn for A;
- balls are returned before the B draw, then 4 numbers are drawn for B;
- 11 prize categories exist;
- the minimum listed winning match configurations include 1+2, 2+1, 0+3 and 3+0;
- 4+4 wins the jackpot;
- public page displays a **2 AZN ticket price**;
- jackpot can roll forward when not won;
- current public tax note says 10% is withheld after subtracting ticket price and 500 AZN from the win amount.

### Critical unresolved pricing point
The public 4+4 page displays `Bilet qiyməti 2₼`, but unlike the current Beşdə 5 page it does **not** explicitly state the cost of one individual variant.

Therefore this research does **not** assume that one 4+4 variant costs 1 AZN. Economic EV remains parameterized until this is verified from an official rule document or an actual purchase flow/receipt.

This matters materially: a 1-AZN and a 2-AZN per-variant interpretation lead to completely different economic conclusions.

## Exact one-board probabilities
For one board, with 4 selected and 4 drawn from 20:

| matches | probability |
|---:|---:|
| 0 | 0.3756449948400413 |
| 1 | 0.4623323013415893 |
| 2 | 0.1486068111455108 |
| 3 | 0.0132094943240454 |
| 4 | 0.0002063983488132 |

Because the balls are returned before the B draw, the A/B probabilities multiply.

## Exact grouped category probabilities
The 11 public winning match groups can be represented as follows:

| Category | A+B match states | Probability | Approx. 1 in N |
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

Probability of any of the 11 prize configurations:

`0.186147241472223` = about **18.614724%**, or **1 in 5.372091**.

Jackpot probability:

`1 / C(20,4)^2 = 1 / 23,474,025`.

The exact implementation is in `src/loto_research/probability.py` and regression-tested in `tests/test_probability.py`.

## Jackpot state observations from official sources
Official operator news provides additional state information that is useful for modelling:

- on 28 July 2026 a **530,359 AZN** jackpot was won;
- the operator stated that the next jackpot would be **250,000 AZN**, confirming a post-win reset/floor at that amount for that rule era;
- the same article states that approximately four months earlier a **913,072 AZN** 4+4 jackpot had been won;
- an official 26 November 2025 article reported the jackpot had exceeded **1,000,000 AZN** for the first time;
- an official January 2026 year-in-review article said more than **1,300,000 AZN** was then waiting in 4+4.

Primary references:
- https://www.azerlotereya.com/xeberler/44da-530-359-manatliq-cekpotu-saatli-sakini-qazandi-41
- https://www.azerlotereya.com/xeberler/44-lotereyasinda-cekpot-1-000-000-manati-kecdi-1883
- https://www.azerlotereya.com/xeberler/azarlotereya-2025-ci-ilda-267-boyuk-udus-qazandirib-1888

### Jackpot component is small by itself
Because the jackpot probability is only 1 / 23,474,025, the jackpot-only gross EV contribution of one variant before tax/sharing is:

- 250,000 AZN jackpot -> about **0.01065 AZN**;
- 530,359 AZN jackpot -> about **0.02259 AZN**;
- 913,072 AZN jackpot -> about **0.03890 AZN**;
- 1,300,000 AZN jackpot -> about **0.05538 AZN**.

Therefore the jackpot level observed so far cannot by itself plausibly overcome a 1–2 AZN variant cost. If 4+4 contains an exploitable state edge, the economically important component is much more likely to be the lower-category allocation/carryover system, or a promotion/price effect, rather than jackpot accumulation alone.

## Evidence that lower-tier payouts are state-dependent
The official public game page does not expose the full historical prize table in crawlable HTML. A secondary archive currently exposes draw-level winner counts and payouts. It must be independently reconciled against primary data before being treated as authoritative.

Secondary archive examples:
- draw 776, 2026-05-19: https://lucky-numbers.ru/lottery/az/4-4/1779205500000
- draw 795, 2026-07-24: https://lucky-numbers.ru/lottery/az/4-4/latest-result (snapshot at retrieval)
- archive: https://lucky-numbers.ru/lottery/az/4-4

Observed payout values vary materially between draws for categories III–IX while categories X and XI in the sampled draws were 6 AZN and 4 AZN respectively. This is a strong signal that a simple fixed-prize-table EV model is inadequate.

For example, using the exact category probabilities and treating one sampled draw's published per-winner payouts as if they were exogenous gives a lower-tier gross expectation greater than 1 AZN per variant. **That calculation is not an executable EV estimate** because:
- per-winner payouts can depend on sales and winner counts;
- our own purchases can change winner counts and pool shares;
- category carryovers may alter a draw's state;
- the per-variant ticket cost is not yet verified;
- jackpot, taxes, purchase limits and execution constraints still need modelling.

The observed variation is therefore a research lead, not a profitability claim.

## H014 candidate — category-pool/carryover state edge
A current 4+4 draw may become materially better value when money accumulated in jackpot and/or lower-tier pools is redistributed into a draw whose expected competing-winner count is low.

To validate or reject this we need, by draw:
1. exact rule-version prize-fund allocation;
2. exact per-variant price;
3. jackpot before draw;
4. any category carryover balances before draw;
5. ticket/variant sales volume;
6. winners and payout by category;
7. tax treatment;
8. online/retail purchase limits;
9. model of how our own portfolio changes payout sharing.

## Immediate next test
Reconstruct at least 50–100 consecutive 4+4 draws with winner counts and payout amounts. Infer whether category prize pools follow stable allocation formulas and whether carryovers can be identified from state transitions. Only then calculate forward-observable EV thresholds.
