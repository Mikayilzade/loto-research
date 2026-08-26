# H281 STATUS — Virginia free-game bonus worst-case floor

Updated: 2026-08-26
Branch: `research-work`
State: **CLOSED / NO STRICT GUARANTEED-PROFIT FLOOR**
Global state remains: **NO SUCCESS; NOT EXHAUSTED**

H225-X* was read first and remains rigorously CLOSED / EXHAUSTED at X20 with 0 coefficient survivors / 0 legal shift tuples. No X21/X22 work was created.

## New checkpoint

Virginia currently gives **10 free Jackpot Spectacular games** when an eligible player cashes a first-ever winning ticket through the mobile app / mobile web flow.

This initially looked useful because it is a deterministic promotional entitlement triggered by a single completed action rather than a large subsidized all-number cart. However, it fails the strict-guarantee criterion at the payout layer: Jackpot Spectacular has published overall odds of winning any prize of **1 in 3.99**, so non-winning outcomes are legal, and the promotion does not guarantee a positive aggregate prize across the ten free games.

Therefore the entire ten-game bonus has strict worst-case cash floor **$0**.

As a cross-check against the smallest exact fixed-payout cover in the same jurisdiction, Virginia Pick 3 Pair has 100 possible pairs and pays $50 on a $1 Pair wager (half on $0.50). A full 100-pair cover returns exactly 50% of stake in every draw:
- $50 cover at $0.50 -> guaranteed $25;
- $100 cover at $1 -> guaranteed $50.

So a deterministic external subsidy must exceed $25 or $50 respectively merely to create strict positive cash profit. The current ten random free games contribute zero to that worst-case hurdle.

## Saved evidence

- `research/h281_virginia_mobile_bonus_floor.md`
- `research/H281_VALIDATION.md`
- `src/loto_research/h281_virginia_mobile_bonus_floor.py`
- `data/derived/h281_virginia_mobile_bonus_floor.json`

## NEXT ACTION

Do not reopen finite uncontrolled free-game promotions unless they carry a binding minimum aggregate payout. Continue searching for deterministic withdrawable Bonus Cash / cashback, a fixed-value post-purchase reward, or a finite/reservable subsidized asset whose guaranteed external value can exceed an exact cover deficit without requiring a fragile large all-number checkout.
