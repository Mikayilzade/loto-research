# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H205 — RI Registered Ticketless Play execution bound**.

### H205 major result
H205 used the current Rhode Island Lottery Rules dated February 20, 2026 plus the current official Keno/app interfaces to tighten the H173/H175 execution gate.

Current rules now explicitly establish:
- Keno may be played via **Registered Ticketless Play**;
- one Keno play selects 1–10 spots from 1–80;
- wager per draw is $1/$2/$5/$10;
- the wager may run for up to 15 consecutive draws;
- maximum price per Keno Ticket or Registered Ticketless Play is $150 base, $300 with Plus or Overtime, $450 with both;
- Keno draws occur every four minutes.

This closes the old shortcut that `$150 maximum` itself implies capacity for 150 different $1 same-draw selections. The monetary caps are fully explainable by `$10 × 15 consecutive draws` and optional equal-cost add-ons. Consecutive draws repeat a selection over future draws and therefore do not reduce the number of distinct selections required in one H173/H175 target draw.

The current public Keno purchase UI remains single-selection shaped: Pick Numbers/Quick Pick -> Amount per game -> Consecutive games -> Plus/Overtime -> Buy Now, with no exposed add-line, quantity-of-different-lines, or bulk-import control in the public page text.

At the same time, current official app materials establish a real Keno-compatible electronic architecture: Keno is offered online, favorite draw-game wagers can be saved/replayed, and digital play slips can be scanned at retailers. This strengthens H204 but still does not publish the number of independently selected Keno lines one QR/digital play slip/scan can carry.

Conditional rate if each distinct selection needs its own completed purchase inside one 240-second draw interval:
- H175 4,336 plays: **18.0667 purchases/s**;
- H173 4,560 plays: **19 purchases/s**.

These are conditional lower bounds only; a proven multi-selection batch mechanism could reduce them.

Files:
- `research/h205_ri_registered_ticketless_play_execution_bound.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H205_APPEND.md`

### Preserved H204 result
The RI Lottery App can make wager selections and generate a QR code for retail purchase at a terminal or SSVM. This proves a pre-purchase selection-transfer channel, but Keno per-QR/per-scan multi-selection capacity remains unproved.

### Preserved H203-H199 execution result
Official Group Play does not prove Keno bulk acquisition. Single-player multi-device/multi-account parallelization is closed. The `$150` Keno cap does not prove 150 distinct same-draw selections. Draw-game cart/replay/QR infrastructure exists, but discretionary limits/rejection and missing Keno batch capacity block guaranteed acquisition.

### Preserved H202 result
`Kick Back with Keno Promotion` is currently live/active, but the homepage `Get a free ticket when you buy 2` teaser resolves to Mega Millions and cannot be attributed to Keno. Exact current Keno promo mechanics remain unresolved.

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
- H205 formally validates current electronic Keno and saved digital wagers but leaves distinct-line batch capacity unresolved.

## NEXT ACTION
1. **Highest priority: recover explicit Keno multi-selection/panel capacity for one RI digital play slip / QR / Registered Ticketless transaction from official app help, screenshots, retailer/vendor terminal or SSVM documentation.**
2. Search vendor/terminal manuals or procurement documents for Keno line counts, QR payload capacity, same-draw transaction batching and processing rate.
3. If finite capacity is recovered, compute exact minimum QR scans, terminals and lawful participants required for H175 (4,336) and H173 (4,560), including cutoff and rejection branches.
4. Continue recovery of exact `Kick Back with Keno Promotion` rules through genuinely new primary-source assets/retailer notices.
5. Resume H191/H188 exact pruning with existing balanced cuts; solver-certified infeasibility closes restricted diagonal family, timeout never does.
6. If diagonal family closes, expand to general cyclic-affine `z=a*x+b*y+c (mod16)` and reuse accumulated witnesses.
7. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H205_APPEND.md`.
Latest case: `research/h205_ri_registered_ticketless_play_execution_bound.md`.
