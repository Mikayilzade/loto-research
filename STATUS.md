# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H200 — RI Keno cart execution and operator-limit gate**.

### H200 major result
H200 revises the Rhode Island Keno execution model using current official iLottery and retailer materials.

New positive execution evidence:
- official FAQ explicitly refers to **cart purchases** for draw games;
- a live Shopping Cart / Checkout exists;
- at least one current draw-game flow (`The Numbers`) exposes `QTY` and `Add to cart`;
- the app supports saved Favorite wagers / replay;
- digital play slips can generate QR wager selections that retailers can scan at a terminal or self-service vending machine.

Therefore H195's former conservative lower bound that H175 necessarily needs ~4,336 fully independent `Buy Now` actions is **withdrawn**. The platform has real batching/replay/QR infrastructure.

However current official online terms also state that the Lottery may limit purchases of any game, ticket, wager, or particular set of numbers **at any time and without notice**, and disclaim losses from delay in or denial of purchase processing. Lottery-set account purchase limits also exist.

Strict-guarantee consequence:
- cart existence does not certify acquisition of all **4,336** H175 or **4,560** H173 same-draw selections;
- Keno-specific cart capacity remains unrecovered;
- Keno-specific QTY semantics remain unrecovered;
- atomic all-or-none acceptance of a huge cart is unproven;
- before the entire basket is confirmed accepted for the target draw, operator purchase-limit/processing branches remain legal failure states.

Files:
- `research/h200_ri_keno_cart_execution_and_operator_limit_gate.md`
- `data/derived/h200_ri_keno_cart_execution_gate.json`
- `research/CHECKED_PROJECTS_AND_TESTS_H200_APPEND.md`

### Preserved H199 result
The `$150` maximum Keno Ticket / Registered Ticketless Play price does **not** imply 150 distinct same-draw selections. Current rules explain it exactly as `$10 × 15 consecutive draws`, so H193's old `4,336/$150 ≈ 29 tickets` inference remains rejected.

### Preserved H198-H196 result
Current `Kick Back with Keno Promotion` is officially listed as live/current in August 2026, but exact public mechanics remain unresolved. Historical Lucky 3 Spot rules prove pre-draw 2x entitlement and multi-game-ticket applicability, not present bulk distinct-selection capacity. Current 50% first-deposit match is capped at $50; even an optimistic deterministic buy-2-get-1-free alone cannot rescue H173 ordinary economics without another nonlinear multiplier/subsidy.

### Preserved H175/H191 mathematical state
The unresolved H175 4,336-play doubled 3-spot hybrid still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

- H185: 297 stored exact witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit exact counterexamples across two rejected candidates; timeout/no-incumbent remained inconclusive.
- H188: globally safe normalized representative count **12,289,536**.
- H189 full-S3 quotient was withdrawn by H190 as globally unsafe.
- H191 exact stabilizer classification safely reduces to **12,277,776** representatives only (~0.096% saving), materially exhausting further coordinate-symmetry quotienting.
- No universal construction or restricted-family impossibility proof exists yet.

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not a current strict guarantee.
- Fixed raffle/scratch/sealed-pack standard takeovers materially closed; residual raffle takeover theorem exists but tested boards fail strict floor.
- Azerbaijan `4+4` ordinary/realistic guarantee routes materially closed except rare exceptional states/rule changes/external subsidy; TezLoto bias route needs reliable bulk history.
- Several Keno/Pick conditional overlays can reach/exceed 100% only in favorable modifier states; random modifier assignment, execution atomicity, liability limits or insufficient prelocked subsidy block terminal guarantee.
- H173 conditional 4,560-play doubled RI 3-spot cover remains mathematically valid.
- H175 4,336-play hybrid remains open pending universal `n3>=3` construction/impossibility.
- Michigan current pre-draw multiplier architecture exists but random ticket tagging prevents strict ex-ante guarantee.
- Historical RI Lucky 3 Spot shows genuine pre-draw 2x printed entitlement.
- H199 closes the `$150 maximum => 150 distinct same-draw selections` shortcut.
- H200 proves real draw-game cart/replay/QR infrastructure, but current discretionary purchase-limit and processing-denial terms block treating it as guaranteed H173/H175 acquisition.

## NEXT ACTION
1. **Highest live priority: recover Keno-specific cart/QTY capacity and atomic checkout behavior.** Inspect current Keno web/app purchase payloads, saved-favorite replay behavior, cart composition, and any authoritative limit docs. Distinguish technical batching capacity from guaranteed acceptance.
2. Recover exact official mechanics for active `Kick Back with Keno Promotion`; determine dates, deterministic/random award, eligible wager/spot types, retailer vs iLottery, caps, cancellation/disqualification and whether any entitlement is known before the draw.
3. Search retailer-terminal training/manual material for QR/digital-slip capacity, replay/batch functions and whether one scan can encode multiple independently specified Keno selections for the same draw.
4. Resume H191/H188 exact pruning in parallel using existing balanced cuts; solver-certified infeasibility closes restricted diagonal family, timeout never does.
5. If diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` and reuse accumulated witnesses.
6. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H200_APPEND.md`.
Latest case: `research/h200_ri_keno_cart_execution_and_operator_limit_gate.md`.
