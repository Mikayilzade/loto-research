# H019 — capped fixed-prize competition saturation / buy-all-entries

Updated: 2026-08-15
Status: **mechanism class formalized and screened; no current guaranteed-profit instance found**

## Question
Can a player guarantee profit in a lawful capped-entry prize competition by buying every possible paid entry so that the random draw cannot select anyone else?

This is structurally different from ordinary lottery full-space coverage. The outcome space is the **entry list itself**. If one entrant atomically owns every valid entry in a one-winner draw, they win with probability 1.

## Guarantee theorem
For a single-winner competition with:
- `N` maximum valid entries,
- fixed entry price `c`,
- guaranteed withdrawable cash prize/cash alternative `V`,
- `x` already-owned valid entries belonging to other people,
- entrant-specific cap `L`,
- no additional free/bonus entries that can appear outside the paid cap,

strict pre-draw guaranteed positive profit requires all of the following:

1. `x = 0` — no external valid entry can remain in the draw;
2. entrant can acquire every valid entry: `L >= N` (or no personal limit);
3. purchase is effectively atomic / sellout closes entry before a competing entry can be accepted;
4. prize is guaranteed to be awarded and is not reduced for undersell;
5. `V > N*c + fees + taxes + execution costs`;
6. eligibility/claim rules are satisfied and organizer cancellation/substitution clauses do not introduce a loss branch.

If **any already-sold external entry exists**, there is a legal draw outcome in which that external ticket wins, so buying only the remaining tickets cannot be a strict guarantee.

If `V <= N*c`, even a perfect zero-race full takeover is non-profitable before fees.

## Current market screen
Fresh web searches screened capped UK skill-based competition operators/pages that publish maximum entries, price, and cash alternative. The sample is not claimed exhaustive; it is a high-value falsification screen for the buy-all mechanism.

Derived table: `data/derived/h019_capped_competition_screen.csv`.

Observed full-cap cash-value / ticket-revenue ratios in the screened examples were all below 1.0, approximately **28.6%–53.3%**. Therefore even the impossible best case of owning every ticket from launch would lose money on the fixed cash alternative before fees.

Examples:
- Coast Competitions Nintendo Switch + Pokémon: 300 × £1.99 = £597 cap revenue vs £280 cash alternative => **46.90%**. Historical page shows only 148/300 sold at draw, proving guaranteed-draw-underfill occurs, but buying all 300 would still have been negative.
- Hot Comps Target Omni/Scolia: 179 × £5 = £895 vs £400 cash alternative => **44.69%**; page also imposes max 35 entries/person.
- Hot Comps LEGO SpongeBob: 189 × £2 = £378 vs £150 => **39.68%**; max 19/person.
- 7days Audi RS3: 299,999 × £0.25 = £74,999.75 vs £40,000 => **53.33%**, strongest ratio in this sample but still deeply negative; max 4,000/person and external entries existed.
- 7days Lamborghini Huracan: 599,999 × £0.35 = £209,999.65 vs £100,000 => **47.62%**; max 2,900/person.
- Urban Draw Rolex Submariner: 900 × £35 = £31,500 vs £9,000 => **28.57%**; max 75/person.
- UKCC Defender 90: 499,999 × £0.19 = £94,999.81 vs £35,000 => **36.84%**; max 7,900/person.

Several operators also expose a **free postal entry route**. This creates an additional external-entry channel unless sellout/closure rules make it impossible for a postal entry to enter after a complete paid takeover. It therefore weakens, rather than helps, a strict guarantee proof.

## Important near-miss structure
This class is not mathematically impossible in principle. A genuine terminal opportunity would exist if a live competition simultaneously had:
- zero external entries at the instant of execution;
- no personal cap below `N`;
- an atomic way to acquire all `N` entries and trigger immediate closure;
- no unresolved free-entry race;
- guaranteed fixed cash prize `V > N*c + all costs`.

That is a crisp monitorable condition. Current screened products fail primarily on **promoter margin (`V < N*c`)**, with personal caps/free routes adding further blockers.

## Sources checked (fresh/current or recently indexed)
- Coast Competitions Nintendo Switch + Pokémon historical guaranteed draw; £280 cash alternative; 300 × £1.99; 148/300 sold at draw.
- Coast current GTA VI and Pokémon pages: capped entry pools, guaranteed draw/no extension, unlimited entries unless stated; current examples have no cash alternative.
- Hot Comps current category/product pages: guaranteed end, published entry caps/prices/cash alternatives, per-person caps, free postal entry route.
- 7days Performance indexed 2026 draws: published price, cap, cash alternative, per-person limits, free postal route, guaranteed draw regardless of sellout.
- Urban Draw indexed 2026 competitions: low absolute ticket counts but explicit per-person caps and cash alternatives.
- UKCC indexed 2026 Defender draw: fixed cap/price/cash alternative and per-person cap.

## Conclusion
**H019 is NOT SUCCESS.** The buy-all-entries mechanism is real in principle but no screened executable instance satisfies the necessary economics or exclusivity conditions. Current examples fail before subtle execution risk because the fixed cash alternative is materially below full ticket-cap revenue; most also impose entrant caps or free-entry channels.

Future work should not re-screen ordinary examples blindly. Re-open H019 only when a live page satisfies the numerical trigger `cash floor > maximum paid-entry revenue` or when a deterministic subsidy/coupon makes effective acquisition cost cross below the guaranteed prize floor.
