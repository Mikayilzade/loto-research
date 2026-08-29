# H351 — Massachusetts Megabucks high-jackpot full-cover duplicate stress

## Question
Can the current unusually high Massachusetts Megabucks jackpot turn a complete 6/44 cover into a strict guaranteed-profit portfolio?

## Current rules/evidence
Massachusetts Lottery currently publishes Megabucks as a 6-from-44 game at $2 per play, with fixed lower prizes of $5,000 for Match 5, $200 for Match 4, and $4 for Match 3. The jackpot is shared equally among all jackpot-winning tickets. The official game page also states that approximately 61.79% of wagers enter the prize pool, and that lower prizes are paid before remaining prize-pool money goes to the jackpot.

For the 2026-08-29 drawing, current public result services report an estimated jackpot of $28.6m.

Sources checked 2026-08-29:
- https://www.masslottery.com/games/megabucks
- https://www.law.cornell.edu/regulations/massachusetts/961-CMR-2-53
- https://www.lotterypost.com/results/ma/megabucks

## Exact complete-cover arithmetic
There are

`C(44,6) = 7,059,052`

possible lines. At $2 each, a one-copy complete cover costs **$14,118,104**.

For any drawn six-number set, the number of cover lines matching exactly k draw numbers is `C(6,k) C(38,6-k)`. Exact multiplicities are:
- k=6: 1
- k=5: 228
- k=4: 10,545
- k=3: 168,720
- k=2: 1,107,225
- k=1: 3,011,652
- k=0: 2,760,681

These sum exactly to **7,059,052**, so partition inconclusive = 0.

Fixed lower-tier gross is:
- 228 × $5,000 = $1,140,000
- 10,545 × $200 = $2,109,000
- 168,720 × $4 = $674,880
- total = **$3,923,880**.

At the advertised $28.6m annuity jackpot and with no external jackpot duplicate, nominal gross is **$32,523,880**, comfortably above the cover cost. So this candidate genuinely passes the isolated arithmetic gate.

## Duplicate stress
The strict guarantee must survive legal external winners. Current rules explicitly share the jackpot equally among all winning jackpot tickets and provide no hard cap on how many external copies of the winning line may exist.

To avoid understating the candidate, grant an impossible-favourable upper bound: pretend **100% of our $14,118,104 stake is added to the jackpot** before sharing. This dominates the actual stated 61.79% prize-pool contribution and also ignores the fact that lower prizes consume pool money.

Dominating jackpot = `$28,600,000 + $14,118,104 = $42,718,104`.

With e external jackpot duplicates, gross is upper-bounded by:

`$3,923,880 + $42,718,104/(e+1)`.

For e=3, this is $14,603,406, still $485,302 above cost. For e=4, it falls to **$12,467,500.80**, which is **$1,650,603.20 below cost**.

Because four external copies of one six-number line are not prohibited or hard-capped by the checked rules, this is a legal below-cost branch. Any real prize-pool accounting, cash-option discount, taxes, acquisition friction, or lower-prize scaling can only weaken the portfolio relative to this deliberately favourable stress.

## Closure
**NO strict guaranteed profit.** This is nevertheless a strong near-candidate: the isolated full-cover state is >100%, and the decisive blocker is external top-tier dilution rather than poor base arithmetic.

Arithmetic inconclusive: 0.  
Closure-relevant inconclusive: 0.

## Next gate
Search for high-jackpot/full-cover or special-event games where the top reward is non-shareable per winning selection, duplicate ownership is structurally impossible, or external duplicates are hard-capped below the exact break-even threshold.
