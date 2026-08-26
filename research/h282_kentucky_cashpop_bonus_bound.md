# H282 — Kentucky CASH POP + August 2026 deposit-bonus bound

Date checked: 2026-08-26
Branch: `research-work`
State: **CLOSED / NO STRICT GUARANTEED-PROFIT FLOOR**

## Why this was opened

H279 showed that Kentucky's current 100% first-deposit match can cross 100% arithmetic for a Pick 3 Pair cover, but the large all-number purchase remains execution-fragile because KLC can refuse purchases / limit number exposure.

CASH POP is materially different and worth a separate packet: the official game exposes a native `Cover All` option for all fifteen numbers, so the player does not need to build a 100-line Pick 3 cart manually. The question is whether the current deposit subsidy is large enough for that small native complete cover.

## Current official promotion

Kentucky Lottery's promotions page currently advertises `First Ever Deposit 100 Percent Match`: eligible first-time depositors receive a 100% match up to $250 during August 1-31, 2026. Bonuses expire after 30 days.

The same page also lists current August deposit offers, including $50 in Bonuses for a qualifying $150 Tiki Tuesday deposit and a 25% match (up to $50) on specified Summer Fridays. H282 deliberately gives the player favorable stacking in the sensitivity checks below even though strict combinability is not needed for the rejection.

Kentucky iLottery Terms state that deposits and Bonuses are tracked separately from prize winnings; deposits and Bonuses cannot be withdrawn, while eligible prize winnings may be withdrawn.

## Exact CASH POP mechanics

Official CASH POP rules:
- winning number is one of 1..15;
- player may select all fifteen numbers using `Cover All`;
- permitted stake per selected number is $1, $2, $5 or $10;
- the ticket computer assigns a prize amount to each played number before the draw;
- minimum published prize amounts are respectively $5, $10, $25 and $50.

Thus every permitted wager has a legal minimum-prize assignment equal to exactly **5x its stake**.

## Portfolio-wide proof

Consider any nonnegative CASH POP portfolio for one draw. Let `s_i` be total stake placed on number `i`.

If some number is uncovered, that number can legally win and the portfolio receives $0, so a strict guarantee requires all fifteen `s_i > 0`.

Now select the legal branch in which every played number receives its minimum published prize. If number `i` wins, gross payout is exactly `5*s_i`. Hence

`worst_case_gross = 5 * min_i(s_i)`.

But

`min_i(s_i) <= (sum_i s_i)/15`.

Therefore

`worst_case_gross <= (5/15) * total_game_spend = total_game_spend / 3`.

This is not merely a Cover-All-ticket calculation. It bounds **every nonnegative CASH POP portfolio**, regardless of ticket grouping, stake mixture, repeated numbers, or multiple draws. For multiple draws, the adversarial minimum-prize / least-covered-number argument applies draw by draw and adds.

## Interaction with the 100% match

A 100% match supplies at most $2 of playable balance per $1 of deposited cash. Spending all of it in CASH POP therefore has strict withdrawable-prize ceiling

`2 * (1/3) = 2/3 = 66.6667%`

of the original cash deposit.

At the maximum $250 match:
- cash deposit: $250;
- playable wallet: $500;
- strict CASH POP prize-floor upper bound: $166.67;
- unrecovered cash: at least $83.33.

So the current 100% match cannot produce strict positive cash profit through CASH POP, even if every purchase is accepted atomically.

## Stronger favorable stacking checks

### Tiki Tuesday

Deliberately grant both current offers on a $150 first deposit:
- cash deposit $150;
- +$150 first-deposit match;
- +$50 Tiki bonus;
- playable balance $350.

CASH POP strict prize-floor ceiling = `$350 / 3 = $116.67`, still below the $150 deposited cash. Cash recovery ceiling: **77.7778%**.

### Summer Friday

Deliberately grant both the 100% first-deposit match and 25% Friday match. This yields 2.25x playable funds per cash dollar. The CASH POP floor ceiling is therefore

`2.25 / 3 = 75%`

of deposited cash, also below break-even.

These stronger-than-required assumptions make the rejection robust to ordinary uncertainty about whether the promotions can stack.

## Conclusion

**H282 is closed.** Kentucky CASH POP's native 15-number `Cover All` solves the cart-size problem but not the economics. Under the published prize table, its universal worst-case gross is at most one-third of playable spend. The current 100% first-deposit match, and even the checked favorable August stacking scenarios, cannot lift withdrawable prize winnings to the original cash deposit.

Reopen only if a deterministic subsidy exceeds **200% of deposited cash** for funds usable on CASH POP, or if the minimum CASH POP prize multiple / number count changes enough to push the exact bound above cash break-even.

## Reproducible files

- `src/loto_research/h282_kentucky_cashpop_bonus_bound.py`
- `data/derived/h282_kentucky_cashpop_bonus_bound.json`
- `research/H282_VALIDATION.md`
- `research/H282_STATUS.md`
