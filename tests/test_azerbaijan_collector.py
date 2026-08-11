import sys
import unittest
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from loto_research.collectors.azerbaijan import normalize_draw  # noqa: E402


class AzerbaijanCollectorTests(unittest.TestCase):
    def test_normalizes_four_plus_four_draw(self):
        draw = normalize_draw(
            "az_4plus4",
            796,
            datetime(2026, 7, 28, 19, 45),
            [20, 3, 13, 8],
            [18, 2, 16, 6],
            source_kind="official",
        )
        self.assertEqual(draw.draw_number, "796")
        self.assertEqual(draw.numbers_a, (3, 8, 13, 20))
        self.assertEqual(draw.numbers_b, (2, 6, 16, 18))

    def test_rejects_duplicate_numbers(self):
        with self.assertRaises(ValueError):
            normalize_draw(
                "az_besde5",
                1,
                datetime(2026, 1, 1, 19, 45),
                [1, 1, 2, 3, 4],
            )

    def test_rejects_out_of_range_number(self):
        with self.assertRaises(ValueError):
            normalize_draw(
                "az_4plus4",
                1,
                datetime(2026, 1, 1, 19, 45),
                [1, 2, 3, 21],
                [1, 2, 3, 4],
            )

    def test_rejects_wrong_draw_count(self):
        with self.assertRaises(ValueError):
            normalize_draw(
                "az_superkeno",
                1,
                datetime(2026, 1, 1, 19, 45),
                list(range(1, 20)),
            )

    def test_rejects_board_b_for_single_board_game(self):
        with self.assertRaises(ValueError):
            normalize_draw(
                "az_besde5",
                1,
                datetime(2026, 1, 1, 19, 45),
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4],
            )


if __name__ == "__main__":
    unittest.main()
