# H347 VALIDATION — UK Thunderball fixed-prize cover

Date: 2026-08-29
Result: **PASS — exact closure certificate; 0 inconclusive**

## Independent checks
1. Universe check: `C(39,5) * 14 = 575,757 * 14 = 8,060,598` legal lines.
2. For a fixed draw, each line is classified uniquely by main-match count `k=0..5` and whether its Thunderball equals the drawn Thunderball.
3. Main-selection multiplicity is `C(5,k) * C(34,5-k)`; Thunderball multiplicity is 1 for a match and 13 otherwise.
4. The 12 resulting category counts sum exactly to **8,060,598**, so there are no unclassified lines.
5. Applying the advertised current prize table gives exact full-cover gross **£4,262,568**.
6. At current £1/line, exact cover cost is **£8,060,598**.
7. Exact deficit is therefore **£3,798,030**, return **52.8815355883%**.
8. The official current National Lottery page says certain prizes may be less than stated in exceptional circumstances. Treating every category at its advertised value is therefore player-favourable for this closure; any reduction cannot repair the deficit.

## Reconciliation by category
- 5+TB: `1 * £500,000 = £500,000`
- 5: `13 * £5,000 = £65,000`
- 4+TB: `170 * £250 = £42,500`
- 4: `2,210 * £100 = £221,000`
- 3+TB: `5,610 * £20 = £112,200`
- 3: `72,930 * £10 = £729,300`
- 2+TB: `59,840 * £10 = £598,400`
- 1+TB: `231,880 * £5 = £1,159,400`
- 0+TB: `278,256 * £3 = £834,768`
- non-prize categories: £0

Gross sum: **£4,262,568**.

## Inconclusive accounting
- arithmetic inconclusive: **0**
- category-classification inconclusive: **0**
- closure-relevant execution inconclusive: **0** (execution cannot improve an advertised-prize upper bound that is already below cost)

## Reproducibility
Executable model: `src/loto_research/h347_uk_thunderball_fixed_cover.py`
Derived certificate: `data/derived/h347_uk_thunderball_fixed_cover.json`

The script asserts the universe, category sum, gross, cost and deficit exactly before emitting results.
