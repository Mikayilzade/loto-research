# H259 — fixed pull-tab pack buyout screen

Date: 2026-08-24
Scope: LOTTERY ONLY
Status: **REJECTED for current ordinary full-pack guarantee**

## Question

Can a lottery product with a genuinely finite, predetermined pack of winning and losing tickets create a strict guaranteed-profit buyout once the entire pack is acquired?

This differs materially from ordinary scratchers. A fixed pull-tab box can publish the complete box size and complete prize composition, so buying the whole box removes draw variance, jackpot sharing, crowd dilution and unknown remaining-inventory composition.

## Current official test case

Wisconsin Lottery `GONE FISHIN'` Pull-Tab Game #2752 is dated January 5, 2026. Official Features and Procedures state:

- ticket price: **$0.50**;
- tickets are sold in boxes;
- each box contains **1,050 tickets**;
- prize composition per box:
  - 200 × $0.50;
  - 25 × $1;
  - 10 × $5;
  - 2 × $15;
  - 2 × $25;
  - 1 × $75;
- there is no drawing.

Official source:
- https://wilottery.com/games/instant-games/gone-fishin-features-procedures

## Exact deterministic arithmetic

Full box acquisition at retail price costs:

`1,050 × $0.50 = $525`.

The complete published fixed prize mass is:

`200×$0.50 + 25×$1 + 10×$5 + 2×$15 + 2×$25 + 1×$75 = $330`.

Therefore a complete box has outcome-independent gross return:

`$330 / $525 = 62.8571428571%`.

Guaranteed loss before any acquisition friction is:

`$525 - $330 = $195`.

Because the pack is already fully covered, selection, prediction, physical-ball bias, RNG analysis and syndicate diversification cannot alter this identity.

## Subsidy / promotion hurdle

If an external promotion multiplied **every** prize in the box for free by `(1+u)`, break-even requires:

`$330 × (1+u) >= $525`,

so

`u >= 59.09090909%`.

Thus even this unusually clean finite-population mechanism needs a deterministic player-eligible subsidy or universal free prize uplift above **59.09%** merely to reach break-even, before taxes/fees/execution.

A random Doubler/Tripler tag does not satisfy this condition for a strict guarantee because a legal execution branch can leave purchased tickets without the tag. A retailer operating margin is also not automatically a player subsidy: ordinary player acquisition is at the ticket retail price unless rules explicitly grant the buyer a deterministic discount.

## General structural conclusion

Predetermined pull-tab boxes are a valid lottery-specific guarantee class because the complete pack can make the prize total deterministic. However, the guarantee test collapses to a simple finite identity:

`guaranteed net = fixed pack prize total + external deterministic subsidy - complete acquisition cost - costs`.

For the current 2026 Wisconsin test case, the fixed pack itself is decisively negative. The class should not be reopened by remaining-prize estimates or selective ticket purchase; doing so destroys the complete-pack certainty that makes the proof possible.

## Reopen conditions

Reopen immediately if a current lawful lottery/pull-tab product has one of:

1. a sealed finite pack whose guaranteed cash prize total exceeds complete player acquisition cost;
2. a deterministic player-eligible discount reducing the `GONE FISHIN'`-style acquisition cost by more than the exact deficit;
3. a universal free prize uplift above the exact pack hurdle (59.0909% for this game), with no random qualification branch and no payout cap that pushes the worst case below stake;
4. a fixed externally funded pack bonus that is guaranteed once the entire pack is purchased.

## Conclusion

**NOT A SUCCESS.** Fixed pull-tab packs remove randomness and sharing cleanly, but the current exact 2026 box tested returns only **62.8571%** of retail cost; no qualifying deterministic subsidy crossing the **59.09%** hurdle was established.

Reproduction:
- `src/loto_research/h259_fixed_pulltab_pack_screen.py`
- `data/derived/h259_fixed_pulltab_pack_screen.json`
