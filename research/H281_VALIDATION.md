# H281 VALIDATION

Validated: 2026-08-26
Packet: **H281 — Virginia current bonus-value worst-case screen**
Result: **PASS / CLOSED AS STRICT-GUARANTEE CANDIDATE**

## Independent arithmetic checks

Virginia Pick 3 Pair outcomes depend on two fixed digit positions. There are 10×10 = **100** possible ordered pairs.

At a $0.50 stake per Pair:
- full one-copy cover cost = 100 × $0.50 = **$50**;
- official Pair prize = one-half of the published $50 prize = **$25**;
- exactly one Pair in the cover matches every draw;
- deterministic gross ratio = $25 / $50 = **50%**;
- deterministic external credit must exceed **$25** for strict positive cash profit versus the player's cash contribution.

At a $1 stake per Pair:
- cost = **$100**;
- guaranteed prize = **$50**;
- deterministic gross ratio = **50%**;
- deterministic external credit must exceed **$50** for strict profit.

The arithmetic in `data/derived/h281_virginia_mobile_bonus_floor.json` matches these identities exactly.

## Promotion-floor check

The current Virginia first-mobile-cashing promotion supplies **10 free Jackpot Spectacular games**. The official game page reports overall odds of winning any prize of 1 in 3.99, which necessarily implies non-winning legal game outcomes. No checked promotion rule guarantees that one or more of the ten free games wins or specifies a positive minimum aggregate prize.

Therefore a legal realization exists in which all promotional games return zero. For strict guaranteed-profit analysis, the promotional bundle's positive cash floor is **$0**.

This remains true regardless of expected value or independence assumptions; no probability calculation is required.

## Closure gate

H281 does **not** claim the underlying lottery is exhausted. It closes only this checked mechanism:

`finite uncontrolled Virginia free instant games -> deterministic subsidy for a Pick 3 exact cover`.

Closure is valid because:
1. exact Pair-cover deficit is established;
2. current promotional worst-case cash floor is zero;
3. zero cannot clear the exact deficit;
4. execution/refusal clauses are therefore unnecessary to the core impossibility result.

Global state remains **NO SUCCESS; NOT EXHAUSTED**.
