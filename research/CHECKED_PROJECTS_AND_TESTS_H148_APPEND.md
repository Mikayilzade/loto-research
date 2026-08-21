# H148 audit append — Omaha August 2026 $2 Monthly Special

Updated: 2026-08-21
Scope: LOTTERY ONLY

| Project / mechanism | Test variant | Result | Status / evidence |
|---|---|---|---|
| **H148 Big Red Keno Omaha August 2026 Monthly Special** | Recover current official numeric promo image, then buy every 3-Spot combination under advertised `$2` stake / `Hit 3 = $102` payout | `C(80,3)=82,160` selections; cost **$164,320**; exactly `C(20,3)=1,140` Hit-3 winners; gross **$116,280**; deterministic return **70.7644%**; deficit **$48,040** | **REJECTED standalone guarantee**; current special recovered and exact coverage closed; `research/h148_omaha_august_2026_3spot_special_full_cover.md` |
| **H148 generalized k-Spot special screen** | Full cover of all `C(80,k)` k-subsets where special stake is `s` and Hit-k payout is `P` | deterministic return `R_k=(P/s)*C(20,k)/C(80,k)`; standalone profit requires `P/s > C(80,k)/C(20,k)` | **VALIDATED fast-screen theorem**; for k=3 break-even multiplier **72.0702x**, so a $2 wager requires payout **>$144.14** |
| **H148 subsidy sensitivity** | Ask what deterministic pre-owned discount/free credit would be required to invert the Omaha special | required face-value subsidy **>29.2356%**, worse than 25% deficit of the existing 75% Pick-1 target | **INFERIOR TARGET**; prioritize Pick-1 >4.00x or other specials with higher exact `R_k` |

Primary/current source:
- Big Red Keno Omaha current page: https://bigredkeno.com/omaha
- Official August 1–31, 2026 promo image: https://bigredkeno.com/Content/Media/Image/Locations/omaha_monthly_keno_special.jpg

Derived data:
- `data/derived/h148_omaha_august_2026_3spot_cover.csv`
