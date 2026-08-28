# H341 VALIDATION

Date: 2026-08-28

## Independent checks
1. `research/H225_EXACT_STATUS.md` was read first. H225-X20 remains terminal at exactly 0 coefficient survivors / 0 legal shift tuples; no H225-X21/X22 was created.
2. Branch `research-work` HEAD before this packet was `df844e0584fa09b8465b24781bcd9d4f85f7a73c` (H340).
3. H340 already rejected non-binding footer/template phone copy. H341 therefore uses two promotions whose specific rules themselves provide phone entry.
4. Global Cash Call specific rules: one random winner from all valid entries; free phone route capped at 300 entries; paid external-entry routes remain legal.
5. Bauer Make Me A Winner current specific rules: one random winner from all valid entries; phone route capped at 250 entries; paid external-entry routes remain legal.
6. In each promotion, a valid external entry is a legal member of the draw universe. Selecting that entry is a legal outcome, giving our portfolio £0 gross.
7. The proof deliberately grants the player zero marginal phone cost. Therefore even the strongest cost assumption yields worst-case profit <= £0, not strict positive profit.
8. Positive standard-network call charges only strengthen the rejection.

## Assertions
- `global_cap == 300`
- `bauer_cap == 250`
- `global_winners == 1`
- `bauer_winners == 1`
- `external_entry_possible == True` for both
- `worst_case_gross == 0` for both
- `strict_positive_guarantee == False` for both

## Inconclusive accounting
- arithmetic inconclusive: **0**
- route inconclusive relevant to closure: **0**
- execution inconclusive relevant to closure: **0**

## Verdict
**CLOSED / NOT SUCCESS.** The finite-cap, single-winner public free-phone class is rigorously blocked by the external-entry branch.
