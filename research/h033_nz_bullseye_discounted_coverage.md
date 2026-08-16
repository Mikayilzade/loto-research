# H033 — New Zealand Bullseye discounted multi-draw full coverage

Updated: 2026-08-16
Status: **REJECTED as a strict guaranteed-cash-profit strategy; unusual deterministic discount validated and retained as an EV overlay lead**

## Why this candidate was worth testing
Bullseye is a compact finite game with exactly 1,000,000 possible six-digit selections (`000000` through `999999`) and an unusually large deterministic multi-draw discount written into the current rules.

Current official New Zealand legislation (latest consolidated Bullseye Rules 2009 as at 29 September 2025) states:
- a normal selection costs NZ$2;
- the same selection entered for 7 consecutive games costs NZ$10 instead of NZ$14;
- 14 consecutive games cost NZ$20 instead of NZ$28.

Thus both discounted packages reduce acquisition cost by exactly **2/7 = 28.5714%**.

Primary official source:
- https://legislation.govt.nz/secondary-legislation/pco-drafted/2009/258/en/latest/

## Exact full-space geometry
The six-digit number line is circular. If every one of the 1,000,000 selections is owned exactly once, then for every draw the portfolio deterministically contains:
- Division 1 exact match: **1** selection;
- Division 2 distance 1–5: **10** selections;
- Division 3 distance 6–50: **90** selections;
- Division 4 distance 51–500: **900** selections;
- Division 5 distance 501–5000: **9,000** selections;
- Division 6 distance 5001–50000: **90,000** selections.

The remaining 899,999 selections receive no prize in that draw.

For 7 consecutive fully covered draws, acquisition cost is **NZ$10,000,000** rather than NZ$14,000,000.
For 14 consecutive fully covered draws, acquisition cost is **NZ$20,000,000** rather than NZ$28,000,000.

Data:
- `data/derived/h033_nz_bullseye_full_space.csv`

Code/tests:
- `src/loto_research/nz_bullseye.py`
- `tests/test_nz_bullseye.py`

## Prize mechanics that matter
Official rules provide:
- the prize pool is determined by the Commission and must be at least 55% of turnover;
- up to 15% of ticket sales may be set aside into the prize reserve fund;
- Divisions 1, 3, 4 and 5 are shared equally between all winning selections in the division;
- Division 2 pays NZ$10,000 per winning selection, but total Division-2 allocation is capped at NZ$250,000 and is shared if necessary;
- Division 6 is paid as a bonus ticket rather than guaranteed withdrawable cash;
- Division 1 jackpots if not won, subject to the threshold/maximum-game rules, and can be reallocated when those rules trigger.

Official sources:
- prize-pool rule 20: https://www.legislation.govt.nz/regulation/public/2009/0258/latest/DLM2322928.html
- divisions/allocation rule 21 and sharing rule 27: current consolidated rules above;
- Division-2 cap rule 25: current consolidated rules above.

## Strict guarantee test
A full-space portfolio guarantees that **we have** a winning selection in every cash division, but it does not guarantee that we are the only claimant.

For Divisions 1–5, outside players may hold duplicate winning selections. No useful pre-draw hard cap on the number of external duplicate winning selections was found in the rules. Therefore, for any finite cash pool, our fraction of the shared pool can be made arbitrarily small as the number of external duplicate winning selections increases.

Division 2 does not solve this: our 10 distance-1..5 selections share a maximum NZ$250,000 allocation with all other Division-2 winning selections.

Division 6 is a bonus ticket. Treating a bonus ticket as guaranteed terminal cash would be invalid because the replay itself can lose.

Therefore the current rules do not provide a strictly positive cash payout floor for the full-space owner that exceeds the NZ$10m / NZ$20m acquisition costs in every legal outcome.

### Necessary-condition proof
Let `P_i` be the finite cash pool for division `i` and `N_i` the number of external winning selections in that division. If our full-space portfolio contributes `m_i` winning selections, our cash share is bounded by approximately

`P_i * m_i / (m_i + N_i)`

for shared divisions. Without a useful hard upper bound on `N_i`, this tends to zero as `N_i` grows. A finite deterministic acquisition cost therefore cannot be dominated by a strictly positive cash floor derived from these shared divisions.

The 28.57% multi-draw discount materially improves EV, but **does not remove sharing risk and does not create terminal guaranteed profit**.

## Important incompatibility with Must-Be-Won / rollover capture
Full coverage itself guarantees a Division-1 winner on every covered draw. Consequently, once full coverage begins, it prevents ordinary no-winner rollover accumulation during the covered sequence. Only a pre-existing jackpot on the first covered draw can be captured; subsequent covered draws cannot continue rolling through our own full-coverage period.

This is the same structural incompatibility seen in other buy-the-pot strategies: the act of guaranteeing the top-prize hit can destroy the state condition that would have created the largest subsidy.

## Conclusion
- deterministic multi-draw discount: **VALIDATED, unusually large (28.5714%)**;
- compact finite full-space geometry: **VALIDATED**;
- standalone strict guaranteed-cash-profit strategy: **REJECTED** because external duplicate winners can dilute all cash divisions and Division 6 is replay value rather than terminal cash;
- strategic value retained: **EV overlay / candidate for conditional states only**, not terminal SUCCESS.
