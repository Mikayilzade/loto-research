# CHECKED PROJECTS AND TESTS — H276 append

## H276 UK National Lottery Thunderball fixed-prize portfolio bound
- Mechanism class: finite fixed-per-winning-line draw game; no share dilution in the checked paytable.
- Why checked: fixed per-selection liabilities are one of the strongest remaining strict-guarantee classes after H225 closure.
- Universe: `C(39,5) * 14 = 8,060,598` legal lines at £1 each.
- Exact one-copy full-cover gross: **£4,262,568** against **£8,060,598** cost = **52.8815355883%**.
- Stronger result: symmetry gives every primitive line the same 52.8815355883% average gross; every nonnegative portfolio inherits that ratio, and `minimum <= average` proves at least one below-cost legal draw.
- Result: **REJECTED / CLOSED for every nonnegative ordinary Thunderball portfolio under the checked fixed paytable**, not merely for a full cover.
- External-player duplicates do not rescue the construction because the relevant checked prizes are fixed per winning line.
- Reopen gate: material deterministic subsidy, discount, free extra draw, or fixed bonus sufficient to lift primitive average return above 100%.
