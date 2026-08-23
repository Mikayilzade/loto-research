# STATUS

Updated: 2026-08-23
Branch: `research-work`
Scope: **LOTTERY ONLY**. Earlier H050-H107 non-lottery automation drift is historical only and must not drive NEXT ACTION.

## Terminal state
**NO SUCCESS; NOT EXHAUSTED**.

- `SUCCESS` = strictly proven lawful guaranteed positive net profit from a lottery/lottery-adjacent mechanism under explicit executable conditions after all costs, taxes, sharing, limits and outcome branches.
- `EXHAUSTED` = all defensible registered lottery-specific edge classes tested/closed without SUCCESS.

## Authoritative current checkpoint
Latest completed lottery packet: **H224 — bulk-vectorized exact H175 restricted-family screen**.

### H224 result
H223's exact result file was still absent at H224 start, so no restricted-family closure claim was available.

H224 identifies and removes the shared computational bottleneck in H219/H222/H223: the legacy `merged_active_rows()` path rebuilds the exact cut bank one affine witness at a time through many small NumPy calls. H224 instead expands the same mathematically valid witness set once, computes all four 128-layer support-incidence blocks in batches of 256 witnesses, concatenates the exact 512-column rows, deduplicates them exactly, asserts recovery of the known 4,878 unique cut rows, and then screens all `36 * 3,992 = 143,712` H212-normalized candidates with the unchanged exact predicate.

The output includes phase timings so any remaining bottleneck can be diagnosed directly. Target: `data/derived/h224_bulk_vectorized_survivors.json`. At this checkpoint that result is pending; missing output remains inconclusive.

Files:
- `src/loto_research/h224_bulk_vectorized_full_screen.py`
- `.github/workflows/h224-bulk-vectorized-screen.yml`
- `research/h224_bulk_vectorized_exact_h175_screen.md`
- `research/CHECKED_PROJECTS_AND_TESTS_H224_APPEND.md`

### Preserved H221 certificate theorem
A schema-valid exact full screen with `survivor_count=0` over all 143,712 H212-normalized classes is itself a finite impossibility certificate for the entire H212-covered restricted diagonal family. No second master MILP is required.

### Preserved H175 mathematical state
The unresolved H175 4,336-play doubled RI 3-spot hybrid still requires universal `n3>=3` on every balanced `4+4+4+4+4` draw.

- H185: 297 stored exact witnesses; 4,878 active unique valid rows after safe affine-orbit expansion.
- H186: 189 additional explicit exact counterexamples across two rejected candidates.
- H188: globally safe normalized representative count `12,289,536`.
- H210: residual translation quotient `768,096` classes.
- H211: combined translation/stabilizer count `767,361`.
- H212: affine-unit quotient `143,712` classes.
- H214: exact joint H212+H191 quotient `143,523` classes.
- H219/H222/H223: exact full-screen implementations; authoritative result files absent through H224 start.
- H221: zero-survivor finite-certificate theorem.
- H224: bulk-vectorized row reconstruction + exact full screen launched; result pending.
- No universal construction or unrestricted-family impossibility proof exists yet.

### Preserved promotion/execution state
- Current RI `Kick Back with Keno Promotion` is officially visible, but exact current mechanics remain unrecovered; do not repeat H209's exhausted searches without new evidence.
- Historical Lucky 3 Spot proves a genuine printed pre-draw 2x entitlement can exist, but doubled tickets were explicitly non-cancellable.
- Current RI online/iLottery and ordinary retailer/SSVM remain closed as sole strict-guarantee execution channels under recovered public rules.

## Preserved lottery conclusions
- Cash WinFall: genuine historical rolldown +EV, not a current strict guarantee.
- Fixed raffle/scratch/sealed-pack standard takeovers materially closed; residual raffle takeover theorem exists but tested boards fail strict floor.
- Azerbaijan `4+4` ordinary/realistic guarantee routes materially closed except rare exceptional states/rule changes/external subsidy; TezLoto bias route needs reliable bulk history.
- Several Keno/Pick conditional overlays can reach/exceed 100% only in favorable modifier states; random modifier assignment, execution atomicity, liability limits or insufficient prelocked subsidy block terminal guarantee.
- H173 conditional 4,560-play doubled RI 3-spot cover remains mathematically valid.
- H175 4,336-play hybrid remains open pending universal `n3>=3` construction/impossibility.

## Azerbaijan live branches
- `4+4`: rare exceptional carryover states / materially better primary rules only.
- `TezLoto`: bulk-history RNG/bias testing only upon reliable data recovery.
- `Poz-Qazan`: remaining-prize conditional edge data-blocked by missing exact live unsold denominator/registration state.
- `Beşdə 5`, `Super Keno`, `ONLOTO`: ordinary/full-space screens negative.

## NEXT ACTION
1. **Check `data/derived/h224_bulk_vectorized_survivors.json` first; also accept late schema-valid H223/H222/H219 exact full-screen results.**
2. If any exact full screen returns `survivor_count=0`, validate schema/counts and close the H212 restricted diagonal family immediately under H221; then expand to general cyclic-affine `z=a*x+b*y+c (mod16)` while reusing accumulated witnesses.
3. If survivors remain, run exact `n3<=2` separation only on those survivors; timeout never validates a design.
4. If H224 fails operationally, use its phase diagnostics or concrete workflow evidence before changing implementation again; do not blindly restart older screens.
5. Reopen current `Kick Back with Keno` only on materially new primary evidence.
6. Continue until lottery-specific `SUCCESS` or `EXHAUSTED`.

## Audit trail
Master ledger: `research/CHECKED_PROJECTS_AND_TESTS.md`. Connector-safe Hxxx append packets are authoritative additions where direct replacement of the large legacy ledger is impractical.
Latest lottery append: `research/CHECKED_PROJECTS_AND_TESTS_H224_APPEND.md`.
Latest case: `research/h224_bulk_vectorized_exact_h175_screen.md`.
