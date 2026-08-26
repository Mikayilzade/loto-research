# H283 EXECUTION CLOSURE — 2026-08-26

State: **CLOSED / EXECUTION-BLOCKED**

## Result

The Pennsylvania referral-bonus arithmetic remains correct, but the strict guaranteed-profit construction is not certifiable because the governing PICK 3 game notice gives the Pennsylvania Lottery an explicit right to stop play on any number or combination of numbers at any time during the game.

This is stronger than the previously open online-cart/atomicity question: a complete Front Pair cover requires acquisition of every ordered pair `00`-`99`. If the Lottery may stop play on even one required number/combination before acquisition completes, there exists a legal execution path in which the portfolio is incomplete. Any incomplete Front Pair cover has at least one legal draw outcome paying zero from the Pair portfolio. Therefore the proposed guarantee fails under the published rules even if the online cart itself were otherwise atomic.

## Authoritative rule evidence

Pennsylvania Bulletin, PICK 3 Terminal-Based Lottery Game, 45 Pa.B. 386 (Jan. 17, 2015), section 7(d):

> The Lottery reserves the right to stop play on any number or combination of numbers at any time during the course of the PICK 3 game.

Source:
- https://www.pacodeandbulletin.gov/Display/pabull?file=%2Fsecure%2Fpabulletin%2Fdata%2Fvol45%2F45-3%2F110.html

The 2016 Wild Ball amendment preserved an analogous stop-play authority for combinations played with Wild Ball; it does not remove the base-game section 7(d) authority.

Source:
- https://www.pacodeandbulletin.gov/Display/pabull?file=%2Fsecure%2Fpabulletin%2Fdata%2Fvol46%2F46-36%2F1528.html

## Previously established positive arithmetic

For an eligible referred new player under the checked 2026 offer:
- external first deposit: `$10`;
- referral Bonus Money: `$100`;
- intended full PICK 3 Front Pair cover: 100 distinct `$1` plays, `00`-`99`;
- full-cover spend: `$100`;
- every completed full cover pays exactly one `$50` Front Pair prize;
- conditional cash profit versus the external deposit: `+$40`.

The arithmetic is not the blocker. Complete deterministic acquisition is.

## Additional lower-line-count attempt: PICK 2 Front Digit / Back Digit

A fresh search tested whether the same referral bonus could avoid the 100-selection execution problem by using PICK 2.

Current official PA Lottery material confirms:
- PICK 2 is playable online;
- FRONT DIGIT and BACK DIGIT are supported;
- each costs `$1` per play;
- each wins `$5` with probability 1/10 for a single digit.

Thus a complete ten-digit Front Digit cover `0`-`9` costs `$10` and guarantees `$5`; ten such complete draw/position covers bought with the `$100` bonus would guarantee `$50` cash, again `+$40` versus the `$10` external deposit.

However the governing PICK 2 notice contains the same blocker. Pennsylvania Bulletin 45 Pa.B. 384, section 7(d):

> The Lottery reserves the right to stop play on any number or combination of numbers at any time during the course of the PICK 2 game.

Source:
- https://www.pacodeandbulletin.gov/Display/pabull?file=%2Fsecure%2Fpabulletin%2Fdata%2Fvol45%2F45-3%2F109.html

So reducing the cover from 100 Pair selections to 10 Digit selections does not restore a rigorous guarantee.

## Closure logic

For both PICK 3 Pair and PICK 2 Digit subsidy constructions:

1. strict profit requires a complete finite cover;
2. published game rules expressly allow the Lottery to stop play on a required number/combination;
3. therefore complete acquisition is not guaranteed by the rules;
4. an incomplete cover admits a legal zero-return result for that cover;
5. conditional positive arithmetic cannot be promoted to a worst-case guaranteed-profit theorem.

H283 is therefore **CLOSED / EXECUTION-BLOCKED**. Do not reopen merely on evidence of large online carts or multi-play checkout. Reopen only if a later authoritative rule/offer removes or overrides the relevant stop-play authority, or if a different deterministic subsidy construction does not require complete acquisition of a stoppable number set.
