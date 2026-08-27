# H324 STATUS

Updated: 2026-08-28
State: **CLOSED / NO SUCCESS**

## Result

Checked current Click Competitions free/multi-winner and cheap finite cash pools.

Strongest new structural result: the free £10,000 giveaway has 40 × £250 winners, a 300,000-entry pool, max 49 entries per person, and 2,367 entries on the checked snapshot. Even granting all 49 allowed entries to one player, at least 2,318 already-entered IDs are external. Since 2,318 >= 40, a legal outcome exists where all 40 prizes go to external entries. Strict one-player cash floor = **£0**.

Paid stronger-than-real full-buyout checks also fail:
- £1,000 LOW ODDS: £1,488.51 impossible full cost -> 67.1813% gross; real cap 5/149.
- £10,000 for 2p: £23,799.90 full cost -> 42.0170%; real cap 50,000/1,189,995.
- £20,000 for 2p: £34,999.98 full cost -> 57.1429%; real cap 50,000/1,749,999.

Thus none of these current pools can produce a rigorous one-player guaranteed profit.

## Files
- `src/loto_research/h324_click_multiwinner_cap_bound.py`
- `data/derived/h324_click_multiwinner_cap_bound.json`
- `research/h324_click_multiwinner_cap_bound.md`
- `research/H324_VALIDATION.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H324_APPEND.md`

## NEXT ACTION

Do not reopen generic free multi-winner or very-cheap cash pools unless the player can eliminate all legal external-winning sets. Search for an electronic finite mechanism with near/full reservability, or a prize schedule that gives every controlled identifier a strictly positive withdrawable-cash floor.

H225-X* remains separately **CLOSED / EXHAUSTED at X20**; do not create X21/X22 under the unchanged family.
