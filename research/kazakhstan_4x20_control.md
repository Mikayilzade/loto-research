# Kazakhstan 4/20 — active state-transition control

Updated: 2026-08-12
Role: **control/comparator for Azerbaijan 4+4; do not transfer rules across jurisdictions**
Status: **state-transition mechanism replicated on three exact consecutive-draw identities**

## Why this game is useful
Kazakhstan's current 4/20 has the same core two-board combinatorics as Azerbaijan 4+4 (4 from 20 in each field), but exposes more of its prize structure publicly and has richer preserved draw tables. It is therefore a control for developing and validating state-accounting methods.

Primary current game page:
- https://sz.kz/420

Primary legal sources:
- https://adilet.zan.kz/rus/docs/Z1600000495
- https://www.adilet.zan.kz/rus/docs/V2300031880

Secondary draw evidence:
- draw 1499: https://lucky-numbers.ru/lottery/kz/4x20/1777734000000
- draw 1500: https://lucky-numbers.ru/lottery/kz/4x20/1777820400000
- draw 1501: https://lucky-numbers.ru/lottery/kz/4x20/1777906800000
- draw 1545: https://lucky-numbers.ru/lottery/kz/4x20/1781708400000
- draw 1546: https://lucky-numbers.ru/lottery/kz/4x20/1781794800000

Normalized transition rows:
- `data/historical/kz_4x20_transition_samples.csv`

## Public structure
The operator page currently states:
- daily draw at 20:00;
- ticket from 300 KZT;
- two fields, four of 20 in each;
- superprize receives 3% plus carried superprize, minimum 5m KZT;
- category funds are divided equally among winners.

The cached page also states PF=50% of realization while the listed percentages sum above 50%; furthermore the cached VI percentage differs from actual June-2026 table arithmetic. This is treated as a rule-version/page-consistency issue, not forced into a timeless model.

Observed 2026 tables are consistent with these base shares of `reported_tickets × 300` before category hierarchy/floor adjustments:
- I: 3%
- II: 2%
- III: 2%
- IV: 3%
- V: 2%
- VI: ~2% in sampled actual tables
- VII: base ~2%, with possible minimum/hierarchy adjustment
- VIII: 6%
- IX: 4%
- X: 6%
- XI: 14.5%
- XII: 11.5%.

Kazakhstan law requires a lottery prize fund of **at least** 50% of revenue. Therefore an observed structure above 50% is not inherently illegal; the cached page wording and current table version still require reconciliation.

## Replicated superprize transition law
The following accounting identity is observed repeatedly:

**J_t = J_(t-1) + unpaid variable-category funds from t-1 + 3% × 300 × reported_tickets_t**

### Transition 1499 → 1500
Draw 1499:
- J = **212,457,078**
- category III: 0 winners, **82,836** assigned
- category V: 0 winners, **82,836** assigned
- unpaid = **165,672**.

Draw 1500:
- tickets = **12,936**
- ordinary 3% contribution = `12,936×300×3% = 116,424`
- J = **212,739,174**.

Observed increase:
`212,739,174 - 212,457,078 = 282,096`

Reconstructed:
`165,672 + 116,424 = 282,096`

**Exact equality.**

### Transition 1500 → 1501
Draw 1500:
- category II: 0 winners, **77,616** assigned
- unpaid = **77,616**.

Draw 1501:
- tickets = **14,434**
- ordinary 3% contribution = `14,434×300×3% = 129,906`
- J = **212,946,696**.

Observed increase:
`212,946,696 - 212,739,174 = 207,522`

Reconstructed:
`77,616 + 129,906 = 207,522`

**Exact equality.**

### Transition 1545 → 1546
Draw 1545:
- J = **226,866,699**
- category II: 0 winners, **99,432** assigned
- category IV: 0 winners, **149,148** assigned
- unpaid = **248,580**.

Draw 1546:
- tickets = **14,742**
- ordinary 3% contribution = `14,742×300×3% = 132,678`
- J = **227,247,957**.

Observed increase:
`227,247,957 - 226,866,699 = 381,258`

Reconstructed:
`248,580 + 132,678 = 381,258`

**Exact equality.**

## Interpretation
Three independent transitions separated by more than a month reproduce the same identity **to the tenge**. This raises the mechanism from a one-draw curiosity to a validated empirical state-transition rule for the sampled 2026 regime.

The legal framework fits the observation: Kazakhstan law defines a superprize as undrawn prize-fund money moving between draws according to game conditions, and otherwise requires draw prize funds to be played in their draw except for cumulative superprize formation.

We still distinguish:
- **validated arithmetic**: three exact transitions;
- **primary legal compatibility**: cumulative superprize is explicitly recognized;
- **missing primary game-condition clause**: we have not yet captured the operator's detailed condition text explicitly stating that every zero-winner category is added to the next superprize.

## Exact pari-mutuel EV model
For a category with probability `p`, current fund `B` and `N` statistically uniform total entries:

`EV = (B/N) × [1 - (1-p)^N]`

The bracket is the chance that the category has at least one winner. Rare categories have meaningful zero-winner probability, so part of their current allocation is often not paid immediately and instead changes the next state.

Implementation:
- `src/loto_research/pari_mutuel.py`
- regression: `tests/test_pari_mutuel.py`

## Current-state economic screen
Using draw 1546 as a representative state:
- N = **14,742** reported 300-KZT units;
- superprize = **227,247,957 KZT**;
- lower-category weights inferred from actual 2026 tables.

Uniform-selection screening model:
- lower categories: **≈155.43 KZT EV**
- superprize: **≈9.68 KZT EV**
- total: **≈165.10 / 300 KZT**
- gross return: **≈55.03%**.

Static break-even superprize at the same crowd size/structure:

**≈3.395 billion KZT.**

So the modern transfer mechanism is real, but the sampled state is very far from +EV.

Caveats: one reported 300-KZT unit is treated as one base two-field entry; category floors/hierarchy adjustments, taxes, promotions, non-uniform selections and large-portfolio self-impact are not yet fully modeled.

## Why accumulation is frequent
At N≈14,742, exact zero-winner probabilities under uniform selection are approximately:
- II: **92.3%**
- III: **40.5%**
- IV: **6.0%**
- V: **10.2%**
- VI: **7.6%**.

Expected unpaid lower-category money under the simple base-weight model is about **141k KZT/draw**, comparable with the ordinary 3% superprize contribution of about **133k KZT/draw**.

Therefore the state can grow materially faster than the advertised 3% contribution alone, but current economics still require a much larger accumulation to approach break-even.

## Relevance to Azerbaijan 4+4
Do **not** copy Kazakhstan's rules into Azerbaijan.

Use the replicated identity as a forensic signature:
1. find an Azerbaijan 4+4 draw with zero winners in a variable category;
2. reconstruct the unpaid category amount from the Azerbaijan U-engine;
3. estimate ordinary next-draw jackpot growth from sales/pool scale;
4. test whether the unexplained next-state increment equals the unpaid amount;
5. repeat across several transitions.

If the Azerbaijan accounting closes repeatedly, H014 becomes an actual state model. If it fails, the comparator still tells us what not to assume.
