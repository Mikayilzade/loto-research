# H168 audit append

Updated: 2026-08-22

| ID | Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|---|
| H168 | NC Pick 3 retailer-discount + forced Double Draw | Current Pick-3-specific discount authority | Current 2025-revised Pick 3 rules explicitly state retailers may authorize promotional discounts if reported at full gross; contrast with Powerball/Mega Millions wording where NCEL may authorize | **VALIDATED retailer-authority architecture**; `research/h168_nc_pick3_discount_authority_and_current_availability.md` |
| H168 | NC Pick 3 Double Draw | Current availability on 2026-08-22 | 2026 promotion verified as July 1-31; not live on current date | **CURRENTLY UNAVAILABLE / monitor recurrence** |
| H168 | NC Pick 3 Double Draw | Forced-state observability | NCEL historical same-day notices explicitly announce guaranteed two-draw evenings when only Yellow Ball remains | **VALIDATED structurally** |
| H168 | NC Pick 3 rollback | Retail ticket cancellation mechanism | Same-terminal cancellation within 15 min or before draw break; retailer reference guide provides normal terminal cancellation procedure | **VALIDATED ticket-by-ticket rollback; atomic bulk rollback NOT PROVEN** |
| H168 | NC Pick 3 deterministic overlay | 100 Front Pair cover on forced Double Draw + retailer discount | $50 face guarantees $50 prize gross; any discount creates pre-tax surplus; H167 tax stress threshold remains >2.9004% | **PROMISING conditional deterministic overlay; NOT terminal SUCCESS** |
