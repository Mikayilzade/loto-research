# H314 VALIDATION — WinWink £50k COIN FLIP

Validated: 2026-08-27
Result: **CLOSED / ZERO STRICT CASH FLOOR**

## Independent arithmetic checks

Published/live quantities used:

- total ticket positions = 142,857;
- committed instant-win positions = 71,428;
- total losing positions = 71,429;
- sold = 1,615;
- instant wins remaining = 70,598;
- instant wins already consumed = 830;
- sold losing positions = 785;
- remaining tickets = 141,242;
- remaining losing positions = 70,644;
- one-player cap = 21,429.

Assertions:

1. `71,428 + 71,429 = 142,857`.
2. `830 + 70,598 = 71,428`.
3. `785 + 830 = 1,615`.
4. `70,644 + 70,598 = 141,242`.
5. `70,644 - 21,429 = 49,215 > 0`.

## Logical gate

The operator states that instant-winning ticket positions are selected, encrypted and sealed before sales, are not readable before purchase, and are revealed when tickets are bought. Thus the player cannot target the hidden winning positions in advance.

Since the remaining losing inventory is larger than the entire permitted one-player portfolio, there is at least one legal realization in which every permitted player ticket is a loser.

Therefore:

**strict guaranteed instant-win cash floor = £0.**

No assumption about expected value, independence, normal approximation, or long-run frequency is used.

## Source

Live operator page checked on 2026-08-27:
https://winwink.co.uk/competitions/50k-coin-flip

The page published the cap, ticket count, sold count, remaining instant-win count, commitment hash, and description of the precommit/reveal mechanism.
