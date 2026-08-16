# H037 — Irish Lotto Plus Million Euro Raffle

Updated: 2026-08-16
Status: **positive-EV overlay lead under plausible participation; strict guaranteed-profit path rejected**

## Why this branch matters
The Irish National Lottery periodically runs a special Lotto Plus Million Euro Raffle. Every Lotto Plus line receives a four-digit raffle number. In an ordinary draw, tickets with the winning raffle number receive €500. In the special event, all tickets with that winning raffle number are entered into a once-off random draw and one ticket owner receives an additional €1,000,000.

Official current sources:
- Lotto Plus rules/info: https://www.lottery.ie/game-information/lotto-plus
- Million Euro Raffle terms: https://www.lottery.ie/game-information/lotto-plus/million-euro-raffle
- 30 May 2026 event announcement: https://www.lottery.ie/news/press-releases/could-you-be-irelands-next-millionaire-1-million-guaranteed-to-be-won-in-saturday-night-s-lotto-plus-raffle
- 2026 pricing announcement confirms two Lotto lines cost €4 and two lines with Lotto Plus cost €6, so the Plus add-on is €1 per line: https://www.lottery.ie/news/press-releases/national-lottery-unveils-exciting-changes-to-lotto-lotto-plus-games

The operator says the ordinary Lotto Plus Raffle typically has about 60–120 winners per draw. The raffle odds are approximately 1 in 10,000 per Plus line.

## 1. Strict guarantee test
A terminal guarantee fails for two independent reasons.

### Random raffle-number assignment
Players do not choose the four-digit raffle number. Buying a finite number of lines cannot force deterministic coverage of all 10,000 raffle codes because duplicate assigned codes can occur.

### External qualifying tickets
Even if a player somehow held at least one instance of every raffle number, the special €1m is not automatically paid to every holder of the winning number. All tickets with the winning raffle number enter a second random draw and one ticket owner is selected.

Therefore any external qualifying ticket creates a legal outcome where another player receives the €1m. No useful hard pre-draw cap or exclusion mechanism is published.

Conclusion: **H037 is REJECTED as a strict guaranteed-profit strategy.**

## 2. Incremental Plus EV — stronger result
The event is nevertheless economically interesting because the extra €1m is a deterministic external subsidy to the set of eligible Lotto Plus entries.

Current pre-autumn-2026 game regime is 6/47. Using the published fixed prize tables for Plus 1 and Plus 2 and the ordinary €500 raffle at odds 1/10,000:

- Plus 1 fixed-prize EV ≈ **€0.22902755 per Plus line**;
- Plus 2 fixed-prize EV ≈ **€0.13263705**;
- ordinary raffle EV = **€0.05**;
- combined fixed Plus package EV ≈ **€0.41166460 per €1 add-on**.

This calculation grants top prizes at face value and therefore should be read as a clean analytical baseline, not a claim about prize-limit edge cases.

### Special €1m event subsidy
Let `T` be total eligible Plus raffle entries in the event. Under entry symmetry, ex-ante expected value of the extra million per entry is:

`€1,000,000 / T`.

So incremental expected payout of the €1 Plus add-on is approximately:

`0.4116645959 + 1,000,000/T`.

Break-even occurs at:

`T ≈ 1,699,710.73 eligible Plus lines`.

Equivalent expected ordinary-raffle winner count is about:

`T / 10,000 ≈ 169.97 winners`.

The operator's own typical range is only **60–120 raffle winners**, corresponding heuristically to about **600k–1.2m Plus entries**. In that range:

| proxy eligible lines | extra €1m EV/line | total Plus EV | ROI on €1 Plus add-on |
|---:|---:|---:|---:|
| 600,000 | €1.6667 | €2.0783 | 207.8% |
| 900,000 | €1.1111 | €1.5228 | 152.3% |
| 1,200,000 | €0.8333 | €1.2450 | 124.5% |

Thus a special Million Euro Raffle event is a **credible positive-EV incremental Plus overlay** if total participation stays below ~1.70m Plus lines.

This is much stronger than a generic promotion because the subsidy is large, guaranteed to be distributed, and the add-on price is only €1 per line.

## 3. Important caveats
- The operator's 60–120 figure is a typical-winner statement, not an audited event-specific sales count.
- Special events can increase participation, so `T` may be higher than normal.
- Exact selection mechanics among multiple qualifying entries/tickets need rules-level confirmation before staking capital.
- Top-prize limits, tax treatment, account limits, purchase limits and execution frictions must be checked for a real-money decision.
- This result is **positive expected value**, not guaranteed profit. The €1m is allocated randomly and an individual line can still return zero.
- The main Lotto line is mandatory. The result above evaluates the **incremental decision to add Lotto Plus** to a Lotto line that would otherwise already be purchased. It is not yet a proof that a fresh €3 Lotto+Plus line has positive total EV.

## 4. Next high-value test
Recover event-specific raffle winner counts and, if possible, exact Plus-entry sales around special €1m dates. Then estimate demand uplift on event days and determine whether the incremental Plus edge survives actual participation rather than the operator's normal 60–120 range.

Also test whether ticket-level versus line-level treatment in the once-off random selection changes the symmetry calculation for multi-line tickets.

## Files
- `src/loto_research/lotto_plus_raffle.py`
- `tests/test_lotto_plus_raffle.py`
- `data/derived/h037_lotto_plus_million_raffle_screen.csv`

## Current conclusion
**No terminal SUCCESS.** Strict guarantee is impossible under published mechanics because the €1m recipient is randomly selected among qualifying tickets and external entries cannot be excluded. However H037 is now one of the strongest live positive-EV leads in the repository: the special-event Plus add-on appears +EV whenever total eligible Plus entries remain below ~1.70m.
