# H173 — Rhode Island doubled 3-spot Keno reduced block cover

Updated: 2026-08-22
Status: **REDUCED STRICT PRE-TAX COVER FOUND CONDITIONAL ON PRE-LOCKED 2X / CURRENT PROMO + EXECUTION STILL UNPROVEN / NOT SUCCESS**

## Purpose
H172 showed that Rhode Island has an official historical/recurring promotion architecture in which a qualifying 3-spot Keno ticket is marked at purchase and every eligible win on that ticket is doubled. Under the screened standard 80/20 3-spot paytable ($25 for match 3, $2.50 for match 2 on a $1 wager), buying all C(80,3)=82,160 triples would return 138.7537% if every ticket is pre-locked for a free 2x. That naive full-space portfolio is too large for a four-minute draw interval.

H173 solves a smaller deterministic portfolio analytically.

## Source facts carried from H172
Official Rhode Island 2025 Lucky 3 Spot rules establish that:
- only 3-spot Keno tickets bought at the specified location/time qualify;
- qualifying winning Keno prize(s) are doubled;
- qualifying entitlement is printed on the ticket at purchase;
- multiple eligible Keno games on a qualifying ticket may all be doubled;
- advance pre-printing is prohibited;
- qualifying doubled Keno tickets cannot be cancelled.

Official rules example:
- https://www.rilot.com/content/dam/interactive/ilottery/pdfs/Promotions/2025/LaunchAlertRules-Lucky3SpotKenoBingoDoubler.pdf

Official 2026 Keno rules establish:
- 20 numbers are drawn from 80;
- $1/$2/$5/$10 wagers;
- up to 15 consecutive draws;
- ordinary Keno ticket price cap $150;
- draws every 4 minutes.

Primary rules:
- https://www.rilot.com/content/dam/interactive/ilottery/pdfs/about-us/RILotteryRules_2026.pdf

The live 2026 homepage still advertises a `Kick Back with Keno Promotion`, but its exact current rules were not recovered in H172/H173, so no current 2x entitlement is assumed.

Current homepage:
- https://www.rilot.com/

## Conditional paytable
As in H172, this packet uses the standard 80/20 3-spot paytable as a conditional screen because the current RI dynamic prize table is not exposed in crawler text:
- match 3: $25 per $1;
- match 2: $2.50 per $1.

Under a free deterministic 2x promotion the corresponding payouts become:
- match 3: $50;
- match 2: $5.

This numerical table remains **secondary-source screened, not current-primary-verified for RI**.

## Construction: four disjoint 20-number groups
Partition the 80 Keno numbers into four disjoint groups `G1,G2,G3,G4`, each of size 20.

Buy every 3-number subset inside each group, and no cross-group triples.

Number of $1 plays:

`4 * C(20,3) = 4 * 1,140 = 4,560`.

So external stake is **$4,560**.

Let the actual 20-number Keno draw contain `s_i` numbers from group `Gi`. Then:

`s_1+s_2+s_3+s_4 = 20`, with `0 <= s_i <= 20`.

For group `Gi`:
- selected triples matching all 3 draw numbers: `C(s_i,3)`;
- selected triples matching exactly 2: `C(s_i,2)*(20-s_i)`.

Under a guaranteed free 2x the portfolio payout for draw-composition `(s_1,...,s_4)` is

`P(s) = sum_i [50*C(s_i,3) + 5*C(s_i,2)*(20-s_i)]`.

Algebra simplifies each group contribution:

`50*C(s,3)+5*C(s,2)*(20-s) = (5/6)*s*(s-1)*(7s+40)`.

The discrete function is convex over integer `s >= 0`; with a fixed sum of 20, the total is minimized when the draw is distributed as evenly as possible among the four equal groups. Here equality is exact:

`(s_1,s_2,s_3,s_4)=(5,5,5,5)`.

At `s=5` per group:
- match-3 triples per group: `C(5,3)=10`;
- match-2 triples per group: `C(5,2)*15=150`;
- doubled payout per group: `10*$50 + 150*$5 = $1,250`.

Across four groups:

**worst-case gross payout = 4*$1,250 = $5,000.**

Therefore conditional strict pre-tax floor:

