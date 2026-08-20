# H139 — Kentucky concurrent deposit-promo stack + Pick 3 Pair coverage

Updated: 2026-08-21
Status: **MULTI-PROMO CONDITIONAL FLOOR IMPROVED / STACKABILITY + PRE-ACCEPTANCE STILL UNLOCKED / NOT SUCCESS**

## Question
H136 proved that the current August 2026 Kentucky Lottery 100% first-deposit match is large enough to make exact Pick 3 Pair coverage pre-tax positive if the full wager basket is accepted. H137 added the concurrent $20 Refer-a-Friend award conditionally.

This packet tests whether other **simultaneously live Kentucky deposit promotions** can stack on the *same first-ever deposit* and materially increase the deterministic margin enough to survive friction/tax uncertainty.

## Current official promotion set
Kentucky Lottery's official Promotions page currently lists all of the following during August 2026:

1. **First Ever Deposit 100 Percent Match** — 100% first-deposit match up to $250, Aug 1–31, 2026.
2. **Tiki Tuesday** — deposit $150 or more in one transaction on Aug 4/11/18/25 and receive $50 in Bonuses.
3. **Summer Fridays** — 25% deposit match up to $50 on Aug 7 and Aug 21, 3:00–5:00 PM ET.
4. **Refer A Friend** — qualifying referred new player who registers and deposits at least $10 receives $20 in Bonuses; award may take up to 5 business days.
5. **Registration Offer** — $5 Bonus for a new Fun Club registration, but the current page expressly says this $5 is to play **Instant Play games**, so it is not counted toward the Pick 3 draw-game floor.

Official current promotion page:
- https://www.kylottery.com/apps/promotions/promotions.html

Official August 100% first-deposit rules:
- https://www.kylottery.com/export/kylmod/galleries/documents/KYLottery_terms/FINAL_Rules_100-FTD-Match-Aug-1-31.pdf

Official current Terms of Use / iLottery terms:
- https://www.kylottery.com/apps/funclub/terms.html?pane=terms

Official current/adjacent Refer-a-Friend rules source recovered:
- https://www.kylottery.com/export/kylmod/galleries/documents/KYLottery_terms/FINAL_Rules_Refer-a-Friend-Promotion-July-UPDATED-4.29.26-1.pdf

The promotion page shows these offers concurrently and no anti-stacking sentence was located in the retrieved public summaries/rules. **Absence of an exclusion is not proof of stackability**, so every multi-promo result below remains conditional until KLC explicitly confirms simultaneous award eligibility on one deposit/account.

## Deterministic coverage unit
From H136, one complete Pick 3 Pair partition is:
- 100 ordered Pair outcomes;
- $0.50 each;
- face spend = **$50**;
- exactly one Pair wins in every draw;
- fixed gross prize = **$30**;
- strict deterministic gross-return ratio = **60%**.

For usable draw-game balance `B`, the number of complete Pair partitions that can be funded is:

`k = floor(B / 50)`

and the deterministic gross cash prize floor is:

`G = 30*k`.

Any leftover balance below $50 is assigned zero guaranteed cash value in the strict floor.

## A. First-deposit match only — control
With external deposit `d` and 100% match:

`B = 2d`.

Minimum exact one-partition state: `d = $25`.

- balance $50;
- payout floor $30;
- pre-tax surplus vs external cash = **+$5**;
- ROI = **+20%**.

This reproduces H136 Pair-cover control.

## B. First-deposit match + Refer-a-Friend
If both awards stack:

`B = 2d + 20`.

Minimum full Pair partition at `d = $15`:
- balance $50;
- payout $30;
- surplus **+$15**;
- ROI **+100%**.

This reproduces H137 and remains the strongest low-capital conditional state.

## C. First-deposit match + Tiki Tuesday
On the remaining Aug 25 Tiki Tuesday window, if the same first deposit receives both awards:

`B = 2d + 50`, for `150 <= d <= 250`.

Because only complete $50 Pair partitions count, the best absolute tested state in the permitted first-match range is:

`d = $250 -> B = $550 -> k = 11 -> G = $330`.

Conditional pre-tax surplus:

`$330 - $250 = +$80` (**+32%** on external cash).

At the minimum qualifying Tiki deposit:

`d = $150 -> B = $350 -> k = 7 -> G = $210 -> +$60` (**+40% ROI**).

Thus Tiki Tuesday would materially increase the dollar safety margin from H136's +$5 Pair case to as much as **+$80 pre-tax**, if simultaneous award eligibility is guaranteed.

## D. First-deposit match + Summer Friday
Current page lists a 25% deposit match up to $50 on Aug 21, 2026, 3:00–5:00 PM ET.

If the first-ever deposit simultaneously receives the 100% first-deposit match and Summer Friday award:

