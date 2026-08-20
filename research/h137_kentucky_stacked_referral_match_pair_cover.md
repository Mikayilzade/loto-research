# H137 — Kentucky stacked referral + 100% first-deposit match + Pick 3 Pair cover

Updated: 2026-08-21
Status: **PROMISING STACKED-SUBSIDY MECHANISM / NOT TERMINAL SUCCESS**

## Question
Can the current August 2026 Kentucky Lottery Refer-a-Friend award be combined with the simultaneous 100% first-ever deposit match to reduce the external cash needed for the deterministic Pick 3 Pair cover identified in H136?

## Current official promotion overlap
Kentucky Lottery's current Promotions page simultaneously lists, for August 1–31, 2026:

1. **Refer A Friend** — a qualifying new referred player who successfully registers and deposits at least **$10** receives **$20 in Bonuses**. The page says the award is added within **5 business days** after the referred player completes the qualifying actions. Deposits cannot be withdrawn.
2. **First Ever Deposit 100 Percent Match** — a first-time deposit receives a **100% match up to $250** in Bonus funds.

Official source:
- https://www.kylottery.com/apps/promotions/promotions.html

The separate official 100%-match rules confirm that:
- the promotion is August 1–31, 2026;
- first-ever deposits receive a 100% Bonus match up to $250;
- the Bonus appears after the funding transaction;
- deposited funds cannot be withdrawn/refunded;
- Bonus funds must be spent on Kentucky Lottery online games.

Official rules:
- https://www.kylottery.com/export/kylmod/galleries/documents/KYLottery_terms/FINAL_Rules_100-FTD-Match-Aug-1-31.pdf

A current official Refer-a-Friend rules packet for the same $50/$20 structure requires a new referred player, the referral registration flow/promo code, and a deposit of at least $10; the referred player gets $20 Bonus. No explicit anti-stacking clause was located in the public material retrieved during this packet.

Important evidence limitation: simultaneous listing and absence of a located exclusion are **not proof that KLC will stack both awards on one account**. Stackability must remain a separate execution gate until an official rule/account confirmation explicitly establishes it.

## Deterministic Pair-cover identity from H136
Kentucky Pick 3 Pair has the same 60% deterministic coverage identity:
- 100 ordered pair outcomes;
- $0.50 per outcome;
- full face coverage = **$50**;
- exactly one covered pair wins;
- guaranteed gross payout = **$30**;
- base deterministic return = **60%**.

## Stacked-subsidy arithmetic
Let external first deposit be `d`, with `10 <= d <= 250`.

If both current player-owned awards stack:
- deposit purchasing balance = `d`;
- first-deposit Bonus = `d`;
- referral Bonus = `$20`;
- total usable online lottery purchasing power = `2d + 20`.

To fund the $50 Pair cover:

`2d + 20 >= 50`

so

`d >= 15`.

At the minimum `d = $15`:
- external cash committed = **$15**;
- first-deposit Bonus = **$15**;
- referral Bonus = **$20**;
- total purchasing power = **$50**;
- deterministic Pair-cover gross payout = **$30**;
- conditional pre-tax surplus over external cash = **+$15**;
- conditional pre-tax ROI on external cash = **+100%**.

This is materially stronger than H136's unstacked Pair cover (`$25 cash + $25 Bonus -> $30 payout -> +$5`).

## Why this still is NOT SUCCESS
### Gate A — stackability is not yet contractually locked
The two offers are concurrently published and their retrieved public summaries do not show an incompatibility clause, but this packet did not recover an authoritative sentence that guarantees both awards to the same referred first-depositor.

Therefore `$15 -> $50 purchasing power` is a **conditional theorem**, not yet an executable guarantee.

### Gate B — referral Bonus timing worsens pre-commitment risk
The current promotions page says referral Bonuses may be added within **5 business days** after the qualifying actions. The external deposit is non-withdrawable during that period.

Thus even if both promotions ultimately stack, the player cannot atomically lock:

`deposit -> both Bonuses -> complete Pair basket`

before the external cash is committed.

### Gate C — complete-basket acceptance remains uncommitted
Kentucky iLottery terms reserve the right to limit game purchases and wagers on particular number sets without notice. H136 already established that there is no public operator commitment to accept the entire deterministic basket before funding becomes irreversible.

Reducing the cover from 1,000 Straight wagers to 100 Pair wagers improves operational practicality but does not remove the legal branch where one or more required selections are refused.

### Gate D — tax remains non-universal
The margin is much larger relative to external cash than H136, but terminal SUCCESS still requires a taxpayer-specific after-tax floor or a rule showing the applicable tax treatment cannot consume the $15 surplus.

## Strong conditional theorem
If, before the $15 external deposit becomes irrecoverable, all of the following are guaranteed:
1. the player is a qualifying new referred player;
2. the current $20 referral Bonus and 100% first-deposit Bonus are stackable on the same account;
3. a $15 first deposit deterministically produces both the $15 match and $20 referral Bonus;
4. all 100 required $0.50 Pair selections for the same draw are accepted;
5. Bonus-funded winning proceeds are withdrawable ordinary winnings;
6. taxes/fees on the complete transaction are < $15;

then the transaction has a strict positive net cash floor of more than $0, with a pre-tax floor of **+$15**.

## Result
- **Simultaneous August promotion overlap: VALIDATED.**
- **Stacked subsidy arithmetic: VALIDATED conditionally.**
- **Minimum external cash for Pair cover if stackable: $15.**
- **Conditional pre-tax guaranteed payout: $30, surplus +$15 / +100% external-cash ROI.**
- **Terminal SUCCESS: NOT ESTABLISHED** because stackability, award timing, complete-basket pre-acceptance and tax are not locked before the non-withdrawable deposit.

## Highest-value next checks
1. Obtain an authoritative August 2026 Refer-a-Friend rules file and search specifically for anti-stacking / one-promotion / promo-code exclusions.
2. Search KLC account/offer documentation for explicit concurrent-promotion stacking behavior.
3. Search for a cart/batch/system mechanism that accepts all 100 Pair selections atomically before settlement/funding.
4. Search other state lotteries for the same >=100% deterministic deposit subsidy where cash remains withdrawable; that would remove the fatal H136/H137 funding-order branch.
