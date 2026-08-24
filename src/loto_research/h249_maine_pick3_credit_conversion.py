"""H249: exact promotional-credit gate for Maine Pick 3 Single Digit cover.

Lottery-only research helper. No network calls.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Cover:
    selections: int = 10
    wager_per_selection: float = 0.50
    guaranteed_winners: int = 1
    payout_per_winner: float = 2.50

    @property
    def face_cost(self) -> float:
        return self.selections * self.wager_per_selection

    @property
    def guaranteed_payout(self) -> float:
        return self.guaranteed_winners * self.payout_per_winner

    @property
    def base_return(self) -> float:
        return self.guaranteed_payout / self.face_cost


def guaranteed_net(credit: float, fee: float = 0.0, acquisition_cost: float = 0.0) -> float:
    """Strict net assuming credit deterministically offsets ticket face cost dollar-for-dollar."""
    cover = Cover()
    cash_face_cost = max(0.0, cover.face_cost - credit)
    return cover.guaranteed_payout - cash_face_cost - fee - acquisition_cost


def strict_credit_threshold(fee: float = 0.0, acquisition_cost: float = 0.0) -> float:
    """For credits no larger than the $5 face cost, strict profit requires B > this value."""
    return 2.50 + fee + acquisition_cost


def build_result() -> dict:
    c = Cover()
    scenarios = []
    for credit in (0.0, 2.0, 2.5, 3.0, 5.0, 10.0):
        scenarios.append(
            {
                "credit": credit,
                "fee": 0.0,
                "acquisition_cost": 0.0,
                "guaranteed_net": guaranteed_net(credit),
            }
        )

    fee_sensitivity = []
    for fee in (0.0, 0.50, 1.00, 2.00, 2.49, 2.50):
        fee_sensitivity.append(
            {
                "credit": 5.0,
                "fee": fee,
                "acquisition_cost": 0.0,
                "guaranteed_net": guaranteed_net(5.0, fee=fee),
            }
        )

    return {
        "packet": "H249",
        "game": "Maine Pick 3 Single Digit",
        "cover": {
            **asdict(c),
            "face_cost": c.face_cost,
            "guaranteed_payout": c.guaranteed_payout,
            "base_return": c.base_return,
            "base_net": c.guaranteed_payout - c.face_cost,
        },
        "theorem": {
            "guaranteed_net": "P - max(0, C-B) - F - A",
            "for_0_le_B_le_5": "G = B - 2.50 - F - A",
            "strict_credit_threshold": "B > 2.50 + F + A",
            "for_B_ge_5": "G = 2.50 - F - A",
        },
        "zero_fee_scenarios": scenarios,
        "five_dollar_credit_fee_sensitivity": fee_sensitivity,
        "terminal_status": "NOT_SUCCESS",
        "blocking_gates": [
            "no current public Maine-eligible deterministic credit above threshold proven on 2026-08-24",
            "Maine Jackpocket Single Digit wager UI support unproven",
            "exact Maine Jackpocket service fee unresolved",
            "promotion terms retain discretionary cancellation/abuse determination",
        ],
    }


def main() -> None:
    result = build_result()
    out = Path("data/derived/h249_maine_pick3_credit_conversion.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