`B = 2d + min(0.25d, 50)`.

At `d = $250`:
- first match $250;
- Summer bonus $50 (cap);
- total balance $550;
- 11 complete Pair covers;
- deterministic payout floor $330;
- conditional pre-tax surplus **+$80**.

For `d <= 200`, the uncapped combined subsidy ratio is 125% of deposit (`B=2.25d`), so the theoretical continuous floor ratio before $50 partition granularity is `0.60*2.25 = 1.35`, i.e. **35% pre-tax margin**.

## E. First-deposit match + $50 deposit promo + Refer-a-Friend
If either Tiki Tuesday or capped Summer Friday $50 award also stacks with the $20 referred-friend Bonus:

`B = 2d + 70`.

Discrete $50 coverage granularity creates the best tested absolute margin at `d = $240`:
- balance = `$480 + $70 = $550`;
- 11 complete Pair covers;
- payout floor = **$330**;
- external cash = **$240**;
- conditional pre-tax surplus = **+$90**;
- conditional ROI = **+37.5%**.

A larger $250 deposit leaves $20 unusable for a strict complete Pair partition, so its floor falls to +$80.

This **+$90** is the largest current Kentucky deterministic pre-tax cover margin found so far under public concurrent-promotion assumptions.

## Registration $5 is excluded from the draw-game theorem
The current Kentucky promotions page says the Registration Offer gives a $5 Bonus to play **Instant Play games**. Although nearby generic text says Bonuses are used on games purchased online, the specific offer description is narrower. The strict Pick 3 coverage theorem therefore assigns this $5 zero draw-game value.

This avoids overstating the subsidy.

## Stackability evidence and blocker
### Evidence supporting possible stacking
- All offers are simultaneously listed on the same official Promotions page.
- First-deposit match eligibility is triggered by a first-ever deposit.
- Tiki Tuesday/Summer Friday eligibility is separately triggered by a qualifying deposit in the specified window.
- Refer-a-Friend eligibility is separately triggered by new registration/referral code + deposit requirement.
- No explicit clause saying `not combinable with other offers`, `one offer per deposit`, or equivalent was located in the retrieved public terms.

### Why this is still not proof
KLC's general terms make promotional offers subject to specific promotion rules and reserve broad rights to modify/cancel promotional offers. Public coexistence plus compatible trigger language does not create an explicit promise that one funding transaction will receive multiple awards.

Terminal use therefore requires one of:
1. official rules explicitly saying the offers may be combined;
2. official KLC written confirmation for the exact account/deposit sequence; or
3. an account UI that pre-displays all simultaneous awards as locked before funding confirmation.

Without one of these, the +$80/+90 floors are conditional only.

## Pre-acceptance blocker remains fatal
Even if stacking is fully confirmed, the main H136/H138 execution failure remains:
- deposited money is non-withdrawable;
- Bonus funds arrive after funding;
- KLC terms reserve the right to refuse an attempted purchase and limit purchases/wagers on particular numbers without notice;
- the online Shopping Cart is not a contractual reservation of all 100 Pair selections.

Therefore there remains a lawful branch:

`deposit committed -> bonuses credited -> one or more required Pair wagers refused`.

That branch destroys the deterministic all-outcome prize floor after external cash has already become irreversible.

The larger subsidy margin does **not** cure this binary completeness problem.

## Tax gate
The larger conditional margin (+$60 to +$90 rather than +$5/+15) makes tax/friction survival more plausible, but terminal SUCCESS still requires taxpayer-specific treatment. No universal after-tax positive floor is asserted.

## Result
- **Current concurrent Kentucky deposit promotions: VALIDATED.**
- **Tiki Tuesday + first-deposit conditional cover: up to +$80 pre-tax floor.**
- **Summer Friday + first-deposit conditional cover: up to +$80 pre-tax floor.**
- **Either $50 deposit promo + referral + first-match: discrete optimum tested at +$90 pre-tax.**
- **Registration $5 correctly excluded from Pick 3 because current offer is Instant-Play-specific.**
- **Stackability: NOT CONTRACTUALLY PROVEN.**
- **Complete-basket acceptance before irreversible funding: STILL NOT LOCKED.**
- **Terminal SUCCESS: NOT ESTABLISHED.**

## Next highest-value checks
1. Recover exact Tiki Tuesday and Summer Friday rule documents or official KLC confirmation and test explicit multi-offer stacking.
2. Search state lottery systems where a bonus is displayed/locked before deposit submission, or deposited principal remains withdrawable before play.
3. Search batch/system Pick 3 interfaces or pre-authorized order mechanisms that atomically accept an entire Pair partition before funds are committed.
4. Search compact fixed-prize games with coverage ratio >60%, because the same subsidy stack would create even wider deterministic margins and fewer required wagers.
