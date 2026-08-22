# H171 — Jamaica compact single-number coverage + Mega/Monsta Ball screen

Updated: 2026-08-22
Status: **CONDITIONAL >100% MODIFIER STATES FOUND / STRICT GUARANTEE REJECTED BECAUSE MODIFIER STATES ARE RANDOM**

## Purpose
Continue H170's search for compact lottery products where one paid selection can participate in extra fixed-prize mechanisms. Jamaica's current Cash Pot and Money Time are unusually compact one-number games and Supreme Ventures currently publishes Mega Ball as an add-on to both. The current results dashboard also still exposes Mega Ball / Monsta Ball result fields, while the promotions index labels Monsta Ball as a past promotion; therefore Monsta is treated only as a structural control unless current sale availability is separately confirmed.

## Current source set
Official current Cash Pot page:
- https://supremeventures.com/game/cash-pot/

Official current Money Time page:
- https://supremeventures.com/game/moneytime/
- https://supremeventures.com/game/money-time/

Official current Mega Ball page:
- https://supremeventures.com/game/mega-ball/

Official Supreme Ventures results dashboard (August 2026 results; includes Cash Pot Mega Ball / Monsta Ball fields):
- https://results.supremeventures.com/

Official Monsta Ball game/promotion pages (payout architecture; promotions index currently classifies Monsta Ball as Past Promotion):
- https://supremeventures.com/game/monsta-ball/
- https://supremeventures.com/promotion/monsta-ball/
- https://supremeventures.com/promotions/

## Cash Pot base full cover
Current official Cash Pot rules state:
- choose one number from 1–36;
- minimum wager J$10;
- winning J$10 wager pays J$280 (28x stake).

Exact all-number cover at minimum stake:
- 36 numbers × J$10 = **J$360 spend**;
- exactly one selected number wins;
- deterministic gross = **J$280**;
- strict base return = **77.7778%**.

This improves on many ordinary compact digit/Keno games but remains below break-even.

## Cash Pot + Mega Ball
Current Mega Ball page says the feature applies to Cash Pot and uses a separate chamber containing **2 white balls and 1 gold ball**, drawn after the main game. The Monsta Ball payout page gives the Cash Pot architecture at J$10 units: base J$280 plus J$700 when Mega is drawn. It also states Mega stake is an additional J$10 when base is J$10.

Assuming the currently published unit economics remain applicable to the current Mega feature:
- cover all 36 Cash Pot numbers with J$10 base + J$10 Mega each;
- total spend = **36 × J$20 = J$720**.

If Gold/Mega Ball is drawn:
- covered winning number receives J$280 base + J$700 Mega = **J$980**;
- conditional cover ratio = **980 / 720 = 136.1111%**;
- conditional pre-tax surplus = **J$260 = +36.1111%**.

If a white ball is drawn:
- no Mega increment;
- gross = J$280;
- strict unfavorable-state ratio = **280 / 720 = 38.8889%**.

Therefore the current Mega architecture creates a very large conditional overlay but cannot create a strict guarantee because Mega outcome is random after betting closes.

## Monsta Ball structural control
The official Monsta page describes a further paid add-on after Mega:
- J$10 base + J$10 Mega + J$10 Monsta = J$30 per selected Cash Pot number;
- both Mega and Monsta drawn: total J$1,980 (J$280 base + J$700 Mega + J$1,000 Monsta);
- Monsta drawn without Mega: J$580 (J$280 + J$300 Monsta).

If this feature were currently purchasable, full 36-number coverage would cost:
- **36 × J$30 = J$1,080**.

Published outcome ratios:
- both Mega + Monsta: `1,980 / 1,080 = 183.3333%`;
- Monsta without Mega: `580 / 1,080 = 53.7037%`;
- neither modifier: `280 / 1,080 = 25.9259%`.

So even the spectacular +83.33% favorable state does not matter for terminal guarantee: allowed modifier-miss branches remain deeply negative. The current promotions index calls Monsta Ball a **Past Promotion**, so this is not relied upon as a current executable product.

## Money Time control
Current official Money Time page describes a 1-of-38 matrix (1–36, 0, 00), minimum J$10, with ordinary number payout J$260 per J$10.

Base full cover:
- 38 × J$10 = **J$380**;
- deterministic gross J$260;
- ratio = **68.4211%**.

The Monsta page describes Mega payout for Money Time as base J$260 + J$700 when Mega is drawn. With equal J$10 base + J$10 Mega per covered state:
- total spend = **38 × J$20 = J$760**;
- favorable Mega gross = J$960;
- conditional ratio = **126.3158%**;
- unfavorable white-ball gross = J$260 = **34.2105%**.

Again: conditional >100%, strict floor far below 100%.

## Reusable conclusion
For a compact one-number game with base state count `N`, base unit stake `c`, deterministic winning payout `P`, and equal-cost binary add-on `a=c` paying extra `B` only on a favorable random state:

- favorable full-cover ratio: `(P+B) / [N(c+a)]`;
- unfavorable full-cover ratio: `P / [N(c+a)]`.

A large favorable ratio does not contribute to a strict all-outcome guarantee unless the favorable modifier state is **known/forced before ticket purchase** or the unfavorable branch itself is >=100%.

Jamaica Cash Pot is a strong example:
- favorable Mega state: **136.11%**;
- unfavorable state: **38.89%**.

## Result
- Current Cash Pot base cover: **77.7778%, REJECTED guarantee**.
- Cash Pot + Mega: **136.1111% conditional**, but **38.8889% strict floor** → NOT SUCCESS.
- Money Time + Mega: **126.3158% conditional**, but **34.2105% strict floor** → NOT SUCCESS.
- Monsta control can reach **183.3333% conditional**, but misses fall to 53.70%/25.93%, and current promotion status is not established → NOT SUCCESS.

## Reopen condition
Reopen only if Supreme Ventures introduces a cumulative-removal Mega/Monsta mechanism whose favorable state is publicly certain before sales close, or a deterministic subsidy/discount large enough to lift the non-modifier branch above 100% after taxes and execution costs.

## Next research
1. Search scheduled/cumulative modifiers where all losing balls are removed over prior draws and the final favorable state can be known pre-purchase.
2. Search compact single-number games with ordinary deterministic cover above Cash Pot's 77.78%, then pair only with deterministic pre-locked discounts or retailer-local subsidies.
3. Continue fixed scheduled Keno special-paytable and deterministic buy-X-get-Y-free monitor.
