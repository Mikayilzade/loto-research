# H314 STATUS

Updated: 2026-08-27
State: **CLOSED / CAP-BLOCKED / ZERO STRICT CASH FLOOR**

## Candidate

WinWink `£50k COIN FLIP!` live finite instant-win pool.

## Exact checkpoint

- total positions: **142,857**;
- committed instant-win positions: **71,428**;
- one-player cap: **21,429**;
- snapshot sold: **1,615**;
- instant wins remaining: **70,598**;
- exact remaining losing positions: **70,644**;
- losing inventory minus full player cap: **49,215**.

Because winning positions are precommitted but hidden/unselectable before purchase, a legal realization exists in which every ticket allowed to one player lies in the remaining losing set. Therefore the guaranteed cash floor is **£0**.

This closes H314 without EV assumptions and supplies a reusable gate: for hidden precommitted instant-win pools, if `remaining_losers >= player_cap`, no one-player portfolio can have positive strict instant-win floor.

## Files

- `research/h314_winwink_coinflip_cap_bound.md`
- `research/H314_VALIDATION.md`
- `src/loto_research/h314_winwink_coinflip_cap_bound.py`
- `data/derived/h314_winwink_coinflip_cap_bound.json`

## NEXT ACTION

Do not reopen H314 unless identifiers become selectable/reservable before payment or the effective player acquisition cap exceeds all remaining losing identifiers.

Continue global research with a genuinely different mechanism: fresh finite inventory where a player can deterministically reserve enough identifiers to eliminate every zero-cash outcome, preferably with player-facing liabilities already above exact acquisition cost.
