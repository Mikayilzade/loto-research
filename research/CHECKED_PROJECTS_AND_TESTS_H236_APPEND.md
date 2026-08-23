# H236 audit append — RI Lucky 3 Spot doubled coverage threshold

Date: 2026-08-24
Scope: lottery-only; Keno promotion, combinatorial coverage, execution.

## Test
Fresh primary-source recheck of Rhode Island Lottery Keno promotions plus an exact full-space theorem for a 3-spot 20/80 doubled-prize entitlement.

## Exact result
For full coverage of all `C(80,3)=82,160` 3-spot selections, every 20-number draw deterministically yields 34,220 tickets at 0/3, 35,400 at 1/3, 11,400 at 2/3, and 1,140 at 3/3.

If every line receives a true 2x entitlement at unchanged $1 cost, deterministic gross is `2*(11,400*P2 + 1,140*P3)` and strict pre-tax profit requires `10*P2 + P3 > 36.03508771929825`.

## Primary rules recovered
Historical RI Lucky 3 Spot rules prove a real pre-draw printed 2x entitlement on qualifying 3-spot Keno tickets. Qualifying Lucky tickets cannot be cancelled; retailers may not preprint Keno tickets. General RI Keno rules ordinarily permit same-day same-terminal cancellation before the draw.

Fresh 2026 official homepage evidence still advertises `Kick Back with Keno Promotion`, but exact current mechanics remain unrecovered; historical Lucky 3 rules may not be imputed to it.

## Status
**REJECTED as an executable strict guarantee on recovered historical evidence.** The mathematical doubled-cover can cross break-even depending on the base 3-spot paytable, but no lawful/operational guarantee was found that the doubled entitlement can be acquired for all 82,160 distinct combinations within the finite promotion constraints. Current Kick Back remains evidence-blocked pending materially new primary rules.

Files:
- `research/h236_ri_lucky3_full_coverage_threshold.md`
- `src/loto_research/h236_ri_lucky3_full_coverage_threshold.py`
- `data/derived/h236_ri_lucky3_full_coverage_threshold.json`
