# H289 independent validation

Validated: 2026-08-26
Verdict: **conditional positive arithmetic; NOT rigorous success**

## H225 guard
- `research/H225_EXACT_STATUS.md` remains terminal: H225-X20 left 0 coefficient survivors and 0 legal shift tuples after the full 44-shard / 11-sector / 306,450-state exact rescreen.
- No X21/X22 work was created.

## Spot-1 exact certificate
1. Kentucky Keno draws exactly 20 distinct numbers from 80.
2. Cover consists of exactly 80 $1 Spot-1 plays, one for each possible number.
3. Therefore exactly 20 cover plays win in every legal draw.
4. Official base Spot-1 payout is $2 for a one-number match.
5. Guaranteed gross = `20 * $2 = $40`.
6. Conditional promo funding = `$30 cash + $30 first-deposit match + $20 referral = $80`.
7. Conditional profit versus external cash = `$40 - $30 = +$10`.

## Spot-2 independent certificate
1. Partition sizes: `[14,14,13,13,13,13]`, total 80.
2. Buy all internal pairs: `2*C(14,2)+4*C(13,2)=494` plays.
3. For 20 drawn numbers, convexity/balancing minimizes internal drawn pairs at distribution `4,4,3,3,3,3`.
4. Guaranteed winning pairs = `2*C(4,2)+4*C(3,2)=24`.
5. Official Spot-2 base payout is $11 for two matches.
6. Guaranteed gross >= `24*$11=$264`.
7. Conditional funding = `$237 cash + $237 match + $20 referral = $494`.
8. Conditional profit versus external cash >= `$264-$237=+$27`.

## Gates that prevent SUCCESS
- The checked official August 2026 material does not explicitly establish that the $20 Refer-A-Friend award may be stacked with the 100% first-deposit match on the same account.
- Kentucky iLottery Terms reserve the right to refuse attempted purchases and to limit wagers on particular number sets without notice. Hence complete same-draw acquisition of all required selections is not guaranteed.

No claim of guaranteed executable profit is valid until both gates are removed by authoritative evidence or a different execution mechanism.
