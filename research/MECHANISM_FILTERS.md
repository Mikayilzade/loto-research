# Reusable Mechanism Filters

Updated: 2026-08-29
Purpose: reject structurally impossible guaranteed-profit candidates cheaply, before a new H packet or expensive exact enumeration.

These are **filters and blockers**, not universal theorems, except where an cited packet contains an exact proof for its stated model. Passing a filter is necessary, never sufficient. All costs, rules, eligibility and execution branches still require validation.

## Screening protocol
For a candidate, write down the proposed source of money, the controlled portfolio, every reachable cash outcome, external participation, the special-event trigger and acquisition contract. Apply F1-F10 in order. A single explicit legal below-cost witness closes a strict-guarantee claim. Use stronger-than-real player-favourable assumptions when they permit a cheap closure.

## F1 — Base payout or average-return ceiling is below cost

**Plain statement.** If a complete controlled outcome set returns less than its acquisition cost even after granting favourable ownership of all relevant fixed/variable receipts, rearranging selections cannot make every outcome profitable. For symmetric full covers, the average payout is also an upper bound on the minimum payout.

**Cheap rejection.** Compute the full issue prize budget / minimum takeover cost or the exact full-cover payout before optimizing portfolios. Reject when the strongest relevant upper bound is below 100%.

**Examples.** H354 Spanish Lotería Nacional has a hard 70% entire-issue return. H347 Thunderball's advertised fixed full-cover return is 52.8815%. H355 EuroDreams remains about 52.0007% even under a player-favourable Boost allocation. H261 capped raffles peak at 52.6122%.

**What defeats it.** A binding external additive subsidy, discount or rollover reserve large enough to push the *minimum* controlled receipts above all-in cost; it must not merely reallocate the same below-cost wager-funded pool.

## F2 — External duplicates dilute a jackpot/top tier

**Plain statement.** Owning one winning selection does not guarantee owning the prize pool. If rules divide a capped top prize among all matching tickets and external matching tickets are unbounded, a legal duplicate count can reduce our share below cost.

**Cheap rejection.** Solve the first integer `d` for which `fixed_lower_receipts + top_pool/(own_winners+d) <= cost`. If `d` is legally possible and not bindingly capped below that value, strict guarantee fails.

**Examples.** H349 fails at three external Super Chance top duplicates. H351 fails at four external Megabucks duplicates even under a stronger-than-real jackpot. H353 NZ Strike fails with one external ordered-tuple copy. H258 EuroMillions cap flow-down and H268 NZ Powerball show the same shared-pool weakness.

**What defeats it.** A fixed payment per winning entry, exclusive/reservable winning identifiers, or a binding pre-draw external-duplicate cap strictly below the computed break-even count.

## F3 — The portfolio prevents the required no-winner/rolldown trigger

**Plain statement.** A strategy cannot rely on a `no top-tier winner` branch when its own coverage guarantees a top-tier winner in every draw. Full coverage can destroy the very event meant to fund the guarantee.

**Cheap rejection.** Ask whether any purchased line is a top-tier winner for each covered draw state. If yes, test the ordinary top-winner payout branch, not the no-winner rolldown fantasy.

**Examples.** H353 Strike cannot force its terminal no-D1 rolldown. H348 South Africa PowerBall XTRA full cover blocks the Jackpot Cascade. H268 NZ Powerball full coverage guarantees own D1 rather than no D1. H245 UK Lotto full coverage similarly prevents the relevant zero-winner branch.

**What defeats it.** A subsidy triggered regardless of whether our portfolio wins the top tier, or a mechanism in which complete ownership itself forces payment of the reserve.

## F4 — Caps or already-issued identifiers prevent full control

**Plain statement.** Finite identifiers help only if the player can own the entire winning support. Per-person caps, uncontrolled external issuance, already-sold tickets and free-play issuance preserve a legal external winner.

**Cheap rejection.** Compare the maximum binding allocation to the eligible universe and identify identifiers already or subsequently issuable to others. One reachable uncontrolled winning identifier is enough for a zero-receipt branch in a single-winner pool.

**Examples.** H262's terminal Gold Ball jackpot is arithmetically powerful, but open computer-generated and Free Play identifiers prevent monopoly. H341 free-phone promotions cap one entrant at 250/300 while paid external entries remain open. H257 LOTTO MAX has no hard external duplicate cap.

**What defeats it.** Exclusive player selection, atomic reservation of all remaining identifiers, a hard issuance stop with certified inventory, or a per-entry payment that does not require monopoly.

## F5 — A legal zero-cash outcome remains reachable

**Plain statement.** If a positive-cost portfolio can legally receive zero withdrawable cash, its guaranteed net profit is non-positive (and normally negative), regardless of attractive expected value.