- spend = **$4,560**;
- minimum gross = **$5,000**;
- minimum surplus = **+$440**;
- strict gross ratio = **109.6491%**;
- strict pre-tax ROI = **+9.6491%**.

This is not an expected-value statement. Under the assumed free, pre-locked 2x and fixed paytable, every possible 20-of-80 Keno draw is covered above cost.

## Reduction versus naive full cover
H172 naive all-triples portfolio:
- 82,160 plays.

H173 partition portfolio:
- 4,560 plays.

Reduction:

`1 - 4560/82160 = 94.450%</approximately`.

At the official $150 ordinary-ticket monetary cap, the theoretical lower bound on ticket-equivalents falls from:
- `ceil(82,160/150)=548` to
- `ceil(4,560/150)=31`.

Important: this is only a **monetary-cap lower bound**. It does not prove that 150 distinct 3-spot selections can be packed onto one physical/terminal ticket or that 31 terminal submissions can actually be completed for the same draw.

## Nearby equal-partition controls
For equal groups of size `g` dividing 80, using all triples within every group, exact worst-case screens are:

| group size | groups | plays | worst doubled gross | floor ratio |
|---:|---:|---:|---:|---:|
| 10 | 8 | 960 | 780 | 81.2500% |
| 16 | 5 | 2,800 | 2,800 | 100.0000% |
| **20** | **4** | **4,560** | **5,000** | **109.6491%** |
| 40 | 2 | 19,760 | 25,500 | 129.0486% |
| 80 | 1 | 82,160 | 114,000 | 138.7537% |

Thus `5 x 16` is an exact break-even structural boundary for this family, while `4 x 20` is the first simple equal partition tested that yields a positive strict floor and remains dramatically smaller than full coverage.

A search over unequal 4-group partitions near this region found `(20,20,20,20)` to be the lowest-play positive member among the tested clique-partition family; nearby unequal examples consume more plays while retaining the same $5,000 minimum gross.

## Why this is still NOT SUCCESS
### Gate 1 — current 2026 promotion mechanic unresolved
The live Rhode Island homepage advertises `Kick Back with Keno Promotion`, but H173 still could not recover official 2026 rules proving it is a free deterministic 2x on every qualifying 3-spot ticket. Historical Lucky 3 Spot rules prove the architecture exists, not that it is active now.

### Gate 2 — current RI 3-spot prize table not primary recovered
The `$25/$2.50` table is a standard 80/20 Keno table and matches the conditional H172 screen, but current Rhode Island primary dynamic prize data remain unresolved. Terminal SUCCESS cannot rely on a secondary paytable.

### Gate 3 — same-draw execution is not guaranteed
The 4,560 distinct plays must all apply to the same Keno draw for the theorem above. With draws every four minutes and historical promotion rules prohibiting advance pre-printing, execution still needs an official mechanism that can submit all required selections for one target draw.

The $150 ticket cap alone only gives a best-case lower bound of 31 ticket-equivalents. The public rules do not establish how many distinct 3-spot selections can be encoded per physical terminal action, nor an atomic/bulk portfolio upload.

### Gate 4 — promotion discretion / validation
Historical Lucky 3 Spot terms reserve broad discretion to modify/suspend/postpone/cancel the promotion and make tickets subject to validation. This must be included in any final execution theorem.

### Gate 5 — tax
The +$440 conditional pre-tax margin must remain positive after applicable wagering-tax treatment and any execution costs. No universal after-tax theorem is claimed here.

## Result
- **A strict reduced deterministic cover exists:** 4,560 plays instead of 82,160.
- **Conditional free-2x worst-case gross = 109.6491%, +$440 pre-tax.**
- **94.45% reduction in wager count relative to naive full space.**
- **Current executable SUCCESS: NO** because current 2026 2x terms/paytable and same-draw bulk acceptance are not proved.

## Next research
1. Recover exact current `Kick Back with Keno` rules and current primary RI 3-spot paytable.
2. Recover physical/terminal ticket encoding limits: number of distinct Keno games/selections per transaction and whether a target future draw can be specified.
3. Search structured designs smaller than 4,560 plays (balanced block/cyclic designs) that preserve `min_draw payout > cost` under the doubled 3-spot table.
4. Search other current pre-locked free doublers on smaller state spaces, where exact cover is operationally trivial.
