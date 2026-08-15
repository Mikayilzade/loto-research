# Powerball US — progressive jackpot threshold and guarantee bounds

Updated: 2026-08-15
Status: **sharing/tax sensitivity implemented; single-ticket +EV requires much larger cash jackpots; full-space terminal guarantee remains unproven and practically dominated by sharing/execution**

## Current primary sources checked 2026-08-15
Powerball official:
- https://www.powerball.com/
- https://www.powerball.com/faqs
- https://www.powerball.com/draw-result?date=2026-07-29&gc=powerball
- https://www.powerball.com/powerball-jackpot-climbs-to-600-million-largest-prize-of-2026

IRS official:
- https://www.irs.gov/instructions/iw2g
- https://www.irs.gov/taxtopics/tc419
- https://www.irs.gov/publications/p515

Current official facts used:
- base Powerball play costs **$2**;
- matrix remains 5 white balls from 69 plus 1 Powerball from 26;
- jackpot is pari-mutuel when multiple jackpot-winning tickets exist;
- UK sales began July 21, 2026, increasing participation without changing odds/drawing mechanics;
- advertised annuity and cash values are before federal/jurisdictional taxes;
- official July 29, 2026 result page reports an estimated **$668m advertised / $292.5m cash** jackpot and no jackpot winner;
- IRS instructions state 24% regular withholding on qualifying lottery proceeds; nonresident-alien US-source gambling winnings are generally subject to 30% withholding absent an applicable exemption/treaty. These are withholding rules, **not universal final effective-tax rates**.

## 1. Exact baseline
Combination space:

`M = C(69,5) * 26 = 292,201,338`.

Existing exact fixed lower-tier EV outside California:

`EV_lower ≈ $0.31987825 per $2 play`.

Required jackpot EV contribution:

`gap = 2 - 0.31987825 = $1.68012175`.

With no tax, no sharing and no execution cost:

`J0 = gap * M ≈ $490,933,823.35 cash`.

This is the absolute optimistic cash break-even floor.

## 2. Jackpot-sharing model
If there are `n` other independently distributed lines and our chosen exact combination has popularity multiplier `a` relative to uniform, then conditional on our line winning:

`q = a/M`

`X ~ Binomial(n,q)` = number of other jackpot-winning tickets.

Expected retained jackpot fraction:

`S(n,a) = E[1/(1+X)]`

`= [1-(1-q)^(n+1)] / ((n+1)q)`.

Therefore the single-ticket break-even cash jackpot under a generic retained-jackpot fraction `r` is:

`J_required = gap * M / (S(n,a) * r)`.

`r` is intentionally generic. It may represent tax/withholding/other jackpot haircut in sensitivity analysis; it must not be interpreted as a universal final tax rate.

Implementation:
- `src/loto_research/powerball_threshold.py`
- `tests/test_powerball_threshold.py`
- `data/derived/h002_powerball_sharing_threshold_curve.csv`

## 3. Sharing + haircut sensitivity
Uniform-combination (`a=1`) examples:

| other lines | expected retained jackpot share | required cash, no tax | with 24% jackpot haircut | with 30% jackpot haircut |
|---:|---:|---:|---:|---:|
| 0 | 100.00% | $490.9m | $646.0m | $701.3m |
| 10m | 98.31% | $499.4m | $657.1m | $713.4m |
| 25m | 95.84% | $512.2m | $674.0m | $731.8m |
| 50m | 91.91% | $534.1m | $702.8m | $763.0m |
| 100m | 84.68% | $579.7m | $762.8m | $828.2m |
| 200m | 72.41% | $678.0m | $892.1m | $968.5m |
| 300m | 62.51% | $785.3m | $1.033bn | $1.122bn |
| 500m | 47.88% | $1.025bn | $1.349bn | $1.465bn |

These haircut columns are deliberately optimistic in one respect: they haircut only the jackpot component while leaving the previously computed lower-tier EV untouched. Actual tax treatment can be more complicated, so they are scenario bounds rather than executable net-EV claims.

### Consequence
The original ~$490.9m threshold is too optimistic for large-jackpot states because the same jackpot growth attracts more tickets and therefore more expected sharing. UK participation since July 21, 2026 adds another demand source to the common jackpot pool.

The official July 29 state ($292.5m cash) was below even the absolute no-sharing/no-tax floor, so it was conclusively negative under this model.

## 4. Anti-popularity interaction
H015 can reduce `a` below 1 for an unpopular exact combination, raising expected retained share. This is economically useful but does not remove the base losing outcomes of a single ticket.

For H002 it should be treated as a threshold reducer, not a terminal guarantee mechanism. A real claim requires jurisdiction-specific crowd calibration; generic `a<1` is only sensitivity analysis.

## 5. Full-space / buy-the-pot identity
Buying all `M=292,201,338` base combinations once costs:

`C_full = 2*M = $584,402,676`.

Because every combination is covered exactly once and lower-tier payouts are fixed, deterministic non-jackpot gross equals:

`G_lower_full = EV_lower * M ≈ $93,468,852.65`.

Therefore the cash jackpot needed merely to break even in an impossible ideal of:
- zero tax;
- zero execution cost;
- no external jackpot winner;

is exactly:

`C_full - G_lower_full ≈ $490,933,823.35`.

This equality is useful: the optimistic single-ticket EV threshold and ideal full-space break-even threshold are the same linear identity.

## 6. Why full-space does NOT yet create a guarantee
Full coverage guarantees that **we own one jackpot-winning line**, but it does not guarantee that we own the jackpot alone.

If there are `k` external jackpot-winning tickets, our jackpot share is at most `1/(k+1)`. With a hard pre-draw upper bound `K` on external jackpot winners, a sufficient no-tax cash-jackpot condition would be:

`J > $490,933,823.35 * (K+1)`.

Examples:
- `K=0`: >$490.9m;
- `K=1`: >$981.9m;
- `K=2`: >$1.473bn;
- `K=10`: >$5.400bn.

But Powerball rules do not give us a useful pre-draw cap on duplicate external winning tickets. A strict all-outcome guarantee therefore cannot assume `K=0` or a small value merely because duplicates are unlikely.

Under a worst-case guarantee standard, external buyers could concentrate many tickets on whichever combination later happens to win. Without a defensible pre-draw bound on exact-combination duplication, **jackpot sharing prevents a strict terminal full-space guarantee theorem**.

Tax and execution only worsen this bound.

## 7. Execution reality
Even before printing/payment/retailer limits are quantified, full-space acquisition requires **292,201,338 plays** and at least **$584.4m gross ticket spend** at the $2 price. This is not currently an executable candidate for the project's terminal SUCCESS standard.

Detailed execution-rate/retailer/network limits belong to H012b only if economics ever survive first-pass bounds.

## 8. Current conclusion
### H002 single-ticket progressive state
- Positive EV remains possible **in principle** at sufficiently extreme cash jackpots.
- Real break-even can move from ~$491m to well above ~$1bn cash when high participation and jackpot haircuts are combined.
- No current executable +EV state has been validated in this packet.

### H012 Powerball full-space guarantee
- Ideal no-sharing break-even identity established.
- **Strict guarantee not validated** because jackpot sharing is outcome-dependent and no useful pre-draw cap on external duplicate winners is guaranteed.
- Acquisition scale is enormous even before operational constraints.

## Next H002 step
Use observed draw-level winner counts / sales proxies to estimate realistic `n(J)` demand response and produce a historically anchored cash-jackpot threshold band. Then repeat the same framework for current Mega Millions ($5 format) and EuroMillions.
