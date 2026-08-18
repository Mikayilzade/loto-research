# H070 — Azerbaijan interbank FX cross-arbitrage

Updated: 2026-08-18
Status: **mechanism valid in principle; synchronized official-bank sample negative; no current SUCCESS**

## Question
Can the same foreign currency be bought from one Azerbaijan bank and immediately sold to another at a higher posted executable rate, producing a deterministic AZN profit after all costs?

For currency `c`, let:
- `ask_i(c)` = AZN price at which bank `i` sells the foreign currency to us;
- `bid_j(c)` = AZN price at which bank `j` buys the foreign currency from us.

A necessary pre-fee arbitrage condition is:

`max_j bid_j(c) > min_i ask_i(c)`.

Gross round-trip return on one foreign-currency unit is:

`R = max_bid / min_ask - 1`.

If this inequality already fails before fees, transport, denomination constraints and branch limits, strict arbitrage is rejected for that snapshot.

## Synchronized official-bank screen — 31 July 2026
I used only quotes attributable to the same calendar date and kept cash and cashless channels separate where the source distinguished them.

Primary official sources:
- ABB, exchange-rate page, last update 31.07.2026.
- PAŞA Bank, exchange-rate page with date selector, 31.07.2026.
- AccessBank, homepage exchange table, updated 31.07.2026.
- Bank Respublika, exchange table, 31.07.2026.

### Cash channel
Best observed posted quotes among the unambiguous same-day cash rows:

| Currency | best bank bid (bank buys) | lowest bank ask (bank sells) | pre-fee spread | gross round-trip return |
|---|---:|---:|---:|---:|
| USD | 1.6970 | 1.7020 | -0.0050 AZN/USD | -0.2938% |
| EUR | 1.9250 | 1.9650 | -0.0400 AZN/EUR | -2.0356% |
| GBP | 2.2510 | 2.3200 | -0.0690 AZN/GBP | -2.9741% |
| RUB (100) | 2.0500 | 2.1500 | -0.1000 AZN/100 RUB | -4.6512% |

No currency crosses zero. Therefore no same-day cash surebet exists in this sampled official set even before operational costs.

### Cashless channel
Where directly published and comparable:
- PAŞA USD 1.6975 / 1.7025; AccessBank USD 1.6950 / 1.7025.
- PAŞA EUR 1.9310 / 1.9820; AccessBank EUR 1.9368 / 1.9857.
- PAŞA GBP 2.2560 / 2.3150; AccessBank GBP 2.2400 / 2.3086.
- PAŞA 100 RUB 1.8900 / 2.3900; AccessBank 100 RUB 1.9200 / 2.3500.

Best observed cashless ratios are also below 1 before fees:
- USD: `1.6975 / 1.7025 - 1 ≈ -0.2937%`;
- EUR: `1.9368 / 1.9820 - 1 ≈ -2.2805%`;
- GBP: `2.2560 / 2.3086 - 1 ≈ -2.2784%`;
- RUB: `1.9200 / 2.3500 - 1 ≈ -18.2979%`.

## Important false-positive control: timestamp alignment
A historical-looking RUB cross can appear if bank pages from different dates are combined. Example: one older Bank Respublika indexed snapshot showed 100 RUB buy around 2.22 while a later Unibank snapshot showed sell around 2.14. That would superficially imply ~3.74% profit, but the quotes were from different dates and were not simultaneously executable.

Therefore H070 requires a hard synchronization rule:
1. same date is the minimum acceptable historical screen;
2. terminal SUCCESS requires contemporaneous executable quotes, ideally locked/confirmed at both legs;
3. never combine cached/indexed quote timestamps as if simultaneous.

## Execution gates for any future candidate
A positive posted cross is not yet SUCCESS. Must also lock:
- exact branch/channel availability;
- quote validity during both legs;
- cash/cashless compatibility;
- transaction commissions and account conversion fees;
- denomination/quality restrictions for banknotes;
- customer/AML/volume limits;
- transport and timing cost;
- tax/reporting treatment if activity becomes systematic.

## Conclusion
**H070 is a valid deterministic-arbitrage class but the synchronized official-bank sample is negative.**

The best sampled pre-fee gap is USD at roughly **-0.294%**, so there is no hidden margin for fees. The branch should not be called SUCCESS unless a genuinely simultaneous positive cross is observed and both legs can be locked before execution.

Reopen H070 only on new synchronized/live quotes or a bank API/feed capable of sub-day cross-bank scanning; do not infer arbitrage from stale search-index snapshots.
