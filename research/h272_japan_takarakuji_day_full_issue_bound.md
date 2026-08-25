# H272 — Japan 2026 Takarakuji Day commemorative lottery full-issuance bound

Date: 2026-08-25
State: **CLOSED / REJECTED for strict guaranteed-profit full-inventory takeover**

## Why this mechanism was opened

The current NEXT ACTION prefers a genuinely finite, hard-capped identifier inventory that could in principle be monopolized. Japan's ordinary printed lotteries are attractive for that screen because the official 2026 Takarakuji Day commemorative lottery (draw 1118) publishes a finite issuance: **2 units of 10,000,000 tickets each**, with a fixed complete prize schedule. The sale period is 2026-08-01 through **2026-08-25**, ticket price JPY 200, draw 2026-08-28.

Instead of arguing about real-world availability of every serial ticket, H272 grants the player the stronger impossible condition of owning **all 20,000,000 issued tickets**. If even that complete takeover is below cost, inventory/reservation friction is irrelevant to the guarantee question.

## Exact full-issuance arithmetic

Official total face value:
- 2 units × 10,000,000 tickets = **20,000,000 tickets**;
- JPY 200 each;
- acquisition cost = **JPY 4,000,000,000**.

Complete published prize schedule:
- 1st: JPY 150,000,000 × 2 = JPY 300,000,000;
- adjacent-to-1st: JPY 25,000,000 × 4 = JPY 100,000,000;
- same-number/different-group: JPY 100,000 × 198 = JPY 19,800,000;
- 2nd: JPY 500,000 × 400 = JPY 200,000,000;
- 3rd: JPY 50,000 × 2,000 = JPY 100,000,000;
- 4th: JPY 10,000 × 20,000 = JPY 200,000,000;
- 5th: JPY 2,000 × 200,000 = JPY 400,000,000;
- 6th: JPY 200 × 2,000,000 = JPY 400,000,000;
- special prize: JPY 30,000 × 6,000 = JPY 180,000,000.

Total winner-facing prize value = **JPY 1,899,800,000**.

Therefore impossible-perfect full ownership returns:
- **47.495% gross**;
- deficit **JPY 2,100,200,000**;
- no outcome dependence remains because owning the entire issued set captures every listed winning ticket.

## Strong conclusion

This is stronger than an ordinary EV rejection. Under the impossible favorable assumption that one player controls every issued ticket at face value and can collect every published prize, the complete prize pool is still only 47.495% of acquisition cost. Any real-world inability to reserve ticket numbers, regional distribution, sold inventory, transaction limits, or acquisition overhead can only worsen the result.

So this particular finite printed-ticket mechanism is decisively closed for strict guaranteed profit. It remains a useful structural benchmark: a hard-capped, monopolizable identifier set is not enough; **the total guaranteed winner-facing liabilities must themselves exceed the cost of buying the whole cap** or an additive external subsidy must cross the deficit.

## Sources checked

Primary source: Japan Lottery official site, 2026-08-05 announcement for 「宝くじの日記念」くじ, draw 1118. It publishes the full prize table, total issuance JPY 4 billion / 2 units, 10 million tickets per unit, JPY 200 ticket price, sale dates 2026-08-01 to 2026-08-25, and draw date 2026-08-28.

Official page: https://www.takarakuji-official.jp/news/recent/?newsId=260802

## Reproducibility

- `src/loto_research/h272_japan_takarakuji_day_full_issue_bound.py`
- `data/derived/h272_japan_takarakuji_day_full_issue_bound.json`
