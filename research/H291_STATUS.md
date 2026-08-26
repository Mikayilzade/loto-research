# H291 STATUS

Updated: 2026-08-26
Status: **SCREENED / NO CURRENT PUBLIC STRICT-PROFIT QUALIFIER**

## H225-X* lane
H225-X* remains **CLOSED / EXHAUSTED** at X20: 44 canonical shards / 11 sectors / exactly 306,450 states -> **0 coefficient survivors / 0 legal shift tuples**. Do not create X21/X22 under the unchanged family.

## H291 checkpoint
Michigan Lottery publicly documents two relevant deterministic online subsidy classes:
- deposit-match **Bonus Credit**;
- `Play & Get Bonus Cash`, where the earned Bonus Cash is withdrawable.

Daily 3 is also documented as available in the Michigan Lottery mobile app in 2026.

Exact one-copy Straight cover:
- all 1,000 outcomes `000..999`;
- $0.50 each;
- $500 total acquisition;
- exactly one $250 Straight winner for every draw;
- deterministic base floor = **50%**.

If a fully spendable deposit match is `m`, external cash required is `500/(1+m)`. Strict profit requires

`250 > 500/(1+m)` -> **`m > 100%`**.

Thus:
- 40% match -> 70% guaranteed cash recovery;
- 100% match -> exact break-even;
- only >100% can cross strict profit for this cover.

The official public bonus FAQ currently gives sample offers (10%, tiered examples up to 40%, and a sample $25 play -> $5 withdrawable Bonus Cash) and says actual offers vary/account-specific. It does **not** establish a current universal >100% match or a repeatable cash reward sufficient to fund the full cover.

## Reopen condition
Reopen only with a current Lottery-controlled eligible offer that is verifiably:
1. >100% fully spendable deposit match with enough cap for the cover; or
2. deterministic withdrawable Bonus Cash large enough to lift the invariant $250 gross above external cash committed; or
3. another fixed-pay online Michigan construction with deterministic floor above 50%.

Files:
- `research/h291_michigan_daily3_bonus_threshold.md`
- `research/H291_VALIDATION.md`
- `src/loto_research/h291_michigan_daily3_bonus_threshold.py`
- `data/derived/h291_michigan_daily3_bonus_threshold.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H291_APPEND.md`

Global state remains **NO SUCCESS; NOT EXHAUSTED**.
