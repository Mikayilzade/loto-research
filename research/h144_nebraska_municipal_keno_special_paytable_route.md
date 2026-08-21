# H144 — Nebraska municipal Keno special-paytable / free-play route

Updated: 2026-08-21
Status: **PROMISING CURRENT STRUCTURAL CLASS / CURRENT >75% PAYTABLE NOT YET CAPTURED / NO SUCCESS**

## Why this packet matters
H143 established Virginia Keno 1-Spot as the best verified current compact deterministic cover at 75%, which means a pre-owned subsidy above 25% is needed. Nebraska county/city keno has a materially different legal architecture: local operators may run special prize schedules and free-play promotions inside the regulated lottery itself. That creates a new route where the cover ratio may be improved directly by the paytable, potentially avoiding the separate-wallet-bonus execution problem.

## Current primary-source facts
Nebraska Department of Revenue Chapter 35 (County/City Lottery / Keno) currently provides:

- free-play keno coupons, gift certificates and similar promotional items may be used for keno play if their face amount is included in gross proceeds (Reg. 35-613.02C(3));
- the retail value of free keno play is treated as a promotional expense when reimbursed by the county/city/village (Reg. 35-613.02C(3)(a));
- the potential payout for each wager type must be made known before number selection (Reg. 35-613.03H);
- the keno system may support paytable updates, and regulatory text expressly identifies pre-programming of **special prize payouts conducted periodically by the lottery operator** as a paytable modification (Reg. 35-614.05);
- prize funds must be secured and prizes paid in full; fixed prizes therefore are not merely promotional promises (Reg. 35-613.11);
- accepted wagers are documented by an outside ticket and transaction log before the game closes (Reg. 35-613.03B), giving a much cleaner execution-lock architecture than H136 Kentucky's post-deposit uncertain basket acceptance.

Primary source:
- https://revenue.nebraska.gov/about/legal-information/regulations/chapter-35-keno

## Current operator evidence
Big Red Keno's current official site (copyright 2026) states that it broadcasts live keno to more than 260 locations on the home page and its current locations page says play is available every five minutes at **more than 295 bars and grills in Nebraska**. Its current promo page explicitly directs players to check the keno special running in their community.

Official current pages:
- https://bigredkeno.com/
- https://bigredkeno.com/locations
- https://bigredkeno.com/promos

The public site currently exposes the existence of active community specials but the exact live pay schedules are image/location dependent and were not recoverable as reliable machine-readable text in this run.

## Deterministic-cover theorem for Nebraska Pick 1
Standard 80-number / 20-draw keno Pick 1 has a simple partition cover:

- buy all 80 distinct numbers at stake `w`;
- total face cost = `80w`;
- exactly 20 selections win every draw;
- if the fixed winning payout is `p*w` (gross, including stake if rules quote that way), deterministic gross = `20*p*w`;
- deterministic cover ratio = `p/4`.

Therefore:

| Pick-1 gross payout multiple p | Deterministic cover ratio | Subsidy needed for >100% |
|---:|---:|---:|
| 2.00 | 50.00% | >50.00% |
| 3.00 | 75.00% | >25.00% |
| 3.25 | 81.25% | >18.75% |
| 3.50 | 87.50% | >12.50% |
| 3.75 | 93.75% | >6.25% |
| 4.00 | 100.00% | >0% (break-even before costs/tax) |
| >4.00 | >100% | direct pre-tax deterministic overlay |

This creates two concrete monitor triggers:
1. any current special Pick-1 schedule paying **>4-for-1 gross** on a freely selectable 80-number cover would be an immediate pre-tax deterministic positive overlay before tax/limits;
2. any schedule in the 3.25–4.00 range sharply lowers the required pre-owned free-play subsidy compared with Virginia's 25% hurdle.

## Execution advantages versus H136 Kentucky
Nebraska's regulated ticket flow is structurally stronger for a guarantee search:
- prize schedule is known before number selection;
- wager acceptance is evidenced by the printed/electronic outside ticket;
- player can verify the accepted selections before the draw closes;
- free-play coupons are expressly recognized in regulation;
- special paytables are an expressly contemplated operator mechanism.

This means a candidate can be tested using the sequence:

`observe posted special paytable -> obtain/verify coupon if any -> submit complete cover -> receive outside tickets proving all selections accepted -> only then let game close`.

That solves the specific H136 problem where external money became nonwithdrawable before complete cover acceptance could be locked.

## Remaining blockers
1. **No current exact special paytable >75% has been captured yet.** Big Red's public promo page confirms community specials but not the numeric schedules in retrievable text.
2. Aggregate prize payout limits may apply. Any candidate must verify the posted limit against the deterministic cover payout before purchase.
3. Free-play promotions may be locally funded/limited and are not assumed available or stackable until a current coupon/rule is captured.
4. U.S. tax treatment must still be included in terminal SUCCESS; a small pre-tax edge is insufficient.
5. Physical presence / local execution and any per-ticket or per-game wager restrictions must be checked for the specific city/operator.

## Result
- **New current lottery-specific structural class VALIDATED:** Nebraska municipal keno allows periodic special paytables + free-play coupons inside a regulated fixed-prize framework.
- **Current Big Red community-special infrastructure VALIDATED.**
- **Direct >75% candidate NOT YET VALIDATED** because the live special numeric paytable is not publicly captured in reliable text.
- **Terminal SUCCESS: NO.**

## Next action
1. Capture current numeric special paytables for Big Red communities (Omaha, Lincoln, Norfolk, Fremont, Blair, Beatrice, Valley, etc.) from official posters/pay schedules or location-posted schedules.
2. Compute exact deterministic cover ratio for every special, prioritizing Pick 1 and partitionable Top/Bottom or color-group games.
3. Trigger immediate execution analysis on any `r > 0.75`; trigger direct SUCCESS-candidate analysis on any fixed `r > 1.00` before tax/costs.
4. Capture current free-play coupon face values and whether they can be used across all selections in a complete cover.
5. Verify aggregate payout limit before declaring any candidate executable.
