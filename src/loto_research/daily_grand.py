from __future__ import annotations

from math import comb


def daily_grand_full_space_counts() -> dict[int, int]:
    """Counts of 5-number selections with exactly m matches to a fixed 5/49 draw."""
    return {m: comb(5, m) * comb(44, 5 - m) for m in range(6)}


def daily_grand_full_space_screen(
    *,
    stake: float = 3.0,
    value_free_play_at_face: bool = True,
    respect_top_pool_caps: bool = True,
) -> dict[str, float]:
    """Deterministic full-space screen for Canada's DAILY GRAND.

    Buy every 5/49 main-number selection paired with every Grand Number 1..7.
    For each main selection exactly one of seven lines matches the Grand Number
    and six miss it. Published current prizes are used.

    Top categories are liability pools: if `respect_top_pool_caps` is True,
    the single 5+GN line receives at most CAD 7m and our six 5-only lines share
    at most CAD 500k in total, assuming no external winners. This is already
    player-favorable; external winners can only reduce these categories.

    A Grand-Number-only prize is a Free Play, not withdrawable cash. It may be
    valued at CAD 3 face for a deliberately generous upper bound, or at zero
    for the strict immediate-cash guarantee floor.
    """
    counts = daily_grand_full_space_counts()
    main_selections = comb(49, 5)
    variants = main_selections * 7
    cost = variants * stake

    # Published fixed/advertised prize table.
    with_gn = {5: 7_000_000.0, 4: 1_000.0, 3: 100.0, 2: 10.0, 1: 4.0}
    without_gn = {5: 500_000.0, 4: 500.0, 3: 20.0, 2: 0.0, 1: 0.0}

    gross = 0.0
    # Lower tiers: one GN-hit line and six GN-miss lines per main selection.
    for m in (4, 3, 2, 1):
        gross += counts[m] * with_gn[m]
        gross += counts[m] * 6 * without_gn[m]

    if respect_top_pool_caps:
        # Our full-space portfolio creates one top-prize line and six second-
        # prize lines. With no external winners, those six split the 500k pool.
        gross += 7_000_000.0 + 500_000.0
    else:
        # Deliberately impossible-overgenerous bound: pay each of six second
        # prize lines the full headline 500k.
        gross += 7_000_000.0 + 6 * 500_000.0

    free_play_count = counts[0]
    free_play_face = free_play_count * stake
    if value_free_play_at_face:
        gross += free_play_face

    return {
        "main_selections": float(main_selections),
        "variants": float(variants),
        "cost": cost,
        "gross": gross,
        "roi": gross / cost,
        "net": gross - cost,
        "free_play_count": float(free_play_count),
        "free_play_face": free_play_face,
    }
