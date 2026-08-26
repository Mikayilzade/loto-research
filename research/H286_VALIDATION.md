# H286 VALIDATION

Date: 2026-08-26
Result: **VALIDATED CLOSED / REJECTED**

Independent checks:
1. The current Michigan Lottery FAQ explicitly says every Daily Spin to Win spin wins a prize.
2. The same FAQ enumerates the current prize classes as in-store free play, online free play/bonuses, or monthly giveaway entries.
3. A monthly giveaway entry is not a cash payment and has a legal non-winning later drawing outcome; its guaranteed withdrawable-cash value is therefore exactly $0.
4. The worst-case cash floor of the spin is the minimum across legally possible prize classes, hence exactly $0.
5. Michigan separately recognizes withdrawable `Bonus Cash`; the Daily Spin FAQ does not guarantee Bonus Cash on every spin.
6. No checked rule establishes a bounded terminal sequence after which a cash prize is forced.

Therefore `every spin wins a prize` is insufficient for the project objective. H286 does not establish a strictly positive guaranteed cash subsidy.

Validated artifacts:
- `research/h286_michigan_daily_spin_cash_floor.md`
- `src/loto_research/h286_michigan_daily_spin_floor.py`
- `data/derived/h286_michigan_daily_spin_floor.json`
