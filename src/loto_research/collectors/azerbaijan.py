"""Normalization and validation for Azerbaijan lottery draw ingestion.

The official archive pages are client-rendered and the underlying historical
API endpoint has not yet been documented in this project.  This module keeps
network discovery separate from data correctness: any future official API,
HTML adapter, saved payload, or secondary reconciliation source must pass
through the same strict normalizer before a draw enters normalized storage.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, Mapping, Optional, Sequence, Tuple


@dataclass(frozen=True)
class GameSpec:
    game_id: str
    board_a_pool: int
    board_a_draw_count: int
    board_b_pool: Optional[int] = None
    board_b_draw_count: Optional[int] = None
    official_archive_url: str = ""


@dataclass(frozen=True)
class DrawRecord:
    game_id: str
    draw_number: str
    draw_datetime: datetime
    numbers_a: Tuple[int, ...]
    numbers_b: Tuple[int, ...] = ()
    source_url: str = ""
    source_kind: str = "unknown"


AZ_GAME_SPECS: Mapping[str, GameSpec] = {
    "az_besde5": GameSpec(
        game_id="az_besde5",
        board_a_pool=36,
        board_a_draw_count=5,
        official_archive_url="https://www.azerlotereya.com/neticeler/besde5",
    ),
    "az_4plus4": GameSpec(
        game_id="az_4plus4",
        board_a_pool=20,
        board_a_draw_count=4,
        board_b_pool=20,
        board_b_draw_count=4,
        official_archive_url="https://www.azerlotereya.com/neticeler/4-4",
    ),
    "az_superkeno": GameSpec(
        game_id="az_superkeno",
        board_a_pool=70,
        board_a_draw_count=20,
        official_archive_url="https://www.azerlotereya.com/neticeler/super-keno",
    ),
}


def _normalize_board(
    values: Iterable[int],
    *,
    pool_size: int,
    draw_count: int,
    board_name: str,
) -> Tuple[int, ...]:
    numbers = tuple(int(value) for value in values)

    if len(numbers) != draw_count:
        raise ValueError(
            f"{board_name} must contain exactly {draw_count} numbers; "
            f"got {len(numbers)}"
        )
    if len(set(numbers)) != len(numbers):
        raise ValueError(f"{board_name} contains duplicate numbers")
    if any(number < 1 or number > pool_size for number in numbers):
        raise ValueError(
            f"{board_name} numbers must be in inclusive range 1..{pool_size}"
        )

    # Canonical storage order is ascending.  Draw order, if economically or
    # mechanically meaningful for another game, should be stored separately.
    return tuple(sorted(numbers))


def normalize_draw(
    game_id: str,
    draw_number: str | int,
    draw_datetime: datetime,
    numbers_a: Sequence[int],
    numbers_b: Sequence[int] = (),
    *,
    source_url: str = "",
    source_kind: str = "unknown",
) -> DrawRecord:
    """Validate and canonicalize one Azerbaijan draw record.

    This function intentionally does not fetch remote data.  A source adapter
    must first extract raw values, then pass them here.  That prevents source-
    specific quirks from silently changing the normalized research dataset.
    """

    if game_id not in AZ_GAME_SPECS:
        raise ValueError(f"unknown Azerbaijan game_id: {game_id}")
    if not isinstance(draw_datetime, datetime):
        raise TypeError("draw_datetime must be a datetime")

    spec = AZ_GAME_SPECS[game_id]
    normalized_a = _normalize_board(
        numbers_a,
        pool_size=spec.board_a_pool,
        draw_count=spec.board_a_draw_count,
        board_name="board A",
    )

    if spec.board_b_pool is None:
        if numbers_b:
            raise ValueError(f"{game_id} does not use board B")
        normalized_b: Tuple[int, ...] = ()
    else:
        if spec.board_b_draw_count is None:
            raise RuntimeError("invalid GameSpec: board B count missing")
        normalized_b = _normalize_board(
            numbers_b,
            pool_size=spec.board_b_pool,
            draw_count=spec.board_b_draw_count,
            board_name="board B",
        )

    draw_number_text = str(draw_number).strip()
    if not draw_number_text:
        raise ValueError("draw_number cannot be empty")

    return DrawRecord(
        game_id=game_id,
        draw_number=draw_number_text,
        draw_datetime=draw_datetime,
        numbers_a=normalized_a,
        numbers_b=normalized_b,
        source_url=source_url,
        source_kind=source_kind,
    )
