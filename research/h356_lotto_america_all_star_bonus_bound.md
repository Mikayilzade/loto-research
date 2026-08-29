# H356 — Lotto America + All Star Bonus exact full-cover bound

Status: **CLOSED FOR CURRENT RULES — NO GUARANTEED PROFIT**

## Why this packet
H355 left a narrow forward filter: prioritize deterministic external subsidy or promotions that can lift an exact full-control floor above 100%. Lotto America's optional All Star Bonus is worth screening because its multiplier has a deterministic minimum of 2x on every non-jackpot prize.

## Current rule facts checked
Official state-lottery pages currently describe Lotto America as 5 main numbers from 1–52 plus one Star Ball from 1–10, at $1 per play. The All Star Bonus costs an additional $1 per play and multiplies every non-jackpot prize by 2x, 3x, 4x, or 5x. Iowa's current prize table gives the base non-jackpot fixed levels $20,000 / $1,000 / $100 / $20 / $5 / $5 / $2 / $2, while also warning that set prizes can be reduced pari-mutuel in exceptional cases. The Iowa page showed the next advertised jackpot for Aug. 29, 2026 as $3.12m (cash option $1.33m).

Sources checked 2026-08-29:
- Iowa Lottery Lotto America game/prize pages.
- Minnesota Lottery Lotto America page.
- South Dakota Lottery Lotto America page.

## Exact complete-cover arithmetic
Outcome space:

`C(52,5) * 10 = 25,989,600` lines.

For any draw, one-copy complete coverage has these exact prize-category multiplicities:
- 5 + Star Ball: 1
- 5 only: 9
- 4 + Star Ball: 235
- 4 only: 2,115
- 3 + Star Ball: 10,810
- 3 only: 97,290
- 2 + Star Ball: 162,150
- 1 + Star Ball: 891,825
- Star Ball only: 1,533,939

Independent full partition over every `(main-match count, Star match/no-match)` category sums exactly to **25,989,600 / 25,989,600**. Arithmetic inconclusive = **0**.

### Base ticket
Cost: **$25,989,600**.

Guaranteed advertised fixed non-jackpot gross under the player-favourable assumption that published set amounts are fully payable:

**$6,991,428 = 26.9008680395%** of cost.

The isolated jackpot needed merely to reach break-even would be **$18,998,172**. Even crediting the entire current advertised $3.12m jackpot to our single covered jackpot line without any dilution gives only **$10,111,428 gross**, deficit **$15,878,172**.

### All Star Bonus
Complete-cover cost doubles to **$51,979,200**. The worst legal multiplier is 2x and applies only to non-jackpot prizes, so the exact deterministic fixed gross is **$13,982,856**.

Return remains exactly **26.9008680395%** because both the fixed component and purchase price doubled. The jackpot is not multiplied, so the isolated jackpot required for break-even worsens to **$37,996,344**.

Even granting the full current advertised $3.12m jackpot, no sharing, no cash-value discount, and full published fixed awards gives only **$17,102,856 gross**, deficit **$34,876,344**.

This is already a deliberately player-favourable upper bound. The official warning that set prizes may become pari-mutuel can only lower the realized gross.

## Closure
All Star Bonus is not the required external subsidy. Its deterministic minimum multiplier is financed by a matching extra ticket charge, leaving the exact fixed-return ratio unchanged, while the jackpot remains unmultiplied and shareable.

**Arithmetic inconclusive: 0. Closure-relevant inconclusive: 0.**

Reopen only if a separately funded promotion grants a multiplier/credit/free duplicate entry without the corresponding $1 per-line surcharge, or otherwise adds a binding deterministic subsidy large enough to cross the exact cover deficit.
