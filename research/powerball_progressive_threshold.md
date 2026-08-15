# Powerball US — progressive jackpot threshold baseline

Updated: 2026-08-15
Status: **first-pass lower bound; real executable threshold is higher**

Primary current sources:
- https://www.powerball.com/
- https://www.powerball.com/powerball-prize-chart

## Current US game structure
- base play: 2 USD;
- 5 white balls from 69 + 1 Powerball from 26;
- jackpot odds: 1 in 292,201,338;
- lower prizes are fixed cash amounts outside California;
- advertised jackpot can be taken as annuity or cash option;
- jackpot can be shared among multiple winners;
- taxes are additional and jurisdiction-dependent.

## Fixed lower-tier expected value
Using the official current prize/odds chart and excluding the jackpot:

`EV_lower ≈ 0.31987825 USD per 2-USD play`.

Therefore the jackpot component must supply at least:

`2 - 0.31987825 = 1.68012175 USD`

of expected value before the base ticket can reach break-even.

## Absolute optimistic cash-jackpot floor
If we make the deliberately favorable assumptions:
- cash jackpot is received in full;
- no federal/state/local tax;
- no other jackpot winner shares the prize;
- no execution cost;

then required cash jackpot is:

`J_cash_floor = (2 - EV_lower) × 292,201,338`

`≈ 490,933,824 USD`.

This is an **absolute optimistic floor**, not a real-world break-even threshold.

Any realistic threshold must be higher because:
- jackpot sharing lowers expected retained share;
- taxes lower retained cash;
- sales increase sharply with jackpot size, increasing collision probability;
- UK participation began in July 2026 and increases the common jackpot player pool without changing US odds;
- some jurisdictions have different payout/tax details;
- transaction/execution constraints may matter for high-volume strategies.

## 2026 captured-state sanity check
Official July 29, 2026 snapshot:
- advertised jackpot: 663m USD;
- cash value: 290.4m USD.

290.4m is far below the optimistic 490.93m cash floor, so that captured state was negative EV even before tax and sharing.

A July 25 snapshot similarly had 613m advertised / 268.4m cash.

## Interpretation
Powerball can only become a serious H002 candidate at cash values well above ~491m USD, and even then only after explicit modeling of:
- expected jackpot share conditional on our chosen combination;
- current sales/player volume, including UK expansion;
- tax by purchase/claim jurisdiction;
- lower-tier jurisdiction differences;
- anti-popularity optimization from H003/H015.

Next step for H002: build the real threshold curve `required cash jackpot = f(sales, sharing model, tax, jurisdiction)` rather than using advertised annuity value.