**Cheap rejection.** Enumerate prize *classes*, not individual tickets. Include losing IDs, external-winner states and non-cash outcomes valued at zero withdrawable cash unless unconditional conversion is contractual.

**Examples.** H340's recovered instant pool had 900/1,000 zero-instant IDs. H341 leaves a legal external single winner and hence a £0 floor. H357 can allocate every Premium Bond prize outside the maximum holding, leaving principal but zero prize.

**What defeats it.** Every reachable controlled outcome binds the operator to positive withdrawable cash, or exhaustive control eliminates all zero-cash/external-winner states.

## F6 — Acquisition or acceptance is not binding/atomic

**Plain statement.** Positive arithmetic conditional on acceptance is not a guarantee if irreversible cost occurs first and rules allow loss, delay, rejection, sellout or reassignment.

**Cheap rejection.** Model dispatch-to-settlement, not accepted-ticket-to-prize. If a compliant attempt may consume postage/fees yet allocate no entry, use that branch as the floor.

**Examples.** H332's 184.824% all-cash takeover lacks atomic reservation and permits delayed reassignment/anti-exploit action. H334 has a positive minimum conditional on accepted postcards, but proof of posting does not guarantee entry. H345 likewise allows a mailed entry to be lost or arrive after the cap.

**What defeats it.** Binding zero-cost digital issuance, atomic paid reservation with enforceable acceptance, or a delivery/acceptance method whose full guaranteed cost remains below the minimum cash receipt.

## F7 — Reward is credit/free play/non-withdrawable value

**Plain statement.** Site credit, bonus balance, free play and non-cash prizes are not cash profit when withdrawal or unconditional cash election is absent.

**Cheap rejection.** Build a `minimum_withdrawable_cash` field. Value restricted credit and non-cash prizes at zero for the strict cash floor, even if their face value is positive.

**Examples.** H342 reconciles 100/100 winning IDs but all prizes are restricted site credit and the cash floor is £0. H340's pool contains 86 site-credit prize IDs. H344 includes physical Prize Grabber outcomes without a guaranteed cash alternative. H247 shows uncontrolled free Quick Picks have no deterministic marginal cash floor.

**What defeats it.** Contractual immediate withdrawal at par with no wagering/fee condition, or an unconditional winner-elected cash alternative whose minimum amount clears cost.

## F8 — Deterministic subsidy is real but too small

**Plain statement.** A promotion can be genuinely external and deterministic yet fail because its maximum contribution does not bridge the exact base-game deficit.

**Cheap rejection.** Compute `maximum guaranteed subsidy / exact required coverage cost` and compare it with `1 - base guaranteed return`, including the price of the add-on.

**Examples.** H260 grants an impossible-favourable C$1.5m across three DAILY GRAND bonus draws yet reaches only 68.675%. H350's complete Irish Lotto Plus Raffle code cycle returns at most 5%. H356's paid All Star Bonus preserves a 26.9009% fixed-return percentage and worsens the absolute jackpot hurdle.

**What defeats it.** A larger additive payment, cheaper deterministic coverage, or a free enhancement that crosses the computed threshold and survives every other filter.

## F9 — Channel, eligibility or timing blocks good arithmetic

**Plain statement.** A numerical edge is not executable if the qualifying route, location, account status, cutoff or rule version does not bind the operator for this player and this transaction.

**Cheap rejection.** Before modelling, verify governing terms (not banner copy), dates, jurisdiction, per-person rules, withdrawal terms and allocation timing. Separate an evidence-blocked lead from a mathematical rejection.

**Examples.** H340's footer mentioned phone entry while governing terms supplied only paid-online/free-postal routes. H342's apparent online presentation did not create a binding free online route. H249/H250 remain conditional on a current deterministic subsidy and fee/entitlement evidence.

**What defeats it.** Current specific terms that expressly grant the required route and eligibility, plus an execution record or binding process closing timing/acceptance branches.

## F10 — Principal preservation gives a zero, not positive, profit floor

**Plain statement.** Returning the stake is valuable but does not satisfy the project's terminal criterion. If all bonus/prize allocations can miss the player, minimum gross equals principal and minimum profit is exactly zero.

**Cheap rejection.** Separate principal redemption from incremental cash. Test whether the incremental component has a binding strictly positive per-holder minimum.

**Examples.** H357 Premium Bonds preserve and redeem £50,000 but allow zero prizes because millions of prizes can all be placed on external bonds. More favourable prize-fund rates change expectation, not the minimum.

**What defeats it.** Contractual positive interest/bonus above principal for every compliant holding, or monopolization of a finite prize support under the ownership cap.

## Combined decision rule
A candidate merits expensive exact work only if it has a named external source of value, no reachable zero-cash branch, no uncontrolled dilution, no self-defeating trigger, binding acquisition/control, and a fast player-favourable necessary bound above 100%. Otherwise record the cheap screen in search coverage without manufacturing a numbered packet.
