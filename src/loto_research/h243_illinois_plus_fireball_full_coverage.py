from dataclasses import dataclass, asdict
import json


@dataclass
class Game:
    name: str
    digits: int
    base_line_cost: float
    fireball_line_cost: float
    base_straight_prize: float
    fireball_straight_prize: float


def evaluate(game: Game):
    lines = 10 ** game.digits
    total_cost = lines * (game.base_line_cost + game.fireball_line_cost)
    # Player-favorable upper bound: one base exact winner plus one full
    # FIREBALL straight award for every digit position.
    gross_upper_bound = game.base_straight_prize + game.digits * game.fireball_straight_prize
    return {
        **asdict(game),
        "full_straight_lines": lines,
        "full_coverage_cost": total_cost,
        "gross_upper_bound": gross_upper_bound,
        "return_upper_bound": gross_upper_bound / total_cost,
        "net_upper_bound": gross_upper_bound - total_cost,
        "guaranteed_profit_possible": gross_upper_bound > total_cost,
    }


def main():
    games = [
        Game("Illinois Pick 3 plus FIREBALL", 3, 1.0, 1.0, 500.0, 250.0),
        Game("Illinois Pick 4 plus FIREBALL", 4, 1.0, 1.0, 5000.0, 2000.0),
    ]
    output = {
        "packet": "H243",
        "date": "2026-08-24",
        "method": "full Straight coverage, player-favorable all-position FIREBALL prize upper bound",
        "results": [evaluate(g) for g in games],
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
