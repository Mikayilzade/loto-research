# H031 — Cash Pop Cover All guarantee screen

Updated: 2026-08-16
Status: **REJECTED as guaranteed-profit path; guarantee-of-a-prize is not guarantee-of-profit**

## Goal
Test a current compact finite product whose own marketing explicitly says that buying all 15 numbers guarantees a prize.

Targets:
- Georgia Lottery Cash Pop;
- Virginia Lottery Cash Pop.

Both current official pages state that the player may select 1–15 numbers, one number from 1–15 is drawn, and each selected number has a prize amount assigned to it at purchase. Both offer $1/$2/$5/$10 wagers per number. Virginia explicitly calls the all-15 option `Cover All`; Georgia states `Play all 15 numbers and you're Guaranteed a win!`.

Primary sources:
- Georgia Lottery: https://www.galottery.com/en-us/games/draw-games/cash-pop.html
- Virginia Lottery: https://www.valottery.com/data/draw-games/cashpop

## Exact Cover-All guarantee theorem
For wager `w`, buying all 15 distinct numbers costs

`15w`.

Exactly one number is drawn. Therefore exactly one of the 15 covered number-plays wins the draw prize.

The official prize tables show that the minimum possible draw prize is `5w` at every wager level:
- $1 wager -> minimum prize $5;
- $2 -> $10;
- $5 -> $25;
- $10 -> $50.

Because prize amounts are randomly assigned by the terminal at purchase, a legal assignment state exists in which the ultimately drawn covered number has the minimum prize. Thus the strict deterministic payout floor of Cover All is only

`5w / (15w) = 1/3 = 33.3333%`.

Guaranteed net floor:

`5w - 15w = -10w`.

So the four wager levels have guaranteed-loss floors:
- $1 each: cost $15, minimum draw payout $5, net -$10;
- $2 each: cost $30, minimum draw payout $10, net -$20;
- $5 each: cost $75, minimum draw payout $25, net -$50;
- $10 each: cost $150, minimum draw payout $50, net -$100.

This rejection does not require assumptions about independence of prize assignments or exact assignment probabilities. It uses only the legal minimum prize and the fact that one of 15 numbers is drawn.

## Expected-value cross-check
Using the published overall prize odds and `EV = sum(prize / odds)` per number-play:

Georgia gross EV ratios:
- $1: 62.9670%;
- $2: 65.1911%;
- $5: 67.8803%;
- $10: 70.4735%.

Virginia gross EV ratios:
- $1: 60.9823%;
- $2: 64.0336%;
- $5: 67.2277%;
- $10: 70.0062%.

These are not needed for the guarantee proof, but independently confirm that ordinary additive play remains negative expectation.

## Georgia retail instant-win add-on
Georgia currently states that every retail/vending-machine Cash Pop play is eligible for an instant cash win equal to double the wager, with published odds:
- $1 -> $2 at 1 in 100;
- $2 -> $4 at 1 in 70;
- $5 -> $10 at 1 in 65;
- $10 -> $20 at 1 in 50.

This add-on is random, not deterministic. A legal all-no-instant-win branch remains. Therefore it contributes **zero** to the strict guaranteed payout floor and cannot rescue Cover All as a guaranteed-profit strategy.

## Adaptive/post-purchase observation check
The prize assigned to a purchased number is shown after purchase. That information does not create a refund/cancel right: Georgia explicitly says ticket purchases cannot be voided or canceled, and Virginia describes the prize as randomly assigned by the terminal to each number-play.

Observing a high assigned prize after buying a number cannot retroactively make the other 14 number states covered for free. Any strategy that leaves a number uncovered retains a legal draw outcome with zero draw payout from that uncovered number. Buying all 15 restores outcome coverage but returns to the 33.3333% strict floor above.

## Conclusion
Cash Pop is a useful control because the operator itself markets an all-outcome `guaranteed win` construction. The guarantee is real in the narrow sense of winning **some prize**, but the minimum prize is only one third of the full coverage cost.

Therefore:
- Georgia Cash Pop Cover All: **REJECTED as guaranteed-profit path**;
- Virginia Cash Pop Cover All: **REJECTED as guaranteed-profit path**;
- Georgia retail instant-win overlay: **REJECTED as guarantee enhancer because it has a no-win branch**.

This closes the current 15-number Cash Pop / Cover-All construction unless a future deterministic rebate or prize-floor rule changes the economics.
