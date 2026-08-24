"""H262: exact arithmetic for LOTTO 6/49 terminal Gold Ball takeover screen."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h262_lotto649_gold_ball_takeover.json"

START_JACKPOT = 10_000_000
WHITE_BALLS = 29
STEP = 2_000_000
PLAY_COST = 3
WHITE_PRIZE = 1_000_000


def main() -> None:
    terminal_jackpot = START_JACKPOT + WHITE_BALLS * STEP
    strict_terminal_max_paid_plays = (terminal_jackpot - 1) // PLAY_COST
    strict_white_max_paid_plays = (WHITE_PRIZE - 1) // PLAY_COST
    out = {
        "packet": "H262",
        "game": "LOTTO 6/49 Gold Ball Draw",
        "currency": "CAD",
        "start_jackpot": START_JACKPOT,
        "white_balls": WHITE_BALLS,
        "jackpot_increment_per_white": STEP,
        "terminal_gold_only_jackpot": terminal_jackpot,
        "play_cost": PLAY_COST,
        "strict_positive_gold_only_max_paid_plays_terminal": strict_terminal_max_paid_plays,
        "white_ball_prize": WHITE_PRIZE,
        "strict_positive_gold_only_max_paid_plays_white_state": strict_white_max_paid_plays,
        "takeover_condition": "player owns every Gold Ball Draw selection issued for the target draw",
        "execution_status": "blocked",
        "blocker": "published mechanics provide computer-generated identifiers in an open all-issued-selection pool, including Free Plays; no finite reservable issuance monopoly established",
        "success": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
