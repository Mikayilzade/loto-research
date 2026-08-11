# Kazakhstan 4/20 — active state-transition control

Updated: 2026-08-12
Role: **control/comparator for Azerbaijan 4+4; do not transfer rules across jurisdictions**

## Why this game is useful
Kazakhstan's current 4/20 has the same core two-board combinatorics as Azerbaijan 4+4 (4 from 20 in each independent field), but exposes more of its prize structure publicly and has richer preserved draw tables. It is therefore a useful control for developing and validating a state-transition model.

Primary current game page:
- https://sz.kz/420

Primary legal sources:
- Kazakhstan Law on lotteries and lottery activity: https://adilet.zan.kz/rus/docs/Z1600000495
- current lottery rules: https://www.adilet.zan.kz/rus/docs/V2300031880

Secondary draw snapshots used for arithmetic reconstruction:
- draw 1545: https://lucky-numbers.ru/lottery/kz/4x20/1781708400000
- draw 1546: https://lucky-numbers.ru/lottery/kz/4x20/1781794800000

## Current public structure
The operator page currently shows:
- daily draw at 20:00;
- ticket from 300 KZT;
- two fields, four numbers selected from 20 in each;
- superprize category receives a stated 3% share plus carried superprize, minimum 5m KZT;
- lower categories are pari-mutuel: each category's fund is divided equally among its winners.

The cached public page contains an internal inconsistency: it says the prize fund is 50% of realization while listed category percentages sum above 50%, and its VI percentage differs from actual 2026 draw-table arithmetic. Treat the current draw tables and rule-version issue separately rather than forcing them into one timeless table.

Observed June-2026 draw tables are consistent with these base shares of `tickets_sold × 300` for ordinary category funds:
- I superprize contribution: ~3%
- II: 2%
- III: 2%
- IV: 3%
- V: 2%
- VI: ~2% in actual sampled tables
- VII: base ~2%, with possible minimum/hierarchy adjustments
- VIII: 6%
- IX: 4%
- X: 6%
- XI: 14.5%
- XII: 11.5%

These observed shares sum to ~58% including the ordinary superprize contribution. Kazakhstan law requires at least 50%, not necessarily exactly 50%.

## Exact modern state-transition proof
Draw 1545, 17 June 2026:
- displayed superprize: **226,866,699 KZT**;
- category II: **0 winners**, assigned pool **99,432 KZT**;
- category IV: **0 winners**, assigned pool **149,148 KZT**;
- unpaid lower-category total: **248,580 KZT**.

Draw 1546, 18 June 2026:
- tickets sold: **14,742**;
- reporting/base amount: `14,742 × 300 = 4,422,600 KZT`;
- 3% ordinary superprize contribution: **132,678 KZT**;
- displayed superprize: **227,247,957 KZT**.

The observed increase is:

`227,247,957 - 226,866,699 = 381,258`

and:

`248,580 + 132,678 = 381,258`

Therefore:

**J_1546 = J_1545 + unpaid_II_1545 + unpaid_IV_1545 + ordinary_3%_1546**

**to the tenge, exactly.**

This is not a correlation or fitted regression. It is a consecutive-draw accounting identity in the preserved tables.

The legal framework is consistent with this mechanism: Kazakhstan law defines a superprize as the part of a draw lottery prize fund not drawn and transferred to the next draw according to the lottery terms; ordinary prize funds must be drawn within the draw except where cumulative superprize formation is used.

We still distinguish:
- **directly observed arithmetic**: the exact transition above;
- **legal compatibility**: law permits/defines cumulative superprize;
- **not yet captured primary game-condition wording**: an explicit clause saying every zero-winner lower-category pool of this 4/20 is added to the next superprize.

## Exact pari-mutuel EV model
For a category with probability `p`, current fund `B` and `N` total statistically uniform entries, a representative entry's expected payout from that shared pool is:

`EV = (B/N) × [1 - (1-p)^N]`

The bracket is the probability that at least one winner exists in the category. For common categories it is almost 1. For rare categories it can be materially below 1; the unpaid money is exactly where an inter-draw state transition can matter.

Implementation:
- `src/loto_research/pari_mutuel.py`

## Current-state economic screen
Use draw 1546 as a representative state:
- N = **14,742** reported 300-KZT units;
- superprize = **227,247,957 KZT**;
- observed ordinary lower-category allocation weights from the 2026 draw tables.

Under a uniform-selection baseline:
- expected immediate lower-category payout ≈ **155.43 KZT** per 300-KZT unit;
- expected superprize component ≈ **9.68 KZT**;
- gross immediate EV ≈ **165.10 KZT / 300 KZT**;
- gross return ≈ **55.03%**.

A simple static break-even superprize at the same N and lower-category structure is approximately:

**3.395 billion KZT.**

That is roughly 15× the observed 227m KZT state. Therefore the transfer mechanism is real, but **the sampled current state is nowhere near +EV**.

This estimate is a screening model, not an executable strategy claim. It assumes one reported 300-KZT unit behaves as one base two-field combination and ignores taxes, promotions, category-floor adjustments, non-uniform player choices and a large portfolio's self-impact.

## Why the mechanism is still strategically important
At N≈14,742, exact zero-winner probabilities under uniform selections are roughly:
- II: **92.3%**
- III: **40.5%**
- IV: **6.0%**
- V: **10.2%**
- VI: **7.6%**.

Thus lower-category money can flow into the superprize frequently. A state variable exists and changes predictably in distribution even though the current jackpot is too small for positive EV.

At the same N, a rough expected lower-category amount left unpaid in a draw is about **141k KZT**, while the ordinary 3% superprize addition is about **133k KZT**. So zero-winner transfers can be of the same order as the ordinary jackpot contribution.

This makes Kazakhstan 4/20 a valuable control for testing:
1. state accounting;
2. exact pre-draw EV from a visible superprize;
3. crowd/self-sharing effects;
4. whether long accumulation can ever approach a threshold before a jackpot hit resets the state.

## Relevance to Azerbaijan 4+4
Do **not** assume Azerbaijan uses the same transfer rule.

Instead, use the Kazakhstan result as a signature to search for in Azerbaijan:
- find an Azerbaijan draw with a zero-winner variable category;
- infer its unpaid normal pool using the reconstructed U-engine;
- compare the next jackpot / category balances with ordinary expected growth;
- test whether the missing amount appears exactly in the next state.

If the Azerbaijan accounting closes similarly, H014 gains a real state-transition model. If it does not, the Kazakhstan control has still prevented us from guessing the wrong mechanism.
