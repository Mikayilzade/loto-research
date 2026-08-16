# H035 — Lotterywest compact fixed-odds games: Super66 + Cash 3

Updated: 2026-08-16
Status: **both standalone guarantee paths rejected**

## Why this packet
After many large combination-space screens, test two compact Western Australia products where full/near-full coverage is computationally exact and current official mechanics are public.

Primary current operator sources:
- Super66: https://www.lotterywest.wa.gov.au/games/super66
- Cash 3: https://www.lotterywest.wa.gov.au/games/cash-3

## 1. Super66
Current Lotterywest page states:
- AUD 1 per game;
- six digits 0–9 in order;
- Division 1 odds 1 in 1,000,000;
- Division 1 pays balance of prize pool, minimum AUD 66,666;
- Division 2/3/4/5 fixed prizes AUD 6,666 / 666 / 66 / 6.60;
- matches may come from either end; if multiple divisions/end matches occur only the larger prize is paid;
- crucial execution rule: **numbers are automatically randomly selected when a ticket is purchased**.

### Hypothetical unique full-space identity
Normalize the winning six-digit string to `000000` by digit symmetry and enumerate all 1,000,000 possible six-digit strings. Classify each string by the longest consecutive match from either end, applying the operator's one-largest-prize rule.

Exact counts:
- Division 1 (6): 1
- Division 2 (5): 18
- Division 3 (4): 180
- Division 4 (3): 1,800
- Division 5 (2): 17,901

At the statutory minimum Division-1 payout, a hypothetical portfolio containing every six-digit string exactly once would cost AUD 1,000,000 and return:

`66,666 + 18*6,666 + 180*666 + 1,800*66 + 17,901*6.6 = AUD 543,480.60`

Minimum-payout gross-return ratio: **54.34806%**.

This is already far below cost, but the more important strict-guarantee obstruction is execution: Lotterywest says Super66 numbers are automatically randomly selected. The player cannot construct the exact unique 1,000,000-string cover. Any finite collection of independently/randomly assigned games can contain duplicates and omit at least one possible winning string with nonzero probability. Therefore ticket count alone cannot create an all-outcome guarantee.

A large accumulated Division-1 jackpot may raise expected value, but does not repair the inability to force complete unique coverage. This branch can only reopen if an authoritative mechanism appears that lets a player deterministically select/obtain a complete permutation of all one-million strings, or another deterministic subsidy changes the acquisition economics.

Status: **REJECTED as executable guaranteed-profit coverage**.

## 2. Cash 3
Current Lotterywest page describes a fixed-odds daily game with these base payouts:
- Exact Order: AUD 0.50 -> AUD 250; AUD 1 -> AUD 500; odds 1/1,000.
- Any Order 3-way (two equal digits, e.g. 223): AUD 0.50 -> AUD 80; AUD 1 -> AUD 160; odds about 1/333.33.
- Any Order 6-way (three distinct digits, e.g. 123): AUD 0.50 -> AUD 40; AUD 1 -> AUD 80; odds about 1/166.67.
- Both Ways is also offered, but it is simply exposure to Exact + Any Order and does not create a documented deterministic discount.

### Exact partition cover of all 1,000 ordered draw outcomes
At the AUD 0.50 stake, cover the outcome space by its multiplicity class:
1. 10 all-equal outcomes (`000`, `111`, ...): buy 10 Exact wagers.
2. 270 ordered outcomes containing one pair: there are 90 unordered 3-way patterns, buy each once as Any Order 3-way.
3. 720 ordered all-distinct outcomes: there are `C(10,3)=120` unordered 6-way patterns, buy each once as Any Order 6-way.

Portfolio:
- total wagers = `10 + 90 + 120 = 220`;
- total cost = **AUD 110**.

Guaranteed payout depends on which outcome class occurs:
- all equal -> AUD 250;
- one pair -> AUD 80;
- all distinct -> AUD 40.

Thus the strict guaranteed gross floor is only **AUD 40 / AUD 110 = 36.3636%**.

Expected gross of this exact cover:

`(10*250 + 270*80 + 720*40)/1000 = AUD 52.90`

Expected-return ratio = **48.0909%**.

The same conclusion follows from linear expectation: Exact has 50% gross EV; both Any Order classes have about 48% gross EV. Any nonnegative additive mixture of these ordinary wagers remains negative expectation; a strict positive-profit portfolio on every outcome would necessarily have positive expectation, contradiction.

Status: **REJECTED as guaranteed-profit additive/coverage class**.

## Files
- `src/loto_research/lotterywest_compact.py`
- `tests/test_lotterywest_compact.py`
- `data/derived/h035_lotterywest_compact_screen.csv`

## Strategic result
This packet closes two more compact current products:
- Super66: theoretical full-space floor is only 54.35% at minimum top payout and, more decisively, deterministic unique coverage is not offered because selections are automatic/random.
- Cash 3: controllable compact coverage exists, but its exact guaranteed floor is only 36.36% and every base additive wager has negative EV.

Next search should continue prioritizing products with **deterministic purchase discounts/rebates plus fixed non-shared cash payouts**, because ordinary compact fixed-odds games continue to cluster far below the guarantee hurdle.
