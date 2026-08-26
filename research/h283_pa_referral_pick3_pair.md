# H283 — Pennsylvania iLottery referral bonus + PICK 3 Pair exact-cover lead

Date checked: 2026-08-26
Branch: `research-work`
Global state: **NO SUCCESS; NOT EXHAUSTED**

## Why this packet matters

This is materially stronger than H279/H280/H282 because the external subsidy is much larger relative to the required exact cover and the core bonus-to-cash bridge is stated in current Pennsylvania Lottery-controlled pages.

Current official Refer A Friend terms state that a referred new player who registers from the referrer's unique link, uses code `FRIEND`, and makes a first deposit of at least **$10** receives **$100 Bonus Money**. The same page states the bonus expires after 30 days and points to the PA iLottery Bonus Policy.

The current Bonus Policy states that Bonus Money may be used on **all Draw Games**, and that prizes won on Draw Games from Bonus Money wagers are paid **in cash regardless of remaining play-through requirement**. It also says cash is consumed before Bonus Money while a promotion is active.

Current PA Lottery PICK 3 material gives:
- Front Pair / Back Pair: 100 possible ordered pairs (`00` through `99`);
- $1 Pair play pays **$50**;
- $0.50 Pair play pays **$25**;
- current terminal operations guide: PICK 3 minimum $0.50 and **maximum value of one PICK 3 ticket $100**.

## Exact conditional construction

Use an eligible referred new account:
1. deposit **$10 cash**;
2. receive **$100 Bonus Money**;
3. before the same PICK 3 drawing, buy every Front Pair `00` through `99` once at **$1 each**;
4. total cover cost = **100 × $1 = $100**;
5. every possible three-digit result has exactly one front pair, so exactly one covered Pair wins;
6. fixed Pair prize = **$50 cash**.

Because cash is deducted first, the $100 cover consumes the $10 external deposit and $90 of Bonus Money. The remaining Bonus Money is irrelevant to the floor. If all 100 plays are accepted, the post-draw cash prize is at least **$50**, hence cash profit versus the only external deposit is:

`$50 - $10 = +$40`.

That is a **5.0x guaranteed cash gross / +400% profit ROI** versus the external cash deposit, conditional on complete acquisition.

The $0.50 version is also positive: $50 cover cost and $25 guaranteed cash prize => **+$15** versus the $10 deposit.

## What is already official / strong

- The $100 referred-player Bonus Money after $10+ first deposit is on the current official PA iLottery Refer A Friend page.
- The Bonus Policy explicitly permits Bonus Money on Draw Games and explicitly converts Draw Game prizes won from Bonus Money to cash despite unmet play-through.
- PICK 3 is currently sold online and starts at $0.50.
- Official current game material gives the fixed Pair prizes and exact 1-in-100 Pair outcome space.
- The 2026 terminal operations guide states a maximum value of **$100 for a single PICK 3 ticket**, numerically matching the $1 full Pair cover.

## Remaining rigorous execution gate

Do **not** call this global SUCCESS yet.

The missing public proof is specific: we have not established from an official online-system document or live authenticated checkout that **all 100 distinct Pair selections can be committed atomically in one PA iLottery online purchase for the same draw**, with no partial acceptance or online-specific line/cart restriction. The retail terminal guide's $100 single-ticket ceiling strongly supports feasibility but is not by itself proof of the online cart's atomic behavior.

The PA iLottery Bonus Policy also reserves discretion to cancel/suspend promotions and disqualify rule-violating/tampering participants. No checked text explicitly bans this exact cover, but a rigorous strategy should not infer execution entitlement beyond the published rules.

## Decision

**PROMISING CONDITIONAL SUCCESS LEAD; NOT YET RIGOROUS SUCCESS.**

This becomes a rigorous strategy for an otherwise eligible Pennsylvania player if the online complete-acquisition gate is established. The next action should focus on that narrow execution question rather than opening another broad bonus search immediately.

## Sources checked

Official PA iLottery current pages and PA Lottery 2026 game/terminal material:
- Refer A Friend page (`FRIEND`, $10 first deposit, $100 referred-player Bonus Money).
- PA iLottery Bonus Policy, especially current clauses 9 and 13.
- PA Lottery PICK 3 current game guide / page.
- WAVE-X Terminal Operations Guide 2026 PICK 3 section (single-ticket max $100).

Derived files:
- `src/loto_research/h283_pa_referral_pick3_pair.py`
- `data/derived/h283_pa_referral_pick3_pair.json`
