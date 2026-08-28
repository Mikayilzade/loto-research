# H327 independent validation

Date: 2026-08-28
Result: **PASS — closure arithmetic and worst-case support verified**

Independent checks from the live KRAZED COSMIC CASH snapshot and Royal Mail price page:

1. Finite pool: 99,999 identifiers; snapshot sold = 316; remaining = **99,683**.
2. One free postal entry receives exactly **10 tickets**; only one free postal entry is permitted per person per competition.
3. Current Royal Mail 2nd Class standard letter/postcard price = **£0.91**.
4. Equivalent 10 paid tickets cost **£1.00**, hence postal effective price = **9.1p/ticket** and deterministic discount = **9%**.
5. Published instant tiers contain exactly **12,029** prize-bearing identifiers and **£5,650** total instant cash face value.
6. Snapshot found counts total **41**, leaving **11,988** instant identifiers.
7. Remaining zero-instant support = `99,683 - 11,988 = 87,695`.
8. Since `87,695 >= 10`, a legal allocation exists in which every ticket in the only subsidised postal bundle receives zero instant cash.
9. Therefore strict guaranteed withdrawable-cash floor = **£0**.
10. Paid max-per-user 999 is also far below the full 99,999 identifier universe, so ordinary paid acquisition cannot turn this into a one-player takeover.

The closure does not rely on EV, independence, or approximate probabilities.

Sources:
- https://krazed.co.uk/competition/cosmic-cash
- https://www.royalmail.com/sending/uk/2nd-class

Validated artefacts:
- `src/loto_research/h327_krazed_cosmic_cash_postal_subsidy.py`
- `data/derived/h327_krazed_cosmic_cash_postal_subsidy.json`
- `research/h327_krazed_cosmic_cash_postal_subsidy.md`
