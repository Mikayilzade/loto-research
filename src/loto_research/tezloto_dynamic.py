from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Optional


@dataclass(frozen=True)
class StateOdds:
    position: int
    next1: Optional[float]
    next2: Optional[float]
    next6_1: Optional[float]
    next6_2: Optional[float]
    next6_3: Optional[float]

    @property
    def remaining(self) -> int:
        # Before the j-th drawn ball there are 49-j balls still available.
        return 49 - self.position


PUBLISHED = [
    StateOdds(1,37,880,6.20,58,670), StateOdds(2,36,840,6.10,56,630),
    StateOdds(3,35,800,6.00,53,590), StateOdds(4,35,770,5.85,51,550),
    StateOdds(5,34,730,5.70,49,510), StateOdds(6,33,700,5.60,47,480),
    StateOdds(7,32,670,5.45,44,440), StateOdds(8,32,640,5.30,42,410),
    StateOdds(9,31,600,5.20,40,380), StateOdds(10,30,570,5.05,38,350),
    StateOdds(11,29,540,4.90,36,330), StateOdds(12,28,520,4.80,34,300),
    StateOdds(13,28,490,4.65,32,275), StateOdds(14,27,460,4.55,31,255),
    StateOdds(15,26,430,4.40,29,230), StateOdds(16,25,410,4.25,27,210),
    StateOdds(17,24,380,4.15,25,190), StateOdds(18,24,360,4.00,24,175),
    StateOdds(19,23,340,3.90,22,155), StateOdds(20,22,315,3.75,21,140),
    StateOdds(21,21,295,3.60,19.5,125), StateOdds(22,21,270,3.50,18,110),
    StateOdds(23,20,250,3.35,16.5,100), StateOdds(24,19,230,3.25,15.5,89),
    StateOdds(25,18,215,3.10,14,78), StateOdds(26,17,195,2.95,13,69),
    StateOdds(27,17,180,2.85,12,60), StateOdds(28,16,160,2.70,10.5,51),
    StateOdds(29,15,145,2.60,9.5,44), StateOdds(30,14,130,2.45,8.5,37),
    StateOdds(31,14,115,None,None,None), StateOdds(32,13,105,None,None,None),
    StateOdds(33,12,90,None,None,None), StateOdds(34,11,80,None,None,None),
    StateOdds(35,10,None,None,None,None),
]


def fair_odds(state: StateOdds) -> dict[str, float]:
    n = state.remaining
    return {
        "next1": float(n),
        "next2": float(comb(n, 2)),
        "next6_1": n / 6.0,
        "next6_2": comb(n, 2) / comb(6, 2),
        "next6_3": comb(n, 3) / comb(6, 3),
    }


def screen() -> list[dict[str, float | int | str]]:
    out = []
    for state in PUBLISHED:
        fair = fair_odds(state)
        for bet_type in ("next1", "next2", "next6_1", "next6_2", "next6_3"):
            offered = getattr(state, bet_type)
            if offered is None:
                continue
            f = fair[bet_type]
            out.append({
                "position": state.position,
                "remaining": state.remaining,
                "bet_type": bet_type,
                "published_odds": float(offered),
                "fair_odds": f,
                "gross_return_ratio": float(offered) / f,
            })
    return out


def best_cell() -> dict[str, float | int | str]:
    return max(screen(), key=lambda row: row["gross_return_ratio"])


if __name__ == "__main__":
    rows = screen()
    best = best_cell()
    print(f"cells={len(rows)}")
    print(best)
    assert len(rows) == 159
    assert best["gross_return_ratio"] < 1.0
