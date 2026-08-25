"""H270: ONCE 11/11 rollover-funding bound.

The 2026 rules allow up to EUR 11m of the already-stated category-1/2 prize
amounts to be funded from unsold prizes of prior draws. This script shows why
that mechanism is not an additive external subsidy.

For a historical 120-series issuance (the official 2024 and 2025 structure),
we also reproduce the published prize-schedule total of EUR 40.936m from the
category table. The lower-category computation is a collision-free upper
bound; repeated complete extractions can only reduce non-accumulable lower-tier
payout, so it is safe for rejecting a guaranteed-profit takeover.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h270_once_1111_rollover_funding_bound.json"

PRICE = 6
NUMBERS_PER_SERIES = 100_000
MAX_PRIOR_UNSOLD_FUNDING = 11_000_000


def schedule_upper_bound(series: int) -> dict:
    assert series > 0
    cost = PRICE * NUMBERS_PER_SERIES * series
    cat1 = 11_000_000
    cat2 = 11 * 1_000_000
    # Category 3/4 exclude the exact number+series winner in each extraction.
    cat3 = (series - 1) * 50_000
    cat4 = 11 * (series - 1) * 2_000
    cat5 = 9 * series * 1_200
    cat6 = 90 * series * 120
    cat7 = 900 * series * 12
    cat8 = 9_000 * series * 6
    gross_upper = sum((cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8))
    return {
        "series": series,
        "issued_coupons": series * NUMBERS_PER_SERIES,
        "acquisition_cost_eur": cost,
        "category_upper_eur": {
            "cat1": cat1,
            "cat2": cat2,
            "cat3": cat3,
            "cat4": cat4,
            "cat5": cat5,
            "cat6": cat6,
            "cat7": cat7,
            "cat8": cat8,
        },
        "scheduled_gross_upper_eur": gross_upper,
        "scheduled_gross_upper_return": gross_upper / cost,
        "current_emission_funding_if_full_11m_imported_eur": gross_upper - MAX_PRIOR_UNSOLD_FUNDING,
        "current_emission_funding_ratio_if_full_11m_imported": (gross_upper - MAX_PRIOR_UNSOLD_FUNDING) / cost,
        "additive_rollover_increment_eur": 0,
    }


def main() -> None:
    historical_120 = schedule_upper_bound(120)
    assert historical_120["acquisition_cost_eur"] == 72_000_000
    assert historical_120["scheduled_gross_upper_eur"] == 40_936_000
    # 2025 official certificate: 56.9% if top prizes are funded by current
    # issuance, about 41.6% if EUR 11m comes from prior unsold prizes.
    assert abs(historical_120["scheduled_gross_upper_return"] - 0.5685555555555556) < 1e-15
    assert abs(historical_120["current_emission_funding_ratio_if_full_11m_imported"] - 0.4157777777777778) < 1e-15
    result = {
        "packet": "H270",
        "mechanism": "ONCE 11/11 prior-unsold-prize funding",
        "rule_date": "2026-05-07",
        "draw_date": "2026-11-11",
        "sale_start": "2026-09-21",
        "price_per_coupon_eur": PRICE,
        "max_prior_unsold_funding_eur": MAX_PRIOR_UNSOLD_FUNDING,
        "key_result": "Prior unsold prize amounts may fund up to EUR 11m of the already-fixed category-1/2 awards; they do not increase the stated prizes.",
        "additive_external_subsidy_eur": 0,
        "historical_120_series_screen": historical_120,
        "status": "CLOSED for additive-rollover subsidy; no guaranteed-profit result",
        "notes": [
            "The 2026 rule fixes category 1 at EUR 11m and category 2 at eleven EUR 1m prizes before describing their funding source.",
            "Paragraph 3.4 says up to EUR 11m of those amounts may come from prior unsold prizes, so prior funds substitute for current-emission funding rather than add to player payout.",
            "The 120-series arithmetic is a historical calibration from official 2024/2025 issuance, not a claim that the 2026 Q4 series count has already been published.",
            "Lower-category repeated-extraction collisions can only make the non-accumulable payout lower than the collision-free schedule upper bound used here.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
