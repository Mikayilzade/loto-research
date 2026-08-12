# Azerbaijan 4+4 — category II primary-source lead

Updated: 2026-08-12
Status: **two primary one-number-short tickets; ~20U category-II hypothesis promising but unvalidated**

## Why category II matters
Category II is the grouped 4+3 / 3+4 state. Exact probability per base variant is:

`0.000005452835634281` = about **1 in 183,390.82**.

In the currently preserved 2026 secondary payout tables, category II repeatedly has zero winners and its assigned pre-draw pool is not displayed. That makes category II one of the most important missing components in both ordinary EV and zero-winner carryover research.

## Primary-source evidence 1 — Nizami Tağıyev
Official winner page:
- https://www.azerlotereya.com/winners/nizami-tagiyev-128

Official Telegram:
- https://t.me/Azerlotereya/2353

The operator says Nizami:
- played 4+4;
- missed the jackpot by only **one number**;
- won **8,609 AZN**;
- while jackpot was above **1.5m AZN**.

The official winner page displays `Qazanma tarixi: 2/6/2026`. The current schedule is Tuesday/Friday, and a secondary archive places draw **#780** on **2026-06-02**. Therefore 2026-06-02 / draw #780 is the working event link.

## Primary-source evidence 2 — Ümüd Hüseynov
Official Telegram:
- https://t.me/Azerlotereya/2516

The operator says Ümüd:
- played 4+4;
- missed a jackpot above **1.8m AZN** by **one number**;
- won **15,986 AZN**.

The exact calendar date/draw has not yet been recovered from the public Telegram archive.

## What “one number short” establishes
For one ordinary 4+4 variant, being one number short of 4+4 means exactly seven of the eight required numbers matched, corresponding to category II (`4+3 / 3+4`).

Therefore both tickets contain at least one category-II winning variant.

However, **do not set the category-II per-winner prize equal to the reported ticket payout**. The game allows 5+5 / 6+6 combination tickets and one ticket can contain multiple winning variants/categories.

## New ~20U working hypothesis
The reconstructed ordinary pool engine operates on a draw-level scale `U` around 400–430 AZN in the sampled 2026 period. Official category-III winner stories independently reproduce that same scale through `reported 4+2 payout / 11`.

The category-II stories produce a striking numerical pattern:
- Nizami: `8,609 / 20 = 430.45`;
- Ümüd: `15,986 / 40 = 399.65`.

Both values sit on the same observed U scale.

A compact hypothesis is therefore:
- ordinary category-II pool weight may be approximately **20U**;
- Nizami may have held one category-II winning variant;
- Ümüd may have held two category-II variants (or an equivalent aggregate produced by a system ticket), giving roughly `2 × 20U`.

This is a **hypothesis, not a rule**. Other explanations remain possible, including additional lower-category wins, a state-dependent category-II pool, or payout aggregation/rounding.

Primary winner cross-check data:
- `data/historical/az_4plus4_official_winner_crosschecks.csv`

## Why 20U would matter economically
If category II normally receives 20U and empirical `U/N≈0.01`, its sales-funded aggregate pool is about:

`20 × 0.01 = 0.20 AZN per sold variant`.

But because category II is rare (~1 in 183,391), many draws will have no category-II winner at the observed volume. Immediate one-draw EV cannot simply add the full 0.20 AZN unless the pool is guaranteed to be distributed in that draw. The zero-winner destination/carryover rule remains decisive.

## Decisive checks
Highest-value evidence now is any of:
1. recover draw #780 full payout table;
2. recover Ümüd's exact draw and full payout table;
3. obtain original ticket/system structure for either winner;
4. find a third official one-number-short winner with known ticket structure;
5. capture detailed registered rules that explicitly state category-II allocation.

If a normal draw with one category-II winner shows a category-II total around `20U`, the hypothesis becomes much stronger. If repeated zero-winner category-II amounts can then be tracked into jackpot or another state, H014 can be converted into an exact transition model.

## Jackpot checkpoint side effect
Official Telegram message IDs provide an ordered jackpot sequence:
- message 2335: jackpot >1.2m AZN;
- message 2344: jackpot >1.4m AZN;
- message 2353: jackpot >1.5m AZN, linked to Nizami/draw #780;
- message 2516: jackpot >1.8m AZN, linked to Ümüd.

Exact calendar dates for 2335/2344/2516 remain unresolved.
