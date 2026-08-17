# H065 — Azerbaijan fixed-cash agricultural/state bounties

Updated: 2026-08-17
Status: **strong conditional cash mechanisms found; no current standalone guaranteed-profit path proven**

## Goal
Search objective/formulaic Azerbaijan state payments where the state cash amount is not merely a percentage reimbursement of an incurred cost, and test whether any can create a strictly positive cash floor after all required incremental costs.

## 1. 2026 fallow-land subsidy — strongest new lead
The Ministry of Agriculture / Agricultural Subsidy Council states that in **2026, for the first time**, rain-fed land in **Shamakhi, Sheki, Gobustan and Yardimli** can receive a fallow-land subsidy when the parcel had been continuously planted and declared in EKTIS during the previous 3 years with wheat or barley.

Published amount:
- wheat history: **220 AZN/ha**;
- barley history: **220 AZN/ha**.

Primary source:
- Ministry of Agriculture, 2026 subsidy-coefficient decision: https://www.agro.gov.az/index.php/az/news/010920254

### Why this is structurally different
Unlike ordinary crop-production support, this payment is attached to **leaving qualifying land fallow**, so it does not require producing/selling output in the subsidized year.

Current Ministry guidance for planting-subsidy transfers states that Farmer Card amounts are generally usable **25% in cash and 75% non-cash** for approved agricultural inputs. The 2026 autumn-payment release repeats the same 25/75 split.

Primary sources:
- https://www.agro.gov.az/az/news/170220261
- https://www.agro.gov.az/az/news/subsidiyalarin-merheleli-sekilde-fermer-kartlarina-koecueruelmesine-baslanilib

If the same standard split applies to the new fallow subsidy, the mechanical per-hectare decomposition is:

- total subsidy: **220 AZN/ha**;
- cashable 25%: **55 AZN/ha**;
- restricted agricultural-use 75%: **165 AZN/ha**.

This is the first screened local mechanism where a qualifying owner/operator can potentially receive positive cash **without current-year production expenditure**.

### Terminal-gate problems
This is **not yet SUCCESS** for four reasons:

1. **Current-entry timing.** Ministry communications about the 2026 campaign state that nationwide autumn declarations ended **30 December 2025**. The fallow subsidy was explained to farmers during that same campaign. As of 17 August 2026, no authoritative public route was found showing that a new applicant can still create a 2026 fallow declaration now.
2. **Cash split not fallow-specific in the public source.** The 25/75 split is documented for planting-subsidy Farmer Card payments generally, but the searched public material does not explicitly spell out the split for the first-year fallow category. Treat 55 AZN/ha cash as a strong inference, not a final contractual fact.
3. **Eligibility/monitoring is factual, not self-certified.** EKTIS history, land documents and monitoring must be accepted. Current Ministry material confirms subsidy declarations and land data are checked and monitored before payment.
4. **Opportunity cost.** For a farmer who would otherwise profitably plant the parcel, foregone crop margin can exceed 220 AZN/ha. A positive standalone floor only exists for an already-qualifying parcel that would independently be left fallow and has zero/hard-bounded incremental compliance cost.

### Conditional theorem
For already-controlled qualifying land with independent decision to leave it fallow, let:
- `S = 220 AZN/ha` subsidy;
- `c` = all incremental cash cost of obtaining/maintaining eligibility for the subsidy;
- `q` = cashable fraction actually applicable to fallow support.

Cash-only floor is:

`cash_net = q*S - c`.

Under the ordinary Farmer Card split `q=0.25`:

`cash_net = 55 - c` AZN/ha.

Therefore this becomes a true positive-cash guarantee **only if** authoritative rules confirm the 25% cash right for fallow support, application/eligibility is already irrevocably satisfied, and `c < 55 AZN/ha` with no foregone economic activity counted as an incremental loss.

Current status: **PROMISING CONDITIONAL LEAD; not currently executable/proven enough for SUCCESS**.

## 2. 100 AZN per healthy calf from artificial insemination
Official Ministry material states that owners receive **100 AZN for each healthy calf born from artificial insemination**, with EKTIS records and post-birth verification. Current Ministry reporting confirms thousands of applications/payments under the mechanism.

Primary sources:
- https://www.agro.gov.az/az/news/sueni-mayalanma-ile-dogulmus-25-370-bas-buzova-goere-fermerlere-subsidiya-oedenilecek
- https://www.agro.gov.az/az/news/fermerler-heyvandarliq-sahesinde-de-subsidiyalari-ektis-sis-vasitesile-alacaqlar

### Guarantee test
The bounty is fixed cash after successful birth, but entry requires artificial insemination and a **healthy calf outcome**. Conception, gestation and live/healthy birth are biological outcome branches; the subsidy is not paid before those uncertainties resolve.

Thus no pre-commitment guaranteed-profit floor exists from initiating insemination solely to capture the subsidy.

Status: **FIXED CASH BOUNTY VALIDATED; standalone guarantee REJECTED by biological outcome risk**.

## 3. 2026 per-ton crop-product subsidies
The 2026 Agricultural Subsidy Council schedule includes objective per-ton payments for delivered qualifying production, including examples such as:
- cotton: **200–215 AZN/t** depending on irrigation/region rules;
- tobacco: **20–36 AZN/t** for specified wet categories;
- sugar beet: **18–19 AZN/t**;
- soy: **100–120 AZN/t**;
- corn: **50 AZN/t**;
- sunflower: **50 AZN/t**;
- wheat: **100 AZN/t**;
- pomegranate: **75 AZN/t**;
- apple: **50 AZN/t**.

Primary source:
- Ministry of Agriculture 2026 coefficient decision: https://www.agro.gov.az/index.php/az/news/010920254

The Ministry also states that product-subsidy claims require delivery/sale records to the purchaser and EKTIS confirmation.

### Guarantee test
These are formulaic incremental revenues **on already-produced and delivered output**, not standalone bounties. Production volume, buyer acceptance and production cost are uncontrolled branches if activity is initiated solely to obtain the subsidy.

Status: **VALIDATED deterministic add-on to independently economic sales; standalone guarantee REJECTED**.

## 4. High per-hectare orchard/planting payments
The 2026 table contains large fixed per-hectare planting subsidies in some intensive horticulture categories, including amounts in the thousands or tens of thousands of AZN/ha.

However each high payment is tied to costly physical requirements such as minimum hectare area, certified planting density, trellis/drip irrigation, altitude/soil conditions, insurance and dated establishment windows.

These remain cost subsidies/investment incentives until acquisition + installation + maintenance + compliance + opportunity cost can be hard-bounded below the subsidy. No such zero-cost loop was found.

Status: **NOT terminal; real investment obligation dominates guarantee test**.

## H065 class result
Three distinct fixed/formulaic payment classes are now separated:

1. **Fallow payment:** unusually strong because current-year output is not required; potentially `55 AZN/ha` cashable under the standard Farmer Card split, but current-entry timing and fallow-specific cash-rule confirmation are missing.
2. **Per-event livestock bounty:** fixed cash only after a biological success event; no pre-event guarantee.
3. **Per-unit production bounty:** deterministic only after independently produced/sold output exists; not standalone.

No H065 route currently proves a strictly positive standalone cash floor for a new entrant on 17 August 2026.

## Next implication
The fallow mechanism should remain a high-priority **conditional** lead only if a new authoritative route can resolve both:
- whether 25% of the 220 AZN/ha fallow subsidy is legally cashable; and
- whether a presently eligible farmer can still lock entitlement for 2026, or whether an equivalent 2027 program opens.

Otherwise move to other fixed state bounties where qualification is based on an already-existing state rather than creating a costly new activity.
