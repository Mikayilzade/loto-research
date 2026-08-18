# H082 — Soviet relay passport/value arbitrage

Updated: 2026-08-18
Status: **PROMISING CLASS / NOT SUCCESS**

## Why this branch
H080/H081 Schneider contactors are execution-gated by unknown original silver-tip gram mass. Soviet relays provide a cleaner pre-acquisition valuation route because many high-value models are identified by **relay type + passport + production date**, with published precious-metal content tables derived from technical/catalog documentation.

This can remove the hidden-mass problem: if the exact marking is visible before purchase and a buyer accepts that exact model/passport at a locked payout, the trade can become deterministic without destructive assay.

## Evidence recovered
### Precious-metal content references
A current relay-buying/reference source lists, among others:
- RES-7: 0.8 g PLI-10 per relay;
- RES-8 passports 050/051/052 through 12/1971: 0.55 g PLI-10;
- RES-9 passports 201/202/208: 0.165 g PLI-10.
PLI-10 is identified as 90% platinum / 10% iridium.

Independent relay-reference material confirms that relay passport/year is essential and that visually similar relay types can differ materially in precious-metal content.

### Local Baku buyer route
A current Baku radio-electronic scrap buyer page explicitly lists precious-metal price indications and radio-component acceptance. Indexed indications used for sensitivity screening:
- platinum: 68 AZN/g;
- palladium: 60 AZN/g;
- silver: 2.13 AZN/g;
- iridium: 255 AZN/g.
The same network explicitly lists RES-8 / RES-9 / RPS-36 among platinum-bearing relay examples and radio components are accepted by quote.

Another active Baku listing advertises collection of Soviet-era radio components/equipment and magnetic starters, confirming local physical execution infrastructure, but it is not a binding model-specific payout schedule.

## Theoretical local metal-value screen
Using only the indexed Baku metal indications as a sensitivity anchor, not as a guaranteed buyer payout:

- RES-7: `0.72 g Pt * 68 + 0.08 g Ir * 255 = 69.36 AZN` theoretical contained-metal quote basis.
- RES-8 050/051/052 <=12/1971: `0.495 g Pt * 68 + 0.055 g Ir * 255 = 47.685 AZN`.
- RES-9 201/202/208: `0.1485 g Pt * 68 + 0.0165 g Ir * 255 = 14.3055 AZN`.
- REN-33 silver-only reference example: `5.07 g Ag * 2.13 = 10.7991 AZN`.

See `data/derived/h082_soviet_relay_value_screen.csv`.

These are **not executable payout values**. A recycler may discount for recovery yield, assay, alloy handling, minimum lot size, or simply quote per relay rather than by contained spot value.

## Execution theorem / strict gate
A relay trade can qualify for project SUCCESS only if all of the following are locked before seller payment:
1. exact relay model, passport and production date are visible and authentic;
2. buyer/refiner confirms the exact accepted classification;
3. buyer gives a binding immediate-cash payout for that exact unit or lot, or a contractually fixed formula with no destructive-surprise branch;
4. payout exceeds seller ask + transport + assay/preparation + tax/fees by a strictly positive amount;
5. seller payment happens only after the buyer-side eligibility/payout gate is locked;
6. no prohibited cross-border movement or precious-metal handling is required.

If a buyer requires destructive assay after irreversible purchase, the branch is not a strict guarantee unless seller payment is contingent on the assay result.

## Marketplace search result
Fresh indexed Azerbaijan searches did **not** recover an active listing explicitly marked RES-7/RES-8/RES-9 with readable passport/year and a fixed ask. Broad local marketplaces do show Soviet equipment/components and local buyers, so inventory exists, but the exact profitable unit is not currently index-visible.

Therefore the current strongest reopening event is **not more generic content research**. It is an exact live relay/lot listing with readable passport/year, paired with a Baku buyer quote before payment.

## Strategic conclusion
H082 improves on H081 because the hidden contact-mass variable can be replaced by a passport/year lookup for qualifying relays. The theoretical margins are large enough to justify continuing this class: for example, even a deeply discounted fraction of the ~47.7 AZN RES-8 reference value could leave room for a low-ask local purchase.

But no exact live seller ask + locked buyer payout pair has been established. Therefore:

**H082 = PROMISING / NOT SUCCESS.**

## Sources used in this packet
- `https://www.radiodetaliplus.ru/radiodragmet2.php` — relay precious-metal content table / PLI-10 identification.
- `https://drm64.ru/rele/` — passport/year identification importance.
- `https://scraptraffic.com/baku/radioelektronnyi-lom` — current Baku indexed precious-metal/radio-scrap quote indications.
- `https://scraptraffic.com/baku/platina` — Baku platinum-bearing relay acceptance examples.
- current Tap.Az `Radiotexnikaların utilizasiya xidməti` listing — local Soviet radio-component pickup route.

## Next move
Search only for exact local or Azerbaijan-accessible lots where the relay body marking is visible. Highest-value models from this first screen: RES-7 and qualifying early RES-8. For each candidate, reject immediately if passport/year is absent; otherwise obtain/locate model-specific buyer payout before considering acquisition.
